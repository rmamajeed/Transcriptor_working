---
title: ColdFusion_OpenAI is Suddenly in Trouble_20260221_part1
audio_file: ColdFusion_OpenAI is Suddenly in Trouble_20260221_part1.mp3
note_id: 8455c97f-5dbc-4e34-b065-0aacc2a55720
date_processed: '2026-03-01'
classification:
  primary_domain: AI
  sub_domains:
  - Machine Learning
  - Natural Language Processing
  - Artificial General Intelligence
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people:
  - name: Sam Altman
    role: CEO of OpenAI
    contribution: Made statements about OpenAI's business model and AI development
  - name: Cal Newport
    role: Computer Scientist
    contribution: Explained the scaling problem in AI
  - name: George Noble
    role: Former Fidelity Asset Manager
    contribution: Commented on OpenAI's financial situation
  - name: Mustafa Suleyman
    role: Microsoft's AI Chief
    contribution: Stated Microsoft's aim to be self-sufficient in AI
  works_cited: []
  concepts_mentioned:
  - Scaling Problem
  - LLMs
  - Transformer Architecture
  - Artificial General Intelligence
  - Chat GPT
  laws_theories_cited: []
concepts:
- name: Scaling Problem
  definition: The issue where giving LLMs exponentially more compute doesn't make
    them proportionally smarter
  parent_concepts:
  - Artificial Intelligence
  related_concepts:
  - LLMs
  - Transformer Architecture
  abstraction_level: Theoretical
  confidence: 0.9
- name: LLMs
  definition: Large Language Models
  parent_concepts:
  - Artificial Intelligence
  related_concepts:
  - Scaling Problem
  - Transformer Architecture
  abstraction_level: Theoretical
  confidence: 0.9
- name: Transformer Architecture
  definition: A type of neural network architecture used in LLMs
  parent_concepts:
  - Artificial Intelligence
  related_concepts:
  - Scaling Problem
  - LLMs
  abstraction_level: Theoretical
  confidence: 0.9
- name: Artificial General Intelligence
  definition: A type of AI that can perform any intellectual task
  parent_concepts:
  - Artificial Intelligence
  related_concepts:
  - Scaling Problem
  - LLMs
  abstraction_level: Theoretical
  confidence: 0.9
- name: Chat GPT
  definition: A conversational AI model developed by OpenAI
  parent_concepts:
  - Artificial Intelligence
  related_concepts:
  - LLMs
  - Transformer Architecture
  abstraction_level: Applied
  confidence: 0.9
relationships:
- source_concept: Scaling Problem
  target_concept: LLMs
  relationship_type: affects
  strength: 0.9
  evidence: Cal Newport's explanation
  reasoning: The scaling problem limits the development of LLMs
- source_concept: Transformer Architecture
  target_concept: LLMs
  relationship_type: enables
  strength: 0.9
  evidence: Cal Newport's explanation
  reasoning: The Transformer Architecture enables the development of LLMs
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: AI
  source_concept: Scaling Problem in LLMs
  target_domain: Biology
  target_concept: Cellular Growth and Division
  insight: Both face challenges in scaling while maintaining functionality and efficiency
  explanation: Just as LLMs encounter difficulties in scaling due to computational
    complexity and data requirements, cellular growth and division in biology face
    challenges in scaling up while maintaining cellular integrity and function. Both
    domains seek optimal solutions for growth without compromising performance. This
    analogy highlights the importance of efficient resource allocation and adaptive
    mechanisms in both AI and biological systems.
  potential_applications:
  - Optimization techniques for LLMs inspired by biological growth patterns
  confidence: 0.8
  historical_example: The study of fractals in nature and their application in optimizing
    computer networks
