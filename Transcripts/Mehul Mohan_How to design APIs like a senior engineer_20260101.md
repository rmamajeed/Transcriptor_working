---
title: Mehul Mohan_How to design APIs like a senior engineer_20260101
audio_file: Mehul Mohan_How to design APIs like a senior engineer_20260101.mp3
note_id: 4c4ffce2-c880-4ddc-bde8-84088289bf2c
date_processed: '2026-03-03'
classification:
  primary_domain: Computer Science
  sub_domains:
  - Software Engineering
  - API Design
  - Backend Development
  difficulty_level: Intermediate
  content_type: Tutorial
entities:
  people:
  - name: Mehul Mohan
    role: Senior Developer
    contribution: Explaining API design best practices
  works_cited: []
  concepts_mentioned:
  - API Design
  - REST API
  - Rate Limiting
  - Data Validation
  - Authentication
  laws_theories_cited: []
concepts:
- name: API Design
  definition: The process of designing and building APIs to interact with backend
    systems
  parent_concepts:
  - Software Engineering
  related_concepts:
  - REST API
  - Rate Limiting
  abstraction_level: Applied
  confidence: 0.9
- name: REST API
  definition: An architectural style for designing networked applications
  parent_concepts:
  - API Design
  related_concepts:
  - API Design
  - Rate Limiting
  abstraction_level: Theoretical
  confidence: 0.9
- name: Rate Limiting
  definition: A technique to control the frequency of requests to an API
  parent_concepts:
  - API Design
  related_concepts:
  - API Design
  - REST API
  abstraction_level: Practical
  confidence: 0.9
- name: Data Validation
  definition: The process of checking the accuracy and consistency of data
  parent_concepts:
  - Software Engineering
  related_concepts:
  - API Design
  - Authentication
  abstraction_level: Fundamental
  confidence: 0.9
- name: Authentication
  definition: The process of verifying the identity of users or systems
  parent_concepts:
  - Software Engineering
  related_concepts:
  - API Design
  - Data Validation
  abstraction_level: Fundamental
  confidence: 0.9
relationships:
- source_concept: API Design
  target_concept: REST API
  relationship_type: supports
  strength: 0.8
  evidence: Mehul Mohan mentions REST API as a common approach to API design
  reasoning: REST API is a specific style of API design
- source_concept: API Design
  target_concept: Rate Limiting
  relationship_type: applies_to
  strength: 0.9
  evidence: Mehul Mohan discusses rate limiting as a crucial aspect of API design
  reasoning: Rate limiting is a technique used in API design to control request frequency
- source_concept: Data Validation
  target_concept: Authentication
  relationship_type: supports
  strength: 0.8
  evidence: Mehul Mohan mentions data validation as a necessary step before authentication
  reasoning: Data validation is used to ensure the accuracy of data before authenticating
    users
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: Computer Science
  source_concept: Rate Limiting
  target_domain: Economics
  target_concept: Supply and Demand
  insight: Managing resource utilization through limits
  explanation: Rate limiting in computer science and supply and demand in economics
    both deal with managing the utilization of resources. In computer science, rate
    limiting is used to prevent abuse and ensure fair usage of APIs, while in economics,
    supply and demand dictate the allocation of resources in a market. Both concepts
    rely on the idea of balancing the availability of resources with the demand for
    them, highlighting a structural analogy between the two domains.
  potential_applications:
  - Resource management in cloud computing
  - Market regulation in economics
  confidence: 0.9
  historical_example: The concept of supply and demand has been applied to resource
    management in various domains, including the management of network resources in
    computer science.
- connection_type: principle_application
  source_domain: Computer Science
  source_concept: Authentication
  target_domain: Biology
  target_concept: Immune System
  insight: Recognizing and responding to foreign entities
  explanation: The principle of authentication in computer science, where systems
    verify the identity of users or entities, has a parallel in the biological immune
    system. The immune system recognizes and responds to foreign entities, such as
    pathogens, to protect the body. This principle of recognition and response can
    be applied across domains, highlighting the importance of authentication in maintaining
    system integrity.
  potential_applications:
  - Biometric authentication
  - Immunotherapy
  confidence: 0.8
  historical_example: The discovery of the immune system's ability to recognize and
    respond to pathogens has inspired advancements in computer security, including
    the development of intrusion detection systems.
