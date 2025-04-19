# Introduction
url: https://draftingstrategy.com/intro

I've worked alongside many talented people who spent years waiting for a chance to finally "do strategy."
My hope is this book convinces you—and maybe them—that waiting is optional.
Strategy isn’t reserved for executives.
It's the art of making thoughtful decisions, and is accessible to everyone--including you.

Even if you'd prefer to avoid strategy, it's still happening all around you.
My first big dose of strategy came managing the team responsible for
[Uber's service migration](https://draftingstrategy.com/uber-strategy/),
where we desperately tried to survive accelerating inbound requests for support.
Since then, I've seen strategy everywhere I worked, from
[Stripe's acquisition of Index](https://draftingstrategy.com/index-acquisition-strategy/) to
[Calm's focusing on being a product engineering company](https://draftingstrategy.com/product-eng-strategy/).
There are even some strategy problems that I've encountered again and again at every company I've joined,
such as [deciding how to decompose monolithic codebases](https://draftingstrategy.com/monolith-decomposition-strategy/).

This book is focused on engineering strategy.
In other words, making thoughtful decisions about engineering.
"Engineering" is defined both as the discipline of writing software,
and also concerns of the Engineering organization within your company.
If this seems like a hopelessly broad topic, then we agree on the scope of my definition.
However, I would never agree it's hopeless.

My decision making has significantly improved over the course of my career.
I believe very strongly that my improvement had very little to do
with _me_, and a lot to do with learning to engage in structured thinking.
I also believe the lessons that I learned slowly are eminently teachable
in the next couple hundred pages.

## Grounded in my direct experience

Strategy is a broad topic, and many strategy books become awkwardly abstract.
To avoid falling into that trap, I've anchored this book in my personal experiences doing
strategy and the strategy work of colleagues that I had the opportunity to witness directly.

As much as possible, I've used examples that I worked on in real companies,
and I've mentioned those companies by name. That's true for more than half the strategies included in this book,
which describe strategies I collaborated on during my time at Stripe, Uber, and Calm.
For the other half of the strategies, I have abstracted away from specific companies because they are sensitive topics
such as [how to work with private equity ownership](https://draftingstrategy.com/private-equity-strategy/),
or expose internal information better kept private as in
[how to manage access to customer data](https://draftingstrategy.com/user-data-strategy/).
In both sorts of examples, I've worked hard to remain honest, even when I've had to omit some details,
out of respect for the companies and individuals involved.

You'll also notice that I've tried to be positive about all of these strategies.
If it seems that I've been too positive, it's because all strategies age.
Even the best strategies eventually turn sour.
It's most interesting to understand strategies in the context they were originally conceived.
Of course, evaluation matters too, which we'll cover in the chapter on [evaluating strategy quality](https://draftingstrategy.com/evaluating-strategy/).

## Adapting Rumelt for engineering

In addition to my own experience, the second largest influence on this book is
Richard Rumelt’s _[Good Strategy, Bad Strategy](https://www.amazon.com/dp/B004J4WKEC)_.
It's a quick read, and was a life-changing discovery for me.
Rumelt describes three pillars of effective strategy:

1. *Diagnosis* \- a theory describing the nature of the challenge. This involves identifying the root cause(s) at play, for example “high work-in-progress is preventing us from finishing any tasks, so we are increasingly behind each sprint” might be a good diagnosis
2. *Guiding policy* \- a series of general policies which will be applied to grapple with the challenge. Guiding policies are typically going to be implicit or explicit tradeoffs. For example, a guiding policy might be “only hire for most urgent team, do not spread hires across all teams.” If a guiding policy doesn’t imply a tradeoff, you should be suspicious of it. “Working harder to get it done” isn’t really a guiding policy, the relevant guiding policy there might be “work folks hard and expect high attrition”
3. *Coherent actions* \- a set of specific actions directed by guiding policy to address the challenge. This is the most important part, and I think the most exciting part, because it clarifies that a strategy is only meaningful if it leads to aligned action

The first time I read this definition was eye-opening: it answered so many strategy questions I'd had for such a long time.
However, although I was grateful to Rumelt for giving me my first framework for thinking about strategy,
I continued noticing how little deliberate strategy existed in the engineering organizations I'd joined.

Eventually, I recognized that if Rumelt's work was trivial to apply to engineering,
we'd see a lot more disciplined engineering strategy in practice.
We'd also, one hopes, see fewer obviously flawed engineering strategies.
This book is the culmination of my past decade spent understanding how to
adapt Rumelt's approach to something that not only _could_ work,
but concretely _has_ worked in the organizations that I've joined.

## Iterative, intellectual *and* mechanical

In addition to anchoring in my personal experience and building on Richard Rumelt's approach,
there are three characteristics that underpin this book's approach:
being iterative, and embracing both the intellectual and the mechanical aspects of strategy.

Even my proudest strategy work has eventually become obsolete.
For some time, I was embarrassed by this realization.
Eventually, I came to recognize that entropy is natural in strategy work;
good strategy embraces change rather than fights it.
This solidified into the concept of [strategy refinement](https://draftingstrategy.com/refine/),
where ideas are deliberately validated and improved rather than treated as immutable.

If you've ever participated in an executive hiring loop, you've probably interviewed
someone who described strategic thinking as a personal strength.
Those candidates often draw a distinction between directing how work should be done,
and being in the weeds of doing the work itself.
It happens enough that you start to appreciate that
many people view strategy as a fundamentally intellectual endeavor about how things ought to work,
rather than a mechanical endeavor that studies how things actually do work in practice.

While strategy does indeed have intellectual elements,
effective strategy is at least equally dependent on the mechanical nuances of reality as it is on intellectual frameworks.
Even the best [policies](https://draftingstrategy.com/policy/) will fail without attention to whether the team is actually adopting the policy's guidance.
Similarly, very effective [operational mechanisms](https://draftingstrategy.com/operations/) to roll out a strategy
won't help your company if the policy being rolled out is a bad one.

As obvious as these ideas seem, many organizations expect strategies to manifest
perfectly into existence from the very beginning.
This book discusses how to bridge the gap between that pressing expectation of perfection
and the reality that effective strategy
development is grounded in iterative work that is both intellectual and mechanical.

## This book's ambition

As I've worked on this book, one of my lingering concerns
is that the ideas in it are perhaps simply too obvious to write down.
Each time I've been tempted to set the project aside, I see a new example,
or am reminded of an old experience, where some of the smartest people I've
ever known have struggled unsuccessfully with a strategy problem that some people
would describe as quite simple.

The belief that strategy is complex often gets people in trouble.
It's appealing to believe that strategies fail due to detailed
errors in decision-making, or the unanticipated move of an adversary.
Maybe that is common when it comes to grand strategy.
However, my experience is that engineering strategies fail for very mundane reasons.
The most common of these mundane reasons is that executives assume their
strategy will roll itself out. The second is forgetting to spend time
validating the details. Both are avoidable with a bit of structure.

This book's framework is not an attempt to discredit all other approaches. Rather, it's a synthesis
of the various approaches I've encountered, along with a few dimensions that
I've not seen addressed in much detail elsewhere.
Even if you don't agree with my framework, I hope it helps you refine your own framework.
Either way, our industry will be much better for it.