- connection_type: principle_application
  source_domain: AI
  source_concept: Transformer Architecture
  target_domain: Economics
  target_concept: Network Effects
  insight: Both leverage the power of interconnectedness to achieve greater value
  explanation: The Transformer Architecture in AI utilizes self-attention mechanisms
    to weigh the importance of different input elements relative to each other, similar
    to how network effects in economics create value through the interactions and
    interconnectivity of participants. This principle of deriving value from relationships
    can be applied across domains to understand and enhance complex systems.
  potential_applications:
  - Modeling economic networks using Transformer-inspired architectures
  confidence: 0.9
  historical_example: The development of the internet and its economic impact through
    network effects
- connection_type: metaphor
  source_domain: AI
  source_concept: Artificial General Intelligence
  target_domain: Psychology
  target_concept: Human Cognitive Development
  insight: AGI development can be seen as a metaphor for human cognitive development,
    with stages of learning and adaptation
  explanation: The pursuit of Artificial General Intelligence can be metaphorically
    understood through the lens of human cognitive development, where both involve
    stages of learning, adaptation, and the integration of new knowledge to achieve
    more general and flexible capabilities. This metaphor can provide insights into
    designing more effective learning pathways for AGI.
  potential_applications:
  - AGI training protocols inspired by human learning mechanisms
  confidence: 0.7
  historical_example: The use of cognitive architectures in AI inspired by human cognition
    models
- connection_type: historical_precedent
  source_domain: AI
  source_concept: Chat GPT
  target_domain: Linguistics
  target_concept: Language Acquisition
  insight: Chat GPT's ability to generate human-like text reflects and challenges
    theories of language acquisition
  explanation: The development and capabilities of language models like Chat GPT offer
    a unique lens through which to examine theories of language acquisition, as they
    mimic certain aspects of human language learning and production. This can provide
    insights into the cognitive and computational processes underlying human language
    abilities.
  potential_applications:
  - Using AI to model and understand human language acquisition processes
  confidence: 0.85
  historical_example: The Turing Test as a historical precedent for evaluating machine
    intelligence and language understanding
bridge_concepts:
- concept: Complexity
  appears_in_domains:
  - AI
  - Biology
  - Economics
  role: Describes systems with many interacting components
  examples:
  - LLMs in AI
  - Ecosystems in Biology
  - Markets in Economics
- concept: Networks
  appears_in_domains:
  - AI
  - Sociology
  - Computer Science
  role: Represents relationships between entities
  examples:
  - Neural Networks in AI
  - Social Networks in Sociology
  - Internet in Computer Science
mental_models:
- name: Systems Thinking
  description: Analyzing complex systems by understanding the relationships and interactions
    within them
  applied_to:
  - Understanding the scaling problem in LLMs
  transferable_to:
  - Biology
  - Economics
  - Environmental Science
- name: Feedback Loops
  description: Cycles of cause and effect that can reinforce or dampen behaviors
  applied_to:
  - Training processes in AI
  transferable_to:
  - Psychology
  - Sociology
  - Ecology
analogies_used:
- source_domain: Biology
  source_concept: Evolution through Natural Selection
  target_domain: AI
  target_concept: Evolutionary Algorithms
  mapping:
    Species: Solutions
    Fitness: Objective Function
  pedagogical_value: Helps in understanding how evolutionary principles can be applied
    to solve complex optimization problems in AI
tags:
  hierarchical:
  - '#AI → #MachineLearning → #NLP'
  - '#AI → #ArtificialGeneralIntelligence → #AGI'
  topical:
  - '#ScalingProblem'
  - '#LLMs'
  - '#TransformerArchitecture'
  methodological: []
  people:
  - '#SamAltman'
  - '#CalNewport'
  concepts:
  - '#ChatGPT'
  - '#ArtificialGeneralIntelligence'
  temporal:
  - '#2022'
  - '#2024'
  - '#2026'
  - '#2027'