- connection_type: metaphor
  source_domain: Computer Science
  source_concept: API Design
  target_domain: Architecture
  target_concept: Building Design
  insight: Designing interfaces for interaction
  explanation: The design of APIs in computer science, which involves creating interfaces
    for different systems to interact with each other, can be metaphorically compared
    to the design of buildings in architecture. Both involve creating structures that
    facilitate interaction, whether it's between systems or people. The principles
    of good API design, such as simplicity and usability, can be applied to building
    design to create more functional and user-friendly spaces.
  potential_applications:
  - Designing smart buildings
  - API-based urban planning
  confidence: 0.7
  historical_example: The design of iconic buildings, such as the Guggenheim Museum,
    has been influenced by principles of interaction and usability, similar to those
    applied in API design.
bridge_concepts:
- concept: Modularity
  appears_in_domains:
  - Computer Science
  - Biology
  - Engineering
  role: Enables complexity management and adaptability
  examples:
  - Software design patterns
  - Biological modules in gene regulation
  - Modular product design in engineering
mental_models:
- name: Systems Thinking
  description: Analyzing complex systems as interconnected components
  applied_to:
  - Understanding API ecosystems
  - Designing resilient systems
  transferable_to:
  - Economics
  - Environmental Science
  - Social Sciences
analogies_used:
- source_domain: Electrical Engineering
  source_concept: Circuit Breakers
  target_domain: Computer Science
  target_concept: Rate Limiting
  mapping:
    Circuit Breaker: Rate Limiter
    Electrical Current: API Requests
  pedagogical_value: Helps understand the purpose and function of rate limiting in
    managing API requests, by comparing it to a familiar concept in electrical engineering.
tags:
  hierarchical:
  - '#ComputerScience → #SoftwareEngineering → #APIDesign'
  topical:
  - '#APIDesign'
  - '#RESTAPI'
  - '#RateLimiting'
  - '#DataValidation'
  - '#Authentication'
  methodological:
  - '#Tutorial'
  people:
  - '#MehulMohan'
  concepts:
  - '#APIDesign'
  - '#RESTAPI'
  - '#RateLimiting'
  - '#DataValidation'
  - '#Authentication'
  temporal: []
summary: 'Here is a concise summary of the main points in 2-3 sentences:


  Mehul Mohan discusses how to design robust backend APIs as a senior developer, emphasizing
  the importance of validating data, rate limiting, and authentication. He recommends
  using a single API endpoint with a POST request, validating the request body using
  a library like Zod, and implementing rate limiting based on the user''s account
  ID, which can be extracted from a JWT signed token. By following these best practices,
  developers can build highly scalable and secure APIs that are resistant to common
  vulnerabilities and attacks.'
key_ideas:
- idea: Here are the 3-5 key ideas or concepts discussed in the transcription text
  description: ''
- idea: Designing a robust backend API**
  description: The speaker emphasizes the importance of designing a robust and scalable
    backend API, and provides guidance on how to achieve this, including using a single
    endpoint, POST requests, and validating data strictly.
- idea: Rate limiting and authentication**
  description: The speaker discusses the importance of rate limiting and authentication
    in backend APIs, and provides recommendations on how to implement these, including
    using a rate limiting key based on the account ID and authenticating users using
    a JWT signed token.
- idea: Validating data and using schemas**
  description: The speaker stresses the importance of validating data and using schemas
    to define the structure of the data, and recommends using libraries such as Zod
    to define and validate input schemas.
- idea: API structure and organization**
  description: The speaker suggests organizing APIs into separate files and folders,
    with each API having its own handler and constants file, and recommends defining
    metadata such as rate limits and validation rules on a per-API basis.
- idea: Using JWT signed tokens for authentication**
  description: The speaker recommends using JWT signed tokens for authentication,
    as they can be verified without a database lookup, and can be used to extract
    the account ID for rate limiting purposes.
---
## Key Concepts

**API Design**  
The process of designing and building APIs to interact with backend systems

**REST API**  
An architectural style for designing networked applications

**Rate Limiting**  
A technique to control the frequency of requests to an API

**Data Validation**  
The process of checking the accuracy and consistency of data

**Authentication**  
The process of verifying the identity of users or systems

## Cross-Domain Connections

**Computer Science → Economics**

*Managing resource utilization through limits*

Rate limiting in computer science and supply and demand in economics both deal with managing the utilization of resources. In computer science, rate limiting is used to prevent abuse and ensure fair usage of APIs, while in economics, supply and demand dictate the allocation of resources in a market. Both concepts rely on the idea of balancing the availability of resources with the demand for them, highlighting a structural analogy between the two domains.

