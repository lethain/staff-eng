---
title: Staff-plus interview processes
url: /guides/staff-plus-interview-process
date: '2020-07-12'
weight: 93000
book_section: Resources
---

When we talk about designing a Staff-plus engineer interview loop, the first thing to talk about is that absolutely no one is confident their Staff-plus interview loop works well. Many loops end up looking for a senior engineer who's _really_ fast at solving problems, which doesn't reflect the actual role. Others focus on communication skills, which _are_ a key part of the role but certainly not the entirety of it. A few companies even construct their process to assess whether the candidate _feels_ like a member of their existing senior engineering team, conflating excellence with familiarity.

Even if no one feels great about their loop, there is still a body of collective learnings to incorporate into your attempt to design a loop, which is what we'll cover here. We'll start with examining the frequent failure modes of Staff-plus interview loops, discuss the signals that you _do_ want to test for in these loops, and finally discuss some interview formats which can be useful for assessing those signals.

## Challenges

While technology interviews, in general, are a bit of a mess, interviews for very senior candidates have enough issues of their own to pack a dedicated struggle bus. It's helpful to start with understanding some of the common failure modes before we move into considering what might work better:

* **A senior engineer, but better.** Many interview processes look at Staff-plus engineers as Senior engineers who are a bit better at everything. They're a bit faster. They're a bit clearer in their communication. They're a bit more nuanced in architecture discussions. This stems from most folks being unfamiliar with Staff roles and usually causes Staff-plus engineers to perform poorly on these loops. In particular, most Staff-plus engineers are programming less than Senior engineers, and consequently are _slower_ rather than _faster_ at rote programming tasks. You'll find some Staff-plus engineers who remain very quick programmers, but you won't find much correlation between that speed and their impact.
* **A senior engineer, but worse.** Conversely, other interview processes recognize that Staff-plus engineers are spending less time programming and anticipate slower performance on some of the more mundane programming exercises. This makes it more likely for Staff-plus engineers to succeed in the loop but doesn't get signal on what makes these sorts of engineers exceptionally impactful. If you don't add additional interviews to capture those strengths, reduced speed on rote work will likely correlate with seniority to some extent, but it correlates more strongly with many other factors.
* **A senior engineer, but they'll accept the offer.** Another failure mode is companies that are struggling to hire Senior engineers and decide to inflate their titles without changing the role expectations. In these cases, the interviews are appropriate to the actual work, but the title isn't. With neither the company nor the candidate fully willing to acknowledge the inflation, all future Staff-plus hiring at the company acquires a veneer of uncertainty.
* **Someone like us.** Many loops focus on whether the Staff-plus candidate _projects_ the same wisdom and confidence as the existing Staff-plus engineers at the company, where the interview debrief might include statements like, "They feel like they'd be a natural part of this team." This sort of approach is more likely to anchor on semi-arbitrary features like how they project their confidence than on the candidate's capabilities.
* **Not better than me.** Especially when hiring your first Staff-plus engineers, you'll often find some earlier career interviewers who undervalue the candidate's strengths and instead anchor on the candidate's capability to perform the interviewer's current role. You'll have an impressive Staff-plus candidate, but the interview panel will be skeptical of their ability to thrive as a mid-level engineer. This seems to be brought up most frequently for women and minority candidates.
* **The reverse filter.** Certain kinds of interviews are signals that you as an organization don't know how to use Staff-plus engineers: whiteboard algorithmic interviews, interviewers are predominantly early career, and so on. Many Staff-plus processes cause the best candidates to opt-out early in the process, often somewhat invisibly to the recruiting metrics.
* **Too title-oriented?** At a certain level of accomplishment, people don't care much about internal leveling, generally because they're already financially secure. This creates a peculiar pressure on folks newly reaching Staff-plus levels to avoid appearing overly career or title motivated, making it harder for folks to attain the title for the first time.

Some of these are quite difficult to address, others are easy as long as you keep them in mind, but all of them are worth considering as you start to design or re-envision your Staff-plus interview process.