summary: 'Here is a concise summary of the main points in 2-3 sentences:


  OpenAI, the company behind Chat GPT, is facing significant challenges, including
  a scaling problem where increasing computational power no longer leads to proportional
  improvements in AI intelligence. The company is also struggling financially, with
  projected losses of $14 billion in 2026 and a commitment to spend over $1 trillion
  on AI infrastructure, leading to concerns about its ability to generate revenue
  and pay back investors. As a result, OpenAI''s future is uncertain, with growing
  competition from other AI companies, including Google, and a lack of confidence
  in its leadership, particularly CEO Sam Altman, who has a history of making promises
  that don''t pan out.'
key_ideas:
- idea: Here are 3-5 key ideas or concepts discussed in the transcription text
  description: ''
- idea: OpenAI, the company behind Chat GPT, is facing significant financial and technological
    challenges, including a potential bankruptcy by 2027, due to its massive spending
    commitments and diminishing returns from its language models.
  description: No description provided by model.
- idea: The company's reliance on scaling up its language models to achieve better
    performance has hit a limit, known as the "scaling problem", where increasing
    computational power no longer leads to proportional improvements in intelligence,
    making it harder for OpenAI to stay ahead of its competitors.
  description: No description provided by model.
- idea: OpenAI is losing market share to competitors such as Google's Gemini, and
    is facing increased competition from other AI companies, including those offering
    open-source models, which could further erode its position in the market.
  description: No description provided by model.
- idea: The company's leadership, particularly Sam Altman, has a questionable track
    record of making promises that don't pan out, and has been accused of lying to
    investors and board members, which raises concerns about its ability to deliver
    on its promises and generate revenue.
  description: No description provided by model.
- idea: OpenAI's shift from a non-profit to a for-profit company has led to a focus
    on valuation and attracting new investment, rather than its original mission to
    benefit humanity, which has led to criticism and skepticism about its long-term
    viability.
  description: No description provided by model.
---
## Key Concepts

**Scaling Problem**  
The issue where giving LLMs exponentially more compute doesn't make them proportionally smarter

**LLMs**  
Large Language Models

**Transformer Architecture**  
A type of neural network architecture used in LLMs

**Artificial General Intelligence**  
A type of AI that can perform any intellectual task

**Chat GPT**  
A conversational AI model developed by OpenAI

## Cross-Domain Connections

**AI → Biology**

*Both face challenges in scaling while maintaining functionality and efficiency*

Just as LLMs encounter difficulties in scaling due to computational complexity and data requirements, cellular growth and division in biology face challenges in scaling up while maintaining cellular integrity and function. Both domains seek optimal solutions for growth without compromising performance. This analogy highlights the importance of efficient resource allocation and adaptive mechanisms in both AI and biological systems.

**AI → Economics**

*Both leverage the power of interconnectedness to achieve greater value*

The Transformer Architecture in AI utilizes self-attention mechanisms to weigh the importance of different input elements relative to each other, similar to how network effects in economics create value through the interactions and interconnectivity of participants. This principle of deriving value from relationships can be applied across domains to understand and enhance complex systems.

**AI → Psychology**

*AGI development can be seen as a metaphor for human cognitive development, with stages of learning and adaptation*

The pursuit of Artificial General Intelligence can be metaphorically understood through the lens of human cognitive development, where both involve stages of learning, adaptation, and the integration of new knowledge to achieve more general and flexible capabilities. This metaphor can provide insights into designing more effective learning pathways for AGI.

## Discussion Topics

- **Here are 3-5 key ideas or concepts discussed in the transcription text:** 
- **OpenAI, the company behind Chat GPT, is facing significant financial and technological challenges, including a potential bankruptcy by 2027, due to its massive spending commitments and diminishing returns from its language models.:** No description provided by model.
- **The company's reliance on scaling up its language models to achieve better performance has hit a limit, known as the "scaling problem", where increasing computational power no longer leads to proportional improvements in intelligence, making it harder for OpenAI to stay ahead of its competitors.:** No description provided by model.
- **OpenAI is losing market share to competitors such as Google's Gemini, and is facing increased competition from other AI companies, including those offering open-source models, which could further erode its position in the market.:** No description provided by model.
- **The company's leadership, particularly Sam Altman, has a questionable track record of making promises that don't pan out, and has been accused of lying to investors and board members, which raises concerns about its ability to deliver on its promises and generate revenue.:** No description provided by model.
- **OpenAI's shift from a non-profit to a for-profit company has led to a focus on valuation and attracting new investment, rather than its original mission to benefit humanity, which has led to criticism and skepticism about its long-term viability.:** No description provided by model.