**Computer Science → Biology**

*Recognizing and responding to foreign entities*

The principle of authentication in computer science, where systems verify the identity of users or entities, has a parallel in the biological immune system. The immune system recognizes and responds to foreign entities, such as pathogens, to protect the body. This principle of recognition and response can be applied across domains, highlighting the importance of authentication in maintaining system integrity.

**Computer Science → Architecture**

*Designing interfaces for interaction*

The design of APIs in computer science, which involves creating interfaces for different systems to interact with each other, can be metaphorically compared to the design of buildings in architecture. Both involve creating structures that facilitate interaction, whether it's between systems or people. The principles of good API design, such as simplicity and usability, can be applied to building design to create more functional and user-friendly spaces.

## Discussion Topics

- **Here are the 3-5 key ideas or concepts discussed in the transcription text:** 
- **Designing a robust backend API**:** The speaker emphasizes the importance of designing a robust and scalable backend API, and provides guidance on how to achieve this, including using a single endpoint, POST requests, and validating data strictly.
- **Rate limiting and authentication**:** The speaker discusses the importance of rate limiting and authentication in backend APIs, and provides recommendations on how to implement these, including using a rate limiting key based on the account ID and authenticating users using a JWT signed token.
- **Validating data and using schemas**:** The speaker stresses the importance of validating data and using schemas to define the structure of the data, and recommends using libraries such as Zod to define and validate input schemas.
- **API structure and organization**:** The speaker suggests organizing APIs into separate files and folders, with each API having its own handler and constants file, and recommends defining metadata such as rate limits and validation rules on a per-API basis.
- **Using JWT signed tokens for authentication**:** The speaker recommends using JWT signed tokens for authentication, as they can be verified without a database lookup, and can be used to extract the account ID for rate limiting purposes.

## Full Transcription




00:00 Mehul Mohan: This is a 15-minute information-dense video on how do you design backend APIs as a senior developer. Now, make sure you leave a like, subscribe to the channel, and also leave a comment below if you like this video. That helps the channel grow. Now, right at it, what we have is a backend system, right? So I will not go into specific frameworks or languages or constructs like GraphQL or, you know, Express.js or any of this. We will not talk about this because I understand every single backend is different. Your tech stack might be different, your technology might be different. But I'm going to show you how a request is supposed to flow in your backend, right?

00:44 Mehul Mohan: So, see, there are multiple ways to go about designing an API. If it's a private API, it doesn't really matter how you're doing it, right? So there's a concept of REST API, which follows a lot of these standards like 200 OK, 404 not found, you know, 500 internal server error and so on. I am not a huge fan of this. Let's put it on record. Let's be honest about this. I as a developer am not a huge fan of REST because it's very easy to lie in REST. It's easy to say that something was 200 OK, but it was not really. It is easy to say 404 not found, but maybe you do have a resource. It's easy to say 500 internal server error even on an error which is supposedly handled by the server in the first place.

01:34 Mehul Mohan: So I don't recommend using REST for your private APIs. For your public APIs, sure, because that is how most LLMs and clients understand. But if you want to have a robust private API, you can also go proprietary. When I say proprietary, I mean just designing the whole API from scratch in the first place. Now, to give you an example, to give you an opinionated example in this, let's say your endpoint is just /api. example.com/api, right? And every API works on a single endpoint, right? So either that, so all of this is POST request because you also want to send data. Or you can have like a scoped access. So /api/v1, then you have /api, /api/v2 and so on.

02:18 Mehul Mohan: This is something that might sound again nice on paper, that hey, you have different routes and different stuff, but I still don't recommend this. And the reason for this is because there is no possibility of batching in this, right? If you just have a single API endpoint, what you unlock is not only just a single API call, but in a lot of environments like frontend web development and in backend, it's also possible to batch certain API calls because user might do it very quickly. Like if user is loading a single page and you want three API calls being made to the server, instead of sending three separate calls, you can batch them together at a 50 millisecond interval, combine them, and send them, right? So this format, this is the one that allows you to batch, where there is no API name inside the URL itself. So that is why I would recommend to start with this first of all. Make it POST because you don't know when you want to send the data. GET requests gets a lot of messy as you scale up.

