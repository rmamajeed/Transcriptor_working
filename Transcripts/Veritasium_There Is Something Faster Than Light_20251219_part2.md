---
title: Veritasium_There Is Something Faster Than Light_20251219_part2
audio_file: Veritasium_There Is Something Faster Than Light_20251219_part2.mp3
note_id: 2722c777-b115-4572-9f5b-a63b467e97fa
date_processed: '2026-01-06'
classification:
  primary_domain: Physics
  sub_domains:
  - Quantum Mechanics
  - Foundations of Physics
  - Experimental Physics
  difficulty_level: Intermediate
  content_type: Lecture
entities:
  people:
  - name: Alain Aspect
    role: Experimental physicist
    contribution: Performed the seminal Bell‑inequality experiments 40 years ago,
      demonstrating violation of local hidden‑variable predictions.
  - name: John Bell
    role: Theoretical physicist
    contribution: Formulated Bell's theorem, showing that quantum mechanics and local
      hidden‑variable theories make different statistical predictions.
  works_cited:
  - title: Bell's theorem
    author: John Bell
    year: 1964
  - title: Aspect's experiment on Bell inequalities
    author: Alain Aspect
    year: 1982
  concepts_mentioned:
  - Disagreement rate
  - Bell's inequality
  - Quantum mechanics (Copenhagen interpretation)
  - Local hidden variable theory
  - Entangled photons
  - Polarizers
  - Stern–Gerlach experiment
  - Non‑locality
concepts:
- name: Bell's inequality
  definition: A mathematical inequality that any local hidden‑variable theory must
    satisfy, but which quantum mechanics can violate.
  parent_concepts:
  - Foundations of Physics
  related_concepts:
  - Local hidden variable theory
  - Quantum mechanics
  - Entanglement
  - Disagreement rate
  abstraction_level: Theoretical
  confidence: 0.98
- name: Disagreement rate
  definition: The proportion of measurement outcomes that differ when two observers
    choose different measurement axes on entangled particles.
  parent_concepts:
  - Experimental Physics
  related_concepts:
  - Bell's inequality
  - Quantum mechanics
  - Local hidden variable theory
  abstraction_level: Fundamental
  confidence: 0.97
- name: Local hidden variable theory
  definition: A class of theories that assume measurement outcomes are predetermined
    by hidden variables that do not allow instantaneous (non‑local) influences.
  parent_concepts:
  - Foundations of Physics
  related_concepts:
  - Bell's inequality
  - Non‑locality
  - Disagreement rate
  abstraction_level: Theoretical
  confidence: 0.96
- name: Quantum mechanics (Copenhagen interpretation)
  definition: The standard formulation of quantum theory that treats measurement outcomes
    as intrinsically probabilistic and allows non‑local correlations.
  parent_concepts:
  - Quantum Mechanics
  related_concepts:
  - Bell's inequality
  - Entanglement
  - Disagreement rate
  - Non‑locality
  abstraction_level: Fundamental
  confidence: 0.99
- name: Entangled photons
  definition: Pairs of photons whose quantum states are correlated such that the measurement
    outcome of one instantly determines the outcome of the other, regardless of distance.
  parent_concepts:
  - Quantum Mechanics
  related_concepts:
  - Bell's inequality
  - Polarizers
  - Disagreement rate
  abstraction_level: Applied
  confidence: 0.95
relationships:
- source_concept: Quantum mechanics (Copenhagen interpretation)
  target_concept: Disagreement rate
  relationship_type: predicts
  strength: 0.96
  evidence: The transcript states quantum mechanics predicts a disagreement rate of
    25% when different axes are measured.
  reasoning: Quantum theory yields the 25% figure, directly linking the theory to
    the observed statistical rate.
- source_concept: Local hidden variable theory
  target_concept: Disagreement rate
  relationship_type: predicts
  strength: 0.94
  evidence: The transcript notes local hidden variables predict disagreement at least
    33% of the time.
  reasoning: Local hidden‑variable models necessarily give a higher disagreement probability,
    contrasting with quantum predictions.
- source_concept: Bell's inequality
  target_concept: Disagreement rate
  relationship_type: relates_to
  strength: 0.97
  evidence: Bell's proof shows different predictions for disagreement rates (25% vs
    ≥33%).
  reasoning: The inequality provides the quantitative test distinguishing the two
    theoretical predictions.
- source_concept: Entangled photons
  target_concept: Bell's inequality
  relationship_type: applies_to
  strength: 0.95
  evidence: The experiment described uses entangled photon pairs to test Bell's inequalities.
  reasoning: Entangled photons are the physical system used to realize the statistical
    tests derived from Bell's inequality.
- source_concept: Local hidden variable theory
  target_concept: Non‑locality
  relationship_type: contradicts
  strength: 0.92
  evidence: Local hidden variables assume no instantaneous influences, whereas quantum
    mechanics (and Bell violations) imply non‑locality.
  reasoning: The two frameworks are mutually exclusive regarding the presence of non‑local
    effects.
cross_domain_insights:
- connection_type: structural_analogy|principle_application
  source_domain: Physics
  source_concept: Bell's inequality
  target_domain: Finance / Economics
  target_concept: No‑arbitrage bounds on correlated asset prices
  insight: Bell's inequality limits the strength of correlations that any local hidden‑variable
    model can produce, just as no‑arbitrage principles bound the joint pricing of
    correlated securities.
  explanation: Both frameworks derive linear inequalities that any admissible joint
    probability distribution must satisfy. Violations signal the need for a richer,
    non‑classical model (quantum entanglement in physics, market frictions or hidden
    systemic risk in finance).
  potential_applications:
  - Design of stress‑testing frameworks that detect hidden systemic risk
  - Development of quantum‑inspired pricing algorithms that incorporate non‑local
    correlation structures
  confidence: 0.86
  historical_example: The 1973 Black–Scholes model introduced risk‑neutral pricing
    constraints analogous to Bell‑type inequalities for derivative markets.
