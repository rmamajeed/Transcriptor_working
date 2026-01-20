---
title: Veritasium_Something Strange Happens When You Trace How Connected We Are_20250930_part1
audio_file: Veritasium_Something Strange Happens When You Trace How Connected We Are_20250930_part1.mp3
note_id: 216c0ca6-a1e0-4efb-8d88-f1d12d6d918c
date_processed: '2026-01-12'
classification:
  primary_domain: Physics
  sub_domains:
  - Complex Networks
  - Social Network Analysis
  - Mathematics
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people:
  - name: Duncan Watt
    role: Mathematician
    contribution: Co-developed the small world model
  - name: Steve Strogatz
    role: Mathematician
    contribution: Co-developed the small world model
  - name: Marlon Brando
    role: Actor
    contribution: Mentioned in the context of six degrees of separation
  - name: Saleh Ben Galli
    role: Falafel salesman and former theater director
    contribution: Participant in the DZeit experiment
  works_cited: []
  concepts_mentioned:
  - Six Degrees of Separation
  - Small World Problem
  - Clustering
  - Shortcuts
  - Random Networks
  laws_theories_cited:
  - Small World Model
concepts:
- name: Six Degrees of Separation
  definition: The idea that any two people on the planet are connected through a chain
    of acquaintances with a maximum of six steps
  parent_concepts:
  - Social Networks
  related_concepts:
  - Small World Problem
  - Clustering
  abstraction_level: Theoretical
  confidence: 1.0
- name: Small World Problem
  definition: The phenomenon where a network exhibits both high clustering and short
    average path lengths
  parent_concepts:
  - Complex Networks
  related_concepts:
  - Six Degrees of Separation
  - Clustering
  abstraction_level: Theoretical
  confidence: 1.0
- name: Clustering
  definition: The tendency of nodes in a network to form tightly connected groups
  parent_concepts:
  - Network Science
  related_concepts:
  - Six Degrees of Separation
  - Small World Problem
  abstraction_level: Theoretical
  confidence: 1.0
relationships:
- source_concept: Six Degrees of Separation
  target_concept: Small World Problem
  relationship_type: equivalent_to
  strength: 0.9
  evidence: The small world model explains the phenomenon of six degrees of separation
  reasoning: The small world model provides a theoretical framework for understanding
    the six degrees of separation phenomenon
- source_concept: Clustering
  target_concept: Small World Problem
  relationship_type: supports
  strength: 0.8
  evidence: Clustering is a key feature of the small world problem
  reasoning: The presence of clustering in a network contributes to the small world
    phenomenon
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: Physics
  source_concept: Six Degrees of Separation
  target_domain: Sociology
  target_concept: Social Network Analysis
  insight: The structure of social networks exhibits small-world properties, similar
    to physical systems.
  explanation: Both physical systems and social networks can be described by networks
    with a small average path length, leading to efficient information transfer. The
    concept of six degrees of separation illustrates how individuals are connected
    through a relatively short chain of acquaintances, mirroring the small-world phenomenon
    in physics. This analogy is useful for understanding the spread of information,
    diseases, or behaviors in social networks.
  potential_applications:
  - Epidemiology
  - Information Diffusion
  confidence: 0.9
  historical_example: The concept of six degrees of separation was first proposed
    by Frigyes Karinthy in 1929 and has since been applied to various domains, including
    sociology and epidemiology.
- connection_type: principle_application
  source_domain: Physics
  source_concept: Clustering
  target_domain: Computer Science
  target_concept: Data Clustering Algorithms
  insight: Clustering principles from physics can be applied to data analysis in computer
    science.
  explanation: The concept of clustering in physics, where particles or objects group
    together due to attractive forces, has a direct analogy in computer science. Data
    clustering algorithms, such as k-means or hierarchical clustering, aim to group
    similar data points together, mirroring the physical process of clustering. This
    application of physical principles to data analysis enables the identification
    of patterns and structures in complex datasets.
  potential_applications:
  - Data Mining
  - Machine Learning
  confidence: 0.8
  historical_example: The k-means clustering algorithm was first proposed in 1967
    by MacQueen, and its development was influenced by the concept of clustering in
    physics.
- connection_type: metaphor
  source_domain: Physics
  source_concept: Small World Problem
  target_domain: Economics
  target_concept: Global Supply Chain Networks
  insight: The small-world problem in physics can be used as a metaphor to understand
    the structure and resilience of global supply chain networks.
  explanation: The small-world problem, which describes how a few long-range connections
    can significantly reduce the average path length in a network, can be applied
    to understand the structure of global supply chain networks. Just as physical
    systems exhibit small-world properties, supply chain networks can be characterized
    by a mix of local and long-range connections, leading to efficient information
    and material transfer. This metaphor can help economists and logisticians design
    more resilient and efficient supply chains.
  potential_applications:
  - Supply Chain Optimization
  - Risk Management
  confidence: 0.7
  historical_example: The concept of the small-world problem has been used to study
    the resilience of various complex networks, including social, technological, and
    biological systems.
bridge_concepts:
- concept: Network Science
  appears_in_domains:
  - Physics
  - Sociology
  - Computer Science
  - Economics
  role: Provides a common framework for analyzing complex systems
  examples:
  - Social network analysis
  - Traffic flow modeling
  - Data clustering algorithms
  - Supply chain optimization
mental_models:
- name: Systems Thinking
  description: A holistic approach to understanding complex systems by analyzing the
    relationships and interactions between components
  applied_to:
  - Analyzing the small-world problem in physics
  transferable_to:
  - Understanding social networks
  - Optimizing supply chain networks
  - Designing resilient systems
