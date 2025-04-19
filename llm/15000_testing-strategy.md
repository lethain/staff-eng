# Strategy testing: avoid the waterfall strategy trap with iterative refinement.
url: https://draftingstrategy.com/strategy-testing

If I could only popularize one idea about technical strategy, it would be that
prematurely applying pressure to a strategy's rollout prevents evaluating whether the strategy is effective.
Pressure changes behavior in profound ways, and many of those changes are intended to make you believe your
strategy is working while minimizing change to the status quo (if you're an executive)
or get your strategy repealed (if you're not an executive). Neither is particular helpful.

While some strategies are obviously wrong from the beginning, it's much more common to see reasonable strategies that
fail because they didn't get the small details right.
Premature pressure is one common cause of a more general phenomenon:
most strategies are developed in a waterfall model,
finalizing their approach before incorporating the lessons that reality teaches
when you attempt the strategy in practice.

One effective mechanism to avoid the waterfall strategy trap is explicitly testing your strategy to refine the details.
This chapter describes the mechanics of strategy testing:

* when it's important to test strategy (and when it isn't)
* how to test strategy
* when you should stop testing
* roles in strategy testing: sponsor vs guide
* metrics and meetings to run a strategy testing
* how to identify a strategy that skipped testing
* what to do when a strategy has progressed too far without testing

Let's get into the details.

---

*This is an exploratory, draft chapter for a book on engineering strategy that I'm brainstorming in [#eng-strategy-book](https://lethain.com/tags/eng-strategy-book/).*
*As such, some of the links go to other draft chapters, both published drafts and very early, unpublished drafts.*

*Many of the ideas here came together while working with [Shawna Martell](https://www.linkedin.com/in/shawnamartell/), [Dan Fike](https://www.linkedin.com/in/danfike/), [Madhuri Sarma](https://www.linkedin.com/in/madhurisarma/), and many others in Carta Engineering.*

## When to test strategy

Strategy testing is ensuring that a strategy will accomplish its intended goal at a cost that you're willing to pay.
This means it needs to happen prior to implementing a strategy, usually in a strategy's early development stages.

A few examples of when to test common strategy topics:

* Integrating a recent acquisition might focus on getting a single API integration working
    before finalizing how the overall approach goes.
* A developer productivity strategy focused on requiring typing in a Python codebase might
    start by having an experienced team member type an important module.
* A service migration might attempt migrating both a simple component (to test migration tooling)
    and a highly complex component (to test integration complexity) before moving to a broader rollout.

In every case, the two most important pieces are testing before finalizing the strategy, and testing narrowly with a focus
on the underlying mechanics of the approach.
Avoid getting caught up in solving broad problems like motivating adoption and addressing conflicting incentives.

That's not to say that you need to test every strategy. A few of the common cases where you might not want to test a strategy are:

* When you're dealing with a [permissive strategy](https://draftingstrategy.com/when-write-stratefy/) that's very cheap to apply,
    testing is often not too important; indeed, you can consider most highly-permissive strategies as a test
    of whether it's effective to implement a similar, but less permissive, strategy in the future.
* Where testing isn't viable for some reason. For example, a hiring strategy where you shift hiring into
    certain regions isn't something you can test in most cases, it's something you might need to run for several years
    to get meaningful signal on results.
* There are also cases where you have such high conviction in a given strategy that it's not worth testing, perhaps
    because you've done something nearly identical at the same company before.
    Hubris comes before the fall, so I'm generally skeptical of this category.

That said, my experience is that you should try very hard to find a way to test every strategy.
You certainly should not try hard to convince yourself testing a strategy isn't worthwhile.
Testing is so, so much cheaper than implementing a bad strategy, that it's almost always a good investment of time and energy.

## How to test strategy

For a valuable step that's so often skipped, strategy testing is relatively straightforward.
The approach I've found effective is:

1. Identify the narrowest, deepest available slice of your strategy, and iterate on applying your strategy to that slice until you're confident the approach works well.

    For example, if you're testing a new release strategy for your Product Engineering organization,
    decide to release exactly one important release following the new approach.
2. As you iterate, identify metrics that help you verify the approach is working; note that these aren't metrics to measure adoption, instead measure impact of the change.

    For example, metrics that show the new release process reduces customer impact, or drives more top-of-funnel visitors.
3. Operate from the belief that people are well-meaning, and strategy failures are due to excess friction and poor ergonomics.

    For example, assume the release tooling is too complex if people aren't using it. (Definitely don't assume that people are too resistant to change.)
4. Keep refining until you have conviction that your strategy's details work in practice, or that the strategy needs to be approached from a new direction.

    For example, if the metrics you identified before show the new release process has significantly
    reduced customer impact of the new release.

The most important details are the things you should _not_ do.
Don't go broad where impact _feels_ higher but iteration cycles are slower.
Don't get caught up on _forcing_ adoption such that you're distracted from improving the underlying mechanics.
Finally, don't get so attached to your current approach that you can't accept that it might not be working.
Strategy testing is only valuable because many strategies don't work as intended, and it's much cheaper
to learn that early.

## Testing roles: sponsors and guides

Sometimes the strategy testing process is led by one individual who is able to sponsor the work
(a principal engineer at a smaller company, an executive, etc) and also coordinate the day-to-day work of validating
the approach (a principal engineer at a larger company, an engineering manager, a technical program manager, etc).
It's even more common for these responsibilities to split between two roles: **sponsor** and a **guide**.

The **sponsor** is responsible for:

1. serving as an escalation point to make quick decisions to avoid getting stuck in development stages
2. pushing past historical decisions and beliefs that prevent meaningful testing
3. marshalling cross organizational support
4. telling the story to stakeholders, especially the executive team to avoid getting defunded
5. preventing overloading of strategy (where people want to make the strategy solve _their_ semi-related problem)
6. setting pace to avoid stalling out
7. identifying when energy is dropping and to change the phase of strategy (from development to implementation)

The **guide** is responsible for:

1. translating the strategy into particulars where testing gets stuck
2. identifying slowdowns and blockers
3. escalating frequently to sponsor
4. tracking goals and workstreams
5. maintaining the pace set by the sponsor

In terms of filling these roles, there are a few lessons that I've learned over time.
For sponsors, what matters the most is that they're genuinely authorized by the
company to make the decision they're making, and that they care enough about the impact
that they're willing to make difficult decisions quickly. A sponsor is only meaningful
to the extent that the guide can escalate to the sponsor, who must rapidly resolve those escalations.
If they aren't available for escalations or don't resolve them quickly, they're a poor sponsor.

For guides, you need someone who can execute at pace without getting derailed by various organizational
messes, and has good, nuanced judgment relevant to the strategy being tested.
The worst guides are ideological (they reject the very feedback created by testing)
or easily derailed (you're likely testing _because_ there's friction somewhere, so
someone who can't navigate friction is going to fail by default).

## Meetings & Metrics

The only absolute requirement for the strategy testing phase is that
the sponsor, guide, and any key folks working on the strategy **must meet together every single week**.
Within that meeting, you'll iterate on which metrics capture the current areas you're trying to refine,
discuss what you've learned from prior metrics or data, and schedule one-off followups to ensure you're making progress.

The best version of this meeting is debugging heavy and presentation light.
Any week that you're not learning something that informs subsequent testing,
or making a decision that modifies approach to testing, should be viewed with some suspicion.
It might mean that you've underresourced the testing effort, or that your testing approach is too
ambitious, but it's a meaningful signal that testing is converging too slowly to maintain attention.

If all of this seems like an overly large commitment, I'd push you to consider
your [strategy altitude](https://draftingstrategy.com/when-write-stratefy/) to adjust the volume
or permissiveness of the strategy you're working on.
If a strategy isn't worth testing, then it's either already quite good (which should be widely evident beyond its authors)
or it's probably only worth rolling out in a highly permissive format.

## Identifying strategies that skipped testing

While not all strategies _must_ be refined by a testing phase, essentially all failing strategies skip
the testing phase to move directly into implementation.
Strategies that skip testing _sound right_, but don't accomplish much.
Fully standardizing authorization and authentication across your company on one implementation _sounds right_,
but can still fail if e.g. each team is responsible for its own approach to determining the standard.

One particularly obvious pattern is something I describe as "pressure without a plan."
This is a strategy that only "sounds right" aspect but lacks concrete details.
Service migrations are particularly prone to this, perhaps due to apocryphal descriptions of
Amazon's service migration in the 2000s, which is often summarized as a top-down zero-details mandate to switch away from the monolith.

Identification comes down to understanding two things:

1. Are there numbers that show the strategy is driving the desired impact?
    For example, API requests made into the new authentication service as a percentage of all authentication requests
    is more meaningful than a spreadsheet tracking teams' commitments to move to the new service.
    
    Try to avoid proxy metrics when possible, but to instead look at the actual thing that matters.
2. If the numbers aren't moving, is there a clear mechanism debugging and solving those issues,
    and is this team actually making progress?
    For example, a team that helps with integration with the new authentication service to understand
    where limitations are preventing effective adoption, and who are shipping working code.
    
    Because the numbers aren't moving, you need to find a different source of meaningful evidence to validate that progress is happening.
    Generally, the best bet is either new software running in a meaningful environment (e.g. production for product code).
    It's also useful to talk with skeptics or failed integrations, but be cautious of debugging exclusively with skeptics.    
    They're almost always right, but often they are out-of-date, such that they're right but aren't describing
    current problems.

Unless one of these two identifications are _obviously true_, then it's very likely that you've
found a strategy that skipped testing.

## Recovering from skipped testing

Once you've recognized a strategy that skipped testing and is now struggling,
the next question is what to do about it.
[Should we decompose our monolith?](https://draftingstrategy.com/monolith-decomposition-strategy/) looks at recovering from a failing service migration,
and is lightly based on my experience dealing with similar, stuck service migration at both Calm and Carta.
The answer to a stuck strategy is always: write a new strategy, and make sure _not_ to skip testing this time.

Typically, the first step of this new strategy is explicitly pausing the struggling strategy
while a new testing phase occurs. This is painful to do, because the folks invested in the current
strategy will be upset with you, but there's always going to be people who disagree with any change.
Long-term, the only thing that makes most people happy is a successful strategy, and anything that
delays progress towards that is a poor investment.

Sometimes it is difficult to officially pause a struggling strategy,
in which case you have to look for an indirect mechanism to implicitly pause without
acknowledging it. For example, delaying new services while you take a month to invest into improving service provisioning
might give you enough breathing room to test the missing mechanisms from your strategy,
without requiring anyone to lose face over a failing migration.
It would be nice to always be able to say these things out loud,
but managing personalities is an enduring leadership challenge;
even when you're an executive, you just have a different set of messy stakeholders.

## Summary

Testing doesn't determine whether a strategy might be good. It exposes the missing details required to translate
a directionally accurate strategy into a strategy that works.
After reading this chapter, you know how to lead that translation process as both a sponsor
and a guide. You can set up and run the necessary meetings to test a strategy, and also put together
the bank of metrics to determine if the strategy is ready to leave refinement and move to a broader rollout.