## Signals

The [best interview loops](https://lethain.com/designing-interview-loops/) reason forward from the signals you want to capture back to the interview topics and format, which means the first important question to answer is, "Which signals are important for hiring successful Staff-plus engineers?"

The signals I'd recommend focusing on are:



* **Self-awareness**. Are they accountable for mistakes? Have they demonstrated growth in areas where they've previously been weaker?
* **Judgment.** Are they able to see around corners to identify problems? Are they able to navigate broad, ambiguous problems? Can they effectively mediate between folks in an argument about tradeoffs or design? Can they derisk the execution of difficult problems?
* **Collaboration.** Do they partner well with others? What about folks less experienced than them? More experienced than them? Their managers? Cross-functionally? Executives?
* **Communication.** Are they good listeners who understand the points made by others? Are they able to communicate their ideas clearly? Can they communicate in the formats that your company relies upon (written, verbal, etc)?
* **Development.** Do they grow others around them? Does the "organizational bench" grow in areas they lead or atrophy? Do broken systems and processes get cleaned up?

It's interesting to note that many would not consider these to explicitly be technical skills. Domain expertise is a major factor in success at all of them, but it's exercising that expertise in conjunction with other critical skills and behaviors that transition someone from a tenured Senior engineer into a Staff-plus one.

## Formats and structures

The two key questions to ask yourself when designing an interview loop are always:



1. What tasks and behaviors will this person need to succeed on a day to day basis?
2. How can we get them to demonstrate actually doing them?

Most senior candidates become increasingly diplomatic and _asking_ them about their work is never as helpful as _watching_ them do the work. If mentorship is the most important activity, don't rely on them talking about mentorship, but instead find a way to _see_ them mentoring someone. If it's architecture, present your current systems and ask them to bring their questions to see how they react to decisions they disagree with -- get away from the ambiguous abstract.

Moving beyond the typical one-on-one discussions and programming interviews, some of the interview formats and structures that I've found particularly effective for evaluating Staff-plus signals are:



* **Structured presentation.** Have the candidate prepare and present for twenty to thirty minutes on a narrow topic to a group of peers. The format gives a great signal on structured thinking, communication, listening to, and answering questions. Depending on the topic you select, you can get strong signals on one or two areas of your choice. This format is particularly effective at hearing how folks talk about their peers and coworkers.
* **Code review.** Prepare a pull request and ask the candidate to provide feedback on it, focusing on empathy, clarity, and usefulness.
* **Data modeling, interfaces, and architecture.** Have the candidate walk through the design of a system, typically with a focus on evolving it to meet changing requirements. These interviews often try to do too much: narrow your focus and add layers to the question to allow you to continue drilling deeper for candidates who make significant progress.
* **Subject matter expertise.** Interviews that test their areas of domain expertise. For example, a frontend engineer might collaborate with a designer and product manager on how technical constraints would impact a proposed design and launch timeline. For backend engineers, you might provide the candidate with a broken piece of software or environment and have them debug the problem back to a fix.
* **Mentorship panel**. It's challenging to hire Staff-plus candidates if your panel consists entirely of earlier career folks, but it's equally risky to hire a Staff-plus candidate if they haven't demonstrated success mentoring folks earlier in their careers. Have a panel of three to four folks they might be expected to mentor come with questions. Watching folks redirect roughly framed questions into a useful discussion is an especially great insight into their ability to mentor in their new role.

If these formats aren't enough, then start asking around! Most companies have designed bespoke approaches to their Staff-plus loops, and you can learn a great deal from that discussion.

## How to pull it together

You might reasonably expect this to end with a precompiled interview loop for your company to use to evaluate Staff-plus engineers, and I hate to disappoint, but I think most of the value comes from thinking through the signals that matter to you and designing formats that get at those signals in a way that resonates to you and your company.

Whatever interviews you end up using, test them, gather candidate feedback, and keep evolving them to be better!
