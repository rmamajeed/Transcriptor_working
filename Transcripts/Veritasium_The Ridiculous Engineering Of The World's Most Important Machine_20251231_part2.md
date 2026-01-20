---
title: Veritasium_The Ridiculous Engineering Of The World's Most Important Machine_20251231_part2
audio_file: Veritasium_The Ridiculous Engineering Of The World's Most Important Machine_20251231_part2.mp3
note_id: f00a1dd9-6b41-44f9-a301-7fa6ddd417aa
date_processed: '2026-01-06'
classification:
  primary_domain: Physics
  sub_domains:
  - Plasma Physics
  - Laser Technology
  - Semiconductor Manufacturing
  - Fluid Dynamics
  difficulty_level: Advanced
  content_type: Discussion
entities:
  people:
  - name: Speaker 1
    role: Engineer/Researcher
    contribution: Describes electron recombination, discharge plasma, laser‑produced
      plasma, tin‑droplet generation, hydrogen cleaning, and shock‑wave analysis.
  - name: Speaker 2
    role: Engineer/Researcher
    contribution: Mentions early laser‑plasma attempts, power scaling limits, and
      mirror contamination concerns.
  - name: Speaker 3
    role: Engineer/Researcher
    contribution: Raises questions about droplet modulation, mirror cleanliness, and
      relates observations to supernova physics.
  - name: Jason
    role: Colleague
    contribution: Referenced in a comment about the droplet formation appearing like
      magic.
  works_cited: []
  concepts_mentioned:
  - electron recombination
  - discharge plasma
  - laser‑produced plasma
  - EUV light (13.5 nm)
  - conversion efficiency
  - tin droplet generation
  - hydrogen gas cleaning (stannane formation)
  - Taylor–von Neumann blast‑wave formula
  - supernova analogy
  laws_theories_cited:
  - Taylor–von Neumann blast‑wave solution
concepts:
- name: Electron recombination
  definition: When free electrons recombine with positive ions, the ion drops to a
    lower energy level and emits a photon.
  parent_concepts:
  - Atomic physics
  related_concepts:
  - Photon emission
  - Plasma formation
  abstraction_level: Fundamental
  confidence: 1.0
- name: Laser‑produced plasma
  definition: A plasma created by focusing a high‑power laser onto a target material,
    heating it to >220,000 °C and ionizing many electrons.
  parent_concepts:
  - Plasma physics
  related_concepts:
  - Discharge plasma
  - EUV generation
  - Tin droplets
  abstraction_level: Applied
  confidence: 1.0
- name: EUV light generation (13.5 nm)
  definition: Production of extreme‑ultraviolet photons around 13.5 nm wavelength,
    used for semiconductor lithography.
  parent_concepts:
  - Optics
  - Photonics
  related_concepts:
  - Laser‑produced plasma
  - Conversion efficiency
  - Tin droplets
  abstraction_level: Applied
  confidence: 1.0
- name: Conversion efficiency
  definition: The ratio of usable EUV light power to the total electrical power supplied
    to the source.
  parent_concepts:
  - Energy engineering
  related_concepts:
  - EUV light generation
  - Xenon vs. tin sources
  abstraction_level: Theoretical
  confidence: 1.0
- name: Tin droplet generation via vibrating nozzle
  definition: Pure tin is melted, forced through a microscopic nozzle, and a high‑frequency
    vibration breaks the stream into uniform droplets.
  parent_concepts:
  - Fluid dynamics
  related_concepts:
  - Laser‑produced plasma
  - Droplet uniformity
  - Hydrogen cleaning
  abstraction_level: Practical
  confidence: 1.0
- name: Hydrogen gas cleaning (stannane formation)
  definition: Low‑pressure hydrogen is introduced to slow and cool tin particles;
    any tin that reaches mirrors reacts to form stannane gas, which is removed from
    the system.
  parent_concepts:
  - Chemical engineering
  related_concepts:
  - Mirror contamination
  - Gas flow control
  abstraction_level: Applied
  confidence: 1.0
- name: Taylor–von Neumann blast‑wave formula
  definition: A solution describing the propagation of a shock wave from a point explosion
    in a surrounding medium.
  parent_concepts:
  - Fluid dynamics
  - Shock physics
  related_concepts:
  - Shock wave in hydrogen gas
  - Supernova analogy
  abstraction_level: Theoretical
  confidence: 0.9
relationships:
- source_concept: Laser‑produced plasma
  target_concept: EUV light generation (13.5 nm)
  relationship_type: causes
  strength: 1.0
  evidence: The laser‑produced plasma recombines electrons and ions to emit EUV photons.
  reasoning: The transcript states that after the laser shuts off, recombination produces
    light at the desired wavelength.
- source_concept: Tin droplet generation via vibrating nozzle
  target_concept: Laser‑produced plasma
  relationship_type: enables
  strength: 1.0
  evidence: Droplets of tin are hit by the high‑power laser to create the plasma source.
  reasoning: The process of shooting tin droplets into the laser is described as the
    method for EUV generation.
- source_concept: Tin droplets
  target_concept: Conversion efficiency
  relationship_type: improves
  strength: 0.95
  evidence: Tin has a higher emission peak around 13.5 nm, yielding five to ten times
    higher conversion efficiency than xenon.
  reasoning: Higher emission at the target wavelength directly raises usable EUV power
    per input watt.
- source_concept: Hydrogen gas cleaning (stannane formation)
  target_concept: Mirror contamination
  relationship_type: mitigates
  strength: 1.0
  evidence: Hydrogen reacts with tin that reaches the collector, forming stannane
    which is removed, keeping mirrors clean.
  reasoning: The described chemical reaction prevents tin buildup on mirrors.
- source_concept: Taylor–von Neumann blast‑wave formula
  target_concept: Shock wave in hydrogen gas
  relationship_type: describes
  strength: 0.9
  evidence: Speaker 3 says the formula exactly describes the repeatable shock wave
    observed after each plasma event.
  reasoning: The formula is applied to model the observed shock wave.
- source_concept: Supernova analogy
  target_concept: Shock wave in hydrogen gas
  relationship_type: supports
  strength: 0.85
  evidence: Speakers compare the plasma‑induced shock wave to miniature supernovas.
  reasoning: The analogy emphasizes similarity in blast‑wave physics.
cross_domain_insights:
- connection_type: structural_analogy|principle_application
  source_domain: Physics
  source_concept: Electron recombination in laser‑produced plasma
  target_domain: Finance
  target_concept: Debt settlement / clearing‑house netting
  insight: Both processes act to neutralize a surplus of free agents (electrons or
    outstanding obligations) and release a stabilising signal (photon emission or
    restored liquidity).
  explanation: In plasma the recombination reduces charge imbalance, emitting photons
    that carry away excess energy. In financial networks, netting aggregates opposite
    positions, eliminating redundant exposures and releasing capital back into the
    system. The mathematics of charge conservation mirrors balance‑sheet conservation.
  potential_applications:
  - Design of stress‑testing models for clearing‑houses using plasma‑recombination
    equations
  - Improved algorithms for real‑time netting in high‑frequency trading
  confidence: 0.86
  historical_example: The 1998 ISDA netting reforms applied balance‑sheet concepts
    to reduce systemic risk, echoing plasma recombination ideas.
