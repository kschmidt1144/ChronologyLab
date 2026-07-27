# P1 adversarial novelty scan — prior-art dossier

Three research agents were tasked to **refute the novelty** of the pre-registered P1 targets
(`P1_TARGET.md`) before we invested in them. Method: forward-citation walks, INSPIRE/arXiv/
Semantic Scholar/PhilPapers sweeps, full-text reads where accessible; every item below carries an
explicit preemption judgment. Scan date: 2026-07-26.

## Verdict (consolidated)

**Not preempted at theorem level — but not virgin ground.** The planned results sit at the
unoccupied intersection of three occupied neighborhoods, and the correct framing is:
*the missing quantitative layer beneath Horwich (1987), Lossev–Novikov (1992), Rovelli (2019),
Devin (2013), and Gavassino (2025) — executing the typicality-measure strategy that Smeenk &
Wüthrich (2011) floated and declared undelivered.* No retrieved work states or proves any of: closure
probability = return probability with monotone decay to the Boltzmann measure of the loop state
(T1); a fluctuation theorem conditioned on loop closure (T2); the e^{−ΔF/k_BT} bound on pastward
free-energy delivery (C3); extensivity of the consistency cost in explicit Markov models (T4);
or the Deutsch-vs-record cost dichotomy as a demonstrated result (R5).

Structural negative evidence: an INSPIRE abstract query for "closed timelike" AND "second law"
returns **zero records**; Devin's preprint — the unique prior attempt at pricing time-machine
reliability thermodynamically — has only self-citations thirteen years on; targeted sweeps for
"fluctuation theorem" × CTC, "Jarzynski/Crooks" × CTC, "Landauer" × CTC returned nothing
combining stochastic thermodynamics with Novikov consistency.

## 1. Physics prior art (agent 1)

| Work | What it actually does | Preempts? |
|---|---|---|
| **Devin, arXiv:1302.3298 (2013)** — closest prior art | Qubit time machine with bit-error rate k; work extraction bounded by −ln k; assembly scaling k_eff = k^N; "exponentially difficult" rhetoric for tourists. No stochastic models, no FT, no closure=return theorem, Deutsch dismissed. Only self-citations. | **Partially** — germs of T3/T4; must be cited and explicitly superseded |
| **Rovelli, arXiv:1912.04702 (2019)** | Essay-level: dS/dτ ≥ 0 around a loop forces dS/dτ = 0; no records/memory survive a CTC; travel to the past "extremely improbable." No formula, model, or exponent. | **Partially** — states T1/T2a's qualitative punchline; zero quantification. Also anticipates Report I's memory corollary (credit adjusted in the ledger) |
| **Gavassino, CQG 42, 015002 (2025), arXiv:2405.18640** | Exact quantum kinematics on a CTC: energy levels discretize, every system returns exactly, memories erased via recurrence. Consistency enforced, never priced. | **Partially** — adjacent ground by a different mechanism; no measure, no FT |
| **Bartkiewicz, Grudka, Horodecki, Łodyga, Wychowaniec, PRA 99, 022304 (2019)** | D-CTC/P-CTC circuits that *decrease* entropy — the exploit genre; consistency assumed free. | No — mandatory contrast citation |
| **Lloyd et al., PRL 106, 040403 (2011)** | P-CTC postselection; amplitude-level suppression of paradox; no thermodynamic scale. | No |
| **Cassidy & Hawking, PRD 57, 2372 (1998)** | Partition-function argument that the number of states → 0 as a spacetime approaches CTC formation — entropy suppresses *forming* the machine, not closing a given loop. | No — genealogy for "entropy suppresses acausality" |
| **Carlini et al., IJMPD 4, 557 (1995); Mikheeva & Novikov, PRD 47, 1432 (1993)** | Consistency from least action; inelastic (dissipative) billiard still admits consistent solutions. Existence, never probability. | No |
| **Deutsch, PRD 44, 3197 (1991)** | Fixed points always exist; max-entropy selection. "Deutsch consistency is cost-free" is folklore — R5's novelty burden sits on the record-level price. | Partially (R5's first half only) |
| Song & Zhang arXiv:2512.03380; Taylor UJC (2015); Schulman two-time boundaries; conditioned-FT toolbox papers | Adjacent motivation or tools; none applied to loop closure. | No |

