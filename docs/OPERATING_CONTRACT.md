# Operating Contract — Public Summary

**Purpose:** Find and query eligible literary agents using only approved materials and authorised channels. **Eligibility and correctness outrank submission volume.**

## Authority

|Permitted within configured autonomy|Human approval / stop required|
|-|-|
|Research prospects; check current official rules|Unverified identity, policy or submission route|
|Rank fit; prepare standard approved packages|New or altered manuscript materials, facts or claims|
|Dispatch a compliant package within standing authority|Manual-only steps, CAPTCHA, fees or contractual commitments|
|Monitor authorised project replies and update records|Manuscript requests, representation offers and substantive replies|

* Public copy is **inactive**: it neither grants credentials nor activates a campaign.
* The latest private configuration targets **10 eligible prospects** and allows **no more than five primary send attempts** per authorised daily run. Targets never override gates.

## Mandatory dispatch gates

|Gate|Required control|Failure disposition|
|-|-|-|
|1 · History|Check prior human/agent sends, recipient duplicates and agency conflicts|`BLOCK` / `HOLD`|
|2 · Fit|Verify credibility and documented interests|`SKIP` / `HOLD`|
|3 · Current policy|Recheck official open status, route, limits and AI conditions **in the run**|`SKIP` / `HOLD`|
|4 · Truthfulness|Use approved declarations and supported author facts|`HOLD`|
|5 · Materials|Match exact approved letter, sample, synopsis and format limits|`HOLD`|
|6 · Preflight|Validate recipient, account, final package and authority|`HOLD`|
|7 · Persist|Write and read back `SENDING`, IDs and manifest in **tracker + event log**|**No send**|
|8 · Dispatch|Send once; seek provider evidence; record outcome and payload assurance|`SENT` / `SEND UNCONFIRMED`|

## Stop and recovery rules

* **Project-wide stop:** substantive request/offer, loss of required mailbox or state access, material integrity issue or failed post-send state commit.
* **Recipient hold:** unresolved policy, unsupported required answer, manual-only gate or uncertain earlier dispatch.
* **Uncertain send:** preserve the original attempt and investigate. A timeout is **not permission to resend**.
* **Replies:** acknowledgements and silence are not rejections. Follow up only where recipient policy and owner authority permit.
* **Records:** distinguish dispatch, package assurance, response and record-commit state. Retain corrections and human/agent provenance.

> Public summary of owner-governed private rules, not a claim that every historical run passed an independent compliance audit.

