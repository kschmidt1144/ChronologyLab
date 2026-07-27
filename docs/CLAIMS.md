# Claim Ledger — does thermodynamics forbid (almost all) time travel to the past?

**Status: Stages S1–S3 executed 2026-07-26 (mini versions) — verdicts assembled in
`report/index.html` ("Report I").** The per-leaf sections below deliberately retain the Stage-0
pre-registered leans as the historical record — the delta between lean and final verdict is data
(no lean flipped; several sharpened; two attribution errors found and fixed — see CHANGELOG §8).
Citation convention: **`[v?]`** marked a reference recalled from model memory; the 2026-07-26
verification sweep (four parallel research agents) checked every load-bearing one against
primary sources — per-item status, quotes, and URLs in the report's References section.

---

## 0. The claim (canonical statement)

> "Almost all time travel to the past is impossible, because of the exponential growth potential
> of energy and disorder mismatches. If time travel is possible, then the universe's state — its
> enthalpy/entropy as well as its total energy — must be exactly the same when time returns to
> the present (the moment the jump to the past occurred). More specifically, all possible paths
> that do not result in an exactly equal energy state will be cancelled out. This is because of
> the infinite looping potential of jumps to the past: even a tiny difference will be driven
> toward infinity or zero as unlimited time-travel jumps occur."
>
> — Kevin, 2026-07-26 (canonical wording adopted the same day at the claimant's direction,
> replacing the informal verbatim capture — spelling/grammar repaired, substance unchanged; see
> CHANGELOG)

The canonical statement is the fixed reference: **the claim under test must not drift in
substance** while we refine our reading of it. The wording repair was made at the claimant's own
direction and touched spelling and grammar only — every term the leaves test, including
"enthalpy" and "total energy," is retained. Any *substantive* repair is logged in §2 as a
steelmanning move, with a reason. This guards against the "motte-and-bailey" failure mode:
quietly proving an easier claim and crediting the original. The superseded informal capture
survives only in git history (initial commit).

### 0.1 Plain-language steelman (what we take the claim to assert)

1. **Loops.** Backward time travel creates causal loops: the present influences the past, which
   evolves forward into the present again.
2. **Bookkeeping constraint.** A history is only acceptable if, going around the loop, the
   universe's thermodynamic books — total energy and entropy — come back *exactly* equal.
3. **Amplification.** Loops can compound without limit, and each circuit multiplies any mismatch,
   so a history with any mismatch ε ≠ 0 is driven toward ∞ (or damped to 0) and is thereby
   eliminated ("cancelled").
4. **Measure conclusion.** Exactly-matching histories are an extreme fine-tuning — a measure-zero
   needle in the haystack of conceivable trips — so *almost every* attempted trip to the past
   corresponds to no allowed history: **almost all time travel to the past is impossible.**

---

## 1. The central ambiguity: three models of "going back"

Before any sub-claim is truth-apt we must fix what "the state of the universe when time returns to
the present" *means*. There are three standard models of pastward travel, and the claim reads
completely differently in each. **This is the single most important clarification in the project.**

