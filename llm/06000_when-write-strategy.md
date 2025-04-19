# When to write strategy, and how much?
url: https://draftingstrategy.com/when-write-stratefy

Even if you believe that strategy is generally useful,
it is difficult to decide that today is the day to start writing engineering strategy.
When you do start writing strategy, it's easy to write so much strategy that
your organization is overwhelmed and ignores your strategy rather than
investing time into understanding it.

Fortunately, these are universal problems, and there are a handful of
useful mental models to avoid both extremes.
This chapter covers:

* when to write strategy, in particular the pain points (like cross-team friction)
    and opportunities (like senior hires) that are good moments to start writing
* how much strategy your organization can tolerate, avoiding the traps of writing so much that it's ignored
    or so little that there's not much impact
* using strategy altitude--how permissive a given strategy is and where it's implemented--to manage the overhead
    that strategies creates
* mechanisms to debug whether you're doing too much or too little strategy work

When you're done reading it, you should have a clear perspective on
when to start writing strategy, determining how many strategies to write,
and using strategy altitude to reduce overhead when you do decide to write a
high-volume of strategies.

## When to write strategy

Shortly after becoming Calm's CTO, I opened a document, titled it “Engineering Strategy”, and then stared into that blank abyss before putting it away for a year.
A year later, I came back and documented three guiding principles: [choose boring technology](https://mcfunley.com/choose-boring-technology), resolve conflict with curiosity, and prefer vendors for commoditized functionality.
These simple statements greatly reduced conflict in decision making, and allowed us to focus more energy on improving our product.
When I started, I'd felt like we needed a clearer strategy, but I just didn't know what to write at that point, so I wrote nothing.

Often writing nothing is the best available choice. Indeed, a common slur against leaders is that they "want to be strategic," implying that they're too focused
on abstract ideas rather than on the concrete needs of today. Behind that allegation is an important
truth: strategy work isn't always the most valuable thing you can spend your time. Sometimes working on
strategy is [just snacking](https://staffeng.com/guides/work-on-what-matters/) to avoid something more important.

Before you start working on strategy, you have to decide whether now is the correct time, which depends
on your organization's current strategic state, the trend of your strategic state over time,
and whether you have enough context to be effective.

The first of those three criteria is the idea of strategic state.
Using the example of [service architecture strategy](https://draftingstrategy.com/monolith-decomposition-strategy/),
your engineering organization is going to be in one of three strategy states:

1. **Globally consistent**: there is a clearly agreed upon strategy, even if it's not written down. When you ask different members of the team
    how to approach a given problem, you get similar answers.
    
    For example, everyone agrees to write new product functionality in the existing monolithic codebase.
2. **Consistent within teams**: there is a clear strategy within pockets of the organization, but there's some inconsistency
    across pockets.
    
    For example, product engineering believes all new functionality should be in a new service within a shared monorepo,
    but all platform engineering believes new functionality should be implemented in a monolith.
3. **Highly varied**: there's little agreement across individuals within engineering on how to approach problems.
    
    For example, some engineers want to do work in new services in a monorepo, others in new services in polyrepos,
    and some believe in implementing new functionality in an existing monolithic service.

If your organization is globally consistent, then it's unlikely that doing more strategy work will be useful unless
your organization is consistently deciding upon an undesirable approach.
If you're in one of the later two states, then it's likely a useful time to write some strategy.

Even if the current state is good, if the organization is trending towards a worse state, it's a valuable time to start doing strategy work.
Conversely, if the current state is decent, and trending towards something better, it's likely not a valuable opportunity.
There are a handful of recurring causes that can lead to abrupt, sometimes unexpected, shifts in state:

1. How much you are, or aren't, hiring. Uber doubled engineering headcount every six months for four years,
    along with opening many distributed engineering offices, which led to highly varied approaches.
    This also meant that the tenure of most engineers was quite low, driving up inconsistency even more.
2. Whether your newly hired external leaders are more playbook-driven or more responsive to the organization's current context.
    Although it's a known anti-pattern in [executive onboarding](https://lethain.com/first-ninety-days-cto-vpe/),
    many leaders are so desperate to make an early impact that they forget to diagnose their new environment
    before making sweeping changes. This creates a strategy rift between teams aligning with the new direction and teams
    maintaining the existing software and infrastructure.
3. How frequently you have significant organizational changes such as reorganizations or layoffs.
    These events can break the mechanisms that propagate culture, which are the sort of subtle [glue work](https://noidea.dog/glue)
    which often gets ignored in spreadsheet-driven exercises.
4. How effectively you've documented historical decisions, and how well you communicate them during onboarding.
    Some companies drill new hires on how decisions are made, and others expect teams to do the training locally.
    Both approaches can work well. Both can work poorly.

Finally, even if the current state is poor and getting worse, you have to assess whether _you_ understand
the organization well enough to start doing useful strategy work. Many new leaders jump in, make assumptions without testing them,
and [attempt a massive migration](https://lethain.com/grand-migration/). That might _feel_ like an audacious example of driving strategy,
but it's mostly just anxiety or ego wrapped in a gantt chart.

The question to ask yourself is whether you understand the history around the areas you want to change,
the individuals who made the decisions, and the context that made them good decisions at that time.
If you know those things for the areas you're focused on, then you're ready to step into strategy.
If not, it's worth slowing down to build the relationships and context necessary to make your subsequent work useful.

If things could be better, or are trending down, and you know enough about the company to get started, then it's
time to start working on strategy.

## How many strategies?

The next question you'll run into after starting work on strategy is: _how much_ strategy should you undertake?
Is it something about programming language choice? Or service decomposition? Or how you prioritize bugs?
Or is it about data warehouses? What about doing all four at once?

With genuinely infinite potential strategies you could work on, it's hard to decide where to start.
By far the most valuable decision you can make is to [limit work in progress](https://lethain.com/limiting-wip/), even if it means starting smaller than you want.
Generally what I've found effective is to start small, iterate on small pieces until you get them working, and only then move on to something larger.
Limit yourself to developing one or two strategies at a time. This gives you bandwidth to ensure the strategies actually work.

To remain effective while limiting concurrent strategy development, it's important to have a clear, but lightly held, point of view
about where you want to get over time. Having a strategy destination makes it possible for each of these smaller chunks to ladder
up into something larger.

Grounding that in a concrete example: at Uber, we were having reliability and productivity issues
related to the monolithic Python codebase. My team didn't have the ability to forbid commits there, but we did have the ability to
make service provisioning really, really easy. So we created a strategy around making service provisioning and operation as painless
as possible. The strategy aimed to solve a later problem of decomposing and departing the monolith, but we didn't address that directly.
We focused on the first step, believing that it was a necessary prerequisite for the subsequent steps. After we proved out the first step,
it then became possible to work strategy on the subsequent steps.

If we had started with the broader strategy, we might have gotten stuck having an intellectual debate about what should happen in the future,
and required many different teams to buy our future vision without having any concrete step for them to take today. By narrowing down, we were
able to iterate on the prerequisites, and delay building consensus until there was a concrete step we needed folks to take.
At that point, there was no intellectual debate about whether it was possible because most people were already operating as we intended.

One of the challenges with reducing the volume of concurrent strategies is that it appears unambitious.
In the Uber example, we _needed_ to solve development in the monolithic codebase, but instead we were talking about
service provisioning, which from a distance seemed like we'd lost the plot. This is a recurring challenge with effective
strategy development: it can appear overly conservative.
Even though in practice it's usually the fastest solution to the underlying problem, it often comes across as slow or indirect.
Solving the appearance of unambition requires proactive storytelling to your stakeholders to explain
both the incremental initiative and the broader vision it will expand to fill over time.

Sometimes this isn't just a stakeholder problem: it can feel slow to you as well.
In those moments, I try to remember that [friction isn't velocity](https://lethain.com/friction-vs-velocity/) and
think about Digg's engineering strategy when I joined.
We had an extremely clear and consistent architecture (a PHP frontend, Python services, Cassandra for all storage),
but the company still collapsed around us.
A few strategies that work are more valuable than a bunch of strategies, even good ones, in a burning building.

## Strategy altitude

Sometimes you _do_ want to lay out a broad, comprehensive strategy,
and you want to do it quickly. That violates the general rule of developing
one strategy at a time, but there's one helpful idea that can often
make this possible: strategy altitude.

It's easiest to explain this idea by starting with a few examples of
operating at different altitudes:

1. A developer experience team wants to increase code quality.
    They create a mechanism that allows teams to define linting rules
    for their own builds. The developer experience team creates opinionated defaults for teams to adopt,
    but each team is empowered to override those defaults locally.
    
    This is a permissive strategy at the engineering organization altitude.
2. A CTO wants to increase code quality.
    They mandate that every pull request must include a test and that CI/CD should block merging pull requests
    that reduce code coverage.
    
    This is a proscriptive strategy at the engineering organization altitude.
3. A product engineering team wants to decrease security vulnerabilities in their software.
    They tell engineers that it's important to consider a number of security issues when
    implementing software, and includes resources for engineers to educate themselves.
    
    This is a permissive strategy at the team altitude.
4. A product engineering team wants to reduce user-impacting bugs.
    They decide that their planning sprints will schedule bug fixes first,
    and only schedule features after draining the bug backlof.
    
    This is a proscriptive strategy at the team altitude.

Permissive strategies are less expensive than prescriptive strategies, because they require little-to-no enforcement.
Lower-altitude strategies (e.g. team strategies) are less expensive than higher-altitude strategies (e.g. org or company strategies),
because they can rely on local mechanisms for rollout and maintenance rather than oversaturated and lossy mechanisms for wider communication
(e.g. communicating in engineering-wide chat channels is, at best, ineffective).

Pulling these ideas together, the formula to increase
strategy volume, is to either reduce altitude or increase permisiveness. Or both.

Going into a concrete example, when I joined Carta, I worked across engineering to roll out quite a bit of strategy work in the first six months.
Some of this was documenting existing strategy, so it didn't require much adoption overhead.
Other parts were a shift in approach, so we focused on developing permissive strategies.
Every strategy included an escape hatch to support local customization, generally asking
each team's [Navigator](https://lethain.com/navigators/) (a Staff-plus engineer responsible for that area) to override
the strategy as appropriate. There was only one place where I was highly proscriptive, which was around
provisioning new services--there, the escape hatch was more restrictive, requiring escalating to the CTO.

Because we focused on permissive strategies, we were able to cover a broad range of topics at high altitude.
If I'd been more proscriptive, the approach would have certainly failed, even though I might have looked like
a more courageous leader. Annoyingly, looking effective and being effective tend to be only lightly correlated.

## Are you doing too much?

Although many engineers feel that their company doesn't have a clear engineering strategy,
it's my experience that significantly more leaders fail by attempting too much strategy work
than by attempting to do too little.

To debug whether you're doing too much, the most valuable question you can ask
is whether your prior strategy work has impacted the subsequent decisions being made.

If you've shared out a bunch of strategy work, but it doesn't seem to be impacting
how your software is written, then you should scale back.
Instead, focus on getting just a single strategy working well, and deeply understand
what's gone wrong in your prior efforts. Then, and only then, return to your prior
work and fix it. Finally, and only after completing the prior steps, expand further.

You may also be doing good work, but simply overwhelming the organization with too much.
Adopting new approaches is hard, and changing everything at once is overwhelming.
Adjust your strategy altitude to make strategies easier to adopt, and slow down on
adding more until the existing ones have been fully adopted.

## Summary

After reading this chapter, you know when it's effective to write strategy, and how to pace yourself to write
a reasonable volume of strategies. You can use strategy altitude to make strategies easier to
adopt, and can debug whether you're overwhelming your organization with too much strategy work.

If you take nothing else away from this chapter, try to always be working on exactly one strategy.
Doing more feels like progress, but usually fails. Doing less is always a missed opportunity.