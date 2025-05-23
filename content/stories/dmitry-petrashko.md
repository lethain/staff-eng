---
title: "Dmitry Petrashko - Tech Advisor to the Head of Infra at Stripe"
url: "/stories/dmitry-petrashko"
date: "2020-05-07"
name: "Dmitry Petrashko"
role: "Technical Advisor to the Head of Infrastructure at Stripe"
weight: 40000
---

_This story was recorded in May, 2020. Learn more about Dmitry on [Twitter](https://twitter.com/darkdimius) or [Linkedin](https://www.linkedin.com/in/darkdimius/), and reading his [presentations](https://d-d.me/site/presentations/)._

___Tell us a little about your current role: your title, the company you work at, and generally what sort of work does your team do?___

I am a Staff engineer and the Technical Advisor to head of Infrastructure at Stripe. 

My current team is all of Stripe Infrastructure, which is responsible for foundational infrastructure services at Stripe - Compute, Networking, Storage, Database, Data Engineering, Performance & Efficiency, Observability Services, and Developer Tools. Our work empowers Stripe engineers to focus on product.

The team that I "grew" from was Developer productivity, which builds processes, tools and core libraries used during product development at Stripe, including testing frameworks, linters, typecheckers, build tools, libraries used for gradual rollout, and many others. I started as an engineer on that team (while it was still a singular team), eventually becoming a Pillar Tech Lead of that group.

**_What does a “normal” Staff-plus engineer do at your company? Does your role look that way or does it differ?_**

A Staff Engineer at Stripe isn’t a role, rather it’s a level that corresponds to expectation of impact, communication, people and project leadership skills. Staff engineers fill different roles, mine is a current one is Technical Advisor (TA). In that role I partner closely with the Head of Foundation, Rahul Patil, with the goal of researching critical topics ahead of time, diving into critical issues (design, code, analytical), brainstorming technical action items, assisting with urgent technical follow-ups, instrumenting code for data collection, etc. This role is designed to expand Rahul’s bandwidth and strategic thinking, but does not directly make technical decisions.

As a stepping stone to that role, I was also a Pillar Tech Lead. As we have more PTLs, the expectations are better defined:

* PTLs help their teams make technical decisions that will play well with each other and with technical decisions made by other groups at Stripe. Teams at Stripe make most technical decisions themselves, but an experienced PTL can help fine tune those decisions to achieve better outcomes. PTLs also work as arbiters in cases where teams cannot reach an agreement amongst themselves on technical topics.
* PTLs guide the technical direction of Stripe, providing input on what are the most important problems to solve and setting the high level technical approaches to solving them.
* PTLs help their organization by representing it to other Pillar Tech Leads and also bring technical decisions made elsewhere back to the teams they work with to create alignment.
* PTLs create opportunities for other engineers to take on impactful projects and help them succeed.

In the PTL role, I used to partner closely with the Head of Developer Productivity and managers of the teams inside the group. We exchanged context and worked towards an agreed goal. 

Both of these roles (PTL and TA) are similar in that they partner with engineering managers and share insight into the needs of our users & tools at our disposal to address them, while the EM has a better understanding of Stripe-wide non-technical constraints (e.g. resourcing constraints).

<div class="pull">
<p><strong>Talks from Dmitry</strong></p>

<ul>
<li><a href="https://www.youtube.com/watch?v=GJOWlDv_Fcs">State of Sorbet</a></li>
<li><a href="https://www.youtube.com/watch?v=Gdx6by6tcvw">Gradual typing for Ruby at Scale with Sorbet</a></li>
<li><a href="https://www.youtube.com/watch?v=8mFl8fywIP4">Adventures in Efficiency and Performance</a></li>
<li><a href="https://d-d.me/site/presentations/">Earlier presentations</a></li>
</ul>
</div>

**_How do you spend your time day-to-day?_**

On a perfect week I’d spend Monday, Wednesday and Friday in meetings or working groups: either 1:1’s or team meetings, collaborating on plans & strategy, both short term and long term. Tuesday and Thursday of my perfect week would be spent coding alone. In reality, depending on team needs at the time, I may end up having more meetings or more time coding. If I’m working to set up a new project, I’ll commonly start by having a week with less meetings: focusing on project briefs, thinking through design, deliverables/milestones and security/reliability implications; followed by a week of socializing the proposal around the company and addressing feedback.

While, from time to time it might seem hard to find time to write code, I believe it’s important as it allows me to maintain a strong connection to engineering and be the bridge between business needs/prioritization and engineering constraints that PTLs need to be.

**_Where do you feel most impactful as a Staff-plus engineer?_**

Staff Engineers, and Pillar Tech Leads in particular, frequently help set direction for a new project. I feel particularly impactful when I can help improve a proposal that's well intentioned and solves a real need, but the team that drafted it lacks either experience or context to write a good plan to capture the opportunity. In such cases, having a well structured plan can help substantially reduce the scope while getting to most of the value, and thus demonstrate impact sooner. Or, alternatively, see that the proposal in hand addresses more use cases than the team had originally anticipated and refocusing the project towards a use case that was not known by the team that would lead to bigger business impact: in both of these cases, I feel impactful by empowering other engineers.

**_Can you think of anything you’ve done as a Staff-plus engineer that you weren’t able to or wouldn’t have done before reaching that title?_**

No, Stripe intends the Staff-badge to not be a gate into new opportunities and I believe we’re good at it. This is also true about the PTL role. We choose engineers for PTL position that are good at representing opinions of others. Even before I became a PTL I felt that prior PTL, [Paul Tarjan](https://paultarjan.com/), always made sure my perspective was presented.

**_Do you spend time advocating for technology, practice, process or architectural change? What’s something you’ve advocated for? Can you share a story of influencing your organization?_**

I was hired specifically to introduce typechecking into Ruby at Stripe. This included, together with [Nelson](https://nelhage.com/) and [Paul](https://paultarjan.com/), architecting and implementing the typechecker, [Sorbet](https://sorbet.org/), and growing the culture around using it.

In the early days of Sorbet, we’ve carefully chosen what features to add based on usecases that Stripe needs the most. I believe we’ve succeeded in covering most of usecases that Stripe had with a typesystem and, at the same time, keeping the simplicity: it’s very easy to get to a typesystem and culture that promotes complexity and elitism for sake of it and I’m happy that our efforts avoided swinging from untypedness to the other end of spectrum.

Today, in my role as Technical Advisor, I advocate for changes that will have outsized impact, most commonly in terms of Reliability, Scalability, Security and Productivity at Stripe. That can be changing the way data is sharded/stored, or changing the way we address change management. The big difference though is that unlike in Sorbet where I stayed on the project for years, I'd be looking to find/grow a person who'll take over the project pretty soon - after organization is bought in, and there's a plan with well articulated milestones and controlled risks. I'll keep having frequent check-ins with people driving these important projects with the goal to help mitigate these risks and discover opportunities to deliver the project faster, and thus my involvement is visible only in the early stages of a project.

**_How do you keep in touch with how things really work as you spend less time on hands-on development?_**

While I was a PTL, I had at least a couple of days a week where I got to code. I worked closely with other engineers on my teams and we continuously learned from each other.

As a Technical Advisor, I wasn't able to write code as much as I was as a PTL. I mostly wrote code when it was [code-yellow situation](https://www.usenix.org/conference/lisa18/presentation/kehoe). But the success in this role is dependent on having good insights and deep engineering understanding. To do this, I speak to our internal customers and stay on top of designs and, notably, failure thresholds and failure modes of systems of teams that I support.

In my role, it's highly important to understand needs of customers. One helpful resource for that is the Stripe-wide engineer survey that Developer Productivity group organises, where we are looking to find what are the biggest things keeping our engineers from being productive: maybe there’s some tool that became slow since the last survey or some use case that had a user base grow that’s not well supported. While this survey rarely finds things that we weren’t aware of, it’s a great tool for relative prioritization: we can compare how many people complain about things and prioritize them accordingly.

Additionally, before the Covid-19-induced lockdown, I used to join random tables for dinners at Stripe. I’d ask 3 questions:

* What are you working on?
* What makes it hard?
* How can infrastructure teams help?

This became a great tool in two ways: 1) connecting me to my users, helping discover their needs; 2) helping mitigate unhappiness of teams that aren’t yet supported by having a discussion similar to: “yes, I agree we could help you by doing X, now, lets together look on what we should stop doing to create space for this,” where a person would frequently discover that, while they would like us to address their pain point, they don't want it addressed at cost of us deprioritizing our current projects. 

As I was transitioning away from role of PTL, I've created a group that's currently called DevProd Assembly that gathers leaders of developer productivity teams. Each member of this group is expected to build a high trust relationship with 2-3 product teams, interview them monthly and aggregate feedback with other members of Assembly.

**_How have you sponsored other engineers? Is sponsoring other engineers an important aspect of your role?_**

While sponsoring other engineers isn’t required for a Staff Engineer, I believe it helps to succeed as one, as it helps you deliver more impact by creating opportunities for others and helping them succeed.

And yes, there have been multiple projects that I have helped scope, kick-off and derisk, while also helping grow a person to take it over from me when I roll off to the next thing.

There’s also a distinction between mentorship and sponsorship and I do both. Mentorship is about helping people grow and deliver impact. Sponsorship is about helping a person get in a position where they could demonstrate their ability to deliver greater impact. In working with my teams, I try to help people work on projects somewhat out of their comfort zone, and in that I sponsor them, and then, I could mentor them to help the project succeed.

**_You first got the title Staff engineer at your current company. Were you hired as a Staff engineer? If not, what was the process of getting promoted to Staff?_**

I wasn’t hired as a Staff Engineer. I had to get upleveled twice to get to Staff level at Stripe. Both of these uplevels were similar: Stripe uplevels after an employee has already been operating on the next level for quite a while and this adjusts expectations that they are expected to continue operating on that level going forward.

**_What two or three factors were most important in you reaching Staff?_**

In order of decreasing importance:

1. Focusing on impact on business and company.
2. Being collaborative: by joining meetings/working groups you should help achieve a better outcome.
3. Technical knowledge.

For me personally, the area that I needed to get good at before getting Staff Engineer was the second item. I was already delivering impact and was considered a person to go to for technical advice. I needed to improve my communication skills and collaboration skills so that I could constructively help people who are outside of my team, who might see me for first time ever and who, despite having good intentions behind their project, may not have the best plan to get it delivered.

A technique that helped me in that was asking for feedback in a private chat immediately after the meeting, in particular after meetings that didn't go perfectly. This has allowed me to learn what I did that might have contributed to other parties not feeling comfortable in these meetings and, in a few cases, genuinely asking how it could have gone better and help fix the outcome of a meeting that has already gone poorly.

**_How have where you worked and your education impacted your path?_**


**Companies:** I appreciate that Stripe has so many opportunities for impact and this definitely helped me.

**Education:** I happened to have got a very practical PhD (on how to build fast & maintainable compilers) that almost fully translated to knowledge that’s applicable to my work: helping a company to scale engineering. And, while it served me well, I think there’s a lot of luck involved: I happened to join the right lab at the right time (when conditions for Scala3 being born became material, I’d been at the lab long enough to not be too “green” but still early enough to not have totally set the direction of my research). I’m unsure if I’d advise others to do a PhD: from my perspective, in practical terms, many of my friends would have learned as much by building systems at Stripe/Google/Facebook for the same 4+ years it takes to complete a PhD. If you’d like to learn how databases work - you’d probably learn this not only at the laboratory that does research on databases, but also at the companies that have some of the highest demands for databases and have teams working to improve them. That said, a PhD was something that was a good tool for me to change my location.

**Location:** I came to the US from Switzerland to join Stripe. I came to Switzerland from Russia to join one of the best PhD programs in Computer Science. I came to Russia to join one of the best ex-USSR universities from Ukraine. In each of these relocations, I feel, I played geographical arbitrage: I was looking to escape the place where I was among the best to the place where I’d be average. In some of them, I think I wasn’t the prime candidate. By joining the people there and learning from them, I grew a lot. It’s hard for me to tell if US vs EU is a better location career-wise, but I can definitely tell from my experience that changing locations helped me grow a lot.


**_There is a popular idea that becoming a Staff engineer requires completing a “Staff Project.” Did you have a Staff Project, and if so what was it?_**

It's a very hard question for me to answer in retrospect. This is because: as far as I know, Sorbet was big enough to be my Staff engineer project, BUT with Nelson and Paul being there and us working closely and very fast with each other, it was very hard to attribute success of the project to specific individuals rather than the whole team.

Around the first performance evaluation into the projects, all three of us got feedback that we should have better ways to prescribe which impact was the result of which individual. While I’d love to say that the fact that we didn’t face a similar issue on the next performance evaluation was due to intentional actions, I don’t think that is true: I think the project just naturally entered a stage where it was much bigger and thus we didn’t need to “quickly iterate in the same 10 files”, naturally leading to us having clearer and bigger areas of ownership.

I became the “internal architecture/subtyping” person, as well as “talk to users” person, while Paul became the “change the code to make typechecker like it” person. Nelson clearly knew better how other systems at Stripe work and thus helped integrate the tool with them. All of these played to our strong points: I had prior experience with type checkers (this is what my PhD was about), Paul has a huge skill for programmatic codemods and Nelson is both very knowledgeable in systems in general and has been at Stripe long enough and early enough to know pretty much every system at Stripe. At this point in the project (stabilization, rollout) all of these became huge areas and thus it became much easier to have a person be a directly responsible individual (DRI) for an area, with others helping occasionally.

After Sorbet I had a couple of other impactful projects delivered in short timeframe (6 months) that, I believe, sealed the deal of me getting the Staff Engineer level, but, if I was to choose one, I’d still choose Sorbet due to vast scope of project: both technical and cultural.

**_Can you remember any piece of advice on reaching Staff that was particularly helpful for you?_**

1. Working with Martin Odersky and Ondrej Lhotak in academia helped me understand how complex systems work together and how to explain that clearly.
2. Brian Goetz helped me understand how much work is behind a simple, yet, robust system to withstand widespread adoption and design.
3. Paul Tarjan showed me the importance of adjusting my communication style to lead to constructive outcomes for all involved parties.

**_What about a piece of advice for someone who has just started as a Staff engineer?_**

At least, at Stripe, Staff Engineers work on very different areas. Make sure you agree with your reporting chain on what is the impact you should be achieving and what are the things you’re allowed to compromise on the way to that impact. Communicate clearly what compromises you're doing and why.

**_Did you ever consider engineering management, and if so how did you decide to pursue the staff engineer path?_**

Every time I considered it in the past it was by asking myself and others around me “would it be a way to bring more impact.” So far, every time the answer was “seems like no.”

That said, I’ve found that learning some management skills from great managers (in my case, James Iry, Scott MacVicar, Will Larson, Christian Anderson and Shane O’Sullivan) provides huge benefits even in an individual contributor role.
