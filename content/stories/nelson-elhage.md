---
title: "Nelson Elhage - Formerly Staff Engineer at Stripe"
url: "/stories/nelson-elhage"
date: "2020-04-07"
name: "Nelson Elhage"
role: "Formerly Staff Engineer at Stripe"
weight: 33000
---


_This story was recorded in April, 2020. Learn more about Nelson on his [Twitter](https://twitter.com/nelhage) and [blog](https://blog.nelhage.com/)._

___Tell us a little about your current role: your title, the company you work at, and generally what sort of work does your team do?___

 I was most recently at Stripe. They do online payment processing, and it’s a pretty fast growing startup of about two thousand people. Engineering was around six hundred. When I left, I technically didn't have a title. If I had stayed another two months, I would have been a Staff Engineer, because they finally rolled out titles after some years of internal debate.

 The team I worked on most recently was called Payment Architecture, which was a team of three or four fairly senior engineers. Payments are the core of Stripe’s product, and we looked after the payments codebase. We were particularly focused on the financial infrastructure layers of the codebase, and building the data model and abstractions we needed to support all of Stripe’s current and aspirational product lines.

 We looked at how code structure fits into organizational structure, including how to structure code within a rapidly growing organization that was adding teams, products, countries, and payments methods. It was particularly important that our architecture support spreading ownership across a number of offices and timezones.

 We drove a lot of initiatives around code quality and code architecture, and did some implementation and rewrite projects. For each of those initiatives, we developed metrics and goals, got teams to take on those goals, and then gave teams tools to help them migrate to the new standards.

<div class="pull">
<p><strong>Some of Nelson's writing</strong></p>
<ul>
<li><a href="https://increment.com/testing/testing-as-communication/">Testing as communication</a></li>
<li><a href="https://blog.nelhage.com/post/systems-that-defy-understanding/">Systems that defy detailed understanding</a></li>
<li><a href="https://blog.nelhage.com/post/computers-can-be-understood/">Computers can be understood</a></li>
<li><a href="https://blog.nelhage.com/post/why-sorbet-is-fast/">Why the Sorbet typechecker is fast</a></li>
</ul>
</div>

___Was the “Payments Architecture” team a permanent team or more of a project team?___

 A little bit of both. It wasn’t a super tactical team with a narrow project or scope to its mandate. But it was also unlikely to last forever as a team. We were taking an experimental approach to evolving our architecture, with the goal of revising and updating our approach as we went. We hoped that the team would eventually work itself out of its job.

___What does a Staff-plus engineer do at your company?___

 It’s hard to say with too much confidence because Stripe was only just introducing titles. It wasn't public who was a Staff Engineer, but you did have a sense of who the senior engineers were based on the people working on the most significant, impactful things.

 There are some clear Staff Engineer archetypes. One is working on deep technical projects, maybe scoping out or building new pieces of infrastructure. Before the Payment Architecture team, I worked on building [Sorbet](https://sorbet.org/), which is our static Ruby type checker. I spent about a year with two other senior engineers building that from scratch, which was a good example of the deep, highly leveraged technical work archetype.

 There were also Staff Engineers who spent time wrangling cross-cutting projects, serving as a combination of architect and project manager to pull together different parts of the organization to work on a large problem. Typically these problems weren’t well-aligned with our current architecture or organization such that they required collaboration across many different teams.

 There were also Staff Engineers who worked with one team, or a small group of teams, and they served as the keepers of the team vision. They’d identify what the team was building towards, and where they wanted to be in one to five years. They’d work across the organization to build and share that vision, then work to implement it.

___How do you spend your time day-to-day?___

 This looked very different between the Payment Architecture role and the Sorbet role. Sorbet was more of a “heads down and code” project. On Payments Architecture, there was still some amount of coding because we had a specific approach that we wanted to both try out and to demo the ideas that we were pushing for.

 I did a decent amount of project management as well. Things like tending to the task tracker, running the daily stand up, figuring out who needed help or who was blocked. I also spent time being communication glue across the company and engineering organization, especially talking to teams that were interested in the tools and patterns we were building and advising them.

 In that effort, I spent time in various meetings figuring out the technical strategy, and also a fair amount of my week writing design documents on the problems we saw along with promoting the shape of architecture that we thought would solve them. Finally, I worked to explain and sell those ideas to leadership and other teams, as a way of setting the agenda and advocating for their investment and prioritization.

___Where do you feel most impactful as a Staff-plus engineer?___

 Certainly the one that's easiest to trace the impact of was [Sorbet](https://sorbet.org/), where in two years a three person team took Stripe from a dynamically typed code base to a substantially statically typed code base. That impacted all of the company’s six hundred engineers’ daily experience in their editors and development environment.

 That said, it's hard to know whether that was truly the most impactful project. There's a more nebulous argument that the architecture strategy work will be more impactful in the long run.

___What’s something you’ve done as a Staff-plus engineer that you weren’t able or allowed to do in earlier roles?___

 The question of “allowed” is interesting, and might not be quite the right question because there were very few official policies on who got what kind of role. Most things relied on more informal gauges of seniority.

 But that said, both Sorbet and the Payments Architecture team were relatively ambitious projects. Sorbet for example required pulling three senior engineers off of more concrete projects. Starting them required high levels of organizational respect and trust to get permission and support to pull the team off their existing work and having them instead work on these projects for a year.

___Do you spend time advocating for technology, practice, process or architectural change?___

 This is somewhat seasonal around the planning process. Prioritization ultimately means staffing, and staffing decisions happen during planning.

 The planning season was a particularly acute period, but I was more or less continually thinking about prioritization at the engineering-wide level. It might be noticing a problem that a lot of engineers were encountering, or seeing something that was slowing teams down. It was a constant, recurring thread that I thought about and it would periodically become an acute priority where I’d spend time advocating for a team to be created or to work on a problem.

___How have you sponsored other engineers? Is sponsoring other engineers an important aspect of your role?___

 That wasn’t an angle that I spent a lot of time thinking explicitly about in those terms, and I can't think of clear examples where I would describe that as what I was doing. An adjacent thing that I did a couple of times was helping to bootstrap teams that I wasn't part of. For example, some team would spin up to take over a system that used to be part my capacity, and I would work with them in a close advisory role to give them context and advice.

___You first got the Architect title at Oracle after the Ksplice acquisition. What was your process for getting the Architect title?___

 I don't remember if [Ksplice](https://en.wikipedia.org/wiki/Ksplice) had titles in place pre-acquisition. After the acquisition I spent one year at Oracle and had the title Architect, which I think at the time was their highest individual contributor level. There was definitely some acquisition title inflation going on there. I don't know if I would have reached that title if I had not come in via acquisition.

___After Ksplice was acquired by Oracle and you became an Architect, did the work you were doing on a day-to-day basis change from before the acquisition?___

 I was broadly doing the same style of work. The thing that changed was that I spent a lot more time interfacing with the Oracle Linux organization within Oracle. I was focused on figuring out how our product would integrate with theirs, and also bringing them up to speed on our technology so that they were able to use it. I had previously spent time training new hires, but that was a much slower rate than what happened at Oracle which was, “We're dropping you into this 400-person org, and now training them is a big part of your job.”

___What two or three factors were most important in you reaching Staff?___

 The specific path I took was very dependent on coming in quite early at Stripe. I was roughly employee \#30. The thing that I did with that though, which I think is not identical to what everyone else did, is I tried to build very broad context and awareness across Stripe. That was comparatively easy to do, when there were 15 engineers; there weren't that many things then.

 But I spent a lot of effort as the company grew trying to stay aware of _everything_ that was going on in engineering: the interactions between teams, the scaling pain points. I tried to have an unusually global perspective. That helped me know which problems were important to work on and especially what the one level removed important problems were. If I knew the organization had a goal of launching a specific product, I would have the perspective to see the reason why it would be hard is because of these previous architectural decisions, or that this downstream system wasn’t currently up to the task.

 As the organization got really big, seeing those one level removed dependencies got increasingly hard, and trying to keep a broad view and systems level view helped with that. It also helped me connect teams together, making me a router of information and ideas, as well as an originator of proposals.

 Many teams get stuck looking at their section of the world, and have a less developed conception of how their internal customers are integrating with them. This happens because they've never worked on the internal customer teams they support. I helped bring teams the context of how other teams truly used their systems, and connected them to other people across the organization whose perspectives they should gather.

 It’s hard to keep all this context as the organization grows, but it’s even harder for someone who didn't start building that global context when the company was smaller. By starting early, you have a huge competitive advantage relative to someone starting later who tries to reverse engineer the architecture and organizational dependencies.

___When I spoke with [Keavy McMinn](https://staffeng.com/stories/keavy-mcminn), one interesting point she made was that sometimes it’s helpful to be able to see things without the full historical context. Did you ever find that your context made it harder to move forward?___

 Absolutely. I would notice myself coming into conversations with a team and I was prepared to give them a seven year history of every time someone had attempted the thing that they're doing and why it didn't work. It would take deliberate effort to review that history and ask myself, “Why is this information helpful or relevant to them?”

 Sometimes the information isn’t useful. On the other hand, if someone tried to do this thing and died on the rocks, there may be some really hard technical problem that's still around. There might be some value in pointing out the rocks, but also there's a lot of value in having the audacity to try again because it’s years later and we've become a different organization.

___There is a popular idea that becoming a Staff engineer requires completing a “Staff Project.” Did you have a Staff Project, and if so what was it?___

 I'm instinctively a little bit wary of this sort of idea of a staff project, in part because one of the archetypes of Staff Engineers that I've seen are people who don't necessarily run grand projects themselves or do big things. But just are sort of incredibly effective gurus and routers who make the whole engineering organization run better.

 Maybe my closest thing to a Staff Project is that I got my final promotion for work on something called the “Data Model Stripe Release Plan.” I led this six month long plan to get a bunch of teams to coordinate on a handful of projects addressing the weaknesses in our data models, and advancing the data model in ways that would, aspirationally, be transformative.

 I don't think it's a great instance of a Staff Project in some ways. For one, we did good work, but it was much less transformative than anyone hoped due to a combination of reasons. Some of which were in my control and some of which were that the problems were just too hard and the organization didn't have the resources to actually fix them in six months.

 While that project wasn’t necessarily better work than I did in other halves, it was a very visible, high profile role. It created visibility and increased my standing in the company in important ways.

___Can you share a piece of advice on being a Staff engineer that was helpful for you?___

 One lesson that I learned was the importance of focus and prioritization. That’s especially true when you have the broad organizational context that I talked about earlier. It's very easy at any moment to identify thirty different things that you would like to be working on.

 Occasionally you can push each of those thirty things forward a little bit. And that's productive for a while, but you need to be careful. If these are things that _aren't_ getting worked on and that you think _should_ get worked on, you're going to have much better luck picking one of them at a time and really focusing your effort rather than pushing a little across many different projects at once.

 One big distinction is whether there are already teams working on those thirty things. If there are already teams working on them, but not in the direction that you think is effective, you can get a lot of leverage out of going to those thirty teams and helping unblock them.

 In the end you have to say, “There are all of these things that I wish I could work on, and I'm not going to do all of them. This year I’ll pick one or two to work on, and I'm going to deliberately ignore the other for a while, even though I think they’re major problems.”

___What about a piece of advice for someone who has just started as a Staff engineer?___

 One thing is that I'm a huge believer in the primacy of Conway's Law to guide organizations’ technical architecture.

 Another is to build and invest in your relationships with engineering leadership: the managers, the directors, and the vice-presidents. I think some of this might be specific to organizational structure, but certainly at Stripe those people often had a lot of implicit power because they were the obvious people to go to with questions. They also have a lot of influence over staffing and prioritization.

 It’s important to have good relationships with them both so that you can influence them with your ideas, but also so that you can understand what problems they're seeing. You need to know what their incentives are, and what problems they perceive that you don't perceive. Having better alignment with leadership makes a lot of things much easier.

 Something else that has been quite valuable for me is estimation. I find it really valuable to be able to look at a system and have the habit of estimating how many gigabytes-per-second is this thing, or how much storage would this data take? You don’t have to get it perfect, getting the nearest power of ten is usually enough to be useful.

___Did you ever consider engineering management, and if so how did you decide to pursue the staff engineer path?___

 I considered it but not very seriously. I have a pretty good understanding of myself that, at least for now, I wouldn't really enjoy that work. I think I’d find all the interactions not a sustainable way to spend my time. I occasionally wish I was more interested in it, because I do perceive it as a way to get a lot of power, but I fortunately have enough self awareness to believe, I think correctly, that I wouldn't enjoy it and therefore wouldn't be good at it.

___What are some resources (books, blogs, people, etc) you’ve learned from?___

 I get that question decently often because I have an unusually broad breadth of general knowledge, and I don't have a good answer for where it came from. I'm pretty voraciously curious about computing, software and architecture. I read lots of different things, and I spend more time reading links on software engineering Twitter than perhaps is healthy.

 It’s also been really valuable for me to cultivate a good personal network of other senior engineers. I chat with them informally about whatever it is that we're working on and thinking about. When you have personal connections, you can get very unvarnished views of the problems people are seeing and the solutions they're considering.

 I’ve mostly bootstrapped this through the friends-of-friends networks of people I've known professionally or going all the way back to when I was in school. It's not something I sought out post facto.

 I read the occasional technical paper, but it's not something I do actively. It’s mostly when it's referenced by someone or comes up in some other context. It's definitely not something I make any effort to keep track of systematically or to review the recent publications. I do think that having a decent handle on the quote unquote foundational literature is really handy. 
