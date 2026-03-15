---
title: Slidebean_The Biggest Mistake in the History of Hollywood_20260220_part1
audio_file: Slidebean_The Biggest Mistake in the History of Hollywood_20260220_part1.mp3
note_id: 802d3134-f11a-486e-9c05-c677e06668eb
date_processed: '2026-03-01'
classification:
  primary_domain: Film and Video Production
  sub_domains:
  - Digital Cinematography
  - Film Restoration
  - Video Streaming
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people:
  - name: Speaker 1
    role: Narrator
    contribution: Explains the history of film and video production
  - name: Speaker 2
    role: Actor
    contribution: Quotes a line from a movie
  - name: Speaker 3
    role: Color Grading Specialist
    contribution: Explains the color grading process
  - name: Speaker 4
    role: Actor
    contribution: Quotes a line from The Lord of the Rings
  works_cited:
  - title: Blade Runner 2049
    author: Denis Villeneuve
    year: 2017
  - title: O Brother, Where Art Thou?
    author: Joel Coen
    year: 2000
  - title: The Lord of the Rings
    author: Peter Jackson
    year: 2001
  concepts_mentioned:
  - Film Production
  - Digital Intermediate
  - 4K Resolution
  - Color Banding
  - Upscaling
  laws_theories_cited: []
concepts:
- name: Digital Intermediate
  definition: A digital master copy of a film used for editing and color grading
  parent_concepts:
  - Film Production
  related_concepts:
  - Color Grading
  - Film Restoration
  abstraction_level: Theoretical
  confidence: 0.9
- name: 4K Resolution
  definition: A high-resolution video format with a horizontal resolution of 3840
    or 4096 pixels
  parent_concepts:
  - Video Production
  related_concepts:
  - Digital Intermediate
  - Upscaling
  abstraction_level: Fundamental
  confidence: 0.9
- name: Color Banding
  definition: A visual artifact that occurs when a digital image has insufficient
    color depth
  parent_concepts:
  - Digital Imaging
  related_concepts:
  - Color Grading
  - Digital Intermediate
  abstraction_level: Practical
  confidence: 0.9
- name: Upscaling
  definition: The process of increasing the resolution of a digital image or video
  parent_concepts:
  - Digital Imaging
  related_concepts:
  - 4K Resolution
  - Digital Intermediate
  abstraction_level: Applied
  confidence: 0.9
- name: Film Restoration
  definition: The process of preserving and restoring old films to their original
    quality
  parent_concepts:
  - Film Production
  related_concepts:
  - Digital Intermediate
  - Color Grading
  abstraction_level: Theoretical
  confidence: 0.9
relationships:
- source_concept: Digital Intermediate
  target_concept: 4K Resolution
  relationship_type: contradicts
  strength: 0.8
  evidence: Many films have a 2K digital intermediate master, which cannot be converted
    to true 4K
  reasoning: The digital intermediate master is the final master copy of a film, and
    its resolution determines the maximum resolution of the final product
- source_concept: Upscaling
  target_concept: 4K Resolution
  relationship_type: supports
  strength: 0.7
  evidence: Some films are upscaled to 4K from a lower resolution
  reasoning: Upscaling can increase the resolution of a digital image or video, but
    it may not always result in a true 4K image
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: Film and Video Production
  source_concept: Digital Intermediate
  target_domain: Audio Production
  target_concept: Mastering
  insight: Both involve refining and enhancing the quality of a digital product
  explanation: The process of creating a digital intermediate in film and video production
    is analogous to the mastering process in audio production. Both involve taking
    a finished product and refining it to ensure the highest possible quality for
    distribution. This step is crucial for optimizing the final product for various
    platforms and formats.
  potential_applications:
  - Improving audio-visual synchrony
  - Enhancing overall production quality
  confidence: 0.9
  historical_example: The development of digital audio workstations (DAWs) and non-linear
    editing systems (NLEs) has bridged the gap between audio and video post-production
