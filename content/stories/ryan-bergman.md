---
title: "Ryan Bergman - Senior Staff Engineer at John Deere"
name: "Ryan Bergman"
role: "Senior Staff Engineer at John Deere"
url: "/stories/ryan-bergman"
date: "2022-01-21"
weight: 52000
---

<span class="date fr">January, 2022</span>
[blog](https://ryber.github.io/),
[twitter](https://twitter.com/ryber),
[linkedin](https://www.linkedin.com/in/ryan-bergman-3665763/)

**_Tell us a little about your current role: where do you work, your title and generally the sort of work do you and your team do._**

I am a senior staff engineer at John Deere Intelligent Solutions Group (ISG) out of Des Moines, Iowa. As you may know, John Deere is a large manufacturer of farming, forestry, construction and turf equipment. The group I work for is responsible for the more advanced computer systems that go along with the equipment. This includes autonomous tractors, displays, navigation, telematics and cloud based data processing.

I mainly work on the cloud processing side where we take streaming data from planters, sprayers and harvesters and create artifacts and reports so farmers can work with agronomists and others on their operations.

I've been with ISG for 10 years. It's a really big domain and it's easy to move around and try out different things. Some of the bigger things I've worked extensively on include:
   * *Remote Display Access* which lets users remote into their equipment from anywhere with a computer or mobile device.
   * The initial agronomic data processing and reporting systems.
   * I was the lead product engineer for our data sharing and userland permission systems.
   * Public API access and authorization (oAuth systems)  

We also have a test farm just outside of town, and on a nice fall day, I can manage to schedule some time out there and let a tractor drive me around for an afternoon. That's not something a lot of tech jobs offer!

**_How do you spend your time day-to-day?_**

I basically have two modes:

*R&amp;D Mode*

I tend to be given experimental projects to flesh out and see if they can work or not. These are often with partners and suppliers and require a lot of external communication. The stacks at ISG can get really big, from embedded C++ on the tractors, to the communication systems, to the cloud processing. Getting your head around all of that at once is impossible, so I coordinate with different teams. You really have to be a bit of a social butterfly. It's a little like what you would expect out of an architect but I do a LOT more coding than most architects I know. If any of the code I write makes it to production it's usually some core logic I wrote into a library. I may or may not work with a specific team on these projects, or I may just hijack some developer to help me, or I'll bounce around. It also gets me out of the office and fun trips to places like San Francisco, Seattle, or Waiverly Iowa when there isn't a global pandemic going on.

*Chaos Mode*

Chaos mode is where I spend the entire day on MS Teams (or wandering the office pre-COVID) just helping people. I get hit up for a lot of different reasons and I have a deep history with a variety of different systems. Some days I just hop from one problem to another unblocking. Hopefully someone kidnaps me to do some pair or mob programming. This is an great use of my time. Even if I get nothing of my own done, unblocking 5 different teams to get their work done is always worth it. I've learned that some days are just going to turn into this like it or not, so you might as well dive in head first. 

**_What two or three factors were most important in you reaching Staff? How have the companies you joined, your location, or your education impacted your path?_**

There are really two sides for what folk are looking for at this level. You need to be very technically capable but you also need to be someone people want to work with. Folk are going to come to you with problems they need solutions for and they want someone pragmatic and creative and empathetic to their goals. They also want someone who understands all the parts that are going to have to change. Not just some small part of it.

Education-wise, I took an alternative path to this position. As a kid with undiagnosed ADHD and dyscalculia I developed an adversarial relationship with math. While I loved computers and loved hacking at home. I believed that a CompSci major wasn't something I was going to be able to do. So I went into the arts with the idea that I could back into computers from graphic design. I actually ended up majoring in City Planning (also in the design college). and then during the first dot-com boom I took a job with a tech startup doing web design while waiting for my fiancée to graduate. I never went back to planning and slowly worked my way down the stack. Still, I find I use my major all the time. Lots of city planning is about politics and how to navigate different groups with different agendas and needs. Once you're a little higher up in the org this is absolutely necessary. I also learned about things like long term project management, how to run a public meeting, and GIS systems which have helped while working on agronomic data.

**_What’s your advice to people pursuing a Staff role?_**

From a tech perspective, constantly reach outside of your comfort zone and your existing wheelhouses. I've been programming professionally for 20 years and at different times I've had Perl, ColdFusion, PHP, JavaScript, C#, Java, and Scala all be the primary world I lived in. Nothing is a hammer and nothing won't eventually be replaced (except C).

Being a senior staff engineer means understanding both low level code and *systems of systems*. I recommend reading up on "systems thinking" to understand the later. Everything exists as a whole. Microservices don't exist in isolation, they are all part of giant distributed monoliths. Once you're at the staff engineering level you need to understand the deep relationships that every part of your org's tech stack has on each other and on the outside world!

From a person perspective and especially if you're in a large org where there are lots of teams it becomes important to know about the org landscape. Who are the people you're going to need to communicate with, to persuade, to influence. I'm not a naturally extroverted person, and I don't do a lot of socializing or schmoozing, but I keep some notes and important emails so I can go back and figure out "oh yeah, who is working on that now"? The wider the net of people, the more influence you have and the better chance you're going to get promoted. I don't know anyone who got to staff on purely tech reasons. Lots of them are quiet and introverted, but they're also friendly and helpful and approachable.


<div class="pull">
<p><strong>Some of Ryan's Public Work</strong></p>
<ul>
<li><a href="https://www.youtube.com/watch?v=k6_xlRUNzF0">Walking Into Mordor: The History &amp; Future of Devops (DevOpsDays Keynote)</a></li>
<li><a href="https://www.youtube.com/watch?v=TGs0YbAR_hs">From Big Bangs To Crockpots: Strategies For Changing Prod With No Downtime</a></li>
<li><a href="https://ryber.github.io/blog/2017/08/24/the-nature-of-programming/">The Nature of Programming</a></li>
</ul>
</div>


**_Do you spend time advocating for technology, practice, process or architectural change? What’s something you’ve advocated for? Can you share a story of influencing your organization?_**

Advocating for all these things is in fact, my primary job. I was originally hired at John Deere as a senior developer and as somewhat of a XP coach. I came from one the primary places in town that practiced TDD, CI, and small batch releases. This was 2011, and many of these things were not common yet. 

So I started at the lowest level. "Let's do TDD" and I worked my way out from there. While I still care today that the teams are doing TDD, I spend more time advocating for tech changes.

Several years ago I was given ownership of the permissions subsystem called SOUP (Security, Organizations, Users, and Partnerships). It was not my favorite part of the system but apparently it got out that I had opinions about it. So I grabbed one other developer and we went to work at what was mostly a gigantic refactoring to get a model that was unified and easy to inspect and slice in the ways the various systems needed. In the end we replaced multiple different sub-systems including a custom RBAC and a LDAP repo with a single rdbms table. We also built out many support tools and reports that didn't exist yet. The one hard part was getting alignment to do the outside work of doing a large change to the permission systems. That means UX, documentation, training, marketing, more UX and user testing. These parts were far more challenging from the people side than the tech. I had to spend a lot of time with different product owners showing them the benefit to their own systems and explaining that if they wanted feature x, it would cost significantly less (or even be possible), if we can just align a little work across these other teams.

Eventually we did get it all done and a couple years later I still get complemented on the subsystem we made and about how elegant it is. Little do they know that this is the 4th of this type of system I've designed in my career. You really don't get a system right until the 4th time.


**_Did you ever consider engineering management, and if so how did you decide to pursue the staff engineer path?_**

At various points in my career I've been a manager. Usually of a pretty small number of people, usually my own team. I have been told by some of my employees that I was a good manager and I believe them, but the role isn't one I seek out or desire. It's not a passion. I love people and I love leading, I don't love being a gatekeeper to someone else's career. I also find it hard to divide being responsible for tech and people at the same time. I think they're just too different. I honestly don't think managers should have any stake in their employees work. They should either be concerned with the employee, or the project, not both. That's a conflict of interest. So if I could find a position where I'm ONLY responsible for mentoring and teaching, I think I would deeply enjoy that. 


**_What are some resources (books, blogs, people, etc) you’ve learned from? Who are your role models in the field?_**

1. Ron Jeffries: He has an <a href="https://www.ronjeffries.com/">excellent blog</a> and over the pandemic has been recreating <a href="https://www.ronjeffries.com/categories/invaders/">classic video games</a>. It's quite fun to watch and play along. He also has a fantastic book on the <a href="https://ronjeffries.com/articles/nature/">Nature of Software Development</a> 
2. As much I enjoy TDD, I have found BDD to be equally, maybe even more important in the way I develop systems. <a href="https://lizkeogh.com/">Liz Keogh</a> has been a big influence on me.
3. The concept of using "real options" in software development has been a big influence on the way I think about things. <a href="https://commitment-thebook.com/">Commitment</a> by Chris Matts, Olav Maassen, and Chris Geary is a short and fun introduction to the concepts (it's a graphic novel)