analogies_used:
- source_domain: Physics
  source_concept: Phase Transitions
  target_domain: Computer Science
  target_concept: Complexity Theory
  mapping:
    Phase transition: Computational phase transition
  pedagogical_value: Helps understand the sudden changes in computational complexity
    that can occur in algorithms and systems
tags:
  hierarchical:
  - '#Physics → #Complex Networks → #Social Network Analysis'
  topical:
  - '#Six Degrees of Separation'
  - '#Small World Problem'
  methodological:
  - '#Mathematical Modeling'
  - '#Network Analysis'
  people:
  - '#Duncan Watt'
  - '#Steve Strogatz'
  concepts:
  - '#Clustering'
  - '#Random Networks'
  temporal:
  - '#1990s'
summary: 'Here is a concise summary of the main points in 2-3 sentences:


  The concept of six degrees of separation suggests that anyone in the world can be
  connected to anyone else through a chain of friends, family, or acquaintances in
  six steps or less. Researchers Duncan Watts and Steve Strogatz developed a model
  to explain this phenomenon, finding that the introduction of random shortcuts in
  a network can significantly reduce the average degree of separation. The structure
  of complex networks, including the presence of hubs and shortcuts, can have a profound
  impact on how information, diseases, and behaviors spread, and understanding these
  networks can help us develop strategies to control and influence these outcomes.'
key_ideas:
- idea: Here are 3-5 key ideas discussed in the transcription text with a short description
    of each
  description: ''
- idea: The concept of six degrees of separation**
  description: The idea that anyone in the world can be connected to anyone else through
    a chain of acquaintances with no more than six intermediate links, and how this
    concept applies to various networks, including social networks and the internet.
- idea: The role of shortcuts and hubs in networks**
  description: How shortcuts (random connections between nodes) and hubs (highly connected
    nodes) can make a network more connected and efficient, but also more vulnerable
    to the spread of diseases or information.
- idea: The small world problem and its solution**
  description: The phenomenon where a network can be highly clustered (with nodes
    forming close-knit groups) yet still have a short average path length between
    any two nodes, and how this can be explained by the presence of shortcuts and
    hubs.
- idea: Preferential attachment and the emergence of hubs**
  description: The process by which new nodes in a network are more likely to connect
    to existing nodes that are already highly connected, leading to the emergence
    of hubs and a scale-free network structure.
- idea: The implications of network structure on behavior and disease spread**
  description: How the structure of a network, including the presence of hubs and
    shortcuts, can influence the spread of diseases, information, and behaviors, and
    how understanding these dynamics can inform strategies for controlling disease
    outbreaks and influencing social behavior.
---
## Key Concepts

**Six Degrees of Separation**  
The idea that any two people on the planet are connected through a chain of acquaintances with a maximum of six steps

**Small World Problem**  
The phenomenon where a network exhibits both high clustering and short average path lengths

**Clustering**  
The tendency of nodes in a network to form tightly connected groups

## Cross-Domain Connections

**Physics → Sociology**

*The structure of social networks exhibits small-world properties, similar to physical systems.*

Both physical systems and social networks can be described by networks with a small average path length, leading to efficient information transfer. The concept of six degrees of separation illustrates how individuals are connected through a relatively short chain of acquaintances, mirroring the small-world phenomenon in physics. This analogy is useful for understanding the spread of information, diseases, or behaviors in social networks.

**Physics → Computer Science**

*Clustering principles from physics can be applied to data analysis in computer science.*

The concept of clustering in physics, where particles or objects group together due to attractive forces, has a direct analogy in computer science. Data clustering algorithms, such as k-means or hierarchical clustering, aim to group similar data points together, mirroring the physical process of clustering. This application of physical principles to data analysis enables the identification of patterns and structures in complex datasets.

**Physics → Economics**

*The small-world problem in physics can be used as a metaphor to understand the structure and resilience of global supply chain networks.*

The small-world problem, which describes how a few long-range connections can significantly reduce the average path length in a network, can be applied to understand the structure of global supply chain networks. Just as physical systems exhibit small-world properties, supply chain networks can be characterized by a mix of local and long-range connections, leading to efficient information and material transfer. This metaphor can help economists and logisticians design more resilient and efficient supply chains.

## Discussion Topics

- **Here are 3-5 key ideas discussed in the transcription text with a short description of each:** 
- **The concept of six degrees of separation**:** The idea that anyone in the world can be connected to anyone else through a chain of acquaintances with no more than six intermediate links, and how this concept applies to various networks, including social networks and the internet.
- **The role of shortcuts and hubs in networks**:** How shortcuts (random connections between nodes) and hubs (highly connected nodes) can make a network more connected and efficient, but also more vulnerable to the spread of diseases or information.
- **The small world problem and its solution**:** The phenomenon where a network can be highly clustered (with nodes forming close-knit groups) yet still have a short average path length between any two nodes, and how this can be explained by the presence of shortcuts and hubs.
- **Preferential attachment and the emergence of hubs**:** The process by which new nodes in a network are more likely to connect to existing nodes that are already highly connected, leading to the emergence of hubs and a scale-free network structure.
- **The implications of network structure on behavior and disease spread**:** How the structure of a network, including the presence of hubs and shortcuts, can influence the spread of diseases, information, and behaviors, and how understanding these dynamics can inform strategies for controlling disease outbreaks and influencing social behavior.

