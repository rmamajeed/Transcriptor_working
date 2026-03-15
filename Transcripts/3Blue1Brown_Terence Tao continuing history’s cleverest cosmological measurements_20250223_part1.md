---
title: 3Blue1Brown_Terence Tao continuing history’s cleverest cosmological measurements_20250223_part1
audio_file: 3Blue1Brown_Terence Tao continuing history’s cleverest cosmological measurements_20250223_part1.mp3
note_id: ea9b4a1e-a309-42b9-b847-52ec28226060
date_processed: '2026-02-18'
classification:
  primary_domain: Physics
  sub_domains:
  - Astronomy
  - Cosmology
  - History of Science
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people:
  - name: Terence Tao
    role: Collaborator
    contribution: Part of the collaboration
  - name: Edmond Halley
    role: Scientist
    contribution: Originally came up with the idea for measuring Venus' distance
  - name: Guillaume Le Gentil
    role: Explorer
    contribution: Attempted to measure the transit of Venus
  - name: Romer
    role: Scientist
    contribution: Measured the speed of light using Io's orbit
  - name: Huygens
    role: Scientist
    contribution: Realized the reason for the delay in Io's orbit
  works_cited: []
  concepts_mentioned:
  - Parallax
  - Transit of Venus
  - Astronomical Unit
  - Speed of Light
  - Orbit of Io
  laws_theories_cited: []
concepts:
- name: Parallax
  definition: The apparent shift of an object's position in the sky due to a change
    in the observer's location
  parent_concepts:
  - Astronomy
  related_concepts:
  - Triangulation
  - Distance Measurement
  abstraction_level: Applied
  confidence: 1.0
- name: Transit of Venus
  definition: The passage of Venus across the Sun's disk, used to measure the distance
    to Venus
  parent_concepts:
  - Astronomy
  related_concepts:
  - Parallax
  - Astronomical Unit
  abstraction_level: Applied
  confidence: 1.0
- name: Astronomical Unit
  definition: The average distance between the Earth and the Sun, used as a standard
    unit of measurement
  parent_concepts:
  - Astronomy
  related_concepts:
  - Parallax
  - Transit of Venus
  abstraction_level: Fundamental
  confidence: 1.0
- name: Speed of Light
  definition: The speed at which light travels, measured using Io's orbit
  parent_concepts:
  - Physics
  related_concepts:
  - Astronomy
  - Optics
  abstraction_level: Fundamental
  confidence: 1.0
- name: Orbit of Io
  definition: The path Io follows as it orbits Jupiter, used to measure the speed
    of light
  parent_concepts:
  - Astronomy
  related_concepts:
  - Jupiter
  - Speed of Light
  abstraction_level: Applied
  confidence: 1.0
relationships:
- source_concept: Parallax
  target_concept: Transit of Venus
  relationship_type: supports
  strength: 0.9
  evidence: The transit of Venus is used to measure the distance to Venus using parallax
  reasoning: The transit of Venus is an application of parallax to measure the distance
    to Venus
- source_concept: Astronomical Unit
  target_concept: Transit of Venus
  relationship_type: derives_from
  strength: 0.9
  evidence: The Astronomical Unit is measured using the transit of Venus
  reasoning: The transit of Venus is used to measure the distance to Venus, which
    is then used to calculate the Astronomical Unit
- source_concept: Speed of Light
  target_concept: Orbit of Io
  relationship_type: supports
  strength: 0.9
  evidence: The speed of light is measured using Io's orbit
  reasoning: The orbit of Io is used to measure the speed of light
cross_domain_insights:
- connection_type: principle_application
  source_domain: Physics
  source_concept: Parallax
  target_domain: Computer Vision
  target_concept: Stereoscopy
  insight: Measuring distance through angle differences
  explanation: The principle of parallax, used in astronomy to calculate distances
    to stars, is structurally similar to how stereoscopy works in computer vision,
    where the difference in angles between two images is used to estimate depth. This
    principle can be applied to various fields where distance or depth needs to be
    calculated based on angular differences. The mathematical underpinnings of parallax
    measurement can be directly applied to understanding how stereoscopy achieves
    depth perception in computer vision.
  potential_applications:
  - Depth sensing technologies
  - 3D modeling
  confidence: 0.9
  historical_example: The use of parallax in astronomy inspired the development of
    stereoscopic photography in the 19th century.
