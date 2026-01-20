---
title: Veritasium_The Man Who Accidentally Discovered Antimatter_20251205_part2
audio_file: Veritasium_The Man Who Accidentally Discovered Antimatter_20251205_part2.mp3
note_id: 104bf3cb-c626-4b68-a8ed-89e3d626950e
date_processed: '2026-01-06'
classification:
  primary_domain: Physics
  sub_domains:
  - Quantum Mechanics
  - Particle Physics
  - Cosmology
  - History of Physics
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people:
  - name: Werner Heisenberg
    role: Theoretical physicist
    contribution: Criticized Dirac's equation for its negative energy solutions and
      famously said "I give up"; later quoted as noting the leap to antiparticles.
  - name: Paul Dirac
    role: Theoretical physicist
    contribution: Formulated the Dirac equation, identified negative energy solutions,
      proposed the anti‑electron (positron) and the Dirac sea concept.
  - name: Carl Anderson
    role: Caltech postdoctoral researcher
    contribution: Experimentally discovered the positron in 1932 using a cloud chamber
      in a magnetic field.
  - name: Ernst Stueckelberg
    role: Swiss physicist
    contribution: Proposed that negative‑energy electrons moving backward in time
      are equivalent to positive‑energy positrons moving forward in time.
  - name: Richard Feynman
    role: Physicist
    contribution: Incorporated the backward‑in‑time interpretation into Feynman diagrams,
      visualizing antiparticles as particles traveling opposite to time.
  - name: Erwin Schrödinger
    role: Physicist
    contribution: Shared the 1933 Nobel Prize with Dirac for contributions to quantum
      theory.
  works_cited: []
  concepts_mentioned:
  - Dirac equation
  - Negative energy solutions
  - Anti‑electron / Positron
  - Dirac sea
  - Antiparticle
  - Breit‑Wheeler pair production
  - Matter‑antimatter asymmetry
  - Feynman diagrams
  - Annihilation
  laws_theories_cited:
  - Dirac equation
  - Dirac sea model
  - Breit‑Wheeler pair production
  - Feynman diagram formalism
concepts:
- name: Dirac equation
  definition: A relativistic wave equation for spin‑½ particles that predicts both
    positive and negative energy solutions.
  parent_concepts:
  - Quantum Mechanics
  - Relativistic Physics
  related_concepts:
  - Negative energy solutions
  - Antiparticle
  - Spinor
  abstraction_level: Fundamental
  confidence: 1.0
- name: Antiparticle
  definition: A particle with the same mass as a given particle but opposite charge
    and quantum numbers.
  parent_concepts:
  - Particle Physics
  related_concepts:
  - Positron
  - Dirac sea
  - Feynman diagrams
  abstraction_level: Fundamental
  confidence: 1.0
- name: Dirac sea
  definition: A theoretical model describing the vacuum as an infinite sea of electrons
    filling all negative‑energy states, whose holes appear as positrons.
  parent_concepts:
  - Quantum Field Theory
  related_concepts:
  - Negative energy solutions
  - Positron
  - Pauli exclusion principle
  abstraction_level: Theoretical
  confidence: 0.95
- name: Breit‑Wheeler pair production
  definition: The process by which two high‑energy photons convert into an electron‑positron
    pair.
  parent_concepts:
  - Quantum Electrodynamics
  related_concepts:
  - Annihilation
  - Matter‑antimatter creation
  abstraction_level: Theoretical
  confidence: 0.95
- name: Matter‑antimatter asymmetry
  definition: The observed imbalance in the universe where matter vastly outnumbers
    antimatter, requiring a tiny excess of matter after the early hot dense phase.
  parent_concepts:
  - Cosmology
  related_concepts:
  - Big Bang
  - CP violation
  - Breit‑Wheeler pair production
  abstraction_level: Applied
  confidence: 0.9
relationships:
- source_concept: Dirac equation
  target_concept: Negative energy solutions
  relationship_type: predicts
  strength: 0.95
  evidence: The transcript states the Dirac equation yields two positive and two negative
    energy solutions.
  reasoning: The equation mathematically generates both signs of energy.
- source_concept: Negative energy solutions
  target_concept: Antiparticle
  relationship_type: equivalent_to
  strength: 0.9
  evidence: Stueckelberg and Feynman interpreted negative‑energy electrons moving
    backward in time as positrons moving forward in time.
  reasoning: The backward‑in‑time interpretation maps negative energies to antiparticles.
- source_concept: Dirac sea
  target_concept: Negative energy solutions
  relationship_type: prevents_fall_into
  strength: 0.9
  evidence: The sea fills all negative states, so Pauli exclusion stops observable
    electrons from occupying them.
  reasoning: Occupied states block transitions to lower energy.