- connection_type: structural_analogy|principle_application
  source_domain: Physics
  source_concept: Disagreement rate (Bell‑test violation probability)
  target_domain: Communication Engineering
  target_concept: Bit error rate (BER) in noisy channels
  insight: The disagreement rate quantifies how often measurement outcomes differ
    from local‑realist predictions, mirroring how BER measures the frequency of bit
    flips caused by channel noise.
  explanation: Both are statistical error metrics derived from repeated binary trials;
    reducing the disagreement rate in a Bell test is mathematically equivalent to
    improving signal‑to‑noise ratio in a communication link.
  potential_applications:
  - Applying error‑correction codes to improve Bell‑test fidelity
  - Using quantum‑enhanced detection methods to lower BER in classical communication
  confidence: 0.92
  historical_example: Shannon's 1948 channel capacity theorem formalized error rates,
    a concept later imported into quantum information theory for analyzing Bell‑test
    efficiencies.
- connection_type: structural_analogy|principle_application|historical_precedent
  source_domain: Physics
  source_concept: Local hidden variable theory
  target_domain: Computational Biology
  target_concept: Hidden Markov models (HMMs) for latent biological states
  insight: Local hidden variables act as unseen parameters that determine observable
    outcomes, just as HMMs posit unobserved states that generate observable sequences
    of biological data.
  explanation: Both frameworks use a probabilistic mapping from hidden variables to
    measurable results, and inference techniques (e.g., Bayesian updating) are employed
    to estimate the hidden parameters from data.
  potential_applications:
  - Adapting quantum‑inspired inference algorithms to improve HMM parameter estimation
  - Using Bell‑type statistical tests to assess the adequacy of hidden‑state models
    in genomics
  confidence: 0.81
  historical_example: The Viterbi algorithm (1967) for decoding HMMs was later mirrored
    in quantum error‑correction decoding schemes that also infer hidden error syndromes.
- connection_type: metaphor|principle_application
  source_domain: Physics
  source_concept: Entangled photons
  target_domain: Computer Science / Distributed Systems
  target_concept: Byzantine fault‑tolerant consensus and shared secret keys
  insight: Entanglement provides correlations that are instantly consistent across
    distance, analogous to how Byzantine consensus protocols maintain a consistent
    system state despite malicious participants, and how quantum key distribution
    supplies a shared secret without prior exchange.
  explanation: Both rely on establishing a resource that cannot be duplicated or forged
    (no‑cloning theorem vs. impossibility of forging a consensus without majority
    agreement), ensuring coordinated outcomes despite adversarial conditions.
  potential_applications:
  - Designing quantum‑enhanced consensus algorithms for blockchain networks
  - Leveraging entanglement‑based randomness to strengthen cryptographic protocols
  confidence: 0.88
  historical_example: The 1999 Paxos algorithm formalized consensus under failures;
    a decade later, quantum key distribution (BB84) demonstrated a practical non‑replicable
    secret sharing mechanism.
bridge_concepts:
- concept: Correlation
  appears_in_domains:
  - Physics
  - Finance
  - Epidemiology
  - Network Science
  role: Serves as the quantitative link that constraints joint outcomes in both quantum
    experiments and market or disease models.
  examples:
  - Bell‑inequality violations show stronger-than‑classical correlations.
  - Correlation matrices are used to price multi‑asset derivatives.
  - Cross‑correlation of infection curves guides public‑health interventions.
- concept: Probability
  appears_in_domains:
  - Physics
  - Statistics
  - Computer Science
  - Philosophy
  role: Underlying language for describing uncertainty, measurement outcomes, and
    decision making across domains.
  examples:
  - Quantum probability amplitudes vs. classical probabilities.
  - Bayesian inference in medical diagnosis.
  - Probabilistic algorithms in randomized computing.
- concept: Measurement
  appears_in_domains:
  - Physics
  - Psychology
  - Engineering
  - Economics
  role: Acts as the interface where theoretical models confront observable data, often
    collapsing possibilities into a single outcome.
  examples:
  - Copenhagen interpretation’s wave‑function collapse upon measurement.
  - Survey instruments translating latent attitudes into scores.
  - Sensors converting physical signals into digital readings.
- concept: Non‑locality
  appears_in_domains:
  - Physics
  - Computer Networks
  - Social Sciences
  role: Describes influence or information transfer that bypasses traditional locality
    constraints.
  examples:
  - Entangled photons exhibiting instantaneous correlations.
  - Content delivery networks serving data from distant caches without latency penalties.
  - Social media memes spreading globally independent of geographic proximity.
mental_models:
- name: First‑Principles Reasoning
  description: Decompose a problem to its most fundamental laws or axioms and rebuild
    solutions from the ground up.
  applied_to:
  - Deriving Bell’s inequality from locality and realism assumptions.
  transferable_to:
  - Designing novel materials by starting from atomic interactions
  - Strategic business planning by questioning underlying market assumptions
- name: Statistical Correlation Constraints
  description: Use linear inequalities that any admissible joint probability distribution
    must satisfy.
  applied_to:
  - Testing local hidden‑variable theories with Bell‑type inequalities.
  transferable_to:
  - Ensuring consistency of multi‑variable risk models in insurance
  - Validating causal inference models in epidemiology
- name: Adversarial Game Theory
  description: Model experiments as games between a verifier and a potential cheater,
    focusing on strategies that expose hidden cheating.
  applied_to:
  - Bell‑test protocols where the ‘hidden variable’ tries to mimic quantum predictions.
  transferable_to:
  - Security auditing of cryptographic protocols
  - Design of robust AI alignment tests
- name: Information‑Theoretic Resource Accounting
  description: Treat entanglement, entropy, or bandwidth as quantifiable resources
    that can be consumed, transformed, or conserved.
  applied_to:
  - Quantifying entanglement as a consumable resource for quantum teleportation.
  transferable_to:
  - Managing data‑center energy budgets
  - Analyzing ecological energy flow in ecosystems