- connection_type: structural_analogy|principle_application
  source_domain: Physics
  source_concept: Taylor–von Neumann blast‑wave formula for EUV‑producing plasma expansion
  target_domain: Epidemiology
  target_concept: SIR model of epidemic shock‑wave spread
  insight: The self‑similar blast‑wave solution describes how a sudden energy release
    propagates through a medium, analogous to how an infection front propagates through
    a susceptible population.
  explanation: Both systems obey conservation laws (mass‑energy in plasma, individuals
    in disease compartments) and exhibit a radius that grows as a power of time (r
    ∝ t^0.4 for blast waves, infection radius ∝ t^0.5 in spatial SIR). The scaling
    exponents can be transferred to estimate peak infection timing from initial ‘energy’
    (index case).
  potential_applications:
  - Rapid early‑phase forecasting of pandemic peaks using blast‑wave scaling
  - Optimising vaccination roll‑out as a ‘damping’ term in the shock‑wave equation
  confidence: 0.91
  historical_example: During the 1918 influenza, researchers used diffusion‑wave analogies
    to predict mortality waves, a precursor to modern blast‑wave epidemiology.
- connection_type: principle_application|metaphor
  source_domain: Physics
  source_concept: Conversion efficiency of laser energy to EUV photons (≈2 %)
  target_domain: Energy Economics
  target_concept: Energy Return on Investment (EROI) for renewable technologies
  insight: Both metrics quantify the ratio of useful output to input, providing a
    common decision‑making yardstick across physical and economic systems.
  explanation: EUV conversion efficiency measures photons per joule of laser input;
    EROI measures kilowatt‑hours of electricity generated per kilowatt‑hour invested.
    The same optimisation framework (maximising output while minimising input) applies,
    allowing cross‑domain benchmarking of technology viability.
  potential_applications:
  - Policy models that treat EUV lithography as a ‘capital‑intensive’ technology comparable
    to solar PV in cost‑benefit analyses
  - Dynamic pricing of EUV‑produced chips based on real‑time efficiency data
  confidence: 0.88
  historical_example: The 1970s oil‑EROI studies set the template for modern efficiency‑based
    policy, later adopted for evaluating semiconductor manufacturing processes.
- connection_type: structural_analogy|historical_precedent
  source_domain: Physics
  source_concept: Tin droplet generation via a vibrating nozzle
  target_domain: Additive Manufacturing / Inkjet Printing
  target_concept: Piezo‑electric droplet ejection for printed electronics
  insight: Both employ controlled mechanical vibrations to produce monodisperse droplets
    on demand, enabling precise placement of functional material.
  explanation: The physics of Rayleigh‑Plateau instability under periodic forcing
    governs droplet breakup in both tin droplet generators and inkjet heads. By tuning
    frequency and amplitude, the same scaling laws predict droplet size and velocity,
    allowing technology transfer from EUV source development to printed circuit fabrication.
  potential_applications:
  - Direct‑write deposition of high‑purity metal inks for flexible electronics
  - Miniaturised EUV sources for on‑chip lithography using printable nozzle arrays
  confidence: 0.93
  historical_example: The 1996 introduction of piezo‑electric inkjet heads for graphics
    printing leveraged the same droplet‑formation theory later adapted for metal‑droplet
    EUV sources.
- connection_type: metaphor|principle_application
  source_domain: Physics
  source_concept: Hydrogen‑gas cleaning that forms stannane (SnH₄) to remove contaminants
  target_domain: Signal Processing
  target_concept: Low‑pass filtering to remove high‑frequency noise
  insight: Hydrogen acts as a selective reactant that binds only to impurity species,
    analogous to a filter that attenuates unwanted frequency components while preserving
    the desired signal (tin droplets).
  explanation: In chemistry, the reaction pathway has an activation energy threshold;
    only species above that energy (contaminants) react with H₂. In signal processing,
    a low‑pass filter passes low‑frequency components (desired tin atoms) and attenuates
    high‑frequency noise (contaminants). Both employ a selective barrier based on
    a threshold criterion.
  potential_applications:
  - Design of adaptive chemical scrubbers modelled on digital filter algorithms
  - Real‑time monitoring of plasma purity using spectral ‘filter’ techniques borrowed
    from signal analysis
  confidence: 0.78
  historical_example: The 1965 Wiener filter concept was later mirrored in catalytic
    scrubber design for industrial gas cleaning, illustrating cross‑pollination of
    filtering ideas.
bridge_concepts:
- concept: Conversion Efficiency
  appears_in_domains:
  - Physics
  - Economics
  - Computer Science
  role: Provides a universal metric for input‑to‑output performance, enabling comparative
    analysis across physical processes, economic investments, and algorithmic runtimes.
  examples:
  - EUV photon yield per joule of laser energy (Physics)
  - Energy Return on Investment for a wind farm (Economics)
  - Algorithmic time‑complexity per operation (Computer Science)
- concept: Wave Propagation
  appears_in_domains:
  - Physics
  - Epidemiology
  - Finance
  role: Describes how a disturbance spreads through a medium, whether it is a shock‑wave,
    an infection front, or a market contagion.
  examples:
  - Taylor‑von Neumann blast wave in plasma (Physics)
  - Spatial SIR model of disease spread (Epidemiology)
  - Liquidity shock diffusion in interbank networks (Finance)
- concept: Droplet Formation
  appears_in_domains:
  - Physics
  - Biology
  - Manufacturing
  role: Represents discrete packet creation governed by fluid‑dynamic instabilities,
    enabling controlled delivery of material or information.
  examples:
  - Tin droplets from a vibrating nozzle for EUV sources (Physics)
  - Microfluidic droplets for single‑cell assays (Biology)
  - Inkjet droplets for printed circuit boards (Manufacturing)
mental_models:
- name: First‑Principles Decomposition
  description: Break a complex system down to its most fundamental physical laws before
    rebuilding a solution.
  applied_to:
  - Deriving EUV conversion efficiency from laser‑plasma interaction physics
  - Optimising tin‑droplet size by starting from Rayleigh‑Plateau instability
  transferable_to:
  - Designing low‑carbon supply chains by starting from thermodynamic limits
  - Developing AI models by stripping to core statistical mechanics
- name: Systems Thinking
  description: Treat the process as an interconnected network of inputs, transformations,
    and outputs, emphasizing feedback loops.
  applied_to:
  - Feedback between hydrogen cleaning and plasma purity
  - Coupling of laser energy delivery, plasma formation, and EUV extraction
  transferable_to:
  - Urban water‑resource management
  - Ecosystem restoration planning
- name: Scaling Laws
  description: Use dimensionless groups to relate size, time, and energy across scales.
  applied_to:
  - Taylor–von Neumann blast‑wave scaling for plasma expansion
  - Droplet size scaling with nozzle vibration frequency
  transferable_to:
  - Predicting traffic jam propagation
  - Estimating data‑center cooling requirements
analogies_used:
- source_domain: Cooking
  source_concept: Whisking egg whites to create a foam
  target_domain: Physics
  target_concept: Vibrating nozzle that creates a monodisperse tin droplet stream
  mapping:
    whisk motion: nozzle vibration
    air bubbles: tin droplets
    surface tension of foam: Rayleigh‑Plateau instability
  pedagogical_value: Helps non‑specialists visualise how periodic forcing breaks a
    fluid column into uniform packets, just as a whisk creates uniform bubbles.
- source_domain: Economics
  source_concept: Liquidity injection during a market flash‑crash
  target_domain: Physics
  target_concept: Laser‑produced plasma burst that generates EUV photons
  mapping:
    capital influx: laser energy
    price shock: plasma temperature spike
    trading volume surge: photon emission burst
  pedagogical_value: Illustrates the idea of a sudden, high‑intensity input causing
    a rapid, turbulent response that then dissipates, making the plasma dynamics more
    relatable.
