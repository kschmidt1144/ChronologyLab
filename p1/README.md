# P1 — computational checks for "The thermodynamic price of a consistent time loop"

Targets and falsifiers are pre-registered in `../docs/P1_TARGET.md` (committed before these ran).
Run: `uv run --with numpy --with matplotlib python p1/run_all.py` → `p1/out/*.svg` +
`p1/out/results.json`.

## Pre-registered can/cannot preambles

- **E1 (two-state closure cost → T1).** CAN: verify, exactly and analytically, that loop-closure
  probability decays monotonically to the Boltzmann weight of the loop state, with the relaxation
  time setting the crossover ("short hops cheap, long loops pay full price"). CANNOT: say
  anything about spacetime dynamics — the loop is a boundary condition, not a metric.
- **E2 (exact path enumeration → T2).** CAN: check the conditional detailed fluctuation theorem
  bin-by-bin against every periodic path of a small chain — a consistency check of the derivation
  chain (the path-ratio identity is definitional in stochastic thermodynamics; the corollaries
  ⟨s⟩_C ≥ 0 and the tail bound are the content). CANNOT: establish the theorem beyond Markovian
  detailed-balance dynamics.
- **E3 (extensivity → T4).** CAN: show the exponential-in-N price for independent components and
  anchor Report I's per-gram number as a derived instance. CANNOT: treat interacting components
  (stated as an open extension).
- **E4 (quantum contrast → T5).** CAN: show numerically that Deutsch density-matrix consistency
  is satisfiable at every tested coupling (no thermodynamic gate) while pointer/record-level
  closure decays to the Boltzmann floor — locating the price on records, not on the loop.
  CANNOT: decide which consistency notion nature uses.