- connection_type: structural_analogy
  source_domain: Physics
  source_concept: Orbit of Io
  target_domain: Economics
  target_concept: Stable Equilibria in Market Dynamics
  insight: Orbital stability analogized to market equilibrium
  explanation: The orbital stability of Io around Jupiter, influenced by gravitational
    forces, can be seen as a structural analogy to stable equilibria in market dynamics,
    where economic forces (supply and demand) influence market stability. Both involve
    complex systems seeking balance under the influence of various forces. The mathematical
    models describing orbital mechanics can provide insights into understanding the
    dynamics of economic systems seeking equilibrium.
  potential_applications:
  - Market analysis
  - System dynamics modeling
  confidence: 0.8
  historical_example: The concept of equilibrium in physics has historically influenced
    the development of equilibrium theories in economics.
- connection_type: metaphor
  source_domain: Physics
  source_concept: Speed of Light
  target_domain: Information Technology
  target_concept: Data Transfer Speed
  insight: Limitations in data transfer speed
  explanation: The speed of light, as the universal speed limit, serves as a metaphor
    for the limitations in data transfer speed in information technology. Just as
    nothing can exceed the speed of light, there are physical limits to how fast data
    can be transferred. This metaphor helps in understanding the fundamental limitations
    and challenges in designing faster data communication systems.
  potential_applications:
  - Optimizing data transfer protocols
  - Quantum communication
  confidence: 0.7
  historical_example: The realization of physical limits in data transfer has driven
    innovations in communication technologies.
- connection_type: historical_precedent
  source_domain: Physics
  source_concept: Transit of Venus
  target_domain: Navigation and Mapping
  target_concept: Geodesy
  insight: Historical method for measuring the Astronomical Unit applied to geodesy
  explanation: The historical method of using the Transit of Venus to measure the
    Astronomical Unit has a precedent in the field of geodesy, where similar principles
    of triangulation and timing are used to measure distances and positions on Earth.
    The methods developed for astronomical measurements have been adapted for terrestrial
    applications.
  potential_applications:
  - Precision mapping
  - GPS technology
  confidence: 0.9
  historical_example: The Transit of Venus expeditions of the 18th century laid groundwork
    for modern geodetic surveying techniques.
bridge_concepts:
- concept: Triangulation
  appears_in_domains:
  - Physics
  - Computer Vision
  - Geography
  role: Method for calculating distances or positions based on angles and known side
    lengths
  examples:
  - Parallax measurement in astronomy
  - Stereoscopy in computer vision
  - Surveying in geography
- concept: Equilibrium
  appears_in_domains:
  - Physics
  - Economics
  - Biology
  role: State of balance between opposing forces or influences
  examples:
  - Orbital mechanics in physics
  - Market equilibrium in economics
  - Homeostasis in biology
mental_models:
- name: Systems Thinking
  description: Analyzing complex systems by understanding the relationships and interactions
    between their components
  applied_to:
  - Understanding the solar system as a complex system
  transferable_to:
  - Economic systems
  - Biological systems
  - Social systems
- name: First Principles
  description: Breaking down complex systems into their fundamental principles to
    understand them
  applied_to:
  - Deriving the laws of motion from first principles
  transferable_to:
  - Problem-solving in any domain
  - Innovation in technology and science
analogies_used:
- source_domain: Everyday Experience
  source_concept: Throwing a Ball
  target_domain: Physics
  target_concept: Projectile Motion
  mapping:
    Trajectory of the ball: Path of a projectile under gravity
  pedagogical_value: Helps in understanding the concept of projectile motion by relating
    it to a familiar experience.
tags:
  hierarchical:
  - '#Physics → #Astronomy → #History of Science'
  topical:
  - '#Parallax'
  - '#TransitOfVenus'
  - '#AstronomicalUnit'
  - '#SpeedOfLight'
  methodological:
  - '#Measurement'
  - '#Observation'
  people:
  - '#TerenceTao'
  - '#EdmondHalley'
  - '#GuillaumeLeGentil'
  - '#Romer'
  - '#Huygens'
  concepts:
  - '#Parallax'
  - '#TransitOfVenus'
  - '#AstronomicalUnit'
  - '#SpeedOfLight'
  - '#OrbitOfIo'
  temporal:
  - '#18thCentury'
summary: 'Here is a concise summary of the main points in 2-3 sentences:


  The video discusses the cosmic distance ladder, a series of methods used to measure
  the vast distances in our universe, starting from the solar system and extending
  to the farthest galaxies. The methods include triangulation using parallax, measuring
  the brightness of stars and Cepheid variables, and using redshift to infer distance,
  with each rung of the ladder building upon the previous one to achieve greater precision
  and scope. By combining these methods, astronomers have been able to create a 3D
  map of the universe, with distances measured to within 10% accuracy, although there
  remains an ongoing mystery of a 10% anomaly in Hubble''s Law at very large scales.'
