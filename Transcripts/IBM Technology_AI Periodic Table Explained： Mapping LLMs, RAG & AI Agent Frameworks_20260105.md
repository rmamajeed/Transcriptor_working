---
title: IBM Technology_AI Periodic Table Explained： Mapping LLMs, RAG & AI Agent Frameworks_20260105
audio_file: IBM Technology_AI Periodic Table Explained： Mapping LLMs, RAG & AI Agent
  Frameworks_20260105.mp3
note_id: ebfedc4a-bab2-420a-87e1-e7cf161d84f2
date_processed: '2026-02-12'
classification:
  primary_domain: AI
  sub_domains:
  - Machine Learning
  - Natural Language Processing
  - Artificial General Intelligence
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people: []
  works_cited: []
  concepts_mentioned:
  - AI Periodic Table
  - Large Language Models
  - RAG
  - Embeddings
  - Guardrails
  laws_theories_cited: []
concepts:
- name: AI Periodic Table
  definition: A framework for organizing AI concepts and architectures
  parent_concepts:
  - Artificial Intelligence
  related_concepts:
  - Machine Learning
  - Natural Language Processing
  abstraction_level: Theoretical
  confidence: 0.9
- name: Large Language Models
  definition: AI models capable of processing and generating human-like language
  parent_concepts:
  - Machine Learning
  related_concepts:
  - RAG
  - Embeddings
  abstraction_level: Applied
  confidence: 0.9
- name: RAG
  definition: Retrieval-Augmented Generation, a technique for improving language models
  parent_concepts:
  - Natural Language Processing
  related_concepts:
  - Large Language Models
  - Embeddings
  abstraction_level: Practical
  confidence: 0.9
- name: Embeddings
  definition: Numerical representations of meaning in language
  parent_concepts:
  - Machine Learning
  related_concepts:
  - Large Language Models
  - RAG
  abstraction_level: Fundamental
  confidence: 0.9
- name: Guardrails
  definition: Runtime safety filters for AI systems
  parent_concepts:
  - Artificial Intelligence
  related_concepts:
  - Large Language Models
  - RAG
  abstraction_level: Practical
  confidence: 0.9
relationships:
- source_concept: Large Language Models
  target_concept: RAG
  relationship_type: supports
  strength: 0.8
  evidence: RAG is used to improve language models
  reasoning: RAG is a technique for improving language models by augmenting them with
    retrieval capabilities
- source_concept: Embeddings
  target_concept: RAG
  relationship_type: derives_from
  strength: 0.8
  evidence: RAG uses embeddings to represent meaning
  reasoning: RAG relies on embeddings to represent the meaning of language
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: AI
  source_concept: AI Periodic Table
  target_domain: Chemistry
  target_concept: Periodic Table of Elements
  insight: Both organize elements based on properties and relationships
  explanation: The AI Periodic Table and the Periodic Table of Elements both use a
    tabular format to organize and relate different elements based on their properties
    and behaviors, demonstrating a structural analogy between the two domains. This
    analogy can help in understanding how AI models can be organized and related to
    each other. The periodic nature of both tables also suggests potential cyclical
    patterns in AI model development and application.
  potential_applications:
  - AI model organization and discovery
  - Elemental property prediction
  confidence: 0.9
  historical_example: The development of the Periodic Table of Elements led to a systematic
    understanding of chemical properties and reactions, similarly, the AI Periodic
    Table could lead to a systematic understanding of AI models and their applications.
- connection_type: principle_application
  source_domain: AI
  source_concept: Large Language Models
  target_domain: Biology
  target_concept: Evolutionary Adaptation
  insight: Both involve iterative improvement through selection and adaptation
  explanation: Large Language Models improve through iterative training and adaptation,
    similar to how species evolve through natural selection and adaptation in biology.
    This principle of iterative improvement can be applied across domains to understand
    how complex systems adapt and evolve over time. The process of generating text
    based on context and feedback in Large Language Models mirrors the evolutionary
    process where organisms adapt to their environment based on selection pressures.
  potential_applications:
  - Evolutionary computation methods for AI
  - Understanding evolutionary dynamics
  confidence: 0.8
  historical_example: The concept of evolutionary adaptation has been applied in various
    fields such as economics and technology to explain how systems adapt over time.
