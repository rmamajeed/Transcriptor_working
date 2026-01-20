---
title: Lex Clips_DeepSeek's GPU optimization tricks ｜ Lex Fridman Podcast_20250205
audio_file: Lex Clips_DeepSeek's GPU optimization tricks ｜ Lex Fridman Podcast_20250205.mp3
note_id: 2b9b667d-e9e1-4ecc-9d61-9d630c7aeff2
date_processed: '2026-01-17'
classification:
  primary_domain: AI
  sub_domains:
  - Deep Learning
  - GPU Optimization
  - Mixture of Experts
  difficulty_level: Advanced
  content_type: Discussion
entities:
  people:
  - name: Speaker 1
    role: Interviewer
    contribution: Asked questions about Deep Seek's GPU optimization tricks
  - name: Speaker 2
    role: Expert
    contribution: Explained Deep Seek's GPU optimization tricks and their implications
  - name: Speaker 3
    role: Expert
    contribution: Discussed the bitter lesson and its relevance to Deep Seek's approach
  works_cited:
  - title: The Bitter Lesson
    author: Rich Sutton
    year: 2019
  concepts_mentioned:
  - Deep Learning
  - GPU Optimization
  - Mixture of Experts
  - Nickel (Nvidia Communications Collective Library)
  - PTX (Parallel Thread Execution)
  - CUDA
  - Sparsity Factor
  - Auxiliary Loss
  laws_theories_cited:
  - The Bitter Lesson
concepts:
- name: Mixture of Experts
  definition: A deep learning model that consists of multiple expert models, each
    handling a specific subset of the input data
  parent_concepts:
  - Deep Learning
  related_concepts:
  - Sparsity Factor
  - Auxiliary Loss
  abstraction_level: Theoretical
  confidence: 1.0
- name: GPU Optimization
  definition: The process of optimizing the performance of deep learning models on
    Graphics Processing Units (GPUs)
  parent_concepts:
  - Deep Learning
  related_concepts:
  - Nickel
  - PTX
  - CUDA
  abstraction_level: Practical
  confidence: 1.0
- name: The Bitter Lesson
  definition: A concept in deep learning that suggests that simple, scalable models
    often outperform complex, hand-engineered ones
  parent_concepts:
  - Deep Learning
  related_concepts:
  - Mixture of Experts
  - GPU Optimization
  abstraction_level: Theoretical
  confidence: 1.0
relationships:
- source_concept: Mixture of Experts
  target_concept: GPU Optimization
  relationship_type: supports
  strength: 0.9
  evidence: Deep Seek's use of Mixture of Experts models requires careful GPU optimization
  reasoning: The complexity of Mixture of Experts models requires efficient GPU optimization
    to achieve good performance
- source_concept: The Bitter Lesson
  target_concept: Mixture of Experts
  relationship_type: derives_from
  strength: 0.8
  evidence: The Bitter Lesson suggests that simple, scalable models like Mixture of
    Experts can be effective
  reasoning: The Bitter Lesson provides a theoretical foundation for the effectiveness
    of Mixture of Experts models
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: AI
  source_concept: Mixture of Experts
  target_domain: Economics
  target_concept: Division of Labor
  insight: Both leverage specialization for efficiency
  explanation: The Mixture of Experts in AI and the Division of Labor in economics
    both rely on dividing tasks into specialized components to achieve greater efficiency
    and productivity. This structural analogy highlights how both domains recognize
    the benefits of specialization. The parallel lies in the distribution of tasks
    to specialized entities, whether they are AI models or human workers, to improve
    overall performance.
  potential_applications:
  - Task allocation algorithms
  - Economic modeling of AI impacts
  confidence: 0.9
  historical_example: Adam Smith's 'The Wealth of Nations' (1776) described the benefits
    of division of labor, a concept that now has a direct analogue in AI's Mixture
    of Experts