key_ideas:
- idea: Here are 3-5 key ideas discussed in the transcription text with a short description
    for each
  description: ''
- idea: The Cosmic Distance Ladder**
  description: The concept of measuring distances in the universe by building upon
    previous measurements, starting from the distance to the Sun and expanding to
    nearby stars, galaxies, and eventually the entire observable universe.
- idea: Parallax Method**
  description: A technique used to measure the distance to nearby stars by observing
    their apparent shift in position against the background stars when viewed from
    opposite sides of the Earth's orbit, allowing for the calculation of their distance
    using trigonometry.
- idea: Standard Candles**
  description: The use of objects with known absolute brightness, such as Cepheid
    variable stars, to measure the distance to galaxies and other celestial objects
    by comparing their apparent brightness to their known absolute brightness.
- idea: Hubble's Law**
  description: The observation that the redshift of light from galaxies is proportional
    to their distance, allowing for the measurement of distances to galaxies and the
    expansion of the universe.
- idea: The Importance of Accurate Measurements**
  description: The need for precise measurements and calibration of methods to ensure
    accurate distances and understanding of the universe, as small errors can propagate
    and affect our understanding of the cosmos.
---
## Key Concepts

**Parallax**  
The apparent shift of an object's position in the sky due to a change in the observer's location

**Transit of Venus**  
The passage of Venus across the Sun's disk, used to measure the distance to Venus

**Astronomical Unit**  
The average distance between the Earth and the Sun, used as a standard unit of measurement

**Speed of Light**  
The speed at which light travels, measured using Io's orbit

**Orbit of Io**  
The path Io follows as it orbits Jupiter, used to measure the speed of light

## Cross-Domain Connections

**Physics → Computer Vision**

*Measuring distance through angle differences*

The principle of parallax, used in astronomy to calculate distances to stars, is structurally similar to how stereoscopy works in computer vision, where the difference in angles between two images is used to estimate depth. This principle can be applied to various fields where distance or depth needs to be calculated based on angular differences. The mathematical underpinnings of parallax measurement can be directly applied to understanding how stereoscopy achieves depth perception in computer vision.

**Physics → Economics**

*Orbital stability analogized to market equilibrium*

The orbital stability of Io around Jupiter, influenced by gravitational forces, can be seen as a structural analogy to stable equilibria in market dynamics, where economic forces (supply and demand) influence market stability. Both involve complex systems seeking balance under the influence of various forces. The mathematical models describing orbital mechanics can provide insights into understanding the dynamics of economic systems seeking equilibrium.

**Physics → Information Technology**

*Limitations in data transfer speed*

The speed of light, as the universal speed limit, serves as a metaphor for the limitations in data transfer speed in information technology. Just as nothing can exceed the speed of light, there are physical limits to how fast data can be transferred. This metaphor helps in understanding the fundamental limitations and challenges in designing faster data communication systems.

## Discussion Topics

- **Here are 3-5 key ideas discussed in the transcription text with a short description for each:** 
- **The Cosmic Distance Ladder**:** The concept of measuring distances in the universe by building upon previous measurements, starting from the distance to the Sun and expanding to nearby stars, galaxies, and eventually the entire observable universe.
- **Parallax Method**:** A technique used to measure the distance to nearby stars by observing their apparent shift in position against the background stars when viewed from opposite sides of the Earth's orbit, allowing for the calculation of their distance using trigonometry.
- **Standard Candles**:** The use of objects with known absolute brightness, such as Cepheid variable stars, to measure the distance to galaxies and other celestial objects by comparing their apparent brightness to their known absolute brightness.
- **Hubble's Law**:** The observation that the redshift of light from galaxies is proportional to their distance, allowing for the measurement of distances to galaxies and the expansion of the universe.
- **The Importance of Accurate Measurements**:** The need for precise measurements and calibration of methods to ensure accurate distances and understanding of the universe, as small errors can propagate and affect our understanding of the cosmos.

## Full Transcription



00:00 - 01:05 **Speaker 1:** This animation is zooming out by a factor of ten every two seconds. Maybe you've seen things like this before, conveying the mind-boggling scale of our universe. But here, in this video, you and I are going to continue the saga through the many moments of delightful ingenuity throughout human history that led us to first discover how far away objects in the cosmos really are. Appreciating *how* we know these distances is to me more amazing than the distances themselves. This is part two of a collaboration with Terence Tao, and it's okay if you haven't yet seen part one. Each video should be relatively self-contained, but for context, we left off with Kepler's ingenious method for deducing the shapes of all of the orbits of the planets around the sun. So people knew what the solar system looked like, but they still didn't have an exact sense of scale. And this left astronomers hungry to measure *any* distance that they could in this system, like maybe how far away a given planet is from Earth at a given moment, since that would be enough to lock everything else into place. Now, I'll admit, while I had vaguely learned about how this was done before, I definitely had not appreciated the cleverness of the details.