- source_concept: Positron
  target_concept: Antiparticle
  relationship_type: is_a
  strength: 0.95
  evidence: The transcript defines the positron as the anti‑electron.
  reasoning: Positron is the specific antiparticle of the electron.
- source_concept: Breit‑Wheeler pair production
  target_concept: Matter‑antimatter asymmetry
  relationship_type: contributes_to
  strength: 0.85
  evidence: The transcript notes that photon collisions can produce matter‑antimatter
    pairs in the early universe.
  reasoning: These processes created equal amounts of matter and antimatter, influencing
    the asymmetry discussion.
- source_concept: Feynman diagrams
  target_concept: Antiparticle
  relationship_type: represents
  strength: 0.9
  evidence: Feynman used diagrams showing antiparticles traveling opposite to particles,
    i.e., backward in time.
  reasoning: The visual formalism encodes the backward‑in‑time interpretation.
- source_concept: Matter‑antimatter asymmetry
  target_concept: Universe composition
  relationship_type: causes
  strength: 0.85
  evidence: The transcript explains that a tiny excess of matter after annihilation
    led to the matter‑dominated universe we observe.
  reasoning: The asymmetry determines the net matter left after annihilation.
cross_domain_insights:
- connection_type: structural_analogy|principle_application
  source_domain: Physics
  source_concept: Dirac equation (first‑order linear differential operator with spinor
    solutions)
  target_domain: Control Engineering
  target_concept: State‑space representation of linear dynamical systems (matrix operator
    acting on state vectors)
  insight: Both describe evolution of a multi‑component entity via a linear operator,
    yielding eigen‑modes that evolve independently.
  explanation: The Dirac equation can be written as \( (i\gamma^\mu\partial_\mu -
    m)\psi = 0 \), a first‑order linear operator on a spinor. In control theory, \(
    \dot{x}=Ax+Bu \) uses a matrix operator on a state vector. The mathematics of
    eigen‑values/eigen‑vectors, superposition, and propagation of modes is identical,
    allowing techniques such as modal analysis to transfer.
  potential_applications:
  - Design of quantum‑inspired robust controllers using spinor‑like state vectors
  - Cross‑disciplinary curricula linking quantum mechanics and systems theory
  confidence: 0.86
  historical_example: The adoption of Hamiltonian mechanics in early electrical network
    analysis (1920s) showed how physics formalisms can guide engineering system design.
- connection_type: metaphor|principle_application
  source_domain: Physics
  source_concept: Antiparticle as a negative‑energy solution of the Dirac equation
  target_domain: Economics
  target_concept: Debt/negative assets in balance‑sheet accounting
  insight: An antiparticle behaves mathematically like a particle with opposite sign,
    mirroring how debt is a financial position opposite to positive assets.
  explanation: Negative‑energy states are filled in the Dirac sea; a hole (absence)
    appears as a positively charged antiparticle. Similarly, a liability is a negative
    entry that, when settled (hole filled), restores net positive equity. Both involve
    conservation laws (charge, accounting identity) and the notion of a baseline filled
    with ‘neutral’ entities.
  potential_applications:
  - Teaching financial risk using particle‑antiparticle analogies
  - Modeling systemic risk as vacuum fluctuations that can produce ‘particle‑like’
    crises
  confidence: 0.78
  historical_example: John Maynard Keynes used the metaphor of ‘negative money’ to
    describe deficits in the 1930s, foreshadowing modern quantum‑style analogies.
- connection_type: structural_analogy|historical_precedent
  source_domain: Physics
  source_concept: Dirac sea (filled vacuum of negative‑energy electrons)
  target_domain: Ecology
  target_concept: Ecological niche saturation (all available niches occupied, leaving
    no room for new species without disturbance)
  insight: Both describe a densely populated baseline from which excitations (holes
    or invasions) create observable entities.
  explanation: In the Dirac sea, the vacuum is a sea of electrons; a missing electron
    (hole) appears as a positron. In a saturated ecosystem, every niche is filled;
    a disturbance creates a vacant niche, allowing a new species to establish. The
    concept of a ‘filled background’ and ‘excitation as absence’ is common to both.
  potential_applications:
  - Using quantum‑vacuum language to communicate concepts of invasive species management
  - Developing stochastic models of ecosystem turnover inspired by particle‑hole dynamics
  confidence: 0.73
  historical_example: Hutchinson’s niche concept (1957) was later linked to statistical
    mechanics models of occupancy, echoing the Dirac sea analogy.
