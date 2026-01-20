---
title: Veritasium_There Is Something Faster Than Light_20251219_part1
audio_file: Veritasium_There Is Something Faster Than Light_20251219_part1.mp3
note_id: 9c570023-db2d-474b-bf8a-8ffb88a3cfa3
date_processed: '2026-01-06'
classification:
  primary_domain: Physics
  sub_domains:
  - Quantum Mechanics
  - Relativity
  - History of Science
  - Philosophy of Science
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people:
  - name: Albert Einstein
    role: Physicist
    contribution: Proposed thought experiments on speed limit and non‑locality; developed
      relativity; criticized Copenhagen interpretation
  - name: Niels Bohr
    role: Physicist
    contribution: Defended Copenhagen interpretation; responded to Einstein’s challenge
      at the 1927 Solvay conference
  - name: Werner Heisenberg
    role: Physicist
    contribution: Mentioned as a disciple of Bohr; associated with uncertainty principle
  - name: Erwin Schrödinger
    role: Physicist
    contribution: Recipient of Einstein’s letter calling Copenhagen a "tranquilizing
      philosophy"
  - name: Adam Becker
    role: Author
    contribution: Wrote *What Is Real*; quoted in the video
  - name: Speaker 1
    role: Narrator
    contribution: Provides main exposition throughout the transcript
  - name: Speaker 2
    role: Narrator
    contribution: Comments on faster‑than‑light actions
  - name: Speaker 3
    role: Commentator
    contribution: Explains Copenhagen interpretation and Schrödinger equation
  - name: Speaker 4
    role: Commentator
    contribution: Echoes point about wave function as complete knowledge
  - name: Speaker 5
    role: Commentator
    contribution: Summarizes popular story of Einstein–Bohr debate
  works_cited:
  - title: What Is Real
    author: Adam Becker
    year: null
  concepts_mentioned:
  - Quantum mechanics
  - Speed of light universal limit
  - Action at a distance
  - General relativity
  - Wave function
  - Wave function collapse
  - Non‑locality
  - Copenhagen interpretation
  - Thought experiment
  laws_theories_cited:
  - Special relativity
  - General relativity
  - Newton's law of universal gravitation (instant action)
  - Quantum mechanics
  - Copenhagen interpretation
  - Heisenberg uncertainty principle (implied)
  - Einstein's equivalence principle (implied)
concepts:
- name: Speed of Light Limit
  definition: The principle that no information or physical influence can travel faster
    than the constant speed c (~3×10⁸ m/s).
  parent_concepts:
  - Relativity
  related_concepts:
  - General Relativity
  - Causality
  - Non‑locality
  abstraction_level: Fundamental
  confidence: 1.0
- name: General Relativity
  definition: Einstein's theory describing gravity as the curvature of spacetime caused
    by mass‑energy, with changes propagating at the speed of light.
  parent_concepts:
  - Relativity
  related_concepts:
  - Speed of Light Limit
  - Gravity
  - Spacetime
  abstraction_level: Theoretical
  confidence: 1.0
- name: Quantum Mechanics
  definition: A physical theory that describes microscopic systems using wave functions,
    probabilities, and inherent uncertainty.
  parent_concepts:
  - Physics
  related_concepts:
  - Wave Function
  - Copenhagen Interpretation
  - Non‑locality
  abstraction_level: Fundamental
  confidence: 1.0
- name: Wave Function Collapse
  definition: The postulated instantaneous reduction of a quantum system’s wave function
    to a single outcome upon measurement.
  parent_concepts:
  - Quantum Mechanics
  related_concepts:
  - Non‑locality
  - Copenhagen Interpretation
  - Measurement Problem
  abstraction_level: Theoretical
  confidence: 0.95
- name: Non‑locality
  definition: The phenomenon where a change in one location appears to affect another
    location instantaneously, violating classical locality.
  parent_concepts:
  - Quantum Mechanics
  related_concepts:
  - Wave Function Collapse
  - Einstein's Thought Experiment
  - Copenhagen Interpretation
  abstraction_level: Theoretical
  confidence: 0.95
- name: Copenhagen Interpretation
  definition: A philosophical framework for quantum mechanics stating that the wave
    function encodes all knowable information and that physical properties are defined
    only upon measurement.
  parent_concepts:
  - Quantum Mechanics
  related_concepts:
  - Wave Function
  - Measurement Problem
  - Einstein
  abstraction_level: Philosophical
  confidence: 0.95
- name: Thought Experiment
  definition: A hypothetical scenario used to explore the implications of a theory
    without performing a physical experiment.
  parent_concepts:
  - Methodology
  related_concepts:
  - Einstein
  - Quantum Mechanics
  - Relativity
  abstraction_level: Applied
  confidence: 1.0
relationships:
- source_concept: Quantum Mechanics
  target_concept: Non‑locality
  relationship_type: supports
  strength: 0.96
  evidence: Transcript states quantum mechanics requires instant influences across
    distance, violating locality.
  reasoning: The description of wave function collapse as instantaneous implies non‑local
    behavior.
- source_concept: General Relativity
  target_concept: Speed of Light Limit
  relationship_type: enforces
  strength: 1.0
  evidence: Einstein’s theory makes gravity propagate at light speed, ensuring cause‑effect
    order.
  reasoning: GR predicts gravitational changes travel as ripples at c, upholding the
    universal speed limit.
- source_concept: Einstein's Thought Experiment
  target_concept: Copenhagen Interpretation
  relationship_type: contradicts
  strength: 0.92
  evidence: Einstein used the experiment to expose a weakness in Copenhagen, arguing
    collapse is non‑local.
  reasoning: His challenge directly opposes the Copenhagen view that the wave function
    is complete.
- source_concept: Wave Function Collapse
  target_concept: Non‑locality
  relationship_type: causes
  strength: 0.95
  evidence: Collapse is described as instantaneous across any distance.
  reasoning: Instantaneous collapse creates effects that are non‑local.
- source_concept: Newton's Instantaneous Gravity
  target_concept: Speed of Light Limit
  relationship_type: contradicts
  strength: 0.88
  evidence: Transcript notes Newton's theory says gravity acts instantly, which conflicts
    with the later‑established light‑speed limit.
  reasoning: Instant action violates the relativistic speed limit.
- source_concept: Copenhagen Interpretation
  target_concept: Wave Function
  relationship_type: equivalent_to
  strength: 0.9
  evidence: Bohr’s view that the wave function is all physics can tell us.
  reasoning: Interpretation treats the wave function as the complete description of
    a system.
cross_domain_insights:
- connection_type: structural_analogy|principle_application
  source_domain: Physics
  source_concept: Speed of Light Limit
  target_domain: Computer Science / Distributed Systems
  target_concept: Maximum message propagation latency (speed of light in fiber) and
    causality constraints in distributed algorithms
  insight: The universal speed limit for information in relativity directly mirrors
    the hard latency floor in wide‑area networks, shaping how consistency and consensus
    protocols are designed.
  explanation: Both domains treat information carriers as moving through a medium
    with a finite maximum velocity, which imposes a light‑cone‑like causal structure.
    In distributed systems this translates into the impossibility of instantaneous
    state agreement, forcing algorithms like Paxos or Raft to respect latency bounds.
  potential_applications:
  - Design of low‑latency financial trading platforms that account for geographic
    light‑cone delays
  - Improved fault‑tolerant consensus mechanisms for blockchain networks spanning
    continents
  confidence: 0.92
  historical_example: The 1975 "Lamport's Logical Clocks" paper explicitly modeled
    causality using a partial ordering analogous to relativistic light cones.
- connection_type: principle_application|metaphor
  source_domain: Physics
  source_concept: Wave Function Collapse
  target_domain: Behavioral Economics
  target_concept: 'Decision collapse: a probability distribution over consumer choices
    resolves into a single purchase once observed'
  insight: Quantum collapse provides a vivid metaphor for how a latent preference
    distribution becomes a concrete choice when a decision point is observed.
  explanation: Both involve a superposition of potential outcomes that remain uncommitted
    until an act of measurement (or choice) forces a single outcome, aligning with
    Bayesian updating where prior probabilities are replaced by a posterior certainty.
  potential_applications:
  - Modeling consumer behavior in online A/B testing as a quantum‑like collapse process
  - Designing marketing interventions that act as 'measurements' to steer choice probabilities
  confidence: 0.87
  historical_example: Kahneman and Tversky's prospect theory (1979) introduced the
    idea of a mental 'measurement' that fixes a gamble's perceived value, echoing
    collapse.