## Full Transcription



[ 0m0s112ms - 0m3s992ms ] In 1999, the German newspaper DZeit ran an experiment.
[ 0m4s332ms - 0m11s652ms ] They asked a falafel salesman and former theater director, Saleh Ben Galli, who in the world he would most like to be connected to.
[ 0m12s82ms - 0m14s682ms ] He chose his favorite actor, Marlon Brando.
[ 0m15s472ms - 0m24s952ms ] So, the reporters then searched for a chain of friends, family or acquaintances, people who knew each other on a first-name basis, who could connect Ben Galli to Brando.
[ 0m25s462ms - 0m38s922ms ] As it happens, Ben Galli had a friend in California, this friend worked alongside the boyfriend of a woman who was the sorority sister of the daughter of the producer of the film Don Juan DeMarco, starring Marlon Brando.
[ 0m39s412ms - 0m43s342ms ] So, in total, it took just six steps, six degrees of separation.
[ 0m44s112ms - 0m50s672ms ] And the idea is that this is not a unique example, that you could connect any two people on the planet in six steps or less.
[ 0m51s702ms - 0m52s832ms ] But is it really true?
[ 0m53s522ms - 0m56s362ms ] And if it is, how does it affect our lives?
[ 0m57s222ms - 1m3s222ms ] How is this possible in a world of now 8 billion people that we could be that close, just six hops or less?
[ 1m3s222ms - 1m6s892ms ] Does that affect how diseases spread, how information travels?
[ 1m7s432ms - 1m11s622ms ] Our math showed, the question is not why is the world small, it's really how could it be otherwise.
[ 1m12s222ms - 1m15s662ms ] But then I got a call from the FBI.
[ 1m16s882ms - 1m25s782ms ] We are making the world smaller all the time, like it's supposed to be good, and yet it does expose you to toxicity and malevolence that you might have been shielded from.
[ 1m26s162ms - 1m30s532ms ] You look at the net effect of it, and it's actually been pretty negative by a lot of measures.
[ 1m30s932ms - 1m32s32ms ] People have suffered.
[ 1m32s322ms - 1m40s722ms ] It's not only dangerous in terms of disease propagation, but anything malevolent now has conduits that it didn't used to have.
[ 1m42s512ms - 1m53s442ms ] If we were all connected to everyone else on the planet completely at random, then it would be almost a mathematical certainty that any two of us would be connected through fewer than six steps.
[ 1m54s532ms - 1m57s222ms ] Let's suppose I have my 100 friends out of 8 billion people.
[ 1m58s302ms - 2m5s562ms ] Each of them knows a 100 people, so two steps away from me is going to encompass 100 times 100 people.
[ 2m6s262ms - 2m7s692ms ] That's already 10 to the fourth people.
[ 2m8s122ms - 2m15s782ms ] And so, if you do 100 to the fifth power, that's 10 to the 10th and that's more people than there are on earth.
[ 2m16s142ms - 2m19s172ms ] So, that notice the number is five, I said to the fifth power.
[ 2m19s522ms - 2m24s122ms ] That's the ballpark reason why six degrees of separation is true.
[ 2m24s701ms - 2m40s621ms ] But the shocking thing about this is the calculation you've just outlined is about having 100 friends at random out of 10 billion and they're all over the world, but we know that in the real world, that's nowhere near what the distribution of friends are like.
[ 2m40s971ms - 2m41s951ms ] Yeah, absolutely true.
[ 2m41s951ms - 2m46s231ms ] So this this really crude calculation I did is is absurd for the reason that you said.
[ 2m46s561ms - 2m48s771ms ] The world is very far from random.
[ 2m49s311ms - 2m51s341ms ] The truth is, people naturally cluster geographically.
[ 2m51s801ms - 2m57s141ms ] Most of the people you know live close to you, and they also have a higher probability of knowing each other.
[ 2m57s611ms - 3m4s271ms ] If you calculate the fraction of people you know who also know each other, that is a measure of the clustering in the network.
[ 3m4s771ms - 3m7s751ms ] So, let's try a model with a high degree of clustering.
[ 3m8s701ms - 3m12s651ms ] Imagine all 8 billion people on Earth are arranged into a circle.
[ 3m13s301ms - 3m18s731ms ] And say each person knows the 100 people closest to them, so 50 to the left and 50 to the right.
[ 3m19s231ms - 3m23s891ms ] Well, in this case, the furthest person you can connect to is just 50 people away.
[ 3m24s281ms - 3m31s431ms ] So, if you wanted to connect to someone on the other side of the planet through a chain of people who know each other, well, it would take 80 million steps.
[ 3m32s31ms - 3m36s231ms ] And to connect any two people would take on average 40 million steps.
[ 3m37s241ms - 3m40s601ms ] Even just getting 10% of the way there would take 8 million steps.
[ 3m41s21ms - 3m44s381ms ] And six steps would get you, well, here.
[ 3m45s411ms - 3m48s161ms ] This is the paradox of six degrees of separation.
[ 3m48s891ms - 3m56s921ms ] We know that we live in these local clusters of friends and acquaintances, but we also seem to be able to connect anyone anywhere in just six steps.
[ 3m57s981ms - 4m6s181ms ] 10 years ago, I did my own experiment on this and I found that the average Veritasium viewer was only 2.7 degrees of separation from me.
[ 4m7s331ms - 4m17s851ms ] In social science, this is known as the small world problem, named after the phenomenon where you're, say, on holiday somewhere and you bump into a stranger who somehow knows your best friend.
[ 4m18s241ms - 4m21s631ms ] And you say, wow, it's such a small world.
[ 4m23s611ms - 4m29s811ms ] In the mid-1990s, two mathematicians, Duncan Watt and Steve Strogatz, set out to solve this small world problem.
[ 4m30s331ms - 4m35s171ms ] Duncan really sort of had very far-seeing imagination at that point.
[ 4m35s441ms - 4m42s1ms ] We had computers that allowed us to simulate environments that were too complicated for for math to work.
[ 4m42s421ms - 4m52s891ms ] Up until then, physicists had studied networks that were ordered and regular like crystal lattices, and mathematicians like Paul Erdosh had done lots of work on totally random networks.
[ 4m53s381ms - 4m56s181ms ] But no one had studied what happens in between.
[ 4m56s531ms - 5m1s811ms ] There's must be some enormous middle ground, and that's what Duncan and I felt like we're starting to explore.
[ 5m2s851ms - 5m8s921ms ] To study this middle ground, Watson and Strogatz imagined a simple, regular network of people or nodes, dotted around a circle.
[ 5m9s311ms - 5m12s651ms ] Each connected to a few of their nearest neighbors.
[ 5m13s381ms - 5m22s741ms ] And so we had this idea, we're going to start with the physicist end of regular, now we're going to turn the randomness knob to make it more and more random through these random shortcuts.
[ 5m23s261ms - 5m25s781ms ] We all have some experience with shortcuts.
[ 5m26s641ms - 5m31s841ms ] I belong to this club called Internet Chess Club. I got to be very friendly with a guy in Holland.
[ 5m32s381ms - 5m41s131ms ] That connection makes the world small because now, even though my friends don't realize it, they're only one step away from a guy in Holland.
[ 5m41s621ms - 5m49s31ms ] And so that kind of connection where you sort of connect to someone outside your normal circle is what we came to call a shortcut.
[ 5m50s191ms - 5m56s651ms ] So, they went around the circle, disconnecting some of the links and reconnecting them at random to a different node in the network.
[ 5m57s261ms - 6m9s11ms ] And as they did that, they watched what happened to the average number of steps it took to get from any one node in the network to another, hopping between connected nodes, in other words, the degree of separation.
[ 6m9s621ms - 6m11s651ms ] This is now the moment for the big reveal.
[ 6m12s221ms - 6m17s671ms ] As Duncan turned the knob in his computer simulations, as soon as he introduced a few shortcuts,
[ 6m19s141ms - 6m21s911ms ] the world immediately gets as small as a random graph.
[ 6m22s471ms - 6m30s901ms ] When they had rewired just 1% of the links to shortcuts, the average degree of separation dropped from 50 in the original fully ordered network to 10.
[ 6m31s721ms - 6m38s741ms ] But Watts and Strogatz also tracked how clustered the network was. That's the fraction of a node's connections that are also connected to each other.
[ 6m39s371ms - 6m43s461ms ] Or in other words, the fraction of my friends who are also friends with each other.
[ 6m44s121ms - 6m48s771ms ] What they found is that clustering remained high for much longer.
[ 6m50s271ms - 6m52s711ms ] The world immediately gets as small as a random graph.
[ 6m53s531ms - 6m56s641ms ] But it stays as clustered as if it were still regular.
[ 6m57s201ms - 7m3s451ms ] So you could simultaneously have the clustering that we know is real and the small world that we know is real.
[ 7m4s961ms - 7m20s591ms ] Now, in Watts and Strogatz's model, they looked at a thousand nodes, but if you apply their model to the 8 billion people on Earth, well, then you would only need three out of every 10,000 friendships to be a shortcut and the average degrees of separation drops to six.
[ 7m21s341ms - 7m26s641ms ] Our math showed, the question is not why is the world small, it's really how could it be otherwise.
[ 7m27s101ms - 7m33s761ms ] Duncan started saying to me, this is about discovering a whole new universe and and its properties and laws.
[ 7m34s851ms - 7m37s181ms ] I I recognized that he was right.
[ 7m37s923ms - 7m43s503ms ] I just wanted to to sort of reflect on what you said about these sort of shortcuts.
[ 7m43s503ms - 7m48s863ms ] I think I've had this phenomenon happen to me sometimes in my life where I'm sort of invited to an event
[ 7m48s863ms - 7m57s563ms ] and it seems like a very random event. Often I kind of feel like, oh I don't really want to go, you know, none of my friends are going.
[ 7m57s563ms - 8m1s893ms ] But but then maybe at the last minute I just say like, well, let's just roll the dice.
[ 8m2s243ms - 8m7s103ms ] And I find that almost invariably those are productive meetings.
[ 8m7s573ms - 8m19s53ms ] I'm kind of wondering if there's a takeaway for people here, which is that they should put themselves in situations where the probability of forming these shortcut links would it sort of increase the luck in your life?
[ 8m19s313ms - 8m26s93ms ] You um have just put your finger on a very famous phenomenon in sociology that is called the strength of weak ties.
[ 8m26s493ms - 8m28s933ms ] As you ask people how they got their job.
[ 8m29s873ms - 8m34s633ms ] And people would say, oh, yeah, I heard about it from, you know, Randy.
[ 8m34s913ms - 8m41s573ms ] And then he'd say, is Randy a friend of yours, and people invariably would say no, he's an acquaintance.
[ 8m41s573ms - 8m42s673ms ] I wouldn't call him a friend, he's an acquaintance.
[ 8m42s863ms - 8m46s433ms ] That's a weak tie, the strong tie is your best friend or your circle of friends.
[ 8m47s733ms - 8m54s533ms ] Excited about their breakthrough, Watts and Strogatz wanted to test their small world model on some real world data.
[ 8m54s743ms - 8m56s653ms ] But this was 1996.
[ 8m57s113ms - 9m2s233ms ] We had to think, well, where are we going to get data on big networks where we could test this?
[ 9m2s633ms - 9m3s333ms ] And it was not so easy.
[ 9m3s763ms - 9m6s913ms ] The internet was not mapped out, Google didn't exist.
[ 9m7s263ms - 9m9s613ms ] So they turned to an unusual source.
[ 9m10s383ms - 9m16s863ms ] There was only one nervous system that had been mapped at that time, which was the worm C. Elegance.
[ 9m17s333ms - 9m22s753ms ] Tiny worm like a millimeter that you can find in the dirt, a favorite of neurobiologists.
[ 9m23s223ms - 9m32s373ms ] They knew every cell in the body of C. Elegance from the time it's a single cell till it becomes a whole organism, so they had the total wiring diagram of that organism.
[ 9m33s443ms - 9m36s233ms ] Watts and Strogatz tested their model on the worm's neural network.
[ 9m36s603ms - 9m41s893ms ] The worm has precisely 282 neurons and on average, they're connected to 14 others.
[ 9m42s243ms - 9m50s153ms ] If you lay that all out in a line along the worm's body, the neurons at the ends would be separated by around 40 steps.
[ 9m50s383ms - 9m53s523ms ] And the average degree of separation would be around 14.
[ 9m54s13ms - 10m1s713ms ] But when Watts and Strogatz ran the calculations, they found the average degrees of separation between any two neurons was just 2.65.
[ 10m2s23ms - 10m6s523ms ] To put that in context, if they were connected totally at random, it would be 2.25.
[ 10m7s243ms - 10m10s733ms ] And yes, okay, so bingo, that was a small world. Then we were popping the champagne.
[ 10m10s733ms - 10m13s513ms ] I mean, that was really exciting the nature had done that.
[ 10m14s143ms - 10m20s223ms ] So then we thought, well, okay, but this should be true of a lots of networks because nature can't resist this mechanism.
[ 10m20s513ms - 10m26s853ms ] So they looked at Hollywood actors and power grids across the US. Sure enough, they were both small world networks.
[ 10m27s313ms - 10m34s773ms ] For example, in the database of over 200,000 Hollywood actors, the average degree of separation was less than four.
[ 10m35s993ms - 10m41s963ms ] Dangerfield was in Caddy Shack with Bill Murray, and Bill Murray was in She's Having a Baby with Kevin Bacon.
[ 10m42s593ms - 10m49s3ms ] Then the real payoff for us as people interested in dynamical systems, more than graph theory was, okay, so what?
[ 10m49s873ms - 10m59s673ms ] You know, so what if the world is small? Does that affect how things get in sync? Does it affect how diseases spread? Does it affect how information travels, whatever?
[ 11m0s283ms - 11m4s43ms ] And so we did a number of experiments again in the computer like that.
[ 11m5s23ms - 11m10s983ms ] Take disease, I wanted to know how a few shortcuts would affect how disease spreads through a network.
[ 11m11s283ms - 11m13s593ms ] So, I asked Casper and the team to make a simulation.
[ 11m14s353ms - 11m20s933ms ] And then the question to you is, do you want to start with a completely regular world where it's completely clustered or do you want to start with completely random?
[ 11m21s363ms - 11m22s753ms ] I would start with a regular world.
[ 11m22s993ms - 11m23s433ms ] Okay.
[ 11m25s23ms - 11m25s473ms ] There it goes.
[ 11m27s113ms - 11m28s323ms ] This is the spread of infections.
[ 11m28s763ms - 11m29s413ms ] Yeah.
[ 11m29s893ms - 11m31s843ms ] So, it takes over the world completely.
[ 11m32s3ms - 11m37s23ms ] Well, if every step was a day it would take 73 days to for the, you know, infection to take over this entire world.
[ 11m37s813ms - 11m39s753ms ] Let's introduce a few shortcuts and see.
[ 11m40s3ms - 11m42s63ms ] Okay. Let's make it small world like 10%.
[ 11m42s983ms - 11m43s463ms ] Let's go.
[ 11m46s223ms - 11m46s853ms ] Boom.
[ 11m47s343ms - 11m48s133ms ] Wow, it's really dramatic.
[ 11m49s133ms - 11m49s313ms ] Right?
[ 11m49s783ms - 11m51s523ms ] That's really dramatic and very fast.
[ 11m51s913ms - 11m52s293ms ] Yeah, so fast.
[ 11m53s293ms - 11m55s693ms ] Yeah, after 26 days the whole world.
[ 11m56s343ms - 12m3s243ms ] And that ramp up does look exponential at the beginning and then it kind of looks linear there as well, but it's almost like you can't go any faster.
[ 12m3s763ms - 12m4s13ms ] Yeah.
[ 12m4s313ms - 12m6s693ms ] Okay, so now let's make it a completely random network.
[ 12m9s253ms - 12m9s583ms ] Boom.
[ 12m10s33ms - 12m11s403ms ] Boom. Crazy.
[ 12m11s953ms - 12m14s333ms ] How many days now for a fully random network?
[ 12m14s783ms - 12m15s423ms ] 25.
[ 12m16s3ms - 12m16s623ms ] Basically identical.
[ 12m17s333ms - 12m20s763ms ] Which is crazy because in the random case, all your links are random.
[ 12m21s303ms - 12m26s643ms ] You know, in the small world case, it's just 10%. It's like if one out of your 10 friends are shortcut.
[ 12m26s863ms - 12m32s373ms ] Which, you know, for some people might be a bit much, but I reckon for you, it's probably about right.
[ 12m32s633ms - 12m33s443ms ] Yeah, I got lots of shortcuts.
[ 12m33s903ms - 12m34s143ms ] [laughter]
[ 12m36s573ms - 12m40s763ms ] But the crazy thing is that in this simulation, we only used 100 nodes.
[ 12m41s843ms - 12m49s23ms ] And if you use the same model to the 8 billion people on earth, then you would actually need less than 1% of all your links to be shortcuts.
[ 12m50s433ms - 12m55s103ms ] In 1998, Watts and Strogatz published their findings in a three-page article in Nature.
[ 12m55s453ms - 12m56s403ms ] And the paper took off.
[ 12m57s23ms - 13m0s883ms ] Within a few years, the paper already had hundreds of citations.
[ 13m1s213ms - 13m5s673ms ] By 2014, it was ranked the 63rd most cited paper of all time.
[ 13m6s143ms - 13m16s343ms ] And today, it's got around 58,000 citations. That's higher than Peter Higgs' paper on the Higgs boson and almost three times as many as Watson and Crick's Nobel Prize winning paper on DNA.
[ 13m17s413ms - 13m25s783ms ] So it's it's probably worth making that distinction that citations are one measure of impact, we're cited a lot more than Einstein and I think you know who's more important.
[ 13m26s273ms - 13m28s553ms ] [laughter] It's not it's not us.
[ 13m28s953ms - 13m31s493ms ] But it does mean people thought it was worth citing.
[ 13m31s793ms - 13m40s483ms ] We had many tens of thousands of citations from people in far-flung fields, from neuroscience to sociology, to graph theory, to computer science.
[ 13m40s783ms - 13m45s313ms ] Even, you know, English literature, people would do things like draw networks between words.
[ 13m45s733ms - 13m51s343ms ] Is there any irony in the fact that this paper on small world networks goes viral itself?
[ 13m51s433ms - 13m52s893ms ] [laughter]
[ 13m53s533ms - 13m55s843ms ] Um, I yes, I I think so.
[ 13m55s843ms - 13m56s183ms ] Maybe so.
[ 13m56s743ms - 13m59s443ms ] But then things got a little weird.
[ 14m0s113ms - 14m2s573ms ] That's when I started getting some strange phone calls.
[ 14m2s823ms - 14m6s133ms ] I got a call from somebody at the FBI.
[ 14m6s523ms - 14m9s13ms ] I was a little scared, what's the FBI calling me about?
[ 14m9s403ms - 14m14s763ms ] And so I called back and the person who picks up says, hair and fiber.
[ 14m15s563ms - 14m15s803ms ] [laughter]
[ 14m16s133ms - 14m26s693ms ] I was calling the hair and fiber network at the FBI, the people who do, you know, criminology based on what tell-tale hairs or fibers are left on the victim's clothes after they've been murdered.
[ 14m27s133ms - 14m36s543ms ] There was a guy who said, what happens when um the police have a suspect and they say, you have fibers on your sweater that match the hair of the victim.
[ 14m36s973ms - 14m49s633ms ] And then the defense lawyer says, well, you know, maybe the victim was on a bus and left her fibers on the bus, and then my client sat on the a secondary transfer, they would call it, of these fibers that doesn't prove anything.
[ 14m50s33ms - 14m57s743ms ] So the FBI wanted to know what's the probability of secondary transfers compared to primary transfers from actually killing the person.
[ 14m58s73ms - 15m0s193ms ] And like, I don't, what do I know?
[ 15m0s423ms - 15m1s23ms ] [laughter]
[ 15m2s123ms - 15m13s383ms ] Now, that's a Steve Strogatz problem. For most of us, a random caller telling you they're an FBI agent is probably a scam. Chances are they got your number from a data leak or a data broker.
[ 15m13s733ms - 15m22s343ms ] Anytime you provide your name, phone number, even your social security number, that personal information can be scraped, packaged and sold to anyone who will pay.
[ 15m22s753ms - 15m29s663ms ] And if criminals get hold of it, well, they can open credit card accounts in your name or even use it to stock or harass you.
[ 15m30s3ms - 15m32s83ms ] Fortunately, today's video sponsor, Incogni, can help.
[ 15m32s513ms - 15m41s473ms ] With your permission, they'll send out a letter to each broker using the correct legal terms and keep insisting until your data comes down.
[ 15m42s83ms - 15m46s833ms ] And remember, even one unremoved profile can be enough for criminals to target you.
[ 15m47s113ms - 15m54s773ms ] If you sign up to Incogni's unlimited plans, you can even flag public websites where your information appears with their custom removals tool.
[ 15m55s143ms - 15m57s323ms ] Their data agents will take care of the rest.
[ 15m57s653ms - 16m5s633ms ] Since I started using Incogni 18 months ago, they filed almost 700 requests for me and over 600 of those have been completed.
[ 16m6s173ms - 16m9s333ms ] With their unlimited family plan, you can protect your whole family, too.
[ 16m9s573ms - 16m17s743ms ] So, to keep your information safe, head over to incogni.com/veritasium by clicking the link in the description or just use this QR code.
[ 16m18s23ms - 16m22s773ms ] And when you do, be sure to use the code VERITASIUM for 60% off your annual subscription.
[ 16m23s213ms - 16m25s793ms ] So, I want to thank Incogni for sponsoring this video.
[ 16m26s163ms - 16m27s663ms ] And now back to networks.
[ 16m29s903ms - 16m37s623ms ] In 1999, Albert-László Barabási was studying the internet. At that time, there were around 800 million web pages.
[ 16m37s893ms - 16m44s633ms ] But despite the web's enormous size, Barabási found that on average, you could connect any two sites with just 19 clicks.
[ 16m46s173ms - 16m48s363ms ] Apparently, the web was a small world, too.
[ 16m48s643ms - 16m53s383ms ] But the strange thing was, it didn't look anything like the small world network in Watts and Strogatz's model.
[ 16m55s593ms - 17m3s43ms ] we ended up mapping out a region of the World Wide Web, and we had a very clear expectation of how that network should look like.
[ 17m3s463ms - 17m15s803ms ] Barabási thought the distribution of pages and links would resemble a bell curve, similar to what you'd get for people's height across a population. Most sites would have some average number of links, and there would be very few outliers either side.
[ 17m16s143ms - 17m17s543ms ] But that is not what he saw.
[ 17m19s143ms - 17m23s43ms ] And so we measured the distribution, and it didn't look anything like what we expected.
[ 17m23s773ms - 17m31s213ms ] The curve started out steep, loads of websites had not many links. Then there was this really long tail.
[ 17m31s723ms - 17m41s73ms ] And here we saw web pages that had not only a little more, but sometimes 100 times more links than the average degree or the average node in the website.
[ 17m42s213ms - 17m46s703ms ] These were websites like Yahoo, super connectors that linked to thousands of other sites.
[ 17m47s343ms - 17m55s683ms ] Barabási called them hubs because when he mapped out the network, they resembled the hub of a wheel with spokes going out to hundreds of other pages.
[ 17m55s833ms - 17m59s943ms ] And it was these hubs that made the web a small world, not shortcuts.
[ 18m0s283ms - 18m4s543ms ] So, Barabási wondered, how could this apply to other networks, too?
[ 18m6s103ms - 18m13s393ms ] Most real networks, or virtually all large networks, follow two very fundamental principles.
[ 18m14s143ms - 18m20s603ms ] First, any large network out there never pops out as a large network, but it grows, right?
[ 18m21s93ms - 18m27s343ms ] You have a tiny World Wide Web in 1991, and now we have trillions of nodes on the World Wide Web.
[ 18m27s533ms - 18m33s183ms ] How did we get to one to a trillion? One at a time, one website at a time.
[ 18m33s693ms - 18m40s753ms ] All the networks out there, no matter how old, how fast they emerged, they always emerge to some kind of growth process.
[ 18m41s173ms - 18m45s183ms ] So, if you think about networks, you must build in that growth process.
[ 18m45s683ms - 18m51s673ms ] Number two, when a new node comes in, you join Facebook, who are you going to connect to, right?
[ 18m52s163ms - 19m2s223ms ] And it is somewhat unpredictable, but it's biased. Your connections are always biased towards the more connected nodes simply because you more more likely to know more connected node than less connected node.
[ 19m3s153ms - 19m5s473ms ] He named this process preferential attachment.
[ 19m6s403ms - 19m12s653ms ] Barabási reasoned that these two principles could explain how hubs naturally emerge when a network grows.
[ 19m12s873ms - 19m16s863ms ] So, together with his colleague Réka Albert, he ran a simulation.
[ 19m17s543ms - 19m19s823ms ] We've also got a simulation for this.
[ 19m21s303ms - 19m24s143ms ] They started with a simple network of just a few connected nodes.
[ 19m24s513ms - 19m33s493ms ] Then they began adding new nodes to the network one at a time, with just one condition. They'd be more likely to connect to nodes that already had links.
[ 19m34s533ms - 19m35s443ms ] That's so cool.
[ 19m36s123ms - 19m38s363ms ] Looks very biological, very organic.
[ 19m39s263ms - 19m50s453ms ] Also, I like how the nodes come out and they don't just sort of stop in one spot, they kind of like wiggle around and like find their location. I I really like enjoyed this.
[ 19m51s53ms - 19m52s133ms ] It looks like a space station.
[ 19m53s773ms - 19m54s743ms ] That's what I was thinking.
[ 19m55s393ms - 19m56s653ms ] Or or like a space colony, right?
[ 19m56s653ms - 20m4s313ms ] Like the war. Yeah, yeah, right? Like each little center one could be a planet, then you've got all the sort of stations going around it.
[ 20m5s63ms - 20m5s693ms ] Yes.
[ 20m6s443ms - 20m10s333ms ] So, when Barabási and Albert let these networks evolve, hubs emerged.
[ 20m10s983ms - 20m17s883ms ] And we showed that growth and preferential attachment together naturally lead to the emergence of the hubs.
[ 20m18s673ms - 20m24s683ms ] With this simulation, Barabási and Albert showed how hubs could emerge in virtually any complex network.
[ 20m25s173ms - 20m26s163ms ] Take airports, for example.
[ 20m27s373ms - 20m36s733ms ] In 1955, Chicago O'Hare opened to commercial flights. Unlike neighboring airport Midway, it had long runways and plenty of space for new jet aircraft.
[ 20m37s23ms - 20m45s843ms ] Airlines began shifting service there. As more airlines connected flights to O'Hare, passengers had more options to connect, making it increasingly attractive.
[ 20m46s173ms - 20m51s233ms ] After deregulation in the 1970s, more airlines were free to add routes, and the feedback loop accelerated.
[ 20m51s673ms - 20m57s393ms ] Each new route made the airport more useful to passengers and more appealing to other airlines.
[ 20m57s713ms - 21m4s43ms ] Today, O'Hare is the most connected airport in the United States with direct flights to well over 200 destinations.
[ 21m5s263ms - 21m14s163ms ] But we don't just see hubs in manmade networks, in food webs, you have a few keystone species like Atlantic cod that connect hundreds of predators and prey.
[ 21m14s513ms - 21m21s333ms ] And in the metabolic networks in our cells, you have a few molecules like ATP that govern hundreds of chemical reactions.
[ 21m21s633ms - 21m28s623ms ] In the neural networks in our brain, you have a few regions like the prefrontal cortex that link hundreds of different functions.
[ 21m29s133ms - 21m40s753ms ] Now, as each of these networks evolved and grew over time, you had new species, new reactions and new circuits that latched on to what was already well connected, and so you get this sort of natural growth.
[ 21m41s473ms - 21m51s433ms ] Now, preferential attachment isn't the only mechanism that can create hubs. There are plenty of other factors at play, particularly in these more complex biological systems.
[ 21m51s803ms - 22m1s333ms ] But what Barabási's and Albert's simulation showed is that all it takes is a tiny bias when growing a network and hubs end up being inevitable.
[ 22m1s743ms - 22m8s123ms ] Once hubs are there, they fundamentally change the system the way the system behaves and the way we understand that system.
[ 22m9s273ms - 22m13s733ms ] Hubs like O'Hare mean you can get pretty much anywhere in the world in just a few flights.
[ 22m14s353ms - 22m17s333ms ] But that connectivity also has consequences.
[ 22m18s263ms - 22m26s243ms ] In August 2025, thunderstorms shut down Chicago O'Hare, and 280 flights were canceled and 80 were diverted.
[ 22m26s643ms - 22m33s493ms ] Overflow hit at least six other US airports, while some planes stuck in Chicago never left for Europe or Asia.
[ 22m34s143ms - 22m43s3ms ] Bad weather in Chicago totally changes not only the the trouble pattern in Chicago, but within 24 hours the whole country is being affected by that.
[ 22m44s183ms - 22m52s133ms ] And we see the same phenomenon in natural networks, knocking out one keystone species like Atlantic cod can destabilize an entire ecosystem.
[ 22m53s203ms - 22m55s593ms ] So this is what we call the Achilles heel of networks.
[ 22m55s793ms - 23m4s433ms ] And this could be good news or it could be bad news, right? Good news if you want to create drugs to to kill bacteria, then you're going to go for the hub.
[ 23m4s633ms - 23m12s213ms ] This idea has created a whole new field of network medicine, where researchers develop drugs to target crucial parts of a disease's metabolic network.
[ 23m12s603ms - 23m18s733ms ] But understanding the role of hubs doesn't just help develop cures for a disease, it can help us control its spread.
[ 23m19s953ms - 23m24s743ms ] In 1990, Thailand was facing one of the fastest growing HIV epidemics in the world.
[ 23m25s173ms - 23m33s423ms ] The government tried broad campaigns like posters, TV ads, and school talks telling everyone to use condoms, but the infection kept spreading.
[ 23m33s693ms - 23m38s743ms ] So in 1991, the government tried something different, they started targeting hubs.
[ 23m39s203ms - 23m43s863ms ] They told brothels around the country that every client must use a condom, or else they'd be shut down.
[ 23m44s203ms - 23m45s383ms ] And the impact was huge.
[ 23m45s733ms - 23m50s563ms ] For example, HIV infections among young men joining the military dropped by more than 50%.
[ 23m50s853ms - 23m57s713ms ] And by 2013, Thailand's Ministry of Public Health estimated the policy had prevented over 5 million infections.
[ 23m58s133ms - 24m1s233ms ] All because they realized the importance of hubs.
[ 24m3s243ms - 24m6s723ms ] Hubs and shortcuts make any complex network more connected than it seems.
[ 24m7s163ms - 24m12s563ms ] That means things spread quickly, whether that's airport delays, information or disease.
[ 24m13s263ms - 24m22s703ms ] But could that impact run even deeper? I mean, could the structure of our social network influence our very behavior and beliefs without us even being aware of it?
[ 24m24s423ms - 24m29s663ms ] Back in 1997, Watts and Strogatz investigated just that, using a game called the Prisoner's Dilemma.
[ 24m30s3ms - 24m36s53ms ] It's probably the most famous problem in game theory and it's used to represent a ton of different conflicts we see in the real world.
[ 24m36s393ms - 24m39s643ms ] We've actually done a full video on it before, but here's a quick recap.
[ 24m39s953ms - 24m45s103ms ] The premise is simple. A banker with a chest full of gold invites you and another player to play.
[ 24m45s373ms - 24m48s773ms ] You each get two choices, you can cooperate or defect.
[ 24m48s943ms - 24m51s973ms ] If you both cooperate, you each get three coins.
[ 24m52s383ms - 24m57s733ms ] But if you defect while your opponent cooperates, you get five coins and they get nothing.
[ 24m57s733ms - 24m59s333ms ] And if you both defect, then you