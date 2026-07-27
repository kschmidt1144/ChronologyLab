# Research Plan — Chronology Lab

**Goal:** deliver a verdict on the frozen claim (`CLAIMS.md §0`) — how much survives as stated —
plus the nearest defensible refined theses (T1 chronology protection · T2 Novikov consistency ·
T3 entropic suppression), each conditional on (framework × travel model).

This file is the operational plan. `CLAIMS.md` holds the claims and their verdicts; the
Orchestrator flow ("Chronology Lab", kykli.dev/orchestrator) mirrors stage status live.

## Pipeline

```
S0 ✅ ──► S1 ──►┬─► S2a ─┬──► S3 ──► S4
decompo-  lit   │        │    derive   report
sition    verify└─► S2b ─┘    + audit
                 (parallel)
```

Evidence flows *into* leaves from two directions — the literature (S1) and our own toys/derivations
(S2/S3) — then leaves compose into the root verdict (S3 audit), which S4 writes up.

> **Status 2026-07-26: the full pipeline S1→S4 was executed in one pass** (S2/S3 as mini
> versions) — deliverable: **Report I**, `report/index.html`. Remaining open follow-ups, in
> priority order for Kevin to choose from: (1) C4b deep dive — close reading + structured
> disagreement map of Kim–Thorne vs Hawking vs KRW; (2) full TM2 billiard (real mechanics, not
> the schematic consistency equation); (3) formalize C2a + C5c into a standalone derivation note;
> (4) SEP "Time Travel and Modern Physics" pass for philosophical counterarguments we haven't
> steelmanned.

> **P1 executed 2026-07-26 → Report II** (`report2/`; follow-up item 3 thereby superseded):
> pre-registered targets T1–T5 all held (one logged sharpening, T2a exact reversibility);
> C2a/C5c upgraded to E1/E2-in-model; adversarial novelty scan in `docs/P1_NOVELTY.md`.
> Remaining open options: C4b deep dive, full TM2 billiard, SEP counterargument pass, P2/P3
> frontier programs.

---

## Stages — inputs, outputs, and what "done" means

### S0 — Decomposition ✅ (2026-07-26)
Frozen claim; steelman with logged repairs; assumptions A0–A5; 19 leaves with pre-registered leans
and falsifiers; theses T1–T3; toy registry TM1–TM6. Outputs: `CLAIMS.md`, `METHODOLOGY.md`.

### S1 — Literature verification sweep ← NEXT
For each of the ~27 `[v?]` references: locate the primary source, confirm it actually supports what
the ledger cites it for, extract the supporting quote + locator (page/eq.), and clear the flag.
- **Reading order:** on-ramps first for orientation (SEP time-travel entries; Visser's *Lorentzian
  Wormholes*; Feynman's *QED*), then primaries grouped by leaf cluster: energy (Wald; Carroll;
  Visser ch. on mouth bookkeeping) → consistency (Consortium 1990; EKT 1991; Deutsch 1991; Carlini
  et al. 1995) → chronology protection (Kim–Thorne 1991; Hawking 1992; KRW 1997; Ori; Krasnikov)
  → quantum CTC models (Lloyd et al. 2011; Aaronson–Watrous 2009; Ringbauer 2014; Politzer;
  Hartle; Friedman–Papastamatiou–Simon) → thermodynamics (fluctuation theorems; Devin; Lewis 1976).
- Leaf statuses upgrade E4 → E1/E2 where the source carries a theorem or computation; **every lean
  the sources flip gets a CHANGELOG entry** (flips are the interesting output).
- **Done when:** no unresolved `[v?]` remains (each verified, or explicitly downgraded/removed as
  "could not verify"), and every leaf's What's-known cites verified sources.

### S2a — Toys: TM1 loop-map lab + TM2 mini-billiard
- **TM1:** implement F = E∘J on small state spaces; scan gain regimes ‖Λ‖ < 1 / > 1 / ≈ 1; build
  the explicit *contracting* counterexample (a stable consistent history) that refutes the
  universal "any mismatch kills the history" (C4c), and map marginal cases (C4d).
- **TM2:** 1-D EKT-style billiard with a time-offset jump; count consistent solutions per initial
  condition across a parameter sweep (C3b existence, C3c multiplicity, C5b measure).
- **Done when:** each toy's pre-registered can/cannot preamble is written *before* running, the
  run is reproducible, and results are attached to leaves with CHANGELOG entries.

### S2b — Toys: TM3 qubit CTC sim + TM4 horizon cartoon + TM5 measure estimate + TM6 arrows demo
- **TM3:** Deutsch fixed-point solver (iterate the CPTP loop map), multiple-fixed-point demo,
  entropy of fixed points; P-CTC postselection incl. a grandfather circuit (C2b, C3b, C3c, C6a).
- **TM4:** geometric series of circuits with gain g = blueshift × defocusing; where the divergence
  lives as g ≷ 1 — the Kim–Thorne vs Hawking disagreement made vivid (C4a, C4b).