01:06 - 01:30 **Speaker 2:** You could measure distances to the planets like Venus; take two measurements on different sides of the Earth. Around the time of Captain Cook, when they were traveling to discover Australia and so forth, part of the reason for this was a scientific mission. I mean, they wanted to know the distance to Venus and Mars and so forth. They wanted people to take precise measurements, say one in Greenwich in the UK and one somewhere in the Southern Hemisphere, at exactly the same time of the same object.

01:31 - 01:46 **Speaker 1:** The key idea here is that as you sail down to the Southern Hemisphere and you observe a given object up in the sky, its position in the sky, say relative to the background constellations, will appear to shift up as the angle of your line of sight slowly changes with your position. We call this parallax.

01:47 - 01:54 **Speaker 2:** It is the same parallax that we use with binocular vision. Our eyes are a certain distance apart, and so we can determine depth for any distance that's not too much larger than the distance between our eyes. It's just that now we figured out how to make two eyeballs on different sides of the Earth.

01:55 - 03:40 **Speaker 1:** Now, if you want to turn this into a measurement, you first need to understand *this* line right here, connecting the two different observation points. Both its distance and its direction. Because people knew the size of the Earth and they could tell where they were on the Earth, that would be taken care of. Then the hard part is for the first observer to take a precise enough measurement of the viewing angle to this object. They need to deduce this angle here, and for the second observer to do likewise. If you can do that, you have a triangle where you know all three of the angles and you also know one of the side lengths. This means with just a little bit of trigonometry, you can figure out any other side length, which for example tells you how far away this object is from one of the observers. Now, the way I'm drawing it here, it makes it look almost easy. But for the real-world measurement, you have to keep in mind just how far away everything is. If we zoom out so that they're both looking at something as far away as the moon, it would look something like this. But the moon, cosmologically speaking, is really quite close. So even if both of them are looking at the nearest planet, Venus, when it is at its absolute closest to Earth, it's around 39 million kilometers away, which is over 6,000 times the radius of the Earth. So zooming back in to those two observers, even if they were as far away as you could get them, one at the top of the Earth and another at the bottom of the Earth, these two lines of sight would be almost parallel. If you work out the little bit of trigonometry, if they're both looking at Venus at its absolute closest point, the difference in angle between these two lines is about one arc minute, which is 1/60th of a degree. So, if this is going to work, your measurements have to be extremely precise and you have to be absolutely sure that both observers are really looking at the same thing at the same moment.

03:41 - 03:59 **Speaker 2:** Now at the time clocks were not good enough that they could actually just say "at this specific time make a measurement". Also, you're not guaranteed that you can even find the planet and so forth. But... um... there's these transits, this thing called the transit of Venus. Sometimes Venus travels um along the Sun, and so you can just time exactly when Venus hits the edge of the Sun.

04:00 - 07:44 **Speaker 1:** This is the part I had not appreciated; in particular, how sensitive everything really is. So up in the Northern Hemisphere, if you're watching the transit of Venus, maybe it looks something like this. And far away at some point down in the Southern Hemisphere, due to parallax, Venus would appear higher up. And you essentially want to know *exactly* how much higher up. Now, this animation is greatly exaggerating the difference. In reality, the two would look much, much more similar, more like this. And remember, there was no photography, so it's not like they could take pictures and closely compare them. When you look at the sun up in the sky, it spans around 32 arc minutes of viewing angle. And this is something they would have been able to measure. The deviation in viewing angle to Venus for these two observations would be a *fraction* of an arc minute. So to measure exactly what that fraction was, each observer would not try to directly describe where it was. Instead, they would measure the *duration* of the transit—how long it takes from the moment that Venus's silhouette first appears on the disk to the moment that it leaves. Critically, they also would have known how fast Venus and the Sun are moving through the sky at this time. And this would let them calculate how long it should take Venus's apparent position to traverse the distance of, say, one Sun diameter. It turns out to be around seven hours. I won't dwell too much on the details for how to calculate this, but at a high level, if you think about Earth and Venus both orbiting the sun, the angle of this line of sight right here—from Earth through Venus—is something that they would have understood well, since thanks to Kepler, they knew the relative shapes of the orbits and how long it takes each planet to go around the Sun. So in principle, they could calculate how long it should take for this line to scan over those 32 arc minutes in the sky that the Sun occupied. The point is that by measuring the durations of the transit from these two different locations, that could tell you the lengths of these two lines drawn across the Sun's disk. These are very similar, but measurably different. And with a little bit of circle geometry, the lengths of those lines will tell you how far apart they are—that fraction of an arc minute separating the two observations. And then this, in turn, from everything that we discussed before, lets you deduce how far away Venus is in terms of the distance between those observers. *That* is just so clever to me. It was Edmond Halley who originally came up with this idea, but sadly he didn't live long enough to see it come to fruition. Before moving on, I simply have to tell you the story of Guillaume Le Gentil. He was another explorer, also tasked with making one of these measurements for the transit of Venus. Specifically, he was going for the one in 1761, but he was delayed by the Seven Years' War and still at sea when the transit happened, so he was unable to make the measurement. Now, the next transit of Venus was going to be eight years later, but after that, it wouldn't be for another 105 years. So he decided to extend his journey, do a bunch of other explorer things, and catch the next one. And by 1769, he was all set up in the Philippines ready to go. But on that day, it was cloudy, so he couldn't see anything. Once he finally got back to France, he found that he had been declared dead, his wife had remarried, and his relatives had all plundered his estate. Now remember, the reason people cared so much was that having this one measurement was enough to lock in place the scale of the whole solar system. So once they had it, they would automatically know every other distance involved.

