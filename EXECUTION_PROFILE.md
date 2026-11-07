# Execution Profile — Public Summary

**Design:** Bounded daily orchestration over a private query tracker, append-style run log, approved-asset register and project-scoped correspondence. Actual service IDs and personal records are excluded.

## Run sequence

|Stage|Work|Control / output|
|-|-|-|
|0 · Validate|Check run uniqueness, authority and record access|Stop on mismatch|
|1 · Reconcile|Resolve uncertain sends; process new replies|Handle project-wide stops first|
|2 · Shortlist|Reuse vetted leads; screen up to **10** new candidates|Target **10** eligible prospects|
|3 · Verify|Check current official rules for each intended recipient|No cached permission to send|
|4 · Prepare|Apply Contract gates to approved package|Hold exceptions for owner|
|5 · Dispatch|Dual-write `SENDING`, attempt once, inspect receipt, commit result|Maximum **5 attempts** per authorised run|
|6 · Close|Sync changed state, record exceptions and measured usage|No compensating run to hit quota|

## Evidence-led fit ranking

|Criterion|Weight|
|-|-:|
|Genre and intended readership|35|
|Demonstrated taste and represented work|30|
|Career-stage compatibility|20|
|Verifiable personalisation opportunity|15|
|**Total**|**100**|

* A score **prioritises research**; it never overrules a mandatory gate.
* Official submission rules govern eligibility; third-party listings are discovery leads only.

## State and recovery model

```text
CANDIDATE → SCREENED-IN → QUEUED → READY → SENDING
     └── SCREENED-OUT / HOLD / BLOCK          ├── SENT
                                               └── SEND UNCONFIRMED
```

|Data layer|Function|
|-|-|
|Query tracker|Current candidate, dispatch and response states|
|Run/event log|Linked attempts, receipts, corrections and recovery|
|History index|Prevent duplicate human/agent approaches|
|Approved assets|Versioned source content and permitted modifications|
|Response monitor|Distinguish acknowledgement, rejection, request and offer|

* Separate **decision**, **dispatch**, **response** and **record-commit** statuses; a `READY` state is not delivery evidence.
* Prefer changed-record reads and deterministic checks; bound research retries and UI operations.
* No default subagents; stop at permission, safety or resource limits.

**Evidence boundary:** These are public operating rules, not reusable credentials, deployable code or independent confirmation of every historical control. See [Execution Evidence](../evidence/EXECUTION_EVIDENCE.md).