- **TM5:** conspiracy-measure estimator — toy phase-space count of the entropy deficit ΔS of a
  consistent macroscopic intervention → suppression exp(−ΔS/k_B), compounding per circuit
  (C2a, C5c, T3).
- **TM6:** Feynman-arrows loop demo — discretized sum over histories with a loop-mismatch dial δ;
  show amplitude(δ) collapse onto δ = 0 with width set by ħ (C6b, C3a).
- Same done-standard as S2a.

### S3 — Derivations + inference audit
- Formalize **C2a**: entropy-periodicity on closed worldlines + the N-circuit compounding bound
  P ~ exp(−N·ΔS/k_B).
- Formalize **C5c**: assemble TM5 + fluctuation-theorem literature into a quantitative suppression
  statement with explicit assumptions.
- **C7 audit:** write C0 as an explicit logical function of leaf verdicts; evaluate it; identify
  the *minimal set of leaf-flips* that would rescue C0 as stated.
- **Done when:** both derivations are written with assumption lists, and the audit table is
  complete.

### S4 — Final report
Verdict on C0 as stated + the conditional table over (framework × travel model) for T1/T2/T3.
Every verdict labeled with evidence level (E1–E5) and provenance (verified/derived/reported/
conjectured); a "surprises" section listing every lean that flipped; a "what would settle it"
section for leaves stuck OPEN. Format: compiled markdown/HTML report in-repo (WorldEconomy style).

---

## Verification matrix — how each leaf gets its verdict

| Leaf | Claim (short) | Lean (pre-reg.) | How it gets settled | Stage |
|---|---|---|---|---|
| C1a | global "energy of the universe" is well-defined | FALSE | textbook verification (Wald; Carroll) | S1 |
| C1b | pastward transport violates conservation | FALSE | Visser wormhole mouth bookkeeping | S1 |
| C1c | state functions periodic on closed worldlines | TRUE-but-weak | settled by definition; write-up + scope note | S3 |
| C2a | dissipation forbids closed worldlines (suppressed) | TRUE | fluctuation-theorem derivation + lit | S1 + S3 |
| C2b | one-shot trip must conserve global entropy | FALSE as stated | D-CTC vs P-CTC entropy bookkeeping | S1 + S2b (TM3) |
| C2c | enthalpy must match | retired | category error; repair logged (A4) | done |
| C3a | consistency = exact fixed point (+ ħ tolerance) | TRUE (M1) | definitional + TM6 tolerance demo | S2b (TM6) |
| C3b | consistent solutions exist generically | TRUE (anti-C0) | verify EKT/Consortium/Deutsch + replicate | S1 + S2a/S2b |
| C3c | the consistent solution is unique | FALSE | same sources + TM2 solution counting | S1 + S2a |
| C4a | something loops unboundedly many times | split | Hawking/KRW reading (fields vs travelers) | S1 |
| C4b | gain>1 divergence destroys machines (protection) | OPEN | map Kim–Thorne vs Hawking vs KRW + TM4 | S1 + S2b |
| C4c | gain<1 "driven to 0" ⇒ impossible | FALSE (backfires) | Banach argument + TM1 counterexample | S2a |
| C4d | marginal/oscillatory gain ≈ 1 | OPEN | TM1 regime scan | S2a |
| C5a | "almost all" needs a declared measure | repair | done (methodological) | done |
| C5b | consistent set is measure-zero | FALSE | lit + TM2 sweep statistics | S1 + S2a |
| C5c | macroscopic intervention entropically suppressed | TRUE (in spirit) | TM5 estimate + S3 derivation | S2b + S3 |
| C6a | postselection cancels mismatched branches | TRUE (P-CTC) | verify Lloyd et al. + TM3 P-CTC sim | S1 + S2b |
| C6b | stationary-phase cancellation (sum over histories) | TRUE as mechanism | verify Carlini et al. + TM6 | S1 + S2b |
| C7 | C0 follows from the leaves | NO as stated | formal reassembly audit | S3 |

## Exit criteria

The project is complete when **every leaf is either (a) settled at E2 or better, or (b) explicitly
OPEN with its blocking unknown named** (e.g. "requires quantum gravity"), **and** the C7 audit and
S4 report are written. Success = calibrated verdicts, not vindication (`METHODOLOGY.md §9`).

## Risks & honesty notes

- **Citation risk:** Stage-0 leans are literature-flavored model memory; S1 may flip several.
  Flips are signal, not failure — they get prominent CHANGELOG entries.
- **Scope risk:** C4b (chronology protection) is a 30-year open problem. Our deliverable is a
  precise *map* of the disagreement and what hinges on it — not a resolution.
- **Tooling:** toys in Python via `uv`, one directory per toy under `toys/`, each ≲ ~300 LOC so
  they stay auditable; every toy's can/cannot preamble written before its first run.