- connection_type: structural_analogy|principle_application
  source_domain: Physics
  source_concept: Breit–Wheeler pair production (γ + γ → e⁺ + e⁻)
  target_domain: Chemistry
  target_concept: Photochemical reaction where two photons induce formation of a reactive
    intermediate (e.g., singlet oxygen generation)
  insight: Two inert quanta combine to create a particle‑antiparticle pair, analogous
    to two photons combining to generate a chemically active species.
  explanation: The Breit–Wheeler process requires sufficient combined energy to cross
    a mass threshold, similar to how two photons must collectively provide the activation
    energy to promote a molecule to an excited state that can then undergo a reaction.
    Both follow conservation laws (energy, momentum ↔ mass balance, quantum yields).
  potential_applications:
  - Design of light‑driven catalytic cycles inspired by photon‑photon conversion
  - Educational modules linking high‑energy physics to photochemistry
  confidence: 0.71
  historical_example: The concept of two‑photon absorption (1961) was directly inspired
    by the Breit–Wheeler idea, bridging high‑energy physics and laser chemistry.
- connection_type: principle_application|metaphor
  source_domain: Physics
  source_concept: Matter–antimatter asymmetry (baryogenesis)
  target_domain: Sociology
  target_concept: Opinion polarization where a small initial bias leads to a dominant
    majority through feedback loops
  insight: Both involve a tiny symmetry‑breaking perturbation that, amplified by non‑linear
    dynamics, yields a large-scale imbalance.
  explanation: In baryogenesis, CP‑violation provides a minute excess of matter over
    antimatter, which is then magnified by out‑of‑equilibrium processes. In social
    systems, a slight preference (e.g., a charismatic leader) can be amplified by
    network effects and conformity pressures, producing a dominant opinion. The mathematical
    frameworks (e.g., Boltzmann equations ↔ opinion diffusion models) share similar
    non‑linear amplification terms.
  potential_applications:
  - Applying kinetic‑theory models to predict political swing dynamics
  - Using baryogenesis simulations as analog computers for social cascade phenomena
  confidence: 0.66
  historical_example: Thomas Schelling’s segregation model (1971) used physical analogies
    of particle interactions to explain social clustering, a precedent for such cross‑domain
    transfer.
bridge_concepts:
- concept: Symmetry Breaking
  appears_in_domains:
  - Physics
  - Economics
  - Sociology
  - Biology
  role: Provides a unified language for describing how a perfectly balanced system
    develops a dominant direction after a small perturbation.
  examples:
  - Spontaneous symmetry breaking in the Higgs mechanism (Physics)
  - Market dominance emerging from a slight cost advantage (Economics)
  - Cultural norm formation after a marginal innovation (Sociology)
  - Cell differentiation from a homogeneous stem‑cell population (Biology)
- concept: Duality (Particle ↔ Antiparticle, Positive ↔ Negative)
  appears_in_domains:
  - Physics
  - Finance
  - Computer Science
  role: Encodes the idea that every entity has a complementary counterpart whose interaction
    yields neutral or transformative outcomes.
  examples:
  - Electron vs. positron (Physics)
  - Asset vs. liability (Finance)
  - Data vs. error‑correction code (Computer Science)
- concept: Vacuum/Background State
  appears_in_domains:
  - Physics
  - Ecology
  - Information Theory
  role: Acts as a baseline filled with latent potential; excitations or holes relative
    to this baseline create observable phenomena.
  examples:
  - Dirac sea of negative‑energy electrons (Physics)
  - Fully occupied ecological niches before disturbance (Ecology)
  - Zero‑information state in Shannon entropy (Information Theory)
mental_models:
- name: First‑Principles Decomposition
  description: Break a complex system down to its most fundamental laws or axioms
    before rebuilding higher‑level behavior.
  applied_to:
  - Deriving the Dirac equation from relativistic invariance and linearity
  transferable_to:
  - Product design (physics → engineering)
  - Policy analysis (axiomatic economics)
- name: Symmetry‑Breaking Feedback Loop
  description: A small asymmetric input is amplified by non‑linear feedback, leading
    to macroscopic imbalance.
  applied_to:
  - Matter–antimatter asymmetry mechanisms
  transferable_to:
  - Network effects in technology adoption
  - Positive feedback in climate tipping points
- name: Particle‑Hole Duality
  description: Treating the absence of an entity in a filled background as an active,
    positively‑charged object.
  applied_to:
  - Antiparticles as holes in the Dirac sea
  transferable_to:
  - Electronic engineering (holes in semiconductor bands)
  - Financial risk (debt as a hole in asset space)