- connection_type: principle_application
  source_domain: AI
  source_concept: The Bitter Lesson
  target_domain: Biology
  target_concept: Evolutionary Adaptation
  insight: Both highlight the importance of adaptability over preconceptions
  explanation: The Bitter Lesson in AI, which emphasizes the superiority of simple,
    adaptive models over complex, preconceived ones, has a parallel in biology's evolutionary
    adaptation. In both domains, the ability to adapt and learn from the environment
    leads to better outcomes than rigid, pre-designed solutions. This principle applies
    across domains, suggesting that adaptability is a key factor in success, whether
    in AI systems or biological organisms.
  potential_applications:
  - Design of adaptive systems
  - Understanding evolutionary processes
  confidence: 0.8
  historical_example: Darwin's theory of evolution by natural selection (1859) demonstrates
    how adaptability leads to survival and success in biological systems, a principle
    now seen as crucial in AI development
- connection_type: metaphor
  source_domain: AI
  source_concept: GPU Optimization
  target_domain: Engineering
  target_concept: Manufacturing Process Optimization
  insight: Optimizing processes for efficiency is a common goal
  explanation: The process of optimizing GPU performance for AI computations shares
    a metaphorical connection with optimizing manufacturing processes in engineering.
    Both involve identifying bottlenecks, streamlining workflows, and fine-tuning
    parameters to achieve maximum efficiency and productivity. This metaphor highlights
    the universal importance of optimization across different domains.
  potential_applications:
  - Cross-domain optimization techniques
  - Efficiency in production lines
  confidence: 0.7
  historical_example: The development of the assembly line by Henry Ford (1913) is
    an early example of process optimization in manufacturing, a concept that now
    applies to optimizing AI computations
bridge_concepts:
- concept: Optimization
  appears_in_domains:
  - AI
  - Engineering
  - Economics
  role: Improving efficiency and productivity
  examples:
  - GPU Optimization in AI
  - Manufacturing Process Optimization in Engineering
  - Resource Allocation in Economics
mental_models:
- name: Systems Thinking
  description: Analyzing complex systems as a set of interconnected components
  applied_to:
  - Understanding the Mixture of Experts as a system
  transferable_to:
  - Analyzing economic systems
  - Understanding biological ecosystems
analogies_used:
- source_domain: Biology
  source_concept: Neural Networks
  target_domain: AI
  target_concept: Artificial Neural Networks
  mapping:
    Biological Neurons: Artificial Neurons
    Synapses: Weights
  pedagogical_value: Helps in understanding how AI neural networks are inspired by
    and mimic the structure and function of biological neural networks
tags:
  hierarchical:
  - '#AI → #DeepLearning → #GPUPerformance'
  topical:
  - '#MixtureOfExperts'
  - '#GPUPerformance'
  methodological:
  - '#Optimization'
  people:
  - '#RichSutton'
  concepts:
  - '#MixtureOfExperts'
  - '#GPUPerformance'
  temporal:
  - '#2025'
summary: 'Here is a concise summary of the main points in 2-3 sentences:


  The conversation discusses the innovations and challenges of training large AI models,
  specifically Deep Seek''s approach to mixture of experts (MOE) models and low-level
  optimization using Nvidia''s NCCL library. The speakers highlight the importance
  of simplicity, scalability, and avoiding human priors in the learning process, as
  outlined in the "bitter lesson" concept, and note that even small implementation
  changes can lead to significant gains. The conversation also touches on the stress
  and uncertainty of initiating training runs, the role of luck and skill in achieving
  success, and the increasing trend of "Yolo runs" where labs devote significant resources
  to a single, high-risk, high-reward training run.'
key_ideas:
- idea: Here are the 3-5 key ideas discussed in the transcription text, along with
    a brief description of each
  description: ''
- idea: Low-level engineering and optimization**
  description: The conversation highlights the importance of low-level engineering
    and optimization in achieving high performance in deep learning models, particularly
    in the context of mixture of experts (MOE) models and GPU programming.