## Full Transcription



**Transcription:**

**00:00 - 00:22** - **Speaker 1:** It is a bit scary to know that the most valuable private company in the world has your address and has shown up and has questions for you. They were asking for every former employee that we had spoken to and what we said to them, every congressional office that we spoke to, every potential investor that we spoke to. Tyler is just one of many advocates suddenly being targeted.

**00:23 - 01:06** - **Speaker 2:** Hi. Welcome to another episode of Cold Fusion. What you just saw there was basically OpenAI knocking on the doors of people who had spoken ill of them. Why are they so scared of what people are saying? Well, this is part of the reason why: on Friday, the 16th of January 2026, OpenAI dropped a bombshell. "We are starting to test ads in Chat GPT Free and Go, new $8 a month option tiers." That's right, OpenAI is incorporating ads into Chat GPT. Now, for any other startup, this is normal, even expected at this point. But for OpenAI, it's an admission that things aren't going so well. In fact, it's their last resort. Those aren't my words, but Sam Altman's words in October of 2024. He stated:

**01:07 - 01:25** - **Sam Altman:** I kind of think of ads as like a last resort for us for a business model. Um, I would do it if it meant that was the only way to get everybody on the world—in the world like access to great services. But if we can find something that doesn't do that, I'd prefer that.

**01:26 - 02:07** - **Speaker 2:** So after hundreds of billions of dollars in investment, increased competition, stupid side projects like the Sora app losing $15 million per day, having trillions in spending commitments, are we witnessing the beginning of the end for OpenAI? After taking 40% of all the RAM on Earth and causing a myriad of social, environmental, and economic problems for everyone, there's a sizeable section of people that would love to see this company go down in flames. And if things continue just the way they are, they just might get their wish. There's talk of the whole company going bankrupt by 2027. As former Fidelity asset manager George Noble states, "I've watched companies implode for decades. This one has all the warning signs."

**02:08 - 03:01** - **Speaker 2:** You are watching Cold Fusion TV. Last episode, we saw how AI failed at 96% of freelance work, but in this episode, we're specifically looking at OpenAI and the problems they're facing. From Anthropic's Claude to the open source Chinese models, the consumer AI landscape has rapidly changed. Today, OpenAI is no longer the clear leader it once was. Look, the way this works is we're going to tell you it's totally hopeless to compete with us on training foundation models, you shouldn't try, and it's your job to like try anyway. And I believe both of those things. I think it is pretty hopeless, but…

**03:02 - 03:40** - **Speaker 2:** They've spent too much money they don't have, the competition is catching up, and they're feeling the heat. In a nutshell, it doesn't look good. They've lost $12 billion in a single quarter. Their traffic has been falling for one year straight. Both Salesforce and Apple have ditched them for Gemini. Top leadership is leaving and they need $143 billion to become profitable. At this rate, even NVIDIA sounds less enthusiastic about investing in them.

**03:41 - 04:26** - **Speaker 3:** Can I just ask quickly about OpenAI again? Sure. Oh yes, yesterday you said that NVIDIA is not going to invest as much as $100 billion in OpenAI. Is that still the current wrong…?

**Speaker 4:** We never—we never said we were going to invest $100 billion in one round. That never was said.

**Speaker 3:** Well, like how about the overall commitment because last September, you and OpenAI…?

**Speaker 4:** There was never a commitment. It was "if they invited us—they invited us to so—let's start over again. They invited us to invest up to $100 billion and of course, we were very happy and honored that they invited us, but we will invest one step at a time."

**Speaker 3:** All right, but is that overall commitment still stand? Or it's not a commitment.