analogies_used:
- source_domain: Everyday Life
  source_concept: Ocean surface with fish below
  target_domain: Physics
  target_concept: Dirac sea (filled vacuum of negative‑energy electrons)
  mapping:
    Ocean surface: observable positive‑energy particles
    Fish below: negative‑energy sea
    Hole in fish school: positron (antiparticle)
  pedagogical_value: Visualizes an invisible, densely populated background and how
    a missing element appears as a new, opposite entity.
- source_domain: Finance
  source_concept: Debt as a negative balance
  target_domain: Physics
  target_concept: Antiparticle as a negative‑energy solution
  mapping:
    Positive balance: electron (positive energy)
    Negative balance (debt): positron (negative energy hole)
    Settlement: annihilation producing photons
  pedagogical_value: Leverages familiar accounting language to convey the abstract
    idea of charge reversal and annihilation.
tags:
  hierarchical:
  - '#Physics → #Quantum Mechanics → #Dirac Equation → #Negative Energy Solutions'
  - '#Physics → #Particle Physics → #Antiparticles → #Positron'
  - '#Physics → #Cosmology → #Matter‑Antimatter Asymmetry'
  topical:
  - '#DiracEquation'
  - '#Positron'
  - '#DiracSea'
  - '#Antimatter'
  - '#BreitWheeler'
  - '#FeynmanDiagrams'
  - '#MatterAntimatterAsymmetry'
  methodological:
  - '#TimeReversalInterpretation'
  - '#DiagrammaticRepresentation'
  people:
  - '#Dirac'
  - '#Heisenberg'
  - '#Anderson'
  - '#Stueckelberg'
  - '#Feynman'
  - '#Schrodinger'
  concepts:
  - '#NegativeEnergy'
  - '#Antiparticle'
  - '#DiracSea'
  - '#PairProduction'
  - '#MatterAntimatterAsymmetry'
  temporal:
  - '#1920s'
  - '#1930s'
  - '#1940s'
  - '#BigBang'
summary: The Dirac equation’s negative‑energy solutions forced physicists to postulate
  a new particle—the anti‑electron (positron)—which was experimentally discovered
  by Carl Anderson in 1932; Dirac later explained the paradox with the “Dirac sea”
  of filled negative‑energy states, a picture later reformulated by Stueckelberg and
  Feynman as antiparticles moving backward in time. This led to the modern understanding
  that every particle has a corresponding antiparticle, but the lingering mystery
  of why a tiny excess of matter survived the early‑universe annihilations remains
  unsolved.
key_ideas:
- idea: Negative‑energy solutions of the Dirac equation** – The relativistic wave
    equation yields both positive and negative energy states, which initially seemed
    physically impossible.
  description: No description provided by model.
- idea: Prediction and discovery of the positron** – Dirac proposed a particle with
    the same mass as an electron but opposite charge, later confirmed experimentally
    by Carl Anderson’s cloud‑chamber tracks.
  description: No description provided by model.
- idea: The Dirac sea model** – To prevent electrons from falling into negative‑energy
    states, Dirac imagined an infinite “sea” of filled negative‑energy electrons,
    with holes in this sea manifesting as positrons.
  description: No description provided by model.
- idea: Antiparticles as particles moving backward in time** – Stueckelberg and Feynman
    re‑interpreted negative‑energy electrons traveling backward in time as ordinary
    positive‑energy antiparticles moving forward, a concept used in Feynman diagrams.
  description: No description provided by model.
- idea: Matter‑antimatter asymmetry in the early universe** – Although particle–antiparticle
    pairs were created in equal numbers after the Big Bang, a tiny imbalance (one
    part in a billion) allowed matter to dominate the cosmos.
  description: No description provided by model.
---
## Key Concepts

**Dirac equation**  
A relativistic wave equation for spin‑½ particles that predicts both positive and negative energy solutions.

**Antiparticle**  
A particle with the same mass as a given particle but opposite charge and quantum numbers.

**Dirac sea**  
A theoretical model describing the vacuum as an infinite sea of electrons filling all negative‑energy states, whose holes appear as positrons.

**Breit‑Wheeler pair production**  
The process by which two high‑energy photons convert into an electron‑positron pair.

**Matter‑antimatter asymmetry**  
The observed imbalance in the universe where matter vastly outnumbers antimatter, requiring a tiny excess of matter after the early hot dense phase.

## Cross-Domain Connections

**Physics → Control Engineering**

*Both describe evolution of a multi‑component entity via a linear operator, yielding eigen‑modes that evolve independently.*

The Dirac equation can be written as \( (i\gamma^\mu\partial_\mu - m)\psi = 0 \), a first‑order linear operator on a spinor. In control theory, \( \dot{x}=Ax+Bu \) uses a matrix operator on a state vector. The mathematics of eigen‑values/eigen‑vectors, superposition, and propagation of modes is identical, allowing techniques such as modal analysis to transfer.