07:45 - 08:00 **Speaker 2:** This was important, actually, because you need to do this in order to work out the distance to the Sun. The distance to the Sun is... is the most important rung of the ladder. It's called the Astronomical Unit. Almost everything beyond the solar system is measured in terms of the Astronomical Unit. And so they really needed really accurate estimates.

08:01 - 08:29 **Speaker 1:** Given what we just saw, you might be able to guess how you can use this Astronomical Unit to measure the distance to nearby stars. But before we get to that, there's actually one more clever deduction that you can make once you know this distance, a little closer to home and incredibly important for physics.

08:30 - 08:58 **Speaker 2:** Romer was measuring Jupiter. And Jupiter has a small moon called Io. Io orbits Jupiter really, really fast because it's really close to Jupiter. Our moon takes 28 days to go around the Earth. Io takes 42 hours.

**Speaker 1:** That's whippin'.

**Speaker 2:** Yeah, it's—it's extremely fast. If you—if you observe Jupiter on a telescope, you know, you see Io, which is just this white dot go in—behind Jupiter's shadow and then out, in, out, in, out.

08:59 - 09:18 **Speaker 1:** Romer was marking down one precise moment for each one of these cycles. You see, Io goes dark when it falls into Jupiter's shadow, which it does every cycle because Jupiter is just so big. As it emerges, it becomes bright again. Watching it through a telescope night after night, you can mark the exact time that it pops back into view. And if you go out with the telescope and you do this a whole bunch, what you'll notice is that these happen in 42-hour increments.

09:19 - 10:48 **Speaker 2:** Like clockwork... except it wasn't clockwork. So, Romer was observing Io go back and forth, back and forth for months. And he observed that at different times of the—of the year, Io was ahead of schedule, sometimes Io was behind schedule. So, let me draw a picture. Earth goes around the Sun; Jupiter also goes around the Sun. Yeah. So, when you're measuring the orbit of Io, um it was... 20 minutes ahead... 20 minutes earlier when the Earth was on the same side... as Jupiter than when the Earth was on the opposite side of Jupiter. It took 20 minutes longer. There was a delay in the orbit. So he measured this after some very precise calculations. And Huygens realized that the reason for this is because light was taking 20 minutes to traverse this extra distance. So, two Astronomical Units is traversed in about 20 minutes.

**Speaker 1:** That's so clever.

**Speaker 2:** Yeah, yeah, yeah, yeah.

