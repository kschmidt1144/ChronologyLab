# Chronology Lab

**Report I live at [kykli.dev/chronologylab](https://kykli.dev/chronologylab/)** · public repo

A claims-ledger research project: take one big conjecture about time travel to the past and
thoroughly prove or disprove it — assumptions explicit, reasoning decomposed into individually
testable pieces, verdicts earned per piece and then recomposed.

## The claim under test (Kevin, 2026-07-26 — canonical statement in `docs/CLAIMS.md §0`)

> "Almost all time travel to the past is impossible, because of the exponential growth potential
> of energy and disorder mismatches. If time travel is possible, then the universe's state — its
> enthalpy/entropy as well as its total energy — must be exactly the same when time returns to
> the present (the moment the jump to the past occurred). More specifically, all possible paths
> that do not result in an exactly equal energy state will be cancelled out. This is because of
> the infinite looping potential of jumps to the past: even a tiny difference will be driven
> toward infinity or zero as unlimited time-travel jumps occur."

## Documents

- **`docs/CLAIMS.md`** — the heart of the project: the frozen claim, its steelman, the assumption
  ledger, the decomposition into 19 testable leaves (C1 energy · C2 entropy · C3 exactness ·
  C4 amplification · C5 measure · C6 cancellation · C7 inference audit), refined theses T1–T3,
  toy-model registry TM1–TM6, and the append-only CHANGELOG of verdict movements.
- **`docs/METHODOLOGY.md`** — how the investigation is run and why: claims-ledger method,
  operationalization, evidence standards E1–E5, pre-registration, literature & toy-model
  protocols, honesty rails. Written as an introduction to doing this kind of research.
- **`docs/PLAN.md`** — the operational plan: stage pipeline S0–S4 with done-criteria, the
  leaf-by-leaf verification matrix (how each of the 19 sub-claims gets its verdict), exit
  criteria, and risks.
- **`report/index.html`** — **Report I** (the deliverable): all 19 leaves executed in order with
  verdict chips, verified primary-source quotes, and computed figures; verdict on the claim +
  what survives. Rebuild with `python3 report/build.py` after editing `report/template.html`.
- **`toys/`** — the six mini computational models + committed outputs (`toys/out/`).

## Roadmap

| Stage | What | Status |
|---|---|---|
| S0 | Decomposition, assumption ledger, pre-registered leans | ✅ 2026-07-26 |
| S1 | Literature verification sweep — every load-bearing citation checked against primaries (4 parallel agents; 2 attribution errors found & fixed) | ✅ 2026-07-26 |
| S2 | Toy models TM1–TM6 (`toys/run_all.py`) | ✅ 2026-07-26 (minis) |
| S3 | Derivations + the C7 inference audit | ✅ 2026-07-26 (first pass) |
| S4 | **Report I** — verdict on the claim + conditional T1–T3 table | ✅ 2026-07-26 — `report/index.html` |

## Orientation (pre-registered, subject to revision by evidence)

The claim's three mechanisms each turn out to shadow a real research program: its runaway loop
amplification ≈ **Hawking's chronology protection conjecture**; its exact-match survival rule ≈
**Novikov self-consistency** / **Deutsch's fixed points**; its cancellation of mismatched paths ≈
**postselected CTCs**. Two known gaps: "total energy of the universe" is not well-defined in
general relativity, and the "driven to 0" horn *stabilizes* time travel rather than forbidding it.
Standing counterevidence: in every studied toy system, self-consistent solutions are generic
(often infinitely many), not measure-zero-rare. Expected shape of the final verdict: *false as
stated; substantially true in refined forms T1–T3* — but that's a lean, and Stages 1–3 exist to
test it.

Upgrade (same day): the cancellation mechanism is now best formulated as **stationary-phase
interference in the sum over histories** (C6b) — the same principle that makes light appear to
take the stationary path — which removes the need for "meta-time" and matches a 1995 result
deriving Novikov consistency from the least-action principle.