- connection_type: principle_application
  source_domain: Film and Video Production
  source_concept: Upscaling
  target_domain: Computer Vision
  target_concept: Super Resolution
  insight: Both apply algorithms to enhance the resolution of images or videos
  explanation: The principle behind upscaling in film and video production—using algorithms
    to increase the resolution of footage—is directly applicable to the field of computer
    vision, particularly in super resolution techniques. These techniques aim to enhance
    the resolution of images or videos using deep learning models or other algorithms.
  potential_applications:
  - Enhancing surveillance footage
  - Improving medical imaging
  confidence: 0.85
  historical_example: The use of deep learning for super resolution tasks has its
    roots in the early 2010s, mirroring advancements in upscaling technologies for
    film restoration
- connection_type: metaphor
  source_domain: Film and Video Production
  source_concept: Color Banding
  target_domain: Data Visualization
  target_concept: Gradient Mapping
  insight: Both deal with the representation of gradients and the potential for artifacts
  explanation: The concept of color banding in film and video production, where gradients
    appear as distinct bands rather than smooth transitions, can be metaphorically
    applied to data visualization. Here, the challenge of representing continuous
    data as discrete gradients without introducing artifacts is akin to mitigating
    color banding in video.
  potential_applications:
  - Improving the readability of data visualizations
  - Enhancing the aesthetic quality of graphical representations
  confidence: 0.8
  historical_example: The early days of computer graphics saw similar challenges in
    both domains, with solutions often crossing over between film, video, and data
    visualization
- connection_type: historical_precedent
  source_domain: Film and Video Production
  source_concept: Film Restoration
  target_domain: Digital Archiving
  target_concept: Data Preservation
  insight: Both involve the preservation and restoration of valuable content for future
    generations
  explanation: The historical precedent of film restoration, which involves preserving
    and restoring classic films to their original quality, has direct parallels with
    digital archiving and data preservation. Both fields face challenges related to
    the degradation of storage media, format obsolescence, and the need for continuous
    migration to new formats.
  potential_applications:
  - Developing sustainable digital preservation strategies
  - Improving methods for restoring damaged or degraded digital content
  confidence: 0.9
  historical_example: The establishment of film archives and restoration programs
    in the mid-20th century laid groundwork for modern digital preservation efforts
bridge_concepts:
- concept: Signal Processing
  appears_in_domains:
  - Film and Video Production
  - Audio Production
  - Telecommunications
  role: Signal processing is fundamental to enhancing, restoring, and transmitting
    signals across various domains
  examples:
  - Noise reduction in film
  - Echo cancellation in telephony
  - Equalization in music
mental_models:
- name: Systems Thinking
  description: Analyzing complex systems by understanding the relationships and interactions
    within the system
  applied_to:
  - Understanding the post-production workflow as a complex system
  transferable_to:
  - Project management in software development
  - Ecosystem analysis in environmental science
analogies_used:
- source_domain: Music
  source_concept: Mastering a track
  target_domain: Film and Video Production
  target_concept: Color grading and finalizing a video
  mapping:
    Track: Video
    Equalization: Color Correction
  pedagogical_value: Helps in understanding the concept of preparing a final product
    for distribution by adjusting its properties to maximize quality and compatibility
    across different platforms
tags:
  hierarchical:
  - '#FilmProduction → #DigitalCinematography → #4KResolution'
  topical:
  - '#FilmRestoration'
  - '#ColorGrading'
  - '#DigitalIntermediate'
  methodological:
  - '#Explainer'
  people:
  - '#Speaker1'
  concepts:
  - '#DigitalIntermediate'
  - '#4KResolution'
  temporal:
  - '#2000s'
  - '#2010s'
summary: 'Here is a 2-3 sentence summary of the main points:


  The speaker discusses the concept of "fake 4K" in movies, where films are mastered
  in 2K resolution but upscaled to 4K for marketing purposes, resulting in no noticeable
  difference in quality. Many movies, including big-budget productions, have been
  mastered in 2K and then upscaled to 4K, with some even using AI to upscale the resolution,
  which can lead to compression and loss of color detail. The speaker argues that
  the emphasis on 4K resolution has been driven by marketing and profit, rather than
  a genuine desire to improve picture quality, and that true film enthusiasts should
  focus on other factors such as color grading and compression to achieve the best
  possible viewing experience.'