- connection_type: metaphor
  source_domain: AI
  source_concept: RAG (Retrieval-Augmented Generation)
  target_domain: Cognitive Psychology
  target_concept: Human Memory Retrieval
  insight: Both involve retrieval and generation based on memory or knowledge
  explanation: RAG in AI involves the retrieval of relevant information from a database
    to augment the generation of new content, similar to how human memory retrieval
    works in cognitive psychology where memories are retrieved to inform decision-making
    or generate new ideas. This metaphor can help in understanding how AI systems
    can be designed to mimic human-like information retrieval and generation processes.
  potential_applications:
  - Designing more human-like AI systems
  - Improving human memory retrieval models
  confidence: 0.85
  historical_example: The development of memory models in cognitive psychology has
    influenced the design of information retrieval systems in AI.
- connection_type: historical_precedent
  source_domain: AI
  source_concept: Embeddings
  target_domain: Linguistics
  target_concept: Semantic Fields
  insight: Both represent meaning in a multidimensional space
  explanation: Embeddings in AI represent words or concepts in a multidimensional
    vector space based on their semantic meaning, similar to how semantic fields in
    linguistics represent words based on their meaning relationships. This historical
    precedent can help in understanding how linguistic theories can inform the development
    of AI models for natural language processing.
  potential_applications:
  - Improving natural language processing models
  - Understanding semantic meaning in language
  confidence: 0.9
  historical_example: The concept of semantic fields in linguistics has been influential
    in the development of word embeddings in AI.
- connection_type: principle_application
  source_domain: AI
  source_concept: Guardrails
  target_domain: Engineering
  target_concept: Safety Constraints
  insight: Both involve setting boundaries to ensure safe operation
  explanation: Guardrails in AI refer to the constraints and safeguards put in place
    to prevent AI systems from causing harm, similar to safety constraints in engineering
    that are designed to prevent accidents or failures. This principle of setting
    safety boundaries can be applied across domains to ensure the safe and reliable
    operation of complex systems.
  potential_applications:
  - Designing safer AI systems
  - Improving engineering safety protocols
  confidence: 0.8
  historical_example: The development of safety protocols in engineering has been
    influential in the design of guardrails in AI.
bridge_concepts:
- concept: Information Theory
  appears_in_domains:
  - AI
  - Biology
  - Engineering
  role: Understanding and quantifying information in complex systems
  examples:
  - Entropy in AI
  - Genetic information in biology
  - Signal processing in engineering
- concept: Complex Systems
  appears_in_domains:
  - AI
  - Biology
  - Economics
  role: Understanding and modeling complex interactions and behaviors
  examples:
  - Neural networks in AI
  - Ecosystems in biology
  - Market dynamics in economics
mental_models:
- name: Systems Thinking
  description: Understanding complex systems as interconnected components
  applied_to:
  - Analyzing AI systems as part of larger socio-technical systems
  transferable_to:
  - Understanding biological ecosystems
  - Analyzing economic markets
- name: First Principles
  description: Breaking down complex systems into fundamental principles
  applied_to:
  - Designing AI models from first principles
  transferable_to:
  - Understanding biological processes
  - Improving engineering designs
analogies_used:
- source_domain: Biology
  source_concept: Evolution through Natural Selection
  target_domain: AI
  target_concept: Iterative Improvement of AI Models
  mapping:
    Species: AI Models
    Selection Pressure: Training Data
  pedagogical_value: Helps in understanding how AI models can adapt and improve over
    time