| | Model | What "the returned state" means | Is the claim's comparison well-posed? |
|---|---|---|---|
| **M1** | **Single self-consistent history** (block universe with closed timelike curves; Novikov [v?]) | There is exactly **one** state at each time. There is no "original 2026 without the traveler" — the only 2026 that exists *already includes* the consequences of the traveler's arrival in 1926. | The comparison is **vacuous**: there are not two versions of 2026 to compare. Consistency is automatic — it is the *definition* of a solution. |
| **M2** | **Branching / many-worlds arrival** (the traveler lands in a different branch; effectively Deutsch's picture [v?]) | The "return" state is in a *different branch* from the departure state. | The constraint **dissolves**: branches need not match each other in energy or entropy at all. The claim does not bite in M2. |
| **M3** | **Mutable timeline with meta-time** ("Back to the Future": the timeline itself *changes*, iteration by iteration) | Successive *versions* of 2026, indexed by a second time parameter ("meta-time") in which the rewriting happens. | Well-posed **only if meta-time exists** — standard physics has no such parameter. We adopt it explicitly as a *modeling fiction* where needed. |

**Key structural insight.** The original claim runs its *dynamics* in M3 (iterated jumps, mismatches
amplified "as infinite time travel jumps occur") and states a *conclusion* that belongs to M1 (only
exactly self-consistent histories survive). The steelmanned synthesis is:

> **M3-iteration is a solution procedure whose fixed points are M1-histories.** Even if you imagine
> timeline-rewriting, the only histories that survive iteration are the exactly self-consistent
> ones; and if the fixed-point set were tiny and repelling, time travel would (almost) never occur.

That synthesis is a respectable heuristic — it is essentially the "fixed-point iteration" reading of
the Novikov self-consistency principle, and its amplification half is the intuition behind Hawking's
chronology protection conjecture (see C4). The project tests whether the heuristic's two factual
inputs — *tiny* fixed-point set, *repelling* dynamics — are actually true.

> **Upgrade (2026-07-26, logged in CHANGELOG):** there is a fourth reading that repairs M3's
> meta-time problem entirely — cancellation as **stationary-phase interference in the quantum sum
> over histories** (Kevin's proposal): inconsistent loop configurations destructively interfere
> *timelessly*, no iteration needed, fully at home in M1. This is now the claim's best
> formulation — see **C6b**.

---

## 2. Assumption ledger

Every result we derive is conditional on entries here. When a verdict depends on an assumption, it
cites the assumption's ID.

- **A0 — Time travel is on the table at all.** General relativity admits spacetimes containing
  closed timelike curves (CTCs): Gödel's rotating universe (1949) [v?], van Stockum cylinders,
  Gott's moving cosmic strings (1991) [v?], and traversable-wormhole time machines
  (Morris–Thorne–Yurtsever 1988) [v?]. All known constructions require exotic conditions (energy-
  condition violations, unbounded structures); whether nature realizes any is open. We do **not**
  assume time machines exist — we ask what would constrain them if they did.
- **A1 — Framework conditionality.** No experiment can currently touch this question, so "prove"
  means *derive within a stated framework*: (a) classical general relativity; (b) semiclassical
  gravity (quantum fields on curved spacetime); (c) quantum-information CTC toy models (Deutsch
  D-CTCs, postselected P-CTCs); (d) full quantum gravity — **unavailable**, and several leaves
  bottom out in "needs (d)". Every verdict carries its framework tag.
- **A2 — Travel model.** M1 / M2 / M3 as defined in §1. Verdicts are given per-model where they
  differ. Default is M1 (the only one standard physics can host without new postulates).
- **A3 — Operationalizations.**
  - "State of the universe at the return moment" → the microstate on a chosen spacelike slice Σ_T
    (classical: a phase-space point; quantum: a density matrix).
  - "The loop" → the **loop map** F = E ∘ J: take a candidate state x at time T, apply the jump J
    (insert the traveler/object into the historical state at T₀), evolve forward with the dynamics
    E from T₀ to T, yielding F(x) — the state the loop *produces* at T.

    ```
              jump J  (departure at T → arrival at T₀)
        x(T) ─────────────────────────────► x'(T₀)
          ▲                                     │
          │        ordinary evolution E         │
          └────────────────  ◄──────────────────┘
                F = E ∘ J   (one circuit of the loop)

        consistency:  F(x*) = x*                    (fixed point)
        stability:    F(x* + ε) ≈ x* + Λ ε,  Λ = DF(x*)   (linearization)
        claim's core: ‖Λ‖ ≠ 1  ⇒  ε → ∞ or 0 under iteration ⇒ only x* survives
    ```

    Caveat: J is really a *merge* operator (the historical state at T₀ **plus** the inserted
    traveler), and iteration of F is physical only in M3; in M1, F(x) = x is a constraint to be
    *solved*, and iterating F is at most a numerical algorithm for solving it. Formalizing J
    precisely is part of toy model TM1.
  - "Almost all" → measure-theoretic: a set of measure zero with respect to a **declared** measure
    (see C5a — undeclared, the phrase is not truth-apt).
  - "Cancelled" → three distinct formal meanings, kept separate: (i) classical: *is not a solution*
    of the equations; (ii) quantum: destructive interference in a sum over histories;
    (iii) postselection: projected out and renormalized away (P-CTCs). See C6.
- **A4 — Category repairs (logged steelmanning moves).**
  - **Enthalpy → dropped.** H = U + PV is defined for a system exchanging volume with a
    constant-pressure environment. The universe has no environment and no pressure bath; enthalpy
    is not a fundamental quantity in GR or cosmology. We replace "enthalpy/entropy" with
    **entropy** (C2) and treat energy separately (C1). *Reason: test the strongest defensible
    version; the entropy leg carries the claim's real force.*
  - **"Total energy of the universe" → localized.** Global energy conservation is not generally
    well-defined in GR (C1a). We test the repaired claims C1b/C1c instead. *Reason: same.*
- **A5 — The second law is statistical, not absolute.** Entropy decreases are not impossible,
  only exponentially improbable (fluctuation theorems: P(−ΔS) / P(+ΔS) ≈ exp(−ΔS/k_B)) [v?].
  Any "forbidden by the second law" verdict must therefore be phrased as *suppressed*, with a
  number, not *impossible*. This distinction turns out to matter enormously for C0's "almost all".

---

## 3. The claim tree

**C0 (root, = the original claim):** *Almost all time travel to the past is impossible, because
only histories whose energy and entropy return exactly to their original values survive the
infinite amplification of loop mismatches.*

```
C0 "almost all pastward time travel is impossible"
├── C1  Energy leg — "total energy must return exactly"
│   ├── C1a  "total energy of the universe" is a well-defined conserved scalar   [lean: FALSE]
│   ├── C1b  pastward transport of mass/energy violates conservation             [lean: FALSE]
│   └── C1c  state functions are periodic around a closed worldline              [TRUE, but tautological]
├── C2  Entropy leg — "entropy must return exactly"
│   ├── C2a  dissipation forbids closed worldlines (up to fluctuations)          [lean: TRUE — strongest leg]
│   ├── C2b  a one-shot trip must conserve the universe's entropy                [lean: FALSE as stated]
│   └── C2c  enthalpy must match                                                 [category error → repaired, A4]
├── C3  Exactness leg — "only exact matches are allowed"
│   ├── C3a  consistency ⇔ exact fixed point of the loop map                     [TRUE in M1, by construction]
│   ├── C3b  consistent solutions EXIST for generic initial data                 [lean: TRUE — cuts AGAINST C0]
│   └── C3c  the consistent solution is unique                                   [lean: FALSE — ∞ solutions]
├── C4  Amplification leg — "mismatches are driven to ∞ or 0"
│   ├── C4a  something traverses the loop unboundedly many times                 [split: fields yes, travelers no]
│   ├── C4b  gain > 1 ⇒ divergence destroys the machine (chronology protection)  [OPEN — the big one]
│   ├── C4c  gain < 1 ⇒ "driven to 0" ⇒ time travel impossible                   [lean: FALSE — backfires]
│   └── C4d  marginal / oscillatory gain ≈ 1                                     [OPEN — needs TM1]
├── C5  Measure leg — "almost all"
│   ├── C5a  "almost all" requires a declared measure                            [methodological repair]
│   ├── C5b  consistent solutions are measure-zero-rare                          [lean: FALSE in studied models]
│   └── C5c  macroscopic pastward intervention is entropically suppressed        [lean: TRUE — best surviving version]
├── C6  Cancellation leg — "non-matching paths are cancelled out"
│   ├── C6a  postselection version (P-CTCs)                                      [TRUE in that framework]
│   └── C6b  stationary-phase / least-action version (sum over histories)        [lean: TRUE as mechanism — best formulation]
└── C7  Inference audit — does C0 follow from the leaves?                        [lean: NO as stated; refined T1–T3]
```

Each leaf below gets: **Statement** (plain + formal) · **Scope** (framework A1, model A2) ·
**What's known** · **Test route** · **Falsifier** (what result would flip it) · **Lean** (+ evidence
level E1–E5, defined in `METHODOLOGY.md §4`).

---

### C1 — the energy leg

**C1a. "The total energy of the universe is a well-defined, conserved scalar."**
- *Formal:* there exists a global functional E[Σ] of the state on a spacelike slice, conserved
  under evolution, for generic spacetimes.
- *Scope:* classical GR (A1a).
- *What's known:* **False in general.** Energy conservation in GR is local
  (∇·T = 0 always holds); a *global* conserved energy requires special structure — a timelike
  Killing vector (stationary spacetimes) or asymptotic flatness (ADM/Bondi mass). An expanding
  universe has neither: CMB photons redshift and their energy goes nowhere — total energy is simply
  not defined; dark-energy density stays constant while volume grows. Standard references: Wald,
  *General Relativity* (1984) [v?]; pedagogically, Carroll, "Energy is not conserved" (2010 blog)
  [v?]. **The universe already fails the claim's conservation test today, with no time machine
  involved.** Deep reason (Noether's theorem [v?]): conservation laws are shadows of symmetries
  of the action — energy conservation corresponds to time-translation symmetry, which a generic
  expanding spacetime lacks. No symmetry, no conserved quantity; C6b connects this leg to the
  action formulation.
- *Test route:* literature verification only (this is textbook material).
- *Falsifier:* a standard construction of conserved total energy for generic (e.g. FRW) spacetimes.
- *Lean:* FALSE (E1-level once cited). Consequence: the energy leg of C0 cannot be formulated
  globally and must retreat to C1b/C1c.

**C1b. "Transporting mass/energy to the past violates energy conservation (there's 'extra energy'
in the past epoch and 'missing energy' in the present epoch)."**
- *Formal:* in a CTC spacetime, local conservation ∇·T = 0 fails, or global charges (where defined)
  change, when a worldline threads the time machine.
- *Scope:* classical GR (A1a), M1.
- *What's known:* In wormhole time machines the books balance **locally and automatically**: the
  field equations enforce ∇·T = 0 everywhere; the wormhole mouths' masses shift to absorb the
  difference (an object of mass m entering mouth A and exiting mouth B changes the mouth masses —
  discussed by Visser, *Lorentzian Wormholes* (1995) [v?]). Nothing is violated; the "duplicate
  traveler" existing 1926–2026 was *always part of* the single history's stress-energy (M1).
- *Test route:* literature (Visser ch. on wormhole mechanics); optional toy bookkeeping model.
- *Falsifier:* a theorem that CTC-threading worldlines force ∇·T ≠ 0 or ill-defined Cauchy data.
- *Lean:* FALSE (conservation does not forbid pastward transport) — E4 pending S1.

**C1c. "Around a closed loop, conserved/state quantities must return to their values."**
- *Formal:* for a truly closed worldline γ (a particle whose worldline is a circle in spacetime),
  every state function is periodic along γ.
- *What's known:* **True but tautological** — a closed worldline revisits the *same events*, so
  "returning to the same value" is just "being the value it is there." The non-trivial content is
  not the periodicity itself but what it costs dynamically — that is the entropy leg, C2a.
  Crucially, this constrains only **closed worldlines**. A one-shot traveler's worldline is *not*
  closed: it starts at their birth and ends at their death, threading the machine once; during
  1926–2026 two segments of it coexist. No periodicity applies to them.
- *Lean:* TRUE-but-weak. The claim's energy constraint has force only for the (exotic) closed-
  worldline case, not for ordinary "visit the past once" scenarios.

---

### C2 — the entropy leg

**C2a. "Dissipation forbids closed worldlines (up to exponentially suppressed fluctuations)."**
This is our repair of "entropy must remain exactly the same" — and the strongest leg of the claim.
- *Formal:* along a closed timelike worldline, any state function — including entropy — is periodic
  (C1c). The local second law says entropy *production* (not mere transfer) is ≥ 0 along the
  worldline. Periodicity ⇒ total production around the loop = 0 ⇒ production = 0 *everywhere* on
  the loop. So a system on a closed worldline must be **perfectly reversible for its entire
  history**, or else the history is a thermodynamic fluctuation with probability
  ~ exp(−ΔS_produced/k_B) (A5).
- *Corollary (our derivation, to formalize in S3):* **you cannot remember completing a closed
  loop.** Recording a memory is irreversible (Landauer erasure cost [v?]); a memory of the loop is
  entropy production; entropy production breaks periodicity. Any "I've looped forever" scenario is
  self-contradictory for a macroscopic rememberer.
- *Compounding (the claim's "driven to 0", made rigorous):* a dissipative system making N circuits
  pays the fluctuation cost each time: P ~ exp(−N·ΔS/k_B) → 0 geometrically as N → ∞. The
  probability measure of many-loop histories of macroscopic dissipative travelers vanishes — this
  is a *precise* incarnation of "infinite looping drives it to 0."
- *Scope:* framework-light (thermodynamics + M1). Verification note (2026-07-26): the Devin
  preprint (arXiv:1302.3298) turned out to be arXiv-only and Maxwell's-demon-focused — too weak to
  carry this leaf, so C2a rests on our own derivation (E3) pending an independent source; the
  recalled "Hawking thermodynamic-arrow remarks" were not located and are dropped.
- *Test route:* derivation (S3) + literature (S1) + toy estimate (TM5).
- *Falsifier:* a consistent macroscopic dissipative closed-worldline model with O(1) probability.
- *Lean:* TRUE as the suppressed-not-impossible version — E3 now, targeting E2.
- *Report II upgrade (2026-07-26):* in the Markovian detailed-balance class the undriven version
  is now an **identity** — every consistent loop has s ≡ 0 exactly (T2a, telescoping) — and the
  fluctuation cost is carried entirely by the closure probability (T1). Status: E1/E2-in-model.
  See `report2/`.
- *Credit adjustment (2026-07-26, found by the P1 novelty scan):* the qualitative content of this
  leaf — dS/dτ must vanish around a CTC, and no records/memory can survive one — was published by
  Rovelli, "Can we travel to the past? Irreversible physics along closed timelike curves"
  (arXiv:1912.04702, 2019), which we had not known when Report I called the memory corollary "our
  derivation." Report I's claim is downgraded to *independent rediscovery, quantified here*;
  Gavassino (CQG 2025, arXiv:2405.18640) reaches memory-erasure by exact quantum kinematics.

**C2b. "A one-shot trip to the past must leave the universe's total entropy unchanged."**
- *What's known:* No such constraint is known. In M1 there is one history; entropy can rise
  monotonically along every slice of it *while the history contains a loop region*. In the quantum
  CTC toy models the bookkeeping is model-dependent: Deutsch's fixed points can be entropy-raising
  (Deutsch proposed selecting the *maximum-entropy* fixed point [v?]); postselected CTCs can
  *lower* entropy (postselection is not a CPTP evolution). What a traveler's arrival does impose is
  **constraint/correlation**: information arriving from the future is a boundary condition on the
  past epoch (see the bootstrap-information puzzle, flagged as out-of-scope note N1).
- *Falsifier / prover:* a theorem in some framework that global entropy at matching slices must be
  equal — none is currently known to us.
- *Lean:* FALSE as stated (the exact-equality version) — E4. The defensible content moved into C2a.

**C2c. "Enthalpy must match."** Category error; repaired at A4 (enthalpy needs a pressure
environment the universe doesn't have). Retired with the repair logged. — settled by definition.

---

### C3 — the exactness / fixed-point leg

**C3a. "A history with time travel is acceptable iff the loop returns the state exactly."**
- *Formal:* consistent histories = Fix(F) = {x : F(x) = x} (A3). In M1 this is **true by
  construction** — it is what "a solution of the equations of motion on a CTC spacetime" means
  (the Novikov self-consistency principle, which Friedman–Morris–Novikov–Echeverria–Klinkhammer–
  Thorne–Yurtsever 1990 argue is not an extra law but a consequence of demanding solutions exist
  [v?]).
- *Sharpening (the claim is too weak here, interestingly):* what must match is the **full
  microstate**, not merely energy and entropy. Equal energy and entropy are *necessary* conditions
  (they're functions of the state) but nowhere near *sufficient* — two states can match in E and S
  and differ in everything else. The original claim understates its own constraint.
- *Quantum sharpening (from the action formulation, C6b):* "exact" acquires a precise tolerance —
  loop configurations within ~ħ of stationary action still add coherently, so consistency is
  enforced only up to action differences of order ħ. For any macroscopic mismatch, ΔS_action/ħ is
  astronomically large and the cancellation is effectively perfect: the classical "exact match"
  rule *emerges* as the ħ → 0 limit rather than being postulated.
- *Lean:* TRUE in M1 (E1, by definition); FALSE in M2 (no constraint); M3 = the iteration story.

**C3b. "Consistent solutions exist for generic initial data." (If false, C0's 'almost all
impossible' gets its best support. If true, C0 is in trouble.)**
- *What's known:* the classic results point **against** C0 here. Echeverria, Klinkhammer & Thorne
  (1991) studied the "billiard ball paradox" (a ball enters a wormhole time machine aimed to knock
  its earlier self off course — the mechanical grandfather paradox) and found that **every initial
  condition they analyzed admitted at least one self-consistent solution — and typically
  *infinitely many*** [v?]. The same group showed free fields on such spacetimes have well-posed
  solutions [v?]. In Deutsch's quantum model, a consistent fixed point **always exists** for every
  circuit — a fixed-point theorem guarantees it (the CTC map is a continuous map of the compact
  convex set of density matrices; Brouwer/Schauder) [v?]. Carlini–Frolov–Mensky–Novikov–Soleng
  argued self-consistency even *follows from* the principle of least action in their toy [v?].
- *Test route:* S1 verify these results; S2 reproduce in miniature (TM2 billiard, TM3 quantum).
- *Falsifier of the lean:* a studied system with initial data admitting **zero** consistent
  solutions.
- *Lean:* TRUE (consistency is generic, not rare) — E4 now. **This is currently the strongest
  known evidence against C0 and we display it prominently (honesty rail, METHODOLOGY §9).**

**C3c. "The consistent solution is unique."**
- *What's known:* generically **no** — EKT found infinitely many consistent solutions for some
  initial data [v?]; Deutsch fixed points are non-unique for some circuits (hence his max-entropy
  selection rule [v?]). The real pathology of time travel in these models is
  **underdetermination** (physics stops predicting which consistent history occurs), not
  overdetermination (no history existing) as C0 asserts.
- *Optics analogy (same stationary-phase mathematics as C6b):* where several stationary paths
  exist, *all* are realized — a gravitational lens shows multiple images of a single quasar.
  Multiple consistent histories are the time-loop version of multiple images.
- *Lean:* FALSE — E4. Noteworthy inversion of the original claim's picture.

---

### C4 — the amplification leg (the claim's core mechanism)

**C4a. "Something goes around the loop infinitely many times."**
- *What's known:* **split verdict.** A one-shot traveler circuits once — no infinity. But **field
  modes** can circulate a wormhole time machine arbitrarily many times: near the moment the machine
  first forms (the *chronology horizon*), there are closed null paths a light ray can traverse
  unboundedly often, and vacuum fluctuations do exactly that. The claim's "infinite looping
  potential" is physically real — for radiation, at the horizon, not for travelers.
- *Lean:* TRUE for fields at compactly generated chronology horizons; FALSE for one-shot travelers.

**C4b. "Per-circuit gain > 1 ⇒ mismatch driven to ∞ ⇒ the time machine self-destroys."**
**This is Hawking's chronology protection conjecture — the original claim's mechanism is a
rediscovery of the leading professional argument against time machines.**
- *Mechanism:* a wave packet exits the past mouth *before* it entered the future mouth, flies back,
  and re-enters — circulating with per-circuit gain g = (blueshift b) × (defocusing attenuation d).
  Summing circuits gives a geometric series that diverges as the chronology horizon is approached;
  the renormalized vacuum stress-energy ⟨T_μν⟩ blows up, and its gravitational backreaction
  plausibly destroys the machine at the moment of formation.
- *What's known:* Kim & Thorne (1991) computed the divergence but argued quantum gravity cuts it
  off soon enough that the backreaction might be too weak to destroy the machine [v?]. Hawking
  (1992) argued the divergence is generic and decisive, coining "chronology protection" ("keeping
  the world safe for historians") [v?]. Kay–Radzikowski–Wald (1997) proved a rigorous semiclassical
  no-go: at a compactly generated chronology horizon, ⟨T_μν⟩ *cannot even be defined* in the usual
  way — the semiclassical framework itself breaks down there, so the question escalates to quantum
  gravity [v?]. Known loopholes: non-compactly generated horizons (Ori's models [v?]) evade KRW;
  Krasnikov exhibited special evading spacetimes [v?]; quantum-energy-inequality results
  (Ford–Roman [v?]) independently squeeze the exotic matter wormholes need.
- *Status:* **OPEN — a genuine research frontier, unresolved for 30+ years, awaiting quantum
  gravity.** Majority lean in the field: protection holds.
- *Test route:* S1 primary sources; TM4 (geometric-series cartoon of g ≷ 1 regimes).
- *Falsifier:* a fully self-consistent semiclassical time-machine formation with bounded ⟨T⟩.
- *Lean:* plausibly TRUE but unproven — E4. Note: if true it yields "**all** macroscopic time
  machines fail," which is *stronger* than C0's "almost all."

**C4c. "Per-circuit gain < 1 ⇒ mismatch driven to 0 ⇒ this too makes time travel impossible."**
- *What's known:* **this horn backfires.** A contracting loop map (‖Λ‖ < 1) is the *good* case for
  time travel: the Banach fixed-point theorem gives a **unique consistent history that nearby
  candidates relax toward** — consistency becomes *stable and self-enforcing*, the opposite of
  fine-tuned. (Quantum version: the Deutsch map is trace-norm non-expansive, which is why its
  consistent fixed points exist and iteration typically converges [v?].) "Mismatch → 0" doesn't
  delete histories; it deletes *mismatches*.
- *Consequence for C0's logic:* the "∞ **or** 0" dichotomy proves impossibility on only one horn.
  As stated, the argument shows at most: *either* machines self-destroy (g > 1, → C4b) *or*
  consistent time travel is robust (g < 1). **This is the claim's central logical gap.**
- *Test route:* TM1 exhibits an explicit contracting loop map with a stable consistent solution —
  a counterexample at E2 to the universal "any mismatch kills the history."
- *Lean:* FALSE as an impossibility argument — E3 now, E2 after TM1.

**C4d. "Marginal gain ≈ 1 / oscillatory (complex) gain."** Neither horn applies; behavior can be
neutral cycling, slow drift, or interference. Quantum interference connects to C6. — OPEN; TM1
maps the regimes.

---

### C5 — the measure leg ("almost all")

**C5a. "Almost all" requires declaring: a measure over *what*?** Candidate spaces: initial
conditions of the universe; spacetime geometries; attempted-intervention strategies. The truth
value can differ per choice — undeclared, the phrase is rhetoric, not mathematics. *Methodological
repair, settled: we will state the measure for every C5 verdict.*

**C5b. "With respect to natural measures on initial data, consistent solutions are measure-zero."**
- *What's known:* in the studied classical toys the situation is the **reverse**: EKT-type systems
  showed consistent solutions for *every* initial condition tried (measure one, not zero) [v?];
  fields likewise [v?]; Deutsch's model guarantees existence always [v?]. What gets suppressed is
  not *solutions existing* but *particular naive stories* ("I knock my earlier self fully off
  course, full stop") — those get replaced by nearby consistent ones (glancing blows), typically
  many.
- *Lean:* FALSE in studied models — E4. Second major standing challenge to C0.

**C5c. "Histories containing macroscopic pastward intervention are entropically suppressed —
'almost all' in the fluctuation-measure sense."** (Our synthesis target — the nearest defensible
version of C0's conclusion.)
- *Sketch:* combine C2a with self-consistency: a consistent history in which a macroscopic,
  dissipative, remembering agent threads a loop must realize conspiratorial correlations (the
  "banana peel" mechanism of Lewis 1976: paradox-averting failures are individually mundane but
  collectively fine-tuned [v?]). Fine-tuned macrostates carry an entropy deficit ΔS; fluctuation
  theorems price them at ~ exp(−ΔS/k_B); N circuits compound the price (C2a). Conjecture to test:
  **P(consistent macroscopic time-trip) ≲ exp(−ΔS_conspiracy/k_B) — astronomically small, never
  zero.** "Almost all … impossible" becomes "all but an exp-suppressed measure … unrealized."
- *Test route:* TM5 toy estimate + S1 literature on statistics of consistent solutions.
- *Falsifier:* consistent macroscopic-intervention solutions shown to carry no measure penalty.
- *Lean:* TRUE in spirit, pending quantification — E5 now, targeting E2/E3.
- *Report II upgrade (2026-07-26):* **quantified** — closure probability = Boltzmann weight of
  the loop state (T1), extensive in components (T4): one conspiratorial gram ⇒ P ≈ 10^{−2.6×10²²},
  now derived with stated assumptions rather than assumed. Provably never zero (floors positive):
  "almost all," never "impossible." Status: E1/E2-in-model. See `report2/`.

---

### C6 — the cancellation leg

**"All paths that do not return the exact state are cancelled out."** Two formal versions, kept
separate (they live in different quantum frameworks). Classically, "cancellation" adds nothing
beyond C3a — non-solutions aren't "cancelled" by any process; they simply never were solutions.

**C6a. Postselection version (P-CTCs).**
- *What's known:* **a literally real mechanism.** In **postselected CTCs** (Lloyd et al. 2011
  [v?]), the loop is implemented as quantum teleportation *postselected on the entangled outcome* —
  every branch in which loop-output ≠ loop-input is **projected out**, and the surviving
  amplitudes are renormalized. Kevin's sentence is close to a definition of P-CTCs. Consequences
  worth knowing: postselection makes the theory nonlinear — paradoxical evolutions get probability
  0 ("the universe refuses the experiment"), near-paradoxes warp outcome statistics
  (banana-peel-like), and the model gains outsized computing power (Deutsch CTCs → PSPACE,
  Aaronson & Watrous 2009, verified; P-CTCs → PP, Lloyd et al. 2011 resting on Aaronson 2005's
  PostBQP = PP — attribution corrected 2026-07-26) — a price tag some read as evidence against
  CTCs, though that is an aesthetic judgment, not a theorem. A P-CTC analogue was even simulated photonically
  (Ringbauer et al. 2014 — a *simulation*, not a real CTC [v?]).
- *Lean:* TRUE within the P-CTC framework (E1-in-toy-model). Note the inversion: cancellation
  makes *some* time travel consistent, rather than making almost all of it impossible.

**C6b. Stationary-phase / least-action version (sum over histories).** *(Added 2026-07-26 —
Kevin's proposal: import the mechanism by which "light takes all paths but only one is visible.")*
- *The borrowed principle, stated carefully:* in the sum-over-histories picture, every conceivable
  path contributes an amplitude e^{iS/ħ}, where S is that path's **action**. In a bundle of
  neighboring paths around a *stationary* point of S (δS = 0 — usually but not always the
  shortest/least-time path), the phases nearly agree and the contributions **add**; everywhere
  else the phases spin rapidly and neighbors **cancel**. The "visible" path of light is the
  surviving stationary bundle (Fermat's principle is the optics special case), with coherence
  tolerance set by ħ.
- *Formal transplant:* amplitude for a time-loop history = Σ over loop configurations of e^{iS/ħ},
  with self-consistency entering as a matching condition around the loop. Configurations with loop
  mismatch δ ≠ 0 destructively interfere; self-consistent configurations sit at stationary points
  and dominate. **This is "cancellation" without meta-time** — it happens once, timelessly, in the
  amplitude sum, and so lives comfortably in M1. It is the strongest formulation of the original
  claim's cancellation mechanism.
- *What's known:* path-integral treatments of CTC spacetimes exist (Politzer 1992 [v?]; Hartle's
  generalized quantum mechanics for nonchronal spacetimes [v?]). Carlini–Frolov–Mensky–Novikov–
  Soleng (1995) derived the Novikov consistency principle *from* the least-action principle in
  their billiard toy [v?] — "consistency = stationary action" is a published result, i.e. this leg
  of the claim independently reproduces a real 1995 research finding. Known cost: interacting
  quantum fields on CTC spacetimes can lose unitarity (Friedman–Papastamatiou–Simon [v?]) — the
  mechanism is coherent, but the resulting theory has open problems.
- *What it buys the other leaves:* a quantitative meaning of "exact" for C3a (match within action
  ~ħ); the Noether linkage for C1a (conservation ⇔ action symmetry); a non-mysterious reading of
  "cancelled" for A3(iii'); and multiplicity-as-lens-images for C3c.
- *Test route:* TM6 (numerical Feynman-arrows demo with a loop); S1 verifies the citations.
- *Falsifier:* a demonstration that the CTC sum over histories fails to localize on
  self-consistent configurations — or that no consistent stationary point generically exists
  (which would instead hand C0 its best support).
- *Lean:* TRUE as a mechanism within quantum frameworks — E4 now, E2 target via TM6. Same
  inversion as C6a: stationary phase *selects* consistent time travel rather than eliminating
  time travel.

---

### C7 — the inference audit (reassembly)

**"Given C1–C6, C0 follows."**
- *The needed pattern:* C0 requires (i) exact-match constraint [C3a — holds in M1], (ii) universal
  elimination of non-matching histories via amplification [needs *both* C4 horns to kill — but C4c
  backfires], and (iii) the surviving set to be tiny in a declared measure [C5b — currently leaning
  the opposite way in studied models].
- *Lean:* C0 **does not follow as stated** (E3, from the structure above; final verdict after
  S1–S3). What survives are three refined theses:

| | Refined thesis | Relation to C0 | Status |
|---|---|---|---|
| **T1** | **Chronology protection** (Hawking): nature prevents macroscopic time machines from forming at all — runaway loop amplification destroys them at birth. | *Stronger* than C0 ("all", not "almost all") — C0's mechanism, professionally formulated. | Open conjecture; majority-favored; needs quantum gravity. |
| **T2** | **Novikov consistency**: if CTCs exist, only exactly self-consistent histories occur — not by luck but enforced by the dynamics; you can visit the past but never change it. Consistent solutions are *generic*, usually *non-unique*. | Adopts C0's exact-match clause, rejects its "impossible" conclusion. | Well-supported within classical toys; predictivity worries (C3c). |
| **T3** | **Entropic suppression**: among consistent histories, macroscopic pastward interventions carry exp(−ΔS/k_B) fluctuation costs, compounding per circuit. | The defensible cousin of "almost all impossible": *all but an exponentially small measure*. | Our synthesis target (C2a + C5c); to be quantified. |

T1, T2, T3 are compatible (different questions: machine formation / history selection / measure).
**Project verdict target:** a conditional table over (framework A1 × model A2) stating which of
T1–T3 hold and exactly how much of C0 survives.

---

## 4. Standing evidence AGAINST the original claim (honesty rail)

Displayed prominently per METHODOLOGY §9 — these are the results our final verdict must defeat or
absorb:

1. **Existence is generic, not rare** — every studied initial condition in the billiard-ball
   literature had ≥ 1 (often ∞) consistent solutions (C3b, C5b) [v?].
2. **Quantum consistency always exists** — Deutsch's fixed-point theorem (C3b) [v?].
3. **The g < 1 horn stabilizes rather than forbids** (C4c) — the claim's own dichotomy contains a
   pro-time-travel branch.
4. **No global energy bookkeeping exists to violate** (C1a) — the conservation half of the claim
   rests on a quantity GR does not define.
5. **In M2 (branching) the whole constraint dissolves** — the claim is model-relative, and M2
   cannot currently be excluded.

## 5. Out-of-scope notes (parked, not forgotten)

- **N1 — bootstrap information** ("where did the looped watch/idea come from?"): entropy-adjacent
  and fascinating, but a different claim. Park until S4; revisit if C2 verdicts need it.
- **N2 — free will / "could I have done otherwise" framings**: philosophy literature (Lewis 1976
  [v?]) enters only where it makes C5c precise (banana-peel measure), not as metaphysics.

## 6. Toy model registry (Stage 2)

| ID | What | Tests | Can show / cannot show |
|---|---|---|---|
| **TM1** | Loop-map lab: explicit F = E∘J on small state spaces; scan ‖Λ‖ < 1, > 1, ≈ 1; basins, fixed-point sets | C3a, C4c, C4d | CAN refute universal "any mismatch kills the history" by counterexample; CANNOT say which regime real spacetimes are in |
| **TM2** | 1-D billiard with a time-offset wormhole (EKT in miniature): count consistent solutions per initial condition | C3b, C3c, C5b | CAN check genericity/multiplicity claims in a mechanical model; CANNOT establish them for our universe |
| **TM3** | Qubit CTC simulator: Deutsch fixed-point solver + P-CTC postselection; grandfather circuit; entropy of fixed points | C2b, C3b, C3c, C6 | CAN verify the quantum models' advertised behavior end-to-end; CANNOT decide which (if either) model nature uses |
| **TM4** | Chronology-horizon cartoon: geometric series of blueshifted/defocused circuits, g ≷ 1 regimes, where the divergence lives | C4a, C4b | CAN make the Hawking/Kim–Thorne disagreement's *structure* vivid; CANNOT resolve it (that needs quantum gravity) |
| **TM5** | Conspiracy-measure estimator: toy phase-space count of the entropy deficit of a consistent macroscopic intervention | C2a, C5c, T3 | CAN put a first number on exp(−ΔS/k_B) suppression in a toy; CANNOT price a real trip |
| **TM6** | Feynman-arrows loop demo: discretized sum over histories for a particle with a time-offset jump; total amplitude vs loop mismatch δ, phase-arrow visualization | C6b, C3a | CAN show inconsistent configurations cancel and "exactness within ~ħ" emerge numerically; CANNOT show nature actually sums this way over real CTCs |

Python via `uv`, matching WorldEconomy conventions. Each toy ships with a written "can/cannot"
preamble; a toy that "works" proves logical coherence of a mechanism, never physical actuality.

## 7. Stage plan

- **S0 ✅ (2026-07-26)** — decomposition, assumption ledger, pre-registered leans (this document).
- **S1 ✅ (2026-07-26)** — verification sweep executed via four parallel research agents; every
  load-bearing citation verified against primaries with quotes + URLs (report §References); two
  attribution errors found & fixed; sharpenings logged in CHANGELOG.
- **S2 ✅ (2026-07-26, mini versions)** — TM1–TM6 built and run (`toys/run_all.py`; pre-registered
  can/cannot preambles in `toys/README.md`); full-scale versions remain optional follow-ups.
- **S3 ✅ (2026-07-26, first pass)** — C2a derivation, TM5 scale estimate, and the C7 inference
  audit are in Report I; formal deep write-ups can follow on request.
- **S4 ✅ (2026-07-26)** — **Report I shipped:** `report/index.html` (+ private artifact) —
  verdict on C0 with the conditional T1–T3 table. Open follow-ups tracked in `PLAN.md`.

## 8. CHANGELOG (append-only; verdicts move only with a logged entry)

- 2026-07-26 — Ledger created; all leaves OPEN with pre-registered leans; no evidence gathered yet.
- 2026-07-26 — **Action-formulation upgrade (Kevin's proposal).** Added C6b (stationary-phase /
  least-action cancellation — repairs M3's meta-time problem; "consistency = stationary action"
  matches Carlini et al. 1995 [v?]); added the ħ-tolerance sharpening to C3a, the Noether note to
  C1a, the lensing-multiplicity analogy to C3c, toy TM6, and glossary/reference entries. Leaf
  count 18 → 19. Methodology note: this is a *mechanism substitution* (METHODOLOGY §2, step 2) —
  the improved mechanism is credited to the upgrade, not read back into the original claim.
- 2026-07-26 — **Stages S1–S3 (mini) executed; Report I shipped (`report/index.html`).**
  Verdicts: C1a refuted (E4) · C1b refuted (E4) · C1c holds-vacuously (E1) · C2a holds as
  suppression (E3, ours) · C2b refuted-as-stated (E2, TM3) · C2c retired · C3a holds in M1 ±ħ
  (E1/E2) · C3b holds — against C0 (E4/E2) · C3c refuted (E4/E2) · C4a split (E4) · C4b OPEN
  (chronology protection; E4) · C4c refuted — backfires (E1/E2, TM1) · C4d open (E2) · C5a repair
  · C5b refuted in studied models (E4/E2) · C5c holds-in-spirit (E3, TM5) · C6a holds in P-CTCs
  (E2/E4) · C6b holds as mechanism (E2/E4, TM6) · **C7: C0 does not follow as stated** — fails at
  C4c (Banach) and C5b (existence generic); survives as T1 (open) / T2 (supported) / T3
  (quantified at toy level). **No pre-registered lean flipped.** Corrections found by
  verification: (1) "P-CTCs = PP" re-attributed from Aaronson–Watrous to Lloyd et al. 2011 (via
  Aaronson 2005); (2) Devin arXiv:1302.3298 downgraded — arXiv-only, Maxwell's-demon-focused,
  cannot carry C2a. Sharpenings: EKT multiplicity is *infinite* for dangerous data ("far too many
  solutions"); EKT existence is a search finding, not a theorem; Lewis's "banana peel" is a later
  gloss; Hawking's "safe for historians" line exact wording documented (common variant misquotes
  it); C1b's checkable primary is Cramer–Forward–Morris–Visser–Benford–Landis 1995 (mechanism:
  Frolov–Novikov 1990), not Visser's book.
- 2026-07-26 — **Claim wording replaced at the claimant's direction.** The informal verbatim
  capture (with typos) was superseded by the canonical statement in §0 — spelling and grammar
  repaired, substance unchanged: every tested term (enthalpy, total energy, exact equality,
  infinite looping, the ∞-or-0 dichotomy) is retained, so no leaf verdict is affected. The freeze
  rule is henceforth "no drift in substance"; the superseded capture remains in git history.
- 2026-07-26 — **P1 executed ("The thermodynamic price of a consistent time loop") — Report II
  (`report2/`).** Pre-registered targets (commit `f039282`) all held; no falsifier fired. In the
  declared Markovian local-detailed-balance class with an ideal junction: **T1** closure
  probability decays monotonically to the Boltzmann weight of the loop state (E1/E2); **T2a
  sharpening** — undriven consistent loops have *exactly zero* entropy production (telescoping
  identity; all 2,187 enumerated loops at s = 0) — C2a's reversibility is an in-class identity,
  with the suppression carried entirely by closure cost; **T2b** driven conditional detailed FT
  verified to 3×10⁻¹⁴ across 6,561 loops, ⟨e^−s⟩_C = 1, ⟨s⟩_C ≥ 0; **C3** no pastward
  free-energy delivery except at e^{−ΔF/k_BT}; **T4** extensivity — one conspiratorial gram ⇒
  P ≈ 10^{−2.6×10²²} (TM5's scale now derived); **R5** Deutsch consistency gate-free at every
  coupling while record-level closure pays the classical price — the cost attaches to
  records/memory. Leaf upgrades: C2a E3 → E1/E2-in-model; C5c E3 → E1/E2-in-model (quantified).
  Novelty positioning: `docs/P1_NOVELTY.md` (3-agent adversarial scan).

## 9. Glossary

- **CTC (closed timelike curve):** a worldline through spacetime that returns to its own past — GR's
  formal object for "time travel to the past."
- **Chronology horizon:** the surface where CTCs first appear when a time machine forms; a type of
  Cauchy horizon.
- **Block universe:** the view (native to relativity) that past/present/future all exist as one 4-D
  structure; histories don't "change," they simply *are*.
- **State function:** a quantity determined by the current state alone (energy, entropy) — hence
  automatically equal whenever the state is the same.
- **Microstate vs macrostate:** the exact configuration vs the coarse description; entropy counts
  microstates per macrostate.
- **Fixed point:** x with F(x) = x; here, a self-consistent history.
- **Contraction mapping / Banach theorem:** if F shrinks distances (‖Λ‖ < 1), it has exactly one
  fixed point and iteration converges to it — stability, not fine-tuning.
- **Measure zero / almost all:** "probability-0-sized" subset with respect to a declared measure;
  "almost all" = complement of measure zero.
- **Novikov self-consistency principle:** the physically realized history on a CTC spacetime is
  globally self-consistent; you can be *in* the past but not *change* it.
- **Chronology protection conjecture (Hawking):** the laws of physics prevent time machines from
  forming — via diverging quantum vacuum stress at the chronology horizon.
- **D-CTC (Deutsch):** quantum CTC model demanding the loop's density matrix be a fixed point of
  the circuit; solutions always exist, sometimes many.
- **P-CTC (postselected CTC):** quantum CTC model via teleportation postselected on loop-output =
  loop-input; mismatched branches are projected out and renormalized — "cancellation" made formal.
- **Semiclassical gravity:** quantum fields on classical curved spacetime — the strongest tool we
  have short of quantum gravity; breaks down exactly at chronology horizons (KRW).
- **Exotic matter / energy conditions:** traversable wormholes need negative-energy-density matter,
  itself tightly constrained (quantum energy inequalities).
- **Fluctuation theorem:** modern sharpening of the second law: entropy-decreasing histories occur
  with probability suppressed as exp(−ΔS/k_B), never exactly zero.
- **Action (S):** a single number scoring an entire candidate history (for a particle, roughly
  ∫(kinetic − potential) dt). Classical law: the realized history makes S *stationary* (δS = 0).
- **Sum over histories (path integral):** the quantum rule — every conceivable history contributes
  an amplitude e^{iS/ħ}; add them all, and interference does the selecting.
- **Stationary phase:** near a stationary-action history, neighboring histories agree in phase and
  reinforce; elsewhere the phases spin and neighbors cancel. Fermat's least-time principle for
  light is the optics special case ("shortest" is really "stationary").
- **Noether's theorem:** every continuous symmetry of the action yields a conservation law
  (time-translation symmetry ⇒ energy conservation) — and where the symmetry is absent, so is the
  law.

## 10. References (ALL `[v?]` until Stage 1 verifies; confidence H/M/L that the reference is correctly recalled)

- Gödel (1949), rotating-universe solution with CTCs — H
- Lewis (1976), "The Paradoxes of Time Travel," *Am. Phil. Quarterly* — H
- Morris, Thorne & Yurtsever (1988), wormholes/time machines/WEC, *PRL* — H
- Friedman, Morris, Novikov, Echeverria, Klinkhammer, Thorne, Yurtsever (1990), "Cauchy problem in
  spacetimes with closed timelike curves," *Phys. Rev. D* ("the Consortium paper") — H
- Echeverria, Klinkhammer & Thorne (1991), billiard balls in wormhole spacetimes, *Phys. Rev. D* — M/H
- Kim & Thorne (1991), vacuum polarization at chronology horizons, *Phys. Rev. D* — M/H
- Deutsch (1991), "Quantum mechanics near closed timelike lines," *Phys. Rev. D* — H
- Hawking (1992), "Chronology protection conjecture," *Phys. Rev. D* — H
- Politzer (1992), path integrals with CTCs, *Phys. Rev. D* — M
- Carlini, Frolov, Mensky, Novikov & Soleng (1995), self-consistency from least action, *IJMPD* — M
- Kay, Radzikowski & Wald (1997), QFT at compactly generated Cauchy horizons, *Comm. Math. Phys.* — M/H
- Visser (1995), *Lorentzian Wormholes: From Einstein to Hawking* (book) — H
- Ford & Roman (mid-1990s), quantum energy inequalities — M
- Ori (2005–07), time-machine models with non-compactly generated horizons — M
- Krasnikov (1990s–2000s), counterexample spacetimes to chronology-protection formulations — M
- Aaronson & Watrous (2009), CTCs make classical and quantum computing equivalent (PSPACE), *Proc. R. Soc. A* — H
- Lloyd et al. (2011), P-CTCs: theory + photonic test, *PRL* / *PRD* — M/H
- Ringbauer et al. (2014), experimental *simulation* of D-CTCs, *Nat. Commun.* — M
- Devin (~2013), thermodynamics of time machines, arXiv — L/M
- Feynman & Hibbs (1965), *Quantum Mechanics and Path Integrals* — H
- Feynman (1985), *QED: The Strange Theory of Light and Matter* (the phase-arrows demo; best
  on-ramp for C6b) — H
- Noether (1918), invariant variational problems (conservation ⇔ symmetry) — H
- Hartle (1994), generalized quantum mechanics for nonchronal spacetimes, *Phys. Rev. D* — M
- Friedman, Papastamatiou & Simon (1992), failure of unitarity for interacting fields on CTC
  spacetimes, *Phys. Rev. D* — M
- Wald (1984), *General Relativity* (energy in GR) — H
- Carroll (2010), "Energy is not conserved" (pedagogical blog) — M/H
- Smeenk & Wüthrich / Arntzenius & Maudlin, SEP entries on time travel — M/H (best newcomer on-ramp)
