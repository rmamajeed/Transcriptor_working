---
title: Veritasium_You've (Likely) Been Playing The Game of Life Wrong_20251126_part1
audio_file: Veritasium_You've (Likely) Been Playing The Game of Life Wrong_20251126_part1.mp3
note_id: 95278cc1-b269-40b7-a08a-f2d5f7ce8599
date_processed: '2026-01-11'
classification:
  primary_domain: Economics
  sub_domains:
  - Probability Theory
  - Statistics
  - Game Theory
  difficulty_level: Intermediate
  content_type: Explainer
entities:
  people:
  - name: Vilfredo Pareto
    role: Italian engineer
    contribution: Discovered the Pareto distribution
  - name: Abraham de Moivre
    role: Mathematician
    contribution: Studied the normal distribution
  works_cited: []
  concepts_mentioned:
  - Normal distribution
  - Power law
  - Log-normal distribution
  - Pareto distribution
  - Game theory
  laws_theories_cited:
  - Normal distribution
  - Power law
concepts:
- name: Normal distribution
  definition: A probability distribution where most data points cluster around the
    mean
  parent_concepts:
  - Probability distributions
  related_concepts:
  - Power law
  - Log-normal distribution
  abstraction_level: Theoretical
  confidence: 1.0
- name: Power law
  definition: A relationship where a quantity changes in proportion to a power of
    another quantity
  parent_concepts:
  - Mathematical relationships
  related_concepts:
  - Normal distribution
  - Log-normal distribution
  abstraction_level: Theoretical
  confidence: 1.0
- name: Log-normal distribution
  definition: A probability distribution where the logarithm of the data follows a
    normal distribution
  parent_concepts:
  - Probability distributions
  related_concepts:
  - Normal distribution
  - Power law
  abstraction_level: Theoretical
  confidence: 1.0
relationships:
- source_concept: Normal distribution
  target_concept: Log-normal distribution
  relationship_type: derives_from
  strength: 1.0
  evidence: Log-normal distribution is derived from normal distribution by taking
    the logarithm
  reasoning: Mathematical transformation
- source_concept: Power law
  target_concept: Pareto distribution
  relationship_type: equivalent_to
  strength: 1.0
  evidence: Pareto distribution is a type of power law distribution
  reasoning: Definition
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: Economics
  source_concept: Power law
  target_domain: Biology
  target_concept: Species distribution
  insight: Power laws in economics and biology
  explanation: Both economics and biology exhibit power law distributions, where a
    small number of extreme events or individuals dominate the majority. This structural
    similarity can be used to model and predict phenomena in both domains. For example,
    the distribution of city sizes and the distribution of species populations can
    both be described using power laws.
  potential_applications:
  - Modeling population growth
  - Predicting economic trends
  confidence: 0.9
  historical_example: Zipf's law (1949) for city sizes
- connection_type: principle_application
  source_domain: Economics
  source_concept: Normal distribution
  target_domain: Engineering
  target_concept: Quality control
  insight: Applying normal distribution to quality control
  explanation: The normal distribution is widely used in economics to model stock
    prices and returns. Similarly, in engineering, the normal distribution can be
    applied to quality control, where it is used to model the distribution of product
    defects and improve manufacturing processes. This principle can be transferred
    across domains to improve process control and reduce variability.
  potential_applications:
  - Quality control in manufacturing
  - Reliability engineering
  confidence: 0.8
  historical_example: Shewhart's control charts (1931)
- connection_type: metaphor
  source_domain: Economics
  source_concept: Log-normal distribution
  target_domain: Computer Science
  target_concept: Network latency
  insight: Modeling network latency with log-normal distribution
  explanation: The log-normal distribution is often used in economics to model income
    and wealth distributions. Similarly, in computer science, network latency can
    be modeled using a log-normal distribution, where the majority of requests have
    short latency, but a small number of requests have much longer latency. This metaphor
    can be used to improve network performance and optimize system design.
  potential_applications:
  - Network performance optimization
  - System design
  confidence: 0.7
  historical_example: Barford and Crovella's network latency study (1998)
bridge_concepts:
- concept: Scaling
  appears_in_domains:
  - Economics
  - Biology
  - Physics
  role: Describing complex systems
  examples:
  - City growth
  - Species evolution
  - Thermodynamic systems
- concept: Variability
  appears_in_domains:
  - Economics
  - Engineering
  - Computer Science
  role: Modeling uncertainty
  examples:
  - Stock prices
  - Manufacturing defects
  - Network latency
mental_models:
- name: Systems Thinking
  description: Analyzing complex systems as interconnected components
  applied_to:
  - Economic systems
  - Biological systems
  transferable_to:
  - Social systems
  - Environmental systems
- name: First Principles
  description: Breaking down complex systems into fundamental components
  applied_to:
  - Economic models
  - Physical systems
  transferable_to:
  - Biological systems
  - Computer networks
analogies_used:
- source_domain: Physics
  source_concept: Thermodynamic entropy
  target_domain: Economics
  target_concept: Information entropy
  mapping:
    Energy: Information
    Temperature: Uncertainty
  pedagogical_value: Helps understand the concept of information entropy and its applications
    in economics
tags:
  hierarchical:
  - '#Economics → #ProbabilityTheory → #Distributions'
  topical:
  - '#NormalDistribution'
  - '#PowerLaw'
  - '#LogNormalDistribution'
  methodological:
  - '#MathematicalDerivation'
  - '#GameTheory'
  people:
  - '#VilfredoPareto'
  - '#AbrahamDeMoivre'
  concepts:
  - '#NormalDistribution'
  - '#PowerLaw'
  - '#LogNormalDistribution'
  temporal: []