analogies_used:
- source_domain: Everyday Life
  source_concept: Matching socks in a drawer
  target_domain: Physics
  target_concept: Bell's inequality and entangled photon correlations
  mapping:
    Sock pair: Entangled photon pair
    Color pattern: Measurement outcome (±1)
    Random drawer pull: Random measurement setting
  pedagogical_value: Illustrates how predetermined properties (hidden colors) cannot
    reproduce the observed statistics without violating the inequality, making the
    abstract quantum correlation tangible.
- source_domain: Computer Networking
  source_concept: Synchronized clocks for packet timestamps
  target_domain: Physics
  target_concept: Copenhagen interpretation’s measurement collapse
  mapping:
    Clock sync: Shared measurement basis
    Timestamp: Observed outcome
    Network latency: Quantum decoherence
  pedagogical_value: Helps learners see measurement as a process that aligns a system
    with an external reference, collapsing many possibilities into a single recorded
    event.
tags:
  hierarchical:
  - '#Physics → #Quantum Mechanics → #Bell''s Inequality → #Disagreement Rate'
  - '#Physics → #Foundations of Physics → #Local Hidden Variable Theory'
  - '#Physics → #Experimental Physics → #Entangled Photons → #Polarizers'
  topical:
  - '#BellInequality'
  - '#QuantumMechanics'
  - '#LocalHiddenVariables'
  - '#Entanglement'
  - '#NonLocality'
  - '#DisagreementRate'
  methodological:
  - '#ThoughtExperiment'
  - '#Derivation'
  - '#Experiment'
  people:
  - '#AlainAspect'
  - '#JohnBell'
  concepts:
  - '#BellInequality'
  - '#DisagreementRate'
  - '#LocalHiddenVariableTheory'
  - '#QuantumMechanics'
  - '#EntangledPhotons'
  temporal:
  - '#1970s'
  - '#2000s'
summary: ''
key_ideas: []
---
## Key Concepts

**Bell's inequality**  
A mathematical inequality that any local hidden‑variable theory must satisfy, but which quantum mechanics can violate.

**Disagreement rate**  
The proportion of measurement outcomes that differ when two observers choose different measurement axes on entangled particles.

**Local hidden variable theory**  
A class of theories that assume measurement outcomes are predetermined by hidden variables that do not allow instantaneous (non‑local) influences.

**Quantum mechanics (Copenhagen interpretation)**  
The standard formulation of quantum theory that treats measurement outcomes as intrinsically probabilistic and allows non‑local correlations.

**Entangled photons**  
Pairs of photons whose quantum states are correlated such that the measurement outcome of one instantly determines the outcome of the other, regardless of distance.

## Cross-Domain Connections

**Physics → Finance / Economics**

*Bell's inequality limits the strength of correlations that any local hidden‑variable model can produce, just as no‑arbitrage principles bound the joint pricing of correlated securities.*

Both frameworks derive linear inequalities that any admissible joint probability distribution must satisfy. Violations signal the need for a richer, non‑classical model (quantum entanglement in physics, market frictions or hidden systemic risk in finance).

**Physics → Communication Engineering**

*The disagreement rate quantifies how often measurement outcomes differ from local‑realist predictions, mirroring how BER measures the frequency of bit flips caused by channel noise.*

Both are statistical error metrics derived from repeated binary trials; reducing the disagreement rate in a Bell test is mathematically equivalent to improving signal‑to‑noise ratio in a communication link.

**Physics → Computational Biology**

*Local hidden variables act as unseen parameters that determine observable outcomes, just as HMMs posit unobserved states that generate observable sequences of biological data.*

Both frameworks use a probabilistic mapping from hidden variables to measurable results, and inference techniques (e.g., Bayesian updating) are employed to estimate the hidden parameters from data.

## Full Transcription



