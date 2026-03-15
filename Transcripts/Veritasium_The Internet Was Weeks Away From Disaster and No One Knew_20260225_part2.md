---
title: Veritasium_The Internet Was Weeks Away From Disaster and No One Knew_20260225_part2
audio_file: Veritasium_The Internet Was Weeks Away From Disaster and No One Knew_20260225_part2.mp3
note_id: 329e2f04-44d1-452a-bae9-42a8e1f822cf
date_processed: '2026-03-08'
classification:
  primary_domain: Computer Science
  sub_domains:
  - Cybersecurity
  - Linux
  - Networking
  difficulty_level: Advanced
  content_type: Explainer
entities:
  people:
  - name: Gia
    role: Hacker
    contribution: Created a backdoor in XZ compression software
  - name: Richard Fearn
    role: Developer
    contribution: Received messages from Gia about updating XZ in Fedora
  works_cited: []
  concepts_mentioned:
  - Backdoor
  - XZ compression
  - Linux
  - SSH
  - RSA authentication
  laws_theories_cited: []
concepts:
- name: Backdoor
  definition: A secret entry point in a computer system that allows unauthorized access
  parent_concepts:
  - Cybersecurity
  related_concepts:
  - Vulnerability
  - Exploit
  abstraction_level: Theoretical
  confidence: 0.9
- name: XZ compression
  definition: A lossless data compression format
  parent_concepts:
  - Data compression
  related_concepts:
  - Compression algorithm
  - Data encoding
  abstraction_level: Theoretical
  confidence: 0.9
- name: SSH
  definition: A secure network protocol for remote access
  parent_concepts:
  - Networking
  related_concepts:
  - Remote access
  - Network security
  abstraction_level: Theoretical
  confidence: 0.9
- name: RSA authentication
  definition: A method of verifying identity using RSA encryption
  parent_concepts:
  - Cryptography
  related_concepts:
  - Encryption
  - Authentication
  abstraction_level: Theoretical
  confidence: 0.9
relationships:
- source_concept: Backdoor
  target_concept: XZ compression
  relationship_type: exploits
  strength: 0.9
  evidence: Gia created a backdoor in XZ compression software
  reasoning: The backdoor is hidden in the XZ compression software
- source_concept: SSH
  target_concept: RSA authentication
  relationship_type: uses
  strength: 0.9
  evidence: SSH uses RSA authentication for secure access
  reasoning: SSH relies on RSA authentication for secure connections
cross_domain_insights:
- connection_type: structural_analogy
  source_domain: Computer Science
  source_concept: Backdoor
  target_domain: Biology
  target_concept: Trojan horse cells
  insight: Both involve covert entry mechanisms
  explanation: In computer science, a backdoor refers to a secret entry point in a
    system's security. Similarly, in biology, Trojan horse cells can be used to deliver
    therapeutic agents or genes into cells, bypassing the cell's natural defenses.
    This structural analogy highlights the concept of exploiting vulnerabilities for
    entry, whether in digital systems or biological ones.
  potential_applications:
  - Biological security measures
  - Intracellular delivery systems
  confidence: 0.8
  historical_example: The concept of a 'Trojan horse' originates from ancient Greek
    history, where a wooden horse was used to infiltrate the city of Troy.
- connection_type: principle_application
  source_domain: Computer Science
  source_concept: XZ compression
  target_domain: Signal Processing
  target_concept: Lossless data compression
  insight: Applying compression principles to signal processing
  explanation: The principles of XZ compression, such as using a combination of LZ77
    and Huffman coding, can be applied to lossless data compression in signal processing.
    This involves reducing the amount of data required to represent a signal, while
    preserving its original information content.
  potential_applications:
  - Audio compression
  - Image compression
  confidence: 0.9
  historical_example: The development of MP3 compression algorithms was influenced
    by earlier work on lossless compression techniques.
- connection_type: metaphor
  source_domain: Computer Science
  source_concept: SSH
  target_domain: Economics
  target_concept: Secure transactions
  insight: Secure transactions as a 'secure shell' for financial exchanges
  explanation: Just as SSH provides a secure, encrypted connection for remote access,
    secure transactions in economics can be thought of as a 'secure shell' for financial
    exchanges. This metaphor highlights the importance of trust and security in facilitating
    reliable transactions.
  potential_applications:
  - Digital payment systems
  - Cryptocurrencies
  confidence: 0.7
  historical_example: The development of HTTPS protocol for secure web transactions
    was influenced by earlier work on SSH.