- idea: Mixture of Experts (MOE) models and sparsity**
  description: The speakers discuss the challenges and benefits of MOE models, including
    the need for efficient communication and scheduling between experts, and the importance
    of sparsity in achieving high performance.
- idea: The role of luck and skill in achieving breakthroughs**
  description: The conversation touches on the idea that luck plays a role in achieving
    breakthroughs in deep learning, but also emphasizes the importance of skill, expertise,
    and a willingness to take risks (i.e., "Yolo runs") in driving progress.
- idea: The importance of standardized libraries and infrastructure**
  description: The speakers mention the importance of standardized libraries like
    Nvidia's Nickel (NCCL) in facilitating efficient communication and optimization,
    and the need for high-quality, readable code in achieving scalable and maintainable
    models.
- idea: The "Bitter Lesson" and the importance of simplicity**
  description: The conversation references the "Bitter Lesson" idea, which suggests
    that simple, scalable approaches often outperform more complex, human-engineered
    solutions, and emphasizes the importance of avoiding human priors and allowing
    models to learn and adapt naturally.
---
## Key Concepts

**Mixture of Experts**  
A deep learning model that consists of multiple expert models, each handling a specific subset of the input data

**GPU Optimization**  
The process of optimizing the performance of deep learning models on Graphics Processing Units (GPUs)

**The Bitter Lesson**  
A concept in deep learning that suggests that simple, scalable models often outperform complex, hand-engineered ones

## Cross-Domain Connections

**AI → Economics**

*Both leverage specialization for efficiency*

The Mixture of Experts in AI and the Division of Labor in economics both rely on dividing tasks into specialized components to achieve greater efficiency and productivity. This structural analogy highlights how both domains recognize the benefits of specialization. The parallel lies in the distribution of tasks to specialized entities, whether they are AI models or human workers, to improve overall performance.

**AI → Biology**

*Both highlight the importance of adaptability over preconceptions*

The Bitter Lesson in AI, which emphasizes the superiority of simple, adaptive models over complex, preconceived ones, has a parallel in biology's evolutionary adaptation. In both domains, the ability to adapt and learn from the environment leads to better outcomes than rigid, pre-designed solutions. This principle applies across domains, suggesting that adaptability is a key factor in success, whether in AI systems or biological organisms.

**AI → Engineering**

*Optimizing processes for efficiency is a common goal*

The process of optimizing GPU performance for AI computations shares a metaphorical connection with optimizing manufacturing processes in engineering. Both involve identifying bottlenecks, streamlining workflows, and fine-tuning parameters to achieve maximum efficiency and productivity. This metaphor highlights the universal importance of optimization across different domains.

## Discussion Topics

- **Here are the 3-5 key ideas discussed in the transcription text, along with a brief description of each:** 
- **Low-level engineering and optimization**:** The conversation highlights the importance of low-level engineering and optimization in achieving high performance in deep learning models, particularly in the context of mixture of experts (MOE) models and GPU programming.
- **Mixture of Experts (MOE) models and sparsity**:** The speakers discuss the challenges and benefits of MOE models, including the need for efficient communication and scheduling between experts, and the importance of sparsity in achieving high performance.
- **The role of luck and skill in achieving breakthroughs**:** The conversation touches on the idea that luck plays a role in achieving breakthroughs in deep learning, but also emphasizes the importance of skill, expertise, and a willingness to take risks (i.e., "Yolo runs") in driving progress.
- **The importance of standardized libraries and infrastructure**:** The speakers mention the importance of standardized libraries like Nvidia's Nickel (NCCL) in facilitating efficient communication and optimization, and the need for high-quality, readable code in achieving scalable and maintainable models.
- **The "Bitter Lesson" and the importance of simplicity**:** The conversation references the "Bitter Lesson" idea, which suggests that simple, scalable approaches often outperform more complex, human-engineered solutions, and emphasizes the importance of avoiding human priors and allowing models to learn and adapt naturally.

## Full Transcription