summary: 'Here is a 2-3 sentence summary of the main points:


  The concept of power laws is discussed, where some phenomena in life, such as income
  distribution and earthquake frequencies, do not follow a normal distribution but
  instead exhibit a power law distribution, where extreme events are more likely to
  occur. This is often seen in systems that are in a critical state, where small causes
  can have large effects, and the system is highly unpredictable and sensitive to
  initial conditions. The idea of self-organized criticality is also introduced, where
  systems naturally drive themselves to a critical state, as seen in forest fires,
  where small fires can escalate into massive ones due to the complex interactions
  within the system.'
key_ideas:
- idea: Here are the 3-5 key ideas discussed in the transcription text with a short
    description of each
  description: ''
- idea: Power Laws**
  description: A power law is a relationship between two quantities where one quantity
    changes in a consistent and predictable way as the other quantity changes, often
    resulting in extreme outliers and heavy-tailed distributions.
- idea: Criticality and Self-Organized Criticality**
  description: Criticality refers to a state where a system is poised between order
    and disorder, and self-organized criticality is the phenomenon where a system
    naturally drives itself to this critical state, resulting in power law distributions
    and unpredictable behavior.
- idea: Fractals and Scale-Free Systems**
  description: Fractals are geometric patterns that repeat at different scales, and
    scale-free systems are those that lack a characteristic scale, often exhibiting
    power law distributions and fractal properties, which can be found in natural
    systems such as forest fires, earthquakes, and magnetic materials.
- idea: Unpredictability and Heavy-Tailed Distributions**
  description: Systems that exhibit power laws and criticality can be highly unpredictable,
    with extreme outliers and heavy-tailed distributions, making it difficult to forecast
    their behavior or estimate the likelihood of rare events.
- idea: Real-World Implications**
  description: The concepts of power laws, criticality, and fractals have important
    implications for understanding and managing complex systems, such as forest fires,
    financial markets, and online networks, where rare and extreme events can have
    significant consequences.
---
## Key Concepts

**Normal distribution**  
A probability distribution where most data points cluster around the mean

**Power law**  
A relationship where a quantity changes in proportion to a power of another quantity

**Log-normal distribution**  
A probability distribution where the logarithm of the data follows a normal distribution

## Cross-Domain Connections

**Economics → Biology**

*Power laws in economics and biology*

Both economics and biology exhibit power law distributions, where a small number of extreme events or individuals dominate the majority. This structural similarity can be used to model and predict phenomena in both domains. For example, the distribution of city sizes and the distribution of species populations can both be described using power laws.

**Economics → Engineering**

*Applying normal distribution to quality control*

The normal distribution is widely used in economics to model stock prices and returns. Similarly, in engineering, the normal distribution can be applied to quality control, where it is used to model the distribution of product defects and improve manufacturing processes. This principle can be transferred across domains to improve process control and reduce variability.

**Economics → Computer Science**

*Modeling network latency with log-normal distribution*

The log-normal distribution is often used in economics to model income and wealth distributions. Similarly, in computer science, network latency can be modeled using a log-normal distribution, where the majority of requests have short latency, but a small number of requests have much longer latency. This metaphor can be used to improve network performance and optimize system design.

## Discussion Topics

- **Here are the 3-5 key ideas discussed in the transcription text with a short description of each:** 
- **Power Laws**:** A power law is a relationship between two quantities where one quantity changes in a consistent and predictable way as the other quantity changes, often resulting in extreme outliers and heavy-tailed distributions.
- **Criticality and Self-Organized Criticality**:** Criticality refers to a state where a system is poised between order and disorder, and self-organized criticality is the phenomenon where a system naturally drives itself to this critical state, resulting in power law distributions and unpredictable behavior.
- **Fractals and Scale-Free Systems**:** Fractals are geometric patterns that repeat at different scales, and scale-free systems are those that lack a characteristic scale, often exhibiting power law distributions and fractal properties, which can be found in natural systems such as forest fires, earthquakes, and magnetic materials.
- **Unpredictability and Heavy-Tailed Distributions**:** Systems that exhibit power laws and criticality can be highly unpredictable, with extreme outliers and heavy-tailed distributions, making it difficult to forecast their behavior or estimate the likelihood of rare events.
- **Real-World Implications**:** The concepts of power laws, criticality, and fractals have important implications for understanding and managing complex systems, such as forest fires, financial markets, and online networks, where rare and extreme events can have significant consequences.

## Full Transcription



