# Is this strategy any good?
url: https://draftingstrategy.com/evaluating-strategy

We've read a lot of strategy at this point in the book.
We can judge a strategy's format, and its construction: both are useful things.
However, format is a predictor of quality, not quality itself.
The remaining question is, how should we assess whether a strategy is any good?

[Uber's service migration strategy](https://draftingstrategy.com/uber-strategy/) unlocked
the entire organization to make rapid progress.
It also led to a sprawling architecture problem down the line.
Was it a great strategy or a terrible one? Folks can reasonably disagree,
but it's worthwhile developing our point of view on why we should prefer one
interpretation or the other.

This chapter will focus on:

* The various ways that are frequently suggested for evaluating strategies,
    such as input-only evaluation, output-only evaluation, and so on
* A rubric for evaluating strategies, and why a useful
    rubric has to recognize that strategies have to be evaluated
    in phases rather than as a unified construct
* Why ending a strategy is often a sign of a good strategist,
    and sometimes the natural reaction to a new phase in a strategy,
    rather than a judgment on prior phases
* How missing context is an unpierceable veil for evaluating other companies'
   strategies with high-conviction, and why you'll end up attempting to
   evaluate them anyway
* Why you can learn just as much from bad strategies as from good ones,
   even in circumstances where you are missing much of the underlying context

Time to refine our judgment about strategy quality a bit.

## How are strategies graded?

Before suggesting my own rubric, I want to explore how the industry appears to grade strategies in practice.
That's not because I particularly agree with them--I generally find each approach misses an important nuance--understanding
their flaws is a foundation to build on.

Grading strategy on its outputs is by far the most prevalent approach I've found in industry.
This is an appealing approach, because it does make sense that a strategy's results are more important
than anything else. However, this line of thinking can go awry.
We saw massive companies like Google move to service
architectures, and we copied them because if it worked for Google, it would likely work for us.
As discussed in the [monolith decomposition strategy](https://draftingstrategy.com/monolith-decomposition-strategy/),
it did not work particularly well for most adopters.

The challenge with grading outputs is that it doesn't distinguish between
"alpha", how much better your results are because of your strategy, and "beta",
the expected outcome if you hadn't used the strategy.
For example, the [acquisition of Index](https://draftingstrategy.com/index-acquisition-strategy/)
allowed Stripe to build a point-of-sale business line, but they were also on track to internally
build that business. Looking _only_ at outputs can't distinguish whether it would have been better
to build the business via acquisition or internally.
But one of those paths must have been the better strategy.

Similarly, there are also strategies that succeed, but do so at unreasonably high costs.
[Stripe's API deprecation strategy](https://draftingstrategy.com/api-deprecation-strategy/) is a good example of a
strategy that was _extremely_ well worth the cost for the company's first decade,
but eventually became too expensive to maintain as the evolving regulatory environment created more overhead.
Fortunately, Stripe modified their strategy to allow some deprecations, but you can imagine an
alternate scenario where they attempted to maintain their original strategy, which would have
likely failed due to its accumulating costs.

Confronting these problems with judging on outputs, it's compelling to switch to the opposite lens and evaluate
strategy purely on its inputs. In that approach, as long as the sum of the strategy's parts make sense,
it's a good strategy, even if it didn't accomplish its goals.
This approach is very appealing, because it appears to focus _purely_ on the strategy's alpha.

Unfortunately I find this view similarly deficient.
For example, the [strategy for adopting LLMs](https://draftingstrategy.com/llm-adoption-strategy/) offers a cautious approach to adopting LLMs.
If that company is outcompeted by competitors in the incorporation of LLMs, to the loss of significant revenue,
I would argue that strategy isn't a great one, even if it's rooted in a proper diagnosis and effective policies.
Doing good strategy requires reconciling the theoretical with the practical,
so we can't argue that inputs alone are enough to evaluate strategy work.
If a strategy is conceptually sound, but struggling to make an impact,
then its authors should continue to [refine it](https://draftingstrategy.com/refine/).
If its authors take a single pass and ignore subsequent information that it's not working,
then it's a failed strategy, regardless of how thoughtful the first pass was.

While I find these mechanisms to be incomplete, they're still instructive.
By incorporating bits of each of these observations, we're surprisingly
close to a rubric that avoids each of these particular downfalls.

## Rubric for strategy

Balancing the strengths and flaws of the previous section's ideas,
the rubric I've found effective for evaluating strategy is:

1. **How quickly is the strategy refined?**
    If a strategy starts out bad, but improves quickly, that's a better strategy
    than a mostly right strategy that never evolves.
    Strategy thrives when its practitioners understand it is a living endeavor.
2. **How expensive is the strategy's refinement for implementing and impacted teams?**
    Just as culture eats strategy for breakfast,
    good policy loses to poor operational mechanisms every time.
    Especially early on, good strategy is validated cheaply.
    Expensive strategies are discarded before they can be validated,
    let alone improved.
3. **How well does the current iteration solve its diagnosis?**
    Ultimately, strategy does have to address the diagnosis it starts from.
    Even if you're learning quickly and at a low cost, at some point you
    do have to actually get to impact.
    Strategy must eventually be graded on its impact.
    

With this rubric in hand, we can finally assess the
[Uber's service migration strategy](https://draftingstrategy.com/uber-strategy/).
It refined rapidly as we improved our tooling, minimized costs because
we had to rely on voluntary adoption, and solved its diagnosis extremely well.
So this was a great strategy, but how do we think about the fact that its diagnosis
missed out on the consequences of a wide-spread service architecture on developer productivity?

This brings me to the final component of the strategy quality rubric:
the recognition that strategy exists across multiple phases.
Each phase is defined by new information--whether or not this information is known
by the strategy's authors--that render the diagnosis incomplete.

The Uber strategy can be thought of as existing across two phases:

* Phase 1 used service provisioning to address developer productivity challenges
    in the monolith.
* Phase 2 was engaging with consequences of a sprawling service architecture.

All the good grades I gave the strategy are appropriate to the first phase.
However, the second phase was ushered in by the negative impacts to developer
productivity exposed by the initial rollout.
The second phase's grades on the rate of iteration, the cost, and the outcomes
were reasonable, but a bit lower than first phase.
In the subsequent years, the second phase was succeeded
by a third phase that aimed to address the second's challenges.

## Does stopping mean a strategy's bad?

Now that we have a rubric, we can use it to evaluate one of the
important questions of strategy: does giving up on a strategy mean
that the strategy is a bad one?

The vocabulary of strategy phases helps us here, and I think
it's uncontroversial to say that a new phase's evolution
of your prior diagnosis might make it appropriate to abandon a strategy.
For example, Digg owned our own servers in 2010, but
would certainly _not_ buy their own servers if they started
ten years later. Circumstances change.

Sometimes I also think that aborting a strategy in its
first phase is a good sign. That's generally true when
the rate of learning is outpaced by the cost of learning.
I recently sponsored a developer productivity strategy that
had some impact, but less than we'd intended.
We immortalized a few of the smaller pieces, and returned
further exploration to a [lower altitude strategy](https://draftingstrategy.com/when-write-stratefy/)
owned by the teams rather than the high altitude strategy that I owned as an executive.

Essentially all strategies are competing with strategies at other altitudes,
so I think giving up on strategies, especially high altitude strategies,
is almost always a good idea.

## The unpierceable veil

Working within our industry, we are often called upon
to evaluate strategies from afar. As other companies rolled out
LLMs in their products or microservices for their architectures,
our companies pushed us on why we weren't making these changes as well.
The [exploration step](https://draftingstrategy.com/explore/) of strategy helps determine
where a strategy might be useful for you, but even that doesn't really help
you evaluate whether the strategy or the strategists were effective.

There are simply too many dimensions of the rubric that you cannot evaluate
when you're far away. For example, how many phases occurred before the idea that
became the external representation of the strategy came into existence?
How much did those early stages cost to implement?
Is the _real_ mastery in the operational mechanisms that are never reported on?
Did the external representation of the strategy ever happen at all,
or is it the logical next phase that solves the reality of the internal
implementation?

With all that in mind, I find that it's generally impossible to accurately evaluate
strategies happening in other companies with much conviction.
Even if you want to, the missing context is an impenetrable veil.
That's not to say that you shouldn't try to evaluate their strategies,
that's something that you'll be forced to do in your own strategy work.
Instead, it's a reminder to keep a low confidence score in those appraisals:
you're guaranteed to be missing something.

## Learning despite quality issues

Although I believe it's quite valuable for us to judge the quality
of strategies, I want to caution against going a step further and
making the conclusion that you can't learn from poor strategies.
As long as you are aware of a strategy's quality, I believe you
can learn just as much from failed strategies as from great strategy.

Part of this is because often even failed strategies have early phases
that work extremely well. Another part is because strategies tend to
fail for interesting reasons. I learned just as much from Stripe's
failed rollout of agile, which struggled due to missing operational mechanisms, as I did from Calm's successful transition to focus primarily on product engineering.
Without a clear point of view on which of these worked,
you'd be at risk of learning the wrong lessons, but with forewarning you don't
run that risk.

Once you've determined a strategy was unsuccessful, I find it particularly valuable
to determine the strategy's phases and understand which phase and where in the [strategy steps](https://draftingstrategy.com/strategy-steps/)
things went wrong. Was it a lack of operational mechanisms? Was the policy itself a poor match for
the diagnosis? Was the diagnosis willfully ignorant of a truculent executive?
Answering these questions will teach you more about strategy than only studying successful strategies,
because you'll develop an intuition for which parts truly matter.

## Summary

Finishing this chapter, you now have a structured rubric
for evaluating a strategy, moving beyond "good strategy" and "bad strategy" to
a nuanced assessment.
This assessment is not just useful for grading strategy, but makes it possible to
specifically improve your strategy work.

Maybe your approach is sound, but your operational mechanisms are too costly for
the rate of learning they facilitate.
Maybe you've treated strategy as a single iteration exercise, rather than
recognizing that even excellent strategy goes stale over time.
Keep those ideas in mind as we head into the final chapter
on [how you personally can get better at strategy work](https://draftingstrategy.com/getting-better/).