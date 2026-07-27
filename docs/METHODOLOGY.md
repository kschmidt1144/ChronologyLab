# Methodology — how this investigation is run (and why)

Written for a first formal research project. Each section explains a move we make in
`CLAIMS.md`, why professionals make it, and the failure mode it prevents.

---

## 1. What kind of question is this?

The first methodological act is classifying the claim, because the *standard of proof* depends on
the class:

- **Empirical claims** ("this drug lowers blood pressure") are settled by experiment and
  statistics.
- **Mathematical claims** ("there are infinitely many primes") are settled by proof from axioms.
- **Theoretical-physics claims** ("time machines self-destruct") sit in between: no experiment can
  reach them today, so they are settled — to the extent they can be — by **derivation within a
  stated framework** (general relativity, semiclassical gravity, quantum-information models),
  plus consistency arguments across frameworks.

Consequence: **every verdict in this project is conditional** ("within semiclassical gravity, X").
That is not a weakness of our project; it is the actual epistemic situation of the field. Black
hole thermodynamics ran this way for 40+ years before any observation touched it. A leaf that ends
"open — requires quantum gravity" is a *result*, and an important one: knowing precisely where the
knowable ends is much of what a literature has to offer.

Corollary: "prove" here means *derive from stated assumptions*; "disprove" means *exhibit a
counterexample or expose an invalid inference step*. Nothing will be "proved about reality"
absolutely. We say so up front to calibrate expectations.

## 2. The claims-ledger method

