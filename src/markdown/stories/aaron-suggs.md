---
title: "Aaron Suggs - Principal Engineer at Glossier"
slug: "/stories/aaron-suggs"
date: "2021-01-21"
name: "Aaron Suggs"
kind: "story"
role: "Principal Engineer at Glossier"
---

<span class="date">January, 2021</span>
[personal site](https://aaronsuggs.org)
[twitter](https://twitter.com/ktheory),
[linkedin](https://www.linkedin.com/in/aaronsuggs/)

**_Tell us a little about your current role: where do you work, your title and generally the sort of work that you and your team do._**

I work at [Glossier](https://www.glossier.com), a direct-to-consumer growth-stage skincare and beauty company with incredibly passionate customers. Our engineering team is ~35 people. I'm a Principal Engineer, mostly focusing on our Site Reliability and Tools team. My recent focus has been leading Glossier's Operational Excellence initiative (nicknamed ✨GLOE✨) and ensuring we're building scalable services and team practices. I define operational excellence as our ability to deliver low defect rates, high availability, and low latency for product features. In practice for the SRE/Tools team, that means improving observability, increasing our infra-as-code adoption, and shepherding our migration from a monolith to microservices.

In the [Staff Eng Archetypes](https://staffeng.com/guides/staff-archetypes), I gravitate most towards being a right-hand, and secondly a solver.

Prior to Glossier, I was a Director of Engineering at Kickstarter. In 2018, I joined Glossier as a Senior Staff Engineer (an IC role), and as the first engineer to focus primarily on internal tools and engineering practices. My first projects were building a feature flag system so we could safely and easily test features with real data; then implementing continuous deployments to accelerate delivery.

After a few months, I switched back to management to lead a new Platform team and prepare for Black Friday. Glossier has an annual Black Friday sale that generates a huge spike in traffic and revenue, and our ambitious growth targets showed we need to rigorously prepare with capacity testing, system hardening, and cross-functional collaboration (See [Surviving Black Friday: Tales from an e-commerce engineer](https://www.youtube.com/watch?v=Jy_-l3v9zsY) for details on Glossier's Black Friday prep). After some re-orgs, the Platform team wound down, but the current SRE/Tools team does similar work. A year ago I gave up my management responsibilities to more deeply focus on operational excellence.

**_Did you ever consider engineering management, and if so how did you decide to pursue the staff engineer path?_**

Absolutely! I've switched from manager to IC twice in my career; and I'll likely do so again.

When I first became a manager in 2015, it was the only career path for a senior engineer at my company. Fortunately, soon ever-smaller engineering teams to created and shared career ladders with parallel IC and management tracks. When I helped create Kickstarter's engineering ladder, I emphasized IC growth paths that didn't require people management.

I was deeply influenced by a section of Camille Fournier's _Manager's Path_ that called out "empire building" as a toxic management practice. It reminded me of the argument in Plato's _Republic_ that the political leaders shouldn't be those that selfishly seek power, rather those whose wisdom makes them duty-bound to lead.

So I don't orient my career around ever-greater management responsibilities: it's one tool in the toolbox. I appreciate management as a rich discipline that I'll spend my career honing; alongside programming and systems engineering.

Here are some important factors for me when switching between manager and IC roles:
* What skills does the team need most acutely: management to coordinate the actions of a group; or an IC to accelerate the execution?
* Will I have sufficient support and feedback to learn and succeed?
* Am I the only one on the team who could do this; or could other's do it well?

**_Can you remember any piece of advice on reaching Staff that was particularly helpful for you?_**

"Replace indignation with curiosity."

Several years ago, I told my manager about another team behaving in a way that caused problems for my team. When I finished, he gave me that advice.  I hadn't been curious about why the other team was acting that way. It turned out they had constraints that made their behavior quite reasonable. By approaching them with curiosity and a helpful mindset (instead of frustration), we quickly found a process that improved both our workflows.

More recently, while struggling with burnout, a career coach asked me, "What would let you approach each day with energy and optimism?"

It's become my morning mantra, ensuring that I make time for operational excellence and mentorship and bring genuine enthusiasm to my work.

**_How do you spend your time day-to-day?_**

My days are roughly 50% scheduled meetings, 35% deep-focus blocks, and 15% unplanned work.

I work hard to make sure the meetings are effective. That usually means at least having an agenda. The meeting should have a clear purpose known to attendees beforehand, such making a decision, generating ideas, or reviewing information. Meetings often have a negative connotation because they're facilitated poorly; but they can be incredibly productive. I try to get better at facilitating productive meetings and using synchronous attention well. _High Output Management_ by Andrew Grove is a great resource to learn about effective meetings.

A technique I recently learned from my CTO is to schedule reading time at the start of a group meeting. Say you're in a hiring debrief: everyone spends the first 5 minutes reading each other's feedback about the candidate. It's a great way to ensure attendees truly read the document and have it top-of-mind. It ultimately saves time and elevates the subsequent discussion.

I also interview quite a bit. In 2020, I did (*checks calendar*) 126 interviews. Improving the long-term health of the team is a key Staff+ responsibility; and helping us hire great people is part of that.

The deep-focus blocks are marked off on my calendar. My company observes "No Meeting Thursday" which helps a lot. I use these blocks for work that's 'important but not urgent' from [Eisenhower's productivity matrix](https://www.eisenhower.me/eisenhower-matrix/). That's usually writing specs and documentation, or researching and prototyping new tools and patterns.

My schedule is unusual in that I stop work around 4pm most days, then work later in the evenings, ~8-10pm. This gives me several high-quality hours with my family each day. I have difficulty concentrating in the afternoon, and can more easily concentrate at night. And I enjoy getting something done right before bedtime. So this schedule has improved both my work/life balance and productivity. I changed my schedule because of childcare needs during the coronavirus pandemic; but I think I'll keep it long-term. I encourage everyone to reflect on what habits and schedules are helpful for their work. An open discussion with your manager and some flexibility can go a long way.

The unplanned work is mostly answering Slack messages, advising on urgent issues, or sometimes responding to a production incident. I try to approach this work with a helpful attitude, and also with an eye towards cross-training and writing discoverable documentation to minimize future unplanned work.

**_Where do you feel most impactful as a Staff-plus Engineer? A specific story would be grand._**

I think of my impact in two ways:
1. Working the plan
2. Serendipity

'Working the plan' is about making daily, incremental progress on a big project with a team. Some examples have been improving our site availability from under 99% to over 99.95%. It took a lot of Learning Reviews (blameless postmortems), training, testing, and refactoring. Another was a 9-month migration from dynamically-generated Rails-based HTML pages to statically-generated React-based ones to improved time-to-first-byte and availability. It took a lot of coaching, buy-in, and coordination. To successfully work the plan, you need clear goals and incremental milestones to keep the team motivated, and continuous alignment with leadership on the desired outcomes and timeline.

'Serendipity' in my work is about sharing an insight with the right people at the right time to make a positive impact. For example, our team was recently choosing a new vendor and the team was split between two mediocre choices. I asked an acquaintance with expertise about the vendors how he would choose; and he recommended a lesser-known new vendor that quickly became a universal team favorite.

Another serendipitous example was an engineer mentioning during standup that a caching optimization wasn't having impact they expected. I happened to be familiar with the config options of the particular Ruby web server; and was able to interpret some complicated metrics on a dashboard they showed to determine we had misconfigured a memory threshold. Later that day, we made a one-line config change to optimize our memory usage that reduced latency by 30%.

Serendipitous impact isn't planned; and isn't necessarily hard work. It's about paying attention (being present), keeping a curious mindset, and sharing the insight in a way that colleagues are open to receiving.

**_How have you sponsored other engineers? Is sponsoring other engineers an important aspect of your role?_**

Certainly! As a Principal Engineer, I try to be an enthusiastic and conspicuous [first follower](https://sive.rs/ff) when other engineers are doing important new practices. Some examples are when colleagues demo'ed React snapshot testing and local development with Docker. After each demo, I'd ask how I can try it out and see the benefits for myself. Then I'd look for other teams and in-flight projects where we can apply these practices to get wider adoption.

I also 'cheerlead': recognizing a colleague's valuable effort in public or a small group, even if the outcomes aren't tangible yet. It could be complimenting a team that's was thorough and reflective during a difficult Learning Review; praising an engineer who reproduced a tricky race condition; or thanking someone who documented a poorly understood process.

I aim to serve two purposes with cheerleading: recognize those doing the valuable behavior, and give positive reinforcement in the hopes that the team does more of that behavior. It's really [operant conditioning](https://en.wikipedia.org/wiki/Operant_conditioning), but cheerleading sounds much nicer.

**_What about a piece of advice for someone who has just started as a Staff Engineer?_**

Other engineers look up to you as a role model, some in ways you may not expect. They'll emulate your coding style, your tone in code reviews, your behavior in meetings, your rationale for making decisions, and the way you treat colleagues.

It can feel like a lot of responsibility to be perfect all the time. But it can also bring clarity to your work: do your best, acknowledge shortcomings, be generous and curious.
