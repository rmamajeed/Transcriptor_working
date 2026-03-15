---
title: Computational Thinking_Zero Knowledge Proofs_20221025
audio_file: Computational Thinking_Zero Knowledge Proofs_20221025.mp3
note_id: ed6de495-a7ce-4abb-b4e8-ca3b593cef2a
date_processed: '2026-02-23'
classification:
  primary_domain: Computer Science
  sub_domains:
  - Cryptography
  - Algorithms
  - Computational Complexity
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people:
  - name: Sherlock
    role: Prover
    contribution: Participated in zero-knowledge proof protocols
  works_cited: []
  concepts_mentioned:
  - Zero-Knowledge Proofs
  - Interactive Protocols
  - Hamiltonian Cycle
  - NP-Hard Problems
  - Cryptography
  laws_theories_cited: []
concepts:
- name: Zero-Knowledge Proofs
  definition: Protocols that allow a prover to convince a verifier of knowing a secret
    without revealing anything about the secret
  parent_concepts:
  - Cryptography
  related_concepts:
  - Interactive Protocols
  - Hamiltonian Cycle
  abstraction_level: Theoretical
  confidence: 1.0
- name: Hamiltonian Cycle
  definition: A cycle in a graph that visits each node exactly once
  parent_concepts:
  - Graph Theory
  related_concepts:
  - NP-Hard Problems
  abstraction_level: Theoretical
  confidence: 1.0
- name: Interactive Protocols
  definition: Protocols that involve multiple rounds of communication between parties
  parent_concepts:
  - Computer Science
  related_concepts:
  - Zero-Knowledge Proofs
  abstraction_level: Theoretical
  confidence: 1.0
- name: NP-Hard Problems
  definition: Problems that are at least as hard as the hardest problems in NP
  parent_concepts:
  - Computational Complexity
  related_concepts:
  - Hamiltonian Cycle
  abstraction_level: Theoretical
  confidence: 1.0
- name: Cryptography
  definition: The practice and study of techniques for secure communication
  parent_concepts:
  - Computer Science
  related_concepts:
  - Zero-Knowledge Proofs
  abstraction_level: Applied
  confidence: 1.0
relationships:
- source_concept: Zero-Knowledge Proofs
  target_concept: Interactive Protocols
  relationship_type: derives_from
  strength: 1.0
  evidence: Zero-knowledge proofs are implemented using interactive protocols
  reasoning: The protocol involves multiple rounds of communication between the prover
    and verifier
- source_concept: Hamiltonian Cycle
  target_concept: NP-Hard Problems
  relationship_type: equivalent_to
  strength: 1.0
  evidence: Hamiltonian Cycle is a known NP-hard problem
  reasoning: The problem is at least as hard as the hardest problems in NP
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: Computer Science
  source_concept: Zero-Knowledge Proofs
  target_domain: Cryptography in Economics
  target_concept: Secure Multi-Party Computation
  insight: Both ensure privacy and security in transactions
  explanation: Zero-Knowledge Proofs in Computer Science and Secure Multi-Party Computation
    in Economics share a structural similarity in ensuring that transactions or computations
    are performed without revealing sensitive information. This is crucial in both
    domains for maintaining privacy and security. The mathematical principles behind
    these concepts can be applied across domains to protect data and ensure trustworthy
    transactions.
  potential_applications:
  - Secure online voting systems
  - Private data sharing in research
  confidence: 0.9
  historical_example: The concept of secure computation was first introduced in the
    1980s, independently in both Computer Science and Economics, highlighting the
    early recognition of the need for secure and private transactions across different
    fields.
