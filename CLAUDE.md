# CLAUDE.md — ChronologyLab

Claims-ledger research project testing Kevin's conjecture that thermodynamic bookkeeping + loop
amplification make almost all pastward time travel impossible. **Docs-only so far (Stage 0 done);
no code yet.**

## Ground rules

- The original claim is **frozen verbatim** in `docs/CLAIMS.md §0` — never edit it; log repairs in
  the assumption ledger (§2 A4).
- Leaf verdicts move **only** with an entry in the CHANGELOG (`docs/CLAIMS.md §8`) naming the
  evidence. Leans ≠ verdicts.
- Citations carry `[v?]` until verified against the primary source (Stage 1); then replace with a
  full reference + located quote.
- Every statement is labeled by evidence level E1–E5 and provenance (verified / derived /
  reported / conjectured) — see `docs/METHODOLOGY.md §4, §9`.
- Kevin is new to formal research methodology — when using a methodological move, briefly explain
  it (he asked for this explicitly).

## Layout

- `docs/CLAIMS.md` — the claim ledger (the project's heart): frozen claim, steelman, assumptions
  A0–A5, leaves C1a–C7, theses T1–T3, toy registry TM1–TM6, changelog, glossary, references.
- `docs/METHODOLOGY.md` — the method and its rationale.
- `docs/PLAN.md` — operational plan: stage pipeline + per-leaf verification matrix + exit
  criteria. Keep it in sync with the Orchestrator flow when stages advance.
- `toys/` — mini versions of TM1–TM6 in `run_all.py` (run:
  `uv run --with numpy --with matplotlib python toys/run_all.py`); pre-registered can/cannot
  preambles in `toys/README.md`; outputs committed in `toys/out/`.
- `report/` — Report I: edit `template.html`, then `python3 report/build.py` regenerates
  `index.html` (standalone) + `artifact.html` (bare, for artifact publishing). The build refuses
  to run while any `PENDING-LIT` slot remains.

## Stage status

S0–S4 ✅ all executed 2026-07-26 (S2/S3 as minis) — **Report I** in `report/`, verdicts + full
changelog in `docs/CLAIMS.md §8`, open follow-ups in `docs/PLAN.md` (status block). Progress is
tracked in an Orchestrator flow.