- connection_type: historical_precedent
  source_domain: Computer Science
  source_concept: RSA authentication
  target_domain: Cryptography
  target_concept: Public-key cryptography
  insight: Public-key cryptography as a historical precedent for RSA authentication
  explanation: The development of RSA authentication was influenced by earlier work
    on public-key cryptography, which dates back to the 1970s. This historical precedent
    highlights the evolution of cryptographic techniques and their application to
    secure authentication protocols.
  potential_applications:
  - Secure online transactions
  - Digital signatures
  confidence: 0.9
  historical_example: The Diffie-Hellman key exchange, developed in 1976, laid the
    foundation for public-key cryptography and later RSA authentication.
bridge_concepts:
- concept: Compression
  appears_in_domains:
  - Computer Science
  - Signal Processing
  - Data Storage
  role: Reducing data size while preserving information
  examples:
  - XZ compression in computer science
  - Lossless data compression in signal processing
  - Data compression in data storage
- concept: Security
  appears_in_domains:
  - Computer Science
  - Economics
  - Cryptography
  role: Protecting against unauthorized access or tampering
  examples:
  - SSH in computer science
  - Secure transactions in economics
  - Public-key cryptography in cryptography
mental_models:
- name: Systems Thinking
  description: Analyzing complex systems as interconnected components
  applied_to:
  - Understanding the impact of XZ compression on system performance
  transferable_to:
  - Analyzing economic systems
  - Modeling biological systems
- name: First Principles
  description: Breaking down complex systems to their fundamental components
  applied_to:
  - Designing RSA authentication protocols
  transferable_to:
  - Understanding the fundamentals of public-key cryptography
  - Analyzing the security of digital payment systems
analogies_used:
- source_domain: Computer Science
  source_concept: Firewall
  target_domain: Biology
  target_concept: Cell membrane
  mapping:
    Incoming traffic: Substances entering the cell
    Blocked traffic: Substances rejected by the cell membrane
  pedagogical_value: Helps understand the concept of selective permeability in cell
    biology
tags:
  hierarchical:
  - '#Computer Science → #Cybersecurity → #Backdoors'
  topical:
  - '#Cybersecurity'
  - '#Linux'
  - '#Networking'
  methodological:
  - '#Exploitation'
  - '#Vulnerability assessment'
  people:
  - '#Gia'
  - '#Richard Fearn'
  concepts:
  - '#Backdoor'
  - '#XZ compression'
  - '#SSH'
  - '#RSA authentication'
  temporal: []
summary: 'Here is a concise summary of the main points in 2-3 sentences:


  A sophisticated hacker, known as Gia Tan, spent two and a half years infiltrating
  the XZ compression project and created a meticulous backdoor that could have given
  him access to millions of systems, including those used by governments and hospitals.
  The backdoor was discovered by a German programmer, Andres Freund, who noticed a
  small slowdown in connection times and dug deeper to uncover the truth, prompting
  a widespread response from the open-source community to patch the vulnerability.
  The true identity of Gia Tan and the motivations behind the attack remain unknown,
  but experts speculate that it may have been a nation-state actor, highlighting the
  need for increased vigilance against sophisticated cyber threats.'
key_ideas:
- idea: Here are the 3-5 key ideas discussed in the transcription text with a short
    description for each
  description: ''
- idea: The XZ backdoor exploit**
  description: A sophisticated backdoor exploit was inserted into the XZ compression
    library, allowing an attacker to gain control of any machine that installs the
    compromised library, with the goal of creating a master key to access secure systems.
- idea: The complexity of the exploit**
  description: The backdoor was carefully designed to avoid detection, using techniques
    such as binary blobs, IFUNC resolvers, and custom encryption, making it difficult
    to identify and requiring a meticulous approach to uncover.
- idea: The discovery and response**
  description: The exploit was discovered by a German programmer, Andres Freund, who
    noticed a slowdown in the server connection times and dug deeper to uncover the
    backdoor, leading to a rapid response from the open-source community to roll back
    the affected libraries and investigate the incident.
- idea: The potential impact and attribution**
  description: The exploit had the potential to compromise millions of systems, allowing
    for spying, ransomware, or taking down entire countries, and while the attribution
    of the attack is unclear, experts speculate that it may be the work of a nation-state
    actor, such as Russia or China.
- idea: The implications for the open-source community**
  description: The XZ backdoor exploit highlights the need for the open-source community
    to be more vigilant and prepared for sophisticated attacks, as the gloves are
    off and attackers are becoming more sophisticated, making it essential to protect
    against these types of backdoors regardless of their origin.
---
## Key Concepts

**Backdoor**  
A secret entry point in a computer system that allows unauthorized access

**XZ compression**  
A lossless data compression format

**SSH**  
A secure network protocol for remote access