- connection_type: principle_application
  source_domain: Computer Science
  source_concept: NP-Hard Problems
  target_domain: Operations Research
  target_concept: Scheduling Problems
  insight: Both involve complex optimization challenges
  explanation: NP-Hard Problems in Computer Science and scheduling problems in Operations
    Research are connected through the principle of optimization under constraints.
    Both domains deal with finding the most efficient solutions to complex problems,
    which often involve trade-offs and constraints. The principles of dealing with
    NP-Hardness, such as approximation algorithms and heuristics, can be applied to
    scheduling problems to find near-optimal solutions efficiently.
  potential_applications:
  - Logistics optimization
  - Resource allocation in manufacturing
  confidence: 0.8
  historical_example: The traveling salesman problem, an NP-Hard problem, has been
    studied in both Computer Science and Operations Research, with early works dating
    back to the 1930s, demonstrating the historical overlap in tackling complex optimization
    problems.
- connection_type: metaphor
  source_domain: Computer Science
  source_concept: Interactive Protocols
  target_domain: Communication Studies
  target_concept: Conversation Models
  insight: Both involve structured exchanges to achieve understanding
  explanation: Interactive Protocols in Computer Science can be seen as a metaphor
    for conversation models in Communication Studies. Both involve a structured exchange
    of information with the goal of achieving a mutual understanding or reaching a
    specific outcome. This metaphor highlights the importance of protocol design in
    human communication, similar to how it is crucial in computer interactions, to
    ensure effective and efficient exchange of information.
  potential_applications:
  - Design of more effective human-computer interfaces
  - Improvement of group communication strategies
  confidence: 0.7
  historical_example: The development of the OSI model for network communication can
    be seen as analogous to the development of models for human communication, such
    as the Transactional Model of Communication, both of which emphasize the structured
    nature of information exchange.
- connection_type: historical_precedent
  source_domain: Computer Science
  source_concept: Hamiltonian Cycle
  target_domain: Genomics
  target_concept: Genome Assembly
  insight: Both involve reconstructing a path or sequence from fragments
  explanation: The Hamiltonian Cycle problem in Computer Science, which involves finding
    a path that visits each vertex exactly once, has historical precedents and applications
    in Genomics, particularly in genome assembly. Genome assembly involves reconstructing
    the complete genome sequence from fragmented data, similar to how the Hamiltonian
    Cycle problem seeks to find a complete path. The algorithms and principles developed
    for solving the Hamiltonian Cycle problem can be applied to improve genome assembly
    techniques.
  potential_applications:
  - More efficient genome assembly algorithms
  - Improved fragment assembly in proteomics
  confidence: 0.85
  historical_example: The use of graph theory in genome assembly dates back to the
    early days of genomics, with the recognition that genome fragments could be represented
    as a graph, where each fragment is a node, and overlaps between fragments are
    edges, directly relating to the graph traversal problems like the Hamiltonian
    Cycle.
bridge_concepts:
- concept: Graph Theory
  appears_in_domains:
  - Computer Science
  - Genomics
  - Social Network Analysis
  role: Graph theory provides a common framework for analyzing and solving problems
    that involve complex networks and relationships.
  examples:
  - Network topology in Computer Science
  - Genome assembly in Genomics
  - Community detection in Social Network Analysis
- concept: Optimization
  appears_in_domains:
  - Computer Science
  - Operations Research
  - Economics
  role: Optimization techniques are crucial for finding the best solution among a
    set of possible solutions, given certain constraints.
  examples:
  - Linear programming in Operations Research
  - Dynamic programming in Computer Science
  - Game theory in Economics
mental_models:
- name: Systems Thinking
  description: A holistic approach to understanding complex systems by analyzing the
    relationships and interactions between their components.
  applied_to:
  - Understanding the security of interactive protocols
  - Analyzing the efficiency of algorithms for NP-Hard problems
  transferable_to:
  - Ecological systems in Biology
  - Economic systems in Economics
- name: First Principles
  description: A method of learning and problem-solving that involves breaking down
    complex problems into their fundamental principles.
  applied_to:
  - Designing zero-knowledge proofs
  - Solving Hamiltonian Cycle problems
  transferable_to:
  - Physics for understanding fundamental laws
  - Philosophy for ethical reasoning
