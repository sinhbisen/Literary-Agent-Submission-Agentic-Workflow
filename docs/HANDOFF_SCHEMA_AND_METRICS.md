# Handoff schema and research metrics — Phase 1

**Public structural description | 30 columns | Private values excluded**

## Column ownership

| Columns | Owner | Meaning |
| --- | --- | --- |
| A:X | Prospecting | Stable candidate ID, agency and person, dated source evidence, 100-point literary score, preliminary route, package category, duplicate history, research state and hold reason |
| Y:AA | Submission | Independent review disposition, specific hold reason, final dispatch candidate link |
| AB | Shared with conflict checks | `record_revision` |
| AC | Prospecting | `fit_qualification` |
| AD | Prospecting | `preliminary_submission_readiness` |

**Controlled values**

- AC: `FIT-QUALIFIED`, `FIT-NOT-QUALIFIED`, `FIT-UNVERIFIED`.
- AD: `SUBMISSION-READY`, `SUBMISSION-NOT-READY`, `SUBMISSION-UNVERIFIED`.
- These labels are distinct from `prospecting_state`, `READY`, `SENDING`, `SENT`, `SEND UNCONFIRMED`, and `PROVEN NOT DELIVERED`.

## Semantics

- AC captures evidenced *literary suitability*. Missing submission documents or a closed agent do not, by themselves, degrade this classification.
- AD captures *provisional feasibility when Prospecting checked the official source*. This value is historical, not a live permission switch.
- **Current actionable-ready** additionally requires a prequalified research state, dated official opening/route evidence no older than 30 days, no later independent HOLD, and no already-sent or uncertain attempt.
- A strong fit behind an opening/package/historical restriction remains AC=`FIT-QUALIFIED`, AD=`SUBMISSION-NOT-READY`, with a release condition.
- Reconciliation with Gmail Sent supports duplicate detection but Prospecting may not send or process agency responses.

## Minimal record example (entirely synthetic)

```json
{
  "candidate_id": "DEMO-001",
  "literary_fit_score": 88,
  "source_checked_on": "2026-11-12",
  "prospecting_state": "HELD-PACKAGE",
  "fit_qualification": "FIT-QUALIFIED",
  "preliminary_submission_readiness": "SUBMISSION-NOT-READY",
  "hold_reason": "Agency requires one combined sample-and-synopsis document; none approved",
  "record_revision": 3,
  "submission_review": null
}
```

## Denominators and metric definitions

| Metric | Formula | Qualification |
| --- | --- | --- |
| Fit qualification | Distinct `FIT-QUALIFIED` / distinct screened | Same dated research cohort |
| Preliminary readiness | Distinct fit-qualified **and** research-ready / distinct fit-qualified | Dated, not live delivery |
| Fit-qualified blocked opportunity | Fit-qualified and not currently actionable | Retain with release reason |
| Submission conversion | Unique provider-confirmed submitted candidates / research-prequalified candidates | Reconcile against external action evidence |
| Fresh actionable inventory | Distinct PREQUALIFIED + FIT-QUALIFIED + SUBMISSION-READY + recent official source, excluding independent dispatch conflicts | Dynamic at report time; **seven-candidate target**; never send authorisation |

The existing 100-point rubric has **no numerical cut-off**. A future ten-agent human calibration is proposed but **has not been completed**. Unknown measurements must be `UNAVAILABLE`, not zero.

## Historical migration note

After the 12 November 2026 submissions, the private handoff was extended from 28 to 30 columns and **15 historical research rows** received conservative retrospective classifications: **11 FIT-QUALIFIED** and **six historically SUBMISSION-READY**. These are evidence-derived annotations, not a new search or re-verification. Five of the six historical ready candidates had already been submitted; the sixth remained on the Submission Agent's HOLD. Therefore **six historically ready does not mean six candidates available to send today**.

## Owner-adjusted targets and stopping evidence

| Item | Revised public rule |
| --- | --- |
| Live actionable target | **7** distinct candidates, not seven historical PREQUALIFIED flags |
| Trigger | Replenish when current actionable inventory is **below 7** |
| Per-pass research cap | **15 net-new substantively screened** candidates |
| Normal end | Seven actionable reached or 15 screened |
| Early closure below both | Specific evidenced global stop, genuine research/source exhaustion, actual resource limit or owner decision; not a generic list of package holds |
| Duplicate and prior-send protections | Unchanged |

**Measure the missed-opportunity question:** log `net_new_screened`, `screen_budget_used = net_new_screened / 15`, `actionable_inventory / 7`, blocked high-fit candidates and a categorised stop reason. Historical rechecks do not consume the net-new allowance. No invented token, cost, source-call or retry numbers.

## Observed 13 November cohort — denominator discipline

- Initial post-policy actionable inventory **1**; revised Prospecting close **7**. Four historical holds released, two net-new qualified; these are different classes of gain.
- **Seven** were independently reviewed by Submission; **five** provider-confirmed submissions, **one** recipient-specific HOLD and **one** ready-but-unsent due to daily capacity.
- Within this *specific handoff cohort*, **5/7** underwent provider-confirmed outward actions (about **71.4%**). This is **not** a representation rate or controlled experiment; the denominator does not describe all agents historically researched.
- Do **not** calculate net-new screening yield from **two qualified** without the actual total net-new screened. The closing evidence only verifies that the cap of 15 was respected; the exact denominator is **UNAVAILABLE**.
- For post-send state, use the **dispatch ledger**, not Prospecting-owned U/AD flags, which can legitimately remain as a historical research judgement.

[Observed supervised execution](../evidence/SUPERVISED_EXECUTION_2026-11-13.md)