key_ideas:
- idea: Here are the 3-5 key ideas discussed in the transcription text with a short
    description of each
  description: ''
- idea: The myth of 4K resolution**
  description: Many movies advertised as 4K are actually upscaled from 2K digital
    intermediates, and the difference between 2K and 4K is often not noticeable to
    the human eye, especially at typical viewing distances.
- idea: The limitations of digital movie distribution**
  description: The process of scanning, editing, and distributing movies digitally
    can result in a loss of color and detail, and streaming services often prioritize
    resolution over color accuracy, leading to a suboptimal viewing experience.
- idea: The importance of color gamut and HDR**
  description: To get the best possible picture quality, it's essential to have a
    TV that supports modern color standards like HDR and Rec. 2020, which can display
    a wider range of colors, but even then, the distribution version of the film may
    not have the necessary color data to take full advantage of these capabilities.
- idea: The cheat code for achieving a film-like look**
  description: Some cinematographers use a process of shooting digital, editing digital,
    and then printing and scanning the film to create a digital intermediate that
    captures some of the texture and feel of film, and viewers can try to replicate
    this experience at home by using the right equipment and settings.
- idea: The marketing of 4K and its impact on consumer choice**
  description: The marketing of 4K as a premium feature has driven consumer demand
    and pricing, but it may not always deliver a noticeably better viewing experience,
    and consumers should be aware of the limitations and trade-offs involved in digital
    movie distribution.
---
## Key Concepts

**Digital Intermediate**  
A digital master copy of a film used for editing and color grading

**4K Resolution**  
A high-resolution video format with a horizontal resolution of 3840 or 4096 pixels

**Color Banding**  
A visual artifact that occurs when a digital image has insufficient color depth

**Upscaling**  
The process of increasing the resolution of a digital image or video

**Film Restoration**  
The process of preserving and restoring old films to their original quality

## Cross-Domain Connections

**Film and Video Production → Audio Production**

*Both involve refining and enhancing the quality of a digital product*

The process of creating a digital intermediate in film and video production is analogous to the mastering process in audio production. Both involve taking a finished product and refining it to ensure the highest possible quality for distribution. This step is crucial for optimizing the final product for various platforms and formats.

**Film and Video Production → Computer Vision**

*Both apply algorithms to enhance the resolution of images or videos*

The principle behind upscaling in film and video production—using algorithms to increase the resolution of footage—is directly applicable to the field of computer vision, particularly in super resolution techniques. These techniques aim to enhance the resolution of images or videos using deep learning models or other algorithms.

**Film and Video Production → Data Visualization**

*Both deal with the representation of gradients and the potential for artifacts*

The concept of color banding in film and video production, where gradients appear as distinct bands rather than smooth transitions, can be metaphorically applied to data visualization. Here, the challenge of representing continuous data as discrete gradients without introducing artifacts is akin to mitigating color banding in video.

## Discussion Topics

- **Here are the 3-5 key ideas discussed in the transcription text with a short description of each:** 
- **The myth of 4K resolution**:** Many movies advertised as 4K are actually upscaled from 2K digital intermediates, and the difference between 2K and 4K is often not noticeable to the human eye, especially at typical viewing distances.
- **The limitations of digital movie distribution**:** The process of scanning, editing, and distributing movies digitally can result in a loss of color and detail, and streaming services often prioritize resolution over color accuracy, leading to a suboptimal viewing experience.
- **The importance of color gamut and HDR**:** To get the best possible picture quality, it's essential to have a TV that supports modern color standards like HDR and Rec. 2020, which can display a wider range of colors, but even then, the distribution version of the film may not have the necessary color data to take full advantage of these capabilities.
- **The cheat code for achieving a film-like look**:** Some cinematographers use a process of shooting digital, editing digital, and then printing and scanning the film to create a digital intermediate that captures some of the texture and feel of film, and viewers can try to replicate this experience at home by using the right equipment and settings.
- **The marketing of 4K and its impact on consumer choice**:** The marketing of 4K as a premium feature has driven consumer demand and pricing, but it may not always deliver a noticeably better viewing experience, and consumers should be aware of the limitations and trade-offs involved in digital movie distribution.

