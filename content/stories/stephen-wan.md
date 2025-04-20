---
title: "Stephen Wan - Staff Engineer at Samsara"
name: "Stephen Wan"
role: "Staff Engineer at Samsara"
url: "/stories/stephen-wan"
date: "2020-09-20"
weight: 44000
---


_This story was recorded in September, 2020. Learn more about Stephen on his [Github](https://github.com/stephen), [Twitter](https://twitter.com/stpnwn), and [Linkedin](https://www.linkedin.com/in/stephenwan/)._

___Tell us a little about your current role: your title, the company you work at, and generally what sort of work does your team do?___

I'm a Staff Engineer at [Samsara](https://www.samsara.com/).

I started at the company four years ago when the company had been around for a year and we had 50 or so employees. Nowadays, we have over a thousand folks at the company, with engineering teams in the Bay Area, Atlanta, and London.

When I first started, we had yet to form real teams and our ten or so engineers worked on whatever came up. Nine months in, we had doubled up and formed product teams around a few core offerings at the time. I did a brief stint leading a product team before switching over to our budding infrastructure group to start our frontend infrastructure team. Over the years, I've gradually shifted down the stack, also taking stretches on our backend and observability systems.

Today, I work in our Infrastructure & Platform (I&P) group, spending most of my time with the Developer Experience team which builds tools to keep our full-stack development workflow productive.

**_What does a “normal” Staff-plus engineer do at your company? Does your role look that way or does it differ?_**

Most of our Staff+ engineers are in specialized roles, either in web infrastructure or device firmware. I suppose that puts me in the majority, but the work our Staff engineers do is varied so it's a bit hard to claim being "normal" in the role.

When looking at parallels between the IC and management tracks, Staff is considered a director-equivalent role. Staff engineers have the option to participate in many processes that are typically reserved for managers. We're invited to the cross-eng director's meeting and, at least in I&P, we're involved in roadmap planning and management syncs. Recently, we've brought in Staff engineers to participate in some promotion calibration meetings.

The level of access gives some sense of having a foot planted on both sides. The role is different enough from Senior levels that it's not quite as much an "individual" software-contributing role, but it's also quite different from our more people-focused management track.

Out of [Will's Staff archetypes](https://staffeng.com/guides/staff-archetypes), I think my role fits somewhere between the Solver and the Tech Lead. Part of the fun for me has been jumping into a different role every 6-12 months, diving into a different part of the system with a different group of folks.

**_How do you spend your time day-to-day?_**

It's pretty varied by the day. Right now, I try to make Tuesdays and Thursdays meeting days so that I have dedicated focus time in the rest of the week.

My meeting days typically include 1:1s with folks I'm working closely with as well as staff meetings. I'll also spend some time pairing with individuals on code and design review or more open-ended design discussions.

On other days my focus time is spent in investigation mode, trying to suss out both current issues and paving foundation for future projects. What systems need investment? How have our teams been executing? What upcoming changes should our group prepare for? This time is spent [shaping](https://basecamp.com/shapeup/1.1-chapter-02) in a broader sense.

Looking back, this focus is distinct from my role prior to Staff. Instead of executing at the individual level working directly on a project or team, the time is centered around a wider lens and over a longer term.

Notably, it's hard for me to guarantee anything longer than a day at a time spent writing code. I don't get counted when we consider engineering roadmap bandwidth, though I do try to reserve at least a day a week for writing some code.

At the micro-level, I keep a document called "what is stephen doing?" that drives my work on the hour-by-hour granularity. There's one main section for the current week and some reminders for future weeks. Every Monday, I start over - unstarted items from the previous week get deleted and few survive to the next week.

![what is stephen doing?](/stephen-wan/what-is-stephen-doing.png)

That delete-by-default intention ends up helping me keep focused and not feel too strewn out. For a long time, I tried to groom a back-burner list of things to do but it mostly had the effect of stressing me out. Most back-burner items would end up deleted and incomplete anyways, a month later.

**_Do you spend time advocating for technology, practice, process or architectural change? What’s something you’ve advocated for? Can you share a story of influencing your organization?_**

Yes. The specific technology or methodology changes quarter to quarter, but advocacy ends up being a big part of my time. On the smaller end, I've helped write culture documents about how we try to approach design documents or code review or code ownership rules.

For a bigger example, I spent a couple quarters helping our product teams adopt Service Level Objectives (SLOs).

At the time, we had a fairly established set of features and customer base, but our measurements for uptime were still primitive. In outages, it was hard to get a sense for customer impact because we lacked the distinctions and definitions to communicate ("What percent of customers are affected? Is it both reads and writes? Is this an outage or an existing bug?"), even though we had plenty of metrics and dashboards to look at.

Though introducing SLOs certainly required new engineering work, I'd guess that the majority of my time on the project was spent writing documentation, talking to people, and doing consultancy-style work with teams. We wanted folks to be able to understand reliability objectives end-to-end: how to define the objective, how to talk about it in outages, how to measure it in systems, how to keep track of it over time, how to react when it becomes unhealthy. That level of depth ends up needing a lot of messaging and massaging to sink in.

As with most of our big "migrations," getting many teams to adopt SLOs came iteratively. We first trialed our new tools with a single team with high-touch support before figuring out the widespread messaging for the rest of the org. I think a key role for me was being able to both talk with engineers about the new tools at a concrete, how-do-I-use-this level, while also convincing director-level folks that it would be worth their effort to speak in SLOs.

This same pattern has held true over most of my projects as a Staff engineer. My role ends up being in brokering deals between groups to sell a change across the organization.

**_How do you keep in touch with how things really work as you spend less time on hands-on development?_**

I put in some time programming and doing code review each week, even if it's just to put up a small bug fix. I try to put in time to participate in the same day-to-day rituals other ICs go through - code review, navigating docs, outage situations, etc.

Of course, that's not enough to keep a high-fidelity model in my head - there's just too much happening across too many teams to keep track of. The rest is a lot of intentionally seeking out feedback and hearing first-hand experiences from others.

I've also tried to help bake feedback loops into our organization. I helped get us started on doing half-year dev team surveys with a mix of questions about both our technical systems and engineering culture. The responses from those surveys have been super helpful in keeping a pulse on how the organization is feeling from the ground up.

**_How have you sponsored other engineers? Is sponsoring other engineers an important aspect of your role?_**

Yes. I've tried to be intentional about giving away my state, stepping back, and letting others build up expertise.

At the organizational level, I think there are ways to structurally sponsor others, pushing other engineers into taking positions as subject-matter experts. As an example, I worked on introducing a new distributed tracing system late last year. Our core web application is powered by a number of different backend systems and over years, the data flows between these systems became trickier to understand and page performance suffered. We needed a tool to dig ourselves out.

I had worked on early iterations of our performance tools before and knowledge of those systems was largely stuck in my head. In the new project, a concrete goal for me was to bring more folks up to speed. It wasn't enough to lay a technical foundation in the systems design: my teammates on the project would have to own that area of expertise for years to come.

Practically, that meant spending more of my time discussing and pairing with the soon-to-be tracing owners and much less time directly contributing code or design. When we beta tested with a product team, I'd push another engineer to work on a sales pitch, or figure out the demo, or get the team onboarded.

Today, the tracing system is widely used and fully managed by our SRE and Observability group. The folks I worked with at the time are now the go-to group for performance questions.

On a more personal level, there are always small spots where I can help nudge other folks into the spotlight. Sponsorship opportunities can start small. Especially if I'm working with someone earlier in their career, I might suggest that they take on more unknown chunks of a new system design, or write a draft for new documentation, or demo our results at our group-wide meeting.

That small push might be all someone needs to get going, but other times I think it flows nicely into an opportunity to mentor and pair as well. Some things (like building up a slide deck for the first time) can feel intractable until you do them a couple times. There, both the sponsorship and mentorship sides end up feeling impactful.

It also feels like there's some tension to get to the right spot. We want to grow folks into positions where they can own more and make systems decisions, but we also want there to be alignment in how those decisions get made and where we're trying to go. It's hard work - it ends up taking a lot of attention to not gatekeep but get to a satisfying result.

**_You first got the title Staff engineer at your current company. Were you hired as a Staff engineer? If not, what was the process of getting promoted to Staff?_**

When I joined the company, we didn't have IC titles. I was leveled into the Staff role when we introduced leveling in early 2019.

I think I had a big advantage from being an early engineer on the team. That history was huge in giving me context on our past decisions - knowing what pitfalls we had already run into and helping land new projects into a good place.

At every stage of growth, we would add more layers of people and management and there'd be a "relearning" period for how the organization worked. Over time, teams would narrow in scope and only be able to see a smaller part of the puzzle. Having a big part of the engineering history in my head not only helped me connect pieces across those divisions, but also gave me a headstart on keeping personal connections over to parts of the organization I stopped working with directly. That breadth naturally lent itself to being able to figure out what could be most impactful for the org.

**_What two or three factors were most important in you reaching Staff? How have the companies you joined, your location, or your education impacted your path?_**

My background is somewhat less traditional - I studied Electrical Engineering instead of Computer Science and dropped out of school before completing my degree. That gap forced me to be more self-taught in my experience, but also left me with a lot of imposter syndrome. I failed a lot of software interviews early on for not having the right credentials. Early in my career, that imposter feeling made me really want to learn as much as I could to cover up for what I feared I didn't know.

The summer before I dropped out, I interned at Stripe. I remember, perhaps through rose-tinted glasses, feeling so energized by the engineering culture there: the hyperfocus on customer experience and excitement about building technology to get there. That experience ended up being quite influential to how I wanted a workplace to feel.

Later when I left school, I started working full-time at a smaller startup where I really didn't know what I was doing. The business meandered a bit during my time there, but I was lucky to have worked closely with thoughtful, senior engineers who had a penchant for mentorship. Working there ended up giving me a lot of flexibility on what I wanted to learn which was good for me but probably bad for the company.

As a last bit of background, I worked at a computer camp for a couple summers in high school, teaching school-aged kids basic computer literacy. That teaching mindset certainly left me with more empathy for how folks end up understanding and interacting with computer systems.

By the time I joined Samsara, those experiences gave me a clear sense for how I wanted work to feel - being an early employee gave me the influence to shape the way there.

The final piece of the puzzle was my first three years at Samsara. I was fortunate enough to get to work with so many thoughtful collaborators in that time. I can easily trace back many of the working habits, mental models, and mannerisms that I have today to those individuals. I can't imagine that I'd be in this spot in my career without their influence.

**_There is a popular idea that becoming a Staff engineer requires completing a “Staff Project.” Did you have a Staff Project, and if so what was it?_**

No, I didn't have a designated Staff Project. Looking back, there were projects over the years that perhaps accumulated into the equivalent of a big Staff project, but it's not something we explicitly talked about in leveling.

As a concept, I'm skeptical of that kind of singularly focused project and worry that they can put folks into a [hero mindset](https://lethain.com/doing-it-harder-and-hero-programming/) when we really want to value engineers that can build the organization, not carry it. I'd be much more excited to see iterative improvement and consistent execution over time: a track record of thoughtful engineering.

I'm happy Samsara seems to agree with that assessment. Our career path document ends up talking much more about that consistent execution over a single large-haul project.

**_What about a piece of advice for someone who has just started as a Staff engineer?_**

A couple things come to mind.

_Get comfortable talking a lot_. I think a big step-change between Senior and Staff roles ends up being the focus on people: reconciling competing priorities, clearing up miscommunication, aligning folks on the same page. Even though they typically don't have direct reports, Staff engineers are working in a system of both the technology and the people: the biggest impact is going to come from influencing both.

_Do your best to not get exhausted_. As I transitioned into a Staff role, it felt easy to slip into a mindset where I was responsible for everything going on and had to timeslice my focus over too many things. It took me a while to recognize that this role didn't mean I had to work many times harder to be involved in everything, but instead I needed to direct change through others in the organization. Trust folks, flag issues, and expect them to work it out.

**_Did you ever consider engineering management, and if so how did you decide to pursue the staff engineer path?_**

Back in 2016, I remember having an initial conversation with my manager about pursuing an IC vs management path. At the time, I still felt early into my professional career and wanted to continue investing in my core technical experience.

I reevaluated that decision every year or so and ended up coming to the same conclusion - that I wasn't done getting my hands dirty on the technical side. Throughout that time, much of the work I was doing was focused around building development experiences for folks at the company. Those efforts ended up pushing me to do more Staff-like work and I naturally progressed from there.

**_What are some resources (books, blogs, people, etc) you’ve learned from? Who are your role models in the field?_**

I tend to prize literature that talks about complicated topics in plain English, both fiction and non-fiction.

I remember reading about novelist [Haruki Murakami](https://en.wikipedia.org/wiki/Haruki_Murakami) writing his first novel in English first, then translating it back to Japanese as a way of shaping the style of his expression. He notes, "I could only write in simple, short [English] sentences. Which meant that, however complex and numerous the thoughts running around my head, I couldn't even attempt to set them down as they came. The language had to be simple, my ideas expressed in an easy-to-understand way."

Writing software is a totally different domain, but it feels like the sentiment fits into some tenet that I really value about communicating: having an understanding in your head is half the battle - being able to express that understanding is just as hard and valuable.

I love reading blogs and papers that really go in depth in a technical area. A few that I've come back to over the years include:

* [Bob Nystrom's blog posts](http://journal.stuffwithstuff.com/category/language/) on programming languages
* [Vyacheslav Egorov's blog](https://mrale.ph/) about compilers and V8 internals (Chrome's JS engine)
* [Brandur's blog](https://brandur.org/articles) on various systems topics
* Nelson Elhage's [Accidentally Quadratic](https://accidentallyquadratic.tumblr.com/)
* [Vicki Pfau's Blog](https://mgba.io/tag/debugging/) on developing a GameBoy Advance emulator
* [fail0overflow's blog](https://fail0verflow.com/blog/) and talks about console architecture and exploits
* [Bungie's engineering publications](http://halo.bungie.net/inside/publications.aspx) on building and producing the original Halo games

As an anecdote, early in my career I had a budding interest in programming language internals and picked up a compilers textbook ("the Dragon book") to learn from. It's a pretty hard book to get through. Maybe it's reasonable to get through it with a professor and a few classmates, but it was truly difficult for me to get a working mental model from a reading. Later, I found Bob Nystrom's [Crafting Interpreters](https://craftinginterpreters.com/) which takes a much more practical approach and it felt like a huge breath of fresh air.

I'm also a big fan of reading codebases. Early on in my career, I recall debugging a tricky React problem where some callback wasn’t happening in the order I expected. Reading the docs didn’t help. Putting in print statements wasn’t enough. My mentor at the time got me to read some of the source code to better understand what was going on and that really blew my mind a little bit. I got a bug fix in but also a much stronger understanding of how React worked.

That was really a turning point. Being able to quickly dive in and jump through unfamiliar code has really felt like a superpower and gives me a larger pattern matching library for different approaches to software design. A recent favorite has been reading through the design and code of [esbuild](https://github.com/evanw/esbuild/blob/master/docs/architecture.md), a super fast javascript bundler.

Finally, some of my favorite recent non-fiction reads in the last couple years have been on the [history of BART](https://www.amazon.com/BART-Dramatic-History-Transit-System/dp/1597143707), the [history of Xerox PARC](https://press.stripe.com/#the-dream-machine), and [an overview of modern Japanese culture](https://www.amazon.com/Making-Common-Policy-Institutional-Studies/dp/0822955105). In each niche, I've found the history and context fascinating as seemingly small, independent events and decisions have culminated into ways the world works today.