[ 0m0s36ms - Speaker 1 ] Some things are not normal.
[ 0m3s241ms - Speaker 1 ] By that, I mean, if you go out in the world and start measuring things like human height, IQ, or the size of apples on a tree, you will find that for each of these things, most of the data clusters around some average value.
[ 0m16s31ms - Speaker 1 ] This is so common that we call it the normal distribution.
[ 0m20s511ms - Speaker 1 ] But some things in life are not like this.
[ 0m24s252ms - Speaker 2 ] Nature shows power laws all over the place.
[ 0m26s892ms - Speaker 2 ] That seems weird, like is nature tuning itself to criticality?
[ 0m31s232ms - Speaker 2 ] If you make a crude measure of how big is a World War by how many people it kills, you find that it follows a power law.
[ 0m37s242ms - Speaker 2 ] The outcome will vary in size over 10 million, 100 million.
[ 0m42s422ms - Speaker 2 ] It's a much more likelihood of really big events than you would expect from a normal distribution.
[ 0m47s482ms - Speaker 2 ] And they will totally skew the average.
[ 0m49s862ms - Speaker 2 ] The system you're looking at doesn't have any inherent physical scale.
[ 0m54s252ms - Speaker 2 ] It's really hard to know what's going to happen next.
[ 0m56s272ms - Speaker 2 ] The more you measure, the bigger the average is, which is really weird.
[ 1m0s532ms - Speaker 2 ] It sounds impossible.
[ 1m1s642ms - Speaker 2 ] It's it's very important to try to understand, you know, which game you're playing and what are the payoffs going to be in the in the long run.
[ 1m10s476ms - Speaker 1 ] In the late 1800s, Italian engineer Vilfredo Pareto stumbled upon something no one had seen before.
[ 1m17s186ms - Speaker 1 ] See, he suspected there might be a hidden pattern in how much money people make.
[ 1m21s996ms - Speaker 1 ] So he gathered income tax records from Italy, England, France, and other European countries, and for each country, he plotted the distribution of income.
[ 1m31s656ms - Speaker 1 ] Each country he looked at, he saw the same pattern, a pattern which still holds in most countries to this day.
[ 1m38s996ms - Speaker 1 ] And it's not a normal distribution.
[ 1m41s136ms - Speaker 1 ] If you think about a normal distribution like height, there's a clearly defined average, and extreme outliers basically never happen.
[ 1m48s796ms - Speaker 1 ] I mean, you're never going to find someone who is say, five times the average height.
[ 1m53s296ms - Speaker 1 ] That would be physically impossible.
[ 1m55s216ms - Speaker 1 ] But Pareto's income distributions were different.
[ 1m58s96ms - Speaker 1 ] Take this curve for England.
[ 1m59s336ms - Speaker 1 ] It shows the number of people who earn more than a certain income.
[ 2m3s286ms - Speaker 1 ] The curve starts off declining steeply, most people earn relatively little, but then it falls away gradually, much more slowly than a normal distribution would.
[ 2m12s656ms - Speaker 1 ] And it spans several orders of magnitude.
[ 2m15s866ms - Speaker 1 ] There were people who earned five times, 10 times, even a hundred times more than others.
[ 2m21s116ms - Speaker 1 ] That kind of spread just wouldn't happen if income were normally distributed.
[ 2m25s946ms - Speaker 1 ] Now, to shrink this huge spread of data, Pareto calculated the logarithms of all the values and plotted those instead.
[ 2m32s636ms - Speaker 1 ] In other words, he used a log-log plot.
[ 2m35s166ms - Speaker 1 ] And when he did that, the broad curve transformed into a straight line.
[ 2m39s926ms - Speaker 1 ] The gradient was around -1.5.
[ 2m42s696ms - Speaker 1 ] That means each time you double the income, say from 200 pounds to 400 pounds, the number of people earning at least that amount drops off by a factor of 2 to the power of 1.5, which is around 2.8.
[ 2m55s236ms - Speaker 1 ] And this pattern holds for every doubling of income.
[ 2m58s396ms - Speaker 1 ] So, Pareto could describe the distribution of incomes with one simple equation.
[ 3m2s826ms - Speaker 1 ] The number of people who earn an income greater than or equal to X is proportional to 1/X to the power of 1.5.
[ 3m10s956ms - Speaker 1 ] Now, that's what Pareto saw for England, but he performed the same analysis on data from Italy, France, Prussia, and a bunch of others.
[ 3m19s166ms - Speaker 1 ] And he saw the same thing again and again.
[ 3m22s386ms - Speaker 1 ] Each time the data transformed into a straight line.
[ 3m25s996ms - Speaker 1 ] And the gradients were remarkably similar.
[ 3m28s556ms - Speaker 1 ] That meant Pareto could describe the income distribution in each country with the same equation: one over the income to some power, where that power is just the absolute gradient of the logarithmic graph.
[ 3m42s216ms - Speaker 1 ] This type of relationship is called a power law.
[ 3m45s386ms - Speaker 1 ] When you move from the world of normal distributions to the world of power laws, things change dramatically.
[ 3m51s366ms - Speaker 1 ] So to illustrate this, let's take a trip to the casino to play three different games.
[ 3m57s256ms - Speaker 1 ] At table number one, you get 100 tosses of a coin.
[ 4m1s366ms - Speaker 1 ] Each time you flip and it lands on heads, you win $1.
[ 4m5s146ms - Speaker 1 ] So the question is, how much would you be prepared to pay to play this game?
[ 4m10s46ms - Speaker 1 ] Well, we need to work out how much you'd expect to win in this game and then pay less than that expected value.
[ 4m15s56ms - Speaker 1 ] So the probability of throwing a head is 1/2.
[ 4m18s736ms - Speaker 1 ] Multiply that by $1 and multiply that by 100 tosses.
[ 4m22s226ms - Speaker 1 ] That gives you an expected payout of $50.
[ 4m25s116ms - Speaker 1 ] So you should be willing to pay anything less than $50 to play this game.
[ 4m29s16ms - Speaker 1 ] Sure, you might not win every time, but if you play the game hundreds of times, the small variations either side of the average will cancel out and you can expect to turn a profit.
[ 4m39s86ms - Speaker 1 ] One of the first people to study this kind of problem was Abraham de Moivre in the early 1700s.
[ 4m44s36ms - Speaker 1 ] He showed that if you plot the probability of each outcome, you get a bell-shaped curve, which was later coined the normal distribution.
[ 4m51s536ms - Speaker 2 ] Normal distributions, the traditional explanation, is that when there are a lot of effects that are random that are adding up, that's when you expect normals.
[ 5m0s116ms - Speaker 2 ] So like how tall I am depends on a lot of random things, about my nutrition, about my parents' genetics, all kinds of things.
[ 5m7s246ms - Speaker 2 ] But, but if they if these random effects are additive, that is what tends to lead to normals.
[ 5m14s36ms - Speaker 1 ] At table number two, there's a slightly different game.
[ 5m17s496ms - Speaker 1 ] You still get 100 tosses of the coin, but this time, instead of potentially winning a dollar on each flip, your winnings are multiplied by some factor.
[ 5m27s156ms - Speaker 1 ] So, you start out with $1, and then every time you toss a head, you multiply your winnings by 1.1.
[ 5m34s146ms - Speaker 1 ] If, instead, the coin lands on tails, you multiply your winnings by 0.9.
[ 5m38s846ms - Speaker 1 ] And after 100 tosses, you take home the total, that is the dollar you started with, times the string of 1.1s and 0.9s.
[ 5m46s466ms - Speaker 1 ] So, how much should you pay to play this game?
[ 5m49s726ms - Speaker 1 ] Well, on each flip, your payout can either grow or shrink.
[ 5m53s836ms - Speaker 1 ] And each is equally likely each time you toss the coin.
[ 5m57s266ms - Speaker 1 ] So the expected factor each turn is just 1.1 plus 0.9 divided by 2, which is 1.
[ 6m3s166ms - Speaker 1 ] So, if you start out with $1, then your expected payout is just $1.
[ 6m8s126ms - Speaker 1 ] That means you should be willing to pay anything less than a dollar to play this game, right?
[ 6m13s266ms - Speaker 1 ] Well, if you look at the distribution of payouts, you can see that you could win big.
[ 6m17s856ms - Speaker 1 ] If you tossed 100 heads, you'd win 1.1 to the power of 100.
[ 6m22s196ms - Speaker 1 ] That's almost $14,000.
[ 6m24s446ms - Speaker 1 ] Although the chance of that happening is around 1 in 10 to the power of 30.
[ 6m27s926ms - Speaker 1 ] You'd be more likely to win the lottery three times in a row.
[ 6m30s986ms - Speaker 1 ] On the other hand, the median payout is around 61 cents.
[ 6m34s496ms - Speaker 1 ] So, if you're only playing the game one time and you want even odds of turning a profit, well then you should pay less than 61 cents.
[ 6m42s516ms - Speaker 1 ] Though, either way, if you played the game hundreds of times, your payout would average out to $1.
[ 6m48s176ms - Speaker 1 ] Now, watch what happens if we switch the X-axis from a linear scale to a logarithmic scale.
[ 6m52s896ms - Speaker 1 ] Well then, you see the curve transforms into a normal distribution.
[ 6m56s656ms - Speaker 1 ] That's why this type of distribution is called a log normal distribution.
[ 7m1s16ms - Speaker 2 ] When random effects multiply, if I have a certain wealth, and then my wealth goes up by a certain percentage next year because of my investments, and then the year after that it it changes by another random factor, as opposed to adding, I'm multiplying year after year.
[ 7m17s316ms - Speaker 2 ] If you have a big product of random numbers, when you take the log of a product, that's the sum of the logs.
[ 7m23s616ms - Speaker 2 ] So if so what was a product of random numbers then gets translated into sums of logs of random numbers, and that's what leads to the so-called log normal distribution.
[ 7m34s146ms - Speaker 2 ] And log normal distributions produce big inequalities.
[ 7m38s506ms - Speaker 2 ] You don't just see a mean, you see a mean with a big long tail.
[ 7m42s946ms - Speaker 2 ] It's much more likelihood of really big events, in this case, tremendous wealth being obtained than you would expect from a normal distribution.
[ 7m51s656ms - Speaker 1 ] The reason this curve is so asymmetric is because the downside is capped at zero.
[ 7m55s986ms - Speaker 1 ] So at most you could lose $1.
[ 7m58s906ms - Speaker 1 ] But the upside can keep growing up to nearly $14,000.
[ 8m3s56ms - Speaker 1 ] Now, let's go on to table three.
[ 8m5s46ms - Speaker 1 ] Again, you'll be tossing a coin.
[ 8m7s46ms - Speaker 1 ] But this time, you start out with a dollar, and the payout doubles each time you toss the coin.
[ 8m12s256ms - Speaker 1 ] And you keep tossing until you get a heads.
[ 8m15s46ms - Speaker 1 ] Then the game ends.
[ 8m17s76ms - Speaker 1 ] So, if you get heads on your first toss, you get $2.
[ 8m20s596ms - Speaker 1 ] If you get a tails first and then hit a heads on your second toss, you get $4.
[ 8m24s936ms - Speaker 1 ] If you flipped two tails and then a head on your third toss, you'd get $8, and so on.
[ 8m30s336ms - Speaker 1 ] If it took you to the nth toss to get a heads, you would get $2 to the n.
[ 8m35s446ms - Speaker 1 ] So, how much should you pay to play this game?
[ 8m39s26ms - Speaker 1 ] Well, as in our previous example, we need to work out the expected value.
[ 8m42s486ms - Speaker 1 ] So, suppose you throw a head on your first try.
[ 8m45s386ms - Speaker 1 ] The payout is $2, and the probability of that outcome is a half.
[ 8m49s316ms - Speaker 1 ] So, the expected value of that toss is $1.
[ 8m52s826ms - Speaker 1 ] If it takes you two tosses to get a heads, then the payout is $4, and the probability of that happening is 1/4.
[ 8m59s26ms - Speaker 1 ] So, again, the expected value is $1.
[ 9m2s26ms - Speaker 1 ] We also need to add in the chance that you flip heads on your third try.
[ 9m4s546ms - Speaker 1 ] In that case, the payout is $8, and the probability of that happening is 1/8.
[ 9m10s256ms - Speaker 1 ] So, again, the expected value is $1.
[ 9m13s376ms - Speaker 1 ] And we have to keep repeating this calculation over all possible outcomes.
[ 9m17s96ms - Speaker 1 ] We have to keep adding $1 for each of the different options for flipping the coin, say 10 times until it lands on heads or 100 times before you get heads.
[ 9m25s936ms - Speaker 1 ] I know it's extremely unlikely, but the payout is so huge that the expected value of that outcome is still $1.
[ 9m33s276ms - Speaker 1 ] So, it still increases the expected value of the whole game.
[ 9m37s236ms - Speaker 1 ] This means that theoretically, the total expected value of this game is infinite.
[ 9m44s66ms - Speaker 1 ] This is known as the St. Petersburg Paradox.
[ 9m47s456ms - Speaker 1 ] If you look at the distribution of payouts, you can see it's uncapped.
[ 9m51s366ms - Speaker 1 ] It spans across all orders of magnitude.
[ 9m53s536ms - Speaker 1 ] You could get a payout of $1,000, $100,000, or even a million dollars or more.
[ 9m59s286ms - Speaker 1 ] And while a million dollar payout is unlikely, it's not that unlikely, it's around 1 in a million.
[ 10m6s146ms - Speaker 1 ] Now, if you transform both axes to a log scale, you see a straight line with a gradient of -1.
[ 10m12s246ms - Speaker 1 ] The payout of the St. Petersburg Paradox follows a power law.
[ 10m16s216ms - Speaker 1 ] The specific power law in this case is that the probability of a payout X is equal to X to the power of -1, or 1/X.
[ 10m24s376ms - Speaker 1 ] In the previous games when you have a normal distribution, or even a log normal distribution, you can measure the width of that distribution, its standard deviation.
[ 10m33s206ms - Speaker 1 ] And in a normal distribution, 95% of the data fall within two standard deviations from the mean.
[ 10m38s506ms - Speaker 1 ] But with a power law, like in the St. Petersburg Paradox, there is no measurable width.
[ 10m44s36ms - Speaker 1 ] The standard deviation is infinite.
[ 10m47s36ms - Speaker 1 ] This makes power laws a fundamentally different beast with some very weird properties.
[ 10m52s576ms - Speaker 2 ] Imagine you take a bunch of random samples and then average them, and then take more random samples and average them.
[ 10m58s756ms - Speaker 2 ] You'll find that the average keeps going up.
[ 11m1s526ms - Speaker 2 ] It doesn't converge.
[ 11m3s236ms - Speaker 2 ] And the more you measure, the bigger the average is, which is really weird.
[ 11m7s366ms - Speaker 2 ] It sounds impossible, but it's because it has such a heavy tail, meaning the probability of really whopping big events is so significant that if you keep measuring, occasionally you're going to measure one of those extreme outliers, and they will totally skew the average.
[ 11m24s746ms - Speaker 2 ] It's sort of like saying, you know, if you're standing in a room with Bill Gates or Elon Musk, the average wealth in that room, you know, is going to be 100 billion dollars or something.
[ 11m36s716ms - Speaker 2 ] Because the average is dominated by one outlier.
[ 11m40s276ms - Speaker 1 ] And that same idea, one outlier can dominate the average, shows up online, too.
[ 11m45s316ms - Speaker 1 ] A handful of companies, servers, and data centers hold the personal information of millions of people.
[ 11m50s696ms - Speaker 1 ] So when one of them gets hacked, it can have ripple effects across the whole network.
[ 11m56s656ms - Speaker 1 ] We've had scammers get a hold of email addresses and phone numbers of writers on our team and then send them messages pretending to be me.
[ 12m4s196ms - Speaker 1 ] That is where today's sponsor NordVPN comes in.
[ 12m7s36ms - Speaker 1 ] NordVPN encrypts your internet traffic so your personal data stays private even when the wider system isn't.
[ 12m13s386ms - Speaker 1 ] It protects you from hackers, trackers, and malware with threat protection, even when you're not connected to a VPN.
[ 12m19s396ms - Speaker 1 ] Within just 15 minutes of registering a new email, we saw that five leaks had already been detected.
[ 12m25s456ms - Speaker 1 ] NordVPN lets you browse securely from anywhere in the world by routing your connection through encrypted servers in over 60 countries.
[ 12m32s376ms - Speaker 1 ] You can try it completely risk-free with a 30-day money-back guarantee.
[ 12m36s976ms - Speaker 1 ] Just scan this QR code or go to nordvpn.com/veritasium to get a huge discount on a two-year plan plus four extra months free.
[ 12m45s416ms - Speaker 1 ] That's NordVPN.com/veritasium for a huge discount.
[ 12m49s636ms - Speaker 1 ] I'll put the link down in the description.
[ 12m50s876ms - Speaker 1 ] I'd like to thank NordVPN for sponsoring this video, and now back to power laws.
[ 12m56s631ms - Speaker 1 ] So, why do you get a power law from the simple St. Petersburg setup?
[ 13m2s181ms - Speaker 1 ] If you look at the payout X, you can see it grows exponentially with each toss of the coin.
[ 13m7s331ms - Speaker 1 ] X equals 2 to the n.
[ 13m9s211ms - Speaker 1 ] But if you look at the probability of tossing the coin that many times to get a heads, you can see that this probability shrinks exponentially.
[ 13m18s21ms - Speaker 1 ] So, the probability of flipping a coin n times is 1/2 to the power of n.
[ 13m22s391ms - Speaker 1 ] But we're not really interested in the number of tosses, we're interested in the payout.
[ 13m26s621ms - Speaker 1 ] Now, we know that X equals 2 to the n, so instead of writing 2 to the n in our probability equation, we can just write X.
[ 13m32s831ms - Speaker 1 ] So, we end up with this.
[ 13m34s141ms - Speaker 1 ] The probability of a payout of X dollars is equal to 1/X, or in other words, X to the power of -1.
[ 13m42s371ms - Speaker 2 ] You put them together, the exponentials conspire to make a power law.
[ 13m47s481ms - Speaker 2 ] And that's a very common thing in nature, that a lot of times when we see power laws, there are two underlying exponentials that are dancing together to make a power law.
[ 13m57s771ms - Speaker 1 ] One example of this is earthquakes.
[ 13m59s471ms - Speaker 1 ] If you look at data on earthquakes, you find that small earthquakes are very common, but earthquakes of increasing magnitudes become exponentially rarer.
[ 14m9s11ms - Speaker 1 ] The destruction that earthquakes cause is not proportional to their magnitude, it's proportional to the energy they release.
[ 14m14s641ms - Speaker 1 ] And as earthquakes grow in magnitude, that energy grows exponentially.
[ 14m20s41ms - Speaker 2 ] So, there's this exponential decay in frequency of earthquakes of a given magnitude, and an exponential increase in the amount of energy released by earthquakes of a certain magnitude.
[ 14m32s21ms - Speaker 2 ] So, when you combine those two exponentials to eliminate the magnitude, what you find is a power law.
[ 14m38s691ms - Speaker 1 ] But power laws also reveal something deeper about the underlying structure of a system.
[ 14m42s841ms - Speaker 1 ] To see this in action, let's go back to the third coin game and the St. Petersburg Paradox.
[ 14m48s171ms - Speaker 1 ] Now, you can draw all the different outcomes as a tree diagram, where the length of each branch is equal to its probability.
[ 14m54s661ms - Speaker 1 ] So, starting with a single line of length 1, and then a half for the first two branches, a quarter for the next four, and so on.
[ 15m1s481ms - Speaker 1 ] Now, when you zoom in, you keep seeing the same structure repeating at smaller and smaller scales.
[ 15m7s221ms - Speaker 1 ] It's self-similar, like a fractal.
[ 15m10s41ms - Speaker 1 ] And that's no coincidence.
[ 15m11s951ms - Speaker 1 ] We see the same fractal-like pattern in the veins on a leaf, river networks, the blood vessels in our lungs, even lightning.
[ 15m19s231ms - Speaker 1 ] And in all of these cases, we can describe the pattern with a power law.
[ 15m24s11ms - Speaker 1 ] Power laws and fractals are intrinsically linked.
[ 15m26s701ms - Speaker 1 ] That's because power laws reveal something fundamental about a system's structure.
[ 15m31s981ms - Speaker 3 ] So, I've got a magnet, and I've got a screw.
[ 15m34s141ms - Speaker 3 ] And you'll notice if I bring them close together, then the screw gets attracted to the magnet.
[ 15m38s641ms - Speaker 3 ] And that's because there's a lot of iron in it, which is ferromagnetic.
[ 15m42s681ms - Speaker 3 ] But watch what happens if I start heating this up.
[ 15m46s761ms - Speaker 3 ] Trying to, oh!
[ 15m48s771ms - Speaker 3 ] You see that?
[ 15m49s31ms - Speaker 3 ] Oh, there it went.
[ 15m49s781ms - Speaker 3 ] There it went.
[ 15m51s231ms - Speaker 3 ] You see, you heat it up and suddenly it becomes non-magnetic.
[ 15m54s511ms - Speaker 3 ] To find out what happened, let's zoom in on this magnet.
[ 15m57s871ms - Speaker 1 ] Inside a magnet, each atom has its own magnetic moment, which means you can think of it like its own little magnet or compass.
[ 16m4s491ms - Speaker 1 ] If one atom's moment points up, its neighbors tend to point that way too, since this lowers the system's overall potential energy.
[ 16m11s291ms - Speaker 1 ] Therefore, at low temperatures, you get large regions called domains where all the moments align.
[ 16m17s221ms - Speaker 1 ] And when many of these domains also align, their individual magnetic fields reinforce to create an overall field around the magnet.
[ 16m25s71ms - Speaker 1 ] But if you heat up the magnet, each atom starts vibrating vigorously.
[ 16m29s151ms - Speaker 1 ] The moments flip up and down, and so the alignment can break down.
[ 16m33s491ms - Speaker 1 ] And when all the moments cancel out, then there's no longer a net magnetic field.
[ 16m38s501ms - Speaker 1 ] Now, if you have the right equipment, you can balance any magnetic material right on that transition point, right between magnetic and non-magnetic.
[ 16m47s321ms - Speaker 1 ] This is called the critical point, and it occurs at a specific temperature called the Curie temperature.
[ 16m53s531ms - Speaker 1 ] I asked Casper and the team to build a simulation to show what's going on inside the magnet at this critical point.
[ 17m0s31ms - Speaker 4 ] Each pixel represents the magnetic moment of an individual atom.
[ 17m4s331ms - Speaker 4 ] Let's say red is up and blue is down.
[ 17m7s121ms - Speaker 4 ] Now, when the temperature is low, we get these big domains, where the magnetic moments are all aligned, and you get an overall magnetic field.
[ 17m15s151ms - Speaker 4 ] But if we really crank up the temperature, then all of these moments start flipping up and down, and so they cancel out, and the magnet loses its magnetism.
[ 17m23s811ms - Speaker 4 ] So, that's exactly what happened in our demo.
[ 17m26s701ms - Speaker 4 ] But if we tune the temperature just right, right to that Curie temperature, then the pattern becomes way more interesting.
[ 17m34s531ms - Speaker 1 ] That looks like a map.
[ 17m36s221ms - Speaker 1 ] Like a map?
[ 17m38s141ms - Speaker 1 ] Yeah, it almost looks like the Mediterranean or something.
[ 17m40s791ms - Speaker 1 ] It's almost stable.
[ 17m43s721ms - Speaker 1 ] Like atoms that are pointing one way tend to point that way for a while, but there is clearly fluctuations as well.
[ 17m53s861ms - Speaker 1 ] So domains are constantly coming and going.
[ 17m56s651ms - Speaker 1 ] It's both got some elements of stability, and some persistence over time, some features which are consistent, but it's also not locked in place, because you notice changes over time.
[ 18m12s251ms - Speaker 4 ] If you zoom in, you find that the same kinds of patterns repeat at all scales.
[ 18m16s341ms - Speaker 4 ] You've got domains of tens of atoms, hundreds, thousands, even millions.
[ 18m20s351ms - Speaker 4 ] There's just no inherent scale to the system, that is, it's scale-free.
[ 18m24s781ms - Speaker 4 ] It's just like a fractal.
[ 18m26s161ms - Speaker 4 ] And if you plot the size distribution of the domains, you get a power law.
[ 18m32s161ms - Speaker 2 ] The underlying geometry suddenly shows a fractal character that it doesn't have on either side of the phase transition.
[ 18m38s221ms - Speaker 2 ] Right at the phase transition you get fractal behavior, and that pops out as a power law.
[ 18m43s611ms - Speaker 1 ] In fact, whenever you find a power law, that indicates you're dealing with a system that has no intrinsic scale.
[ 18m49s861ms - Speaker 1 ] And that is a signature of a system in a critical state, which turns out has huge consequences.
[ 18m56s891ms - Speaker 4 ] See, normally in a magnet below the Curie temperature, each atom influences only its neighbors.
[ 19m2s221ms - Speaker 4 ] If one atom's magnetic moment flips up, then that means that its neighbors are slightly more likely to point up too.
[ 19m7s581ms - Speaker 4 ] But that influence is local.
[ 19m9s11ms - Speaker 4 ] It dies out just a few atoms away.
[ 19m11s161ms - Speaker 4 ] But as the magnet approaches its critical temperature, those local influences start to chain together.
[ 19m16s91ms - Speaker 4 ] One spin nudges its neighbor, and that neighbor nudges the next, and so on, like a rumor spreading through a crowd.
[ 19m22s751ms - Speaker 4 ] And the result is that the effective range of influence keeps expanding, and right at the critical point, it becomes effectively infinite.
[ 19m30s301ms - Speaker 4 ] A flip on one side can cascade throughout the entire material.
[ 19m35s361ms - Speaker 4 ] So, you get these small causes, just a single flip to reverberate throughout the entire system.
[ 19m41s131ms - Speaker 2 ] And it gets right into that that point where the system is maximally unstable.
[ 19m48s171ms - Speaker 2 ] Anything can happen.
[ 19m49s221ms - Speaker 2 ] It's also maximally interesting in a way.
[ 19m51s341ms - Speaker 2 ] It's it means the system is most unpredictable, most uncertain.
[ 19m56s651ms - Speaker 2 ] It's really hard to know what's going to happen next.
[ 19m58s301ms - Speaker 2 ] And that seems to be a natural procedure that happens in many different systems in the world.
[ 20m3s251ms - Speaker 1 ] One such system is forest fires.
[ 20m7s271ms - Speaker 1 ] In June 1988, a lightning strike started a small fire near Yellowstone National Park.
[ 20m12s31ms - Speaker 1 ] This was nothing out of the ordinary.
[ 20m14s351ms - Speaker 1 ] Each year Yellowstone experiences thousands of lightning strikes.
[ 20m17s71ms - Speaker 1 ] Most don't cause fires, and those that do tend to burn a few trees, maybe even a few acres before they fizzle out.
[ 20m24s141ms - Speaker 1 ] Three quarters of fires burn less than a quarter of an acre.
[ 20m28s171ms - Speaker 1 ] The largest fire in the park's recent history occurred in 1931.
[ 20m32s301ms - Speaker 1 ] That burned through 18,000 acres, an area slightly larger than Manhattan.
[ 20m37s181ms - Speaker 1 ] But the 1988 fire was different.
[ 20m39s261ms - Speaker 1 ] That initial spark spread, slowly at first, covering several thousand acres, then over the next couple of months it merged with other small fires to create an enormous complex of megafires that blazed across 1.4 million acres of land.
[ 20m54s501ms - Speaker 1 ] That's around the size of the entire state of Delaware.
[ 20m58s201ms - Speaker 1 ] That's 70 times bigger than the previous record and 50 times the area of all the fires over the previous 15 years combined.
[ 21m7s251ms - Speaker 1 ] So, what was so special about the 1988 fires?
[ 21m10s391ms - Speaker 1 ] Well, to find out, we made a forest fire simulator.
[ 21m13s961ms - Speaker 4 ] We've got a grid of squares, and on each square, either a tree could be there, it could grow, or it could not be there.
[ 21m21s301ms - Speaker 4 ] There's going to be some probability for lightning strikes, so, you know, the higher the probability, the more fires we're going to have.
[ 21m27s661ms - Speaker 4 ] We can run this.
[ 21m29s411ms - Speaker 1 ] So, trees are growing.
[ 21m31s211ms - Speaker 4 ] Trees are growing.
[ 21m32s31ms - Speaker 1 ] Forest is filling in.
[ 21m35s31ms - Speaker 1 ] Nice.
[ 21m36s121ms - Speaker 1 ] Getting pretty dense.
[ 21m37s921ms - Speaker 4 ] What do you expect is going to happen?
[ 21m39s701ms - Speaker 1 ] I expect to see some fires.
[ 21m43s461ms - Speaker 1 ] Probably, you know, now that, oh!
[ 21m46s431ms - Speaker 1 ] That was good.
[ 21m46s841ms - Speaker 1 ] That was a good little fire.
[ 21m49s21ms - Speaker 1 ] Whoa!
[ 21m52s111ms - Speaker 1 ] Whoa!
[ 21m54s531ms - Speaker 1 ] No way.
[ 21m57s161ms - Speaker 1 ] Oh, that's crazy.
[ 21m59s201ms - Speaker 1 ] You haven't adjusted the parameters, right?
[ 22m0s771ms - Speaker 1 ] It's just like,
[ 22m1s711ms - Speaker 4 ] Not yet.
[ 22m2s141ms - Speaker 4 ] Not yet.
[ 22m2s751ms - Speaker 1 ] This seems like a very critical situation just by itself.
[ 22m7s431ms - Speaker 1 ] I say that because of how big that fire was.
[ 22m9s991ms - Speaker 4 ] This sort of system will tune itself to criticality.
[ 22m14s351ms - Speaker 4 ] And you can, you can see it start to happen.
[ 22m15s781ms - Speaker 4 ] So right now, I think is a good moment where you have basically domains of a lot of different sizes.
[ 22m21s561ms - Speaker 4 ] And then one way to think about it is if some of these domains become too big, then you get a single fire, like that one, perfectly timed, burns them all up.
[ 22m31s141ms - Speaker 4 ] It's just going to propagate throughout the whole thing and burn it back down a little.
[ 22m34s321ms - Speaker 4 ] But then if it goes too hard, then now you've got all these domains where there are no trees, and so it's going to, you know, grow again to bring it back to that critical state.
[ 22m42s311ms - Speaker 1 ] I can see how it's the feedback mechanism, right?
[ 22m45s181ms - Speaker 1 ] That the fire gets rid of all the trees, and then there's nothing left to burn, and then that has to fill in again.
[ 22m51s321ms - Speaker 4 ] Yeah.
[ 22m52s71ms - Speaker 1 ] Yeah, but if there hasn't been a fire, then the forest gets too thick, and then it's ripe for this sort of massive fire.
[ 23m0s241ms - Speaker 4 ] For a magnet, you have to painstakingly tune it to the critical point, but the forest naturally drives itself there.
[ 23m6s911ms - Speaker 4 ] This phenomenon is called self-organized criticality.
[ 23m10s21ms - Speaker 4 ] Yeah, and if you let it run, what you get is, again, a power law distribution.
[ 23m15s151ms - Speaker 4 ] So this is log-log.
[ 23m16s81ms - Speaker 4 ] So it should be a straight line.
[ 23m18s311ms - Speaker 2 ] That kind of stuff seems so totally random and unpredictable, and it is in one way, and yet it follows a pattern.
[ 23m26s31ms - Speaker 2 ] There's a consistent mathematical pattern to all these kind of disasters.
[ 23m31s471ms - Speaker 2 ] It's it's shocking.
[ 23m33s271ms - Speaker 1 ] Is there something fractal about this?
[ 23m36s271ms - Speaker 4 ] Mostly in terms of the, I guess, domains of the trees when you're at that critical state.
[ 23m42s371ms - Speaker 4 ] So you get very dense areas, you get non-dense areas.
[ 23m45s731ms - Speaker 4 ] And as a result, when a single lightning bolt strikes, you can get fires of all sizes.
[ 23m50s561ms - Speaker 4 ] Most often, you get small fires of 10 or fewer trees burning.
[ 23m54s161ms - Speaker 4 ] A little less frequently, you get fires of less than 100 trees.
[ 23m57s711ms - Speaker 4 ] And then, every once in a while, you get these massive fires that reverberate throughout the entire system.
[ 24m4s41ms - Speaker 4 ] Now, you might expect that because the fire is so large, there has to be a significant event causing it.
[ 24m9s621ms - Speaker 4 ] But that's not the case, because the cause for each fire is the exact same.
[ 24m13s551ms - Speaker 4 ] It's a single lightning strike.
[ 24m15s891ms - Speaker 4 ] The only difference is where it strikes and the exact makeup of the forest at that time.
[ 24m21s311ms - Speaker 4 ] So, in some very real way, the large fires are nothing more than magnified versions of the small ones.
[ 24m27s251ms - Speaker 4 ] And even worse, they're inevitable.
[ 24m29s71ms - Speaker 4 ] So, what we've learned is that for systems in a critical state, there are no special events causing the massive fires.
[ 24m35s611ms - Speaker 4 ] There was nothing special about the Yellowstone fire.
[ 24m39s161ms - Speaker 1 ] In 1935, the US Forest Service established the so-called 10:00 a.m. policy.
[ 24m43s861ms - Speaker 1 ] The plan was to suppress every single fire by 10:00 a.m. on the day following its initial report.
[ 24m49s21ms - Speaker 1 ] Now, naively, this strategy makes sense.
[ 24m52s171ms - Speaker 1 ] I mean, if you keep all fires under strict control, then none can ever get out of hand.
[ 24m57s11ms - Speaker 1 ] But it turns out this strategy is extremely counter-intuitive.