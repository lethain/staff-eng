---
title: Staff projects
url: /guides/staff-projects
date: '2020-09-09'
weight: 18000
book_section: Getting the title where you are
---

> There isn't an explicit expectation, nor is it listed anywhere as a formal requirement, but it is understood that you'll complete a Staff Project to get promoted. I can't think of any Staff promotion that didn't include a really strong project, typically a multi-person project where the engineer was the Tech Lead.  
> \- [Ritu Vincent](/stories/ritu-vincent)

A popular recurring idea around reaching a Staff-plus role is that first, you need to successfully complete a "Staff project." This is a project that is considered complex and important enough that the person who completes it has proven themselves as a Staff engineer. However popular this idea is, if you're pursuing a Staff-plus role, it's important to pierce the mythology of these projects and focus on the experiences of folks who've walked the path before you.

The short answer on Staff projects is that most engineers don't complete one as part of reaching a Staff role, although a large minority do complete one, particularly folks who attain the role via promotion at a company they've grown up in. For the folks who don't complete one, typically, it's either because they accumulated a track record of success over a longer period without a single capstone or because they switched companies to reach the title.

We'll dig into a few different angles on staff projects:

1. Folks who didn't complete Staff projects
2. Folks who did complete Staff projects, including where they don't end up working as planned
3. Identifying and approaching your Staff project

Into the messy details, we go.

## No Staff project required

When I asked folks whether they had a Staff project, some of the answers were quite concise:

* [Joy Ebertz](https://staffeng.com/stories/joy-ebertz), _"I actually didn't really have a Staff Project."_
* [Diana Pojar](https://staffeng.com/stories/diana-pojar), _"No, I did not have an assigned 'Staff Project,' and that is not something that is part of the promotion process at Slack."_

Some folks were even skeptical of the Staff project concept overall. [Nelson Elhage](https://staffeng.com/stories/nelson-elhage ) said,

> I'm instinctively a little bit wary of this sort of idea of a staff project, in part because one of the archetypes of Staff engineers that I've seen are people who don't necessarily run grand projects themselves or do big things. But just are sort of incredibly effective gurus and routers who make the whole engineering organization run better.

There are also folks like [Dan Na](https://staffeng.com/stories/dan-na) or [Damian Schenkelman](https://staffeng.com/stories/damian-schenkelman) who took a detour through engineering management to reach the role. Damian describes bypassing the Staff project,

> I did not. Because of how I grew at Auth0, I kind of "skipped that part". As a Director at a startup, I got the opportunity to technically lead a lot of big, critical initiatives, but there was no specific/explicit "staff/principal project."

From these stories, it's clear that anyone who tells you that you _must_ complete a Staff project to reach a Staff-plus title is wrong: there are many avenues to reach Staff-plus titles without doing a Staff project, with [a stint in engineering management](https://charity.wtf/2017/05/11/the-engineer-manager-pendulum/) prominent among them.


## Staff project required

However, it's also true that many companies require, or informally enforce, Staff projects for internal promotions, and consequently, many folks do take on a Staff project as part of their role transition.

[Ritu Vincent](/stories/ritu-vincent) describes her experience at Dropbox,

> I definitely had a Staff Project. Back in the day, Dropbox was initially a consumer product that people downloaded and installed on their machines. When we launched Dropbox for Business, there was a request for both your personal and work Dropbox accounts to work simultaneously, including being able to switch across them without needing to log out and log back in.
> The initial implementation was written under immense time pressure, and it ran multiple Dropbox processes. One for your personal account and another for business. My Staff project was to make it so a single Dropbox process could run with multiple users logged in. The hard part was that the project stretched from the kernel all the way to the user interface. I had to understand every single layer of the Dropbox system.
> Initially, we thought it would take six months, and it ended up taking eighteen months. It took up most of the Desktop Client team's resources for quite a while.

[Ras Kasa Williams](https://staffeng.com/stories/ras-kasa-williams) joined an inflight project that he later became the lead on, which served as his Staff project:

> I joined Mailchimp as a Senior engineer. I was immediately added to a project team (which included an Engineering Director and two Principal engineers) meant to build out Mailchimp's first internal, self–service analytics platform.
> A key aspect of this project was being effective and executing at a high level. For better, or for worse, having two other Principal engineers meant expectations for me likely weren't that high. But I was able to jump in immediately and start contributing to core aspects of the project with very little hand-holding from them; by the end, I was one of the key contributors on the team. I would ultimately be formally installed as a tech lead to help continue shepherding that project work as it was absorbed into my current engineering group, Data Services.

Few companies write down their Staff project requirements. They're more frequently the sort of "soft gate" that's brought up during a promotion meeting, sometimes to the surprise of both the manager and the would-be Staff engineer. The most reliable technique for uncovering these requirements is your "sure thing" promotion not getting approved, but that isn't much fun. Almost as reliable and much less frustrating is relying on the strategy of [maintaining and getting feedback on your promotion packet](https://staffeng.com/guides/promo-packets) well in advance of your promotion attempt.


## Why you should do a Staff project

Sometimes it's hard to determine the precise line between gatekeeping and evaluation, and the premise of a Staff project exists in that hazy realm. Taking on a project of immense scope, navigating that ambiguity, and delivering it successfully is an effective way to distinguish folks who've reached Staff-plus impact, but it's also clear that many folks attain Staff-plus roles without completing such a project.

My advice is that although you can attain a Staff-plus role without completing a Staff project, they're a particularly valuable opportunity to develop yourself as an engineer. You will _personally_ be stretched and grown by this kind of project in a way that you won't be by other varieties of Staff level work.

[Keavy McMinn](https://staffeng.com/stories/keavy-mcminn) describes how her Staff project helped her,

> I've never heard it given a name, but I understand the idea. I did lead and architect that type of project - solving gnarly engineering problems, with large impact for the company - a few times, but unfortunately, they didn't lead to me being promoted. They did lead to my career progression though. Those projects gave me the experience, knowledge, and confidence to position myself differently. Even to give public conference talks or know that "I've done X and could do X again."

Although each of these projects is different, there are a few typical characteristics that capture why they're so effective at stretching you as an engineer:



* **Complex and ambiguous** - early in your career, you're given well-defined problems, but as you get deeper into it, you'll increasingly encounter poorly defined or undefined problems, and Staff projects will generally start with a poorly scoped but complex and _important_ problem. Your project might start with only the assertion that your company's aging monolith is crippling product development. From that broad, unclear (and potentially wrong) statement, you'll have to identify a concrete approach that works.
* **Numerous and divided stakeholders** - the easiest projects start with organizational alignment around both the problem and the solution, but your Staff project might likely start with neither. It might be an area which management views as an existential risk, but many engineers feel it is good enough. It might be an area that everyone agrees is a problem, but with strong factional disagreement about approach, for example, disagreement between pursuing a service strategy or reinvesting in your existing monolith.
* **Named bet where failure matters** - it's going to be a project important enough that senior leadership talks about it at all-organization or all-company meetings. This means folks will be watching your work closely, and any failures will be very visible. Success will be highly visible, as well!

If you meet these, it's probably a staff project. These can be pretty nerve-wracking, which is also why they're so effective at developing you.


## Getting access to Staff projects

While deciding that you want to take on a Staff project is the first step, you still need to get _access_ to these projects, which depends on your management chain trusting you enough to bet on your success.

This comes down to three factors.

1. First is learning to stay aligned with your leadership team, some strategies for which are described in [Getting in the room](https://staffeng.com/guides/getting-in-the-room) and [Staying aligned with authority](https://staffeng.com/guides/staying-aligned-with-authority).
2. Second, you need to be known to have the technical aptitude for the problem at hand, which requires [Being Visible](https://staffeng.com/guides/being-visible).
3. Third, is less in your control, which is your company having a pressing need to solve a Staff-level problem, which can require some patience.


## Should you pursue a Staff project?

In summary, if you're looking to get promoted within your current company and haven't previously held a Staff or management title before, then you'll likely need to pursue a Staff project to establish yourself at that level. In other cases, you likely won't.

In any case, it's worth keeping in mind that whether or not these projects are required, they are also some of the most challenging work you can find and are the sort of work that will stretch and develop you into a better engineer. In the short-term pursuit of the title, it may well be optimal to avoid these projects, but in the long-term pursuit of self-growth, they're irreplaceable.