tags:
  hierarchical:
  - '#AI → #MachineLearning → #NLP → #LLMs'
  topical:
  - '#AI'
  - '#RAG'
  - '#Embeddings'
  - '#Guardrails'
  methodological: []
  people: []
  concepts:
  - '#AIPeriodicTable'
  - '#LargeLanguageModels'
  - '#RAG'
  - '#Embeddings'
  - '#Guardrails'
  temporal: []
summary: The speaker proposes a conceptual "AI Periodic Table" to organize and structure
  the various terms and concepts in the field of artificial intelligence. The table
  is divided into rows and columns, with rows representing different levels of complexity
  (primitives, compositions, deployments, and emerging technologies) and columns representing
  different families or groups of related concepts (reactive, retrieval, models, and
  validation). The speaker fills in the table with various elements, such as prompts,
  embeddings, large language models, and guardrails, and demonstrates how these elements
  can be combined to create different AI systems and reactions. The goal of the AI
  Periodic Table is to provide a framework for understanding and categorizing the
  many different AI concepts and terms, and to help people navigate the complex and
  rapidly evolving field of AI.
key_ideas:
- idea: Here are the 3-5 key ideas discussed in the transcription text
  description: ''
- idea: The concept of an **AI Periodic Table** is introduced as a way to organize
    and structure the various elements and concepts in the field of Artificial Intelligence,
    similar to the periodic table in chemistry, which categorizes elements into families
    and periods.
  description: No description provided by model.
- idea: The AI Periodic Table is composed of **rows and columns**, with rows representing
    different levels of complexity (primitives, compositions, deployment, and emerging)
    and columns representing different families or groups of elements (reactive, retrieval,
    models, validation, and orchestration).
  description: No description provided by model.
- idea: The table includes various **elements**, each representing a specific concept
    or technology in AI, such as prompts, embeddings, large language models, and guardrails,
    which can be combined in different ways to create different **reactions** or AI
    systems.
  description: No description provided by model.
- idea: The AI Periodic Table can be used as a **framework for understanding and analyzing
    AI systems**, allowing users to identify the elements and reactions involved in
    a particular system and evaluate its safety, efficiency, and effectiveness.
  description: No description provided by model.
- idea: The table is not exhaustive, and there are still **gaps and emerging areas**
    in the field of AI that need to be explored and incorporated into the table, such
    as synthetic data, interpretability, and thinking models.
  description: No description provided by model.
---
## Key Concepts

**AI Periodic Table**  
A framework for organizing AI concepts and architectures

**Large Language Models**  
AI models capable of processing and generating human-like language

**RAG**  
Retrieval-Augmented Generation, a technique for improving language models

**Embeddings**  
Numerical representations of meaning in language

**Guardrails**  
Runtime safety filters for AI systems

## Cross-Domain Connections

**AI → Chemistry**

*Both organize elements based on properties and relationships*

The AI Periodic Table and the Periodic Table of Elements both use a tabular format to organize and relate different elements based on their properties and behaviors, demonstrating a structural analogy between the two domains. This analogy can help in understanding how AI models can be organized and related to each other. The periodic nature of both tables also suggests potential cyclical patterns in AI model development and application.

**AI → Biology**

*Both involve iterative improvement through selection and adaptation*

Large Language Models improve through iterative training and adaptation, similar to how species evolve through natural selection and adaptation in biology. This principle of iterative improvement can be applied across domains to understand how complex systems adapt and evolve over time. The process of generating text based on context and feedback in Large Language Models mirrors the evolutionary process where organisms adapt to their environment based on selection pressures.

**AI → Cognitive Psychology**

*Both involve retrieval and generation based on memory or knowledge*

RAG in AI involves the retrieval of relevant information from a database to augment the generation of new content, similar to how human memory retrieval works in cognitive psychology where memories are retrieved to inform decision-making or generate new ideas. This metaphor can help in understanding how AI systems can be designed to mimic human-like information retrieval and generation processes.

## Discussion Topics