**Speaker 4:** I told you just now. Yeah, you keep putting words in my mouth. It's not… Yeah, yeah, I know that. They invited us to invest up to $100 billion and and we are honored that they invited us. We will consider each round one step at a time. Yeah.

**04:27 - 05:20** - **Speaker 2:** It appears that confidence in OpenAI is fading. As reported by the Financial Times, their closest partner, Microsoft, has signaled that they're distancing themselves from OpenAI. Microsoft's AI chief, Mustafa Suleyman, said that Microsoft is aiming to be self-sufficient in the AI space. So the problems for OpenAI can be split into four main parts: 1. The scaling problem; 2. Losing market share; 3. The financial black hole; and 4. The trust problem. If OpenAI was the only company on Earth with this technology, then maybe they'd be more of a chance to overcome these challenges. But with so much competition, it's going to be tough.

**05:21 - 07:11** - **Speaker 2:** Now, researching this topic made me realize one thing: understanding software is crucial. Which is why we've partnered with today's sponsor, boot.dev, to help you learn how to code. It sounds great in theory, but most people just watch a few tutorials, copy some code, and then give up. But with boot.dev, instead of passively watching videos, you learn by building things and solving problems from day one, just like how developers learn on the job. We've been using boot.dev at Cold Fusion and it feels more like a game than a course. You earn XP, complete quests, and fight bosses, all while learning real backend development skills. Their curriculum takes you through languages like Python, SQL, and Go, and when you're stuck, boot.dev's AI tutor called Boots helps guide you back on track. They've also just launched the training grounds, where you can grind unlimited challenges to lock in your skills before moving forward. Even if you vibe code for your projects, knowing how to code results in much better outcomes. All of boot.dev's content is free to read and watch, and a paid membership unlocks the interactive coding, AI assistance, project tracking, and game mechanics. There's also a 30-day no-questions-asked refund and a free demo of the interactive experience on every course. So if you've ever wanted to learn how to code or actually stick with it this time, head to boot.dev and use my code Cold Fusion to get 25% off your first year on the annual plan. Thanks to boot.dev for sponsoring this video.

**07:12 - 07:54** - **Speaker 2:** Now, back to the story. The first problem for OpenAI is that the capabilities of Chat GPT have somewhat stalled. It's at the infancy stages, but you can tell by their recent decisions. Sam Altman has gone from curing cancer to AI sex bots and a meme slot factory, and more recently, a translator app. All of this isn't a sign of a healthy business. Moreover, AI capabilities that are getting exponentially more powerful. Chat GPT made an absolute splash in its release in December 2022. Chat GPT 4 was another leap forward, but GPT-5 and beyond wasn't quite the revolution that was promised by Sam Altman. It seemed like stagnation had hit and hit hard. But why is this?

**07:55 - 08:30** - **Speaker 2:** It's an issue called the scaling problem. The scaling problem in AI, put simply, is the following: giving LLMs exponentially more compute doesn't make them proportionally smarter. Once upon a time, this was true, but that seems to be coming to an end. Here's computer scientist Cal Newport to explain it in more detail. It takes a second to get through the story, but it's interesting.

