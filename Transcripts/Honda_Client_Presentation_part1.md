---
title: Honda_Client_Presentation_part1
audio_file: Honda_Client_Presentation_part1.mp3
date_processed: '2025-12-12'
tags:
- '#AITemplateValidation'
- '#AgenticAI'
- '#LLMAccuracy'
- '#DataProcessing'
- '#Honda'
- '#Honda_Client_Presentation_part1'
domain: Artificial Intelligence
summary: The discussion centers on leveraging AI/LLMs to automate the validation of
  a large volume of diverse document templates (up to 700) and their associated data,
  a task challenging for traditional regression testing due to varied positional designs
  and fields. The proposed solution involves a Python orchestrator utilizing enterprise
  cloud LLMs to verify template formats, field names, and data accuracy. For scaling,
  achieving higher accuracy (near 100%), and handling complex scenarios like embedded
  formulas, an "agentic AI" multi-agent system is suggested.
key_ideas: []
note_id: 97cde416-0e74-4099-b03e-53170755414e
---
## Discussion Topics

- **Here are 5 key ideas or concepts discussed in the transcription:** 
- **AI for Template and Data Validation:** ** The core function of the AI is to validate the structure and positional setup of various document templates against expected data fields, ensuring correct data population.
- **Agentic AI for Scalability and Complexity:** ** An agentic AI system is proposed to scale the solution, allowing specialized agents to handle different levels of template complexity and specific rules, which also helps mitigate LLM hallucination.
- **Deployment Architecture and Data Privacy:** ** The system will utilize a Python orchestrator script hosted on-premise, extracting data to be sent to enterprise cloud LLMs (Azure or AWS), with discussions about safeguarding PII and options for local LLM hosting.
- **AI Accuracy and Hallucination:** ** The current accuracy for validation is estimated at 85-95% per letter, with strategies like fine-tuning prompts and implementing guardrails suggested to achieve 100% accuracy and prevent LLM hallucination.
- **Validation of Formulaic Data:** ** A specific challenge is how the AI will validate calculated fields or formulas within templates, as LLMs are generally poor at complex mathematical operations, suggesting a need for custom tools within an agentic system.