- **Here are the 3-5 key ideas discussed in the transcription text:** 
- **The concept of an **AI Periodic Table** is introduced as a way to organize and structure the various elements and concepts in the field of Artificial Intelligence, similar to the periodic table in chemistry, which categorizes elements into families and periods.:** No description provided by model.
- **The AI Periodic Table is composed of **rows and columns**, with rows representing different levels of complexity (primitives, compositions, deployment, and emerging) and columns representing different families or groups of elements (reactive, retrieval, models, validation, and orchestration).:** No description provided by model.
- **The table includes various **elements**, each representing a specific concept or technology in AI, such as prompts, embeddings, large language models, and guardrails, which can be combined in different ways to create different **reactions** or AI systems.:** No description provided by model.
- **The AI Periodic Table can be used as a **framework for understanding and analyzing AI systems**, allowing users to identify the elements and reactions involved in a particular system and evaluate its safety, efficiency, and effectiveness.:** No description provided by model.
- **The table is not exhaustive, and there are still **gaps and emerging areas** in the field of AI that need to be explored and incorporated into the table, such as synthetic data, interpretability, and thinking models.:** No description provided by model.

## Full Transcription



00:00 - 00:30 Speaker 1: Does the world of AI feel a bit like this to you? A thousand terms all flying around. Everyone's talking about agents, and RAG, and embeddings, and guardrails, and you're just kind of supposed to know how it all fits together? Well, how about we put a structure to all this chaos? What if we could organize AI like chemistry organizes the elements into families and periods and predictable reactions? Well, welcome to the AI Periodic Table.

00:31 - 01:03 Speaker 1: Now, a quick disclaimer: there is no official AI periodic table like there is in chemistry. This is my take on what the structure could look like. But, once you understand it, you can basically decode any AI architecture, any product demo, any vendor pitch. You'll see which elements they're using, how they connect, and then maybe even what might be missing. So, let's fill in this table, starting at the top.

01:04 - 02:07 Speaker 1: So, you know what a prompt is, right? Well, that's my first element: PR. Now, a prompt contains instructions that you give to an AI, like "write me an email" or "summarize this document" or "explain quantum physics." And where this sits, actually matters. So, this element sits in a particular row, row number one, and row number one, this represents primitives. Now, you can't really break prompting down any further than this. You could say that it's atomic. And then this also sits in a column as well, which we're going to call groups or families. So, this is G1, and G1 is reactive because prompts are reactive. You change one word in your prompt, well, you're going to get a completely different output. So, that's the made-up element of PR for prompting.

02:08 - 02:40 Speaker 1: But prompting isn't alone in this group. It has a family of elements that get more reactive as you go down. And it's not alone in this row, either. So, we're going to map out five families across the top, and then we've got four rows down the side. And then you see these empty spaces here? Well, they're there for a reason, and we'll get to that. But let's fill in the rest of the primitives, row number one.

02:41 - 03:30 Speaker 1: So, what's the next element? Well, the next element is EM. That's for embeddings. So, if you've heard of vector databases or semantic search, you've probably bumped into embeddings, because they are numerical representations of meaning. So, you take some text, like "the cat sat on the mat," and you can turn that text into a list of numbers that capture its meaning. And similar meanings get similar numbers. It's still in row one, it's a primitive, but this is in group two now. And we're going to call group two the retrieval family, because now we are actually retrieving stuff. Embeddings are how AI systems search and remember.

03:31 - 04:22 Speaker 1: Okay, now we're going to skip ahead to the end here, to the next element. That's the element of LG: the Large Language Model, the LLM, you know, like ChatGPT, and Claude, and IBM Granite. You know these. And this goes all the way over here into this family, which we're calling G5, and G5 is the models family. These are, well, kind of the noble gases, the stable foundational capabilities that everything else reacts around. And notice that row one here, it only has three elements: prompts, and embeddings, and LLMs. That's it. And that's because in some ways, everything else in AI is built from combining these primitives.

