---
title: "Writing engineering strategy"
slug: "/guides/engineering-strategy"
date: "2020-11-02"
kind: "guide"
---

One of the projects from my time at Stripe that I’m proud of was writing our engineering strategy, which I later sanitized into a public version in [Magnitudes of exploration](https://lethain.com/magnitudes-of-exploration/). The strategy was an elegant document that carefully reconciled two worldviews that had initially appeared incompatible within the engineering organization. While it was both a conceptually pure and utterly pragmatic document, in the end, it wasn’t particularly useful. It reflected how we _described_ making tradeoffs as opposed to how we _genuinely_ made tradeoffs.

Excessive optimism is one of several recurring patterns that prevent most companies from creating a useful engineering strategy. The most damaging of those patterns is disagreement on what an engineering strategy ought to accomplish.

Someone in most companies has read [Good Strategy, Bad Strategy](https://lethain.com/good-strategy-bad-strategy/), and can quote Rumelt’s classic definition of strategy as a diagnosis, guiding policy, and coherent action. This is an excellent definition of “strategy” but isn’t entirely what folks mean when they ask your engineering leadership team, “What’s our engineering strategy?” When folks ask for an engineering strategy, [the questions they want to answer are](https://lethain.com/survey-of-engineering-strategies/):



1. What will our organization look like in two to three years?
2. How does my team fit into the broader organization?
3. What are our approved technologies?
4. How do we evaluate and adopt new technologies?
5. What technologies should we use for this particular project?

Companies with cohesive engineering strategies don’t rely on any single document to answer this messy expanse of questions. They guide engineering strategy with three tools: a vision, a collection of context-specific strategies to route towards your vision, and technical specifications that explain the decisions you made at each juncture thus far.


## Definitions

Vision, strategy, and specification are all overloaded terms, so it’s helpful to define how I’m using them.
In fact, my core argument is that when folks ask for "an engineering strategy", it takes all three documents
to properly answer their request.

A **vision** describes how you want your technology and organization to work in two to three years. Tastelessly [quoting myself](https://lethain.com/strategies-visions/), “Visions should be detailed, but the details are used to illustrate the dream vividly, not to prescriptively constrain its possibilities.” It creates lightweight alignment across projects, aligning their vectors’ direction. There are, unfortunately, few public examples of this sort of engineering vision. The closest you can get is to infer a company’s vision from its organizational chart, which also implicitly [reflects its technical architecture](https://en.wikipedia.org/wiki/Conway%27s_law).

A **strategy** guides tradeoffs _and_ explains the rationale behind that guidance. This is the “diagnosis” and “guiding policies” components of _Good Strategy, Bad Strategy_’s definition (the “coherent action” component is handled in your technical specifications). A couple of great examples to refer to are [A Framework for Responsible Innovation](https://multithreaded.stitchfix.com/blog/2019/08/19/framework-for-responsible-innovation/) and [How Big Technical Changes Happen at Slack](https://slack.engineering/how-big-technical-changes-happen-at-slack/).

A **specification** describes the decisions and tradeoffs you’ve made in a specific project, and various companies  might call them RFCs, tech specs, or design docs. If strategies are the “legal precedent” for a given area, then each specification is an individual case. There are many formats to pick from. I’d recommend starting with [Design Docs, Markdown, and Git](https://caitiem.com/2020/03/29/design-docs-markdown-and-git/) and [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/).

For additional concrete examples, refer to [the collection of resources](https://staffeng.com/guides/learning-materials).


## More synthesis than genius

In a computer science course learning about object-oriented design, you might write an _Animal_ class that is later extended by _Dog_ and _Cat_. Starting at the top and working your way down into the details is an efficient way to model a problem because the downstream details uniformly benefit from their inherited constraints.

It’s tempting to follow that same approach when defining your company’s engineering strategy. Start by writing a compelling vision, decompose that into a handful of specific strategy documents, and finally write technical specifications influenced by those strategies. It’s an appealing approach, but it’s not how successful engineering organizations practice strategy. Attempts at top-down engineering strategy ultimately describe how the authors _wish_ things worked rather than how they _actually_ work.

In my first year as CTO at Calm, the most important engineering strategy decision I made was sequencing our move to services firmly _after_ establishing clear interfaces within our monolithic application. Was this the sort of inspiring, audacious strategy that you’d build a vision around in a vacuum? Nope. Was it the thing we needed to align and move forward together effectively? Yep, and this strategy was only obviously important after several technical specifications got caught up in questions around service boundaries and size.

An effective engineering strategy starts with technical specifications that explain the reasoning behind a specific solution to a particular problem. As a pattern becomes more prominent, it is then graduated into a “diagnosis and guiding policy” strategy document. Once you’ve accumulated enough strategy documents, you can finally extrapolate their impact on your long term vision. Even then, your vision and strategies aren’t stone tablets. Instead, they’re living documents that influence and are influenced by each new specification your organization writes.


## Guidelines

Engineering strategy isn’t created by a team of architects, it’s a living corpus that anyone doing any technical work can contribute to. If you’ve viewed your role in engineering strategy as bemoaning that someone else hasn’t done a better job at it, this can be an intimidating inversion of perspective. But it doesn’t have to be an intimidating process if you follow a few guidelines to evolving strategy.


### Start where you are

When you start trying to write an engineering strategy, it’s easy to get overwhelmed by the sheer number of things you don’t know. When you show your initial writings to peers for feedback, don’t be surprised if the first thing they say is, “We need to know our product roadmap for next year before we can write this” or maybe “We need to finalize our long term org structure before we make these decisions.”

Working on strategy, it’s easy to be paralyzed by the inherently vast ambiguity we work in, but you’ve just got to dive in and start writing. Waiting for missing information doesn’t work: every missing document is missing for a good reason. Those documents you’re waiting on will be your Sisyphean boulder, never letting you make forward progress. Rest assured that whatever you write will need to change, and if you write something particularly bad, you’ll quickly realize the need to change it. Where you are now is always the best place to start.

If there are additional materials that would help you, add them to a list. If there are folks who you think are likely to disagree, add them to a list too. If you don’t feel comfortable speaking for the entire engineering organization, then speak from the perspective of your team. If your ideas aren’t perfect, then frame them as an attempt to provoke discussion. If you look for reasons not to get started, you’ll always find them.

On the other hand, sometimes folks try to write reality out of existence by not acknowledging
existing decisions (say, a commitment staying profitable) or ignoring major constraints that genuinely do exist
(say, a large Python monolith). That doesn't work either, you need to acknowledge what exists.
Good strategy aligns with your  business, company and technical realities.

Start wherever you are, and start now.


### Write the specifics

One of the reasons to start by writing technical specifications is that specifications are inherently specific. When you’re describing the design decisions for next week’s projects, there’s a proximity to implementation that focuses you on the details.

Strategies and visions are not inherently specific, and it’s easy to get in trouble by writing overly general statements. It’s pleasant that “We never compromise on quality,” but if five people read that statement they’ll interpret it five different ways. The goal of engineering strategy is to create alignment, but generic statements instead create the illusion of alignment. You’re better off being explicitly not aligned--at least you know it’s an area to work on--than to allow generic statements to mislead you into believing you’re aligned when you aren’t.

When you’re writing strategy and vision, write until you start to generalize, and then stop writing. If you can’t be specific, wait until you’ve written more technical specifications to flow into the strategy (or written more strategies to flow into the vision).


### Show your work

Good strategies and visions are opinionated. If they aren’t opinionated, then they won’t provide any clarity on decision making, which means they won’t create much alignment. Indeed, if your document doesn’t narrow folk’s possible approaches, then you should just skip writing it--it won’t be worth the cognitive load it creates by existing. However, being opinionated on its own isn’t enough.

In math classes growing up, you had to show your work to get full credit. Here too, you must show the rationale behind your opinions. Showing your work builds confidence in the first version of a document, but even more importantly, by showing your work, you make it possible for others to modify and extend your work as the underlying context shifts.


### Synthesize in batch

Effective incident management programs depend on identifying remediations that eliminate entire categories of problems. Failing incident management programs focus on custom fixes that never ladder into something larger. The former look at incidents in batches. The latter look at them individually.

The same logic applies to writing your strategies and vision. If you write a strategy based on a single specification, it’s almost certainly going to be a short-lived strategy. It’s much more effective to look at the specifications in batch, synthesize the common themes, and then write your strategy.


## Practical over audacious

There’s something about the word “strategy” that inspires folks to shove a thesaurus and a lifetime’s supply of ambition into one overwrought document. Sometimes this approach creates a beautiful document, but it’s rarely a useful one. You don’t need to do something flashy to contribute towards engineering strategy. The seeds of your strategy already exists in each of the technical specifications you’ve written. Keep writing specifications. Occasionally synthesize specifications into guiding strategies. Very rarely extrapolate where those strategies are taking you into a shared vision.

If any of that sounds intimidating, don’t get caught up in the challenges; just start writing and the rest will take care of itself as you go. Every successful engineering strategy grows from a single technical specification, slowly accumulating and refining into something uniquely powerful for your particular company and your particular needs.