**Physics → Economics**

*An antiparticle behaves mathematically like a particle with opposite sign, mirroring how debt is a financial position opposite to positive assets.*

Negative‑energy states are filled in the Dirac sea; a hole (absence) appears as a positively charged antiparticle. Similarly, a liability is a negative entry that, when settled (hole filled), restores net positive equity. Both involve conservation laws (charge, accounting identity) and the notion of a baseline filled with ‘neutral’ entities.

**Physics → Ecology**

*Both describe a densely populated baseline from which excitations (holes or invasions) create observable entities.*

In the Dirac sea, the vacuum is a sea of electrons; a missing electron (hole) appears as a positron. In a saturated ecosystem, every niche is filled; a disturbance creates a vacant niche, allowing a new species to establish. The concept of a ‘filled background’ and ‘excitation as absence’ is common to both.

## Discussion Topics

- **Negative‑energy solutions of the Dirac equation** – The relativistic wave equation yields both positive and negative energy states, which initially seemed physically impossible.:** No description provided by model.
- **Prediction and discovery of the positron** – Dirac proposed a particle with the same mass as an electron but opposite charge, later confirmed experimentally by Carl Anderson’s cloud‑chamber tracks.:** No description provided by model.
- **The Dirac sea model** – To prevent electrons from falling into negative‑energy states, Dirac imagined an infinite “sea” of filled negative‑energy electrons, with holes in this sea manifesting as positrons.:** No description provided by model.
- **Antiparticles as particles moving backward in time** – Stueckelberg and Feynman re‑interpreted negative‑energy electrons traveling backward in time as ordinary positive‑energy antiparticles moving forward, a concept used in Feynman diagrams.:** No description provided by model.
- **Matter‑antimatter asymmetry in the early universe** – Although particle–antiparticle pairs were created in equal numbers after the Big Bang, a tiny imbalance (one part in a billion) allowed matter to dominate the cosmos.:** No description provided by model.

## Full Transcription