**RSA authentication**  
A method of verifying identity using RSA encryption

## Cross-Domain Connections

**Computer Science → Biology**

*Both involve covert entry mechanisms*

In computer science, a backdoor refers to a secret entry point in a system's security. Similarly, in biology, Trojan horse cells can be used to deliver therapeutic agents or genes into cells, bypassing the cell's natural defenses. This structural analogy highlights the concept of exploiting vulnerabilities for entry, whether in digital systems or biological ones.

**Computer Science → Signal Processing**

*Applying compression principles to signal processing*

The principles of XZ compression, such as using a combination of LZ77 and Huffman coding, can be applied to lossless data compression in signal processing. This involves reducing the amount of data required to represent a signal, while preserving its original information content.

**Computer Science → Economics**

*Secure transactions as a 'secure shell' for financial exchanges*

Just as SSH provides a secure, encrypted connection for remote access, secure transactions in economics can be thought of as a 'secure shell' for financial exchanges. This metaphor highlights the importance of trust and security in facilitating reliable transactions.

## Discussion Topics

- **Here are the 3-5 key ideas discussed in the transcription text with a short description for each:** 
- **The XZ backdoor exploit**:** A sophisticated backdoor exploit was inserted into the XZ compression library, allowing an attacker to gain control of any machine that installs the compromised library, with the goal of creating a master key to access secure systems.
- **The complexity of the exploit**:** The backdoor was carefully designed to avoid detection, using techniques such as binary blobs, IFUNC resolvers, and custom encryption, making it difficult to identify and requiring a meticulous approach to uncover.
- **The discovery and response**:** The exploit was discovered by a German programmer, Andres Freund, who noticed a slowdown in the server connection times and dug deeper to uncover the backdoor, leading to a rapid response from the open-source community to roll back the affected libraries and investigate the incident.
- **The potential impact and attribution**:** The exploit had the potential to compromise millions of systems, allowing for spying, ransomware, or taking down entire countries, and while the attribution of the attack is unclear, experts speculate that it may be the work of a nation-state actor, such as Russia or China.
- **The implications for the open-source community**:** The XZ backdoor exploit highlights the need for the open-source community to be more vigilant and prepared for sophisticated attacks, as the gloves are off and attackers are becoming more sophisticated, making it essential to protect against these types of backdoors regardless of their origin.

## Full Transcription