analogies_used:
- source_domain: Travel
  source_concept: Finding the shortest path between two cities
  target_domain: Computer Science
  target_concept: Dijkstra's algorithm for finding the shortest path in a graph
  mapping:
    Cities: Nodes
    Roads: Edges
    Distance: Weight
  pedagogical_value: This analogy helps in understanding how Dijkstra's algorithm
    works by relating it to a real-world scenario that is easy to visualize and comprehend.
tags:
  hierarchical:
  - '#ComputerScience → #Cryptography → #ZeroKnowledgeProofs'
  topical:
  - '#ZeroKnowledgeProofs'
  - '#HamiltonianCycle'
  - '#NPComplete'
  methodological:
  - '#InteractiveProtocols'
  - '#ProofByContradiction'
  people:
  - '#Sherlock'
  concepts:
  - '#ZeroKnowledgeProofs'
  - '#HamiltonianCycle'
  temporal: []
summary: 'Here is a concise summary of the main points in 2-3 sentences:


  The video discusses zero-knowledge proofs, which are interactive protocols between
  two parties where a prover convinces a verifier of knowing a secret without revealing
  anything about the secret. Examples of zero-knowledge proofs include the "Where
  is Waldo?" problem, a color-blind scenario with Sherlock and Watson, and the Hamiltonian
  Cycle problem, which can be used to prove any problem in NP. These protocols involve
  multiple rounds of challenges and responses, and require careful consideration of
  third-party verification and dishonest verifiers to ensure true zero-knowledge proof.'
key_ideas:
- idea: Here are the 3-5 key ideas discussed in the transcription text
  description: ''
- idea: Zero-knowledge proofs**
  description: These are interactive protocols between two parties where a prover
    wants to convince a verifier of knowing a secret without revealing anything about
    the secret, allowing the verifier to be convinced of the prover's knowledge without
    gaining any information about the secret itself.
- idea: Protocols for zero-knowledge proofs**
  description: Various protocols, such as the "Where is Waldo?" and color-blind examples,
    and the Hamiltonian cycle problem, can be used to demonstrate zero-knowledge proofs,
    where the prover can convince the verifier of their knowledge without revealing
    any information about the secret.
- idea: Requirements for zero-knowledge proofs**
  description: Zero-knowledge proofs require that the verifier learns absolutely nothing
    except that the prover has knowledge of the secret, and that the protocol can
    withstand dishonest verifiers and third-party observers, ensuring that no information
    is leaked during the proof.
- idea: Challenges in achieving zero-knowledge proofs**
  description: Achieving zero-knowledge proofs can be tricky, as demonstrated by the
    examples in the video, where small changes to the protocol can compromise the
    zero-knowledge property, and a formal model is needed to prove that a protocol
    is indeed zero-knowledge.
- idea: Applications of zero-knowledge proofs**
  description: Zero-knowledge proofs have potential applications in various fields,
    including cryptography and secure communication, where they can be used to verify
    the authenticity of a message or the identity of a user without revealing any
    sensitive information.
---
## Key Concepts

**Zero-Knowledge Proofs**  
Protocols that allow a prover to convince a verifier of knowing a secret without revealing anything about the secret

**Hamiltonian Cycle**  
A cycle in a graph that visits each node exactly once

**Interactive Protocols**  
Protocols that involve multiple rounds of communication between parties

**NP-Hard Problems**  
Problems that are at least as hard as the hardest problems in NP

**Cryptography**  
The practice and study of techniques for secure communication

## Cross-Domain Connections

**Computer Science → Cryptography in Economics**

*Both ensure privacy and security in transactions*

Zero-Knowledge Proofs in Computer Science and Secure Multi-Party Computation in Economics share a structural similarity in ensuring that transactions or computations are performed without revealing sensitive information. This is crucial in both domains for maintaining privacy and security. The mathematical principles behind these concepts can be applied across domains to protect data and ensure trustworthy transactions.

**Computer Science → Operations Research**

*Both involve complex optimization challenges*