## Full Transcription



**00:00 - 00:30 Speaker 1:** I sat down the other day for my annual rewatch of Blade Runner 2049, and I noticed this. Is this… is this pixelated? Is this color banding? I checked my internet connection, I checked my TV settings, I checked my HDMI cable. It was still there. So, here’s the Netflix version: still there. And here’s the Apple version; this is where I even owned the damn movie: still there. There has to be a version of this film that doesn’t have the color banding, right? I pay extra money for my 4K Netflix plan; like, there has to be a way. Where is it?

**00:30 - 01:21 Speaker 1:** So, over the last few weeks, I went down this streaming and movie watching rabbit hole, which I don’t mind at all, honestly. But I wanted to uncover some deep conspiracy and I wanted to blame Netflix for it. But I ended up mixed in this heated war of formats and disks and streaming services and the ultimate answer is even simpler; like, 99% of the time, 4K is a lie. But for those of you who are willing to chase that other 1%, that 1% of perfect movie projection, man, there are some incredible hidden gems out there if you know where to look. So, let me drag you into this rabbit hole with me.

**01:21 - 01:51 Speaker 1:** So, before we look at 4K movies, we need to understand where that image came from because for years, for decades, films were film. A movie would get shot on good old 35-millimeter film, and the movie that you saw in the theater was just an edited copy of that film. It was never turned into pixels. And of course, I know what you’re thinking: old films, right? Classics?

**01:51 - 01:59 Speaker 2:** All right, Mr. DeMille, I’m ready for my close-up.

**01:59 - 02:29 Speaker 1:** This guy in a black and white world cutting strips of film. Well, let me tell you, this was the process for 99% of the films that released in the 90s. And the 90s were just what, like, 15 years ago? Every movie from our millennial childhoods was cut by hand. And to do that cutting from that original, priceless negative that came out of the actual camera that was used to shoot the movie, the studio would make a copy. Now that copy was called the workprint, and that’s what editors would cut. Physically cut.

**02:29 - 02:59 Speaker 1:** Your favorite 90s film was just a Frankenstein cut of pieces of film, all done on this workprint copy using a machine like this. When the director finally approved the edit, the most pro, the master boss, the sigma job here, the negative cutter, they’d go back to the original negative and cut it to match the workprint cut. So, this workprint was really just a temporary file, a disposable version to avoid damaging that precious original negative. 

**02:59 - 03:22 Speaker 1:** And then a color grading lab—not a computer, not Photoshop, not DaVinci—they would grade the film using real filters and different film stock and chemicals.

**03:00 - 03:11 Speaker 3:** You make this scene a little yellower, a little bluer, a little redder. You have certain, you know, controls and overall kind of feel of the film, warm or cool, or a little bit of this, a little bit of that.

**03:22 - 03:53 Speaker 1:** Then this finalized copy would be duplicated thousands of times and it’d get sent to movie theaters for you to watch and chug on that popcorn. Now those copies, there were reels of film, they were sent in a can, and they were projected in the theater. With film projection in movie theaters, if you wanted that top 1% premium experience, it really mattered that you went to see the film early. Because after a few weeks, the 35-millimeter film would start to get damaged and scratched.

**03:53 - 04:18 Speaker 1:** But what is the resolution of that film? Is it 4K? Is it more? Well, resolution and pixels, they didn’t matter back then. Like, I don’t think people knew what a pixel was. Like, these guys, they were working from film to film. There is no 4K conversion here, there’s just chemistry in film stock capturing an image and then more chemistry in the copy.

**04:18 - 05:08 Speaker 1:** Now obviously, editing like this is very artsy, but it’s terribly slow and even a little dangerous. So, they took almost a hundred years of filmmaking to come up with a better solution. Arguably, a better solution. But we’ll get there. In the 90s, the industry got digital editing tools, but they’re not what you think. What tools like Avid or Lightworks did was replace the workprint, not the final edit. The original negative would get scanned into the computer so that’d be easy to edit digitally. But that scan was 320 by 240, like that’s all these early computers could deal with. The first film cut using Avid was Let’s Kill All the Lawyers, and I… I looked in the darkest parts of the internet and I could not find that film for the life of me. But what I can guarantee you is that when this movie was released in movie theaters, it didn’t look like 320 by 240.