04:23 - 05:41 Speaker 1: All right, let's move on to row number two now. And the first element here is the element of FC. That's function calling. So, this is when your LLM calls a tool before giving an answer. So, perhaps it invokes an API. If you ask a model "what's the weather," well, the model's going to call a weather API to give you some real data. So, it's still in the reactive family, group one. It's making things happen and taking action. But it's not a primitive anymore. So, this is row two, and row two is all about compositions. You need a model, and structured output, and tool integration. That makes a composition. And watch how the reactive family continues to evolve. So, down here, we've got the element AG, that's agents. Now, these use think-act-observe loops, so the AI plans, it takes an action, maybe using function calls, and it observes the result, and it keeps going until it reaches a goal. And that is row three, which is all about deployment: putting these things actually into production. So, look at the progression we've got here: from prompt, to function, to agent. Or we could say from control, to action, to autonomy. That's the reactive family.

05:42 - 06:33 Speaker 1: All right, let's fill in the rest of row two here. So, the next element, that is the element of VX: vector databases. These are data stores optimized for semantic search. You can store millions of embeddings and then query them to find the most relevant ones. This is group two now, the retrieval family, because vector databases are storage for semantic search. You compose embeddings, that's why it's row two, into a vector store.

06:34 - 07:25 Speaker 1: Okay, what's next? Well, the element of RG. That's RAG: Retrieval-Augmented Generation. One of my favorites, we've done a bunch of videos on this. So, you have a question, the system retrieves relevant context from your documents using embeddings and vector databases, then it augments the prompt with that context. Then the LLM can generate an answer based on what it retrieved. So, where does that go? Which family? It's going to go under the family of G3, which is the orchestration family, because RAG orchestrates multiple elements together: embeddings, and vector stores, and models. And notice that there is no primitive here in row one. That's because you can't really orchestrate one thing. Orchestration only emerges when you're combining multiple pieces.

07:26 - 07:51 Speaker 1: Okay, next in row two, we have the element of GR: guardrails. So, we're talking runtime safety filters, maybe schema validation. Basically, just making sure that the AI doesn't say something that it shouldn't do or just kind of output pure garbage. And that sits under the group four, which is all about validation.

07:52 - 08:23 Speaker 1: And then rounding out row two, the last element is MM. That's for multimodal models. So, these are LLMs that can kind of process images and they can process audio, as well as being able to read text. So, still column five, the models family. And that is row two complete. We've got five compositions that honestly basically power most AI systems today: these guys.

08:24 - 09:16 Speaker 1: All right, let's finish row three. So, we had AG for agent. The next element is FT for fine-tuning. So, you take a base model and then you adapt it. You train it on your specific data, on your domain, on your use case, like fine-tuning on medical papers or on your company's code base. Now, it's under the retrieval family because fine-tuning is adaptation. It's baking memory directly into the model's weights. So, look at that column now: we've got embeddings, which encode meaning; we've got vector databases, which store for search; and then we've got fine-tuning, which stores in parameters. So, three timescales of memory.

09:17 - 09:33 Speaker 1: Okay, next up is FW. That stands for framework. So, we're talking about things like, well, LangChain. These are the platforms that tie everything together to build and deploy AI systems. So, very much under the orchestration family.

09:34 - 09:49 Speaker 1: Next is RT, that's red teaming. This is adversarial testing where we're basically trying to break the AI, so jailbreaks and prompt injection and data exfiltration. It's under the validation family.

09:50 - 10:04 Speaker 1: And then under models, let's also throw in the element of SM. That's for small models: distilled, specialized models. They're fast, they're cheap, and they maybe run on your phone.

10:05 - 10:52 Speaker 1: All right, one last row, and first up is the element of MA. That is multi-agent, multi-agent systems. So, this is not one AI, it's multiple AIs that are all working together. They're debating and collaborating and specializing. So, maybe one agent does the research, one does the writing, one critiques all of it, and they coordinate to solve complex problems. So, this is a new row, it's row number four, and I'm going to call row number four "emerging." Now, this is not science fiction, it's stuff that's happening now, but it is still rapidly evolving. This is the reactive family kind of taken to the extreme.

