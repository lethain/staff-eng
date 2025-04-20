---
title: Writing engineering strategy
url: /guides/engineering-strategy
date: '2020-11-02'
weight: 6000
book_section: Operating at Staff
---

> I kind of think writing about engineering strategy is hard because good strategy is pretty boring, and it's kind of boring to write about. Also I think when people hear "strategy" they think "innovation" - [Camille Fournier](https://twitter.com/skamille/status/1328763503973429250)

Few companies understand their engineering strategy and vision. One consequence of this uncertainty is the industry belief that these documents are difficult to write. In some conversations, it can feel like you're talking about something mystical, but these are just mundane documents. The reality is that good engineering strategy is boring and that it's _easier_ to write an effective strategy than a bad one.

To write an engineering strategy, write five design documents, and pull the similarities out. That's your engineering strategy. To write an engineering vision, write five engineering strategies, and forecast their implications two years into the future. That's your engineering vision.

If you can't resist the urge to include your most brilliant ideas in the process, then you can include them in your prework. Write all of your best ideas in a giant document, delete it, and never mention any of them again. Now that those ideas are out of your head, your head is cleared for the work ahead.

Durably useful engineering strategy and vision are the output of iterative, bottom-up organizational learning. As such, all learning contributes to your organization's strategy and vision, but your contribution doesn't have to be so abstract. Even if you're not directly responsible for that work, there are practical steps that _you_ can take to advance your organization's strategy and vision, starting _right now_.

## When and why

Before diving into the recipe for creating effective strategies and visions,
a good starting question is, "When and why should I actually create them?"
Strategies are tools of proactive alignment that empower teams to move quickly and with confidence.
Strategies allow everyone--not just the empowered few--to make quick, confident decisions that might have otherwise cost them a week of discussion.
Strategies are also the bricks that narrow your many possible futures down enough that it's possible to write a realistic vision.
If you realize that you've rehashed the same discussion three or four times, it's time to write a strategy.
When the future's too hazy to identify investments worth making, it's time to write another vision.
If neither of those sound like familiar problems -- move on to other work for now and return later.


## Write five design docs

