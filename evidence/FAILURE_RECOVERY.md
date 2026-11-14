# Failure modes, prevention and residual risk

A sanitised analysis of the owner-supervised workflow. This is a **design learning record**, not a copy of raw provider logs.

| Failure | Cause or observation | Change introduced | Remaining risk |
| --- | --- | --- | --- |
| Strong candidates held for package reasons | Asset-selection precedence misapplied | Separate literary-fit label from readiness; canonical asset selection rules | Missing actual approved combined files still require HOLD |
| No persistent dual labels | Run report values were not stored in a structured column | Appended AC and AD as research-owned validated fields | Historical backfill still requires human calibration |
| Stale research opportunity | An old PREQUALIFIED state could linger | 30-day official opening/routing refresh before actionable count | Send-day independent recheck still necessary |
| Browser-origin prompt injection | Public agency pages and form text could issue instructions to an agent | External content treated as data; Prospecting cannot submit | Browser tool actions not hard-isolated in supervised mode |
| Unnecessary Gmail restriction proposed | Research needs Sent-folder history to avoid duplicates | **Retained Gmail Allow read actions**; Prospecting writes forbidden | Human approval must continue to deny prohibited writes |
| Weak configuration comparison | Matching versions were checked by text alone | File identity, revision metadata and optional SHA-256 verification; compact verified digest | Hash unavailable in some tools; record honestly |
| Two attachments failed in email preparation | Incorrect connector file-reference handling | Binary file handles, correct attachment array, unsent diagnostic | Provider/tool changes need fresh validation |
| Hosted-form upload failed | Browser permission not available | Scoped owner approval and new attempt **only** after proven non-delivery | Permission refusal remains legitimate HOLD |
| Named agent requirement ambiguous | Generic owner-authored immutable letter conflicted with addressing preference | Distinguish advisory vs mandatory subject vs mandatory body | One submitted case still lacks independent agency-acceptance proof |
| Possible delivery without receipt | Unsafe blind-retry pressure | `SEND UNCONFIRMED`, reserved slot, no automatic retry | Manual evidence reconciliation may remain necessary |
| Governance edited during an active sending run | Owner updated private documents after startup; Submission detected modifications **after** last outward action | Recorded explicit configuration monitoring exception; proposed immutable run snapshot and pre-send revision check | **NOT FIXED/TESTED** — late detection could matter if future edits affect substantive sending rules |
| Submission-stage covering-letter constraint | Research regarded a high-fit lead as preliminarily ready; independent review found a required human-authored cover-letter addition | Recipient-specific HOLD rather than unauthorised rewrite or send | Improve earlier research-stage package detection without weakening independent review |
| Reply filing could be forgotten | Inbound classification did not itself guarantee project-mail organisation | Mandatory pre-archive label verification and ledger readback under existing Gmail label | Safe priority-mail handling and idempotence still need failure injection tests |

## Retry invariant

A failed *preparation* step can be corrected before any external action. Once a transmission might have occurred, never repeat it on an assumption of failure. A later attempt requires proof of prior non-delivery, new authorisation and a new attempt identity.

## Deployment honesty

- A model-visible prohibition is **not** the same as technical isolation. Supervised Prospecting retains Gmail read access but no sending authority; browser submissions require stronger tooling to be truly impossible.
- File modification metadata is **not** a content hash; only report a digest if actually computed.
- The 30-column schema was adopted **after the 12 November five-send trial**. The 13 November supervised cycle subsequently exercised the new labels and independent review; no controlled causal experiment or human calibration has been completed.
- The enclosed offline tests verify the **synthetic example only**, not connected production systems.

## New failure hypothesis — premature research closure (13 November 2026)

The observed supervised pass checked five net-new leads and two previously held candidates; it finished with one currently actionable prospect. The close report cited unresolved package requirements, **not an evidenced exhaustion of the authorised search budget**. This establishes an early-termination explanation gap, not a demonstrated model or web-tool outage.

**Later observed result:** the revised supervised 13 November rerun began with **one** actionable prospect and closed with **seven**, releasing four historical holds and qualifying two net-new leads. This supports the practical effectiveness of revised candidate-level hold reasoning and research continuation **in one attended case**. The total number of net-new candidates screened was not quantified in the closing log; the test does not establish repeatability or autonomy. See [execution evidence](SUPERVISED_EXECUTION_2026-11-13.md).