03:19 Mehul Mohan: Now, once your request is there, once your request has been sent to the backend, the very first thing is obviously the load balancer and WAF, which I'll skip because we have discussed this in past and this is also not the topic of the video. So you just configure this somehow, and then it finally reaches your API server or whatever your VM, your Lambda, whatever it is that you are running. Now, with your API server in place, the first thing, the very first thing it should be doing, if it's not being already done by your WAF or rate limiter or load balancer actually, is the rate limiting. And your rate limiting must be done in a special way. Ideally, what you should be doing is you should have an algorithm which checks if unauthorized, that means the user is not logged in, then you must rate limit on IP. And your application again, depending on the kind of application that you have, you should try to authorize people for sensitive actions, right, which are supposedly high rate limits. Because IP addresses are tricky. They are shared, there is NAT traversal, so you will have one IP which spawns through like hundreds or even thousands of potential users. Especially true for colleges, universities, for office-based people who are, you know, behind a single network. So rate limiting on IP is not really a good solution, but you don't have any other option if you don't know who the user is in the first place.

04:20 Mehul Mohan: If the user is authorized, on the other hand, if authorized, then you should rate limit on the account, account ID, right? Whatever ID they are signed in with, you should use that as one of the components in constructing the key of the rate limiter key. This should also consist of the API name, right? API name that the user is trying to access because, see, you don't want to rate limit the user completely from your backend if they have mistakenly done some refreshes on some specific page, right? So this is where, you know, this POST request that we are making, the body of this POST request contains a lot of information. One of the parameters should be API name, you know, "get user data," let's say something like that. You construct this rate limit key and you ask whatever, you ask your unlocked database table or you ask whatever your Redis, whatever your solution is for rate limiting, you ask that, then you move forward.

05:18 Mehul Mohan: The next thing, the most important thing that you do after this point, after you have validated, you know, that the rate limit is fine, is that you validate the data, validate the data strictly. And I think it can also happen before rate limiting if I'm not wrong. Yeah, I think it's supposed to happen a little bit before rate limiting because you also need to get the API name out of the body, right? In the first place. So this might also be a field which is there in the payload of your body which is getting requested. So I would assume that validate the data strictly is probably going to be before rate limiting. Let's just remove this connection. Let's just move this whole thing a little bit ahead. All right. So over here, before you actually do the rate limiting stuff, you actually need to validate your data, validate the POST body. It is so critically important that you get this right that I would say like most of the vulnerabilities that happen always are happening because of this missing step or this step being weak, not even like missing.

06:21 Mehul Mohan: So how do you validate the POST body in the first place? Well, this goes back to how do you create your API in the first place. What I would say is that you should create an API structure which looks like this. Let's say you have an API folder, whatever in your backend, and then you have "get user data" as one of the APIs. You know, then you have, let's say, "start login" as second API and, you know, you have like "register user" as third API and so on. Every single one of these APIs that you are creating is independently stored as separate files, right, as separate folders rather. And each one of them is supposedly having two files at least. The first one is some sort of handler, which is the actual code that gets executed, and the second one is some sort of constants or metadata file, right? Which includes all the information about how the function is supposed to behave in terms of rate limiting, in terms of validation and so on and so forth.

07:18 Mehul Mohan: So that is what actually you would also use. So this rate limiting that I'm talking about, the limits like how many requests per minute are allowed, you can define this on a per-API level, per-API basis inside this specific file that you say that, okay, I want only 60 requests per minute maximum or I want like 600 requests per minute. So that'll go inside this constants file, right? And the handler is supposed to just execute the code in the first place. So, one another thing that goes inside constants is the schema of the accepting POST body, right? So let's say you have this "start login" as one of the options, as one of the APIs, right? So over here you can have like input schema as one of the things that what you are expecting the user to pass in the first place.

08:04 Mehul Mohan: And if you're using something like TypeScript, I would recommend Zod as a library. Extremely good, extremely cool library. So over here you would define that the input schema is that you have to pass the email like this and you have to pass the password like this. You know, what this does is imagine for some reason that you don't have this and you're just doing JSON parse from body and you let's say have MongoDB as a database. Then somebody can just pass, you know, a database, a NoSQL injection sort of, where, you know, somebody just passes this syntax which is like a typical NoSQL injection which is possible.