Design documents describe the decisions and tradeoffs you've made in specific projects. Your company might call them RFCs or tech specs. Stranger names happen, too; Uber bewilderingly called them DUCKS until they later [standardized on RFC](https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/). A good design document describes a specific problem, surveys possible solutions, and explains the selected approach's details. There are many formats to pick from; a few places to start your thinking are [Design Docs, Markdown, and Git](https://caitiem20.wordpress.com/2020/03/29/design-docs-markdown-and-git/), [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/), and [Technical Decision-Making and Alignment in a Remote Culture](https://multithreaded.stitchfix.com/blog/2020/12/07/remote-decision-making/).

Whether a given project requires a design document comes down to personal judgment, but I've found a few rules useful. You should write design documents for any project whose capabilities will be used by numerous future projects. You should also write design documents for projects that meaningfully impact your users. You should write a design document for any work taking more than a month of engineering time.

A batch of five design docs is the ideal ingredient for writing an effective strategy because design documents have what bad strategies lack: detailed specifics grounded in reality. It's easy for two well-meaning engineers on the same team to interpret an abstract strategy in different ways, but it's much harder to stay misaligned when you're implementing a specific solution.

A few recommendations as you write:

*   **Start from the problem.** The clearer the problem statement, the more obvious the solutions. If solutions aren't obvious, spend more time clarifying the problem. If you're stuck articulating the problem, show what you have to five people and ask them what's missing: fresh eyes always see the truth.
*   **Keep the template simple.** Most companies have a design document template, which is a great pattern to follow. However, those templates are often expanded to serve too many goals. Overloaded templates discourage folks from writing design documents in the first place. Prefer minimal design document templates that allow authors to select the most useful sections and only insist on exhaustive details for the riskiest projects.
*   **Gather and review together, write alone.** It's very unlikely that you personally have all the relevant context to write the best design document on a given topic. Before getting far into the process, collect input from folks with relevant perspectives, particularly those who will rely on the output of your design document. However, be skeptical of carrying that collaborative process into writing the design document itself. Most folks are better writers than they are editors. This means it's usually harder to edit a group document into clear writing than to identify one author to write a clear document. Gather perspectives widely but write alone. Just be careful not to fall in love with what you've written until _after_ you've reviewed it with others.
*   **Prefer good over perfect.** It's better to write a good document and get it in front of others than it is to delay for something marginally better. This is particularly valuable to keep in mind when giving feedback on other folks' designs; it's easy to fall into the trap of expecting their designs to be just as good as your best design. Particularly as you become more senior, it's toxic to push every design to meet the bar of your own best work. Focus on pushing designs to be good, rather than fixating on your own best as the relevant quality bar.

It takes a lot of practice to write great design documents. If you want to improve yours, my best advice is to reread your designs _after_ you've finished implementing them and study the places where your implementation deviated from your plan--what caused those deviations? Oh, and of course, just keep writing more of them.

## Synthesize those five design docs into a strategy

After your organization has written five design documents, sit down and read them all together. Look for controversial decisions that came up in multiple designs, particularly those that were hard to agree on. A recent example of mine was getting stuck debating whether Redis was appropriate as durable storage or only as a cache. Rather than starting from zero in each design document review, wouldn't it be easier if we reviewed our recent decisions about using Redis, reflected on how we made those decisions and wrote them down as a strategy?

Good strategies guide tradeoffs and explain the rationale behind that guidance. Bad strategies state a policy without explanation, which decouples them from the context they were made. Without context, your strategy rapidly becomes incomprehensible--why did they decide this?--and difficult to adapt as the underlying context shifts. A few interesting strategies to read while thinking about writing your own are [A Framework for Responsible Innovation](https://multithreaded.stitchfix.com/blog/2019/08/19/framework-for-responsible-innovation/) and [How Big Technical Changes Happen at Slack](https://slack.engineering/how-big-technical-changes-happen-at-slack/).

If you're a [Good Strategy, Bad Strategy](https://www.amazon.com/dp/B004J4WKEC) convert--and that book has wholly transformed how I think about strategy--then you'll note this definition of strategy is the "diagnosis" and "guiding policies" sections, deferring "coherent action" to the design documents.

My best advice for writing a strategy document is:

*   **Start where you are.** Working on strategy, it's easy to be paralyzed by the inherently vast ambiguity we work in, but you've just got to dive in and start writing. Waiting for missing information doesn't work: every missing document is missing for a good reason. Whatever you write will need to change, and if you write something particularly bad, you'll quickly realize the need to change it. Where you are now is always the best place to start.
*   **Write the specifics.** Write until you start to generalize, and then stop writing. If you can't be specific, wait until you've written more design documents. Specific statements create alignment; generic statements create the illusion of alignment.
*   **Be opinionated.** Good strategies are opinionated. If they aren't opinionated, then they won't provide any clarity on decision making.  However, being opinionated on its own isn't enough. You also need to show your work.
*   **Show your work.** In math classes growing up, you had to show your work to get full credit. Here too, you must show the rationale behind your opinions. Showing your work builds confidence in the first version of a document, but even more importantly, by showing your work, you make it possible for others to modify and extend your work as the underlying context shifts.

Some of the best strategies you write may at the time feel too obvious to bother writing. "When should we write design documents?" is a strategy worth writing. "Which databases do we use for which use cases?" is a strategy worth writing. "How should we stage our migration from monolith to services?"
is worth writing, too. As we leave behind the idea of strategy as demonstrations of brilliance,
we can start to write far more of them, and we can write them more casually. If it ends up not being used, you can always deprecate it later.

## Extrapolate five strategies into a vision

As you collect more strategies, it'll become increasingly challenging to reason about how the various strategies interact. Maybe one of your strategies is to [Run less software](https://www.intercom.com/blog/run-less-software/) and rely more on cloud solutions, but another one of your strategies is to prefer offloading complexity to the database whenever possible. How do you reconcile those strategies if you identify a database that would allow you to offload a great deal of complexity, but that isn't offered by your cloud vendor?

Take five of your recent strategies, extrapolate how their tradeoffs will play out over the next two to three years. As you edit through the contradictions and weave the threads together, you've written an engineering vision. The final version will give you what [Tanya Reilly](https://twitter.com/whereistanya) calls [a robust belief in the future](https://leaddev.com/technical-direction-strategy/sending-gifts-future-you), which makes it easier to understand how your existing strategies relate to each other and simplifies writing new strategies that stand the test of time.

For a useful vision, a few things to focus on are:

*   **Write two to three years out.** Companies, organizations, and technology all change quickly enough that thinking too far into the future is fraught. It also doesn't work if you write a vision that expires in six months--how many strategies would you realistically write within that six-month window? Try to focus on two to three years out; you can expand that horizon a bit if you're a fairly established company.
*   **Ground in your business and your users.** Effective visions ground themselves in serving your users and your business. That tight connection keeps the vision aligned with your leadership team's core values--users and business. Bad visions treat technical sophistication as a self-justifying raison d'être--a view that is never shared by your company's leadership.
*   **Be optimistic rather than audacious.** Visions should be ambitious, but they shouldn't be audacious. They should be possible, but the best possible version if possible. Do write what you could accomplish if every project is finished on time and without major setbacks. Don't write what you think would be possible with infinite resources.
*   **Stay concrete and specific.** Visions get more useful as they get more specific. Generic statements are easy to agree with but don't help reconcile conflicting strategies. Be a bit more detailed than you're comfortable with. Details in visions are often illustrative rather than declarative, giving a taste of the future's flavor rather than offering a binding commitment.
*   **Keep it one to two pages long.** The reality is that most people don't read long documents. If you write something five or six pages long, readers will start dropping off without finishing it (or will skim it very rapidly without engaging with the details). Force yourself to write something compact, and reference extra context by linking to other documents for the subset of folks who want the full details.

After you finish writing your vision, the first step folks usually take is sharing it widely across the engineering organization. There is so much work behind the vision--five design docs for each strategy, five strategies for one vision--it's hard _not_ to get excited when you're done. So excited that it's easy to get discouraged, then, when the response to your strategy will almost always be muted. There are a few reasons for the muted response. First, the core audience for your vision is folks writing strategies, which is a relatively small cohort. Second, a great vision is usually so _obvious_ that it bores more than it excites.

Don't measure vision by the initial excitement it creates. Instead, measure it by reading a design document from two years ago and then one from last week; if there's marked improvement, then your vision is good.