NP-Hard Problems in Computer Science and scheduling problems in Operations Research are connected through the principle of optimization under constraints. Both domains deal with finding the most efficient solutions to complex problems, which often involve trade-offs and constraints. The principles of dealing with NP-Hardness, such as approximation algorithms and heuristics, can be applied to scheduling problems to find near-optimal solutions efficiently.

**Computer Science → Communication Studies**

*Both involve structured exchanges to achieve understanding*

Interactive Protocols in Computer Science can be seen as a metaphor for conversation models in Communication Studies. Both involve a structured exchange of information with the goal of achieving a mutual understanding or reaching a specific outcome. This metaphor highlights the importance of protocol design in human communication, similar to how it is crucial in computer interactions, to ensure effective and efficient exchange of information.

## Discussion Topics

- **Here are the 3-5 key ideas discussed in the transcription text:** 
- **Zero-knowledge proofs**:** These are interactive protocols between two parties where a prover wants to convince a verifier of knowing a secret without revealing anything about the secret, allowing the verifier to be convinced of the prover's knowledge without gaining any information about the secret itself.
- **Protocols for zero-knowledge proofs**:** Various protocols, such as the "Where is Waldo?" and color-blind examples, and the Hamiltonian cycle problem, can be used to demonstrate zero-knowledge proofs, where the prover can convince the verifier of their knowledge without revealing any information about the secret.
- **Requirements for zero-knowledge proofs**:** Zero-knowledge proofs require that the verifier learns absolutely nothing except that the prover has knowledge of the secret, and that the protocol can withstand dishonest verifiers and third-party observers, ensuring that no information is leaked during the proof.
- **Challenges in achieving zero-knowledge proofs**:** Achieving zero-knowledge proofs can be tricky, as demonstrated by the examples in the video, where small changes to the protocol can compromise the zero-knowledge property, and a formal model is needed to prove that a protocol is indeed zero-knowledge.
- **Applications of zero-knowledge proofs**:** Zero-knowledge proofs have potential applications in various fields, including cryptography and secure communication, where they can be used to verify the authenticity of a message or the identity of a user without revealing any sensitive information.

## Full Transcription

 Let's begin.

00:00:00 - 00:00:02 **Speaker 1:** This video is about zero-knowledge proofs.

00:00:03 - 00:00:07 **Speaker 1:** Zero-knowledge proofs are interactive protocols between two parties.

00:00:07 - 00:00:13 **Speaker 1:** In a zero-knowledge proof, a prover wants to convince a verifier of knowing a secret without revealing anything about the secret.

00:00:14 - 00:00:15 **Speaker 1:** Let’s start with an example.

00:00:16 - 00:00:20 **Speaker 1:** This is Waldo, and the goal is to find Waldo in this park.

00:00:20 - 00:00:21 **Speaker 1:** Can you find Waldo?

00:00:22 - 00:00:26 **Speaker 1:** I want to show you that I know where Waldo is without telling you where he is.

00:00:27 - 00:00:28 **Speaker 1:** How can I do that?

00:00:28 - 00:00:30 **Speaker 1:** Please pause the video to think about it.

00:00:34 - 00:00:35 **Speaker 1:** Let’s try the following technique.

00:00:35 - 00:00:39 **Speaker 1:** I take a large black sheet of paper with a little hole in it.

00:00:39 - 00:00:43 **Speaker 1:** The black sheet is four times the size of the picture of the park.

00:00:44 - 00:00:49 **Speaker 1:** Now I move the sheet of paper on top of the picture and place it such that Waldo appears in the little hole.

00:00:49 - 00:00:53 **Speaker 1:** If I can do that, then it means that I know where Waldo is.

00:00:54 - 00:00:58 **Speaker 1:** On the other hand, you only see Waldo, but not Waldo’s relative position in the image.

00:01:01 - 00:01:07 **Speaker 1:** Let’s do another example with Watson on the left and Sherlock on the right.