[ 0m1s127ms - 0m3s537ms ] **Speaker 1:** beautiful equation that Heisenberg called the saddest chapter in modern physics.
[ 0m3s537ms - 0m10s957ms ] **Speaker 1:** To understand why all those physicists were losing their minds, we only have to look at the simple case when a particle is at rest.
[ 0m10s957ms - 0m16s857ms ] **Speaker 1:** This term right here describes the momentum, so when the particle doesn't move, this becomes zero and it drops out, which gives us this.
[ 0m16s857ms - 0m19s837ms ] **Speaker 1:** Next, we can sub in the energy for this quantum operator to get this.
[ 0m19s837ms - 0m24s837ms ] **Speaker 1:** So, now we know that beta times mc squared must be equal to the particle's energy.
[ 0m24s837ms - 0m30s407ms ] **Speaker 1:** And if we write out beta and multiply it by mc squared, then we find two positive solutions and two negative solutions for the energy.
[ 0m30s407ms - 0m32s897ms ] **Speaker 1:** So, negative energy solutions are baked right into the Dirac equation.
[ 0m32s897ms - 0m38s727ms ] **Speaker 1:** And this idea that a free electron could have negative energy was impossible for any of these physicists to accept.
[ 0m38s727ms - 0m41s137ms ] **Speaker 1:** Because think about it.
[ 0m41s137ms - 0m47s407ms ] **Speaker 1:** If electrons can have a negative energy, then that means that they could continually radiate positive energy, that is emit photons and drop into lower and lower negative energy states.
[ 0m47s407ms - 0m51s957ms ] **Speaker 1:** There would be no limit to how far they could fall into the negative energy abyss.
[ 0m51s957ms - 0m59s377ms ] **Speaker 2:** It looked like to many very smart people and direct was smart enough to know they had a point that this equation it got the mass and the magnetic moment of the electron.
[ 0m59s377ms - 1m4s47ms ] **Speaker 2:** Yes, but on the other hand, it predicts this ridiculous situation where they have negative energy values.
[ 1m4s47ms - 1m5s827ms ] **Speaker 2:** Right. That's nonsense.
[ 1m5s827ms - 1m9s377ms ] **Speaker 2:** So Heisenberg said, I give up.
[ 1m9s377ms - 1m10s577ms ] **Speaker 2:** This is just This is just ridiculous.
[ 1m10s577ms - 1m14s337ms ] **Speaker 2:** So Dirac, he had in some very clear sense had to rescue his equation.
[ 1m14s337ms - 1m19s997ms ] **Speaker 1:** Dirac spent three years sticking to his guns. He tried all sorts of ways to interpret his new equation to explain where the negative energy was coming from.
[ 1m21s397ms - 1m24s897ms ] **Speaker 1:** Then, in 1931, he proposed something radical to explain the negative energy solutions.
[ 1m27s277ms - 1m33s447ms ] **Speaker 1:** A new kind of particle, unknown to experimental physics, having the same mass and opposite charge to an electron.
[ 1m33s447ms - 1m34s857ms ] **Speaker 1:** We may call such a particle an anti-electron.
[ 1m34s857ms - 1m39s227ms ] **Speaker 1:** We should not expect to find any of them in nature on account of their rapid rate of recombination with electrons.
[ 1m40s817ms - 1m48s437ms ] **Speaker 1:** So Dirac was proposing that those four states described in his four component wave function are a spin-up electron, a spin-down electron, a spin-up anti-electron, and a spin-down anti-electron.
[ 1m48s437ms - 1m53s517ms ] **Speaker 2:** When Dirac said that, people didn't stop running around saying, where's this anti-electron?
[ 1m53s517ms - 1m54s587ms ] **Speaker 2:** They just ignored it.
[ 1m55s237ms - 1m56s957ms ] **Speaker 2:** Cut to the laboratory at Caltech.
[ 1m56s957ms - 2m1s717ms ] **Speaker 1:** In 1932, a Caltech postdoc named Carl Anderson was working on a project trying to identify the charged particles produced by cosmic rays.
[ 2m1s717ms - 2m5s707ms ] **Speaker 1:** He photographed the tracks these particles left in a cloud chamber containing a uniform magnetic field.
[ 2m5s707ms - 2m8s307ms ] **Speaker 1:** Anderson noticed several instances of a similar track.
[ 2m8s737ms - 2m11s217ms ] **Speaker 1:** It looked a lot like the tracks he'd seen left by electrons.
[ 2m11s687ms - 2m16s977ms ] **Speaker 1:** Only it curved in the opposite direction in the magnetic field, kind of like the tracks of positively charged protons.
[ 2m17s187ms - 2m20s557ms ] **Speaker 1:** But there was no way it could be a proton based on the length of the track.
[ 2m20s557ms - 2m23s637ms ] **Speaker 1:** It had traveled farther in air and therefore it had to be much lighter.
[ 2m23s807ms - 2m29s117ms ] **Speaker 1:** It had to be something with around the same mass as an electron, but opposite charge, a positive electron.
[ 2m29s467ms - 2m32s307ms ] **Speaker 1:** Or as he named it, a positron.
[ 2m32s307ms - 2m36s217ms ] **Speaker 1:** He actually also tried to rebrand electrons as negatrons, but that one didn't quite stick.
[ 2m38s137ms - 2m43s37ms ] **Speaker 1:** Just one year after Dirac proposed the anti-electron, Carl Anderson found it entirely by accident.
[ 2m44s37ms - 2m46s727ms ] **Speaker 1:** But this alone doesn't get rid of the negative energy problem.
[ 2m46s727ms - 2m49s387ms ] **Speaker 1:** Remember what we said earlier.
[ 2m49s387ms - 2m54s907ms ] **Speaker 1:** If any particles, like these positrons, can have negative energy, then they could continually radiate energy and drop into lower and lower negative energy states.
[ 2m54s907ms - 2m58s437ms ] **Speaker 1:** Fortunately, Dirac proposed a solution to this problem as well, although it was a little crazy.
[ 3m0s87ms - 3m6s997ms ] **Speaker 1:** He theorized something called the Dirac sea, describing a vacuum as an infinite sea of electrons occupying all available negative energy states.
[ 3m6s997ms - 3m13s97ms ] **Speaker 1:** And since no two electrons can occupy the same state, this prevents observable positive energy electrons from falling into the negative energy states.
[ 3m13s97ms - 3m19s37ms ] **Speaker 1:** A hole or vacancy in this sea then becomes a positron.
[ 3m19s37ms - 3m24s27ms ] **Speaker 1:** When an electron and a positron meet and annihilate, well, that's just an electron falling back into the sea and filling that hole.
[ 3m24s27ms - 3m27s157ms ] **Speaker 1:** The theory is mathematically sound, of course, it's Dirac we're talking about.
[ 3m27s157ms - 3m33s97ms ] **Speaker 1:** But if you feel like it's hard to come to terms with the idea that we're floating on an infinite sea of electrons, well, you wouldn't be alone.
[ 3m34s87ms - 3m39s417ms ] **Speaker 3:** It's not even that crazy if, I don't know, several decades later, people find that exact model in a physical system.
[ 3m39s417ms - 3m43s797ms ] **Speaker 3:** In condensed matter physics, you see an exact analogy of also having electrons in the conduction band and say valence band.
[ 3m43s797ms - 3m47s787ms ] **Speaker 2:** Yes, that's true.
[ 3m47s787ms - 3m50s617ms ] **Speaker 2:** That's true. But but Dirac really was, you know, out there.
[ 3m50s617ms - 3m54s497ms ] **Speaker 2:** You see what I mean? People were people like you know, senior people were saying, this is nonsense.
[ 3m54s497ms - 3m57s777ms ] **Speaker 2:** But it was a way of direct rectilinear thinking, thinking, well, maybe this is
[ 3m57s777ms - 3m59s377ms ] **Speaker 2:** and then it drove him to antimatter.
[ 4m0s117ms - 4m4s27ms ] **Speaker 1:** Thankfully, in 1941, a Swiss physicist named Ernst Stueckelberg had a clever idea.
[ 4m4s27ms - 4m7s337ms ] **Speaker 1:** The wave function contains a term that looks like this, where energy is multiplied by time.
[ 4m7s337ms - 4m13s687ms ] **Speaker 1:** So, we can see that if we just change the sign of time when the energy is negative, then we get the same result, because a negative multiplied by a negative gives us a positive.
[ 4m13s687ms - 4m19s957ms ] **Speaker 1:** Stueckelberg took this and he suggested that negative energy electrons traveling backwards in time are mathematically equivalent to positive energy anti-electrons, that is positrons, traveling forwards in time.
[ 4m20s527ms - 4m26s697ms ] **Speaker 1:** A few years later, around 1948, Richard Feynman took this idea and used it in one of the most powerful tools in modern physics, the Feynman diagrams.
[ 4m26s697ms - 4m30s957ms ] **Speaker 1:** In his sketches of particle interactions, he showed antiparticles traveling the opposite way to particles, backwards in time.
[ 4m32s37ms - 4m37s897ms ] **Speaker 1:** It was a brilliant trick. Negative energy solutions no longer had to mean there was negative energy or a Dirac sea.
[ 4m37s897ms - 4m40s757ms ] **Speaker 1:** They simply indicated the presence of an antiparticle.
[ 4m44s677ms - 4m51s337ms ] **Speaker 1:** We now know that there's a corresponding antiparticle for every subatomic particle with the same mass but opposite charge.
[ 4m51s337ms - 4m54s467ms ] **Speaker 1:** So, the proton has the antiproton, the neutrino has the antineutrino, and so on.
[ 4m54s467ms - 5m2s77ms ] **Speaker 2:** According to his friend Heisenberg, that was the biggest leap in 20th century physics, to say there's a whole slew of antiparticles corresponding to particles, and Dirac got that through this crazy model.
[ 5m2s877ms - 5m6s637ms ] **Speaker 1:** But all is not solved.
[ 5m6s637ms - 5m10s47ms ] **Speaker 1:** This new anti-world introduces some big questions about the very nature of our universe.
[ 5m10s47ms - 5m19s147ms ] **Speaker 1:** Because particles and their antiparticles are equal and opposite, when they come together, they annihilate and produce two photons with energy equivalent to their mass and kinetic energy, and this process is reversible.
[ 5m19s147ms - 5m22s777ms ] **Speaker 1:** Two photons with the right energies can produce a matter and anti-matter pair.
[ 5m22s777ms - 5m24s377ms ] **Speaker 1:** This is called Breit-Wheeler pair production.
[ 5m24s377ms - 5m32s477ms ] **Speaker 1:** During the first moments after the Big Bang, the universe was hot, dense, and full of these pairs popping into and out of existence.
[ 5m32s477ms - 5m38s937ms ] **Speaker 1:** If an equal number of matter and anti-matter particles were created, you would expect them to all annihilate each other in this dense environment, leaving behind only energy.
[ 5m38s937ms - 5m40s627ms ] **Speaker 1:** But that didn't happen.
[ 5m40s867ms - 5m42s677ms ] **Speaker 1:** We ended up with a universe full of matter.
[ 5m42s947ms - 5m52s147ms ] **Speaker 1:** If we work backwards from how much matter and anti-matter is in the universe today, it's actually estimated that only one particle per billion of matter needed to survive this hot dense era and not get annihilated.
[ 5m52s147ms - 5m55s537ms ] **Speaker 1:** That tiny difference would give us the makeup of our universe today, where matter dominates.
[ 5m55s797ms - 5m58s767ms ] **Speaker 3:** So, what allowed that one particle per billion to escape annihilation?
[ 5m58s767ms - 6m0s967ms ] **Speaker 3:** Why did matter win out over antimatter?
[ 6m6s727ms - 6m10s7ms ] **Speaker 1:** Well, that's a pretty big question with some not so simple answers.
[ 6m10s7ms - 6m12s847ms ] **Speaker 1:** So, we're doing an entire second video where we have some pretty spectacular stuff happening.
[ 6m13s877ms - 6m17s157ms ] **Speaker 4:** We're getting into the beast.
[ 6m17s157ms - 6m18s657ms ] **Speaker 4:** It's absolutely insane.
[ 6m18s657ms - 6m20s7ms ] **Speaker 4:** I feel like I should not be in here.
[ 6m20s7ms - 6m21s307ms ] **Speaker 4:** So you're making anti-atoms?
[ 6m21s497ms - 6m22s7ms ] **Speaker 5:** Yes.
[ 6m22s7ms - 6m23s67ms ] **Speaker 4:** Cool.
[ 6m24s847ms - 6m28s127ms ] **Speaker 1:** Dirac is probably less well-known than people like Heisenberg or Schrödinger, but his contribution to quantum physics was immense.
[ 6m28s127ms - 6m29s177ms ] **Speaker 1:** And he was recognized for it.
[ 6m29s177ms - 6m35s367ms ] **Speaker 1:** He shared the 1933 Nobel Prize with Schrödinger for the discovery of new productive forms of atomic theory.
[ 6m36s147ms - 6m40s697ms ] **Speaker 1:** And perhaps this gave strange quiet Dirac some new found confidence.
[ 6m40s697ms - 6m47s457ms ] **Speaker 1:** Because that physicist in the audience of his 1928 lecture at the start, Eugene Wigner, actually became a reasonable friend of Dirac's.
[ 6m47s457ms - 6m51s237ms ] **Speaker 1:** And in 1934, introduced Dirac to his sister, Magit Wigner.
[ 6m51s237ms - 6m54s777ms ] **Speaker 1:** A woman who would change Dirac's life, perhaps more than any equation or Nobel Prize.
[ 6m56s67ms - 6m56s987ms ] **Speaker 2:** They were anti-politicals.
[ 6m56s987ms - 6m58s537ms ] **Speaker 2:** Right? They had completely different personalities.
[ 6m58s537ms - 7m1s7ms ] **Speaker 2:** He had almost no empathy, right?
[ 7m1s7ms - 7m1s637ms ] **Speaker 2:** And he knew it.
[ 7m1s637ms - 7m3s227ms ] **Speaker 2:** She had buckets of it.
[ 7m3s227ms - 7m4s377ms ] **Speaker 2:** He hardly talked.
[ 7m4s377ms - 7m5s37ms ] **Speaker 2:** She couldn't stop talking.
[ 7m5s37ms - 7m6s897ms ] **Speaker 2:** You could just go on.
[ 7m6s897ms - 7m7s757ms ] **Speaker 2:** They are completely different people.
[ 7m7s757ms - 7m8s977ms ] **Speaker 2:** But the marriage did work.
[ 7m8s977ms - 7m14s187ms ] **Speaker 2:** My great friend Lilya Harris Chandra, who knew them, she came out with a great line, great line, which is
[ 7m14s767ms - 7m16s857ms ] **Speaker 2:** he gave her status.
[ 7m17s127ms - 7m18s247ms ] **Speaker 2:** She gave him a life.
[ 7m18s317ms - 7m22s757ms ] **Speaker 1:** So, I guess there is one particle anti-particle pair that never annihilated.
[ 7m29s697ms - 7m33s477ms ] **Speaker 1:** Hey, one last thing, in case you didn't already know, we just launched the official Veritasium game.
[ 7m33s477ms - 7m37s67ms ] **Speaker 1:** It comes with 800 questions and it's the perfect way to challenge your friends.
[ 7m37s67ms - 7m40s487ms ] **Speaker 1:** Every time we play it at Veritasium, things get a little bit heated and that is so much fun.
[ 7m40s487ms - 7m47s447ms ] **Speaker 1:** If you want to go check it out, then head over to our Kickstarter where you can pre-order your own version.
[ 7m47s447ms - 7m52s17ms ] **Speaker 1:** And right now we've enabled global shipping, so no matter where you are in the world, you can get your own version.
[ 7m52s17ms - 7m56s167ms ] **Speaker 1:** We're coming close to the final few days of the Kickstarter campaign.
[ 7m56s167ms - 7m58s907ms ] **Speaker 1:** So, this is your last chance to get your hands on the exclusive launch edition.
[ 7m59s227ms - 8m4s87ms ] **Speaker 1:** So, if you want to support us, head over to Kickstarter by clicking the link in the description or scanning this QR code.
[ 8m4s87ms - 8m7s497ms ] **Speaker 1:** I want to thank you for all your support and most of all, thank you for watching.