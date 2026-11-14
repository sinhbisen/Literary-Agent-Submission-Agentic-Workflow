"""Offline demonstration of a *subset* of the two-agent control contract.

ALL data is synthetic. There are no browser, Gmail, Drive or network calls.
SENT denotes a local mock acknowledgement, not an actual submission.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

SIMULATED_AS_OF = date(2026, 11, 12)  # Fixed for reproducible historical fixtures.
FIT_VALUES = {"FIT-QUALIFIED", "FIT-NOT-QUALIFIED", "FIT-UNVERIFIED"}
READINESS_VALUES = {"SUBMISSION-READY", "SUBMISSION-NOT-READY", "SUBMISSION-UNVERIFIED"}


@dataclass
class Ledger:
    events: list[dict] = field(default_factory=list)
    outcomes: dict[str, str] = field(default_factory=dict)
    attempted: set[str] = field(default_factory=set)

    def record(self, candidate_id: str, state: str, detail: str) -> None:
        self.events.append({"candidate_id": candidate_id, "state": state, "detail": detail})
        self.outcomes[candidate_id] = state

    def warn_duplicate(self, candidate_id: str) -> None:
        """Never overwrite a confirmed result when the input repeats a candidate."""
        self.events.append({"candidate_id": candidate_id, "state": "DUPLICATE_SKIPPED",
                            "detail": "Candidate already processed; prior outcome retained"})


class SimulatedSender:
    """An in-memory local placeholder. Cannot transmit externally."""
    def __init__(self) -> None:
        self.actions = 0

    def send_once(self, candidate_id: str, package: list[str]) -> str:
        if not package:
            raise ValueError("Missing approved synthetic package")
        self.actions += 1
        return f"MOCK-ACK-{candidate_id}"


def days_since_source(candidate: dict, as_of: date) -> int | None:
    raw = candidate.get("source_checked_on")
    try:
        source_date = date.fromisoformat(raw)
    except (ValueError, TypeError):
        return None
    elapsed = (as_of - source_date).days
    return elapsed if elapsed >= 0 else None


def research_assessment(candidate: dict, as_of: date = SIMULATED_AS_OF) -> dict:
    """Report independent historical labels and current actionable eligibility.

    Important: a previous SENT overrides current *actionability*, but it does
    not erase the original fit/readiness classification.
    """
    fit = candidate.get("fit_qualification", "FIT-UNVERIFIED")
    preliminary = candidate.get("preliminary_submission_readiness", "SUBMISSION-UNVERIFIED")
    if fit not in FIT_VALUES or preliminary not in READINESS_VALUES:
        raise ValueError("Invalid research classification")
    age = days_since_source(candidate, as_of)
    stale = age is None or age > 30
    protected = candidate.get("prior_status") in {"SENT", "SEND UNCONFIRMED", "SENDING"}
    actionable = (fit == "FIT-QUALIFIED"
                  and preliminary == "SUBMISSION-READY"
                  and candidate.get("research_state") == "PREQUALIFIED"
                  and not stale and not protected)
    return {"fit": fit, "preliminary_readiness": preliminary,
            "evidence_age_days": age, "stale": stale,
            "currently_actionable_for_review": actionable}



RESEARCH_TARGET = 7
NET_NEW_RESEARCH_CAP = 15


def nearest_approved_asset(requested_words: int, category: str, required_format: str,
                           approved_assets: list[dict], range_upper: int | None = None) -> dict:
    """Choose an existing, same-category approved document; never create/alter text.

    This models the owner's *selection* exception, not agency acceptance of a
    hard cap, portal limit or mandatory truth declaration.
    """
    if requested_words <= 0 or (range_upper is not None and range_upper < requested_words):
        raise ValueError("Invalid word-count requirement")
    choices = [a for a in approved_assets if a.get("approved") is True
               and a.get("category") == category and a.get("format") == required_format
               and isinstance(a.get("words"), int) and a["words"] > 0]
    if not choices:
        raise ValueError("No approved asset of required category and format")

    def distance(asset: dict) -> int:
        words = asset["words"]
        if range_upper is not None:
            return max(requested_words - words, words - range_upper, 0)
        return abs(words - requested_words)

    return min(choices, key=lambda a: (distance(a), a["words"], a["key"]))


def rename_attachment_bytes(content: bytes, new_name: str) -> tuple[str, bytes]:
    """Simulate filename-metadata change without altering underlying bytes."""
    if not isinstance(content, bytes) or not content:
        raise ValueError("Missing approved binary content")
    if not new_name or "/" in new_name or "\\" in new_name:
        raise ValueError("Invalid requested attachment name")
    return new_name, content


def prospecting_pass(screened_candidates: list[dict], starting_actionable: int = 0,
                     target: int = RESEARCH_TARGET, net_new_cap: int = NET_NEW_RESEARCH_CAP) -> dict:
    """Offline *research* budget demo; never contacts agents or edits records.

    Each fixture denotes a substantively screened net-new candidate. Held and
    failed-source cases consume screening effort but cannot become actionable.
    """
    if min(starting_actionable, target, net_new_cap) < 0 or target <= 0 or net_new_cap <= 0:
        raise ValueError("Invalid research target or cap")
    actionable = starting_actionable
    screened = 0
    seen: set[str] = set()
    for c in screened_candidates:
        if actionable >= target or screened >= net_new_cap:
            break
        cid = c["id"]
        if cid in seen or not c.get("net_new", True):
            continue
        seen.add(cid)
        screened += 1
        # A candidate-level source issue, hold or mismatch does not stop the pass.
        if c.get("source_available", True) and c.get("actionable", False):
            actionable += 1
    if actionable >= target:
        reason = "ACTIONABLE_TARGET_REACHED"
    elif screened >= net_new_cap:
        reason = "NET_NEW_CAP_REACHED"
    else:
        # The synthetic input ended. A real agent needs to evidence this reason.
        reason = "CANDIDATE_SOURCE_EXHAUSTION_NEEDS_EVIDENCE"
    return {"net_new_screened": screened, "actionable_at_close": actionable,
            "target": target, "net_new_cap": net_new_cap, "stop_reason": reason}


def eligibility(candidate: dict, as_of: date = SIMULATED_AS_OF) -> str | None:
    """Synthetic Submission review. Explicitly ignores all source-page prose.

    A source page can contain actual agency requirements, but cannot grant
    permission or change an agent's role. This demo never evaluates or runs text.
    """
    if candidate.get("prior_status") in {"SENT", "SEND UNCONFIRMED", "SENDING"}:
        return "HOLD: protected historical attempt"
    x = research_assessment(candidate, as_of)
    if x["fit"] != "FIT-QUALIFIED":
        return "HOLD: literary fit not qualified"
    if x["preliminary_readiness"] != "SUBMISSION-READY":
        return "HOLD: preliminary research readiness not established"
    if candidate.get("research_state") != "PREQUALIFIED":
        return "HOLD: not prequalified"
    if x["stale"]:
        return "HOLD: official opening/route evidence stale or unavailable"
    if candidate["ai_policy"] == "strict_ai_free_content":
        if candidate["query_asset"] != "LOCKED_HUMAN_AUTHORED":
            return "HOLD: missing human-authored locked query"
        if candidate["greeting"] == "mandatory_body_name":
            return "HOLD: mandatory named body greeting conflicts with locked query"
    if candidate["requires_exact_attestation"] and candidate["sample_words"] > candidate["max_words"]:
        return "HOLD: exact limit declaration would be false"
    if not candidate["permission_granted"]:
        return "HOLD: external form permission denied"
    if not candidate["attachments"]:
        return "HOLD: approved assets missing"
    return None


def simulate(candidates: list[dict], daily_ceiling: int = 5, used_slots: int = 1,
             as_of: date = SIMULATED_AS_OF) -> tuple[Ledger, SimulatedSender]:
    """Local, deterministic example of immutable attempt and capacity controls."""
    if used_slots < 0 or daily_ceiling < used_slots:
        raise ValueError("Invalid daily capacity")
    ledger, sender = Ledger(), SimulatedSender()
    for candidate in candidates:
        cid = candidate["id"]
        if cid in ledger.outcomes:
            ledger.warn_duplicate(cid)  # Do not overwrite SENT with HOLD.
            continue
        reason = eligibility(candidate, as_of)
        if reason:
            ledger.record(cid, "HOLD", reason)
            continue
        if used_slots + sender.actions >= daily_ceiling:
            ledger.record(cid, "HOLD", "Daily possible-delivery ceiling reached")
            continue
        attempt_id = f"MOCK-ATTEMPT-{cid}"
        if attempt_id in ledger.attempted:
            ledger.record(cid, "HOLD", "Duplicate attempt key")
            continue
        ledger.attempted.add(attempt_id)
        ledger.record(cid, "SENDING", f"Mock prewrite/readback: {attempt_id}")
        receipt = sender.send_once(cid, candidate["attachments"])
        ledger.record(cid, "SENT", f"Simulated provider acknowledgement only: {receipt}")
    return ledger, sender


def main() -> None:
    candidates = json.loads(Path(__file__).with_name("synthetic_candidates.json").read_text(encoding="utf-8"))
    ledger, sender = simulate(candidates)
    print(json.dumps({"offline_only": True, "real_transmissions": 0,
                      "fixture_as_of": SIMULATED_AS_OF.isoformat(),
                      "mock_send_actions": sender.actions,
                      "research": {c["id"]: research_assessment(c) for c in candidates},
                      "outcomes": ledger.outcomes, "events": ledger.events}, indent=2))


if __name__ == "__main__":
    main()