- connection_type: structural_analogy|historical_precedent
  source_domain: Physics
  source_concept: General Relativity – curvature of spacetime
  target_domain: Urban Economics / Geography
  target_concept: Economic potential fields where curvature represents market density
    and transport costs
  insight: The geometric language of GR can be repurposed to describe how economic
    activity bends the 'cost landscape', guiding flows of goods and people much like
    geodesics guide particle trajectories.
  explanation: In GR mass-energy tells spacetime how to curve; analogously, agglomerations
    of economic activity generate gradients in transportation cost, dictating optimal
    routes (geodesics) for logistics and commuting.
  potential_applications:
  - Simulation tools that treat cities as curved manifolds to predict traffic patterns
  - Policy analysis of how new infrastructure reshapes the economic curvature and
    thus regional inequality
  confidence: 0.81
  historical_example: Walter Christaller's Central Place Theory (1933) used a spatial
    field analogy that prefigured later curvature‑based models.
- connection_type: principle_application|metaphor
  source_domain: Physics
  source_concept: Quantum Non‑locality (Entanglement)
  target_domain: Sociology / Network Science
  target_concept: Instantaneous correlation of opinions or behaviors across distant
    nodes in social networks
  insight: Entanglement illustrates how distant entities can exhibit correlated outcomes
    without a mediating signal, mirroring phenomena like viral meme spread where distant
    individuals align their actions simultaneously.
  explanation: Both systems display correlations that cannot be explained by local,
    step‑by‑step transmission; instead, a shared underlying state (quantum or cultural)
    enforces synchrony, useful for modeling emergent consensus.
  potential_applications:
  - Design of influence‑maximization algorithms that exploit pre‑existing entangled
    sub‑communities
  - Understanding rapid coordination in decentralized activist movements
  confidence: 0.78
  historical_example: The 1970s "small‑world" experiments by Milgram hinted at non‑local
    shortcuts in social graphs, later formalized in Watts‑Strogatz network models.