00:01:07 - 00:01:10 **Speaker 1:** Sherlock has two spheres, one blue and one red.

00:01:11 - 00:01:13 **Speaker 1:** On the other hand, Watson is color blind.

00:01:13 - 00:01:16 **Speaker 1:** For Watson, both spheres look the same.

00:01:16 - 00:01:22 **Speaker 1:** Can Sherlock prove to Watson that he is not color blind and can differentiate between the two spheres?

00:01:23 - 00:01:28 **Speaker 1:** Zero knowledge requires that Sherlock does not reveal to Watson which sphere is blue and which sphere is red.

00:01:28 - 00:01:33 **Speaker 1:** Please take a moment to come up with a protocol that is zero knowledge.

00:01:34 - 00:01:38 **Speaker 1:** Let us show how Sherlock and Watson experience the scene, side-by-side.

00:01:39 - 00:01:42 **Speaker 1:** On top we have Sherlock’s view, on the bottom is Watson’s color-blind view.

00:01:43 - 00:01:44 **Speaker 1:** The protocol goes as follows.

00:01:45 - 00:01:50 **Speaker 1:** Watson takes the two spheres behind his back and he can choose to do one of the following:

00:01:50 - 00:01:51 **Speaker 1:** Keep the spheres as they are.

00:01:52 - 00:01:54 **Speaker 1:** Or switch them.

00:01:54 - 00:01:57 **Speaker 1:** Next, Watson shows the spheres to Sherlock.

00:01:57 - 00:02:00 **Speaker 1:** Sherlock must tell whether Watson switched the spheres.

00:02:01 - 00:02:04 **Speaker 1:** In this particular case, Sherlock must answer, “switched.”

00:02:05 - 00:02:08 **Speaker 1:** Of course, Sherlock might be lucky, so they repeat the protocol many times.

00:02:09 - 00:02:13 **Speaker 1:** If Sherlock always answers correctly, then Sherlock can distinguish the colors with a high probability.

00:02:14 - 00:02:17 **Speaker 1:** And none of Sherlock’s answers reveal the color of the spheres.

00:02:18 - 00:02:22 **Speaker 1:** But we need to be careful; zero knowledge is a strong attribute.

00:02:22 - 00:02:28 **Speaker 1:** In particular, zero knowledge demands that Watson cannot convince a third-party that Sherlock can see the colors.

00:02:32 - 00:02:34 **Speaker 1:** Does our protocol fulfill this requirement?

00:02:34 - 00:02:39 **Speaker 1:** Say Watson records the whole interaction with Sherlock as a movie and shows the recording to you.

00:02:40 - 00:02:42 **Speaker 1:** Will you be convinced that Sherlock can see color?

00:02:43 - 00:02:44 **Speaker 1:** Pause the video to think about it.

00:02:47 - 00:02:53 **Speaker 1:** The movie cannot convince you that Sherlock can distinguish the colors because Watson and Sherlock can create the same movie even if Sherlock is color blind.

00:02:53 - 00:02:55 **Speaker 1:** How can they do that?

00:02:55 - 00:02:58 **Speaker 1:** Sherlock and Watson can first decide in what order to switch the spheres.

00:02:59 - 00:03:02 **Speaker 1:** After they have agreed on the order, they start recording the movie.

00:03:02 - 00:03:07 **Speaker 1:** You can never tell whether it was a genuine recording where Sherlock was proving to Watson that he could distinguish the colors, or whether they agreed on the order beforehand.

00:03:08 - 00:03:12 **Speaker 1:** So, our protocol also fulfills this strong requirement.

00:03:12 - 00:03:16 **Speaker 1:** However, zero knowledge needs an even stronger requirement.

00:03:16 - 00:03:21 **Speaker 1:** Zero knowledge requires that Watson learns absolutely nothing except that Sherlock can distinguish the colors.

00:03:21 - 00:03:25 **Speaker 1:** This must apply even if Watson behaves dishonestly.