00:00 - 00:05 **Speaker 1**: works even when you're not connected to the VPN. So, a lot of these attacks never get the chance to start in the first place.
00:05 - 00:15 **Speaker 1**: I use NordVPN whenever I'm traveling or working on public Wi-Fi because it means that I don't have to think about who's running the network.
00:15 - 00:30 **Speaker 1**: It's just one click, and it's so fast that I often forget that it's on. Not just that, if there's a show that's no longer available in my region or a sports team that's blacked out, like I'm often watching international football and they don't quite have it where I'm going,
00:30 - 00:40 **Speaker 1**: Well, in that case, I can just switch my server location with one click to unlock the content. Apparently, you can even use it to find better deals on plane tickets by changing your IP address to another country.
00:40 - 01:01 **Speaker 1**: I haven't tried it yet, but that sounds fascinating. So, if you want to try it, you can get the best deal by going to NordVPN.com/veritasium. When you use that link or this QR code, you'll get a huge discount. Also, you get a 30-day money-back guarantee through Nord, so it's a no-brainer.
01:01 - 01:10 **Speaker 1**: So, again, that's NordVPN.com/veritasium, or you can click the link in the description below. Thanks so much to Nord, and let's get back to Gia and the prize he's got his eyes on.
01:10 - 01:13 **Richard Fearn**: At this point, we were preparing RHEL 10.
01:13 - 01:23 **Speaker 1**: See, Red Hat ships two major flavors of Linux: Fedora, which is free and publicly available, and Red Hat Enterprise Linux, or RHEL, which is available through a paid subscription.
01:23 - 01:34 **Speaker 1**: This one has to be stable and secure because it's widely used on the most important machines, like in governments and hospitals. Gia wants his code in RHEL, but RHEL only has a new major release about once every three years.
01:34 - 01:39 **Richard Fearn**: So, there's definitely a deadline. That deadline was around sort of March, April in 2024.
01:39 - 01:46 **Speaker 1**: Gia has to act fast. He wants complete control of any compromised machine, and to pull it off, he has three steps in his plan.
01:46 - 01:49 **Speaker 1**: Step one: the Trojan Horse.
01:49 - 02:00 **Speaker 1**: The code for XZ lives on a website called GitHub, which tracks all edits to XZ's code using a tool called Git, which was also developed by Linus Torvalds.
02:00 - 02:11 **Speaker 1**: So, Gia starts by making small changes. He changes the primary contact for bug reports to his own email. He tweaks small tools that will help him later.
02:11 - 02:20 **Speaker 1**: But he can't sneak in the payload this way. I mean, it'd be too obvious. So, he needs a way to sneak it in without it ever appearing as normal source code on GitHub.
02:20 - 02:32 **Richard Fearn**: So, when you're writing compression software, it's very often the case that your software is full of these binary blobs, as we call them, so just lumps of binary which are used to test the compression or decompression is still working.
02:32 - 02:44 **Speaker 1**: Nobody reads these test blobs. They're included without ever appearing in the human-readable source code. They're assumed to be garbage data. But for Gia, this is the perfect place to hide his payload.
02:44 - 02:56 **Speaker 1**: Inside something that at first glance looks harmless. But in reality, it's a Trojan Horse. But with the Trojan Horse inside of XZ, it's still just a lump of data in a binary blob. He has to unpack it.
02:56 - 03:09 **Speaker 1**: So, in the code that builds the project, he slips in a small, easy-to-miss change. It hides among all the automatically generated code and quietly unpacks his payload, inserting it into the XZ library.
03:09 - 03:18 **Speaker 1**: But now that it's inside of XZ, it still has to pick the right time to act. On to step two: Goldilocks.
03:18 - 03:29 **Speaker 1**: Gia's end goal is to compromise a very specific part of the SSH connection process: the RSA authentication step.
03:29 - 03:41 **Speaker 1**: He realizes that if he can slip a small malicious component in there—let's call it the payload—then every time SSH checks for a key, his code will run first. It will quietly look for a special master key that only he knows, and if it sees that key, it'll let him straight in.
03:41 - 03:52 **Speaker 1**: If it doesn't, it'll call the real code and no one's the wiser. So, he will have his backdoor entrance to open SSH. But he can't just go in and rewrite RSA decrypt, the function that verifies a client's identity during the login. It's not that easy.
03:52 - 04:02 **Speaker 1**: See, when you build an application, you could take all the code you need from different libraries and bundle it into your application. But there's a big drawback to this approach.
04:02 - 04:13 **Speaker 1**: If 10 different applications on a system all bundle the same library, you end up with 10 separate copies on your machine. So, it's redundant. That's why modern systems mostly use shared libraries.
04:13 - 04:24 **Speaker 1**: When an application starts, the linker fills in a table of addresses. These addresses point to the functions and variables it needs from the libraries it links to. That table is called the Global Offset Table, or GOT.
04:24 - 04:34 **Speaker 1**: Now, when it wants to use something from a shared library, it just checks the GOT and jumps to the right spot in memory. RSA decrypt doesn't belong to OpenSSH at all. It comes from a shared crypto library.
04:34 - 04:45 **Speaker 1**: So, to hijack authentication, Gia can overwrite the GOT entry that tells SSH where it is. And to do that, he can use a little-known tool called an IFUNC resolver.
04:45 - 04:57 **Richard Fearn**: IFUNC is used where, let's say you want to optimize your code to run on Intel's hardware and AMD's hardware. Now, you could write the software just for Intel, and it would run very fast on Intel, and it probably would run very badly on AMD hardware.
04:57 - 05:08 **Richard Fearn**: Instead, you keep multiple versions of the same function, and the IFUNC resolver picks the right one for the hardware you're on. At first glance, that sounds like a way for Gia to trick the system into thinking it's running hardware that needs its own compromised version of RSA decrypt.
05:08 - 05:22 **Richard Fearn**: But there is a catch. A library can only define IFUNC resolvers for its own functions. And since RSA decrypt doesn't belong to XZ, it can't use an IFUNC resolver to overwrite it. But IFUNC can still help him.
05:22 - 05:35 **Richard Fearn**: So, it will very, very early on in the running of the program, it will do this sort of determination of what hardware is available. And crucially, it does let you run your own code in the library very early on.
05:35 - 05:46 **Speaker 1**: Now, at this early stage, from within an IFUNC resolver, Gia could try to directly rewrite the GOT entry for RSA decrypt. But at this point, the system is still filling in the GOT.
05:46 - 05:58 **Speaker 1**: So, even if Gia changes the RSA decrypt slot, the loader will come along later and write the real address back in, wiping out his change. And there's a limit on the other side as well.
05:58 - 06:10 **Speaker 1**: To make this sort of hijacking harder, once every entry is filled in the GOT, the system marks the table read-only. That means that if Gia waits too long, the RSA decrypt entry is frozen.
06:10 - 06:21 **Speaker 1**: So, he has to slip it in at a very precise moment. After the RSA decrypt entry is filled in legitimately, but before the table gets marked read-only. And that tiny window is the Goldilocks zone.
06:21 - 06:25 **Speaker 1**: And to hit it, he's going to need another tool.
06:25 - 06:36 **Speaker 1**: Linking shared libraries in the GOT often leads to bugs. So, Linux has a special debugging feature that tracks what the system's doing. It lets you run code whenever the linker writes a symbol's address into the GOT.
06:36 - 06:48 **Speaker 1**: It's called a dynamic audit hook. And normally, you'd use it to profile performance. But crucially for Gia, there are no real guardrails. The hook can run any code he wants.
06:48 - 06:59 **Speaker 1**: And this is where IFUNC finally pays off. Gia uses an IFUNC resolver to set the audit hook early. Then, when the linker writes in the real RSA decrypt address, the hook fires and swaps in his payload.
06:59 - 07:11 **Speaker 1**: Right in the middle of the Goldilocks zone. There is one final complication, though. Audit hooks are normally configured by the system, not by libraries like XZ.
07:11 - 07:22 **Speaker 1**: So, when Gia is first looking for the audit hook variable that he's supposed to rewrite, it's actually hidden from him. So, he first has to find it. Within the IFUNC, he scans a small region of binary code, hunting for signs of the hook.
07:22 - 07:33 **Speaker 1**: But it's just raw bytes. So, he writes a tiny decoder to turn them back into instructions that he can read. Now, Gia can find where the hook lives in memory and finally plant his code.
07:33 - 07:44 **Speaker 1**: Then, when RSA decrypt gets called legitimately, it triggers the payload and he's in. But now that he's in, what does he do? And how does he get out of there cleanly? Step three: the Cat Burglar.
07:44 - 07:56 **Speaker 1**: With Gia's exploit in place, SSH isn't just checking for a legitimate login anymore. It's also listening for a hidden master key. And Gia's careful.
07:56 - 08:08 **Speaker 1**: He doesn't want anyone else stumbling onto the backdoor, so that master key isn't just a simple password. It's actually a mini-cryptographic exchange of its own. First, the backdoor code checks for a shared secret. Then second, it authenticates the user.
08:08 - 08:21 **Speaker 1**: And only if both checks pass does the payload run. In effect, it's like the backdoor's running a miniature version of the encryption for SSH inside of SSH. But in SSH, it uses that encryption to keep the attackers out.
08:21 - 08:34 **Speaker 1**: In this case, the backdoor is using that encryption to make sure that it's only the attackers that can get in. But he's still careful. One of the main ways defenders catch intrusions is through SSH logins.
08:34 - 08:46 **Speaker 1**: So, to cover his tracks, he wipes evidence the backdoor ever fired. And this is on top of the numerous safety checks he's inserted throughout the process to make sure the system supports the backdoor and doesn't crash and draw attention.
08:46 - 08:58 **Speaker 1**: And this is the genius of Gia's trap. It's cautious and meticulous, designed to slip through only where it will run invisibly. With all three of these steps complete, he can finally control the machine undetected.
08:58 - 09:12 **Speaker 1**: All he needs to do now is get his updated XZ implemented in the next release. But just as Gia's completing his backdoor, an open-source developer requests to remove the dependency that links XZ to OpenSSH.
09:12 - 09:24 **Speaker 1**: This would spell disaster for Gia Tan. He becomes frantic, pushing harder and harder to get his compromised XZ into major Linux releases. He gets it into an early experimental build of Debian. He files a request to have it added to Ubuntu.
09:24 - 09:35 **Speaker 1**: He's trying to land the backdoor everywhere he can before anyone realizes what's going on. And it's then that Richard gets his first message from Gia. Over the next few weeks, he gets more and more insistent, urging Richard to add the updated XZ into the next release of Fedora.
09:35 - 09:47 **Richard Fearn**: I'm always very keen to talk to keen upstream contributors, contributors who are really excited about new things in their software, who are really willing to help us get stuff into Fedora. So, you know, that's great. Love it.
09:47 - 09:59 **Richard Fearn**: That's kind of makes my day. It's my happy place. Eventually, Gia gets what he wants. Richard adds the updated XZ to a pre-release version of Fedora. Gia has succeeded.
09:59 - 10:13 **Speaker 1**: Except, there's a bug. In low-level code like the backdoor, things you normally take for granted, like memory management, are not done automatically. If a function grabs a bit of memory, it also has to give that memory back when it's done.
10:13 - 10:24 **Speaker 1**: And if it doesn't, then every time the function runs, it grabs more and more memory and then never releases it. Over time, the program just keeps growing. That's called a memory leak.
10:24 - 10:35 **Speaker 1**: And to catch problems like this, developers use a tool called Valgrind. It runs the program more slowly but watches every memory operation for anything suspicious. And Valgrind is raising hell on Gia's code.
10:35 - 10:44 **Richard Fearn**: We put XZ, this version 5.6.0, into Fedora 40. We get a bug report initially.
10:44 - 10:56 **Speaker 1**: And the backdoor in XZ specifically is generating invalid writes errors. Well, the logic was written by hand, bypassing the compiler safety checks, and so they accidentally wrote outside the memory stack. Now, lucky for Gia, all this isn't immediately obvious.
10:56 - 11:03 **Richard Fearn**: Richard still hasn't noticed what's happening. New software has bugs, right? It's the state of nature of software. Software is absolutely full of bugs all the time.
11:03 - 11:15 **Speaker 1**: Now, the real problem is inside the malicious code in the test file. But Gia can't just go and fix that. That would completely expose the backdoor. So, he invents a cover story.
11:15 - 11:27 **Speaker 1**: He claims that the random data he used to generate the original test files, well, it's not reproducible, so he's replacing it. And in this updated code, he fixes the memory error.
11:27 - 11:38 **Richard Fearn**: It's a very convincing and plausible explanation for why this test blob has to be updated. But of course, it's not the real reason. All right, so now the real fix is in.
11:38 - 11:51 **Speaker 1**: But if the bug just magically went away, it would look a bit suspicious. So, he has to find a way to cover it up. So, what he then does is he changes the IFUNC code in a way where he adds like a whole bunch of comments and changes to the code around it that doesn't actually change the code but is plausible enough to look like he's changing how the IFUNC works to fix the Valgrind bug.
11:51 - 12:05 **Speaker 1**: It does. Listening to it, I'm like, I know that this is the evil hacker Gia Tan, but I'm like, ooh, that's clever, you know?
12:05 - 12:13 **Richard Fearn**: Yeah, I mean, look, the guy is obviously not an idiot, right? But none of this is suspicious. This is what we expect from compression software.
12:13 - 12:26 **Richard Fearn**: And as a packager, it's not really my job to fix every bug in upstream software. As soon as it gets to a certain level of difficulty, my thought here is, well, Gia Tan has actually been writing this software, right?
12:26 - 12:38 **Richard Fearn**: So, he's got it all in his head, he knows how it works. It's easier for me to just give him the problem. And I send the bug over to him, and like a day later, he sends the fix back. So, from my point of view, it's problem solved.
12:38 - 12:50 **Richard Fearn**: It works, the system works, right? I made the right call. I don't see at that point, knowing what I know then, I don't see that there's any problem.
12:50 - 13:02 **Speaker 1**: So, we downloaded Gia Tan's version of XZ, which was available on Fedora publicly. But we made a slight modification. Instead of using Gia's secret code, we're using our own.
13:02 - 13:14 **Speaker 1**: And that means that we can take advantage of Gia's backdoor. In this case, we're targeting the Veritasium.com website. And once we get control of it, I got a little trick in store for Derek.
13:14 - 13:25 **Speaker 1**: Now, to make sure I don't mess with any real traffic too bad and lose my job, we actually cloned the Veritasium website and put it on a very similar URL. But it will work the same way. Of course, Derek doesn't know that I've covered my bases.
13:25 - 13:37 **Speaker 2**: Oh no. Man, when you guys do these things, I just—I start to get more and more scared now. I want it to work for the video, but I also don't want it to work because I don't want to screw stuff up.
13:37 - 13:42 **Speaker 1**: So, yeah. It is a concern.
13:42 - 13:48 **Speaker 1**: I'm going to execute a script here, which is going to open up—it's opening up a port on the Veritasium server. And then on this side, I'm going to execute a little script.
13:48 - 14:00 **Speaker 2**: Uh-oh. Henrytasium. Who is this goof on the main photo? You spent time getting all suited up there?
14:00 - 14:08 **Speaker 1**: Of course. Looking sharp, sir.
14:08 - 14:14 **Speaker 1**: Thank you, thank you. Videos Derek would never approve of. Uh-oh. The concept was, over the years that we've worked together, you've said no to a bunch of my ideas, and I figured now with control of the website, it's about time the world saw it.
14:14 - 14:26 **Speaker 1**: Surviving seven days living underwater. How do saturation divers live at minus a thousand feet? I mean, you wouldn't be outside, right? So, I don't know why you need goggles there and like a respirator. But you're—you're not underwater.
14:26 - 14:38 **Speaker 1**: Why it's almost impossible to shoot 4,000 meters. A sniper video. Yeah. The CIA lied: exposing how the CIA lied about torture. I feel like that still goes into tough territory for us.
14:38 - 14:51 **Speaker 1**: How xenon gas replaced oxygen. I attempted to climb Mount Everest on xenon gas. That sounds like a terrible idea. This is—this is what this whole video was about. This whole video was just about trying to get me to greenlight your projects.
14:51 - 15:02 **Speaker 1**: You know, if people like these video ideas, they can feel free to let us know in the comments. We can actually make them. The top-upvoted comment one, I will greenlight. Let's go.
15:02 - 15:11 **Speaker 1**: Is this live to the public right now? It is live on—yeah, it's live on the server, yeah. If anyone's on the website right now, that would be very strange for them. Look, I'm not pleased. I would like you to change it back.
15:11 - 15:23 **Speaker 1**: It doesn't seem like this should be possible on a Linux server. So, the big question is, how did you do it? The address is the server. The seed is our code to get in.
15:23 - 15:35 **Speaker 1**: Then the command is what we're doing to essentially open up, in this case, NC, which is like opening up a port on the machine that we can then access from this second terminal. Then what we're doing is, on this side, we're doing—running a script that's connecting to that port that's just been opened up, copying our files, and then by the end, we're going to have root access on the server.
15:35 - 15:47 **Speaker 1**: That means that it thinks that we own the thing. That's so crazy. This—this is a very scary hack. I do not like. Another thing is that this is a very obvious way of demonstrating this attack.
15:47 - 15:59 **Speaker 1**: Like, I've changed everything on the website. You immediately know that I've gone in and hacked the server. If we were doing this for real, we would do it a lot sneakier. I mean, as you say, right? The thing to do would not be to totally rework someone's website so everyone notices, but to change it subtly so nobody notices.
15:59 - 16:12 **Speaker 1**: So you can skim data or, yeah, like get credit card details or get—take payments to a different location and stuff like that. So, you can copy anything you want, you can change anything you want, you can delete anything you want.
16:12 - 16:24 **Speaker 1**: So, if there's any interesting documents or crypto tokens, any files you're interested in, those are yours now. If there's secret communications going across this—and let's keep in mind all of our communication networks are also built around Linux—those communication streams are yours now.
16:24 - 16:36 **Speaker 1**: If you wanted to encrypt something and ask for ransom, that's possible now. The possibilities really are endless. After two and a half years of hard work, slowly infiltrating the XZ project and weaving in this ingenious backdoor, Gia's done it.
16:36 - 16:48 **Speaker 1**: He now has free rein on any machine that installs the new Fedora pre-release. And he also gets the same access on Debian testing and Ubuntu's pre-release environments. And with RHEL 10 coming up, his code could infect some of the most important computers in the world.
16:48 - 17:00 **Speaker 1**: Now he should be able to relax, wait for the release, and he's got his backdoor key. But just when he thinks everything's going right...
17:00 - 17:08 **Speaker 1**: Andres Freund is a German programmer. He's not a security researcher, he's not a hacker. He's just an employee at Microsoft working on an open-source project called Postgres.
17:08 - 17:21 **Speaker 1**: One day in March 2024, he tries out the unstable release of Debian to make sure that Postgres will run smoothly. But while checking the server connection times, he notices something odd. A slowdown.
17:21 - 17:33 **Speaker 1**: It's not much. In the worst case, it's only half a second. But it's enough to make Andres suspicious. We tested the connection times ourselves on our own version of the XZ hack, and we found the exact same thing.
17:33 - 17:44 **Speaker 1**: Consistent slowdowns of about 400 to 500 milliseconds. Andres had already seen the problems with XZ and Valgrind weeks earlier. And this only makes him more suspicious.
17:44 - 17:56 **Speaker 1**: So, he digs in deeper. He looks at recent additions to OpenSSH and traces the delay back to an update in XZ. He sees the binary test files but notices that they were never used in a test.
17:56 - 18:08 **Speaker 1**: It's even stranger. Andres tries to get back to work, but he can't stop thinking about it. He remembered sitting in a bunch of meetings and like not really being able to concentrate because it feels like, I should—I need to continue looking into this.
18:08 - 18:20 **Speaker 1**: Eventually, Andres sees the truth. This isn't some bug. This is a backdoor. And this backdoor is meticulous. It hunts through memory to find the audit hook.
18:20 - 18:32 **Speaker 1**: It implements a decoder to read those raw bytes and then it wraps everything in custom encryption and safety checks so that it only triggers on the right kind of connection. I mean, it even garbles its own string so that it won't be detected.
18:32 - 18:41 **Speaker 1**: It's incredibly cautious. But all of that takes time. And in the end, that's what grabs Andres's attention. Without this obfuscation, I probably would not have noticed anything was wrong.
18:41 - 18:52 **Speaker 1**: Now, XZ's security contact is Gia Tan. So, Andres can't exactly report it through the usual channels. Instead, he emails the Debian security team directly and posts a detailed report to a public security mailing list.
18:52 - 19:00 **Speaker 1**: Then, all hell breaks loose. I'm called up on, I think it was a Friday evening, in fact, I'm sure it was a Friday evening, to join an internal Red Hat meeting.
19:00 - 19:13 **Speaker 1**: And it's immediately obvious that this is not a normal meeting because, like, our head of security is there. It's explained to me that it's been found by somebody in the community that XZ has a backdoor. And immediately I'm like, WTF? How did this happen?
19:13 - 19:25 **Speaker 1**: To cover their bases, Red Hat quickly rolls Fedora back and tells all their users to reverse. And the whole open-source community starts digging into the project to understand what went wrong.
19:25 - 19:34 **Speaker 1**: One thing is clear, though. Andres is a hero. Now, the fact that this was discovered in a different test at all, that was lucky. But then, what are the chances that someone who isn't looking for a security bug spends days investigating this?
19:34 - 19:46 **Speaker 1**: So, um, big kudos to the researcher. And, yeah, saved us all from possibly a doomsday on the internet. I think that Andreas did a brilliant job, because he—he did what I should have done, actually, which is I should have looked at the—you know, I should have looked at the bug when—when I saw it.
19:46 - 19:58 **Speaker 1**: And I should have gone there, you know, like a—like a crazy hound, sort of sniffing around trying to find out what's going on. Andres even gets a shout-out from the CEO of Microsoft.
19:58 - 20:10 **Speaker 1**: But when the story breaks, the mainstream response is surprisingly muted. I'm still surprised now that the mainstream, um, news outlets haven't really covered this very much. But I can tell you how many systems would have been compromised, which would have been millions.
20:10 - 20:23 **Speaker 1**: Anything from spying to ransom to just taking down entire countries, you could have done this with this backdoor. I guess the big question is, who is Gia Tan? That's the question, isn't it?
20:23 - 20:35 **Speaker 1**: Um, okay. So, my feeling is that Gia Tan, the person I talked to, I believe is—is one person. But I also believe that behind him must be a group of people. And they worked for quite a while.
20:35 - 20:47 **Speaker 1**: I mean, they were at this for perhaps two and a half years that we know about. If you look back at the accounts pressuring Lassa, they share some similarities. They use free email addresses, and they have almost no footprint outside of the XZ threads.
20:47 - 20:59 **Speaker 1**: These were very likely sock puppet accounts, identities manufactured to apply pressure as part of a multi-stage social engineering campaign. Now, who spends a million dollars and takes two and a half years to attempt to break into every hotel room on the internet with the master key?
20:59 - 21:11 **Speaker 1**: I—I think it's not a criminal organization, because I don't think a criminal organization would have that patience to spend that time without any real return. So, I think it has to be a nation-state actor here.
21:11 - 21:24 **Speaker 1**: A lot of the aliases, like Gia Tan, they sound like Asian names, and the published changes are all timestamped in UTC+8, Beijing time. So, the signs point to China.
21:24 - 21:36 **Speaker 1**: And that's why it's probably not China. I mean, why would they make it that obvious? Every other part of the operation has been so meticulous, so cautious. And they also worked on Chinese New Year, but not on Christmas.
21:36 - 21:49 **Speaker 1**: And over the years, there were nine changes that fall outside of the Beijing time, into UTC+2, which is a time zone that includes Israel and parts of western Russia. That's why some experts have speculated that this could be the work of APT-29, a Russian state-backed hacker group also known as Cozy Bear.
21:49 - 22:01 **Speaker 1**: But again, do we know? No, of course we don't know who it is. And we likely will never know. Gia Tan himself just disappeared as soon as this exploit became publicly known and never heard from again.
22:01 - 22:13 **Speaker 1**: In a sense, it doesn't matter whether this was Russian or Chinese or Iranian. We need to protect from these types of backdoors, no matter where they're coming from. I see this as like, you know, the canary in the coal mine of what's going to be happening as attackers get more sophisticated.
22:13 - 22:25 **Speaker 1**: They make fewer mistakes. You know, the—the gloves are off in a way. And I don't think that the Linux community is fully, um, you know, is fully ready for this yet.
22:25 - 22:36 **Speaker 1**: In the aftermath of XZ, the open-source community poured over countless small similar projects, looking for...