10:49 - 13:25 **Speaker 1:** Historically, this was all *before* the measurement to Venus, so at that time they didn't actually know the true Astronomical Unit. So their estimates for the speed of light frankly don't look that impressive if you see them. But at that time, it was not even obvious that light *had* a speed. For most experiments you could do down on Earth at that time, it just looks instantaneous. But at astronomical scales, it's actually really slow. And this very clever way to measure its speed by observing Io, imprecise though it was, laid the groundwork for more precise experiments down on Earth once people had at least a rough sense of how fast it really was. I also really like this because it comes back around to the distance ladder. These days, with technology, the more accurate way that we measure the distances to planets like Venus is not with parallax, but using radar. But this, of course, relies on knowing the speed of light. And now, let's finally leave our solar system and measure the nearby stars. Again, you can use parallax. It's essentially identical reasoning for how we got the distance to Venus, only this time the two observation points are not opposite sides of the Earth; they're opposite sides of Earth's orbit. That is, you measure the star at one time of the year, and then you wait six more months for the Earth to be on the other side of the Sun, make another measurement, and compare the two angles. Again, for demonstration purposes, I'll be drawing this star unrealistically close. In principle, over the course of six months, the line of sight from the Earth to a star slowly changes angle, so the position of that star in the sky should slowly drift over those months. And it's very subtle, but you can actually see this in practice. This right here is a timelapse of a very zoomed-in view for our nearest neighbor, Proxima Centauri, taken over six months. And you can see that over that time, it does gently drift with respect to the background stars. But as before, the mind-blowing part is to appreciate just how subtle the effect is, and therefore how impressive it is that people were able to use this for calculation back in the 19th century. Let's actually work out the math here. Suppose a star is a given distance *D* away, and to make everything easy, let's assume it's perpendicular to this connecting line between our two observation points. This angle right here represents half of the change in viewing angle between those two observations. The tangent of that angle, opposite over adjacent, gives you the ratio between one Astronomical Unit and the distance between that star and our Sun. Rearranging a little bit, this change in angle looks like two times the inverse tangent of that ratio. So, what is that ratio? Well, for that closest star that I mentioned, Proxima Centauri, it's over 40 trillion kilometers away, which is over four light years and around 260,000 times an Astronomical Unit. Now if you plug that in, it means that this change in angle from the two observation points is a tiny, tiny portion of a degree. Let me see if I can show you how small this is. This right here is a circle representing 360 degrees of full viewing angle. And if we zoom in real close to one degree, you'll remember I mentioned earlier that the Sun—and also the Moon for that matter—take up about half a degree of viewing angle. And we often think of this as being divided into 60 arc minutes. Well if you zoom in even further to one arc minute, this is commonly divided into 60 arc seconds. At its largest, Jupiter will span about 50 arc seconds of viewing angle. So, this parallax for Proxima Centauri, the nearest star, is only about 1.5 arc seconds. As another way to put that in perspective, this is about the same angular size as if you held out a dime in front of you, but two and a half kilometers away—a mile and a half down from where your eye is. And that's the closest star; it only gets worse from there. The first measurement of this kind was successfully done in 1838 by Friedrich Bessel. It wasn't Proxima Centauri; they wouldn't have been able to know which star was closest. But over the course of the next century, there was a monumental effort for many more measurements to try to catalog as many stars as we could. But this parallax idea only really works for a tiny portion of our galaxy. So to figure out the full size of the Milky Way, that requires a new idea.

13:26 - 13:50 **Speaker 2:** Roughly speaking, the Milky Way is this... I can't draw a spiral. Okay, this is again maybe a place where your graphics are going to be much better than... than what I—I draw here. Okay. So, our sun is on one of the arms. Yeah. Yeah. So, by using parallax, by about the 19th century, there was about a thousand stars close enough to the Sun that they knew how far away these stars were, you know, maybe about 10, 100 light years away.

13:51 - 14:04 **Speaker 2:** So they knew how far away these stars are, and they knew how bright they looked.

**Speaker 1:** Right.

**Speaker 2:** And so they knew how bright they *were* by... by the inverse square law of... of light propagation.

14:05 - 15:42 **Speaker 1:** Just to spell this out a little more explicitly, if you imagine you have some star in space emitting a bunch of light in all directions, then at a given distance away, all of that light is evenly spread along a sphere. So if you're that distance away and you're measuring the brightness with some little patch of area—maybe that represents your camera or a photosensor or your pupil, something like that—the amount of light you're receiving depends on the proportion of this total sphere that your little area represents. So for example, if you were twice as far away, that same beam of light that you *had* been measuring up close is now spread along four times the area. So out at this distance, if you used the same photosensor with the same area as before, it would only be measuring a quarter as much light. In general, the amount of light that you see, the apparent brightness of the star, is proportional to its absolute brightness—the total amount of light it's giving away—divided by the square of the distance between you and that star. So for all of those stars whose distance we could measure using parallax, by also measuring the apparent brightness, astronomers could know their absolute brightness. The other thing they could observe is the color of all of these stars—the frequency of light that they're emitting—which is actually incredibly helpful. For example, you can start looking for patterns in this data. Imagine you organize all of your stars onto a plot where in the x-direction we're going to sort them by the color. The common, kind of backward-seeming convention is for higher-frequency light like blue to go on the left, and lower-frequency like red to be on the right. Then in the y-direction, you can sort according to the absolute brightness of these stars, which again you can deduce by knowing their distance and using the inverse square law.