A compound claim ("almost all time travel is impossible **because** energy books must balance
**and** loops amplify mismatches") cannot be evaluated wholesale — a single true/false hides which
part did the work and which part failed. The method:

1. **Freeze the original.** Quote it verbatim, typos and all, and never edit it. The thing under
   test must not drift.
2. **Steelman with a logged diff.** Repair category errors and ambiguities *in the strongest
   direction for the claim*, and log every repair with a reason (our `CLAIMS.md §2 A4`). Why: if
   we attack a weak reading, refuting it is worthless ("straw man"); if we silently strengthen it,
   we may later "prove" something nobody claimed ("motte-and-bailey"). The log keeps us honest in
   both directions.
3. **Operationalize.** Replace every vague term with a formal object (see §3).
4. **Decompose to leaves.** Each leaf states *one* proposition that could be defended or denied on
   its own. Test: if you can't imagine two competent people disagreeing about a leaf *while
   agreeing about the others*, it isn't yet atomic — split further.
5. **Assign each leaf a test route and a falsifier** — *in advance* (see §5).
6. **Gather evidence per leaf** (literature first, then our own derivations and toy models).
7. **Reassemble with an explicit inference audit** (our C7): the root claim is a logical function
   of the leaves; write that function down and check whether the leaf verdicts actually compose
   into the root verdict. Arguments usually die here — every *step* is plausible but the
   *composition* is invalid (our C4c is exactly such a break).

## 3. Operationalization — making terms truth-apt

A claim containing an undefined term is not yet true *or* false — it is unready. Examples from this
project:

- "the state of the universe when time returns" → splits three ways depending on the model of time
  travel (M1 single history / M2 branching / M3 mutable + meta-time). The claim's meaning is
  **model-relative**; some disputes dissolve into "depends on which model, which is empirically
  open." Recognizing dissolution *is* progress.
- "almost all" → meaningless without a **measure** ("almost all real numbers are irrational" is
  precise because Lebesgue measure is declared). We require every "almost all" verdict to name its
  measure (C5a).
- "cancelled out" → three inequivalent formalizations (not-a-solution / destructive interference /
  postselection), each living in a different framework (C6).

Rule of practice: when you meet a vague term, do not argue about it — *list its candidate
formalizations and carry them separately*. Half of all apparent disagreements evaporate.

## 4. Evidence standards (the E-scale)

Every verdict carries a tag for *how* it is supported, in descending strength:

- **E1 — theorem** within a stated framework (proof we can check).
- **E2 — explicit computation** in a fully specified model (including our toys; reproducible).
- **E3 — controlled heuristic**: dimensional analysis, limiting cases, structural arguments —
  persuasive, not binding.
- **E4 — literature/consensus**: "the field's results say X" — only as good as our reading; every
  E4 claim carries `[v?]` until Stage 1 checks the primary source.
- **E5 — intuition/plausibility.** Allowed as a *lean*, never as a verdict.

A leaf "settled" at E5 is not settled. The point of Stages 1–3 is to push leaves up this ladder or
discover they won't go.

## 5. Pre-registration: leans and falsifiers, recorded before testing

Borrowed from experimental science's answer to hindsight bias. We record, *now*:

- a **lean** per leaf (what we currently expect, and at what E-level), and
- a **falsifier** per leaf (what concrete finding would flip it).

Why: after reading persuasive papers, everyone believes they "always basically thought that."
The pre-registered lean makes belief-change *visible* — and belief-change is the signal. If the
evidence moves us, that's the project working; if nothing could move us, we were never doing
research. Surprises get logged in the CHANGELOG with special prominence.

Meta-note for this project: the Stage-0 leans were drafted with an AI research assistant whose
training data includes this literature — so the leans are already literature-flavored (E4-ish),
not naive. The discipline still applies: Stage 1 verifies against primary sources, and any lean
the sources contradict gets flipped loudly, not quietly.

## 6. Literature protocol

1. **On-ramps before primaries** (for orientation): the Stanford Encyclopedia of Philosophy
   entries on time travel; Visser's *Lorentzian Wormholes*; Thorne's popular *Black Holes and
   Time Warps*. These give the map; they are not citable evidence for leaf verdicts.
2. **Primary sources for load-bearing claims.** Any leaf verdict resting on "paper X showed Y"
   requires the actual paper, with the supporting passage located (page/equation), quoted into the
   ledger. Until then the citation stays `[v?]`.
3. **Disagreements are first-class objects.** Kim–Thorne vs Hawking on whether the divergence
   destroys the machine is not noise to be averaged away — it is the *content* of the open
   problem. We record who disagrees with whom and on what premise.
4. **Citation hygiene.** Author-year recalled from memory is a *pointer*, not a fact. Verify
   existence, venue, and — most importantly — that the paper actually says what we're citing it
   for. (Papers are routinely cited for things they don't quite say; checking is rare and cheap.)

## 7. Toy-model protocol

When experiments are impossible, small explicit models are the workhorse. Their epistemic power is
asymmetric, and we state it per toy (see `CLAIMS.md §6`):

- A toy **CAN refute a universal claim.** "ANY mismatch is driven to ∞ or 0" is refuted by one
  explicit counterexample map, even an unphysical one — universality was the claim's force, so one
  counterexample kills the universal version and forces a retreat to "which regime is physical?"
- A toy **CAN demonstrate a mechanism is coherent** (P-CTC cancellation actually works end-to-end
  on qubits).
- A toy **CANNOT establish facts about our universe.** Showing a contracting loop map behaves
  nicely does not show real spacetime loops contract.

Each toy ships with: target leaves, assumptions, and an explicit can/cannot preamble — written
*before* the toy is run (pre-registration again).

## 8. Reassembly: the inference audit

At the end we return to the root. Concretely, we write the root as a function of leaves, e.g.:

> C0 ⇐ C3a (only exact matches allowed) ∧ [C4b ∧ C4c] (both amplification horns eliminate) ∧ C5b
> (survivors are measure-zero)

and check each conjunct's verdict. Already visible at Stage 0: C4c likely fails (the damping horn
*stabilizes* time travel), and C5b currently leans the wrong way in every studied model — so C0 as
stated is expected to fail *even if* its spirit substantially survives as T1/T2/T3. The final
deliverable is a **conditional verdict table**: for each (framework × travel model), which refined
theses hold, and exactly how much of the original claim survives. "Your claim is false as stated
but its mechanism is the field's leading conjecture" is a perfectly good research outcome — far
better than a bare true/false.

## 9. Honesty rails

- **Against-us evidence is displayed prominently**, not buried (see `CLAIMS.md §4`). A conclusion
  that has never stared its best counterevidence in the face is worthless.
- **Verdicts move only with a CHANGELOG entry** naming the evidence. No silent drift.
- **Provenance labels** on every statement: *verified* (we checked the primary) / *derived* (our
  own math, shown) / *reported* (someone says so — cite) / *conjectured* (ours, flagged). The
  reader must always be able to tell which they're getting.
- **The measure of success is calibration, not vindication.** If the claim dies, the project
  succeeded. If it survives refined, the project succeeded. The only failure is an unfalsifiable
  shrug.

## 10. Working conventions

- All edits to leaf statuses happen in `CLAIMS.md`; discussion lives in flow updates
  (Orchestrator) and, later, per-stage notes under `docs/`.
- Citations: `[v?]` until verified; then replaced by a full reference with a located quote.
- Code (Stage 2+): Python via `uv`, one directory per toy under `toys/`, each with a README
  stating target leaves + can/cannot.