[ 0m3s354ms ] Speaker 1: And some of this is requires low-level engineering. Just is a giant mess and trickery. So, as I understand that went below Cuda. So they go super low programming of GPUs.
[ 0m15s48ms ] Speaker 2: Effectively, Nvidia builds this library called Nickel, right? Uh, in which, you know, when you're training a model, you have all these communications between every single layer of the model, and you may have over 100 layers, right?
[ 0m26s374ms ] Speaker 1: What does Nickel stand for?
[ 0m26s934ms ] Speaker 2: It's NCCL. Nvidia Communications Collective Library.
[ 0m30s784ms ] Speaker 1: Nice. Damn.
[ 0m34s74ms ] Speaker 2: Um, and so,
[ 0m34s834ms ] Speaker 2: when when you're training a model, right, you're going to have all these all reduces and all gathers, right? Uh between each layer, between the uh multi layer perceptron or feed forward network and the attention mechanism, you'll have you'll have basically the model synchronized, right? Um, or you'll have all the you'll have all reduce or all gather. Um, and and this is a communication between all the GPUs in the network, whether whether it's in training or inference.
[ 0m56s654ms ] Speaker 2: So Nvidia has a standard library. This is one of the reasons why it's really difficult to use anyone else's hardware uh for training is because no one's really built a standard communications library. Um and and Nvidia has done this at a sort of a higher level, right? Uh deep seek because they have certain limitations around the GPUs that they have access to, the interconnects are limited to some extent um by the restrictions of the GPUs that were shipped into China legally, not the ones that are smuggled, but legally shipped in, uh that they used to train this model, they had to figure out how to get efficiencies, right?
[ 1m28s704ms ] Speaker 2: And one of those things is that instead of just calling the Nvidia library, nickel, right? They instead created their, they scheduled their own communications, uh, which which the some of the labs do, right? Uh, Meta talked about in Lama 3 how they made their own custom version of Nickel. This is, they didn't, they didn't talk about the implementation details. This is some of what they did, probably not as well as, maybe not as well as deep seek because deep seek, you know, necessity is the mother of innovation, and they had to do this, whereas, uh, in the case, you know, Open AI has people that do this sort of stuff and tropic, et cetera. Uh, but, you know, Deep Seek certainly did it publicly and they may have done it even better because they were gimped on a certain aspect of the chips that they have access to.
[ 2m10s74ms ] Speaker 2: And so, they scheduled communications, uh, um, you know, by scheduling specific SMs. SMs, you could think of as like the core on a GPU, right? So there's hundreds of cores, or there's, you know, a bit over 100 cores, SMs on a GPU, and they were specifically scheduling, hey, which ones are running the model, which ones are doing all reduce, which one are doing all gather, right? And they would flip back and forth between them, and this requires extremely low-level programming.
[ 2m35s934ms ] Speaker 1: This is what Nickel does automatically. Or other Nvidia libraries handle this automatically, usually.
[ 2m40s24ms ] Speaker 2: Yeah, exactly. And so, technically they're using, you know, PTX, which is like sort of like, you could think of it as like an assembly type language, it's not exactly that or instruction set, right? Like coding directly to assembly or instruction set. It's not exactly that, but, uh, that's still part of technically CUDA, but it's like, do I want to write in Python, you know, PyTorch equivalent and call Nvidia libraries? Do I want to go down to the C level, right? Uh, you know, and code even lower level, or do I want to go all the way down to the assembly or ISO level? And, and there are cases where you go all the way down there at the very big labs, but most companies just do not do that, right? Because it's a waste of time and the efficiency gains you get are not worth it, but deep seeks implementation is so complex, right? Especially with their mixture of experts, right? Um, people have done mixture of experts, but they're generally 8, 16 experts, right? And they activate two. So, you know, one of the words we like, you like to use is like sparsity factor, right? Or usage, right? So, so you might have four, you know, one fourth of your model activate, right? And and and that's what Mistral's, uh, Mistral model, right? Uh, they're their model that really catapulted them to like, oh my god, they're really, really good. Um, Open AI has also had models that are MOE and and and so have all the other labs that are major closed.
[ 3m51s584ms ] Speaker 2: But what Deep Seek did that maybe only the leading labs have only just started recently doing is have such a high sparsity factor, right? It's not one fourth of the model, right? Two out of eight expert activating every time you go through the model, it's eight out of 256.
[ 4m5s694ms ] Speaker 3: And there's different implementations for mixture of experts where you can have some of these experts that are always activated, which this just looks like a small neural network and then all the tokens go through that, and then they also go through some that are selected by this routing mechanism.
[ 4m22s704ms ] Speaker 3: And one of the innovations in Deep Seek's architecture is that they change the routing mechanism in mixture of expert models, there's something called an auxiliary loss, which effectively means during training, you want to make sure that all of these experts are used across the tasks that the model sees. Why there can be failures in mixture of experts is that when you're doing this training, the one objective is token prediction accuracy, and if you just let training go with a mixture of expert model on your own, it can be that the model learns to only use a subset of the experts.
[ 4m58s384ms ] Speaker 3: And in the MOE literature, there's something called the auxiliary loss, which helps balance them. But if you think about the loss functions of deep learning, this even connects to the bitter lesson, is that you want to have the minimum inductive bias in your model to let the model learn maximally. And this auxiliary loss, this balancing across experts could be seen as intention with the prediction accuracy of the tokens. So we don't know the exact extent that the Deep Seek MOE change, which is instead of doing an auxiliary loss, they have an extra parameter in their routing, which after the batches, they update this parameter to make sure that the next batches all have a similar use of experts. And this type of change can be big, it can be small, but they add up over time.
[ 5m42s374ms ] Speaker 3: And this is the sort of thing that just points to them innovating, and I'm sure all the labs that are training big MOEs are looking at this sort of things, which is getting away from the auxiliary loss, some of them might already use it. But you just keep, you keep accumulating gains, and we'll talk about the philosophy of training and how you organize these organizations. And a lot of it is just compounding small improvements over time, in your data, in your architecture, in your post-training, and how they integrate with each other. Deep Seek does the same thing, and some of them are shared, or a lot, we have to take them on face value that they share their most important details. I mean, the architecture and the weights are out there, so we're seeing what they're doing. And it adds up.
[ 6m19s14ms ] Speaker 2: Going back to sort of the like efficiency and complexity point, right? It's 32 versus four, right? For like Mistral and other MOE models that have been publicly released. So this ratio is extremely high and sort of what Nathan was getting at there was, when you have such a different level of sparsity, um, you can't just have every GPU have the entire model, right? The model's too big, there's too much complexity there. So you have to split up the model, um, with different types of parallelism, right? And so you might have different experts on different GPU nodes, but now what, what happens when a, you know, this set of data that you get, hey, all of it looks like this one way and all of it should route to one part of my, you know, model, right? Um, so, so when all of it routes to one part of the model, then you can have the, you can have this overloading of a certain set of the GPU resources or a certain set of the GPUs and then the rest of the the training network sits idle because all of the tokens are just routing to that. So this is the biggest complexity, one of the biggest complexities with running a very, you know, sparse mixture of experts model, uh, I.e., you know, this 32 ratio versus this four ratio is that you end up with so many of the experts just sitting there idle.
[ 7m28s174ms ] Speaker 2: So how do I load balance between them? How do I schedule the communications between them? This is a lot of the like extremely low-level detailed work that they figured out in the public first and potentially like second or third in the world and maybe even first in some cases.
[ 7m43s467ms ] Speaker 1: What, uh, lesson do you, uh, in the direction of the bitter lesson, do you take from all of this? Where is this going to be the direction where a lot of the gain is going to be, which is this kind of low-level optimization? Or is this a short-term thing where the biggest gains will be more on the algorithmic high-level side of like post-training. Is this like a short-term leap because they've figured out like a hack because constraints, necessity is the mother of invention? Or is there, is there still a lot of gains?
[ 8m14s637ms ] Speaker 3: I think we should summarize what the bitter lesson actually is about. The bitter lesson essentially, if you paraphrase it, is that the types of training that will win out in deep learning as we go are those methods that which are scalable and learning and search is what it calls out. And this scale word gets a lot of attention in this. The interpretation that I use is effectively to avoid adding human priors to your learning process. And if you read the original essay, this is what it talks about, is how researchers will try to come up with clever solutions to their specific problem that might get them small gains in the short term, while simply enabling these deep learning systems to work efficiently and for these bigger problems in the long term might be more likely to scale and continue to drive success.
[ 9m11s957ms ] Speaker 3: And therefore, we were talking about relatively small implementation changes to the mixture of expert model. And therefore, it's like, okay, like we will need a few more years to know if one of these were actually really crucial to the bitter lesson. But the bitter lesson is really this long-term arc of how simplicity can often win. And there's a lot of sayings in the industry like the models just want to learn. You have to give them the simple lost landscape where you put compute through the model and and they will learn and getting barriers out of the way.
[ 9m43s727ms ] Speaker 1: That that's where the power of something like Nickel comes in where standardized code that can be used by a lot of people to create sort of simple innovations that can scale, which is why the hacks, the I imagine the the code base for Deep Seek is probably a giant mess.
[ 9m59s147ms ] Speaker 3: I'm sure they have, Deep Seek definitely has code bases that are extremely messy where they're testing these new ideas. Multi headlay and attention probably started could start in something like a Jupyter notebook or somebody tries something on a few GPUs, and that is really messy, but the stuff that trains a Deep Seek V3 and Deep Seek R1, those libraries, if you were to present them to us, I would guess are extremely high quality code where
[ 10m24s287ms ] Speaker 1: So high quality readable code.
[ 10m26s317ms ] Speaker 2: Yeah, I think there is one aspect to note though, right? Is that there is the general general ability for that to transfer across different types of runs, right? You may make really, really high quality code for one specific model architecture at one size. And then that is not transferable to, hey, when I, when I change this architecture tweak, everything's broken again, right? Like that's, that's something that could be, uh, you know, with their, with their specific low-level coding of like scheduling SMs, is specific to this model architecture and size, right? And, and whereas like Nvidia's collective library is more like, hey, it'll work for anything, right? You want to do an all reduce, great. I don't care what your model architecture is, it'll work. Uh, and you're giving up a lot of performance when you do that, uh, in many cases, but it's it's worthwhile for them to do the specific, uh, optimization for this specific run given the constraints that they have regarding compute.
[ 11m18s247ms ] Speaker 1: I wonder how stressful it is to like, you know, these frontier models like initiate training. Like to have the code to push the button that like you're now spending a large amount of money and time to train this. Like there must, I mean there must be a lot of innovation on the debugging stage of like making sure there's no issues that you're monitoring and visualizing every aspect of the training, all that kind of stuff.
[ 11m46s707ms ] Speaker 2: when when people are training, they have all these various dashboards, but like the most simple one is your loss, right? Uh and it continues to go down, but in reality, especially with more complicated stuff like MOE, the biggest problem with it or FP8 training, which is another innovation, you know, going to a lower precision number format, I.e., less accurate, is that you end up with loss spikes, right? And and no one knows why the loss spike happened. And for a long,
[ 12m8s927ms ] Speaker 1: Some of them you do.
[ 12m10s167ms ] Speaker 3: Some of them you do. Some of them are bad data. I can give AI2's example of what blew up our earlier models is a subreddit called Microwave Gang. We love to shout out this out. It's a real thing, you could pull up Microwave Gang. Essentially, it's a subreddit where everybody makes posts that are just the letter M. So it's like, So there's extremely long sequences of the letter M, and then the comments are like beep beep because that's what the microwave vents. But if you pass that into a model that's trained to be a normal producing text, it's extremely high loss because normally you see an M, you don't predict Ms for a long time. So like this is something that caused a loss spikes for us. But when you have much like this is this is old, this is not recent. And when you have more mature data systems, that's not the thing that causes the loss spike. And what Dylan is saying is true, but it's like it's it's levels to this sort of idea.
[ 12m55s617ms ] Speaker 2: With regards to the stress, right? These people are like, you know, you'll go out to dinner with a friend that works at one of these labs and they'll just be like, they'll just be like looking at their phone every like 10 minutes and they're not like, you know, it's one thing if they're texting, but they're just like like, is the lost going to be okay?
[ 13m11s187ms ] Speaker 3: Yeah, it's literally like tokens per second, loss not blown up. They're just walking, watching this.
[ 13m16s867ms ] Speaker 1: And the heart rate goes up if there's a spike.
[ 13m19s507ms ] Speaker 2: And some level of spikes is normal, right? It'll it'll recover and be back. Sometimes a lot of the old strategy was like, you just stop the run, restart from an old version and then like change the data mix and then it keeps going.
[ 13m30s117ms ] Speaker 3: They're even different types of spikes. So Doug Grenfell has a theory at AI2 that's like fast spikes and slow spikes where there are sometimes where you're looking at the loss and there are other parameters, you could see it start to creep up and then blow up, and that's really hard to recover from, so you have to go back much further. So you have the stressful period where it's like flat or it might start going up and you're like, what do I do? Whereas there are also loss spikes that are it looks good and then there's one spikey data point. And what you could do is you just skip those. You you see that there's a spike, you're like, okay, I can ignore this data, don't update the model and do the next one and it'll recover quickly. But these like on trickier implementations, as you get more complex in your architecture and you scale up to more GPUs, you have more potential for your loss blowing up. So there's like there's there's there's a distribution.
[ 14m14s357ms ] Speaker 2: And the whole idea of groking also comes in, right? It's like, just because it slowed down from improving and loss doesn't mean it's not learning because all of a sudden it could be like this and it could just spike down in loss again because it learned, truly learned something, right? Uh and it took some time for it to learn that. It's not like a gradual process, right? And that's that's what humans are like, that's what models are like. It's it's really a stressful task, as you mentioned.
[ 14m35s147ms ] Speaker 1: And the whole time, the dollar count is going up.
[ 14m38s137ms ] Speaker 3: Every company has failed runs. You need failed runs to push the envelope on your infrastructure. So a lot of news cycles are made of X company had Y failed run. Every company that's trying to push the frontier of AI has these. So is yes, it's noteworthy because it's a lot of money and it can be week to month setback, but it is part of the process.
[ 14m58s477ms ] Speaker 1: But how do you get, if you're deep seek, how do you get to a place where, holy shit, there is a successful combination of hyper parameters?
[ 15m6s667ms ] Speaker 3: A lot of small failed runs.
[ 15m8s417ms ] Speaker 1: And so, so rapid iteration through failed runs until
[ 15m13s197ms ] Speaker 3: and successful ones, you just
[ 15m14s617ms ] Speaker 1: And then you build up some intuition, like this, this mixture of expert works, and then this implementation of MLA works.
[ 15m22s877ms ] Speaker 3: key hyper parameters like learning rate and regularization and things like this. And you find the regime that works for your code base. I've talking to people at frontier labs, there's a story that you can tell where training language models is kind of a path that you need to follow. So you need to like unlock the ability to train a certain type of model or a certain scale. And then your code base and your internal know-how of which hyper parameters work for it is kind of known. And I you look at the deep seek papers and models, they've they've scaled up, they've added complexity, and it's just continuing to build the capabilities that they have.
[ 15m55s987ms ] Speaker 2: There's there's the concept of a Yolo run. Um, so Yolo, you only live once. Yep. Um, and and what it is is like, you know, there's, there's, there's all this experimentation you do at the small scale, right? Uh, research, oblations, right? Like you have your Jupyter notebook with your experimenting with MLA on like three GPUs or whatever. Um, and you're doing all these different uh things like, hey, do I do four expert, four active experts, 128 experts? Do I arrange the experts this way, you know, all these different uh model architecture things you're testing at a very small scale, right? Couple researchers, few GPUs, tens of GPUs, hundreds of GPUs, whatever it is. And then all of a sudden you're like, okay, guys, no more, no more fucking around, right? Uh, no more screwing around. Everyone take all the resources we have, let's pick what we think will work and just go for it, right? Yolo. And this is where that sort of stress comes in is like, well, I know it works here, but some things that work here don't work here, and some things that work here don't work down here, right? In terms of scale, right? So it's, it's, it's really truly a Yolo run. And and sort of like, there is this like, like discussion of like certain researchers just have like this methodical nature, like they can find the whole search space and like figure out all the oblations of different research and really see what is best. And there's certain researchers who just kind of like, you know, have that innate gut instinct of like, this is the Yolo run, like, I'm looking at the data, I think this is it.
[ 17m14s177ms ] Speaker 3: This is why you want to work in post-training because the GPU cost for training is lower, so you can make a higher percentage of your training runs yolo runs.
[ 17m20s767ms ] Speaker 2: Yeah, for now.
[ 17m21s347ms ] Speaker 3: Yeah, for now. For now, for now.
[ 17m24s427ms ] Speaker 1: So some of this is fundamentally luck still.
[ 17m28s447ms ] Speaker 2: Luck is skill, right? In many cases.
[ 17m30s987ms ] Speaker 1: Yeah, I mean it looks lucky, right? When you're
[ 17m32s837ms ] Speaker 3: But the hill to climb if you're out one of these labs and you have an evaluation and you're not crushing, there's a repeated playbook of how you improve things. There are localized improvements, which might be data improvements, and these add up into the whole model just being much better. And when you zoom in really close, it can be really obvious that this model is just really bad at this thing, and we can fix it, and you just add these up. So, it some of it feels like luck, but on the ground, especially with these new reasoning models we're talking to, is just so many ways that we can poke around, and normally it's that some of them give big improvements.
[ 18m5s257ms ] Speaker 2: The search space is near infinite, right? And and yet the amount of compute and time you have is very low and you're, you're you have to hit release schedules, you have to not get blown past by everyone, otherwise, you know, what happened with Deep Seek, you know, crushing Meta and Mistral and co here and all these guys, they moved too slow, right? They maybe were too methodical, I don't know, they didn't hit the Yolo run, whatever the reason was, maybe they weren't as skilled. Uh, whatever, you know, you can call it luck if you want, but at the end of the day, it's skill.
[ 18m32s17ms ] Speaker 1: So 2025 is the year of the Yolo run. It seems like all the labs are like going in.
[ 18m38s847ms ] Speaker 2: I I think it's even more impressive what Open AI did in 2022, right? At the time no one believed in mixture of experts models, right? At Google, uh, who had all the researchers. Uh, Open AI had such little compute and they devoted all of their compute for many months, right? All of it, 100% for many months to GPT 4, with a brand new architecture, with no belief that, hey, let me spend a couple hundred million dollars, which is all of the money I have on this model, right? That is truly Yolo. Right? Uh, now, now, you know, people are like, all these like training run failures that are in the media, right? It's like, okay, great, but like, actually, a huge chunk of my GPUs are doing inference, I still have a bunch doing research constantly, and yes, my biggest cluster is training, but like, on, on this Yolo run, but like that Yolo run is much less risky than like what Open AI did in 2022. Or maybe what Deep Seek did now or, you know, like sort of like, hey, we're just going to throw everything at it.
[ 19m33s447ms ] Speaker 1: The big winners throughout human history are the ones who are willing to do Yolo at some point.