15:43 - 15:50 **Speaker 2:** A thousand points of data, all of intensity and color. Okay. And this is the main sequence. Most stars live on this sequence.

15:51 - 18:05 **Speaker 1:** This is known as the Hertzsprung-Russell diagram, initially created around 1911. The data that went into it, though, represents decades of effort. A lot of it comes from this group of women at the Harvard College Observatory, commonly known as the "Harvard Computers." The diagram exposes how the color of a star can tell you something about its absolute brightness. This main sequence represents one very common type of star; it includes our Sun, during a phase of its evolution when it's burning hydrogen in its core. Stars in this category that are bigger and brighter also tend to burn hotter, and they have black-body radiation more in the blue direction, while those that are smaller burn cooler and they radiate more in the red direction. So, if you see some star very far off—way too far for parallax measurement—and if you also know that it should fall into this main sequence (more on that in a moment), its color can tell you its absolute brightness; you fit it to this curve. And then by using its apparent brightness with the inverse square law, you can deduce how far away it is. Now you might ask, how would you know that a star should fall on this main sequence? The full diagram is much more splotchy than a clean line; it's got a lot of different components representing different types of stars. The thing to keep in mind is that the color information you get from a star is much richer than what a single number on this x-axis could convey. For example, this right here represents all of the relative intensities for light that we get from our Sun, across many different wavelengths. It's what we call its spectrum. This is the usual pattern you see: you have a general lump representing the black-body radiation, with certain wavelengths greatly reduced. Those correspond to the wavelengths of light absorbed by the atoms in the Sun. And where specifically those absorption lines fall will tell you what the atoms are in the star. And from that, it helps classify what kind of star it even is. So for example, while those Harvard Computers were doing a bunch of detailed analysis of spectra from all these stars, some of them—including Antonia Maury and Annie Cannon—came up with very useful classification systems for these stars based on the spectra. You can then use that classification scheme to tell you which cluster you would expect a given star to fall in, in this Hertzsprung-Russell diagram. For example, whether it should be in this main sequence or if it's something else entirely, like a red giant.

18:06 - 18:22 **Speaker 2:** And then once you have this law, you can then go all throughout the galaxy and you can now measure. But... it stops working past the galaxy because the—each individual star becomes too faint. The galaxy is only a really tiny portion of the full universe.

18:23 - 18:34 **Speaker 2:** Okay, so you have one tiny little galaxy here. So there's all these other galaxies.

**Speaker 1:** Yeah.

**Speaker 2:** Yeah. And so in a galaxy, most stars, um, you cannot measure the brightness of a—of a single star because there's just billions of them all crammed into the same place.

18:35 - 19:46 **Speaker 2:** But... there are some amazingly bright stars that are called Cepheids. These supergiant stars that are thousands and hundreds of times brighter than the Sun. Some of them live in our own galaxy, and some of them live in other galaxies. They still blend in, but—but you can still kind of measure their brightness. These stars are what are called variable stars. Um, so most stars, they stay the same intensity for all time, but these Cepheid stars, their—their brightness oscillates. So they have a period of intensity, like every 20 days, every 10 days, they oscillate. And it turns out that the bigger the Cepheid, the brighter it is, the longer the period. Henrietta Swan Leavitt, who was a 20th-century astronomer, she measured all of the—the Cepheids that she could in our own galaxy, and she plotted the period against the intensity. And she found basically a linear law: that the brighter the Cepheid, the longer it took. That, like the Hertzsprung-Russell diagram before, gave a standard candle. That, um, that if a galaxy happened to have a Cepheid in it, you could just observe it, work out its period, that gave you its intensity, that knows—so now you know how bright it *should* be, and you know how bright it looks, you can measure its distance. That gave the next rung of the ladder. So a couple thousand galaxies where you could measure the distance. But that, again, is only a tiny portion of the universe.

19:47 - 20:06 **Speaker 1:** Using these powers of ten...

**Speaker 2:** Oh yeah, yeah, yeah, yeah. To kind of zoom and zoom.

**Speaker 1:** Oh, yeah.

**Speaker 2:** So now this sort of local cluster where—where thanks to Leavitt, you could work out the distances. And then there's the rest of the universe.

**Speaker 1:** But it's enough to get data of some kind.

**Speaker 2:** Yes, yes.