## 2. Philosophy prior art (agent 2)

| Work | What it actually does | Preempts? |
|---|---|---|
| **Horwich 1987 (Asymmetries in Time, ch. 7; restated 1995)** | The improbability/coincidences argument — purely qualitative-inductive; "a rash of coincidences would apparently not violate any law" (Sider's restatement). | No — conceptual ancestor |
| **Black 1956; Dummett 1964** | The bilking lineage; qualitative. | No |
| **Smith 1997 (BJPS); Dowe 2003; Sider 2002; Vihvelin 1996; Ismael 2003; Riggs 1997** | The debate over Horwich — all sides argue with informal probability only. | No |
| **Smeenk & Wüthrich 2011 (Oxford Handbook), §2.2** | Poses the measure problem explicitly ("we should be in the position to define an adequate event space with a principled, well-defined measure"), records Callender's Liouville/typicality suggestion in a footnote, and concludes the construction does not exist and "we are at a loss." | **Partially — and the key positioning citation: affirmative documentary evidence of the gap P1 fills** |
| **Arntzenius 2006 (Phil. Compass)** | Single qualitative sentence: someone on a loop "can not have a continuously increasing entropy"; deflationary about improbability arguments. | Partially — one seed sentence, nothing derived |
| **Mellor 1998 / Berkovitz 2001** | Chance/frequency calculus on causal loops — most formal probability neighbor; no entropy, no Boltzmann. | No |
| **Wasserman 2018 ch. 4; Effingham 2020; Kutach 2003; Frisch 2010; SEP entries** | No statistical mechanics anywhere; SEP "Time Travel and Modern Physics" rejects the coincidences objection qualitatively. | No |

Residual risk (agent 2): Horwich 1975 full text, Wasserman ch. 4 §3 body, and Effingham 2020 were
verified only via reviews/secondary restatements — none shows any hint of statistical mechanics,
but exact wording was not fully inspected.

## 3. Novikov-school scan

*Status note:* the deep-archive agent ran long; its single highest-risk item (Lossev–Novikov's
"Jinn") was therefore **verified directly in-session** (IOP abstract, verbatim) and is included
below; the agent's full return is appended on completion, and any material change would be folded
into Report II via a documented amendment commit.

| Work | What it actually does | Preempts? |
|---|---|---|
| **Lossev & Novikov, "The Jinn of the time machine: nontrivial self-consistent solutions," CQG 9, 2309 (1992)** — abstract verified verbatim | Hypothesizes objects with closed worldlines ("Jinn") and identifies their thermodynamic maintenance requirement: "These systems are possible only if they can, by interacting with external objects, gain energy to regenerate their internal structure." Qualitative; no probabilities, no measure, no fluctuation relations. | **Partially** — names the free-energy regeneration requirement of closed worldlines; P1's T1/C3 supply its price (closure measure e^{−ΔF/k_BT}) |
| Carlini, Frolov, Mensky, Novikov & Soleng 1995; Mikheeva & Novikov 1993 (covered in scan 1) | Consistency from least action; dissipative billiard still admits consistent solutions — existence, never probability. | No |

## Positioning obligations for the write-up

1. Cite Devin 2013 prominently and state exactly what it did (−ln k bound; k^N) and did not do.
2. Frame T1's headline as the first *fluctuation-theorem-grade quantification* of claims made
   qualitatively by Horwich 1987 / Rovelli 2019 — never as a brand-new idea.
3. Cite Smeenk & Wüthrich 2011 §2.2 as the documented statement of the gap; note that P1 executes
   (in a tractable model class) the typicality strategy their fn. 11 floats and drops.
4. Credit-adjust Report I's memory corollary to Rovelli 2019 (done — ledger CHANGELOG + erratum).
5. Cite Gavassino 2025 and Bartkiewicz et al. 2019 as the nearest quantum-side neighbors, and
   Mikheeva–Novikov 1993 for dissipative-consistency existence.