**05:08 - 05:43 Speaker 1:** 320 by 240 is shit, even for 90s standards. But it’s the beginning of the end for film quality. It’s the start of our fake 4K. Now back in the 90s, that low-res scan of the film was really just a like a proxy, a preview. It was never intended to be used for the final film. Like, Avid would export a cutlist, a little receipt that went back to that holy man, the negative cutter, that’d just follow those specs to cut the negative by hand and go through the same process that had been used for decades.

**05:43 - 06:40 Speaker 1:** Now we’re still working from film to film, so pixels in that Avid copy of the movie, it doesn’t really matter. But fast forward to the 2000s, and this is where the cheating begins. By the 2000s, technology had come to this point where we could actually get 2K resolution scans of that 35-millimeter film. 2000 pixels. And so, the Coen Brothers and Roger Deakins, the cinematographer, made one radical change that would transform movies forever. Now they wanted to give this film this sepia, sort of old faded postcard sort of look, and it’s a look that it was really hard, almost impossible to accomplish using the old-school grading process at the lab. So, what they did is they scanned the negatives of the production using a Philips Spirit DataCine. It’s a device that could scan the original film in that 2000-pixel resolution. And then they color-graded that digital movie file in the computer.

**06:40 - 07:11 Speaker 1:** And so, they exported that computer-graded movie back to film. That was done using a Kodak Lightning film recorder that kind of converts digital files into film, sort of like a printer, I guess. Now that printed copy would then be duplicated thousands of times and sent to all movie theaters around the world. But there is a huge problem with that process. Did you catch it?

**07:11 - 07:49 Speaker 1:** The point of this whole story so far is that because of this decision, there is no 4K version of O Brother, Where Art Thou? anywhere, ever. It’s impossible to get one; it’s gone. When that negative was scanned into digital, it was scanned at a width of 2048 pixels. And because this film is widescreen, the actual resolution of the movie might have been something like 2048 by 850. And that’s it; that’s the master file for this film. There’s nothing else to it. The original negative, if it still exists, maybe has that detail, but you’d need to basically scan, edit, grade the movie again to be able to make it 4K, not to mention having to deal with the damage of that 26-year-old negative.

**07:49 - 08:31 Speaker 1:** The movie that we got was shot on celluloid, yes, but then it was converted to pixels and even if you convert it back to celluloid, you’re always going to be limited by the pixels in that original scan. You’ve lost all that extra detail forever. How many movies do you think suffer from this? How many movies do you think are tricking you with this fake 4K? Just wait for it. Now this master file is actually called a digital intermediate, a DI. And after O Brother, Where Art Thou?, 2K DIs started to become a standard, and for the most part, this meant the end of negative cutters.

**08:31 - 09:11 Speaker 1:** Now with the rise of digital projectors around the mid-2000s, it also meant that a lot of movie theaters also switched from film rolls to just projecting a digital copy of that master. No more scratchy, jittery film, but a digital copy instead. But 2K, 2K is not the 4K that I’m paying for. Like, any film with a 2K digital intermediate master could never be converted into 4K, right? So, which films were limited by this? I’ve been going through a list of my favorite movies, like some of these are big-budget Hollywood productions, like some of the biggest movies of the last couple decades. Some of these were released on IMAX, and they’re all 2K masters. Like, all… at least all of these.

**09:11 - 11:32 Speaker 1:** So why are they showing up as 4K films in my streaming services? Is this the explanation for the color banding? Now Netflix, Netflix knows exactly where to put that 4K logo so that it appeals to the nerds like me, and they have piles of data to prove it and to test it. But regular UI designers don’t. But now they have Figma Make. Figma Make lets you prototype dozens of versions of your product not in days, not in hours, but in minutes. You can iterate on proposals by just chatting or even submitting reference images of what you like. And these are not static; these are clickable prototypes that have data and interconnections. Figma Make integrates with your existing design system libraries so that you can get credible on-brand mocks. You can also connect Figma Make to Figma Sites to customize a website or test interaction and just publish. Or you can even connect it to Superbase and turn your idea into a web app that is ready to ship. It doesn’t replace the role of the designers or the product managers; it just empowers them to move a lot faster. You can get free access to Figma Make along with AI credits by using the link in the description or just snatching this QR code over here. And of course, you also support our channel and our videos in the process. Okay, so let me get back to that list of fake 4K.