tags:
  hierarchical:
  - '#Physics → #PlasmaPhysics → #LaserProducedPlasma → #EUVGeneration'
  - '#Physics → #FluidDynamics → #DropletFormation → #TinDroplets'
  - '#Physics → #ChemicalEngineering → #HydrogenCleaning → #StannaneFormation'
  topical:
  - '#EUV'
  - '#TinDroplets'
  - '#LaserPlasma'
  - '#ConversionEfficiency'
  - '#HydrogenCleaning'
  - '#ShockWave'
  - '#TaylorVonNeumann'
  methodological:
  - '#Analogy'
  - '#FormulaApplication'
  - '#ExperimentalObservation'
  people:
  - '#Speaker1'
  - '#Speaker2'
  - '#Speaker3'
  - '#Jason'
  concepts:
  - '#ElectronRecombination'
  - '#LaserProducedPlasma'
  - '#EUVLight'
  - '#ConversionEfficiency'
  - '#TinDropletGeneration'
  - '#HydrogenGasCleaning'
  - '#TaylorVonNeumannBlastWave'
  temporal:
  - '#2011'
  - '#2012'
  - '#2013'
summary: ''
key_ideas: []
---
## Key Concepts

**Electron recombination**  
When free electrons recombine with positive ions, the ion drops to a lower energy level and emits a photon.

**Laser‑produced plasma**  
A plasma created by focusing a high‑power laser onto a target material, heating it to >220,000 °C and ionizing many electrons.

**EUV light generation (13.5 nm)**  
Production of extreme‑ultraviolet photons around 13.5 nm wavelength, used for semiconductor lithography.

**Conversion efficiency**  
The ratio of usable EUV light power to the total electrical power supplied to the source.

**Tin droplet generation via vibrating nozzle**  
Pure tin is melted, forced through a microscopic nozzle, and a high‑frequency vibration breaks the stream into uniform droplets.

## Cross-Domain Connections

**Physics → Finance**

*Both processes act to neutralize a surplus of free agents (electrons or outstanding obligations) and release a stabilising signal (photon emission or restored liquidity).*

In plasma the recombination reduces charge imbalance, emitting photons that carry away excess energy. In financial networks, netting aggregates opposite positions, eliminating redundant exposures and releasing capital back into the system. The mathematics of charge conservation mirrors balance‑sheet conservation.

**Physics → Epidemiology**

*The self‑similar blast‑wave solution describes how a sudden energy release propagates through a medium, analogous to how an infection front propagates through a susceptible population.*

Both systems obey conservation laws (mass‑energy in plasma, individuals in disease compartments) and exhibit a radius that grows as a power of time (r ∝ t^0.4 for blast waves, infection radius ∝ t^0.5 in spatial SIR). The scaling exponents can be transferred to estimate peak infection timing from initial ‘energy’ (index case).

**Physics → Energy Economics**

*Both metrics quantify the ratio of useful output to input, providing a common decision‑making yardstick across physical and economic systems.*

EUV conversion efficiency measures photons per joule of laser input; EROI measures kilowatt‑hours of electricity generated per kilowatt‑hour invested. The same optimisation framework (maximising output while minimising input) applies, allowing cross‑domain benchmarking of technology viability.

## Full Transcription