- connection_type: thought_experiment|principle_application
  source_domain: Physics
  source_concept: Thought Experiment (e.g., Schrödinger's cat)
  target_domain: Public Policy / Ethics
  target_concept: Scenario planning and moral imagination for future technologies
  insight: Physics' disciplined use of imagined setups to probe theoretical limits
    parallels policy makers' use of hypothetical futures to test ethical frameworks.
  explanation: Both employ a controlled mental sandbox where variables are isolated,
    allowing stakeholders to explore consequences without real‑world risk, thereby
    sharpening reasoning about uncertainty and responsibility.
  potential_applications:
  - Structured foresight workshops for AI governance using Schrödinger‑style paradoxes
  - Ethical audits that frame climate‑impact decisions as quantum‑style superpositions
    of outcomes
  confidence: 0.84
  historical_example: The 1945 "Einstein‑Podolsky‑Rosen" thought experiment inspired
    later policy‑level debates on privacy and surveillance in the digital age.
bridge_concepts:
- concept: Causality
  appears_in_domains:
  - Physics
  - Computer Science
  - Law
  role: Defines permissible ordering of events; in physics via light cones, in computing
    via happens‑before relations, in law via liability chains.
  examples:
  - Relativistic light cone
  - Lamport's logical clock
  - Chain of causation in tort law
- concept: Probability Distribution
  appears_in_domains:
  - Quantum Mechanics
  - Economics
  - Machine Learning
  role: Represents superposed possibilities that resolve upon observation or decision.
  examples:
  - Wave function before collapse
  - Consumer choice model
  - Predictive model output probabilities
- concept: Curvature
  appears_in_domains:
  - General Relativity
  - Geography
  - Network Science
  role: Quantifies how a space deviates from flatness, influencing paths of least
    action.
  examples:
  - Spacetime around a massive body
  - Economic potential field in a city
  - Graph curvature affecting diffusion dynamics
mental_models:
- name: First‑Principles Decomposition
  description: Breaking a problem down to its most fundamental, indisputable truths
    before rebuilding a solution.
  applied_to:
  - Deriving the speed‑of‑light limit from Lorentz invariance
  - Analyzing market frictions by stripping to transport cost fundamentals
  transferable_to:
  - Engineering design
  - Strategic business planning
  - Policy formulation
- name: Thought Experiment
  description: A purely mental scenario used to explore the implications of a theory
    without physical execution.
  applied_to:
  - Schrödinger's cat illustrating superposition
  - Policy scenario planning for autonomous weapons
  transferable_to:
  - Ethics workshops
  - Risk assessment
  - Innovation brainstorming
- name: Bayesian Updating (Probability Collapse)
  description: Revising beliefs in light of new evidence, mathematically analogous
    to wave function collapse.
  applied_to:
  - Quantum measurement formalism
  - Consumer choice revision after price reveal
  transferable_to:
  - Medical diagnosis
  - Financial forecasting
  - Machine learning inference
analogies_used:
- source_domain: Everyday Traffic
  source_concept: Speed limit signs
  target_domain: Physics
  target_concept: Speed of Light as universal speed limit
  mapping:
    Speed limit sign: Invariant speed c
    Roadway: Spacetime manifold
    Vehicle: Information carrier
  pedagogical_value: Leverages intuitive understanding of traffic rules to convey
    why no object can exceed c, reinforcing the notion of causality constraints.
- source_domain: Dice Rolling
  source_concept: Outcome becomes known only after the roll is observed
  target_domain: Physics
  target_concept: Wave function collapse upon measurement
  mapping:
    Dice faces: Quantum superposition states
    Roll: Measurement interaction
    Visible result: Collapsed eigenstate
  pedagogical_value: Maps a familiar random process to quantum uncertainty, helping
    learners grasp why observation forces a single reality.
tags:
  hierarchical:
  - '#Physics → #Quantum Mechanics → #Wave Function Collapse'
  - '#Physics → #Relativity → #General Relativity'
  - '#Physics → #Philosophy of Science → #Copenhagen Interpretation'
  - '#Physics → #Methodology → #Thought Experiment'
  topical:
  - '#SpeedOfLight'
  - '#NonLocality'
  - '#Gravity'
  - '#MeasurementProblem'
  methodological:
  - '#ThoughtExperiment'
  - '#HistoricalNarrative'
  - '#PhilosophicalDebate'
  people:
  - '#AlbertEinstein'
  - '#NielsBohr'
  - '#ErwinSchrödinger'
  - '#AdamBecker'
  concepts:
  - '#QuantumMechanics'
  - '#GeneralRelativity'
  - '#WaveFunction'
  - '#WaveFunctionCollapse'
  - '#CopenhagenInterpretation'
  temporal:
  - '#1927SolvayConference'
  - '#1935ThoughtExperiment'
  - '#1905EinsteinPaper'
  - '#2025VideoRelease'
summary: ''
key_ideas: []
---
## Key Concepts

**Speed of Light Limit**  
The principle that no information or physical influence can travel faster than the constant speed c (~3×10⁸ m/s).

**General Relativity**  
Einstein's theory describing gravity as the curvature of spacetime caused by mass‑energy, with changes propagating at the speed of light.

**Quantum Mechanics**  
A physical theory that describes microscopic systems using wave functions, probabilities, and inherent uncertainty.

**Wave Function Collapse**  
The postulated instantaneous reduction of a quantum system’s wave function to a single outcome upon measurement.

**Non‑locality**  
The phenomenon where a change in one location appears to affect another location instantaneously, violating classical locality.

## Cross-Domain Connections

**Physics → Computer Science / Distributed Systems**

*The universal speed limit for information in relativity directly mirrors the hard latency floor in wide‑area networks, shaping how consistency and consensus protocols are designed.*

Both domains treat information carriers as moving through a medium with a finite maximum velocity, which imposes a light‑cone‑like causal structure. In distributed systems this translates into the impossibility of instantaneous state agreement, forcing algorithms like Paxos or Raft to respect latency bounds.

**Physics → Behavioral Economics**

*Quantum collapse provides a vivid metaphor for how a latent preference distribution becomes a concrete choice when a decision point is observed.*

Both involve a superposition of potential outcomes that remain uncommitted until an act of measurement (or choice) forces a single outcome, aligning with Bayesian updating where prior probabilities are replaced by a posterior certainty.

**Physics → Urban Economics / Geography**

*The geometric language of GR can be repurposed to describe how economic activity bends the 'cost landscape', guiding flows of goods and people much like geodesics guide particle trajectories.*

In GR mass-energy tells spacetime how to curve; analogously, agglomerations of economic activity generate gradients in transportation cost, dictating optimal routes (geodesics) for logistics and commuting.

## Full Transcription



[ 0m0s117ms - 0m3s377ms ] Speaker 1: In 1935, Einstein came up with a thought experiment that showed quantum mechanics breaks one of the most sacred principles in physics, that nothing can go faster than the speed of light.
[ 0m3s667ms - 0m14s367ms ] Speaker 1: Physicists assumed he was wrong. They thought that at 56, Einstein was an old man, past his prime, and just unable to accept the new theory of physics because it was too radical.
[ 0m14s637ms - 0m19s997ms ] Speaker 1: But 30 years later, one man stumbled across Einstein's forgotten paper when he realized something. The prediction could actually be tested.
[ 0m20s427ms - 0m23s267ms ] Speaker 1: When scientists ran the experiment, they were shocked.
[ 0m23s267ms - 0m26s737ms ] Speaker 1: Quantum physics really does break the universal speed limit.
[ 0m26s937ms - 0m30s377ms ] Speaker 2: We are obliged to invoke something like actions going faster than light.
[ 0m30s377ms - 0m31s777ms ] Speaker 2: from one place to another.
[ 0m32s377ms - 0m38s87ms ] Speaker 1: This is a video about one of the spookiest and most misunderstood experiments in all of physics.
[ 0m38s367ms - 0m41s967ms ] Speaker 1: And it might even be the strongest evidence we have that we live in many worlds.
[ 0m45s367ms - 0m48s997ms ] Speaker 1: If the sun were to disappear all of a sudden, how long would it take until we noticed and were released out into space?
[ 0m49s97ms - 0m52s897ms ] Speaker 1: Newton's theory says that gravity acts instantly across any distance.
[ 0m53s57ms - 0m55s237ms ] Speaker 1: So, if there's a change in gravity, we should feel it immediately.
[ 0m56s167ms - 0m57s717ms ] Speaker 1: But Newton himself was disturbed by this.
[ 0m58s307ms - 1m4s377ms ] Speaker 1: That one body may act upon another at a distance is to me so great an absurdity that I believe no man who has a competent faculty of thinking can ever fall into it.
[ 1m6s387ms - 1m10s7ms ] Speaker 1: But in 1905, Einstein realized action at a distance isn't just absurd.
[ 1m10s337ms - 1m12s227ms ] Speaker 1: It leads to outright paradoxes.
[ 1m13s127ms - 1m16s387ms ] Speaker 1: Einstein had discovered that observers moving at different speeds can disagree about when events happened.
[ 1m16s887ms - 1m21s347ms ] Speaker 1: Let's say you see two things happen at the same time, an observer speeding past would see it differently.
[ 1m21s347ms - 1m25s787ms ] Speaker 1: To them, one of these happened first, and both points of view are equally valid.
[ 1m26s77ms - 1m27s687ms ] Speaker 1: But in the case of gravity, this leads to disaster.
[ 1m28s197ms - 1m30s957ms ] Speaker 1: Say you see the sun disappearing and Earth flying off at the same time, as Newton predicted.
[ 1m31s437ms - 1m37s207ms ] Speaker 1: Then, the other observer sees something impossible. They see the Earth flying off first, even while the sun is still there, and it should, of course, be pulling the Earth in.
[ 1m37s207ms - 1m38s997ms ] Speaker 1: So to them, it looks like cause and effect are reversed.
[ 1m39s207ms - 1m42s657ms ] Speaker 1: The only way out of this paradox is to reject the assumption we started with, so gravity can't be instant.
[ 1m44s387ms - 1m48s137ms ] Speaker 1: It took Einstein 10 years to fix this issue, and in the process, he completely overhauled our understanding of gravity.
[ 1m49s317ms - 1m50s677ms ] Speaker 1: Gravity is caused by the bending of space-time.
[ 1m51s237ms - 1m56s397ms ] Speaker 1: When there's a change in gravity, that only affects the local space-time, and then that ripple spreads out to nearby regions, which spread farther out until eventually they reach us.
[ 1m56s657ms - 2m0s987ms ] Speaker 1: This theory of gravity is local because effects spread from place to place at the speed of light, instead of being instant.
[ 2m1s487ms - 2m4s187ms ] Speaker 1: From our frame of reference, if the sun disappeared, that ripple would take about 8 minutes to reach us.
[ 2m4s677ms - 2m9s47ms ] Speaker 1: Another observer might disagree about the length of the delay, but now we all agree that the sun disappeared first.
[ 2m9s277ms - 2m11s407ms ] Speaker 1: This is why nothing can go faster than light.
[ 2m11s407ms - 2m14s337ms ] Speaker 1: The delay between cause and effect ensures all observers agree on the order.
[ 2m14s637ms - 2m17s187ms ] Speaker 1: After Einstein fixed gravity, all of classical physics obeyed this important rule.
[ 2m17s547ms - 2m21s307ms ] Speaker 1: But then, Einstein studied the new theory of quantum mechanics and made a terrible discovery.
[ 2m23s827ms - 2m26s707ms ] Speaker 1: This is one of the most famous photographs in physics.
[ 2m26s967ms - 2m31s97ms ] Speaker 1: It was taken at the 1927 Solvay conference, where the architects of the brand new quantum theory gathered to discuss it.
[ 2m31s527ms - 2m34s857ms ] Speaker 1: Around 60% of the attendees would win Nobel prizes.
[ 2m34s857ms - 2m38s577ms ] Speaker 1: But Einstein thought they'd gotten something fundamentally wrong, and this was his chance to prove it.
[ 2m38s847ms - 2m40s777ms ] Speaker 1: So he took to the stage with a thought experiment.
[ 2m41s107ms - 2m44s877ms ] Speaker 1: Imagine you fire a single electron through a narrow slit toward a circular detection screen.
[ 2m45s187ms - 2m50s637ms ] Speaker 1: Well, quantum mechanics says that this electron has some sort of wave associated with it, called a wave function, which spreads out through space as it travels.
[ 2m51s37ms - 2m52s897ms ] Speaker 1: When the electron hits the screen, you detect it at a single point.
[ 2m53s597ms - 2m55s907ms ] Speaker 1: Where it turns up depends on the amplitude of the wave.
[ 2m56s347ms - 2m59s477ms ] Speaker 1: If the wave is very big in a particular area, the electron is more likely to turn up there.
[ 2m59s477ms - 3m0s967ms ] Speaker 1: Let's say it appears here.
[ 3m1s257ms - 3m2s187ms ] Speaker 1: So far, everyone was following.
[ 3m2s577ms - 3m4s137ms ] Speaker 1: This is what quantum mechanics predicts.
[ 3m4s337ms - 3m6s407ms ] Speaker 1: But Einstein's next question surprised them.
[ 3m6s727ms - 3m9s277ms ] Speaker 1: Why doesn't the electron turn up at this other spot a moment later?
[ 3m9s707ms - 3m11s437ms ] Speaker 1: There's only one electron so we can't detect it twice.
[ 3m11s677ms - 3m17s227ms ] Speaker 1: But the way quantum mechanics ensures this is that when the electron was detected at the first spot, its wave function collapsed to zero everywhere else instantly.
[ 3m17s677ms - 3m18s967ms ] Speaker 1: That's why the probability of finding it at the second spot is now zero.
[ 3m19s187ms - 3m20s597ms ] Speaker 1: There's no longer any wave there.
[ 3m21s347ms - 3m24s817ms ] Speaker 1: But Einstein asked the audience to think about what this means.
[ 3m25s277ms - 3m28s127ms ] Speaker 1: The measurement here must instantly affect the wave function over here.
[ 3m28s487ms - 3m30s377ms ] Speaker 1: No matter how far apart these locations are.
[ 3m30s557ms - 3m33s987ms ] Speaker 1: In other words, quantum mechanics requires instant influences across distance.
[ 3m33s987ms - 3m35s347ms ] Speaker 1: It violates locality.
[ 3m36s547ms - 3m40s297ms ] Speaker 1: Einstein concluded his talk by saying this is an entirely peculiar mechanism of action at a distance.
[ 3m40s627ms - 3m43s757ms ] Speaker 1: And that this implies to my mind a contradiction with the postulate of relativity.
[ 3m44s397ms - 3m48s177ms ] Speaker 1: Einstein's argument was so simple and his talk so short that people didn't know what to make of it.
[ 3m48s577ms - 3m54s557ms ] Speaker 1: One audience member said, "I feel myself in a very difficult position because I don't understand what precisely is the point which Einstein wants to make. No doubt, it is my fault.
[ 3m54s767ms - 3m58s967ms ] Speaker 1: That man was Niels Bohr, the most influential figure in quantum physics at the time.
[ 4m4s337ms - 4m6s707ms ] Speaker 1: Bohr's institute in Copenhagen had become the hub for the new field.
[ 4m6s707ms - 4m8s997ms ] Speaker 1: Dozens of young scientists like Werner Heisenberg came to learn from him.
[ 4m9s367ms - 4m14s337ms ] Speaker 1: As one of his disciples remembers, Bohr had invited a number of us to his home where we sat close to him, some literally at his feet on the floor so as not to miss a word.
[ 4m15s67ms - 4m19s47ms ] Speaker 1: Bohr wasn't the one who wrote the mathematical rules of quantum mechanics.
[ 4m19s457ms - 4m22s7ms ] Speaker 1: Instead, he told everyone what they meant. While others were confused by the theory, Bohr offered answers.
[ 4m22s197ms - 4m25s7ms ] Speaker 1: His philosophy became known as the Copenhagen interpretation of quantum mechanics.
[ 4m26s161ms - 4m33s31ms ] Speaker 3: My general understanding of the Copenhagen interpretation is, you have the wave function, it describes everything that you can know about a particle or a system, and it evolves according to the Schrödiner equation.
[ 4m33s31ms - 4m36s271ms ] Speaker 3: And at some point, you're going to make a measurement, and at that point, the wave function collapses.
[ 4m36s461ms - 4m40s981ms ] Speaker 4: And I think that one bit of that that you said was like, the wave function is all you can know about the particle.
[ 4m40s981ms - 4m42s911ms ] Speaker 4: And I think that was like a pretty important point to Bohr.
[ 4m43s461ms - 4m46s841ms ] Speaker 1: As Bohr would put it, it's wrong to think that the task of physics is to find out how nature is.
[ 4m47s501ms - 4m50s671ms ] Speaker 1: The job of physics is just to predict measurements in the lab, which quantum mechanics does incredibly well.
[ 4m51s101ms - 4m55s681ms ] Speaker 1: As for what the electron is doing when you're not looking, well, to Bohr, that question didn't even make sense to ask.
[ 4m55s981ms - 4m58s511ms ] Speaker 1: The wave function tells you everything physics can or should tell you.
[ 4m58s761ms - 5m0s981ms ] Speaker 1: Einstein couldn't stand the Copenhagen interpretation.
[ 5m1s211ms - 5m4s91ms ] Speaker 1: In a letter to his ally Schrödinger, he called it a tranquilizing philosophy or religion.
[ 5m4s831ms - 5m9s341ms ] Speaker 1: Einstein felt his thought experiment exposed a critical weakness in the Copenhagen interpretation.
[ 5m9s571ms - 5m13s71ms ] Speaker 1: He'd shown that the way the wave function collapses is non-local, and so he reasoned, maybe the wave function is the problem.
[ 5m13s531ms - 5m16s881ms ] Speaker 1: Maybe it's not the best way to describe the electron after all.
[ 5m17s181ms - 5m20s571ms ] Speaker 1: He may not have convinced Bohr of this during his talk, but he was determined to do it during the rest of the conference.
[ 5m23s218ms - 5m26s848ms ] Speaker 5: Physicists tell a version of this story. You know, that you will find in physics textbooks.
[ 5m27s158ms - 5m32s378ms ] Speaker 5: And in pop science books and that, you know, physicists tell amongst ourselves, that what happened was,
[ 5m33s8ms - 5m37s8ms ] Speaker 5: Einstein and Bohr had a great debate, and Einstein was unhappy with quantum mechanics.
[ 5m37s8ms - 5m39s868ms ] Speaker 5: Because it was fundamentally probabilistic.
[ 5m39s998ms - 5m45s378ms ] Speaker 5: He tried to show that there were conceivable experiments that you could use to get around those uncertainty relations. And Bohr showed over and over and over again that you couldn't do that.
[ 5m45s738ms - 5m48s238ms ] Speaker 5: And eventually, everybody agreed with Bohr.
[ 5m50s8ms - 5m53s868ms ] Speaker 1: That's Adam Becker, author of What Is Real, a great book about the history of quantum mechanics.
[ 5m53s868ms - 5m58s308ms ] Speaker 1: As he explained to us, Bohr may have just misunderstood the purpose of Einstein's thought experiments.
[ 5m58s508ms - 6m2s578ms ] Speaker 1: We have documented evidence of this in at least one case. Einstein described a thought experiment that involved a box of photons and a mirror.
[ 6m2s788ms - 6m5s638ms ] Speaker 1: Its purpose was to show the non-locality of the Copenhagen interpretation in action.
[ 6m7s108ms - 6m8s128ms ] Speaker 5: Bohr just misunderstood it.
[ 6m8s128ms - 6m16s628ms ] Speaker 5: And when he recounted it to others later on, he drew a little diagram of what Einstein's thought experiment setup was, and it just didn't have the mirror in it at all.
[ 6m17s38ms - 6m19s148ms ] Speaker 5: And yet, this is taken as like the great victory.
[ 6m19s148ms - 6m23s148ms ] Speaker 5: for Bohr over Einstein, which is crazy, but history is written by the victors, right?
[ 6m23s838ms - 6m27s368ms ] Speaker 1: To understand what Einstein was arguing for, think of the relationship between Newton's gravity and general relativity.
[ 6m27s668ms - 6m31s478ms ] Speaker 1: Newton's theory works well in most situations, but in that theory, gravity is a non-local force, leading to paradoxes.
[ 6m31s848ms - 6m34s748ms ] Speaker 1: This was the motivation for coming up with Einstein's general relativity, which is local.
[ 6m35s308ms - 6m39s598ms ] Speaker 1: Einstein believed the same logic applied to quantum mechanics. His thought experiment revealed that quantum theory is non-local.
[ 6m39s888ms - 6m42s718ms ] Speaker 1: So, just like with Newton's gravity, quantum mechanics must not be the final theory.
[ 6m42s968ms - 6m44s458ms ] Speaker 1: There must be a local one that will replace it.
[ 6m44s798ms - 6m47s578ms ] Speaker 1: And as a bonus, he thought, this new theory might even unify gravity with the quantum world.
[ 6m47s796ms - 6m50s566ms ] Speaker 3: would be hard to imagine coming to the final theory right away.
[ 6m50s566ms - 6m54s596ms ] Speaker 3: And and yeah, and the fact that you can see paradoxes like this would make you think there's got to be more to it that we just don't have yet.
[ 6m54s746ms - 6m55s126ms ] Speaker 4: Absolutely.
[ 6m55s216ms - 6m57s566ms ] Speaker 1: But Einstein hadn't even persuaded Bohr that quantum mechanics really is non-local.
[ 6m57s816ms - 7m2s416ms ] Speaker 1: So in 1935, he made one last attempt to convince the community that there was a contradiction between quantum mechanics and relativity.
[ 7m2s676ms - 7m8s296ms ] Speaker 1: With the help of two younger colleagues, Boris Podolsky and Nathan Rosen, he formulated another, even more striking thought experiment that shows the non-locality of quantum mechanics.
[ 7m8s556ms - 7m10s406ms ] Speaker 1: This paper is now known as the EPR paper, after its authors.
[ 7m14s356ms - 7m16s716ms ] Speaker 1: Here is a simplified version of their thought experiment.
[ 7m17s126ms - 7m21s336ms ] Speaker 1: Imagine a single high-energy photon suddenly becomes two particles.
[ 7m21s596ms - 7m25s76ms ] Speaker 1: One of them is an electron, and to conserve total charge, the other is a positron.
[ 7m25s296ms - 7m26s696ms ] Speaker 1: Since one is negative and the other is positive, they cancel out.
[ 7m27s156ms - 7m29s196ms ] Speaker 1: But both electrons and positrons have a property called spin.
[ 7m29s446ms - 7m31s296ms ] Speaker 1: And like electric charge, this also needs to be conserved.
[ 7m31s726ms - 7m34s856ms ] Speaker 1: If the light started out with zero spin, well then the two particles together must have zero total spin as well.
[ 7m35s366ms - 7m40s46ms ] Speaker 1: For example, if the direction of the electron's spin is this, the positron has to have spin in the opposite direction so that they perfectly cancel out.
[ 7m40s596ms - 7m44s696ms ] Speaker 1: But the electron spin could have been this instead, or this.
[ 7m45s36ms - 7m47s706ms ] Speaker 1: All of these possibilities are valid, so the rules of quantum mechanics say that the electron does all of these possible things at once until it's measured.
[ 7m48s166ms - 7m51s346ms ] Speaker 1: It's not just that we don't know what the spin is, the electron really is doing everything.
[ 7m51s676ms - 7m56s166ms ] Speaker 1: The only restriction is whatever the electron is doing, the positron must do the exact opposite.
[ 7m56s416ms - 7m59s236ms ] Speaker 1: This also means that when the electron is measured and its state is determined, so is the positron's.
[ 7m59s536ms - 8m1s236ms ] Speaker 1: This is what we mean by entanglement.
[ 8m1s236ms - 8m2s936ms ] Speaker 1: The two particles states depend on each other.
[ 8m3s236ms - 8m5s466ms ] Speaker 1: But how do we measure the particles and force them to do one thing?
[ 8m5s886ms - 8m7s876ms ] Speaker 1: Well, for that, we use the Stern-Gerlach machine.
[ 8m8s976ms - 8m10s986ms ] Speaker 1: It's essentially a strangely shaped magnet.
[ 8m10s986ms - 8m12s656ms ] Speaker 1: And it's how we measure spin.
[ 8m13s66ms - 8m15s666ms ] Speaker 1: The orientation of the magnets determines what axis you're measuring the spin in.
[ 8m16s216ms - 8m21s306ms ] Speaker 1: For example, if the machine is like this and we shoot in a particle with spin in the positive Z direction, it will certainly go to this spot, we'll call plus.
[ 8m21s736ms - 8m24s896ms ] Speaker 1: If instead, a particle has negative Z spin, it will certainly go down to minus.
[ 8m25s296ms - 8m28s636ms ] Speaker 1: So, this Stern-Gerlach machine measures spin in the Z-axis.
[ 8m956ms - 8m31s436ms ] Speaker 1: So what happens when we put in one of our entangled particles?
[ 8m33s46ms - 8m36s456ms ] Speaker 1: When the electron goes into this machine, it either goes to plus or to minus with 50/50 probability.
[ 8m36s886ms - 8m39s706ms ] Speaker 1: Let's say our electron goes to plus.
[ 8m39s926ms - 8m43s226ms ] Speaker 1: Well, this means it went from being in an indeterminate state to positive Z-spin.
[ 8m43s506ms - 8m46s826ms ] Speaker 1: But what about the positron? Well, the only way to conserve spin is if it's now in the negative Z-spin state.
[ 8m47s116ms - 8m49s596ms ] Speaker 1: When it's measured, there is a 100% chance it's minus.
[ 8m49s856ms - 8m51s166ms ] Speaker 1: It has to be that way to conserve spin.
[ 8m51s536ms - 8m54s536ms ] Speaker 1: But the authors of the paper realized, there's something very odd about this result.
[ 8m55s684ms - 8m58s904ms ] Speaker 4: To see what's wrong with this, let's imagine that the electron and the positron carry these envelopes with them.
[ 8m59s344ms - 9m2s754ms ] Speaker 4: These envelopes represent the state of the two particles.
[ 9m3s4ms - 9m7s164ms ] Speaker 4: Until they're measured, both of the particles are in a superposition of being plus and minus at the same time.
[ 9m7s414ms - 9m10s4ms ] Speaker 4: So, both options are in the envelope.
[ 9m15s444ms - 9m18s294ms ] Speaker 4: But now, let's move the positron to someone who's far, far away.
[ 9m28s194ms - 9m30s384ms ] Speaker 4: In this analogy, opening the envelope is like measuring the spin of the electron.
[ 9m30s674ms - 9m35s364ms ] Speaker 4: But that causes the wave function of the electron to collapse to just one possibility.
[ 9m36s144ms - 9m37s204ms ] Speaker 4: In this case, it's plus.
[ 9m37s714ms - 9m41s54ms ] Speaker 4: But what happens to the other envelope far away? Well, it needs to instantly collapse to minus.
[ 9m41s474ms - 9m47s484ms ] Speaker 4: Because otherwise, when the experimenter opens their envelope, they have a chance of seeing plus, which would violate the conservation of spin.
[ 9m47s744ms - 9m54s94ms ] Speaker 4: But if it needs to collapse instantly when the electron is measured, then how does it know what to collapse to? It must receive intel from the far away electron.
[ 9m54s344ms - 9m59s14ms ] Speaker 4: But that message has to travel much faster than the speed of light to get to the positron in time.
[ 9m59s474ms - 10m5s674ms ] Speaker 4: And so, with this argument, Einstein, Podolsky and Rosen had shown that the Copenhagen interpretation of quantum mechanics really is non-local.
[ 10m6s34ms - 10m9s914ms ] Speaker 4: Einstein had already shown this in his conference talk, but this argument was even more decisive.
[ 10m10s264ms - 10m11s684ms ] Speaker 3: It does seem like it's the same thing.
[ 10m12s34ms - 10m15s524ms ] Speaker 3: But now it's ramped up and you've got these two separate particles to do those two separate measurements.
[ 10m15s524ms - 10m17s334ms ] Speaker 3: And one measurement influencing the other measurement definitely feels wrong.
[ 10m17s414ms - 10m17s924ms ] Speaker 4: Yeah, exactly.
[ 10m17s924ms - 10m21s34ms ] Speaker 4: I think he really realized that it's measurements that are the problem in quantum mechanics.
[ 10m21s432ms - 10m25s82ms ] Speaker 1: The wave function of a single particle or of this pair of particles can end up spread over vast distances.
[ 10m25s352ms - 10m26s492ms ] Speaker 1: That isn't itself an issue.
[ 10m26s702ms - 10m31s42ms ] Speaker 1: But when the wave function collapses, the information about that collapse needs to spread everywhere the wave function is.
[ 10m31s42ms - 10m32s632ms ] Speaker 1: That's what makes quantum mechanics non-local.
[ 10m33s182ms - 10m37s232ms ] Speaker 4: The EPR paper didn't just point out this non-locality issue.
[ 10m37s492ms - 10m42s682ms ] Speaker 4: They proved that there is only one local alternative theory for explaining this experiment.
[ 10m43s612ms - 10m47s692ms ] Speaker 4: In this local story, instead of the electron choosing whether to be plus or minus when it's measured,
[ 10m47s692ms - 10m51s972ms ] Speaker 4: it actually makes that choice when it's still in contact with the positron.
[ 10m53s202ms - 10m57s22ms ] Speaker 4: There's some random way that this plus and minus gets put into these two envelopes.
[ 11m4s332ms - 11m7s22ms ] Speaker 4: Which is why the plus and minus are called hidden variables.
[ 11m7s222ms - 11m12s122ms ] Speaker 4: And because this alternative theory assigns these hidden variables in a local way while they're still in contact with each other,
[ 11m12s122ms - 11m15s82ms ] Speaker 4: rather than over a big distance, we call this a local hidden variable theory.
[ 11m15s372ms - 11m20s52ms ] Speaker 4: Now, this local hidden variable theory is going to be able to explain this experiment really simply.
[ 11m20s272ms - 11m21s762ms ] Speaker 4: Let's pass away the positron.
[ 11m27s372ms - 11m32s302ms ] Speaker 4: And now, when the electron is measured as a plus, it doesn't have to rush to tell the positron.
[ 11m32s762ms - 11m34s132ms ] Speaker 4: The positron already knows.
[ 11m34s532ms - 11m36s12ms ] Speaker 4: There is no action at a distance.
[ 11m36s532ms - 11m39s202ms ] Speaker 4: This local hidden variable story is so much more sensible than the quantum one.
[ 11m39s417ms - 11m44s407ms ] Speaker 1: So, we're forced to accept one of two explanations for this experiment, either non-locality, like the Copenhagen interpretation of quantum mechanics,
[ 11m44s407ms - 11m52s87ms ] Speaker 1: or a local hidden variable theory. Given that non-local action at a distance contradicts relativity, Einstein thought this was definitive proof that the Copenhagen interpretation of quantum mechanics is wrong, and therefore there must be some local hidden variable theory that will replace it.
[ 11m54s537ms - 11m58s757ms ] Speaker 1: Einstein showed us that quantum mechanics allows influences that seem to travel faster than light.
[ 11m59s37ms - 12m4s147ms ] Speaker 1: But with today's video sponsor, you can have your own spooky action at a distance. With one click, Nord VPN can teleport your digital presence anywhere in the world.
[ 12m4s497ms - 12m9s817ms ] Speaker 1: Now, it's not actually faster than light, but it might feel like it. Nord VPN has thousands of servers in over 120 countries, which means you can access content that would otherwise be region locked.
[ 12m10s197ms - 12m16s147ms ] Speaker 1: This way, you can access all your favorite content from wherever you are with virtually no lag. But it's not just about access.
[ 12m16s147ms - 12m21s97ms ] Speaker 1: Every time you connect to public Wi-Fi at a coffee shop, at an airport, or a hotel, you're potentially exposing your data to anyone on that network.
[ 12m21s437ms - 12m25s787ms ] Speaker 1: Now, Nord VPN encrypts your connection, so even if someone intercepts your traffic, all they see is gibberish.
[ 12m26s167ms - 12m30s377ms ] Speaker 1: And with their strict no logs policy, your browsing stays private. One account covers up to 10 devices.
[ 12m30s377ms - 12m33s707ms ] Speaker 1: So, you can protect your phone, laptop, tablet, even your router.
[ 12m34s147ms - 12m38s857ms ] Speaker 1: When you use my link, you'll get a huge discount on a two-year plan plus four additional bonus months.
[ 12m39s247ms - 12m43s567ms ] Speaker 1: Get it at NordVPN.com/veritasium. It's risk-free with Nord's 30-day money-back guarantee.
[ 12m43s917ms - 12m47s577ms ] Speaker 1: So, go check it out at NordVPN.com/veritasium.
[ 12m47s577ms - 12m51s97ms ] Speaker 1: You can scan this QR code or click that link down in the description.
[ 12m51s347ms - 12m53s977ms ] Speaker 1: I want to thank Nord VPN for sponsoring this part of the video, and now back to Bell's theorem.
[ 12m58s595ms - 13m1s485ms ] Speaker 1: The EPR paper certainly got a lot of attention.
[ 13m2s235ms - 13m7s495ms ] Speaker 1: Without asking Einstein, Podolsky leaked the paper to the press and the story ended up in the New York Times.
[ 13m7s815ms - 13m10s175ms ] Speaker 6: Religious harvest of the day's intelligence is reached.
[ 13m12s225ms - 13m15s475ms ] Speaker 1: Einstein was the most famous scientist in the world, and he was going after the strange but successful theory of quantum mechanics.
[ 13m15s475ms - 13m17s645ms ] Speaker 1: So, of course, the press loved it.
[ 13m17s875ms - 13m20s515ms ] Speaker 1: But what did scientists think of the argument itself?
[ 13m24s105ms - 13m28s525ms ] Speaker 5: So, the reaction of the physics community was at first mixed.
[ 13m28s985ms - 13m33s275ms ] Speaker 5: You know, there were some people, sort of old allies of Einstein's, who were very happy with it.
[ 13m33s615ms - 13m34s775ms ] Speaker 5: Schrödinger being sort of at the top of that list.
[ 13m35s35ms - 13m42s935ms ] Speaker 5: And in fact, in an attempt to clear up some of the misunderstandings that people were having about the EPR paper, Schrödinger publishes the thought experiment known as Schrödinger's cat, sort of back up Einstein and show the kind of problem.
[ 13m43s25ms - 13m45s385ms ] Speaker 5: that he and Einstein had with quantum physics.
[ 13m45s735ms - 13m48s795ms ] Speaker 5: Bohr, meanwhile, was like, oh my god, what what the hell is this?
[ 13m48s795ms - 13m50s555ms ] Speaker 5: He must be wrong. How do we show that he's wrong?
[ 13m51s705ms - 13m55s395ms ] Speaker 5: Then Bohr ultimately, you know, in his sort of painful and complicated style, ends up coming up with a response to the EPR paper.
[ 13m55s765ms - 14m3s835ms ] Speaker 5: This response is sort of famously obscure and difficult to understand and and I have I have read it in detail and I will tell you, Bohr's reply is either nonsensical or makes some actual mistakes.
[ 14m4s195ms - 14m11s435ms ] Speaker 7: Very, very well-turned sentence, which I believe bore took a great deal of trouble in formulating and whose meaning is just absolutely obscure to me.
[ 14m12s385ms - 14m20s325ms ] Speaker 5: Bohr said in his reply to EPR, in his multiple replies to EPR, that there is no question of anything non-local going on.
[ 14m20s595ms - 14m30s35ms ] Speaker 5: So, the ultimate reaction of the physics community, at least in the immediate years and decades following the publication of EPR and Bohr's reply in 1935, was to think that Bohr had settled it with his reply, even though people didn't really understand what Bohr had said.
[ 14m31s415ms - 14m33s845ms ] Speaker 1: Two decades later, Einstein died.
[ 14m33s845ms - 14m36s125ms ] Speaker 1: Still questioning quantum mechanics.
[ 14m36s545ms - 14m38s755ms ] Speaker 1: But the majority of the physics community had moved on without him.
[ 14m39s205ms - 14m42s595ms ] Speaker 1: Bohr, however, never forgot about the EPR paper.
[ 14m43s145ms - 14m47s325ms ] Speaker 1: In 1962, seven years after Einstein's death, Bohr gave an interview about Einstein.
[ 14m47s715ms - 14m52s755ms ] Speaker 1: And he lamented that Einstein wasted decades on fruitless thought experiments because he simply could not accept quantum mechanics.
[ 14m53s525ms - 14m56s145ms ] Speaker 1: It was terrible that Einstein fell in that trap to work with Podolsky, Bohr said.
[ 14m57s115ms - 14m59s595ms ] Speaker 1: Rosen is worse from my point of view.
[ 14m59s595ms - 15m1s855ms ] Speaker 1: Rosen even today believes the EPR thought experiment.
[ 15m2s15ms - 15m4s415ms ] Speaker 1: Podolsky has given it up, as far as I know.
[ 15m4s725ms - 15m6s775ms ] Speaker 1: The whole idea is absolutely nothing when one really gets into it.
[ 15m8s125ms - 15m10s255ms ] Speaker 1: You may think that I say it too strongly, but it is true.
[ 15m10s755ms - 15m12s865ms ] Speaker 1: There's absolutely no problem in it.
[ 15m13s385ms - 15m15s665ms ] Speaker 1: The next day, Bohr took a nap after lunch and never woke up.
[ 15m18s35ms - 15m20s455ms ] Speaker 1: And so, after many decades, the Einstein Bohr debate was over.
[ 15m21s305ms - 15m24s815ms ] Speaker 1: Bohr's authority was part of the reason the EPR paper didn't get the attention it deserved.
[ 15m25s5ms - 15m32s465ms ] Speaker 1: But there was another reason physicists ignored it. In the EPR experiment, both theories, Copenhagen quantum mechanics and Einstein's local hidden variable alternative, make exactly the same prediction.
[ 15m32s955ms - 15m35s655ms ] Speaker 1: You get the same results either way.
[ 15m35s965ms - 15m39s925ms ] Speaker 1: Debating two different interpretations of the same experimental result seemed like armchair philosophy, not real physics.
[ 15m40s285ms - 15m42s685ms ] Speaker 1: The Copenhagen interpretation makes good predictions, so why not just teach that and move on?
[ 15m43s150ms - 15m45s670ms ] Speaker 3: It just seems like, you know, shut up and calculate.
[ 15m45s670ms - 15m47s400ms ] Speaker 3: I think is the message that kind of gets pushed.
[ 15m47s540ms - 15m49s180ms ] Speaker 5: The general attitude was, this is done.
[ 15m49s590ms - 15m51s900ms ] Speaker 5: Who cares? None of this matters.
[ 15m52s110ms - 15m54s540ms ] Speaker 5: It's all settled. Einstein and Bohr had a big debate about it.
[ 15m54s540ms - 15m56s160ms ] Speaker 5: And Bohr won.
[ 15m56s160ms - 15m57s560ms ] Speaker 5: Do you think you're smarter than Niels Bohr?
[ 15m57s560ms - 15m59s60ms ] Speaker 5: Do you think you're smarter than Albert Einstein?
[ 15m59s470ms - 16m1s710ms ] Speaker 1: It seemed like it would be impossible to resolve this debate.
[ 16m2s10ms - 16m5s70ms ] Speaker 1: until another physicist turned his attention to it.
[ 16m6s10ms - 16m9s270ms ] Speaker 1: John Bell was an undergraduate student shortly after World War II.
[ 16m9s480ms - 16m13s300ms ] Speaker 1: In this new era of physics, and so, of course, he was taught the Copenhagen interpretation.
[ 16m14s30ms - 16m19s110ms ] Speaker 5: John Bell's doubts about quantum mechanics, by his own recollection, showed up basically the minute he learned it.
[ 16m19s110ms - 16m23s670ms ] Speaker 5: In his first quantum mechanics class, he was, you know, getting pretty upset with the instructors.
[ 16m23s670ms - 16m25s790ms ] Speaker 5: And saying, you're being too vague, what the heck do you mean about measurement?
[ 16m26s160ms - 16m29s900ms ] Speaker 1: Bell was never fully satisfied by the answers he got about the foundations of quantum mechanics.
[ 16m30s310ms - 16m33s900ms ] Speaker 1: But when he was doing his PhD, he was encouraged to study something a little bit more respectable.
[ 16m34s130ms - 16m36s790ms ] Speaker 1: And so he studied nuclear physics and went on to have a very accomplished career at CERN.
[ 16m37s150ms - 16m41s510ms ] Speaker 1: But after eight years of working in particle physics, in 1963, he took an academic sabbatical.
[ 16m41s820ms - 16m44s310ms ] Speaker 1: And finally, he had time to focus on his doubts about quantum mechanics.
[ 16m44s700ms - 16m46s290ms ] Speaker 1: He said, I always knew that was waiting for me.
[ 16m49s30ms - 16m55s230ms ] Speaker 1: He began by re-examining the old debates and the papers that most physicists had long since dismissed as philosophical distractions, including the EPR paper.
[ 16m55s590ms - 17m3s700ms ] Speaker 1: After this research, he said, "I felt that Einstein's intellectual superiority over Bohr in this instance was enormous, a vast golf between the man who saw clearly what was needed and the obscurantist.
[ 17m3s910ms - 17m5s800ms ] Speaker 1: He realized Einstein's logic was sound.
[ 17m6s80ms - 17m7s750ms ] Speaker 1: One of the two conclusions is true.
[ 17m8s340ms - 17m10s400ms ] Speaker 1: The question was, could you prove which one using an experiment?
[ 17m12s200ms - 17m14s230ms ] Speaker 1: An experiment of this sort seemed much more feasible by Bell's time.
[ 17m14s640ms - 17m18s440ms ] Speaker 1: The EPR paper was the first to consider the idea of entanglement.
[ 17m18s830ms - 17m21s340ms ] Speaker 1: These days, entanglement is a core feature of quantum mechanics.
[ 17m21s730ms - 17m24s840ms ] Speaker 1: But Einstein had been first to even point out entanglement existed.
[ 17m25s230ms - 17m28s190ms ] Speaker 1: This is why the EPR paper was set up as a thought experiment, because no one had made such an exotic state of matter in 1935.
[ 17m28s880ms - 17m34s360ms ] Speaker 1: But in the intervening decades between Einstein's work and Bell's, between 1935 and 1964, entanglement had become a serious topic of study.
[ 17m34s770ms - 17m38s260ms ] Speaker 1: By Bell's time, there were reliable ways to make it in the lab.
[ 17m38s490ms - 17m41s510ms ] Speaker 1: In fact, Madame Woo had famously reproduced the EPR thought experiment as a real experiment.
[ 17m41s860ms - 17m45s840ms ] Speaker 1: But simply doing the EPR experiment in real life isn't enough to tell you which explanation is correct, since both predict the same thing.
[ 17m46s290ms - 17m49s860ms ] Speaker 1: But Bell wondered if there was another version of the experiment where the non-local and local theories would have to give a different result.
[ 17m51s340ms - 17m57s710ms ] Speaker 5: If you're asking that question and you're playing with the EPR setup, then it's like, oh, it's literally, not just figuratively, a twist, right?
[ 17m58s200ms - 18m0s880ms ] Speaker 1: Here's a simplified version of Bell's experiment.
[ 18m1s210ms - 18m2s990ms ] Speaker 1: Make your entangled electron and positron again.
[ 18m3s350ms - 18m8s20ms ] Speaker 1: But now instead of just measuring them with a Stern-Gerlach machine like this, the experimenters get a choice about how to orient their machine.
[ 18m8s20ms - 18m11s680ms ] Speaker 1: The three different choices are 0 degrees, 120 degrees, and 240 degrees.
[ 18m11s850ms - 18m13s380ms ] Speaker 1: This is the twist on the EPR experiment.
[ 18m14s190ms - 18m15s80ms ] Speaker 1: The experimenters get to choose independently.
[ 18m15s470ms - 18m18s240ms ] Speaker 1: So, the electron might be measured at 0 degrees, while the positron is measured at 240 degrees.
[ 18m20s300ms - 18m23s220ms ] Speaker 1: If both experimenters happen to choose the same axis, then we know what happens.
[ 18m23s590ms - 18m26s60ms ] Speaker 1: They have to get the opposite result as each other to conserve spin.
[ 18m26s490ms - 18m28s640ms ] Speaker 1: The interesting case is when the experimenters happen to choose different axes.
[ 18m30s330ms - 18m32s460ms ] Speaker 1: The number we want to predict here is the disagreement rate, the probability that the electron's result is different from the positron's.
[ 18m35s300ms - 18m37s200ms ] Speaker 1: First, let's see what quantum mechanics predicts for this number.
[ 18m40s280ms - 18m44s90ms ] Speaker 1: Let's say the electron is measured with the 0 degree axis and comes out as plus.
[ 18m44s560ms - 18m47s440ms ] Speaker 1: Now that its spin has collapsed to positive Z, the positron spin needs to instantly collapse to be negative Z.
[ 18m47s690ms - 18m49s860ms ] Speaker 1: This is the non-local part of quantum mechanics.
[ 18m50s100ms - 18m53s530ms ] Speaker 1: But what happens when this positron is measured by a machine tilted at 120 degrees?
[ 18m54s70ms - 18m57s710ms ] Speaker 1: You can see that the positron spin is already almost facing the plus end of the machine, so it's much more likely to go to plus.
[ 18m58s300ms - 19m2s20ms ] Speaker 1: In fact, there's a 75% chance it goes to plus and only a 25% chance it goes to minus.
[ 19m2s20ms - 19m4s180ms ] Speaker 1: So, the disagreement rate is 25%.
[ 19m4s600ms - 19m7s570ms ] Speaker 1: And we can show that for any two different axes the experimenters choose, the disagreement rate is given by the formula, sine squared of theta over two.
[ 19m7s570ms - 19m11s400ms ] Speaker 1: Where theta is the angle between the two different axes that they picked.
[ 19m12s20ms - 19m12s860ms ] Speaker 1: This is the quantum mechanical prediction.
[ 19m13s300ms - 19m16s380ms ] Speaker 1: Now, what about Einstein's local hidden variable theory?
[ 19m16s710ms - 19m21s630ms ] Speaker 1: In this theory, the electron and the positron already know how they're going to behave when they're measured at 0 degrees, 120 degrees, and 240 degrees.
[ 19m21s970ms - 19m23s820ms ] Speaker 1: Their envelopes contain all of the answers.
[ 19m24s140ms - 19m26s640ms ] Speaker 1: Let's say, for example, the envelope contains plus at 0 degrees,
[ 19m26s930ms - 19m29s660ms ] Speaker 1: plus at 120 degrees, and minus at 240 degrees.
[ 19m30s300ms - 19m32s370ms ] Speaker 1: Then, if the electron is measured at 0 degrees,
[ 19m32s650ms - 19m34s100ms ] Speaker 1: it's certainly going to be plus.
[ 19m34s510ms - 19m36s970ms ] Speaker 1: If the positron is measured at 240 degrees,
[ 19m37s200ms - 19m38s700ms ] Speaker 1: it's certainly going to be minus.
[ 19m39s20ms - 19m40s260ms ] Speaker 1: Now, let's consider the disagreement rate.
[ 19m40s660ms - 19m43s460ms ] Speaker 1: For the local hidden variable theory, there is no chance involved.
[ 19m43s720ms - 19m45s380ms ] Speaker 1: The answers are predetermined.
[ 19m45s670ms - 19m48s170ms ] Speaker 1: The disagreement rate depends on the initial state of the envelopes.
[ 19m48s540ms - 19m51s550ms ] Speaker 1: If the initial state had been this, the disagreement rate would be this.
[ 19m51s920ms - 19m55s20ms ] Speaker 1: If it had been this, the disagreement rate would be this, and so on.
[ 19m55s230ms - 19m57s390ms ] Speaker 1: Bell calculated that the overall disagreement rate for all possible initial states is bounded.
[ 19m57s710ms - 20m1s740ms ] Speaker 1: And for any three axes, the disagreements are related in this way.
[ 20m2s40ms - 20m5s670ms ] Speaker 1: The probability of disagreement between A and B is less than or equal to the probability of disagreement between A and C, plus the probability of disagreement between B and C.
[ 20m6s170ms - 20m7s790ms ] Speaker 1: This is Bell's inequality.
[ 20m8s150ms - 20m11s460ms ] Speaker 1: Einstein's local hidden variable theory must obey this inequality.
[ 20m11s720ms - 20m12s650ms ] Speaker 1: Quantum mechanics does not.
[ 20m13s10ms - 20m15s780ms ] Speaker 1: So, by comparing these two different predictions, the debate between Einstein and Bohr could finally be settled.
[ 20m16s200ms - 20m19s10ms ] Speaker 1: If the experiment agrees with the inequality, Einstein was right.
[ 20m19s400ms - 20m21s630ms ] Speaker 1: If it violates the inequality, Bohr was right.
[ 20m22s100ms - 20m23s800ms ] Speaker 1: The challenge now was to run the experiment.
[ 20m24s120ms - 20m26s650ms ] Speaker 1: The first successful test was conducted in 1972.
[ 20m27s300ms - 20m28s760ms ] Speaker 1: The results were clear.
[ 20m29s130ms - 20m32s320ms ] Speaker 1: The experiment violated Bell's inequality and was in agreement with quantum mechanics.
[ 20m32s760ms - 20m35s300ms ] Speaker 1: Einstein's local hidden variable theory was wrong.
[ 20m35s630ms - 20m38s950ms ] Speaker 1: The debate about quantum mechanics was settled in favor of the Copenhagen interpretation.
[ 20m39s450ms - 20m41s10ms ] Speaker 1: Quantum mechanics is non-local.
[ 20m41s510ms - 20m42s590ms ] Speaker 1: But this doesn't mean that faster than light travel is possible.
[ 20m43s320ms - 20m47s40ms ] Speaker 1: Quantum mechanics is non-local in a subtle way that prevents us from sending faster than light messages.
[ 20m47s480ms - 20m48s790ms ] Speaker 1: This is called no communication theorem.
[ 20m49s160ms - 20m51s800ms ] Speaker 1: Let's go back to our local hidden variable theory and its envelopes.
[ 20m52s220ms - 20m54s550ms ] Speaker 1: To transmit a signal from one envelope to the other,
[ 20m54s810ms - 20m57s710ms ] Speaker 1: you would need to be able to choose the spin of the electron to be, say, plus.
[ 20m58s10ms - 20m59s200ms ] Speaker 1: But you can't do that.
[ 20m59s470ms - 21m2s40ms ] Speaker 1: The most you can do is orient the Stern-Gerlach machine,
[ 21m2s280ms - 21m4s420ms ] Speaker 1: but the result is always probabilistic.
[ 21m4s780ms - 21m8s880ms ] Speaker 1: When you look at the other envelope, it's still 50/50 whether it's going to be plus or minus.
[ 21m9s360ms - 21m12s220ms ] Speaker 1: Even though the collapse is non-local, the probabilities are not.
[ 21m12s510ms - 21m14s320ms ] Speaker 1: You can't use it to send a message.
[ 21m14s760ms - 21m17s140ms ] Speaker 1: The experiment proved the non-locality of quantum mechanics.
[ 21m17s400ms - 21m19s180ms ] Speaker 1: The problem is, it did not prove Einstein was wrong.
[ 21m19s520ms - 21m24s840ms ] Speaker 1: Bell's theorem says there's no local hidden variable theory that can reproduce the predictions of quantum mechanics.
[ 21m25s170ms - 21m27s920ms ] Speaker 1: That leaves the door open to one alternative.
[ 21m28s170ms - 21m30s650ms ] Speaker 1: The hidden variable theory could be non-local.
[ 21m31s250ms - 21m34s530ms ] Speaker 1: This is the position of David Bohm's theory, also known as the pilot wave theory.
[ 21m34s810ms - 21m36s790ms ] Speaker 1: In this theory, the electron has a definite spin,
[ 21m37s100ms - 21m39s360ms ] Speaker 1: but there's a corresponding wave that guides it.
[ 21m39s830ms - 21m41s590ms ] Speaker 1: And this wave is non-local.
[ 21m41s960ms - 21m44s790ms ] Speaker 1: It's an interpretation of quantum mechanics that is non-local,
[ 21m45s30ms - 21m47s560ms ] Speaker 1: but in a way that is compatible with relativity.
[ 21m47s910ms - 21m50s200ms ] Speaker 1: And just like the Copenhagen interpretation,
[ 21m50s450ms - 21m52s830ms ] Speaker 1: it perfectly explains the result of Bell's experiment.
[ 21m53s290ms - 21m56s140ms ] Speaker 1: Bell's experiment is probably the most profound experiment ever done.
[ 21m56s650ms - 21m58s640ms ] Speaker 1: It shows that the universe is non-local.
[ 21m59s90ms - 22m3s20ms ] Speaker 1: And it also suggests there are many ways to interpret the result.
[ 22m3s200ms - 22m5s410ms ] Speaker 1: There's the Copenhagen interpretation,
[ 22m5s410ms - 22m7s480ms ] Speaker 1: which is a non-local theory without hidden variables.
[ 22m7s930ms - 22m10s470ms ] Speaker 1: And then there's Bohm's theory, which is a non-local theory with hidden variables.
[ 22m10s980ms - 22m13s920ms ] Speaker 1: And then there's the many-worlds interpretation, which is local,
[ 22m14s230ms - 22m16s620ms ] Speaker 1: but there's no collapse of the wave function at all.
[ 22m17s220ms - 22m19s500ms ] Speaker 1: It's just that there are many worlds that don't communicate.
[ 22m20s0ms - 22m23s210ms ] Speaker 1: So, Bell's theorem did not solve the mystery of quantum mechanics.
[ 22m23s550ms - 22m26s640ms ] Speaker 1: It just gave us a new perspective on the most radical possibilities.
[ 22m27s360ms - 22m28s190ms ] Speaker 8: The mystery remains.
[ 22m29s170ms - 22m30s30ms ] Speaker 8: The mystery remains.
[ 22m30s30ms - 22m31s210ms ] Speaker 8: What are those things?
[ 22m31s520ms - 22m32s370ms ] Speaker 8: Those non-localities.
[ 22m32s370ms - 22m33s800ms ] Speaker 8: Are they real or are they not real?
[ 22m34s100ms - 22m35s360ms ] Speaker 8: How do we interpret this?
[ 22m35s840ms - 22m36s710ms ] Speaker 8: Yeah. It's a mystery.
[ 22m37s240ms - 22m38s140ms ] Speaker 8: Thanks for watching.
[ 22m38s720ms - 22m39s260ms ] Speaker 8: Have a good one.