**11:32 - 12:46 Speaker 1:** Now there are a couple of tiny exceptions on this list and I’m going to get to those, but the truth is that most of these films have just taken the 2K digital intermediate master and upscaled it to 4K. Sometimes using some really bad AI, and sometimes just lying to you about it. One of the most extreme cases is The Lord of the Rings. 

**12:40 Speaker 4:** Is it secret? Is it safe?

**12:46 - 13:32 Speaker 1:** From around the 2000s as well, shot on film but mastered on a 2K intermediate, which then they used for the theater versions, the DVDs, the extended versions, the Blu-rays, and the streaming version. But how do they go from 2K to 4K? What they’ve said is they’ve gone to all the original camera negatives of the live action stuff, and they’ve gone to all of that original film-out, that film-printed VFX shots. That was not true. Lord of the Rings nerds, at least more nerds than I am, compared the old Blu-ray releases with the new 4K releases, and they found that they were the same film; they just stretched out the 2K intermediate image, messed up the colors in the process, which is a story for another day, and they slapped a 4K sign on the box and on my streaming service.

**13:32 - 14:30 Speaker 1:** And this goes into the 2010s as well. Prometheus, The Social Network, Mad Max; like, I remember I distinctly remember paying top dollar to watch Mad Max on IMAX. And now you’re telling me that it was just an upscaled 2K film that pretended to be an IMAX? Why would they do that? I wasn’t even close to the end of this rabbit hole. There is some debate on this, but the general consensus is that if you scan a 35-millimeter film into digital and you store that image at a resolution of 4K, you’ve captured all the detail in that 35-millimeter negative. Now some people will argue that there is more detail in there, that there’s detail enough for like a 6K scan from a 35-millimeter negative, but honestly, ah, not really.

**14:30 - 15:44 Speaker 1:** Now the first movie to scan film in 4K was Spider-Man 2. They scanned all the negatives in 4K and they mastered the film in 4K. That means the DI was 4K, which I’m sure crippled all those 2004 computers. Funny enough, not the special effects. Rendering those tentacles at 4K would have been impossible with 2004 computers, not to mention crazy expensive. It’s still crazy expensive today to render in 4K. So, the animation in Spider-Man 2 is actually 2K resolution renders placed on top of that 4K footage. But anyway, aside from this being you know a good nerd curiosity, did you notice that difference between the 4K footage and the 2K render? That is the catch. Despite everything you’ve been told, despite all the money that you’ve already spent on that 4K TV, do you even need 4K? Mad Max looked pretty great at 2K. So, is 4K even useful?

**15:44 - 16:40 Speaker 1:** Well, most of the time, it’s not. Now let me explain why. Here in my living room, the distance between my couch and my TV is 2.8 meters or 9.3 feet. That 75-inch TV takes about 33 degrees in my field of view when I’m sitting over there. And if I place my living room on this chart, I would land somewhere like here. Now that means that at this distance, my eyes should be able to tell the difference in pixels between 1080p and 4K. Now if I had a slightly smaller TV or if my couch was a little bit further away, 4K would not make any difference; it would be just as good as 2K. I’m going to link some materials on this below if you’re interested in testing your living room distances.

**16:40 - 17:38 Speaker 1:** And the same problem happens in a movie theater. Most seats in a movie theater fall within this 1080p region of the chart. It’s a huge screen, but the distance is much larger. And unless you’re sitting way up front, which comes with its own set of problems, 4K versus 2K will not make a difference. That is the reason why most movies, even today, are mastered in 2K. In 99% of cases, it’s not worth the effort or the extra equipment costs. So why did we get 4K shoved down our throats? Why was it sold to us as this golden standard in the movie experience? A big reason 4K is in our mind is because it’s easier to market.

