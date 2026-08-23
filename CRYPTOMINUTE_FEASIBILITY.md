# CryptoMinute Feasibility Probe

Run: 2026-08-23T13:41:28.526559

## Verdict: API_UNRELIABLE

Public DNS for `api.cryptominute.com` does not resolve from this Mac/network:
`URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>`.

This is a hard blocker for live smoke. Source-level schema review passed,
but runtime data availability cannot be confirmed without DNS reachability.

## Scope
- Source review: completed
- Live smoke: blocked at DNS resolution
- Reproducibility: not runnable
- Historical coverage: not runnable

## Implication for H11
Do not pre-register `news-event abnormal return study` until live API
reachability and historical depth are independently confirmed.