**08:31 - 10:25** - **Cal Newport:** In the beginning, we had language models. So we had these for a long time, and they were pretty good. You give them a bunch of text, and they were pretty grammatically good. They could produce pretty fluent text. But it was kind of they would veer off, and they couldn't really respond well to specific questions. But that was like the state of the world, right? So we had language models, these were studied for years in academia. Then we start to get this sort of accelerated sequence of advances. So the first of these advances comes in 2017. It's a team of researchers at Google figure out a better way to build these models; they're called Transformer architecture. The details don't matter, but it made it possible for these models to produce like long text, like produce a whole article, like produce a couple thousand words. So that was exciting. Then the second breakthrough comes. They do a research study. There's a researcher at OpenAI named Jared Kaplan, and he leads a group of researchers at OpenAI that includes Dario Amodei, who went on to be the CEO of Anthropic, and actually brought Kaplan with him. And they do a pretty simple experiment. They took basically GPT-2 and said, "What happens if we make this bigger?" It seems like an obvious thing to check, but there was this whole conventional wisdom in machine learning at this time that says, "Look, you can't make a model too big. If you make it too big, it's just going to memorize the training, and then when you give it new examples, it'll be terrible." And they said, "Let's check what happens if we actually just make these things bigger and forget about that concern." And what they found in that paper was it gets much better. It like defied the conventional wisdom of decades within the field of machine learning which was like, "Don't get too big. Your model's going to stop working if it gets too big. It's going to, you know…" It didn't. They're like, "Oh, it gets better, and not only does it get better, but it gets better pretty fast." And they drew a curve through the data points they had, and they extrapolated that curve, and it went up really fast. And so they said, "Let's try this." And the thing they tried it on was GPT-3.

**10:26 - 11:11** - **Speaker 2:** The GPT-3 model hype encouraged OpenAI to just make the model bigger—15 times bigger. The performance was so high that it validated the scaling laws. This sparked a frenzy in Silicon Valley. Soon, Sam Altman was saying that AI would automate the entire economy.

**Cal Newport:** Not only did it jump ahead, it jumped ahead fast. Like, so it really validated this curve. The Normies don't know this because they weren't as plugged into the AI world. But this sent Silicon Valley going crazy. And like, "Oh my God, if we keep making this bigger, GPT-5 or 6, this thing is going to be artificial general intelligence. It'll be able to do anything a human can do. We might only be like five years away." All right, so what happens next? Well, they say we need to show this to the public. So Chat GPT is GPT-3 tamed for public consumption. So now the public all knows about this. Four months later, GPT-4 comes out. And GPT-4 leaped up the curve exactly as predicted, exactly as—huge leap forward exactly as predicted by the paper. So now they're like, "Oh my God, we're like two iterations away. Like, this is it. All the money in the world needs to come to us because whoever wins this race is going to control the economy."

**11:12 - 12:32** - **Speaker 2:** But despite this massive scale, we may be reaching diminishing returns.

**Cal Newport:** GPT-5, they start working on it right away. So they build an even bigger data center, an even bigger model. They're calling this project Orion. By the summer of 2024—so last summer—they finished training this thing. Altman is telling his people, "This thing is going to blow away GPT-4, like, and is like, 'This thing scary. Scary me what this thing is going to do, right? Like, I don't know, this is it. We're about to go through the looking glass.'" They train this thing, then it stops working. Slightly better than GPT-4. Like, oh crap, this leaping up the curve every time we make this much bigger—this didn't work anymore. And so there is like this real realization of, "Oh, just making models bigger and training them on more data, it—the scaling law broke. It broke around GPT-4."

**12:33 - 13:44** - **Speaker 2:** There's a real risk that there may be inherent limits to current-day LLMs. Just adding more data may not be feasible for an exponential increase. Think of it this way: it's like a father saying, "My son was born just 10 months ago, and in that time he's gone from crawling to walking, and recently he's started running. In two years, little Timmy is definitely going to be able to fly." Obviously, that's not how it works, but it's the same concept here. There are certain limitations, mathematical limitations that cannot be crossed by scaling up. I showed it clearly mathematically in my book. So there were many different ideas of how to advance AI. One was, "We already actually have all the techniques that we need and we just need to scale them." But that was considered a very extreme opinion. And then on the other extreme, it was, "We don't even have the techniques yet." And interestingly, recently there's a New York Times story that says why we likely won't get to AGI anytime soon by Cade Metz. And he cites this stat that 75% of the longest-standing, most respected AI researchers actually still think to this day we don't actually have the techniques to get to AGI, if we will ever. So it's—we're kind of coming full circle now and it is starting to become unpopular again, this idea that you can just scale your way to so-called intelligence.

**13:45 - 15:43** - **Speaker 5:** Chat GPT, I need to wash my car and the car wash is 100 meters away. Should I walk or drive?