08:38 Mehul Mohan: If you have Zod schema, it's basically just not possible to pass something like this as long as the schema is fine. And I would go like one more step ahead and I would say like you can even define like a password schema itself, which is like strict version of z.string where, you know, you can have like min of four, max of 100 or 50 whatever you have, and then you have like some regex or something that validates that the password is strong enough or not. So this is absolutely necessary, absolutely necessary to be done on an every single API level that you're creating. Do not skip this step. This would be a make or break step for you in your API for your backend to be potentially getting hacked one day.

09:21 Mehul Mohan: So once you have this done, obviously this constants.ts file will also have something like rate limit as a construct, let's say 60 per minute somehow you are able to define this. So depends on what sort of backend you have, but you have all these information, all these metadata in a separate file, right? Now again, this is framework agnostic. This could be Rust, this could be Go, this could be anything. Could be like TypeScript for all I care. But what matters here is that you have to have this construct. You have to have this flow of, you know, API endpoints and stuff available.

09:56 Mehul Mohan: Then once your request POST body is validated, you go ahead and check the rate limits. If the rate limits are right or not, you know, and if they are right, you just decide to move forward with all this stuff. As you move forward, you actually execute the handler code. Now over here, again, I would recommend that every single handler code is supposed to start with the authentication, right? So you have to authorize if the user is supposed to access that specific code or not. So every single handler that we have over here, this handler file which you have inside here, if I can give you an example of something like this, every single file should start with something like "require admin" or, you know, "await require user" or whatever, whatever your roles are, right?

10:48 Mehul Mohan: So these functions can be premade, these can be preconstructed depending on what you are. And Mehul Mohan says make it a habit that every single handler is supposed to have something as a first line of code: "require XYZ." And this function should be very well tested. It should be very well tested that it handles all the edge cases, it's extracting out the token. So in this specific case, like I mentioned over here, your header can have, you know, X-access-token or something, which is like a validation token. Or it can also have a cookie, which is like HTTP-only cookie if you have, if you have a local storage access token, you can pass it like this. This access token or this validation is what you are supposed to read when you are doing this stuff, right? When you are doing the handler execution and when you are extracting out the admin.

11:49 Mehul Mohan: Now you might say that, "Hey Mehul, this is fine, but you asked us to construct a rate limiting key based on the account ID. So if we don't do the authentication before that, then how are we supposed to have the account ID in the rate limiting key before we actually do the authentication?" And that is an extremely good question. And what I would suggest you for this is that your X-access-token itself should be ideally a JWT signed token, right? So once it's a signed token instead of just an arbitrary string, you don't have to do a database lookup for verifying if the user is legit or not. If your access token itself is JWT signed, let's say your signed token is just, you know, just the user ID 1 2 3 4 5, nothing, nothing special.

12:30 Mehul Mohan: So if you sign this token, you create a JWT out of it, what you can do is even without performing a database call, you can take out the authorized actual legit account ID, and nobody can even fake it, right? Because you are not just checking Base64 encoding, you're actually verifying if the JWT is valid or not. So you get the account ID for rate limited part, and when you actually need the user or you actually need the user instructor, admin, whatever, you do the actual decoding of the JWT, call the database, verify the session expiry, all of that beyond this you actually do the further code execution.

13:00 Mehul Mohan: And very, very fundamentally speaking, that's all you need. That is all you need to build an extremely high-robust, high-scalable, high-traffic API that knows its own functions, it knows what the rate limiting is, what the code to execute is, has a very strictly defined input schema. And I would say like go ahead and also make an output schema if you want. This is strictly for type safety, right? So output schema is something that your backend will return. It's strictly for type safety, it's not for enforcing anything because your backend is supposed to be trusted code, right? So it's not going to send anything which the client is not expected. But if you just return like status as, you know, something like OK or whatever, you can actually use this schema and copy the types on frontend by some type generator, use them to create like fully typed end-to-end API systems.

13:48 Mehul Mohan: And I'm not even talking about using some library or something. This could be literally something that you do within your company and it's not more than like a maybe like a few days of time, and I mean even a day's time these days if you know what you're doing with these cloud code setups and, you know, these AI systems. So this is an extremely robust, extremely cool way of building APIs, and this is how you should build APIs moving forward. There are a lot of interesting paths which happen here inside, you know, once the API has been built and here as well on the load balancer WAF side, which I'll be happy to discuss, but I want you to leave a comment on what do you like in this video and what would you want to see next. I would want you to like, hype this video, subscribe to the channel, share it with your friends so that I can create a lot more interesting content like this continuously. That's all for this one, and I will see you in the next video very soon.