10:53 - 11:24 Speaker 1: Right, so what else can we add to this row? Well, I would argue we could put SY here for synthetic data. This is using AI to generate training data for AI, which, yeah, sounds kind of weird, but it works. So, if you can't get enough real examples, you can generate synthetic ones. Now, this is not new, but it is emerging because as we hit the limits of available data for AI to train on, more and more is being done with synthetic data.

11:25 - 11:40 Speaker 1: All right, notice there's a gap here. I think there's really no clear emerging orchestration paradigm yet, at least to my eyes. What goes beyond frameworks here? Well, I should be curious to learn what you think would fill in that gap at some point.

11:41 - 12:03 Speaker 1: Anyway, moving on, the next element is IN for interpretability. So, this is about understanding why a model does what it does, kind of peeking inside of the black box and finding the neurons responsible for specific behaviors. And it's in the validation family as this is frontier safety work.

12:04 - 12:27 Speaker 1: And then rounding things out, we have the element of TH. This is for thinking models: models that don't answer immediately. They spend time reasoning. It's basically chain-of-thought built directly into the architecture: test-time compute scaling. These are the smartest models today, those are the ones that tend to be thinking models.

12:28 - 12:47 Speaker 1: So, there it is: the AI Periodic Table. At least my attempt at it. But periodic tables aren't just for memorization, they're for predicting reactions. And let me show you how these elements combine. So, I'm going to show you two reactions, but any AI system could be modeled here.

12:48 - 14:08 Speaker 1: So, first, let's build a chatbot that knows your company's documentation. It's one of the most common patterns in production AI. So, it starts with the element EM: embeddings. So, you take your documents and you turn them into vectors, and then you store them. Where do you store them? In the element of VX, into vector databases. Now, when a user asks a question, we use RAG, that's the element RG, and that is going to query the vector database and retrieve the relevant chunks. And those chunks augment the prompt here, the PR element, and that gets sent to the Large Language Model, the LG, to generate an answer that's grounded in your data. So, we've got these five elements here all combining. And actually, smart companies are going to probably add in one more element as well, and that is the element GR of guardrails because this kind of wraps the whole thing in safety filters and makes sure that the model isn't going to be leaking sensitive information. So, that, that's production RAG.

14:09 - 15:23 Speaker 1: All right, one other reaction I wanted to show you, which is the agentic loop. So, you give the AI a goal, let's say the goal is "book me a flight to Tokyo next month under $800." So, the element we're going to use for that is AG. Now, the AG agent is going to take that goal and it's going to break it down. So, first the agent needs to search flights, then check the calendar, then compare prices, and then book. So, to do that, it uses FC, function calling. Function calling calls external tools: the flight APIs, the calendar APIs, and the payment systems. And then the agent observes the results and decides the next action. So, this is basically a loop that goes back and forth here: think, act, observe; think, act, observe.

15:24 - 15:53 Speaker 1: So, that's the start of the reaction, but you might also build and deploy this using a framework. And that framework kind of gives you all of the plumbing you need for this loop. So, we've got here the AG element that's looping around FC and it's deployed into FW, into the framework. That's the agentic reaction.

15:54 - 16:60 Speaker 1: And there are so many different reactions we could show here. AI image generators, for example, which use the prompt as the text description, which is then sent to a multimodal model to output an image. Or code assistants, which are fine-tuned on code, which is then used to build a prompt with the context, and is then processed by the Large Language Model, the LG, to generate completions. They all basically fit somewhere in here.

16:01 - 16:48 Speaker 1: So, here's your challenge. Next time somebody pitches you with a fancy new AI feature, or a new AI product, or even an AI startup idea, try mapping it to this table. What elements are they using? What reactions are they running? Are they missing a safety element? Are they over-engineering the orchestration? Are they using a thinking model when perhaps a small model would do the job just as well? It's, it's all right here: a way to categorize and link all of these AI terms we talked about at the beginning. So, what do you think? Will we be seeing a version of this plastered on school classroom walls like the real periodic table at some point? Let me know in the comments.