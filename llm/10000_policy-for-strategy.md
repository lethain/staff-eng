# Setting policy
url: https://draftingstrategy.com/policy

This book's introduction started by defining strategy as "making decisions."
Then we dug into [exploration](https://draftingstrategy.com/explore/),
[diagnosis](https://lethain.com/diagnosis-for-strategy), and
[refinement](https://draftingstrategy.com/refine/).
Those are three chapters where you could argue that we didn't decide anything at all.
Clarifying the problem to be solved is the prerequisite of effective decision making, but eventually decisions do have to be made.
Here in this chapter on policy, and the [following chapter on operations](https://draftingstrategy.com/operations/), we finally start making some decisions.

In this chapter, we'll dig into:

* How we define policy, and how setting policy differs from operating policy as discussed
    in the next chapter
* The structured steps for setting policy
* How many policies should you set? Is it preferable to have one policy, many policies,
    or does it not matter much either way?
* Recurring kinds of policies that appear frequently in strategies
* Why it's valuable to be intentional about your strategy's altitude,
    and how engineers and executives generally maintain
    different altitudes in their strategies
* Criteria to use for evaluating whether your policies are likely to be impactful
* How to develop novel policies, and why it's rare
* Why having multiple bundles of alternative policies is generally
    a phase in strategy development that
    indicates a gap in your diagnosis
* How policies that ignore constraints sound inspirational,
    but accomplish little
* Dealing with ambiguity and uncertainty created by missing strategies
    from cross-functional stakeholders

By the end, you'll be ready to evaluate why an existing strategy's policies are struggling
to make an impact, and to start iterating on policies for strategy of your own.

## What is policy?

Policy is interpreting your [diagnosis](https://draftingstrategy.com/diagnosis/) into a concrete plan.
That plan will be a collection of decisions, tradeoffs, and approaches.
They'll range from coding practices, to hiring mandates, to architectural decisions,
to guidance about how choices are made within your organization.

An effective policy solves the entirety of the strategy's diagnosis,
although the diagnosis itself is encouraged to specify which aspects can be ignored.
For example, the [strategy for working with private equity ownership](https://draftingstrategy.com/private-equity-strategy/)
acknowledges in its diagnosis that they don't have clear guidance on what kind of reduction to expect:

> Based on general practice, it seems likely that our new Private Equity ownership will expect us to reduce R&D headcount costs through a reduction. However, we don’t have any concrete details to make a structured decision on this, and our approach would vary significantly depending on the size of the reduction.

Faced with that uncertainty, the policy simply acknowledges the
ambiguity and commits to reconsider when more information becomes available:

> We believe our new ownership will provide a specific target for Research and Development (R&D) operating expenses during the upcoming financial year planning. We will revise these policies again once we have explicit targets, and will delay planning around reductions until we have those numbers to avoid running two overlapping processes.

There are two frequent points of confusion when creating policies
that are worth addressing directly:

1. Policy is a subset of strategy, rather than the entirety of strategy,
    because policy is only meaningful in the context of the strategy's diagnosis.
    For example, the ["N-1 backfill policy"](https://draftingstrategy.com/private-equity-model/) makes sense in the context of [new, private equity ownership](https://draftingstrategy.com/private-equity-strategy/).
    The policy wouldn't work well in a rapidly expanding organization.
    
    Any strategy without a policy is useless, but you'll also find policies without context
    aren't worth much either. This is particularly unfortunate, because so often
    strategies are communicated without those critical sections.
2. Policy describes how tradeoffs should be made, but it doesn't verify how the tradeoffs
    are actually being made in practice.
    The next chapter on operations covers how to inspect an organization's behavior to ensure policies
    are followed.
    
    When reworking a strategy [to be more readable](https://draftingstrategy.com/readable-strategy/),
    it often makes sense to merge policy and operation sections together.
    However, when drafting strategy it's valuable to keep them separate.
    Yes, you _might_ use a weekly meeting to review whether the policy is being followed,
    but whether it's an effective policy is independent of having such a meeting,
    and what operational mechanisms you use will vary depending on the number of policies
    you intend to implement.

With this definition in mind,
now we can move onto the more interesting discussion of how to set policy.

## How to set policy

Every part of writing a strategy feels hard when you're doing it,
but I personally find that writing policy either feels uncomfortably
easy or painfully challenging. It's never a happy medium.
Fortunately, the exploration and diagnosis usually come together
to make writing your policy simple: although sometimes that simple
conclusion may be a difficult one to swallow.

The steps I follow to write a strategy's policy are:

1. **Review diagnosis** to ensure it captures the most important themes.
    It doesn't need to be perfect, but it shouldn't have omissions so obvious
    that you can immediately identify them.
2. **Select policies** that address the diagnosis.
    Explicitly match each policy to one or more diagnoses that it addresses.
    Continue adding policies until every diagnoses is covered.

    This is a broad instruction, but it's simpler than it sounds because you'll
    typically select from policies [identified during your exploration phase](https://draftingstrategy.com/explore/).
    However, there certainly is space to tweak those policies,
    and to reapply familiar policies to new circumstances.
    
    If you do find yourself developing a novel policy,
    there's a later section in this chapter, _Developing novel policies_,
    that addresses that topic in more detail.
3. **Consolidate policies** in cases where they overlap or adjoin.
    For example, two policies about specific teams might be generalized into a policy about all teams
    in the engineering organization.
4. **Backtest policy** against recent decisions you've made.
    This is particularly effective if you maintain a [decision log](https://infraeng.dev/decision-log/)
    in your organization.
5. **Mine for conflict** once again, much as you did in developing your diagnosis.
    Emphasize feedback from teams and individuals with a different perspective than your own,
    but don't wholly eliminate those that you agree with.
    Just as it's easy to crowd out opposing views in diagnosis if you don't solicit their input,
    it's possible to accidentally crowd out your own perspective if you anchor too much on others' perspectives.
6. **Consider refinement** if you finish writing, and you just aren't sure your approach works -- that's fine!
    Return to the refinement phase by deploying [one of the refinement techniques](https://draftingstrategy.com/refine/) to increase your conviction.
    Remember that we _talk_ about strategy like it's done in one pass,
    but almost all real strategy takes many refinement passes.

The steps of writing policy are relatively pedestrian, largely because
you've done so much of the work already in the exploration, diagnosis, and refinement steps.
If you skip those phases, you'd likely follow the above steps for writing policy,
but the expected quality of the policy itself would be far lower.

## How many policies?

Addressing the entirety of the diagnosis is often complex,
which is why most strategies feature a set of policies rather than just one.
The [strategy for decomposing a monolithic application](https://draftingstrategy.com/monolith-decomposition-strategy/)
is not one policy deciding not to decompose, but a series of four policies:

1. Business units should always operate in their own code repository and monolith.
2. New integrations across business unit monoliths should be done using gRPC.
3. Except for new business unit monoliths, we don’t allow new services.
4. Merge existing services into business-unit monoliths where you can.

Four isn't universally the right number either.
It's simply the number that was required to solve that strategy's diagnosis.
With an excellent diagnosis, your policies will often feel inevitable, and perhaps even boring.
That's great: what makes a policy good is that it's effective, not that it's novel or inspiring.

## Kinds of policies

While there are _so many_ policies you can write, I've found they generally fall into one of four major
categories: approvals, allocations, direction, and guidance. This section introduces those categories.

**Approvals** define the process for making a recurring decision.
This might require invoking an architecture advice process,
or it might require involving an authority figure like an executive.

In the [Index post-acquisition integration strategy](https://draftingstrategy.com/index-acquisition-strategy/),
there were a number of complex decisions to be made, and the approval mechanism was:

> Escalations come to paired leads: given our limited shared context across teams, all escalations must come to both Stripe’s Head of Traffic Engineering and Index’s Head of Engineering.

This allowed the acquired and acquiring teams to start building trust between each other
by ensuring both were consulted before any decision was finalized.
On the other hand, the [user data access strategy](https://draftingstrategy.com/user-data-strategy/)'s approval
strategy was more focused on managing corporate risk:

> **Exceptions must be granted in writing by CISO.** While our overarching Engineering Strategy states
> that we follow an advisory architecture process as described in _Facilitating Software Architecture_,
> the customer data access policy is an exception and must be explicitly approved, with documentation, by the CISO. Start that process in the #ciso channel.

These two different approval processes had different goals,
so they made tradeoffs differently. There are so many ways to tweak approval,
allowing for many different tradeoffs between safety, productivity, and trust.

**Allocations** describe how resources are split across multiple potential investments.
Allocations are the most concrete statement of organizational priority, and also articulate
the organization's belief about how productivity happens in teams.
Some companies believe you go fast by swarming more people onto critical problems.
Other companies believe you go fast by forcing teams to solve problems without additional headcount.
Both can work, and teach you something important about the company's beliefs.

The strategy on [Uber's service migration](https://draftingstrategy.com/uber-strategy/) has two concrete examples
of allocation policies. The first describes the Infrastructure engineering team's
allocation between manual provision tasks and investing into creating a self-service provisioning platform:

> **Constrain manual provisioning allocation to maximize investment in self-service provisioning.** The service provisioning team will maintain a fixed allocation of one full time engineer on manual service provisioning tasks. We will move the remaining engineers to work on automation to speed up future service provisioning. This will degrade manual provisioning in the short term, but the alternative is permanently degrading provisioning by the influx of new service requests from newly hired product engineers.

The second allocation policy is implicitly noted in this strategy's diagnosis,
where it describes the allocation policy in the Engineering organization's higher altitude strategy:

> Within infrastructure engineering, there is a team of four engineers responsible for service provisioning today. While our organization is growing at a similar rate as product engineering, none of that additional headcount is being allocated directly to the team working on service provisioning. We do not anticipate this changing.

Allocation policies often create a surprising amount of clarity for the team,
and I include them in almost every policy I write either explicitly,
or implicitly in a higher altitude strategy.

**Direction** provides explicit instruction on how a decision *must* be made.
This is the right tool when you know where you want to go, and exactly the way
that you want to get there. Direction is appropriate for problems you understand
clearly, and you value consistency more than empowering individual judgment.

Direction works well when you need an unambiguous policy that doesn't leave room for interpretation.
For example, [Calm's policy for working in the monolith](https://draftingstrategy.com/product-eng-strategy/):

> We write all code in the monolith. It has been ambiguous if new code (especially new application code) should be written in our JavaScript monolith, or if all new code must be written in a new service outside of the monolith. This is no longer ambiguous: all new code must be written in the monolith.
>
> In the rare case that there is a functional requirement that makes writing in the monolith implausible, then you should seek an exception as described below.

In that case, the team couldn't agree on what should go into the monolith.
Individuals would often make incompatible decisions, so creating consistency required removing personal judgment from the equation.

Sometimes judgment is the issue, and sometimes consistency is difficult due to misaligned incentives.
A good example of this comes in [strategy on working with new Private Equity ownership](https://draftingstrategy.com/private-equity-strategy/):

> We will move to an “N-1” backfill policy, where departures are backfilled with a less senior level.
> We will also institute a strict maximum of one Principal Engineer per business unit.

It's likely that hiring managers would simply ignore this backfill policy if it was stated more
softly, although sometimes less forceful policies are useful.

**Guidance** provides a recommendation about how a decision _should_ be made.
Guidance is useful when there's enough nuance, [ambiguity](https://lethain.com/navigating-ambiguity/), or complexity
that you _can_ explain the desired destination, but you _can't_ mandate the path to reaching it.

One example of guidance comes from the [Index acquisition integration strategy](https://draftingstrategy.com/index-acquisition-strategy/):

> **Minimize changes to tokenization environment**: because point-of-sale devices directly work with customer payment details, the API that directly supports the point-of-sale device must live within our secured environment where payment details are stored.
>
> However, any other functionality must not be added to our tokenization environment.

This might read like direction, but it's clarifying the desired outcome of avoiding unnecessary complexity
in the tokenization environment. However, it's not able to articulate what complexity is necessary,
so ultimately it's guidance because it requires significant judgment to interpret.

A second example of guidance comes in the [strategy on decomposing a monolithic codebase](https://draftingstrategy.com/monolith-decomposition-strategy/):

> **Merge existing services into business-unit monoliths where you can.** We believe that each choice to move existing services back into a monolith should be made “in the details” rather than from a top-down strategy perspective. Consequently, we generally encourage teams to wind down their existing services outside of their business unit’s monolith, but defer to teams to make the right decision for their local context.

This is another case of knowing the desired outcome, but encountering too much uncertainty
to direct the team on how to get there. If you ask five engineers about whether it's possible
to merge a given service back into a monolithic codebase, they'll probably disagree.
That's fine, and highlights the value of guidance: it makes it possible to make incremental progress in areas
where more concrete direction would cause confusion.

When you're working on a strategy's policy section, it's important to consider all of these categories.
Which feel most natural to use will vary depending on your team and role, but they're all usable:

* If you're a developer productivity team, you might have to lean heavily on guidance in your policies
    and increased support for that guidance within the details of your platform.
* If you're an executive, you might lean heavily on direction. Indeed, you might lean _too_ heavily on direction,
    where guidance often works better for areas where you understand the direction but not the path.    
* If you're a product engineering organization, you might have to narrow the scope of your direction
    to the engineers within that organization to deal with the realities of complex cross-organization dynamics.

Finally, if you have a clear approach you want to take that doesn't fit cleanly into any of these
categories, then don't let this framework dissuade you. Give it a try, and adapt if it doesn't initially work out.

## Maintaining strategy altitude

The chapter on [when to write engineering strategy](https://draftingstrategy.com/when-write-stratefy/)
introduced the concept of strategy altitude, which is being deliberate about where
certain kinds of policies are created within your organization.

Without repeating that section in its entirety, it's particularly relevant when
you set policy to consider how your new policies eliminate flexibility within your
organization. Consider these two somewhat opposing strategies:

* [Stripe's Sorbet strategy](https://draftingstrategy.com/stripe-sorbet-strategy/) only worked in an organization
    that enforced the use of a single programming language across
    (essentially) all teams
* [Calm's strategy for resourcing Engineering-driven projects](https://draftingstrategy.com/project-resourcing-strategy/)
    knew that resourcing had to be managed by the team directly.
    Attempting to solve the problem at another level would simply result
    in someone talking to the team directly to rewrite their priorities
    to incorporate a new urgent project.

Stripe's organization-altitude policy took away the freedom of individual teams
to select their preferred technology stack. In return, they unlocked the ability
to centralize investment in a powerful way.
Calm went the opposite way, recognizing that only teams were empowered to
manage the contents of their roadmap; executives were more senior, but frequently
overridden by other executives' out-of-band instructions.

Both altitudes make sense. Both have consequences.

## Criteria for effective policies

In _[The Engineering Executive's Primer](https://www.amazon.com/Engineering-Executives-Primer-Impactful-Leadership/dp/1098149483/)_'s
chapter on [engineering strategy](https://lethain.com/eng-strategies/), I introduced three criteria for evaluating policies.
They ought to be applicable, enforced, and create leverage. Defining those a bit:

1. **Applicable**: it can be used to navigate complex, real scenarios, particularly when making tradeoffs.
2. **Enforced**: teams will be held accountable for following the guiding policy.
3. **Create Leverage**: create compounding or multiplicative impact.

The last of these three, create leverage, made sense in the context of a book about
engineering executives, but probably doesn't make as much sense here.
Some policies certainly should create leverage
(e.g. [the policy to avoid deprecating APIs](https://draftingstrategy.com/api-deprecation-strategy/) makes other customer retention mechanisms more effective)
but others might not
(e.g. [moving to an N-1 backfill policy](https://draftingstrategy.com/private-equity-strategy/)).
Outside the executive context, what's important isn't necessarily creating leverage,
but that a policy solves for part of the diagnosis.

That leaves the other two--being applicable and enforced--both of which are necessary
for a policy to actually address the diagnosis.
Any policy which you can't determine how to apply, or aren't willing to enforce,
simply won't be useful.

Let's apply these criteria to a handful of potential policies.
First let's think about policies we might write to improve the
talent density of our engineering team:

* **"We only hire world-class engineers."**
    This isn't applicable, because it's unclear what a world-class engineer means.
    Because there's no mutually agreeable definition in this policy, it's also not consistently enforceable.
* **"We only hire engineers that get at least one 'strong yes' in scorecards."**
    This is applicable, because there's a clear definition.
    This is enforceable, depending on the willingness of the organization to reject seemingly good candidates
    who don't happen to get a strong yes.

Next, let's think about a policy regarding code reuse within a codebase:

* **"We follow a strict Don't Repeat Yourself policy in our codebase."**
    There's room for debate within a team about whether two pieces of code are truly
    duplicative, but this is generally applicable.
    Because there's room for debate, it's a very context specific determination to decide how to enforce a decision.
* **"Code authors are responsible for determining if their contributions violate Don't Repeat Yourself, and rewriting them if they do."**
    This is much more applicable, because now there's only a single person's judgment to assess the potential repetition.
    In some ways, this policy is also more enforceable, because there's no longer any ambiguity around who is deciding whether
    a piece of code is a repetition.

    The challenge is that
    enforceability now depends on one individual, and making this policy effective will require
    holding individuals accountable for the quality of their judgement.
    An organization that's unwilling to distinguish between good and bad judgment
    won't get any value out of the policy.
    This is a good example of how a good policy in one organization might become a poor policy in another.

If you ever find yourself wanting to include a policy that for some reason
either can't be applied or can't be enforced, stop to ask yourself what you're
trying to accomplish and ponder if there's a different policy that might be better suited to that goal.

## Developing novel policies

My experience is that there are vanishingly few truly novel policies
to write. There's almost always someone else has already done something similar to your intended approach.
[Calm's engineering strategy](https://draftingstrategy.com/product-eng-strategy/) is such a case:
the details are particular to the company, but the general approach is common across the industry.

The most likely place to find truly novel policies is during the adoption phase of a new widespread technology,
such as the rise of ubiquitous mobile phones, cloud computing, or large language models.
Even then, as explored in [the strategy for adopting large-language models](https://draftingstrategy.com/llm-adoption-strategy/),
the new technology can be engaged with as a generic technology:

> **Develop an LLM-backed process for reactivating departed and suspended drivers in mature markets.** Through modeling our driver lifecycle, we determined that improving onboarding time will have little impact on the total number of active drivers. Instead, we are focusing on mechanisms to reactivate departed and suspended drivers, which is the only opportunity to meaningfully impact active drivers.

You could simply replace "LLM" with "data-driven" and it would be equally readable.
In this way, policy can generally sidestep areas of uncertainty by being a bit abstract.
This avoids being overly specific about topics you simply don't know much about.

However, even if your policy isn't novel to the industry,
it might still be novel to you or your organization.
The steps that I've found useful to debug novel policies are the same steps as running a condensed version
of the strategy process, with a focus on exploration and refinement:

1. Collect a number of _similar_ policies, with a focus on how
    those policies differ from the policy you are creating
2. Create a [systems model](https://draftingstrategy.com/systems-modeling/) to
    articulate how this policy will work,
    and also how it will differ from the similar policies you're considering
3. Run a [strategy testing](https://draftingstrategy.com/strategy-testing/) cycle
    for your proto-policy to discover any unknown-unknowns about how it
    works in practice

Whether you run into this scenario is largely a function of the extent
of your, and your organization's, experience. Early in my career, I found
myself doing novel (for me) strategy work very frequently, and these days
I rarely find myself doing novel work, instead focusing on adaptation
of well-known policies to new circumstances.

## Are competing policy proposals an anti-pattern?

When creating policy, you'll often have to engage with the question of
whether you should develop one preferred policy or a series of potential strategies to pick from.
Developing these is a useful stage of setting policy, but rather than
helping you refine your policy, I'd encourage you to think of this as
exposing gaps in your diagnosis.

For example, [when Stripe developed the Sorbet ruby-typing tooling](https://draftingstrategy.com/stripe-sorbet-strategy/),
there was debate between two policies:

1. Should we build a ruby-typing tool to allow a centralized team to gradually
    migrate the company to a typed codebase?
2. Should we migrate the codebase to a preexisting strongly typed language like Golang
    or Java?

These were, initially, equally valid hypotheses. It was only by clarifying our diagnosis
around resourcing that it became clear that incurring the bulk of costs
in a centralized team was clearly preferable to spreading the costs across many teams.
Specifically, recognizing that we wanted to prioritize short-term product engineering velocity,
even if it led to a longer migration overall.

If you do develop multiple policy options, I encourage you to move the alternatives
into an appendix rather than [including them in the core of your strategy document](https://draftingstrategy.com/readable-strategy/).
This will make it easier for readers of your final version to understand how to follow your policies,
and they are the most important long-term user of your written strategy.

## Recognizing constraints

A similar problem to competing solutions is developing a policy that you cannot possibly fund.
It's easy to get enamored with policies that you can't meaningfully enforce,
but that's bad policy, even if it would work in an alternate universe where it
was possible to enforce or resource it.

To consider a few examples:

* The [strategy for controlling access to user data](https://draftingstrategy.com/user-data-strategy/) might have proposed
    requiring manual approval by a second party of every access
    to customer data. However, that would have gone nowhere.
* Our [approach to Uber's service migration](https://draftingstrategy.com/uber-strategy/)
    might have required more staffing for the infrastructure engineering team,
    but we knew that wasn't going to happen, so it was a meaningless policy proposal to make.
* The strategy for [navigating private equity ownership](https://draftingstrategy.com/private-equity-strategy/) might
    have argued that new ownership should not hold engineering accountable to a new standard
    on spending. But they would have just invalidated that strategy in the next financial planning period.

If you find a policy that contemplates an impractical approach,
it doesn't _only_ indicate that the policy is a poor one,
it also suggests your policy is missing an important pillar.
Rather than debating the policy options, the fastest path to
resolution is to align on the diagnosis that would invalidate
potential paths forward.

In cases where aligning on the diagnosis isn't possible,
for example because you simply don't understand the possibilities
of a new technology as encountered in the [strategy for adopting LLMs](https://draftingstrategy.com/llm-adoption-strategy/),
then you've typically found a valuable opportunity to use [strategy refinement](https://draftingstrategy.com/refine/)
to build alignment.

## Dealing with missing strategies

At a recent company offsite, we were debating which policies we might adopt to deal
with annual plans that kept getting derailed after less than a month.
Someone remarked that this would be much easier if we could get the executive team to
commit to a clearer, written strategy about which business units we were prioritizing.

They were, of course, right. It would be much easier. Unfortunately,
it goes back to the problem we discussed in the [diagnosis chapter](https://draftingstrategy.com/diagnosis/)
about reframing blockers into diagnosis. If a strategy from the company or a peer function is missing,
the empowering thing to do is to include the absence in your diagnosis and move forward.

Sometimes, even when you do this, it's easy to fall back into the belief that you cannot set a policy
because a peer function might set a conflicting policy in the future.
Whether you're an executive or an engineer, you'll never have the details you want to make
the ideal policy. Meaningful leadership requires taking meaningful risks,
which is never something that gets comfortable.

## Summary

After working through this chapter,
you know how to develop policy, how to assemble policies to solve your diagnosis,
and how to avoid a number of the frequent challenges that policy writers encounter.
At this point, there's only one phase of strategy left to dig into,
[operating the policies you've created](https://draftingstrategy.com/operations/).