**17:38 - 18:55 Speaker 1:** In the mid-2010s, when 4K TVs were entering the mainstream, it was very easy to just go out and market four times the pixels versus that crappy 1080p TV you used to have. It was easy to get people to upgrade because 4K was the future, and this allowed TV companies to suddenly ramp up pricing on TVs and profit margins. And once you did upgrade, well, now you need 4K content, right? So, film studios found the perfect excuse to resell that same movie in a new 4K Blu-ray packaging. Or streaming services found the perfect excuse for a new, more premium plan. And again, most of the time what they were using were just upscaled 2K intermediates. Why pay for 4K then? There is some logic to these 4K plans being more expensive because in theory, you’re streaming a bigger file, it’s four times larger than the previous one, there’s more data in there, which naturally will cost more to stream, right? But there’s your answer. Bigger files are better. It’s what we want, right? We want more information, we want more detail, we want less compression, and we want more picture quality.

**18:55 - 20:30 Speaker 1:** So let me go back to my Blade Runner 2049. Blade Runner has a 4K digital intermediate, so there was real 4K there. And funny enough, it was shot by the same cinematographer as O Brother, Where Art Thou? Assuming that they used an industry-standard codec for that file, that would probably be something like ProRes. The DI file for Blade Runner might have been something like 1800 gigabytes, like 1.7 terabytes. That’s the purest form of the movie, the one that’s stored in the studio servers. But they can’t send a 1.7-terabyte file to every cinema in the world because hardly any computer could play that thing. It needs to be compressed and still look good, so how do they do that? So, to send this movie to theaters, they might compress it to a DCP file of maybe 600 gigabytes; that’s for high-end projectors like an IMAX digital release. Now lower-end movie theaters, they might get a smaller copy, maybe a 300-gigabyte copy. And yet, movies at the movie theater look great not because they’re 4K or 2K. So, we already saw that at a certain distance, the 2K or the 4K don’t even matter. 

**20:30 - 21:32 Speaker 1:** Movies in the theater look great because they get a hard drive copy of the film, a file that is hundreds of gigabytes in size, and it’s as close as possible to that original DI. Now here’s every color that is visible to the human eye. Now a DI master, a digital intermediate, will probably use the ACES encoding system, which covers 100% of these colors. It kind of lives like here. Theater distribution copies of the film, they’re compressed. They’re compressed in a standard called DCI-P3, which covers 53% of the colors that we can see. And it’s kind of a triangle here. In other words, there are some greens and there are some magentas that we can see in the real world that we’re never going to be able to see in a movie theater. Now that detail may have been captured by the camera because cameras can generally do that. That detail may still be in the digital intermediate because the codec can handle it. But it’s gone, it’s gone even from the best copy of the film that you will ever be able to see in a digital format. 

**21:32 - 22:19 Speaker 1:** Now by the time that we get our streaming copy, the movie will be even more compressed. Normally, it’s going to be compressed kind of at this range. This is the Rec. 709 range, and we’ve lost even more colors. We’ve lost some of these greens and these yellows and these reds and magentas that the codec just can’t handle. Rec. 709 only covers about 35% of the colors that are visible to the eye. And a bunch of colors are gone. Now this right here is the cause of my color banding. Like the oranges, between this orange and this orange, that information is just gone; it doesn’t exist in the movie copy anymore. Streaming services rely on different codecs; codecs are like encoding algorithms that try to preserve as much detail as possible while shrinking the file size. But it is a lot of shrinkage. 

**22:19 - 22:53 Speaker 1:** A study by 4K Film DB found that most streaming services don’t go over 40 megabits per second. Apple TV wins this one, followed by HBO, then Netflix, then Amazon. So, why won’t they stream at a better quality? Like, home internet is already in the hundreds or thousands of megabits per second, like they could do it, right? Are the streaming services just cheating on us? I wanted to blame Netflix’s greed, but ah, that’s not really the case. I mean, it would increase their broadband and their CDN costs like tenfold, but it’s not just their fault; that’s the thing. It’s also the Ethernet ports or the Wi-Fi antennas in our devices; many of them, they’re just capped at 100 megabits per second. It’s also the processing power that’s needed to decode and play a file that is so large; most TVs just couldn’t handle it.