[ 0m0s694ms - 0m7s744ms ] Speaker 1: Disagreement rate is 25%. And we can show that for any two different axes the experimenters select, the geometry is analogous. So, they all have the same disagreement rate of 25%.
[ 0m7s744ms - 0m14s314ms ] Speaker 1: Anytime the experimenters choose different axes, they will get the same outcome 75% of the time, and different outcomes 25% of the time.
[ 0m15s264ms - 0m18s244ms ] Speaker 2: Now, let's consider the local hidden variable alternative theory.
[ 0m18s244ms - 0m20s54ms ] Speaker 2: The particles here are on a mission.
[ 0m20s54ms - 0m27s364ms ] Speaker 2: Their aim to make you believe that they're acting according to quantum mechanics when really they're acting locally.
[ 0m27s714ms - 0m30s304ms ] Speaker 2: Now, we are anthropomorphizing, but I think it is really useful to just imagine them this way.
[ 0m30s534ms - 0m36s984ms ] Speaker 2: We're trying to figure out if it's always possible for them to use a hidden variable theory to get the same experimental outcomes as Copenhagen quantum mechanics.
[ 0m37s204ms - 0m41s54ms ] Speaker 2: Or, if in this new situation, our scheming particles won't be able to fool us.
[ 0m41s594ms - 0m43s54ms ] Speaker 2: You can think of it like this.
[ 0m44s304ms - 0m50s674ms ] Speaker 2: Each of the particles is going to be asked one of three possible questions, and they need to decide on their answer while they're still together.
[ 0m50s674ms - 0m52s744ms ] Speaker 2: So that they can coordinate on their strategy.
[ 0m53s164ms - 1m1s524ms ] Speaker 2: When they're done figuring out a plan for how they would answer any of the three questions, they pack away those hidden variables into three sealed envelopes for each particle.
[ 1m1s524ms - 1m6s814ms ] Speaker 2: The question is, what strategy should our sneaky particles take to make people believe that they're following quantum mechanics?
[ 1m7s354ms - 1m10s494ms ] Speaker 2: Remember, quantum mechanics predicted a disagreement rate of 25%.
[ 1m11s44ms - 1m12s654ms ] Speaker 2: And so our particles want to match that.
[ 1m13s394ms - 1m18s124ms ] Speaker 2: Whenever they happen to be asked different questions, their answer needs to disagree about 25% of the time.
[ 1m18s834ms - 1m19s834ms ] Speaker 2: So, what's the best strategy?
[ 1m20s474ms - 1m22s774ms ] Speaker 2: Well, there's actually only two things that they really can do.
[ 1m23s214ms - 1m26s644ms ] Speaker 2: The first strategy is this, the electron answers the same way for each of its axes
[ 1m26s644ms - 1m27s984ms ] Speaker 2: and the positron answers in the opposite way.
[ 1m28s194ms - 1m30s914ms ] Speaker 2: Let's say the electron answers with minus
[ 1m32s374ms - 1m34s144ms ] Speaker 2: and the positron with plus.
[ 1m36s294ms - 1m43s974ms ] Speaker 2: But this is a terrible idea because whatever two different axes the experimenters happen to choose, the disagreement rate is 100%, which is very different from 25%.
[ 1m43s974ms - 1m45s844ms ] Speaker 2: And so that strategy doesn't work.
[ 1m45s844ms - 1m48s524ms ] Speaker 2: But there's only one other strategy that the particles could use.
[ 1m48s774ms - 1m52s824ms ] Speaker 2: Instead of the electron doing exactly the same thing for all three axes,
[ 1m53s54ms - 1m56s654ms ] Speaker 2: it does the same thing for any two of its axes and then something different for the last one.
[ 1m56s654ms - 1m58s904ms ] Speaker 2: Let's just say, for example, that it does this.
[ 2m0s984ms - 2m2s184ms ] Speaker 2: And then the positron does the opposite.
[ 2m2s394ms - 2m6s64ms ] Speaker 2: This is just one example, but it turns out for all possible strategies like this, the disagreement rate is going to be the same.
[ 2m7s414ms - 2m12s904ms ] Speaker 2: Let's imagine first that the experimenter who's measuring the electron happened to measure it in the 120° axis, and it gets the answer minus.
[ 2m13s384ms - 2m15s84ms ] Speaker 2: They make this choice a third of the time.
[ 2m15s684ms - 2m22s874ms ] Speaker 2: And now, to calculate the disagreement rate, we need to see what happens when the experimenter who's measuring the positron happens to measure a different axis from this one.
[ 2m23s344ms - 2m24s254ms ] Speaker 2: So, one of these two.
[ 2m24s744ms - 2m27s844ms ] Speaker 2: But in either one of these cases, the positron is also minus, and so the two answers agree with each other.
[ 2m28s394ms - 2m29s624ms ] Speaker 2: And so the answers have no disagreement.
[ 2m30s354ms - 2m31s524ms ] Speaker 2: And so we can multiply this
[ 2m32s634ms - 2m33s184ms ] Speaker 2: by zero.
[ 2m35s304ms - 2m40s404ms ] Speaker 2: But two thirds of the time, the experimenter who's measuring the electron will happen to measure it in one of the other two axes.
[ 2m40s404ms - 2m41s224ms ] Speaker 2: Let's say this one.
[ 2m44s144ms - 2m46s704ms ] Speaker 2: The experimenter measuring the positron will measure in one of these two axes.
[ 2m47s64ms - 2m49s724ms ] Speaker 2: But you can see that they only pick an axis that disagrees
[ 2m50s4ms - 2m51s784ms ] Speaker 2: a half of the time.
[ 2m51s974ms - 2m53s514ms ] Speaker 2: That's 1/3, which is roughly equal to 33%,
[ 2m54s594ms - 2m55s984ms ] Speaker 2: which is a different number from the quantum one.
[ 2m56s594ms - 3m1s484ms ] Speaker 2: When our scheming local particles are interrogated, their answers for different questions match just a little too often.
[ 3m2s104ms - 3m5s604ms ] Speaker 2: They simply can't fake the results of Copenhagen quantum mechanics.
[ 3m6s576ms - 3m14s36ms ] Speaker 3: So, Bell's proof showed that non-local and local theories make different predictions about how often the two results will disagree when the experimenters measure different axes.
[ 3m14s186ms - 3m17s336ms ] Speaker 3: Non-local quantum mechanics predicts disagreement only 25% of the time.
[ 3m17s816ms - 3m21s346ms ] Speaker 3: Local hidden variables predicts disagreement at least 33% of the time.
[ 3m22s226ms - 3m25s766ms ] Speaker 3: So, to find out if there really is a local hidden variable theory, you just need to do the experiment.
[ 3m26s646ms - 3m27s666ms ] Speaker 4: Okay, so
[ 3m27s926ms - 3m29s156ms ] Speaker 4: welcome at the
[ 3m29s566ms - 3m30s346ms ] Speaker 4: Institute Optique.
[ 3m31s226ms - 3m39s26ms ] Speaker 4: You are here in the place where Alain Aspect performed 40 years ago his experiments on the measurement of Bell's inequalities, and here are some of the original pictures of this experiments.
[ 3m39s26ms - 3m41s76ms ] Speaker 4: Which was much more challenging than it is today.
[ 3m41s326ms - 3m43s546ms ] Speaker 4: And it was a real experimental tool de force.
[ 3m48s946ms - 3m51s236ms ] Speaker 2: So is this one of the original equipment from that?
[ 3m51s496ms - 3m52s156ms ] Speaker 4: This is one
[ 3m52s576ms - 3m53s646ms ] Speaker 4: of the, yeah, of the polarizers.
[ 3m56s926ms - 3m57s856ms ] Speaker 4: It looks like that
[ 3m58s266ms - 4m0s116ms ] Speaker 4: now. Uh, so,
[ 4m0s476ms - 4m3s836ms ] Speaker 4: only on this small breadboard, right?
[ 4m4s556ms - 4m6s106ms ] Speaker 4: It's our main source.
[ 4m7s336ms - 4m10s476ms ] Speaker 4: And this beam is directed towards this element
[ 4m10s476ms - 4m11s926ms ] Speaker 4: which is the key element of the setup.
[ 4m12s246ms - 4m15s46ms ] Speaker 4: So it's a pair of crystals that produces pairs of entangled photons.
[ 4m15s996ms - 4m20s516ms ] Speaker 4: We will produce a pair of entangled photons and both are propagating
[ 4m20s966ms - 4m22s796ms ] Speaker 4: along each of these two arms.
[ 4m22s796ms - 4m23s826ms ] Speaker 4: They are separated.
[ 4m24s426ms - 4m26s246ms ] Speaker 4: So here we have the two detection arms.
[ 4m27s46ms - 4m31s326ms ] Speaker 4: And we can rotate the half wave plate to change the orientation of the measurement basis.
[ 4m35s36ms - 4m41s546ms ] Speaker 2: The experiment that we did with light was a little bit different from the one we described earlier with electrons and protons.
[ 4m41s546ms - 4m43s506ms ] Speaker 2: So, I'm going to explain how they correspond.
[ 4m44s386ms - 4m46s236ms ] Speaker 2: Here's a little diagram of the photon experiment.
[ 4m47s216ms - 4m50s6ms ] Speaker 2: So, first we have this element that makes the entangled pair of particles.
[ 4m52s176ms - 4m52s746ms ] Speaker 2: So that's these two.
[ 4m53s386ms - 4m56s936ms ] Speaker 2: Then, the entangled particles go off on separate arms of the experiment.
[ 4m57s616ms - 5m3s186ms ] Speaker 2: In our previous experiment, we could decide the direction that we're going to measure the particles in by rotating the Stern Gerlach machines.
[ 5m3s586ms - 5m9s36ms ] Speaker 2: And in this experiment, it's actually really similar, so we have these two polarizers that we're able to rotate independently.
[ 5m9s36ms - 5m13s316ms ] Speaker 2: And that is going to decide which direction these particles are measured in.
[ 5m14s36ms - 5m16s796ms ] Speaker 2: And so this experiment with light is completely equivalent to Bell's experiment.
[ 5m17s183ms - 5m24s83ms ] Speaker 5: Bell expected that the, that the experiments would show that the predictions of quantum mechanics were correct and that, you know, there was some kind of non-locality in nature.
[ 5m24s283ms - 5m30s63ms ] Speaker 3: Before the first Bell test was done, John Bell said, "In view of the general success of quantum mechanics, it's very hard for me to doubt the outcome of such experiments."
[ 5m30s313ms - 5m33s403ms ] Speaker 5: He didn't expect quantum physics to be wrong, because who would bet against quantum physics?
[ 5m33s403ms - 5m34s503ms ] Speaker 5: You'd have to be crazy.
[ 5m34s833ms - 5m40s753ms ] Speaker 2: Remember, the two different outcomes for Bell's theorem depend on how often two different measurement axes
[ 5m41s173ms - 5m44s323ms ] Speaker 2: are going to have results that disagree with each other.
[ 5m44s943ms - 5m46s43ms ] Speaker 2: Here's how we measure that disagreement rate.
[ 5m46s843ms - 5m50s333ms ] Speaker 2: First, we're going to start with both of the measurements being in the same direction.
[ 5m51s103ms - 5m54s13ms ] Speaker 2: And now we expect that these two are always going to disagree with each other because they have opposite spins.
[ 5m54s353ms - 5m58s753ms ] Speaker 2: So, we're going to create a bunch of entangled particles and find out how many of them disagree with each other per second.
[ 5m59s33ms - 6m2s573ms ] Speaker 2: This is going to give us a measure of the total number of particles coming per second.
[ 6m3s23ms - 6m5s733ms ] Speaker 2: That's because this device is making loads and loads of entangled particles.
[ 6m6s143ms - 6m7s323ms ] Speaker 2: And so we just need to know how many of them are coming at a time.
[ 6m7s693ms - 6m8s413ms ] Speaker 2: Then,
[ 6m12s243ms - 6m13s533ms ] Speaker 2: we rotate
[ 6m16s383ms - 6m19s143ms ] Speaker 2: one of the axes.
[ 6m19s833ms - 6m21s663ms ] Speaker 2: And now we measure the number of disagreeing
[ 6m21s663ms - 6m24s373ms ] Speaker 2: pairs per second.
[ 6m24s843ms - 6m26s163ms ] Speaker 2: And then dividing these two
[ 6m26s163ms - 6m27s283ms ] Speaker 2: will give us the disagreement rate.
[ 6m27s663ms - 6m30s303ms ] Speaker 2: And remember, quantum mechanics predicts that the disagreement rate will only be a quarter,
[ 6m30s623ms - 6m33s273ms ] Speaker 2: whereas local hidden variables
[ 6m33s783ms - 6m35s313ms ] Speaker 2: expects this number to be a third.
[ 6m36s972ms - 6m37s892ms ] Speaker 4: So I started
[ 6m40s272ms - 6m42s592ms ] Speaker 4: at 2000s, right?
[ 6m43s562ms - 6m46s72ms ] Speaker 4: And now I have five 500s, so That's that really works.
[ 6m46s72ms - 6m48s772ms ] Speaker 4: Well, well.
[ 6m48s992ms - 6m51s532ms ] Speaker 2: We did do this experiment again and the number we got very much
[ 6m51s532ms - 6m53s532ms ] Speaker 2: agreed with quantum mechanics.
[ 6m57s712ms - 7m0s642ms ] Speaker 2: But this is one of the most misunderstood experiments in all of physics.
[ 7m1s213ms - 7m6s573ms ] Speaker 5: You will find in all sorts of physics textbooks and papers and whatnot that what Bell's theorem proves
[ 7m7s73ms - 7m10s393ms ] Speaker 5: is that it rules out local hidden variables
[ 7m10s773ms - 7m12s183ms ] Speaker 5: or local realism.
[ 7m12s653ms - 7m14s363ms ] Speaker 5: John Bell said that was an error.
[ 7m15s803ms - 7m18s993ms ] Speaker 5: Um, you know, he he said like it's really quite remarkable how many people make that error.
[ 7m19s383ms - 7m23s803ms ] Speaker 3: I always get confused at the conclusion of Bell's theorem.
[ 7m23s803ms - 7m26s103ms ] Speaker 3: Yeah. Because there's a lot of people who say like, okay, it rules out hidden variables,
[ 7m26s933ms - 7m29s693ms ] Speaker 3: or things have to be non-local or whatever, but
[ 7m29s893ms - 7m30s783ms ] Speaker 3: what do you think?
[ 7m31s33ms - 7m34s143ms ] Speaker 2: Yeah, I think it is super confusing. And when I first learned Bell's theorem, um I was told
[ 7m34s143ms - 7m35s333ms ] Speaker 2: that it rules out local hidden variables.
[ 7m35s663ms - 7m38s943ms ] Speaker 3: I've heard this other argument that it sort of disproves either locality or realism.
[ 7m39s153ms - 7m42s93ms ] Speaker 5: If you say, okay, it means that you give up local realism.
[ 7m44s3ms - 7m48s73ms ] Speaker 5: Um, and so that means you somehow have a choice between giving up locality and giving up realism.
[ 7m48s73ms - 7m49s783ms ] Speaker 5: If you're giving up realism, realism about what?
[ 7m51s643ms - 7m52s463ms ] Speaker 5: Like,
[ 7m53s283ms - 7m58s93ms ] Speaker 5: like you got to, you got to tell me, because like for most definitions of that word,
[ 7m58s763ms - 8m0s883ms ] Speaker 5: you'd also be giving up locality.
[ 8m0s883ms - 8m2s233ms ] Speaker 5: So what the hell are you saving?
[ 8m3s563ms - 8m3s833ms ] Speaker 5: Um,
[ 8m4s603ms - 8m7s433ms ] Speaker 5: like I just don't, yeah, it's it's a really deep misunderstanding
[ 8m7s433ms - 8m9s813ms ] Speaker 5: that shows up in almost every single textbook on the subject.
[ 8m10s133ms - 8m12s223ms ] Speaker 3: So, what does Bell's theorem really prove?
[ 8m12s433ms - 8m13s383ms ] Speaker 3: Well, here's the logic.
[ 8m13s543ms - 8m16s133ms ] Speaker 3: Start by assuming locality for the entangled particles.
[ 8m16s383ms - 8m20s223ms ] Speaker 3: Using the EPR argument, the only way for them to coordinate their outcomes is using local hidden variables.
[ 8m20s683ms - 8m24s83ms ] Speaker 3: Then, Bell's proof showed that local hidden variables predict an incorrect experimental result.
[ 8m24s353ms - 8m26s733ms ] Speaker 3: Therefore, the assumption of locality must have been wrong.
[ 8m27s923ms - 8m31s73ms ] Speaker 1: We are obliged to invoke something like actions going faster than light from one place to another.
[ 8m31s383ms - 8m36s713ms ] Speaker 3: The EPR paper by itself had shown that the Copenhagen interpretation is non-local, which is why Einstein thought there must be an alternative way to describe the experiment that is local.
[ 8m36s963ms - 8m38s133ms ] Speaker 3: But Bell's theorem says
[ 8m38s363ms - 8m39s263ms ] Speaker 3: that's not true.
[ 8m39s813ms - 8m42s683ms ] Speaker 3: Any theory that correctly describes this experiment must be non-local.
[ 8m42s843ms - 8m48s13ms ] Speaker 5: But I, I still, I would hesitate to say that that means that Einstein was wrong, right?
[ 8m48s233ms - 8m52s133ms ] Speaker 5: Because what I would, I would say is this shows that Einstein was right to be concerned about all of this.
[ 8m52s663ms - 8m57s773ms ] Speaker 3: People often claim that Einstein's problem was that he simply couldn't accept quantum mechanics, but it was only because he refused to shut up and calculate
[ 8m57s773ms - 9m2s233ms ] Speaker 3: that he discovered two of the most important aspects of quantum mechanics, entanglement and non-locality.
[ 9m2s573ms - 9m7s533ms ] Speaker 5: The heart of the debate between Einstein and Bohr
[ 9m8s243ms - 9m11s653ms ] Speaker 5: was about whether there was a problem,
[ 9m12s23ms - 9m13s333ms ] Speaker 5: whether there was something to be
[ 9m13s333ms - 9m17s313ms ] Speaker 5: concerned about. And the major concern that Einstein brought to the table
[ 9m17s743ms - 9m20s373ms ] Speaker 5: from the beginning was about locality.
[ 9m20s723ms - 9m22s733ms ] Speaker 5: But, you know, what Bell showed was,
[ 9m23s23ms - 9m27s363ms ] Speaker 5: "Oh, yeah, all that stuff that Einstein was concerned about about locality,
[ 9m27s743ms - 9m30s303ms ] Speaker 5: he was completely right to be worried about it.
[ 9m30s303ms - 9m31s433ms ] Speaker 5: We have a problem."
[ 9m32s33ms - 9m34s913ms ] Speaker 3: If these particles really are acting non-locally, this should cause paradoxes, shouldn't it?
[ 9m35s313ms - 9m36s733ms ] Speaker 3: Well, it does,
[ 9m36s973ms - 9m38s883ms ] Speaker 3: but the paradox seems to be surprisingly tame.
[ 9m39s333ms - 9m42s63ms ] Speaker 3: Imagine you and your friend are measuring a pair of entangled particles.
[ 9m42s373ms - 9m46s223ms ] Speaker 3: Suppose an observer sees you measure yours first and then your friend measures hers.
[ 9m46s703ms - 9m50s633ms ] Speaker 3: That observer thinks that you collapse the overall state of both particles and your friend just finds out the result when she measures.
[ 9m50s993ms - 9m54s533ms ] Speaker 3: But another observer will see the situation in reverse. They see her measure first and then you.
[ 9m54s813ms - 9m57s53ms ] Speaker 3: To them, it was her measurement that caused the collapse, not yours.
[ 9m57s323ms - 1m0s403ms ] Speaker 3: But who's right? Which measurement was the cause of the collapse and which was the effect?
[ 1m0s693ms - 1m2s493ms ] Speaker 3: It seems to depend on your frame of reference.
[ 1m3s233ms - 1m6s823ms ] Speaker 3: This paradox is worrying, but it isn't as bad as the usual faster than light paradoxes.
[ 1m7s163ms - 1m10s403ms ] Speaker 3: In relativity, if you can communicate faster than light, then you can exploit how different observers disagree about timing.
[ 1m10s863ms - 1m17s143ms ] Speaker 3: If your friend who's on a rocket sends you an instant message and you send an instant message back, in some frames of reference, your message can arrive before she even sent the first one.
[ 1m17s643ms - 1m21s333ms ] Speaker 3: If your message says, "Don't send your original message," and so she doesn't,
[ 1m21s493ms - 1m23s233ms ] Speaker 3: then you've got yourself a paradox.
[ 1m23s233ms - 1m25s793ms ] Speaker 3: What prompted you to send this message if she never sent you anything in the first place?
[ 1m26s163ms - 1m30s323ms ] Speaker 3: Quantum mechanics sidesteps these paradoxes through a fundamental constraint: the outcomes are random, so you can't send messages faster than light.
[ 1m30s653ms - 1m33s773ms ] Speaker 3: When you measure your particle, you get a plus or a minus completely at random.
[ 1m34s143ms - 1m36s603ms ] Speaker 3: Your friend measuring their particle also gets a random result.
[ 1m37s183ms - 1m38s703ms ] Speaker 3: Now, the results will be correlated,
[ 1m38s883ms - 1m43s213ms ] Speaker 3: but they're still completely random, so there's no way to send any faster than light message in this way.
[ 1m43s463ms - 1m46s43ms ] Speaker 3: That's what prevents us from sending messages back in time using quantum mechanics.
[ 1m46s413ms - 1m48s593ms ] Speaker 3: So, quantum mechanics is non-local,
[ 1m48s893ms - 1m51s973ms ] Speaker 3: but it doesn't lead to the sort of catastrophic paradoxes you might expect from relativity.
[ 1m52s223ms - 1m53s593ms ] Speaker 3: But it's an uneasy truce.
[ 1m53s863ms - 1m56s893ms ] Speaker 3: Quantum mechanics may not break the letter of relativity's laws, but it certainly violates the spirit.
[ 1m57s263ms - 2m0s763ms ] Speaker 3: And non-locality isn't the only troubling thing about quantum mechanics.
[ 2m0s763ms - 2m4s333ms ] Speaker 3: The Copenhagen interpretation still doesn't explain what an electron is really doing and why it acts so differently when measured.
[ 2m5s633ms - 2m10s433ms ] Speaker 3: Despite this, many physicists took Bell's theorem to mean that the Copenhagen interpretation was right all along.
[ 2m10s683ms - 2m11s953ms ] Speaker 3: Bell himself rejected this.
[ 2m12s243ms - 2m17s143ms ] Speaker 3: He spent the rest of his life championing alternative interpretations of quantum mechanics, including the hidden variable interpretation called pilot wave theory or Bohmian mechanics.
[ 2m17s493ms - 2m21s303ms ] Speaker 3: Bell's theorem doesn't rule this interpretation out because the pilot wave theory is non-local, just like the Copenhagen interpretation.
[ 2m22s223ms - 2m28s13ms ] Speaker 3: It was Bell's theorem and Bell's subsequent tireless work that made studying the meaning of quantum mechanics respectable again.
[ 2m28s193ms - 2m32s333ms ] Speaker 3: He showed that mere armchair philosophy and thought experiments can have real consequences in physics.
[ 2m32s633ms - 2m35s333ms ] Speaker 5: We need to be teaching quantum physics in a different way.
[ 2m35s333ms - 2m36s793ms ] Speaker 5: We need to be teaching Bell's theorem in a different way.
[ 2m36s793ms - 2m40s753ms ] Speaker 5: We do often teach Bell's theorem to physics students, and it's taught as something that rules out local hidden variables.
[ 2m40s753ms - 2m41s843ms ] Speaker 5: That's just not true.
[ 2m44s3ms - 2m50s463ms ] Speaker 5: Bell's theorem, you know, says that quantum physics is in very serious tension with relativity on the issue of locality.
[ 2m50s853ms - 2m53s153ms ] Speaker 3: John Bell passed away suddenly at the age of 62.
[ 2m53s593ms - 2m56s263ms ] Speaker 3: He didn't know it, but he had been nominated for the Nobel Prize just a year earlier.
[ 2m56s593ms - 2m58s933ms ] Speaker 5: In a talk he gave in Geneva in January 1990,
[ 3m0s113ms - 3m2s183ms ] Speaker 5: he said, "I think you're stuck with non-locality.
[ 3m3s153ms - 3m5s413ms ] Speaker 5: I don't know any conception of locality
[ 3m5s413ms - 3m7s23ms ] Speaker 5: which works with quantum mechanics."
[ 3m7s513ms - 3m9s203ms ] Speaker 5: That was 8 months before he died.
[ 3m9s963ms - 3m11s403ms ] Speaker 5: Um, so, pretty much his last word on the subject.
[ 3m11s683ms - 3m14s173ms ] Speaker 3: And so that's it. There really are faster than light influences in the universe.
[ 3m14s383ms - 3m15s473ms ] Speaker 3: Bell's theorem proves it.
[ 3m16s383ms - 3m17s323ms ] Speaker 3: But maybe there is a way out.
[ 3m18s173ms - 3m21s333ms ] Speaker 3: There is another way to interpret quantum mechanics that's even more bizarre than the Copenhagen interpretation.
[ 3m21s633ms - 3m23s283ms ] Speaker 3: Imagine the EPR thought experiment again.
[ 3m23s943ms - 3m29s843ms ] Speaker 3: We can think of the entangled state as being in a superposition of the electron being up and the positron down, and the electron being down and the positron being up.
[ 3m30s143ms - 3m34s173ms ] Speaker 3: In the Copenhagen interpretation, when you measure a particle and you get only one result, say plus, the other part of the superposition collapses.
[ 3m34s773ms - 3m37s893ms ] Speaker 3: But in our examples, we've seen that measurement collapse seems to be the source of non-locality.
[ 3m38s203ms - 3m39s913ms ] Speaker 3: So, why don't we just get rid of collapse altogether?
[ 3m40s203ms - 3m42s803ms ] Speaker 3: This is what the many worlds interpretation of quantum mechanics proposes.
[ 3m43s133ms - 3m49s53ms ] Speaker 3: When you measure a particle, instead of you collapsing the particle to one outcome, both outcomes happen, and there's two parallel versions of you who sees each outcome.
[ 3m49s463ms - 3m54s53ms ] Speaker 3: You have become entangled with your particle because your state depends on what the particle is doing.
[ 3m54s253ms - 3m56s653ms ] Speaker 3: It sounds strange, but there's one huge benefit of this interpretation.
[ 3m56s983ms - 4m3s63ms ] Speaker 3: When your friend is about to measure her electron, your positron doesn't need to rush to tell the electron what the answer will be. There are already two versions of the electron, and they contain the right answer for each version of her.
[ 4m3s413ms - 4m5s603ms ] Speaker 3: There was no need for faster than light communication to explain the EPR experiment.
[ 4m5s763ms - 4m8s343ms ] Speaker 3: But how is that possible?
[ 4m8s343ms - 4m10s93ms ] Speaker 3: Doesn't Bell's theorem prove that the two particles must communicate faster than light?
[ 4m10s333ms - 4m13s63ms ] Speaker 3: Well, in Bell's proof, we assumed that all measurements have just one outcome.
[ 4m13s483ms - 4m15s863ms ] Speaker 3: But that assumption just isn't true in many worlds.
[ 4m16s133ms - 4m18s993ms ] Speaker 3: This means that technically, that proof doesn't even apply in the many worlds case.
[ 4m19s393ms - 4m20s523ms ] Speaker 3: So, is many worlds local?
[ 4m20s873ms - 4m27s363ms ] Speaker 3: In one sense, no, because just like in Copenhagen quantum mechanics, entangled pairs can be separated by a huge distance and still share their state.
[ 4m27s513ms - 4m32s423ms ] Speaker 3: However, it is local, unlike Copenhagen, in the sense that these far away entangled particles do not influence each other faster than light.
[ 4m32s763ms - 4m35s363ms ] Speaker 3: Many worlds obeys Einstein's universal speed limit.
[ 4m35s663ms - 4m39s643ms ] Speaker 3: But is it really worth accepting that there are many versions of you in parallel universes just to recover locality?
[ 4m39s863ms - 4m42s93ms ] Speaker 3: Well, locality isn't the only reason many worlds has become more and more popular.
[ 4m42s183ms - 4m43s733ms ] Speaker 3: I also really like Many Worlds.
[ 4m43s733ms - 4m45s333ms ] Speaker 3: I cuz Copenhagen never sits right.
[ 4m45s333ms - 4m50s233ms ] Speaker 3: And when you start telling the story, right, of like what happens at measurement, it's like, well, what is a measurement?
[ 4m50s233ms - 4m55s123ms ] Speaker 3: It's when you have like this quantum system and there's some other system which is like much larger and so, you know?
[ 4m55s453ms - 4m56s653ms ] Speaker 3: But it it always feels a little bit arbitrary.
[ 4m56s653ms - 5m3s153ms ] Speaker 3: Whereas this this argument that every time two quantum particles are interacting, their wave functions are essentially, you know, combining and becoming entangled.
[ 5m3s663ms - 5m5s63ms ] Speaker 3: That to me feels more consistent.
[ 5m5s183ms - 5m5s463ms ] Speaker 2: Yes.
[ 5m5s643ms - 5m6s613ms ] Speaker 2: I, I think that's right.
[ 5m6s613ms - 5m8s123ms ] Speaker 2: What do you think are like the problems with many worlds?
[ 5m9s63ms - 5m14s333ms ] Speaker 3: The biggest problem is I think people's struggle to deal with sort of the infinity that that brings forth.
[ 5m14s493ms - 5m15s43ms ] Speaker 2: For sure.
[ 5m15s253ms - 5m17s813ms ] Speaker 3: But I, I don't know that that's necessarily an argument against it.
[ 5m17s813ms - 5m20s323ms ] Speaker 3: Just cuz like, just cuz it's hard to imagine, doesn't mean
[ 5m20s323ms - 5m21s993ms ] Speaker 3: it's not what's happening.
[ 5m22s343ms - 5m23s673ms ] Speaker 3: If many worlds is right,
[ 5m23s853ms - 5m24s833ms ] Speaker 3: everything changes.
[ 5m25s183ms - 5m26s933ms ] Speaker 3: The conflict between quantum mechanics and relativity vanishes.
[ 5m27s363ms - 5m32s373ms ] Speaker 3: Physicists have been struggling for decades to unite quantum mechanics with general relativity, to build a theory of quantum gravity.
[ 5m32s763ms - 5m36s123ms ] Speaker 3: And maybe we've been failing because we've been trying to marry relativity to a non-local theory.
[ 5m36s583ms - 5m41s123ms ] Speaker 3: But if quantum mechanics ultimately turns out to be local, well then Einstein's dream of a local description of reality
[ 5m41s123ms - 5m42s963ms ] Speaker 3: might not be dead after all.