---
[ 0m0s644ms - Speaker 1 ] on per. letter, account, commutation right. And every row will basically has has to be compared in this approach to a unique PDF.
[ 0m14s274ms - Speaker 2 ] Correct. So, yes, uh I understand that. So, uh, when we are ingesting the CSV, see, this is just a proof of uh, not even a proof of concept, it's just a very high uh preliminary demo to show what AI can do, right? But the way the data is being processed and ingested and given to the uh LLM, that will depend on what file we have. As of now, we are not using any real data. We just created manually a sample CSV. So, we just made one line of data and we are processing it. But, uh I understand that the CSV is going to have like, uh, for example, 500 lines of data and correspondingly 500 uh templates are going to be there. So, this has to go as a uh for loop as in one line after the other and correspondingly pick the uh template from uh uh respective template from the data set and then compare these two together and give it out. So, uh, I'm just showing here the core uh AI processing part over here. The surrounding setup, that needs to be built around it depending on the real data what we can see.
[ 1m26s641ms - Speaker 3 ] Okay. Got it. Thank you.
[ 1m28s645ms - Speaker 2 ] Yeah. So the fine, uh finally this is how the data is going to be uh uh shown uh as a that also depends on what we want. As of now, I just put it as a template. I asked it to put it as a template, so it is showing that. Yes, Amit.
[ 1m45s684ms - Speaker 4 ] Uh quick question for Vishal. So Vishal, how what does the data look like? So the data is not really tied to the template, right? It's generally basically
[ 1m53s867ms - Speaker 5 ] It is. So, for the there's a relation to the template as well as to, right? So, this is a two-way approach. So, for each account number, we have a list of, I mean, for each letter ID, we have a bookmarks, then that bookmarks are tied uh Uh the letter ID is there. Yeah. So, letter ID based upon the letter ID. So, for example, here, right, what you're seeing, there would be a policy number bookmark or name address bookmark, city, state, zip bookmark, right? So, And then for that particular account number, uh we would give the data.
[ 2m26s638ms - Speaker 4 ] So, so, okay. Okay. So, the AI program has to look for that letter ID basically and and validate the the bookmarks and fields. Okay.
[ 2m28s329ms - Speaker 5 ] Uh, yes.
[ 2m35s341ms - Speaker 4 ] Yeah. So, uh uh a question uh
[ 2m39s417ms - Speaker 2 ] Sure.
[ 2m39s897ms - Speaker 4 ] for the team. So, we we are looking at this, I'm sure maybe you have this later on. Uh so, we're looking at validating the fields and the data. How about the uh we're also talking about the template. Does the template itself gets verified in the same way? Uh so, if the data because we are matching the expected fields, right? So, if if it's wrongly mapped, then I will the support cover that as well.
[ 2m56s187ms - Speaker 2 ] Yes. Exactly. So, uh the template format uh what you have, that uh the AI has the capability to uh validate that as well. So, that's where uh we we think AI is the uh better solution for this since 700 templates are going to have 700 different positional designs, right? To to put it in such a way. Uh if we have a uh very uh structured uh uh legacy type of creating the uh regression testing per se, 700 different things cannot be done uh again and again, right? That is where AI comes in. AI can understand the positional difference, positional uh setup of the template. The value can be in first line, the last line, in the middle of it, even in the uh some templates may have the va uh field values in the body of the letter, the AI will be able to figure that out. And semantically understand that, okay, this needs to be matching over there and uh give us a uh uh uh report accordingly.
[ 4m10s754ms - Speaker 4 ] Okay. So, I think one of the one of the examples I think Vishal you gave earlier was that if you are expecting F name, L name, right? And instead of that uh they put something else uh in the template by mistake. Uh
[ 4m23s803ms - Speaker 5 ] right.
[ 4m24s945ms - Speaker 4 ] Uh so, this how how does this uh program react to that? Uh So, let's say instead of first name, last name, they they put zip code for example, by mistake. In the template. Yes. The mapping mapping is wrong.
[ 4m30s300ms - Speaker 5 ] it would be the bookmark, right? So, the bookmark is wrong, right? So, in that case, you will not see any data being populated over there, whereas our expectation was that F name would be there at that particular bookmark.
[ 4m39s799ms - Speaker 4 ] Yeah, the bookmark is wrong. Or the wrong data gets populated and we compare it to the CSV value. Yeah, but uh but the field name itself is wrong.
[ 4m51s238ms - Speaker 2 ] Uh no, but the thing is, uh the CSV will have a title as well. Correct. Uh the column title.
[ 5m4s409ms - Speaker 5 ] Yeah, bookmark, right?
[ 5m5s679ms - Speaker 2 ] Yeah, bookmark, the field name, basically. So, uh the field, uh so it's not going to just look at the uh value of it. It needs to match it with the variable name, that is the field name as well. So, both need to be tied up. So, it Yeah, that makes sense. Yeah. So, because uh see, uh we are anyway giving uh the CSV file to it and the CSV file is going to contain the data of uh the variable name, that's the field name and the value inside that. So, it is just Yes, that's the that's the single source of truth. So, it is going to have both data in it. We can parse it uh according to that.
[ 5m19s109ms - Speaker 4 ] Yes. And the value. Yes. So, that's the source of truth, yeah.
[ 5m46s222ms - Speaker 3 ] But, but Vishal, uh I was based on what Amit said, I was just thinking if they make a mistake in positioning the bookmark, for example, you're populating the correct value. So, first name and last name, they are map to the bad value.
[ 5m55s232ms - Speaker 5 ] That that that would needs a human eye to make sure. For example, they they give the zip code in between the first name and middle name, right? Technically, it is correct. Yes. Uh but, you know, that is that is
[ 6m4s492ms - Speaker 3 ] Correct.
[ 6m17s335ms - Speaker 5 ] positionally. It's wrong.
[ 6m18s245ms - Speaker 3 ] positionally wrong.
[ 6m18s835ms - Speaker 5 ] That means, you know, we are also doing the UT over there, right?
[ 6m21s915ms - Speaker 3 ] Correct. Correct. I'm just trying to think what we will not be able to validate versus what we will, right? So, if they if they define the bookmark, they map it correctly, but it's defined in the wrong place. Yeah. I guess in that case, it's a visual comparison with existing letter will probably catch that, right?
[ 6m22s735ms - Speaker 5 ] Yeah.
[ 6m34s855ms - Speaker 2 ] Yes.
[ 6m42s205ms - Speaker 4 ] Yes, if we have a if we have a master,
[ 6m42s515ms - Speaker 2 ] Yeah, that's the point.
[ 6m44s35ms - Speaker 4 ] Yeah, we have if we have a master source of letters, right? Um, then they can be compared.
[ 6m47s485ms - Speaker 2 ] Correct.
[ 6m50s185ms - Speaker 2 ] Right. So, uh my my just my uh thought as an extension of what you're discussing right now. See, uh as of now, we are discussing everything as a uh JNAI uh solution, right? But, uh as I said, once the proof of concept is uh uh understood and we agree to it, when we scale it up, my suggestion is we uh can go in the agentic AI route, where we give all the context to it. The sample uh uh files what you have, uh if you have certain specific scenarios where uh we the the rules are going to be a little bit even more specific to it, those kind of contextual information can be provided and one separate agent can take care of that. So, we can have an orchestrator agentic system where depending on the complexity of the template, different agents can perform different uh sets of rules and operations. So, that's why I said when we are going to scale it up, uh we can go through the agentic AI root, multi-agentic system.
[ 7m59s206ms - Speaker 4 ] Can you give an example of how that works?
[ 8m1s636ms - Speaker 2 ] So, uh let's say, see, the one of my uh from my understanding, my experience, I've uh I've played around and built certain uh uh agentic AI systems. So, from my uh experience, right? This AI, uh LLM, whatever capability it is, it has its own drawbacks as well. It has its own challenges too. The more you keep on loading it, the more rules or the more step-by-step instructions you give, it starts to go uh hallucinate itself, right? Because in the core DNA, it has been trained to do certain things. Because of that, it starts to hallucinate. Now, when it comes to agentic AI system, we provide very specific instructions to certain certain agents. Let's say, uh the template or template is a little bit simple, like what we saw right now. There is an orchestrator, uh let me just go here. Okay. Okay. Let's say, we have a central uh orchestrator over here, okay? Now, this orchestrator will be the uh manager agent or the parent agent. Parent agent will first see what kind of a uh template complexity it is. It will decide whether it's going to be a very uh simplified template uh with simplified data. If that's the case, the rules are going to be a little different, the validations are going to be a little different. That can go to agent one. Okay. But, as you are saying, there are some one-off cases uh where the complexity is very very much different and the rules are going to be very very much specific. The parent agent is going to classify it and send it to agent C depending on the complexity, right? So, in this way, we don't give one agent to do or to perform everything. You have different complexity levels, depending on that, we split it among different teams.
[ 10m1s16ms - Speaker 4 ] Okay.
[ 10m3s696ms - Speaker 4 ] Yeah, I guess we'll know more if we see an example later on. But overall, conceptually, I do understand.
[ 10m5s136ms - Speaker 2 ] Right.
[ 10m11s291ms - Speaker 5 ] So for the POC, we do want to I don't want to use one record only. Right? I saw in the file. We need to do a loop, you know, so to go more than one, right? So we we confirmed that this person's going to work, right? And also, uh is this is stalled on what is this panel that you're sharing? Is it something home grown? Or are we expecting if you go with this solution, are we expecting it to install anywhere? Then Honda premises.
[ 10m17s491ms - Speaker 3 ] Yeah.
[ 10m44s114ms - Speaker 2 ] Uh okay, two things. One, uh the next slide was supposed to be that. Okay. Let's say, we build the system, right? Uh so, as of now, I understand that the data at the moment, the cache system, everything is an on-prem. The templates are in on-prem system, right? So, the uh the application what we are going to build, it will be a Python uh orchestrator script. This can be set up in your Honda's uh local environment, that is your on-prem uh system. And the model, I suppose, uh you you have an enterprise version of Azure and AWS Bedrock as well, which has its own suite of LLM models with different multimodal capabilities, right? So, the core data and the script, everything will be in your local uh on-prem environment. The uh AI will be your enterprise uh AI model. The data will be extracted and passed on to the uh uh Azure and or AWS based on what is available and then come back to it. So, everything will be hosted in your on-prem system. So, the core data remains there, only the extracted data gets sent out to uh the AI in uh in Azure or AWS Bedrock.
[ 10m49s394ms - Speaker 5 ] Okay.
[ 12m0s426ms - Speaker 5 ] So, that's to the cloud, right?
[ 12m1s600ms - Speaker 2 ] Yeah, that's to the cloud.
[ 12m4s787ms - Speaker 4 ] So, Vishal, we have PII in it, right? Yeah, we have, I mean, we have scrambled data in QA. So, we should be good.
[ 12m7s497ms - Speaker 5 ] Yeah, we have.
[ 12m13s267ms - Speaker 4 ] testing purpose, we're going to use QA, right? With Yeah, QA.
[ 12m13s687ms - Speaker 5 ] testing purpose, we're going to use QA, right? Yeah, QA.
[ 12m16s597ms - Speaker 4 ] QA. So, that is scrambled.
[ 12m17s337ms - Speaker 5 ] QA, QA. So, that is scrambled. The information is scrambled.
[ 12m20s327ms - Speaker 4 ] So, that's defined, right? Do we need to get compliance uh guidance on this uh just to get
[ 12m27s667ms - Speaker 5 ] We should we should get a guidance. Yeah. Yeah. Yeah.
[ 12m32s954ms - Speaker 4 ] Okay.
[ 12m33s274ms - Speaker 2 ] Sure. Right. So, that uh that was the initial uh uh demo, but uh going forward, as I said, everything is in on-prem, but you can have a cloud pipeline approach as well where if there is a possibility, this is just a possibility. I I understand that it's a uh financial data. So, uh and customer data as well, privacy may be a concern. So, depending on what uh uh your security rules are, we can have either in localized system, uh sending only to an LLM in cloud or we can move everything to cloud as well. Since uh if it's an enterprise uh uh setup what you uh have in Honda, right? And if even I will also suggest uh uh I haven't put it here, but just as a thought. If you are still uh there is a concern of data privacy of sending things to uh the server, uh there are certain models which you can host it on your local uh server too. So, that uh track also we can try it out.
[ 13m35s664ms - Speaker 4 ] Okay.
[ 13m41s476ms - Speaker 5 ] Uh so, do you have any Uh we have more slides, huh?
[ 13m45s386ms - Speaker 2 ] Yeah, no, this is the last one. Uh just the approach two approaches which is uh complexity levels and stuff like that. But more the core solutioning is uh where we saw this uh demo and the other stuff.
[ 13m58s306ms - Speaker 2 ] Yes, Amit.
[ 13m59s106ms - Speaker 5 ] Yeah. Can you go to to the last slide where you have accuracy?
[ 14m2s576ms - Speaker 4 ] Yeah, Rashi, I just wanted to point that out. So, Yeah, yeah. So, this is 80 to 90%, 85. So, there is still Aditya, there's still manual uh you know, validation would be needed in this case because we we have to go with a 100%.
[ 14m16s386ms - Speaker 2 ] Yes. So, uh what I will uh so, sorry. To cover that part, right? See this value what I have what we have added over here, it is uh more on the trial and error things what we have done with the existing data, right? But, uh if we need uh 100% accuracy, we need to a little bit fine tune the prompting what we are going to provide and put proper guard rails so that the LLM doesn't hallucinate much. There are uh specific pipelines which are there to guard these things to make the accuracy uh very high. Uh specifically, for example, in uh uh this may be a separate top uh uh sideline topic, but uh if you go go and check uh Salesforce's uh uh agentic system, it has specific uh uh pipeline, since it's going to handle all the CRM data, customer data, it has pipeline to have have the security in place, but also to avoid almost 0% of hallucination as well. So, there are systems for that, which we can put in place once we are going to scale it up.
[ 14m52s896ms - Speaker 4 ] Okay. So, there were there were two more parts of the testing, right? I think we we briefly touched one where we said that that we gave the example that the first name, last name ended ended up putting a wrong field like in zip code. So, so you said that when we go with the agentic AI that that might be able to solve that. So, that's one thing. And the other other thing, I think uh Vishal you had mentioned and maybe Aditya you also that there is some formula in there. Uh and sometimes uh that is that is set up as wrong. So, I'm curious how how would we deal with that?
[ 15m25s606ms - Speaker 2 ] Again,
[ 15m57s326ms - Speaker 4 ] And then Vishal, can you give me an example, please, of how the formula would be wrong. Like is it like a field wrong or something or Aditya sorry.
[ 16m2s586ms - Speaker 5 ] Aditya, I'm just opening up your letter example which Aditya had given me. So yeah, it's taking two values and doing a calculation uh on it to populate a bookmark. Now, those two values could be other two bookmarks or values from the same letter or some other Okay. Yeah, in that yeah, in that case, right? The formula is inside the template, Aditya. Mostly. Inside the right, there's a there's an addiction. Bookmark plus one plus bookmark two, right? They would be having that calculation setup here.
[ 16m6s446ms - Speaker 3 ] Uh.
[ 16m25s396ms - Speaker 4 ] Okay. So, in that CSV output that you give Vishal for that this letter for a test account will for that It will not have, okay. So, we will not that bookmark, it will not output in the CSV.
[ 16m39s596ms - Speaker 5 ] It will not have.
[ 16m56s186ms - Speaker 5 ] The bookmark name in sometime what happens is they just give like a a generic bookmark. Oh, because you have we have OBJD ID or or sometimes what they have is they give a like a generic bookmark name which is not there in their database, but in the formula, they will give the actual bookmark name. So there.
[ 17m1s526ms - Speaker 4 ] Oh, because you have.
[ 17m12s866ms - Speaker 4 ] So, so if the formula is value A, over value B and some percentage. So, I think I think if we look at the three cases that we looked at where one is verifying the template and by verifying we mean that the right bookmark is at the right place and we look at the third option, third uh thing that we want to verify, which is the formula. They're the same thing basically. So, So, what you're saying is that the right bookmark should exist at the right place.
[ 17m18s606ms - Speaker 5 ] Yeah.
[ 17m40s416ms - Speaker 4 ] I think I think I think that will solve the issue, right?
[ 17m40s466ms - Speaker 5 ] I think I think that will solve the issue.
[ 17m43s376ms - Speaker 5 ] If if if AI can tell, you know, that if data is wrong, then a human can go and verify it. Right? I don't think so, it's that many templates which have, you know, those formulas, it might be just five, 10 templates which have those formulas. But if AI can pinpoint that this is uh this is a discrepancy, then a human can go and and verify, you know, yes, this is an acceptable that
[ 17m43s566ms - Speaker 2 ] Uh,
[ 17m55s906ms - Speaker 3 ] So, what's the I I'm just trying, I think like for me, it will be a little bit better to understand once I have a look at the CSV that we will get just to visualize, right? What what that fields will look at.
[ 18m7s166ms - Speaker 2 ] Understand. Understand.
[ 18m18s836ms - Speaker 5 ] I'm going to run it right now for couple of table that I can have a meeting with you later, Aditya to share.
[ 18m25s606ms - Speaker 2 ] Sure.
[ 18m26s646ms - Speaker 3 ] Yeah, so I'm still trying to think in this case what the CSV output will have because the bookmark is part of the letter, but it is not directly mapped to a value, right? So, it will still output the bookmark, but it will be null or something like that or?
[ 18m36s226ms - Speaker 5 ] We have we have a lot of calculated bookmark, right? What you mentioned over there. They were they are not exactly in our database because they're only inside the template. Right. Okay. So, the value is based the value is based upon other fields which are coming through.
[ 18m51s366ms - Speaker 3 ] Right. Okay. Okay. So, the test will not even fail. It's just something that will not be tested, right? Because the CSV will not necessarily output that.
[ 19m4s6ms - Speaker 5 ] Yeah. Yeah. I can I can Give me the letter you had, right? I'll that is the letter ID, right? Which you gave me, I can run uh uh data for that. Okay. Yeah, you that will be a good example, I think. That letter has combinations of different things. So, Okay. Got it.
[ 19m6s726ms - Speaker 3 ] Yeah, you try.
[ 19m23s220ms - Speaker 5 ] Can also going back to the accuracy. When you say 80 85% or whatever the numbers are, is it uh you know, is it on the total volume of the letter or within the letter? So, for example, if I say here's the letter, right? It's So, the on accuracy is for a letter or Volume of the letter.
[ 19m37s280ms - Speaker 2 ] It is So, as of now, Correct. Uh what we are saying it as for the letter because uh as of now, we haven't tested it for 700 uh templates. We are just doing one uh letter or one uh
[ 19m51s610ms - Speaker 5 ] Oh, so this accuracy is within one letter, right? So, bookmarks are right, template.
[ 19m53s860ms - Speaker 2 ] Yeah. So, I think it is uh we have we judicially sorry, uh cautiously we have put it as 85 to 95, but uh we see it is a little more than that uh most of the time.
[ 20m8s510ms - Speaker 5 ] Do you also know the industry standards on this one? So, if you happen to know.
[ 20m13s920ms - Speaker 2 ] Uh with respect to or for these kind of testing or with respect to industry standards, right? What I generally uh uh read about is, it also depends on the which LLM model we are picking up, right? Uh so, what is available as well. If it is if we pick up a model which has a very good uh multimodal capability with reasoning uh capability, it's going to be uh uh the accuracy is going to be very, very, very good. But if you're going to go with a lighter model like uh uh for example, flash uh models of uh Google, uh they are faster, but the accuracy is going to come down. So, depending on uh what we have and what we are going to select, the accuracy is going to go up and down accordingly to that.
[ 20m16s380ms - Speaker 5 ] For this kind of for testing or or
[ 21m4s410ms - Speaker 5 ] Okay. And for this purpose, you use AWS Bedrock.
[ 21m7s690ms - Speaker 2 ] Uh no, the demo what I'm showing now, that is using uh Gemini's uh flash model, 2.5 flash model because that's that's the one which was available to us. So, we tested it over there. But uh what what whatever is available to you, we can work on it and see how to integrate those things.
[ 21m29s646ms - Speaker 5 ] So, can we check on that Amit? So, what do you suggest if we go with Azure?
[ 21m34s746ms - Speaker 2 ] Yeah, so
[ 21m35s396ms - Speaker 5 ] Or AWS, what's the highest accuracy.
[ 21m36s856ms - Speaker 2 ] I I digged up a little bit. I think AWS Bedrock has uh Anthropic's uh 4.0 model available, which is going to be a very a little bit expensive model, but uh the accuracy is top notch over there. Similarly in Azure side, uh anything above 4O uh or 5 is going to be very good. Uh anything in 4O mini or something, the accuracy is going to go down.
[ 22m21s627ms - Speaker 5 ] So, uh we have to check internally what's the Honda approach, right? Uh what's the Honda approach.
[ 22m27s667ms - Speaker 2 ] Right. Uh just a thought, sorry. Uh regarding the uh the the formula one which you uh use case you are talking about, right? Uh that's also why I wanted the agentic system to come in play. The reason is, there may be uh since it's going to be a financial that even before this meeting, that was my assumption. Since it's going to be a financial system, there are going to be some calculations and mathematical things uh getting involved. Uh LLMs are very, very bad at that. They they they they they can mimic uh that they're going to do some calculations right, but they're they're very bad at it. That's where uh an agentic system again comes into picture where we build a custom tool, that is a custom Python program for these kind of use cases and we give it to the agent. So, if the as I said, uh the the parent agent is going to route to the specific agent if depending on the complexity, that particular child agent is going to have this tool in hand. If you have a specific formula to be evaluated, it will use that particular Python function to uh basically validate that part as well. So, we can uh work on that and see how to develop that segment. But the I uh the the the architecture uh is uh there is a possibility in that architecture for that.
[ 23m47s329ms - Speaker 5 ] So for POC, what are you planning to use?
[ 23m49s569ms - Speaker 2 ] Uh for POC, as I said, uh the the JNAI is what we are we were uh pitching. Since it's going to be fast, uh we can prove with as much uh at least for 100 to 100 and uh 200 or even 500 templates, we will be able to prove it uh depending on uh assuming the complexity is not very high. For the very niche use cases or uh like uh from 500 to 700, let's say, those things can be done later.
[ 24m18s969ms - Speaker 5 ] But do you know the record, what do you see, what do you what's your opinion about is it complex?
[ 24m25s269ms - Speaker 2 ] Uh it will take little uh longer time. That's the only agentic system will take a little longer than a JNAI solution. Uh I understand uh I mean I had an understanding that this uh POC has a timeline of another week or so, uh probably a week or 10 days. Uh for that kind of a time line, JNAI POC for handling uh 400 to 500 template types is possible. But building a agentic AI system with all the other surrounding things, that will take uh