00:03:26 - 00:03:31 **Speaker 1:** Is there some way for Watson to trick Sherlock into revealing the colors of the spheres?

00:03:31 - 00:03:33 **Speaker 1:** Pause the video to think about it.

00:03:36 - 00:03:41 **Speaker 1:** Let us consider the case where Watson owns two other spheres that look exactly like Sherlock’s.

00:03:42 - 00:03:47 **Speaker 1:** In addition, let us assume that Watson’s spheres are secretly marked, so Watson knows which one is red and which one is blue.

00:03:47 - 00:03:49 **Speaker 1:** Now he can do the following trick.

00:03:50 - 00:03:52 **Speaker 1:** First, Watson shows Sherlock spheres.

00:03:53 - 00:03:55 **Speaker 1:** But then Watson shows his marked spheres.

00:03:56 - 00:04:00 **Speaker 1:** Based on Sherlock’s answer, Watson can now infer the colors of Sherlock’s spheres.

00:04:00 - 00:04:05 **Speaker 1:** For example, if Sherlock answers “not switched”, Watson can map the colors as shown here.

00:04:06 - 00:04:10 **Speaker 1:** At the beginning of the protocol, Watson only knew the colors of his spheres.

00:04:10 - 00:04:13 **Speaker 1:** But now Watson knows the colors of all four spheres.

00:04:14 - 00:04:18 **Speaker 1:** Thanks to the protocol, Watson learned the colors of Sherlock’s spheres.

00:04:18 - 00:04:21 **Speaker 1:** Hence the protocol is not zero knowledge.

00:04:24 - 00:04:29 **Speaker 1:** Another example of a zero-knowledge proof is the Hamiltonian Cycle problem.

00:04:29 - 00:04:34 **Speaker 1:** Hamiltonian cycle is the problem of finding a cycle in a graph that visits each node exactly once.

00:04:35 - 00:04:37 **Speaker 1:** A possible solution is shown here.

00:04:37 - 00:04:44 **Speaker 1:** Of course, in this small example, it is easy to find such a Hamiltonian cycle, but in general, Hamiltonian cycle is a known NP-hard problem.

00:04:44 - 00:04:50 **Speaker 1:** This means that a zero-knowledge proof for Hamiltonian cycle can be used as a zero-knowledge proof for every problem in NP.

00:04:54 - 00:04:57 **Speaker 1:** We can represent a graph with an adjacency matrix.

00:04:57 - 00:05:03 **Speaker 1:** So, let’s assume that Sherlock knows a Hamiltonian cycle in the graph, and Watson does not.

00:05:03 - 00:05:08 **Speaker 1:** Sherlock wants to prove to Watson that he knows the cycle without revealing anything else.

00:05:08 - 00:05:10 **Speaker 1:** How can Sherlock do that?

00:05:10 - 00:05:14 **Speaker 1:** Take a moment to think about potential protocols.

00:05:15 - 00:05:18 **Speaker 1:** First, Sherlock tells Watson to look away.

00:05:18 - 00:05:22 **Speaker 1:** Then Sherlock creates a permutation of the graph by simply permuting the names of each node in the graph.

00:05:23 - 00:05:28 **Speaker 1:** For example, Sherlock renames x1 with x3, x2 with x5, and so on.

00:05:28 - 00:05:30 **Speaker 1:** This leads to permuted adjacency matrix.

00:05:31 - 00:05:36 **Speaker 1:** Sherlock only uses the adjacency matrix, hides every entry of the permuted matrix and tells Watson to look back.

00:05:37 - 00:05:39 **Speaker 1:** Watson now has two choices.

00:05:39 - 00:05:43 **Speaker 1:** He can request Sherlock to open the matrix and show the permutation.

00:05:44 - 00:05:48 **Speaker 1:** Sherlock can do this by opening every matrix entry and showing how he changed the names.

00:05:49 - 00:05:51 **Speaker 1:** Watson’s second option is to ask for the cycle.

