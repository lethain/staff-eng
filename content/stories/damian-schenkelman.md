---
title: "Damian Schenkelman - Principal Engineer at Auth0"
name: "Damian Schenkelman"
role: "Principal Engineer at Auth0"
url: "/stories/damian-schenkelman"
date: "2020-08-10"
weight: 43000
---

_Story recorded in August, 2020. Learn more about Damian on his [blog](https://yenkel.dev), [Twitter](https://twitter.com/dschenkelman), and [Linkedin](https://www.linkedin.com/in/damianschenkelman/)._

___Tell us a little about your current role: your title, the company you work at, and generally what sort of work does your team do?___

I'm a Principal Engineer at [Auth0](https://auth0.com/), an Identity as a Service platform. I work in the Systems Architecture group, which today has three Principal Engineers. We work with different teams on strategic initiatives and also shape Auth0's [technical strategy](https://yenkel.dev/posts/achieving-alignment-and-efficiency-through-a-technical-strategy), architecture decisions, and guidelines.

At the time of writing, I am working with a group of [Identity and Access Management](https://auth0.com/learn/cloud-identity-access-management/) (IAM) teams as a tech lead of a large new product feature, as well as driving reliability and scaling related initiatives with other teams.

**_What does a “normal” Staff-plus engineer do at your company? Does your role look that way or does it differ?_**

Within Engineering, we are organized in domains (today Identity & Access Management, Developer Experience, Service Management, and Platform). Auth0's Staff Engineers are people that can technically lead teams within a domain. A Staff Engineer would typically be part of a single team in a domain, while also being able to actively contribute to initiatives across the scope of a domain.

Principal is the next level in our ladder. Principal Engineers can either be in a specific team (depth) or work with multiple teams and their scope spans the entire organization (breadth). Today I am operating in "breadth mode." This means both working on specific initiatives and also the definition of technical strategy, technology choices for our Platform, and leading the Design and Architecture workgroup (a.k.a. DNA).

DNA has 6 members (3 permanent Principal, and 3 Staff/Senior II that rotate every 6 months). The workgroup defines decisions and guidelines to help drive Auth0's technology in a specific direction (e.g. avoid language proliferation so we can build libs once and people can switch teams easily) and also collaborate with teams in technical reviews of large initiatives.

The biggest way in which my role differs, because I have been at the company for 6+ years, 3+ of those as a Director of Engineering, is that I have the "broadest scope." I work with both Product and Platform teams on initiatives and also work often with other parts of the company: joining conversations with high profile prospects, working with our legal team on contract language, or collaborating with Marketing.

<div class="pull">
<p><strong>Some talks from Damian</strong></p>
<ul>
    <li><a href="https://www.youtube.com/watch?v=OoA-gx-19tQ">The dirty secrets of building large, highly available, scalable HTTP APIs</a></li>
    <li><a href="https://www.youtube.com/watch?v=vGywoYc_sA8">Multi-Region High-Availability Architecture that Scales to 1.5B+ Logins/Month</a></li>
    <li><a href="https://www.youtube.com/watch?v=1PVyDzfX1Ng">The Path to SRE</a></li>
    <li><a href="https://www.youtube.com/watch?v=88OLQ_fb2Oo">Real-Life Node.js Troubleshooting</a></li>
</ul>
</div>

**_How do you spend your time day-to-day?_**

This varies a lot. A typical week involves a lot of meetings, so I am trying a new thing: grouping meetings on Mondays, Wednesdays, and Fridays. Thursdays are completely blocked, and Tuesdays are only for urgent matters. Because we are remote all meetings are over Zoom.

On meeting days I have recurrent:
* 1:1s: to catch up with my manager (VP of Engineering), or a team manager or tech lead. Those conversations are great to stay up to date with them and know their challenges. I feel being too detached from that would impact my ability to get things done effectively.
* team meetings: Engineering leadership, Design & Architecture workgroup.

Non-recurrent meetings also take place. Some example topics might be:

* specific initiatives I am tech leading
* helping a group of teams figure out how to get something started
* doing a sync design review

On Thursdays (and as much of I can on Tuesdays) I spend my time thinking about:

* current initiatives and how they are going
* what we could/should be doing in the future (next quarter, next year)
* writing docs, guidelines, blog posts
* (not often) doing POCs and/or writing small tools

**_Where do you feel most impactful as a Staff-plus engineer? A specific story would be grand._**

The biggest impact comes from being able to help achieve "people scale," positively influencing the work of as many people as possible internally. The book [Scaling Up Excellence](https://www.amazon.com/dp/B00EGMQIDG/) provides an easy to understand analogy: scaling is a ground war, not a one-off airstrike. It requires a lot of time, and patience but to get to your goals you need to align the whole company in terms of goals and how to get to them.

As a Principal Engineer, I try to find opportunities/gaps that I believe will set a direction for as many people as possible in the long term. There's a lot more value to align the ~200 people we have in our Product Delivery organization around a certain topic than to code a solution for a problem myself. The former has more impact, it scales better.

**_Can you think of anything you’ve done as a Staff-plus engineer that you weren’t able to or wouldn’t have done before reaching that title?_**

Before becoming a Principal I was a Director of Engineering at Auth0. The most interesting thing is that as a Principal Engineer people get a lot less defensive when I provide feedback and they seem a lot more open in 1:1s. I think it might be related to the fact that as a Principal Engineer you are not "representing a part of the organization".

In that regard, being an individual contributor feels a lot better.

**_Do you spend time advocating for technology, practice, process or architectural change? What’s something you’ve advocated for? Can you share a story of influencing your organization?_**

A common problem for fast-growing companies is that there's usually some "lack of clarity." In our case, there was a lot of confusion about what was coming in the future and that made us slow and inefficient in making technological decisions. Teams were uncertain if they should be using a particular technology because they didn’t know if that technology would be supported in the future, they were uncertain if they should be building a particular product in a certain way because they didn’t know if that approach was aligned with our long-term technical strategy, etc. Naturally, this caused a lot of inefficiencies.

![](/damian-schenkelman/Damian-Schenkelman0.jpg)

We believed we needed a long-term direction that explained how to approach the technical implementation of problems today and how to bridge the gap between our initial situation and the future vision. More precisely, we needed a documented technical strategy that would detail what we should and shouldn’t be doing to be successful in the long run.

After talking to a great number of people I learned that all of them have been exposed to inconsistent information, and rumors, which made them afraid of making decisions, e.g.: "I heard the company is going for X in the future" or "I heard this particular technology Y is not going to be supported by our platform teams." A lot of confusion was caused by a particular rumor that we were going to support a certain customer need and its technical implications. People kept hearing about it, but concrete plans were never announced. I wrote down these issues, connecting all the dots and aiming to translate that information into knowledge. I realized we needed both short and long term ways of solving the problem.

**Short term:** We had to fill the gap of uncertainty relating to some more urgent and short-term matters. Teams needed to make technical decisions and couldn't wait for a full-fledged technical vision and roadmap. We also realized that once we had that long term vision and decisions, there would naturally be the need to review decisions for specific exceptions. I put together the "design and architecture" (DNA) group, which also wrote guidelines and recommendations, including "approved" technology choices, to guide teams towards independent decisions that don't require review, and also established an RFC review process.

**Long term:** I came up with a set of topics that I believed the company needed to make decisions about. I tailored my presentations to suit two different audiences -- executive and technical. For the executive audience, I developed a succinct presentation, applying non-technical analogies and explanations, and providing actionable solutions. The technical presentation was much more detailed and included many technical terms. I used [nemawashi](https://en.wikipedia.org/wiki/Nemawashi) (an informal process of quietly laying the foundation for some proposed change or project, by talking to the people concerned, gathering support and feedback, and so forth) and shared with my VP of Engineering, other execs, my peers, and other senior leaders through to get buy-in before formally making a decision. More specifically, I approached people asking them for their thoughts and opinions securing the buy-in, so that by the time we met to discuss our decisions, it wouldn't be the first time they were seeing the ideas. We finally met, discussed tradeoffs, and arrived at a set of decisions. All decisions were documented in a decision log and we committed specific owners -- in writing -- to carry them forward.

**_How do you keep in touch with how things really work as you spend less time on hands-on development?_**

There are two aspects of this, keeping up with technology in general and keeping up with what goes on at Auth0 and the current "state of affairs" in Engineering teams.

These are the things I do to keep in touch with things related to Auth0:
* Internally: keep an ear to the ground both through Slack and having 1:1s with some tech leads and Engineering Managers. This helps me understand what challenges they are having first hand, and also find patterns or arrive at global solutions instead of local ones.
* Externally: talk with customers/prospects to see how they use the product, read tweets and news mentioning Auth0 and the identity space.

I don't feel I am "keeping in touch" as much as I'd like technology-wise, but I do try to. So many new important new things are happening in our industry every month that it is hard to keep up. Accepting the fact that meetings and not being hands-on means that I will likely be less in touch than I'd like with things is important. Once I accepted that I could start prioritizing what was valuable.

I read books, carve out time to do some POCs or read blogs/papers about specific topics, and ask to lead specific initiatives to stay up to date with how we are developing even if I don't code that often.

**_How have you sponsored other engineers? Is sponsoring other engineers an important aspect of your role?_**

Yes, a lot! I am a member of our Engineering Leadership team. We meet twice a week to discuss topics around the organization. This, together with keeping an ear to the ground, and being part of meetings about mid-term plans helps me know about (and sometimes propose) opportunities that might be available ahead.

Whenever that happens I typically propose the names of people that I believe would benefit from that opportunity, explain why I think they would be good at it, and, if helpful, offer to mentor them in case there are any perceived skill gaps.

**_You first got the title Principal engineer at Auth0. Were you hired as a Principal engineer? If not, what was the process of getting promoted to Principal?_**

My story here is a particular one. I started at Auth0 in May 2014 as the fifth engineer, ~tenth employee. There were no titles, no ladder, nothing like that. Around 2015, I started mentoring and doing 1:1s with a couple of new hires. Towards the end of 2015, I was working on my initiatives, and also leading others, helping with hiring, etc. Late 2015 [Matias Woloski](https://twitter.com/woloski), Auth0's CTO and co-founder, was looking for someone to lead Engineering teams and he asked me if I would be a Director of Engineering.

I've been privileged enough to be able to approach my career in a way that maximizes learning and opportunities for hard problem-solving. That's the main principle that helps me make decisions. When he offered me, a 25 year old living in Argentina, the opportunity to lead the Engineering organization for a "Silicon Valley," remote-first company that was growing exponentially I naturally said "yes." I had never thought "I want to manage," it just happened because I wanted to learn and solve hard problems.

![](/damian-schenkelman/Damian-Schenkelman1.jpg)

Things worked out great. I learned a lot about building teams, organizations, leading people, etc. Because I was one of the first engineers, had built a lot of the systems and I enjoyed technical conversations I also did a lot of technical leadership in that role, both with Product and Platform/Infrastructure teams. Towards early 2019 as a Director of Platform, I started thinking that I was not learning as fast as before and that I wanted a broader scope than just working on our platform. After many conversations with [Christian McCarrick](https://twitter.com/cmccarrick), Auth0's VP of Engineering at the time, I realized that the challenge I wanted to take up next would be being one of Auth0's technical leaders. I transitioned to Principal Engineer in August 2019.

**_What two or three factors were most important in you reaching Principal? How have the companies you joined, your location, or your education impacted your path?_**

A quote I love from Seneca is _"Luck is what happens when preparation meets opportunity."_ Getting to Principal required getting some things right, but also a lot of luck. I want to call out some of the key factors that got me to Principal and also show how luck played a part in them.

**First job:** In Argentina it's common to start working while you are in University. When I finished high school I found a job at a fantastic company called [Southworks](https://www.southworks.com/). The two key things about that place were that:

- the company worked on projects with cutting edge technologies, which gave me lots of opportunities to hone my learning skills
- the company worked mainly as a Microsoft US vendor remotely, which meant that not only technical skills were valued, but also we got to practice communication, expectation management, and other interpersonal skills often.

The reason I could work in software right out of high school was that when I was eleven I started telling my mom I wanted to "build video games" and my parents found and paid for a high school that taught programming.

**How luck played a part:** I was about to take a job at another company when a friend of mine from high school told me her brother worked at Southworks and they were looking to hire junior people. He did a good job selling the company to me and I decided to put the other opportunity on hold to see if I could get into Southworks.

**Auth0:** I was one of the first engineers at Auth0 and over the years I worked on many parts of its product and infrastructure, which makes it easy for me to help people and provide valuable input on various topics. Being a Director of Engineering also helped me understand many things about our business that help me be a more effective contributor.

**How luck played a part:** the success of any startup requires a lot of luck at many different points in time. If Auth0 had not grown as it did, I wouldn't have had the opportunities to learn what I did and be where I am. This is particularly important because I live in Argentina where the Software industry is much smaller than it is in the US and most companies don't have dual tracks.

**Team sports:** I played basketball as a kid and during my teens and I realized early on it felt a lot better to win by scoring any amount of points than to lose scoring lots of points. That shaped how I worked in two ways:
* it led me to help team members often to see how we could succeed as a team
* it led me to learn and do things that would be required to "cover gaps," which helped me build leadership and interpersonal skills that are very useful as I grew in my career

**_There is a popular idea that becoming a Staff engineer requires completing a “Staff Project.” Did you have a Staff Project, and if so what was it?_**

I did not. Because of how I grew at Auth0 I kind of "skipped that part". As a Director at a startup, I got the opportunity to technically lead a lot of big, critical initiatives, but there was no specific/explicit "staff/principal project."

I think implicitly the closest thing to a "Staff Project" was the work I led in 2017 & 2018 to increase the reliability and scalability of Auth0, leading some projects to offer higher SLAs for a subset of our key customers.

**_What piece of advice do you have for someone who has just started as a Staff engineer?_**

Staff means different things at different places, so the first piece of advice I would give is to talk to as many people as possible to define expectations where they are.

The next thing I would tell people is to be patient. They probably got to where they are because they are fairly technical and got results, but as you grow in the ladder the outcome of your work takes time to develop. You might be working on more things at once, and the impact of them has a longer time horizon. You are also now influencing more people in different roles, and sometimes it takes them longer to "see" the things that you might see clearly. Being patient, progressively influencing people, and teaching others pays off long term.

Finally: get used to writing things down and repeating them to others. Writing down thoughts, plans, reasoning, and standards is the way you will scale yourself. When you document something you make it easy for anyone to access it and read in the future, it is easier to reference. It is a lot better than "just talking about it": it scales better and it also reduces the chances of things being misunderstood. Repetition is also necessary as just publishing written documents is not useful, so you have to share your ideas with people. Hosting AMAs, brown bags, and other sessions to explain what your thoughts are very valuable.

<div class="pull">
<p><strong>Some of Damian's writing</strong></p>
<ul>
<li><a href="https://yenkel.dev/posts/achieving-alignment-and-efficiency-through-a-technical-strategy">Achieving Alignment and Efficiency Through a Technical Strategy</a></li>
<li><a href="https://yenkel.dev/posts/starting-a-personal-mentoring-program-at-work">Starting a Personal Mentoring Program at Work</a></li>
<li><a href="https://yenkel.dev/posts/jiro-dreams-of-sushi-lessons-for-saas">'Jiro dreams of sushi' lessons for SaaS</a></li>
</ul>
</div>

**_Did you ever consider engineering management, and if so how did you decide to pursue the staff engineer path?_**

I wasn't planning for it, but when the opportunity came to be Director I took it. However, my thinking is that [there's a pendulum](https://charity.wtf/2017/05/11/the-engineer-manager-pendulum/) where you can go back and forth between the two paths. How easy it will be will depend on the company and how specialized the skills as a Staff/Principal are, but I think it is possible.

Nowadays I am very interested in continuing to develop my technical skills and leadership skills, as that's what I think will bring the most valuable learnings and challenges.

**_What are some resources (books, blogs, people, etc) you’ve learned from? Who are your role models in the field?_**

I try to follow people on Twitter who I think are doing interesting things and from who I can learn. There are so many people doing interesting things and so much to learn! Some of the names that come to mind:

* [Aphyr](https://twitter.com/aphyr)'s work with [Jepsen](https://jepsen.io/) and general content about distributed systems is great.
* [Tanya Reilly](https://twitter.com/whereistanya) has some very good content like [RFC process @ Squarespace](https://engineering.squarespace.com/blog/2019/the-power-of-yes-if) and [Being Glue](https://www.youtube.com/watch?v=KClAPipnKqw).
* [David Fowler](https://twitter.com/davidfowl) shares a lot of content about the .NET Framework and ASP.NET internals which I find interesting. There's also this video of him sharing how he became the [ASP.NET Architect](https://channel9.msdn.com/Shows/Careers-Behind-the-Code/Becoming-the-ASPNET-Architect-with-David-Fowler).
* At Auth0 I work with [Jon Allie](https://www.linkedin.com/in/jon-allie-b250296) who is a fantastic engineer and person. He strives for simplicity, can explain things very clearly, and is extremely humble considering how much he knows.

I haven't found a lot of books or similar content specific to senior "individual contributors" (might be interesting to write one). I recently read [Fundamentals of Software Architecture](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/) that does a fairly good job at describing that role while also understanding the nuances and gray areas of it.

Some books about management are useful to get organizational awareness and help with mentoring, 1:1s, hiring which are things one typically helps with as a staff-plus engineer. In [High Output Management](https://www.amazon.com/dp/B015VACHOK/) Andrew Grove refers defines the "know-how manager" as "people who may not supervise anyone directly but who even without strict organizational authority affect and influence the work of others", which sounds an awful lot like staff-plus engineers. I strongly recommend [Managing Humans](https://www.amazon.com/Managing-Humans-Humorous-Software-Engineering/dp/1484221575/) as it shares stories that are easy and fun to read, and also helps generate empathy with managers, which is important as a staff-plus engineer. [The 7 habits of highly effective people](https://www.amazon.com/dp/B00GOZV3TM/) is also a book that has a lot of good lessons for staff-plus engineers.

[Accelerate](https://www.amazon.com/dp/B07B9F83WM/) is another great book that helps tie company success to engineering practices and outcomes in a way that is useful to influence stakeholders, especially at an executive level.