**Chat GPT:** Honestly, 100 meters is barely a stroll; it'll take just a minute or two on foot. Unless you've got heavy gear or there's something unusual going on, walking is probably the simplest and most pleasant choice. Plus, you'll save a little gas and get a tiny bit of fresh air.

**Speaker 5:** All right, so you think I should walk to the car wash instead of driving my car there?

**Chat GPT:** That's what I'd do. It's a short jaunt and it'll probably be less hassle than starting the car just for that.

**Speaker 5:** All right, so how do I wash my car if I walk there?

**Chat GPT:** You'll just bring what you need, maybe a small bag with your payment method and the car wash will have everything else. Once you get there, they'll handle the washing while you wait. You'll walk back with a sparkling car and maybe a little extra pep in your step.

**Speaker 5:** So my question is, um, how will the car get washed if the car is still at my house?

**Chat GPT:** Oh, I see what you mean now. If the car stays at home, it's not getting any cleaner, right? So yes, to actually wash it, you'll need to bring the car along. In that case, driving those 100 meters makes perfect sense.

**15:44 - 17:11** - **Speaker 2:** While Chat GPT and other LLMs can be extremely brilliant, even in high-level physics and maths, they don't yet have a true model of the world. Some computer scientists believe that that's an integral part of intelligence. Now I could be wrong, and a new fundamental neural network technique could be discovered, and that could move things along again. But as it stands right now, it seems that we're reaching a local limit. Now I have to be clear: every AI company faces this problem, but some are faring better than others. And one of those is Google. Now that Google has found their footing after the shock release of Chat GPT, new data suggests that Chat GPT is losing market share to Gemini. Chat GPT's market share dropped to 65% in January, which is approximately 20% lower than its 86% market share in January 2025. Chat GPT usage also stalled in late 2025. Average daily time spent per user dropped from 27 minutes to 21 minutes. While both have their strengths and weaknesses, Gemini appears to be much better in research, real-time information, and multimodal tasks, while Chat GPT is better at writing, coding, and conversation. Real-time information and multimodal tasks—i.e., uploading a photo or pointing a phone camera at a scene and getting information about it—is arguably more useful for the everyday person, especially on mobile. So Apple pushing OpenAI aside and going for Gemini makes sense. It's amazing to think that back in late 2022, Google was caught with their pants down when Chat GPT first came out. But today, they've more than caught up.

**17:12 - 18:01** - **Speaker 2:** And after all, it was Google researchers who laid the groundwork for the AI revolution with their 2017 breakthrough of the Transformer architecture. OpenAI simply took Google's work and ran with it. So in theory, Google researchers have the brains to come up with new theories in computer science to push AI forward. Some recent papers include nested learning and Simmer2, an AI that can reason and play video games generally. OpenAI, on the other hand, has a problem with staff continuously leaving. AI images is also another loss for OpenAI. The release of Google's Nano Banana Pro in November of 2025 triggered an internal crisis at OpenAI. Sam called a Code Red and paused all other projects to focus on image generation, but they still ended up falling short.

**18:02 - 19:23** - **Speaker 2:** And then there's the flood of open source Chinese models. Kling AI and Kwen are also gaining ground. Then there's the wildcards like Google's Project Genie, an AI that builds worlds, albeit static, just from a prompt. All of this is to say that OpenAI has threats from all sides. Knowing this, it's possibly the worst time for OpenAI to be shopping around for billions more in investment. If just in a year's time the competition will only be stronger. But it is a business. So I'm just wondering, like, eventually is the idea to kind of like license technologies? Will you have customers that you're going to be customizing algorithms for them or how how is it going to work?

**Sam Altman:** You know, the honest answer is we have no idea. Um, we we have never made any revenue. We have no current plans to make revenue. We have no idea how we may one day generate revenue. Um, we have made a soft promise to investors that once we've build this sort of generally intelligent system, um, basically we will ask it to figure out a way to generate an investment return for you.