20:07 - 21:28 **Speaker 2:** And so Hubble, Edwin Hubble, was measuring all these galaxies. And they have certain spectral lines. For example, um, you know, there's—there's a lot of hydrogen around... um... each of these... um... these galaxies. And so there's certain spectral lines of hydrogen that get absorbed, and so there's—there's certain lines that are missing, or almost missing, in a spectrum. But he noticed that for some of the galaxies, their spectrum was shifted to the red from where it should be. But not all of them. And so he measured it. So he measured this redshift against distance. And again, he got the linear relationship. Um, there's actually a famous plot in his paper, which is now called Hubble's Law. That the redshift is proportional to the distance. Nowadays, we know why this is true: it's because general relativity predicts that the universe is expanding at a—at a uniform rate. And the further away things are, the more they recede, and the faster they recede, the more redshift they have. But again, this is a predictable law. So if you have a galaxy far, far away, if you know what its redshift is—you just measure its spectrum—you apply this law, you work out its distance. And so this is the largest rung of the ladder that we know today. The entire bubble of the observable universe, which we think is about 20%... of the whole universe, we don't know. Pretty much every object in the universe that emits light, or some sort of radiation, we can now measure the distance to. Usually by seeing how spectral lines shift.

21:29 - 22:42 **Speaker 2:** And so you can start mapping things. You can do 3D pictures of the universe. There's something called the Sloan Galactic Survey, which is... kind of doing this.

**Speaker 1:** For this visualization, what I did is read in some data from the Sloan Digital Sky Survey, which aggregates data about a huge number of galaxies, including their angle in the sky, and then critically, their distance away, as measured by redshift. This set doesn't include all of the angles in the sky—that's why it has this kind of wonky shape. This represents about half a million different galaxies, visualized as a simple point cloud. And in a sense, what you're looking at is a snapshot of our little corner of the universe, measured out to a radius of about 1.6 billion light years.

**Speaker 2:** And one thing that has been discovered is that galaxies are not just sort of randomly strewn in space; they form these filaments. They form these massive structures. So a galaxy is itself part of—of these much larger structures. The thing is, that's actually predicted by theory, or at least by experiment. So we can run in a computer billions of virtual galaxies uh orbiting by gravity for billions of years. And what we have found with simulations is that the galaxies, as they... um... evolve, do organize into strands that *do* resemble the strands that we're beginning to see. So that is, in some sense, some confirmation that all our theory is basically correct.

22:43 - 24:36 **Speaker 1:** If you're using redshift, what's the error that it'll give you on the distance?

**Speaker 2:** That's a good question. It's hard to calibrate at very large scales because we have very few other ways to measure the distance. Um, the gravitational black hole things, those are the—the most exciting. Normally to measure distances at—at this distance, you need to stack together a huge amount of rungs of the ladder. First of all, the distance to the Sun, and then from that, parallax to work out distance to nearby stars, and then from *that*, you can work out using main sequence fitting distance to other stars in the galaxy, and then Hubble's Law... no there's—there's Cepheids between that. And then Hubble's Law. You can use the gravitational measurements to *directly* measure the distance. Unfortunately, I—I don't quite remember... they're kind of like "standard sirens" is what they're called. There's a certain amount of energy that's released by a black hole collision. And so you kind of know how loud they are in absolute terms. And—but you can also measure how... how loud they are from the observatory. Um, and they're billions and billions of times fainter at that point because of the vast distance traveled. But they can use that to infer the distance. That they cross-checked against the Hubble... the redshift calculation. It matched to within like 10%.

**Speaker 1:** That's reassuring.

**Speaker 2:** Yeah, yeah, no, it—it is very reassuring. Although that 10% is controversial. It seems like there's something a bit wonky with Hubble's Law at very large scales. Like, this same 10% is showing up elsewhere too. It's an ongoing mystery exactly what is the cause of this 10% anomaly. And is one of our laws of physics wrong? There's something very basic called the Copernican Principle that is an article of faith now... uh... since the Copernican revolution, that we believe the laws of the universe are pretty much the same everywhere in the universe. Right. And this is a fundamental assumption that allows us to extend the ladder, and it's—so it's always rewarded us in the—in the past. It always fits. It leads to new laws of physics; it's everything self-consistent. But there's this slight 9% anomaly, or 10%, and it—it's an ongoing area of—the subject is—is a living subject, astronomy. But we've gotten a long way from that—that poor graduate student walking down...

**Speaker 1:** (Laughs)

**Speaker 2:** ...a long walk down Egypt.

**Speaker 1:** Yes.

24:37 - 25:01 **Speaker 1:** Maybe this goes without saying, but the cosmic distance ladder is too broad a topic for two videos to fully convey. After showing an early view of this on Patreon, for example, a number of people expressed sadness that there was no discussion of type 1a Supernovas. And fitting a story like this into an hour necessarily involves at least a little simplification along the way. Luckily, for the extra-curious among you, Terry has kindly put together an FAQ...