**22:53 - 23:30 Speaker 1:** Now because of those limitations, 4K prioritized more resolution because it was easier to market and in exchange, well, it made us sacrifice color. Sometimes to include pixels that weren’t even there in the first place. Just look at an old 1080p Blu-ray; they often look better than a 4K movie from streaming. So, the extra storage in that disk is being used for that detail and for that color, not for pixels. That again, you probably won’t see if your TV is too far away. But if you’re still with me, I’m sure that you now you want to know, well, how to get around this compression codec fake 4K mess? How to get the closest possible experience to real film in your couch? And this is my favorite part of the rabbit hole; how to learn from all of this nerding to get movies at home that look like the original.

**23:30 - 24:25 Speaker 1:** So, looking like the original film. That’s obviously a loaded sentence because so much of this process has changed now. Most movies, they aren’t even shot on film anymore. 

**23:41 - 23:51 Speaker 3:** A dinosaur: dead. It scratches, it breaks, it’s dirty, it’s a nightmare.

**23:59 - 24:25 Speaker 1:** Some cameras can shoot footage in up to 12K, and that’s the original file, and that’s a file, not a negative, and then that file gets sampled down into that 4K or sometimes even a 2K digital intermediate. The Martian is a is a good example of this. The Martian was shot digitally in 6K and all that 6K information was there, it was there in the footage. But because The Martian had so many visual effects shots, the digital intermediate ended up being 2K because nobody wanted to render all of those special effects in 6K. 

**24:25 - 25:01 Speaker 1:** Purists will agree that movies shot on digital are shit. To me, the magic of movies is connected to 35-millimeter. Real films are shot on film, right? That’s a heated debate; I’m not going to get into it today; I’m sure there’s going to be some shouting matches in the comments. But what I will talk about is a cheat code. Now some cinematographers, they strive for that OG film look but shooting on film is very expensive and fewer and fewer people are willing to pay for it or can afford it or even know how to do it. What they do is they shoot digital, they edit the film digital, and then they go through the trouble of printing that precut of the movie into film at a lab and then scanning it again to generate their 2K intermediate or their 4K intermediate. Because it went through film, it catches some of that film texture. That’s the trouble they go through just to try and get some of that original film feeling.

**25:01 - 26:15 Speaker 1:** But back to our home. How do we get close to that OG experience? First of all, might need a bigger TV; you might need to move your couch closer to make sure that you’re squeezing all that 4K resolution. And if you’re not squeezing it, you can save yourself some money and downgrade your plan. Second, you have to make sure that your TV supports today’s color standards. Movies encoded in HDR support a lot more colors than movies in SDR. HDR as a standard is a mess; it’s a mess of color and brightness. We used to make YouTube videos in HDR and we had to stop making them because nobody… everybody got a different version of our video and some of them looked like shit. But let me walk you through what really matters about HDR, which is color. HDR files support colors in the Rec. 2020 gamut, which is kind of like here, and and it’s huge. Rec. 2020 has like 75% of all the colors that we can see. So many colors, in fact, that most TVs can’t even display it. So, the information is in the file; it’s just that the TV can’t display it.

**26:15 - 27:00 Speaker 1:** Now high-end TVs, they probably operate something closer to the P3 gamut, so kind of all the way up to here. Lower-end TVs in 2026, ah, they settled for around 75% of the P3 space, so probably something close to here. There are some top-tier, top-tier screens and projectors that are starting to get closer to this Rec. 2020 gamut. But, but, but, before you go hunting for that, remember: distribution versions of the film often only have P3 DCI data. So, there aren’t more colors in there. The fact that Rec. 2020 HDR supports more colors than the movie actually has is great, but it doesn’t make the movie look better. It’s like putting a 12-ounce soda inside a 20-ounce bottle; like, the bottle is bigger, but there’s still only 12 ounces of liquid inside. Now here’s where things can get really dangerous for your wallet. Dis-