00:05:51 - 00:05:55 **Speaker 1:** In this case, Sherlock only shows the entries that make up a cycle.

00:05:56 - 00:06:01 **Speaker 1:** They repeat the protocol many times, and in each repetition, Watson can either ask for the permutation or for the cycle, but never for both.

00:06:02 - 00:06:06 **Speaker 1:** Can Watson convince a third-party that Sherlock knows the cycle?

00:06:06 - 00:06:08 **Speaker 1:** Take a moment to think about it.

00:06:11 - 00:06:17 **Speaker 1:** Even if Sherlock does not know the cycle, Watson and Sherlock can create the same movie by agreeing on the order of the challenges beforehand.

00:06:18 - 00:06:22 **Speaker 1:** If the challenge is to open the permutation, Sherlock hides a random permutation of the graph.

00:06:22 - 00:06:25 **Speaker 1:** This way he can easily answer, “show permutation” challenge.

00:06:25 - 00:06:29 **Speaker 1:** If the challenge is to open a cycle, Sherlock hides a matrix that contains only ones.

00:06:30 - 00:06:34 **Speaker 1:** This way, Sherlock can also easily open a random cycle.

00:06:34 - 00:06:39 **Speaker 1:** Note that Sherlock knows the challenge before each round since Watson and Sherlock agreed on the order beforehand.

00:06:40 - 00:06:45 **Speaker 1:** Similar to the color-blind example, you can never tell whether it is a genuine recording or the one where Watson and Sherlock decided on the order beforehand.

00:06:46 - 00:06:51 **Speaker 1:** However, as mentioned before, zero knowledge is a stronger property and states that no information leaks.

00:06:51 - 00:06:55 **Speaker 1:** One can show that Hamiltonian cycle is zero knowledge.

00:06:55 - 00:06:59 **Speaker 1:** However, to do so, we need a more formal model.

00:06:59 - 00:07:04 **Speaker 1:** Such a formal model exists, but we cannot explain the details in this video.

00:07:04 - 00:07:07 **Speaker 1:** But why should Watson be convinced that Sherlock knows the cycle?

00:07:08 - 00:07:13 **Speaker 1:** If Sherlock can answer both questions, he knows a Hamiltonian cycle in the graph, since he can simply revert the permutation and get the cycle in the original graph.

00:07:14 - 00:07:18 **Speaker 1:** So, if Sherlock can answer both questions, it follows that Sherlock knows the cycle.

00:07:19 - 00:07:22 **Speaker 1:** Conversely, if Sherlock does not know the cycle, he can answer only one question.

00:07:23 - 00:07:27 **Speaker 1:** If Sherlock does not know the cycle, Sherlock can survive every round with a probability one half.

00:07:27 - 00:07:32 **Speaker 1:** The probability decreases exponentially if Watson and Sherlock repeat the test n times.

00:07:32 - 00:07:37 **Speaker 1:** If Sherlock does not know how to compute a Hamiltonian cycle, he will likely not be able to answer a challenge in one of the rounds.

00:07:38 - 00:07:43 **Speaker 1:** The exact math is a bit tricky, since Sherlock might also guess correctly randomly.

00:07:46 - 00:07:48 **Speaker 1:** In this video, we have seen zero-knowledge proofs.

00:07:49 - 00:07:54 **Speaker 1:** These are protocols that allow a prover to convince a verifier of knowing a secret without revealing absolutely anything about the secret.

00:07:55 - 00:07:59 **Speaker 1:** We have seen different round-based protocols, where the verifier makes a challenge in each round.

00:07:59 - 00:08:03 **Speaker 1:** This video has three examples: “Where is Waldo?”, color blind, and Hamiltonian cycle.

00:08:04 - 00:08:09 **Speaker 1:** We have also learned that zero knowledge is a tricky concept, and includes being able to deal with third parties and dishonest verifiers.

00:08:09 - 00:08:11 **Speaker 1:** Thank you for watching this video.