**19:24 - 20:29** - **Speaker 2:** The third issue for OpenAI is the company's finances. The publication The Information saw internal documents from OpenAI, and the numbers don't look good. Setting aside the myriad of lawsuits, including a $134 billion one from Elon Musk, there's some real financial problems. After hundreds of billions in investment, 2026 will see a $14 billion loss. That's roughly three times worse than early 2025 estimates. OpenAI expects their first profit of $14 billion in 2029, but that's after losing $44 billion first. By some estimates, they'll be out of money by 2027. OpenAI is committed to spending over $1 trillion in AI data center infrastructure over eight years, and that's despite only bringing in $13 billion a year in recurring revenue. That's 1% of what they're promising to spend. OpenAI has also agreed to pay Oracle $60 billion per year starting in 2027. And in all of this, somehow OpenAI predicts that they'll be at $100 billion revenue by 2029. That's close to what NVIDIA makes. So it's possible, but unlikely. Other investors think so too. Blue Owl Capital recently pulled out of a $10 billion deal to fund an Oracle/OpenAI data center in Michigan. It could be a sign that investors are worried about OpenAI's ability to pay them back.

**20:30 - 21:25** - **Speaker 2:** Google, on the other hand, doesn't really have to worry about cash flow. The company made $86 billion in nine months and they can basically pour as much money as they want into AI. OpenAI, on the other hand, has to scream at the top of their lungs to attract more venture capital. There's yet more company behavior that indicates financial trouble. There's the floundering to spend $6.4 billion acquiring Jony Ive's design firm, and that's to build an AI hardware device. But according to reports, the development is going poorly, and it could end up like the Humane AI Pin. The AI erotica version of Chat GPT is self-explanatory, and the Sora app's user base has collapsed. Despite not having much to show versus the competition, Sam needs to talk a big game to get the investment rolling in. Curing cancer, replacing your GP, and discovering new science is a massive promise, but can we trust him?

**21:26 - 22:45** - **Speaker 2:** The final issue for OpenAI lies with Sam himself. His track record, frankly, is poor. It's almost like Altman's entire career was a series of promises that didn't pan out, all starting from his first company, Loopt, that he founded in 2005. It was kind of like a strange GPS-based social network. Sam Altman claimed a massive user base of 50,000, but they didn't exist. In reality, they had only 500 users. But he sold off the company for millions anyway. The next example happened in 2014 with Reddit. He scraped the whole website to feed into OpenAI's products, and then he promised to give 10% of the value back to the community, but this never happened. Next, OpenAI co-founder Ilya Sutskever, who has since left OpenAI, has accused Sam of a consistent pattern of lying. According to insiders, Sam Altman lied to OpenAI board members before being fired in 2023. So with this kind of track record, is he the guy who's going to deliver trillions in value? Or is most of this just talk, pumping up new investment? I'll leave that up to you.

**22:46 - 23:31** - **Speaker 2:** So little personal story. Back in 2022, I believe, I was in Melbourne and I watched Sam Altman give a talk. After the talk, he was swarmed by crowds of people wanting to take a photo with him. But today, the sentiment couldn't be more different. And it's partly to do with this: in 2015, OpenAI started as a non-profit. It was meant to benefit humanity. Now the only thing the company cares about is valuation and saying whatever they need to to attract new investment, by any means necessary. So to summarize everything: OpenAI went from a non-profit that had no plans to make revenue to a for-profit company that commits to spending a trillion dollars on data centers—a trillion dollars for diminishing returns due to the fundamental scaling problem with LLMs—all the while losing billions of dollars and losing out to growing competition in a sector that may just become a commodity in the end. Just in my opinion, it's not really a great financial bet as it stands. But after all that we've talked about, what do you think? Do you think OpenAI will survive or will the competition eat them alive? Anyway, that's about it from me. My name is Dagogo, and you've been watching Cold Fusion, and I'll catch you again soon for the next episode. Cheers guys. Have a good one.