[ 0m0s421ms - 0m3s91ms ] Speaker 1: But it was quickly rolled out because each machine needed its own source.
[ 0m3s561ms - 0m7s751ms ] Speaker 1: The other two methods are based on the same principle: when an electron recombines with an ion,
[ 0m7s751ms - 0m11s651ms ] Speaker 1: the ion drops to a lower energy level, and it releases that excess energy as a photon.
[ 0m12s211ms - 0m15s811ms ] Speaker 1: And if you choose the ion just right, then that photon will have exactly the wavelength you need.
[ 0m16s861ms - 0m19s101ms ] Speaker 1: Now, there are two ways you can create those ions.
[ 0m19s471ms - 0m25s471ms ] Speaker 1: The first is you take a metal, heat it up until you get a metal vapor, and then you apply a strong electric field across it.
[ 0m26s641ms - 0m29s861ms ] Speaker 1: This causes free electrons to knock into nearby atoms and ionize them.
[ 0m31s381ms - 0m33s961ms ] Speaker 1: If you then turn off the electric field, the electrons recombine with the ions and produce light.
[ 0m34s531ms - 0m35s771ms ] Speaker 1: This is discharge produced plasma.
[ 0m36s271ms - 0m37s811ms ] Speaker 2: That's the concept we use first.
[ 0m38s151ms - 0m40s261ms ] Speaker 2: Yeah, because of its relative simplicity.
[ 0m41s41ms - 0m42s681ms ] Speaker 2: Uh, we quickly got it to a few watts.
[ 0m43s261ms - 0m45s311ms ] Speaker 2: We wanted to get 100 watts and we struggled.
[ 0m45s491ms - 0m45s841ms ] Speaker 2: Forever.
[ 0m45s951ms - 0m46s711ms ] Speaker 1: So you couldn't scale it.
[ 0m47s41ms - 0m47s811ms ] Speaker 2: We could not scale it.
[ 0m48s1ms - 0m48s951ms ] Speaker 1: They needed a drastic change.
[ 0m49s631ms - 0m51s331ms ] Speaker 1: So, they switched to the second method.
[ 0m51s331ms - 0m56s161ms ] Speaker 1: This method uses a high-powered laser to hit a target material, creating a plasma that's more than 220,000° C hot.
[ 0m56s761ms - 1m1s81ms ] Speaker 1: The electrons have so much energy that the nucleus can't hold onto them anymore, and up to 14 electrons escape their orbits.
[ 1m1s591ms - 1m4s961ms ] Speaker 1: After the laser shuts off, the electrons and ions recombine to produce light.
[ 1m5s461ms - 1m7s751ms ] Speaker 1: This is laser produced plasma and it was the only method that seemed scalable.
[ 1m10s331ms - 1m14s761ms ] Speaker 1: In fact, this was the same method that the engineering test stand used, a 700-watt laser fired into a stream of xenon gas
[ 1m14s761ms - 1m17s541ms ] Speaker 1: to produce 13.4 nanometer light.
[ 1m18s411ms - 1m20s351ms ] Speaker 1: But xenon had a big problem.
[ 1m20s771ms - 1m25s861ms ] Speaker 1: The conversion efficiency, that is, the ratio of usable light to the amount of power you put in, was terrible.
[ 1m25s861ms - 1m26s931ms ] Speaker 1: It was only around 0.5%.
[ 1m27s281ms - 1m32s81ms ] Speaker 1: That's because while xenon does emit light in the 13 to 14 nanometer range, there's much more light released around 11 nanometers.
[ 1m32s81ms - 1m34s871ms ] Speaker 1: So, most of the energy went into making light that the mirrors couldn't reflect.
[ 1m35s341ms - 1m39s761ms ] Speaker 1: Plus, the laser didn't ionize all the atoms, so leftover neutral xenon atoms would strongly reabsorb some of that 13.4 nanometer light.
[ 1m41s351ms - 1m43s541ms ] Speaker 1: So, ASML started looking at another material, tin.
[ 1m44s121ms - 1m48s521ms ] Speaker 1: Now, tin has a much higher emission peak around 13.5 nanometers, which results in a five to ten times higher conversion efficiency than xenon.
[ 1m48s891ms - 1m52s81ms ] Speaker 1: But just like xenon, neutral tin atoms also absorb EUV light, so they came up with a crazy idea,
[ 1m52s81ms - 1m54s561ms ] Speaker 1: to shoot one tiny tin droplet at a time.
[ 1m55s611ms - 1m58s981ms ] Speaker 1: But to get the required power, you would have to make and hit thousands of droplets every second,
[ 1m59s371ms - 2m1s601ms ] Speaker 1: all of which have to be the exact same shape and size.
[ 2m3s281ms - 2m5s631ms ] Speaker 1: But it turns out that you can't instantly make thousands of tin droplets that are the exact same.
[ 2m6s21ms - 2m6s911ms ] Speaker 1: So, they found a workaround.
[ 2m7s511ms - 2m12s221ms ] Speaker 1: To make the droplets, extremely pure tin is melted and pushed through a microscopic nozzle by high-pressure nitrogen.
[ 2m12s651ms - 2m15s781ms ] Speaker 1: This nozzle vibrates at a high frequency, breaking the stream into tiny droplets.
[ 2m16s341ms - 2m18s901ms ] Speaker 1: These droplets are irregular in size, shape, velocity, and distance, and the whole process is chaotic.
[ 2m19s521ms - 2m24s81ms ] Speaker 3: That's like our magic sauce is uh how do you modulate that tin jet so that it forms the droplets that we want and that they're stable.
[ 2m24s291ms - 2m32s81ms ] Speaker 1: I think we found some paper uh that described this process and it was sort of eye-opening to me that it seems like all the droplets actually come out irregular out of the nozzle.
[ 2m32s511ms - 2m41s131ms ] Speaker 1: But then before they reach the side where they get hit by the laser, like the little irregular droplets come together to form these perfectly spaced, perfectly regular droplets that are about the same size and shape,
[ 2m41s841ms - 2m43s461ms ] Speaker 1: and all traveling at the same velocity.
[ 2m43s861ms - 2m44s951ms ] Speaker 1: That feels like magic to me, Jason.
[ 2m45s331ms - 2m49s861ms ] Speaker 3: Yeah, it's exactly that. It's how do you take a long stream of a tin jet that wants to break up into all these uh irregular droplets
[ 2m50s451ms - 2m54s771ms ] Speaker 3: and like force onto it that it's going to collapse into a single droplet and then happen again and again and again.
[ 2m55s391ms - 3m0s421ms ] Speaker 1: You also don't have that many variables to play with, so you've got the pressure with which you push out the tin, and the frequency of the nozzle.
[ 3m0s821ms - 3m1s911ms ] Speaker 1: Yeah, it seems like a hard problem to solve.
[ 3m2s151ms - 3m5s761ms ] Speaker 3: There's not a whole lot of variables to play with and so mastering that modulation of the jet is is how we make the droplets.
[ 3m8s111ms - 3m11s451ms ] Speaker 1: But these droplets not only have to be identical, they have to be moving incredibly fast.
[ 3m13s101ms - 3m17s131ms ] Speaker 3: What will happen is if the next droplet that's coming down the line is too close, then it'll actually get like disturbed
[ 3m17s691ms - 3m19s181ms ] Speaker 3: and mess up the next plasma event.
[ 3m19s551ms - 3m24s411ms ] Speaker 3: So, we have a requirement, which is both that we make 50,000 droplets per second, but also that they're traveling extremely fast.
[ 3m25s41ms - 3m28s651ms ] Speaker 1: By 2011, their laser produced plasma source reached 11 watts, which was more than double what they managed with their previous source.
[ 3m29s151ms - 3m31s271ms ] Speaker 1: But they were still limited to just five wafers per hour.
[ 3m31s841ms - 3m35s311ms ] Speaker 1: So, they needed to increase the power and fast because they promised they'd hit 60 wafers per hour by the end of 2011.
[ 3m35s871ms - 3m37s871ms ] Speaker 1: Unfortunately, this new method had a major flaw.
[ 3m38s151ms - 3m40s721ms ] Speaker 2: Now, the problem with the tin is you hit the droplet, you generate EUV
[ 3m41s351ms - 3m42s911ms ] Speaker 2: with a very decent conversion efficiency.
[ 3m42s911ms - 3m43s781ms ] Speaker 2: Where does the tin go?
[ 3m43s781ms - 3m49s311ms ] Speaker 2: Because like uh, you know, 30 centimeters away, you have this atomically flat, very beautiful, very expensive mirror, four buffer in size.
[ 3m49s801ms - 3m52s101ms ] Speaker 2: And in the early days, we would coat the thing within like this.
[ 3m52s931ms - 3m54s591ms ] Speaker 3: These machines need to run for a year.
[ 3m55s101ms - 3m59s341ms ] Speaker 3: You're putting liters of tin through this plasma event, and a single nanometer of tin, if it was to land on that collector mirror,
[ 3m59s341ms - 4m1s231ms ] Speaker 3: you'd have to take the collector out of commission.
[ 4m1s651ms - 4m4s41ms ] Speaker 3: We need to keep it almost perfectly clean for for a year.
[ 4m4s271ms - 4m5s261ms ] Speaker 1: Yeah, how do you even approach that?
[ 4m6s101ms - 4m8s31ms ] Speaker 3: So, our our main tool here is the hydrogen gas, actually.
[ 4m9s111ms - 4m12s221ms ] Speaker 1: They fill the chamber with low-pressure hydrogen. This slows and cools the tin particles down.
[ 4m12s651ms - 4m15s821ms ] Speaker 1: And even if some tin makes it to the collector, the hydrogen pulls it off to form a gas called stannane.
[ 4m16s221ms - 4m17s941ms ] Speaker 1: This way, the machine cleans the collectors while it's running.
[ 4m18s281ms - 4m21s231ms ] Speaker 1: But that hydrogen gas also gets hot from all those tin explosions.
[ 4m21s591ms - 4m25s71ms ] Speaker 1: So, they need to keep flushing new, cooler hydrogen into the system while flushing out the stannane and hotter gas.
[ 4m26s121ms - 4m28s191ms ] Speaker 1: But they had to get the pressure and the flow rate just right.
[ 4m28s441ms - 4m32s381ms ] Speaker 1: I mean, too little hydrogen, and the mirrors would get too dirty, but too much hydrogen would not only absorb too much EUV light,
[ 4m32s651ms - 4m34s141ms ] Speaker 1: but it would also cost the system to overheat.
[ 4m34s401ms - 4m37s201ms ] Speaker 3: But the question is, how much heat is there? How much energy is being deposited into the gas?
[ 4m37s921ms - 4m42s651ms ] Speaker 3: And we were stumped for quite some time. If you look at an E V light source, what you'll see is that it's it's kind of like a globe
[ 4m42s651ms - 4m44s391ms ] Speaker 3: of like purplish red light.
[ 4m44s951ms - 4m46s231ms ] Speaker 3: And you kind of ask yourself like, why is that happening?
[ 4m46s691ms - 4m49s381ms ] Speaker 3: So, we bought an ultra-fast camera where we realized is that after every plasma event,
[ 4m49s381ms - 4m52s541ms ] Speaker 3: there's a shock wave that goes propagating out into the hydrogen gas.
[ 4m53s211ms - 4m54s741ms ] Speaker 3: And it's extremely repeatable.
[ 4m54s991ms - 4m56s651ms ] Speaker 3: And you think to yourself, there must be like an explanation for this.
[ 4m57s261ms - 5m2s411ms ] Speaker 3: And there's there's this formula, the Taylor Von Neumann's that all formula that explains point source explosions in an environment, like say, a nuclear blast out to like supernova.
[ 5m2s911ms - 5m5s131ms ] Speaker 3: So, I took this formula, and it like exactly describes the data.
[ 5m5s131ms - 5m9s621ms ] Speaker 3: It's just fantastic that we're seeing these like little tiny little supernovas happening in our vessel 50,000 times a second.
[ 5m10s171ms - 5m12s651ms ] Speaker 1: And is that a fair way to think about this, like creating mini supernovas?
[ 5m13s1ms - 5m15s871ms ] Speaker 3: Yeah, it's actually pretty similar. It's almost like very similar to like a Type 1A supernova, it turns out.
[ 5m15s871ms - 5m18s241ms ] Speaker 3: where you kind of have an object that just fully evaporates and explodes apart.
[ 5m18s651ms - 5m24s251ms ] Speaker 3: And when all that energy goes into the hydrogen gas, it produces a shock wave, a blast wave that comes flying out, which is basically the same thing you look up in the night sky.
[ 5m24s251ms - 5m26s681ms ] Speaker 3: There are these like remnant supernovas that you can see coming from space.
[ 5m27s211ms - 5m30s31ms ] Speaker 1: Using those energy calculations, they discovered they needed to flush the hydrogen at incredibly high speeds,
[ 5m30s411ms - 5m34s141ms ] Speaker 1: around 360 kilometers per hour. That's more than a Category 5 hurricane, even if, you know, those speeds are at low density.
[ 5m35s441ms - 5m37s241ms ] Speaker 1: But 2012 came and went, and they still didn't have enough power.
[ 5m37s891ms - 5m41s71ms ] Speaker 1: In fact, by 2013, ASML just reached 50 watts by shooting 50,000 tin droplets per second.
[ 5m41s541ms - 5m43s561ms ] Speaker 1: But this increased power came at a price, because more power means more heat.
[ 5m43s861ms - 5m47s481ms ] Speaker 1: Heat that ends up slightly shifting the mirrors, resulting in misaligned light and misaligned chip layers.
[ 5m47s911ms - 5m54s51ms ] Speaker 1: So, Zeiss built a nervous system directly into the optics, robot-guided sensors that constantly measure the exact position and angle of each mirror down to the nanometer and the picoradian, which is absolutely insane.
[ 5m54s491ms - 6m0s421ms ] Speaker 2: So, how accurate do we need to control this mirror? Now, one of the things you can do a thought experiment,
[ 6m0s821ms - 6m1s161ms ] Speaker 1: Okay.
[ 6m1s161ms - 6m5s701ms ] Speaker 2: and I can place a little laser on the side of this mirror, then we go all the way to the moon,
[ 6m6s101ms - 6m8s1ms ] Speaker 2: and we put a dime here.
[ 6m8s511ms - 6m13s551ms ] Speaker 2: So, then this light travels all the way here, and then, with the accuracy I can control this mirror, I can decide whether I point to this side of the dime
[ 6m13s921ms - 6m16s791ms ] Speaker 2: or whether I point to this side. What?
[ 6m16s791ms - 6m17s311ms ] Speaker 1: That's crazy.
[ 6m18s441ms - 6m22s191ms ] Speaker 2: So, you can see that the pointing accuracy is uh that's also in picoradians.
[ 6m22s711ms - 6m24s281ms ] Speaker 2: Uh, that is something very extreme.
[ 6m25s111ms - 6m27s661ms ] Speaker 1: This allowed them to control the light even when the power increased.
[ 6m28s311ms - 6m30s311ms ] Speaker 1: While Zeiss was doing a stellar job with the optics,
[ 6m30s621ms - 6m32s391ms ] Speaker 1: ASML was still struggling with the power source.
[ 6m32s631ms - 6m37s201ms ] Speaker 1: The problem was that the tin droplets were too dense, meaning that most of the emitted EUV light was still getting reabsorbed by the neutral atoms before it could ever reach the collector mirror.
[ 6m37s671ms - 6m40s521ms ] Speaker 2: The way we blasted the droplet was so not enough light, too much debris.
[ 6m40s791ms - 6m45s311ms ] Speaker 1: To make matters worse, they could see that about 10 years from now, they would need a new generation of machine, a high-NA EUV machine.
[ 6m45s681ms - 6m48s301ms ] Speaker 1: Essentially, one with a larger optics system that could print smaller features.
[ 6m48s771ms - 6m52s151ms ] Speaker 1: So, what did they do? They decided to double down and invest in the next generation
[ 6m52s661ms - 6m54s791ms ] Speaker 1: before they even got the current one to work.
[ 6m55s101ms - 6m56s651ms ] Speaker 2: The most doubtful period was in the beginning.
[ 6m57s71ms - 7m10s71ms ] Speaker 2: So, I started to work on this in 2012, by that time, EUV was not working, and there was this crazy idiot working on the next generation uh where we could not even uh make the EUV light in the first place.
[ 7m10s241ms - 7m13s211ms ] Speaker 1: Not only are you all in on EUV, you're doubling down even before you know if EUV is going to work.
[ 7m13s261ms - 7m13s521ms ] Speaker 2: Yes.
[ 7m13s921ms - 7m14s351ms ] Speaker 2: Yes.
[ 7m15s161ms - 7m17s181ms ] Speaker 1: But to keep funding the development, they needed money, and lots of it.
[ 7m17s541ms - 7m19s531ms ] Speaker 1: So, they turned to the very people who needed this technology.
[ 7m21s31ms - 7m25s741ms ] Speaker 4: ASML reached out to its main customers, okay, you want this technology for the next generation of chips.
[ 7m25s741ms - 7m29s901ms ] Speaker 4: Well, you need to make us able to invest more by investing in us.
[ 7m30s161ms - 7m34s171ms ] Speaker 1: Intel invested around 4.1 billion dollars and Samsung and TSMC invested another 1.3 billion combined.
[ 7m34s671ms - 7m37s81ms ] Speaker 1: So, they can keep the research going, but with no product to show, customers were running out of patience.
[ 7m38s131ms - 7m40s291ms ] Speaker 2: We were uh crucified at every conference
[ 7m40s671ms - 7m43s461ms ] Speaker 2: that the promises we made last year, we we were unable to live up to.
[ 7m43s461ms - 7m43s701ms ] Speaker 1: Yeah.
[ 7m43s861ms - 7m47s401ms ] Speaker 2: And he said, "This is what you showed two years ago, this is what you show last year, and this is what you're telling me this year, so why would I believe you?"
[ 7m47s571ms - 7m48s591ms ] Speaker 1: They were getting desperate.
[ 7m49s311ms - 7m55s531ms ] Speaker 2: But this was, I think, about 2012 or 13, we were struggling to get the EUV power up.
[ 7m55s531ms - 7m58s711ms ] Speaker 2: And Kinoshita visited us, I took him to dinner in a small town nearby,
[ 7m59s211ms - 8m0s421ms ] Speaker 2: and across from the restaurant was a Maria Chapel.
[ 8m0s881ms - 8m3s571ms ] Speaker 2: And now, you know, science, we have come to the limits of science.
[ 8m3s761ms - 8m4s741ms ] Speaker 2: Hey, let's go for divine intervention.
[ 8m4s741ms - 8m5s711ms ] Speaker 2: So, we went to the chapel,
[ 8m6s101ms - 8m10s951ms ] Speaker 2: so Kinoshita, just to be safe, lit three candles for the three suppliers that were pursuing EUV technology at the time.
[ 8m11s111ms - 8m12s231ms ] Speaker 2: And lo and behold,
[ 8m12s861ms - 8m16s381ms ] Speaker 2: and I have the data to prove it, there is a very strong correlation between us lighting the candle
[ 8m16s591ms - 8m16s791ms ] Speaker 1: Okay.
[ 8m17s121ms - 8m18s481ms ] Speaker 2: and uh power going up.
[ 8m18s731ms - 8m20s711ms ] Speaker 2: It's not a causal effect, but there is a strong correlation.
[ 8m21s91ms - 8m23s891ms ] Speaker 1: The big idea was instead of hitting the droplet once, hit it twice.
[ 8m24s451ms - 8m27s361ms ] Speaker 2: one shot to hit the droplet and it expands in like a pancake shape.
[ 8m28s171ms - 8m31s211ms ] Speaker 2: And then, only then have the second shot, the more powerful main pulse,
[ 8m31s211ms - 8m33s271ms ] Speaker 2: where you evaporate the pancake and turn it into a plasma.
[ 8m33s611ms - 8m34s711ms ] Speaker 2: This was a major breakthrough.
[ 8m35s141ms - 8m38s941ms ] Speaker 1: By changing the target from a droplet to a pancake, you got a larger surface area for the laser to vaporize,
[ 8m39s251ms - 8m43s141ms ] Speaker 1: but without the cost of adding more debris or neutral atoms, because now the tin is vaporized all at once.
[ 8m44s311ms - 8m47s41ms ] Speaker 1: By 2014, they finally managed to hit that coveted 100 watts mark.
[ 8m47s561ms - 8m53s51ms ] Speaker 1: But improvements in multipatterning with 193 nanometers now meant that EUV would only be useful if the source reached at least 200 watts and made 125 wafers per hour.
[ 8m53s431ms - 8m56s941ms ] Speaker 2: The source went from 100 to 200, but is the industry moved on. Nobody waits for you, you know, they find other solutions.
[ 8m57s341ms - 8m59s351ms ] Speaker 2: We had to catch up, so it was a moving goalpost.
[ 8m59s831ms - 9m2s231ms ] Speaker 1: One of the problems was how do you perfectly time the laser so you hit each of these droplets.
[ 9m3s421ms - 9m4s541ms ] Speaker 3: So the analogy is a bit like a golf ball
[ 9m5s311ms - 9m7s51ms ] Speaker 3: that you need to land in the hole 200 meters away.
[ 9m8s211ms - 9m10s401ms ] Speaker 3: Not like land on the green, not bounce, and then get in the hole, but like land in the hole every time.
[ 9m10s711ms - 9m12s221ms ] Speaker 3: That's the level of precision that we need to deliver the droplets.
[ 9m12s731ms - 9m15s661ms ] Speaker 3: Those droplets are traveling through this like maelstrom of hydrogen flow.
[ 9m15s661ms - 9m17s311ms ] Speaker 3: The speeds are tremendously high, it's like shoot golf balls through a tornado.
[ 9m17s921ms - 9m20s511ms ] Speaker 3: And then right when it lands at the hole, that's when it needs to get hit by the laser.
[ 9m20s661ms - 9m24s841ms ] Speaker 3: So, in order to basically track the droplets, for that we use laser curtains, and we can sort of look at when does the droplet pass through a laser curtain.
[ 9m25s171ms - 9m27s671ms ] Speaker 3: Those scattered photons tell us basically when and where is the droplet,
[ 9m28s191ms - 9m30s781ms ] Speaker 3: and then importantly tells us when to fire the laser. So, we actually have to take into account how long
[ 9m30s781ms - 9m33s181ms ] Speaker 3: will it take for the light pulse to hit the droplet after we send the pulse.
[ 9m35s341ms - 9m38s421ms ] Speaker 1: Now, by 2015, they were getting closer and closer to that coveted 200 watt mark.
[ 9m38s771ms - 9m40s721ms ] Speaker 1: When all of a sudden, the ASML board members got summoned.
[ 9m40s971ms - 9m46s301ms ] Speaker 2: this was one of these decisive moments where our customers were really thin on patience and Martin and all the board members were summoned to Korea
[ 9m46s301ms - 9m47s111ms ] Speaker 2: to show 200 watt.
[ 9m47s691ms - 9m48s861ms ] Speaker 2: And they were really fed up with it.
[ 9m48s861ms - 9m50s191ms ] Speaker 2: You know, you either show it now or you
[ 9m50s581ms - 9m51s331ms ] Speaker 2: go away.
[ 9m51s331ms - 9m52s791ms ] Speaker 2: And when they entered the plane, the experiment was still running.
[ 9m53s51ms - 9m53s291ms ] Speaker 1: Okay.
[ 9m53s581ms - 9m56s161ms ] Speaker 2: When they exited the plane, they had the first results demonstrating 200 watt.
[ 9m56s161ms - 9m57s211ms ] Speaker 2: This is how close we came.
[ 9m57s441ms - 10m1s61ms ] Speaker 1: With the source power up, there was one final problem that had to be solved before they could begin manufacturing their machine.
[ 10m1s521ms - 10m7s751ms ] Speaker 1: See, while the hydrogen gas did protect the collector mirror from debris, it wasn't perfect. All the intense high-energy photons and hydrogen ions zipping around deteriorated a very special top coating on the collector.
[ 10m8s291ms - 10m10s331ms ] Speaker 1: So, they still had to clean the mirrors every 10 hours,
[ 10m10s771ms - 10m12s231ms ] Speaker 1: which, you know, is terrible for productivity.
[ 10m12s461ms - 10m15s151ms ] Speaker 1: Martin van den Brink asked for updates every day on their progress,
[ 10m15s521ms - 10m17s921ms ] Speaker 1: but then one of the engineers noticed that every time they opened up the machine,
[ 10m18s441ms - 10m20s351ms ] Speaker 1: the mirrors suddenly seemed cleaner.
[ 10m20s461ms - 10m27s151ms ] Speaker 4: that he kind of chimed in and said, "Oh, uh wait a second, whenever we opened up the machine, oxygen comes in and our problem is solved. Couldn't we think of a way to add just a little oxygen to our system
[ 10m27s151ms - 10m29s871ms ] Speaker 4: and make sure that the collector stays clean longer?"
[ 10m30s371ms - 10m35s361ms ] Speaker 4: And so they started experimenting with the amount of oxygen that was needed in the vacuum, and then finally got to this point, "Okay, if we add so much oxygen, we'll keep the collector clean for longer."
[ 10m35s751ms - 10m38s991ms ] Speaker 1: With this fix, ASML's machine could run continuously for much longer, and it finally became commercially viable.
[ 10m39s481ms - 10m44s391ms ] Speaker 1: By 2016, orders started pouring in, and now all of the most advanced chips need ASML's machine, making them perhaps the most important tech company in the world.
[ 10m45s371ms - 10m49s381ms ] Speaker 1: ASML's first commercial machines had a numerical aperture of 0.33 and could print 30-nanometer lines.
[ 10m49s781ms - 10m51s231ms ] Speaker 1: These are called the low-NA machines,
[ 10m51s671ms - 10m52s801ms ] Speaker 1: and ASML still makes them.
[ 10m53s81ms - 10m57s711ms ] Speaker 1: But the machine that Jan's team started working on back in 2012 was the next generation, which had a larger optics system so they could print even smaller features.
[ 10m58s91ms - 11m0s851ms ] Speaker 1: This is the high-NA machine with a numerical aperture of 0.55,
[ 11m1s311ms - 11m2s911ms ] Speaker 1: and we get to see their latest version up close.
[ 11m3s631ms - 11m4s491ms ] Speaker 1: How much is the machine?
[ 11m4s491ms - 11m8s121ms ] Speaker 2: Uh, we always say north of 350 million euros.
[ 11m8s241ms - 11m8s851ms ] Speaker 1: And you can actually buy it, right?
[ 11m8s991ms - 11m9s671ms ] Speaker 2: You can, if you want. Yeah.
[ 11m9s671ms - 11m10s471ms ] Speaker 1: If I had the money, I could buy it.
[ 11m10s471ms - 11m10s861ms ] Speaker 2: Yes, you could.
[ 11m12s241ms - 11m13s91ms ] Speaker 1: How many people have seen this before?
[ 11m13s371ms - 11m15s871ms ] Speaker 2: We really limit the amount of people that get to go inside the clean room.
[ 11m16s381ms - 11m18s291ms ] Speaker 1: ASML's machines are built in a super strict clean room.
[ 11m18s571ms - 11m22s111ms ] Speaker 1: In any cubic meter, there can be no more than 10 particles only 0.1 microns large
[ 11m22s341ms - 11m23s861ms ] Speaker 1: and nothing bigger than that.
[ 11m24s81ms - 11m25s781ms ] Speaker 1: A speck of pollen is around 20 microns
[ 11m25s781ms - 11m27s11ms ] Speaker 1: and extremely fine sand is around 10 microns.
[ 11m27s741ms - 11m32s41ms ] Speaker 1: To put all of this in perspective, hospital operating rooms, which have to be extremely clean, only allow a maximum of 10,000 particles per cubic meter that are 0.1 microns wide.
[ 11m33s231ms - 11m35s661ms ] Speaker 1: It's so unfair how much better Mark looks though.
[ 11m35s661ms - 11m37s891ms ] Speaker 1: It is light suit. I felt like a little Smurf.
[ 11m39s201ms - 11m40s751ms ] Speaker 1: Okay, so we're going to go through the air showers.
[ 11m41s211ms - 11m43s51ms ] Speaker 1: So you're going to have to do as I do.
[ 11m43s461ms - 11m47s401ms ] Speaker 1: So this is washing down all the particles that are still on. Yeah, so this is like super clean air blowing us clean.
[ 11m49s611ms - 11m50s571ms ] Speaker 1: This place is huge.
[ 11m50s691ms - 11m50s971ms ] Speaker 2: It's huge.
[ 11m51s101ms - 11m52s151ms ] Speaker 1: It's insane.
[ 11m52s381ms - 11m54s591ms ] Speaker 1: I've been in a clean room a couple times before, but it's nothing compared to this.
[ 11m54s901ms - 11m56s651ms ] Speaker 1: Are there any secret areas here where almost no one has access to?
[ 11m57s111ms - 11m57s711ms ] Speaker 2: Uh,
[ 11m57s711ms - 11m58s931ms ] Speaker 2: I can't tell you.
[ 11m59s1ms - 12m0s421ms ] Speaker 1: Great answer. Okay, so this is the total system.
[ 12m1s21ms - 12m1s521ms ] Speaker 2: This is it.
[ 12m3s351ms - 12m4s11ms ] Speaker 1: This is crazy.
[ 12m4s481ms - 12m5s131ms ] Speaker 1: Look how big it is.
[ 12m6s411ms - 12m8s411ms ] Speaker 1: This is the most advanced machine humanity's ever built.
[ 12m8s411ms - 12m12s231ms ] Speaker 1: It's taken many, many years, decades of development, many billions of dollars all to get this humongous beauty.
[ 12m13s51ms - 12m14s511ms ] Speaker 1: So this is the first high-NA machine.
[ 12m14s581ms - 12m14s861ms ] Speaker 2: Yes.
[ 12m15s51ms - 12m17s311ms ] Speaker 2: So, if you saw pictures on the internet or whatever,
[ 12m17s311ms - 12m17s541ms ] Speaker 1: Yeah.
[ 12m17s541ms - 12m18s731ms ] Speaker 2: That's this machine.
[ 12m18s831ms - 12m21s331ms ] Speaker 2: So, the very first lines ever printed at 8 nanometers and stuff,
[ 12m21s331ms - 12m22s411ms ] Speaker 2: that was this machine.
[ 12m22s411ms - 12m23s821ms ] Speaker 1: This is the smoothest object on Earth.
[ 12m23s821ms - 12m24s111ms ] Speaker 2: Yeah.
[ 12m24s351ms - 12m24s641ms ] Speaker 2: It's all in here.
[ 12m24s641ms - 12m24s891ms ] Speaker 2: Yeah.
[ 12m25s321ms - 12m26s641ms ] Speaker 1: Wait, so let me see if I can figure this out.
[ 12m27s681ms - 12m28s171ms ] Speaker 1: This is the light source.
[ 12m29s621ms - 12m30s651ms ] Speaker 1: So where they make the extreme ultraviolet?
[ 12m30s651ms - 12m30s871ms ] Speaker 2: Yes.
[ 12m31s391ms - 12m32s631ms ] Speaker 1: And then the laser must come in from,
[ 12m32s631ms - 12m33s571ms ] Speaker 1: yeah, let's take a look at the laser.
[ 12m33s841ms - 12m35s581ms ] Speaker 1: In fact, we got to see just how the laser and light source work.
[ 12m36s271ms - 12m37s371ms ] Speaker 1: I think we're entering the laser system here.
[ 12m37s811ms - 12m40s411ms ] Speaker 1: Mark's just making sure I think that we can actually film here, that we're not catching anything we're not supposed to.
[ 12m41s131ms - 12m42s611ms ] Speaker 1: Oh, wow. This looks dangerous.
[ 12m43s1ms - 12m44s311ms ] Speaker 1: Now, the laser system is covered by all of these brown cabinets,
[ 12m44s681ms - 12m45s681ms ] Speaker 1: but here is a model version.
[ 12m46s171ms - 12m50s561ms ] Speaker 1: A carbon dioxide laser of just a few watts enters this amplifier, where it bounces around until it's roughly five times its original power.
[ 12m51s51ms - 12m54s511ms ] Speaker 1: It then goes through a total of four different amplifiers to bring the final laser up to 20,000 watts,
[ 12m54s511ms - 12m56s261ms ] Speaker 1: which is four times stronger than lasers that cut through steel.
[ 12m57s71ms - 12m58s971ms ] Speaker 2: Over here, we have the the amplifiers
[ 12m59s111ms - 12m59s321ms ] Speaker 1: Yeah.
[ 12m59s321ms - 13m1s491ms ] Speaker 2: that generate this this powerful laser beam,
[ 13m1s851ms - 13m4s601ms ] Speaker 2: and then it basically comes out and this is part of the beam transport system
[ 13m5s31ms - 13m5s761ms ] Speaker 2: where it's brought to the machine.
[ 13m6s41ms - 13m7s711ms ] Speaker 2: So, this pipe here has the big laser beam.
[ 13m8s1ms - 13m8s881ms ] Speaker 1: And this this has a mirror.
[ 13m8s881ms - 13m9s111ms ] Speaker 2: Yes.
[ 13m9s621ms - 13m10s981ms ] Speaker 1: Then the pulses travel to the light source module.
[ 13m12s61ms - 13m14s351ms ] Speaker 1: It kind of looks like a transformer or like a
[ 13m14s681ms - 13m15s941ms ] Speaker 1: I don't know, like a spaceship.
[ 13m16s241ms - 13m17s181ms ] Speaker 1: There's so many wires going everywhere.
[ 13m17s591ms - 13m18s241ms ] Speaker 2: Don't touch this.
[ 13m20s51ms - 13m21s381ms ] Speaker 1: Holy crap.
[ 13m21s881ms - 13m23s61ms ] Speaker 2: This is pretty big, huh?
[ 13m23s151ms - 13m23s631ms ] Speaker 1: This is insane.
[ 13m23s861ms - 13m24s661ms ] Speaker 1: And this is just the light source.
[ 13m24s661ms - 13m25s411ms ] Speaker 2: This is just the light source.
[ 13m25s411ms - 13m26s101ms ] Speaker 1: That's incredible.
[ 13m26s271ms - 13m27s11ms ] Speaker 1: Can we do a little walk around?
[ 13m27s111ms - 13m27s741ms ] Speaker 2: We can do a little walk.
[ 13m28s191ms - 13m28s831ms ] Speaker 1: Let's go.
[ 13m29s641ms - 13m31s211ms ] Speaker 2: So, basically, this is the heart of the source.
[ 13m31s381ms - 13m32s71ms ] Speaker 1: Can I stand on here?
[ 13m32s411ms - 13m35s311ms ] Speaker 2: Uh, if you're below 137, you can.
[ 13m35s781ms - 13m36s881ms ] Speaker 1: I think I am.
[ 13m38s901ms - 13m39s151ms ] Speaker 1: Ooh.
[ 13m39s891ms - 13m41s131ms ] Speaker 1: And so the tin droplets are coming in from the left.
[ 13m41s131ms - 13m41s351ms ] Speaker 2: Yes.
[ 13m41s861ms - 13m42s911ms ] Speaker 1: Then we're shooting the laser from here?
[ 13m42s911ms - 13m43s221ms ] Speaker 2: Yeah.
[ 13m43s791ms - 13m44s381ms ] Speaker 1: Okay, it explodes.
[ 13m44s381ms - 13m45s951ms ] Speaker 2: And then the light, the light goes out there.
[ 13m48s1ms - 13m50s561ms ] Speaker 1: One improvement from ASML's first EUV machine to their newest one is the number of pulses that hit the droplet.
[ 13m51s101ms - 13m53s521ms ] Speaker 1: The first pre-pulse still flattens the droplet into a pancake.
[ 13m53s861ms - 13m57s211ms ] Speaker 1: But now, there's also a second pre-pulse that further reduces the density, it basically turns it into a low-density gas.
[ 13m57s341ms - 13m57s841ms ] Speaker 1: It rarefies it.
[ 13m58s431ms - 14m0s211ms ] Speaker 1: And then the final pulse essentially ionizes all of it.
[ 14m0s691ms - 14m3s151ms ] Speaker 1: So, for basically the same power coming from the drive laser, they get even more EUV light.
[ 14m3s561ms - 14m5s21ms ] Speaker 1: Now, if they want even more light, then the only way to do that is by hitting more droplets.
[ 14m5s441ms - 14m6s31ms ] Speaker 1: And that's exactly what they did.
[ 14m6s321ms - 14m12s161ms ] Speaker 3: Our most recent EUV light sources that we're shipping right now, which are around the 500-watt level, uh, we increase the repetition rate up to 60,000 times per second, and then we have a roadmap that's going to go to 100,000 droplets per second.
[ 14m12s161ms - 14m15s81ms ] Speaker 3: We've actually now already demonstrated this 100,000 droplets per second in the lab, so it's not an if, but a win.
[ 14m15s361ms - 14m15s661ms ] Speaker 1: Crazy.
[ 14m16s581ms - 14m22s221ms ] Speaker 2: The three pulses that we use, to make the pancake, to blow up the pancake a little bit, and then to evaporate the pancake.
[ 14m22s751ms - 14m26s691ms ] Speaker 2: The first two pulses, they would be coming in through this pipe here,
[ 14m27s111ms - 14m29s461ms ] Speaker 2: and then the main pulse with the big laser, the laser beam would be delivered through this pipe here.
[ 14m29s871ms - 14m33s71ms ] Speaker 1: Both the high and low-NA machine shipping out right now use three pulses, and eventually, they will hit more droplets per second.
[ 14m33s491ms - 14m35s361ms ] Speaker 1: But the light source is just one small part of the full machine.
[ 14m35s781ms - 14m38s991ms ] Speaker 1: After bouncing off the collector mirror, the EUV light moves to the illuminator.
[ 14m39s451ms - 14m41s691ms ] Speaker 1: A set of mirrors shape and focus the light before it hits the reticle.
[ 14m42s91ms - 14m44s381ms ] Speaker 1: The reticle is the top half, and this module is built in a separate facility and installed later.
[ 14m45s121ms - 14m47s711ms ] Speaker 1: Next, the light goes into the projection optics box, which is a set of mirrors that shrink the light down.
[ 14m48s171ms - 14m51s611ms ] Speaker 1: The high-NA machine can shrink the pattern eight times in the vertical direction and four times in the horizontal direction.
[ 14m52s381ms - 14m53s511ms ] Speaker 1: The mirrors are also much smoother still.
[ 14m53s831ms - 14m56s651ms ] Speaker 1: If the low-NA's mirrors were the size of Germany, the tallest bump would be about a millimeter.
[ 14m57s31ms - 15m0s691ms ] Speaker 1: But if the high-NA's mirrors were the size of the world, the tallest bump would be about the thickness of a playing card.
[ 15m1s211ms - 15m4s331ms ] Speaker 1: By the combination of both of these improvements, ASML was able to increase the numerical aperture from 0.33 to 0.55.
[ 15m5s111ms - 15m8s121ms ] Speaker 1: And finally, the light hits the wafer. In order to print around 185 wafers per hour,
[ 15m8s491ms - 15m12s81ms ] Speaker 1: the reticle whips back and forth at accelerations of over 20 Gs. That's over five times the acceleration of a Formula 1 car.
[ 15m12s601ms - 15m16s31ms ] Speaker 1: And this is some actual footage of what that's like inside this machine, and notice that this is not sped up.
[ 15m18s241ms - 15m22s751ms ] Speaker 1: But the crazy thing to me about this machine isn't how fast the reticle moves, or even how small it can print,
[ 15m23s211ms - 15m26s681ms ] Speaker 1: but it's just how insanely accurate it needs to be. The most any two layers can be off, which is called the overlay is one nanometer.
[ 15m27s371ms - 15m28s621ms ] Speaker 1: That's five freaking silicon atoms of precision.
[ 15m29s171ms - 15m29s701ms ] Speaker 1: That's insane.
[ 15m30s121ms - 15m32s461ms ] Speaker 2: So, typically what we do as system engineers is that we make a budget.
[ 15m33s111ms - 15m34s81ms ] Speaker 2: So, we say, hey, you get, let's say, a nanometer,
[ 15m34s91ms - 15m40s751ms ] Speaker 2: and uh and we divide then uh the nanometers uh to to smaller fractions. The nanometers total. It's not like you get a nanometer, you get no, no, you get a nanometer in total.
[ 15m40s751ms - 15m41s131ms ] Speaker 1: You get a nanometer?
[ 15m41s481ms - 15m41s921ms ] Speaker 2: Yes.
[ 15m42s211ms - 15m44s381ms ] Speaker 2: So, you have to uh to fight for the for your part of the nanometer.
[ 15m45s101ms - 15m50s61ms ] Speaker 2: It's kind of cool to realize that like every smartphone nowadays has a chip that is made with the machine that was actually put together here.
[ 15m50s381ms - 15m51s231ms ] Speaker 2: So, that's a cool thought.
[ 15m52s141ms - 15m52s781ms ] Speaker 1: Take a look at this.
[ 15m53s531ms - 15m54s51ms ] Speaker 2: It's pretty massive, huh?
[ 15m54s341ms - 15m54s741ms ] Speaker 1: So big.
[ 15m54s851ms - 15m56s141ms ] Speaker 1: So do you cover it up?
[ 15m56s261ms - 15m58s551ms ] Speaker 2: Yes, at the customer fab it will be looking like a big white box.
[ 15m59s441ms - 16m0s241ms ] Speaker 1: I like it better like this.
[ 16m0s241ms - 16m0s761ms ] Speaker 2: Yeah, me too.
[ 16m1s771ms - 16m5s731ms ] Speaker 1: It's funny, you need such a big machine, so much infrastructure to make the tiniest things we can make at scale.
[ 16m5s921ms - 16m7s91ms ] Speaker 2: It's inversely proportional.
[ 16m7s91ms - 16m8s511ms ] Speaker 1: Yeah.
[ 16m8s511ms - 16m10s41ms ] Speaker 1: The smaller you want to go, the larger everything around it becomes.
[ 16m10s521ms - 16m12s151ms ] Speaker 1: After the machines are assembled, tested, and approved,
[ 16m12s151ms - 16m13s921ms ] Speaker 1: they are disassembled to ship all around the world.
[ 16m14s631ms - 16m18s441ms ] Speaker 1: 5,000 companies supply 100,000 parts, 3,000 cables, 40,000 bolts, and 2 kilometers of housing.
[ 16m18s831ms - 16m23s141ms ] Speaker 1: ASML ships their high-NA machine in 250 containers, spread out over 25 trucks and seven Boeing 747s.