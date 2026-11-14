# Offline synthetic demonstration — Phase 1

This is a **standard-library Python illustration**, not the production literary-agent workflow. Every agent, agency, filename, receipt and provider acknowledgement is invented. The code uses **no network requests, account credentials, Gmail, Drive, browser tools or LLM calls**. `SENT` is a mock local outcome.

## Run

From `demo/`:

```bash
python simulate.py
python -m unittest -v test_workflow.py
```

The fixture date is deliberately frozen at **12 November 2026** so its 30-day freshness tests remain reproducible. This is *not* a claim that today's actual agency openings have been verified.

## What is demonstrated

- Separate persistent fit and preliminary readiness labels, without pretending either is final send authority.
- A fit-qualified prospect blocked by an unavailable combined sample stays visible in the opportunity backlog.
- Official route/opening evidence older than 30 days is excluded from actionable readiness while preserving literary fit.
- A previously `SENT` or `SEND UNCONFIRMED` prospect cannot be re-sent, even if the research-stage readiness label says `SUBMISSION-READY`.
- External page text cannot grant sending permission or override a historical duplicate; the sample contains a deliberately malicious page instruction that remains inert text.
- Strict AI-free author content, truthfulness about exact word limits, mandatory body greetings, attachment availability and portal permissions remain independent checks.
- Unique mock attempts, a combined daily capacity limit and protection against duplicated input records.

The synthetic tests **do not validate** live Google Sheets conflict handling, Gmail scopes, browser isolation, owner permissions or external provider behaviour. For actual observed results see [the case study](../evidence/TWO_AGENT_CASE_STUDY.md).

## Added owner-policy demonstrations — 13 November 2026

The supplementary tests exercise:

- A **seven-actionable target** and **15 net-new research ceiling**; held/unverified candidates do not count towards seven, and a candidate-level problem cannot end the research pass.
- A **nearest approved same-category asset** choice for word-count guidance, including approximately 500 vs the existing shorter synopsis and approximately 10,000 vs a 10,014-word approved sample. A mismatch does not claim formal agency acceptance.
- **Metadata-only attachment naming** without altering contents.
- Semantic matching of available author details is a **human/agent judgement** in the operational workflow, not validated by this local demo; the synthetic test shows only that availability is distinct from approval to alter an immutable query.

The tests do not establish production autonomy, web-source coverage, live Gmail permissions or secure scheduler behaviour.
