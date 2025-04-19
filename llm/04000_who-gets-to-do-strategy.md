# Who gets to do strategy?
url: https://draftingstrategy.com/who-does-strategy

If you talk to enough aspiring leaders, you'll become familiar with
the prevalent idea that they need to be promoted before they can
work on strategy.
It's widely accepted as true, but I've found this idea fundamentally incorrect:
you can work on strategy from anywhere in an organization.
It just requires different tactics to do so.

Both _Staff Engineer_ and _The Engineering Executive's Primer_ have chapters
on strategy. While the chapters' contents are quite different, both present
a practical path to advancing your organization's thinking about complex topics.
This chapter explains my belief that
_anyone_ within an organization can make meaningful progress on strategy,
particularly if you are honest about the tools accessible to you
and thoughtful about how to use them.

The themes we'll dig into are:

* How to do strategy as an engineer, particularly an engineer who hasn't
    been given explicit authority to do strategy
* Doing strategy as an engineering executive who is responsible for your
    organization's decision-making
* How you can develop engineering strategy even in difficult situations,
    such as when there's no existing strategy,
    when acknowledging certain problems is politically sensitive,
    or when misaligned incentives make consensus challenging
* If this book's argument is that everyone should do strategy,
    is there anyone who, nonetheless, really should not do strategy?

By the end, you'll hopefully agree that engineering strategy is accessible to
everyone, even though you're always operating within constraints.

## Doing strategy as an engineer

It's easy to get so distracted by an executive's top-down approach to
strategy that you convince yourself that there aren't other approachable
mechanisms to doing strategy. There are!

_Staff Engineer_ introduces an approach I call [Take five, then synthesize](https://staffeng.com/guides/engineering-strategy/),
which does strategy by:

1. Documenting how five current and historical related decisions have been made in your organization.
    This is an extended exploration phase
2. Synthesizing those five documents into a diagnosis and policy.
    You are naming the implicit strategy,
    so it's impossible for someone to reasonably argue you're not empowered
    to do strategy: you're just describing what's already happening

At that point, either the organization feels comfortable with what you've written--which is their current strategy--or
it doesn't in which case you've forced a conversation about how to revise the approach.
Creating awareness is often enough to drive strategic change,
and doing so doesn't require any explicit authorization from an executive to do.

When awareness is insufficient, the other pattern I've found highly effective
in low-authority scenarios is an approach I wrote about in
_An Elegant Puzzle_, and call  [model, document, and share](https://lethain.com/model-document-share/):

1. Model the approach you want others to adopt.
    Make it easy for them to observe how you've changed the way you're doing things.
2. Document the approach, the thinking behind it, and how to adopt it.
3. Share the document around. If people see you succeeding with the approach,
    then they're likely to copy it from you.

You might be skeptical because this is an influence-based approach.
However, as we'll discuss in the next section, even an executive-driven
strategy is highly dependent on influence.

<div class="bg-light-gray br4 ph3 pv1">

**Strategy archaeology**

Vernor Vinge's _[A Deepness in the Sky](https://en.wikipedia.org/wiki/A_Deepness_in_the_Sky)_,
published in 1999, introduced the term software archaeologists,
folks who created functionality by cobbling together millennia
of scraps of existing software.

Although it's a somewhat different usage, I sometimes think of the "take five, then synthesize" approach as
performing strategy archaeology. Simply by recording what has happened in the past,
we make it easier to understand the present, and influence the future.

</div>

## Doing strategy as an executive

The biggest misconception about executive roles, frequently held by
non-executives and new executives who are about to make a series of regrettable
mistakes, is that executives operate without constraints.
That is false: executives have an extremely high number of constraints that
they operate under.
Executives have budgets, CEO visions, peers to satisfy, and a team to motivate.
They can disappoint any of these temporarily, but in long-term they have to satisfy
all of them.

Nonetheless, it is true that executives have more latitude to mandate
and cajole participation in the strategies that they sponsor.
_The Engineering Executive's Primer_'s [chapter on strategy](https://lethain.com/eng-strategies/)
is a brief summary of this entire book, but it doesn't say much about
how executive strategy differs from non-executive strategy.

How the executive's approach to strategy differs from the engineer's
can be boiled down to:

1. Executives can mandate adherence to their strategy, which empowers their policy options.
    An engineer can't prevent the promotion of someone who refused to follow their policy, but an executive can.

    Mandates only matter if there are consequences. If an executive is unwilling to
    enforce consequences for non-compliance with a mandate, the ability to issue a
    mandate isn't meaningful.

    This is also true if they _can't_ enforce a mandate because of lack of support from
    their peer executives.
2. Even if an executive is unwilling to use mandates, they have significant visibility
    and access to their organization to advocate for their preferred strategy.
3. Neither access nor mandates improve an executive's ability to diagnose problems.
    However, both often create the appearance of progress.
    This is why executive strategies can fail so spectacularly and endure so long despite failure.

As a result, my experience is that executives have an easier time doing strategy,
but a much harder time learning how to do strategy well,
and fewer protections to avoid serious mistakes.
Further, the consequences of an executive's poor strategy tend to be
much further reaching than an engineer's.
Waiting to do strategy until you are an executive is a recipe for disaster,
even if it looks easier from a distance.

## Doing strategy in other roles

Even if you're neither an engineer nor an engineering executive,
you can still do engineering strategy.
It'll just require an even more influence-driven approach.

The engineering organization is generally right to believe that they know
the most about engineering, but that's not always true.
Sometimes a product manager used to be an engineer and has
significant relevant experience.
Other times, such as the [early adoption of large language models](https://draftingstrategy.com/llm-adoption-strategy/),
engineers don't know much either, and benefit from outside perspectives.

## Doing strategy in challenging environments

Good strategies succeed by accurately diagnosing circumstances and picking policies that address those circumstances.
You are likely to spend time in organizations where both of those are challenging due to internal limitations,
so it's worth acknowledging that and discussing how to navigate those challenges.

### Low-trust environment

Sometimes the struggle to diagnose problems is a skill issue.
Being bad at strategy is in some ways the easy problem to solve: just do more strategy work to build expertise.
In other cases, you may see what the problems are fairly clearly, but not know how to acknowledge the problems
because your organization's culture would frown on it.
The latter is a diagnosis problem rooted in low-trust, and does make things more difficult.

The chapter on [Diagnosis](https://draftingstrategy.com/diagnosis/) recognizes this problem,
and admits that sometimes you have to whisper the controversial parts of a strategy:

> When you’re writing a strategy, you’ll often find yourself trying to choose between two awkward options:
> say something awkward or uncomfortable about your company or someone working within it, or
> omit a critical piece of your diagnosis that’s necessary to understand the wider thinking.
> Whenever you encounter this sort of debate, my advice is to find a way to include the diagnosis, but to reframe it into a palatable statement that avoids casting blame too narrowly.

In short, the solution to low-trust is to translate difficult messages into
softer, less direct versions that are acceptable to state.
If your goal is to hold people accountable, this can feel dishonest or
like a ethical compromise, but the goal of strategy is to make better decisions,
which is an entirely different concern than holding folks accountable for the past.

<div class="bg-light-gray br4 ph3 pv1">

**Karpman Drama Triangle**

Sometimes when the diagnosis seems particularly obvious,
and people don't agree with you,
it's because you are wrong.
When I've been obviously wrong about things I understand well,
it's usually because I've fallen into viewing a situation through the
[Karpman Drama Triangle](https://en.wikipedia.org/wiki/Karpman_drama_triangle),
where all parties are mapped onto roles as persecutor, rescuer, or victim.

</div>

## Poor-judgment environment

Even when you do an excellent job diagnosing challenges,
it can be difficult to drive agreement within the organization
about how to address them.
Sometimes this is due to genuinely complex tradeoffs,
for example in [Stripe's acquisition of Index](https://draftingstrategy.com/index-acquisition-strategy/),
there was debate about how to deal with Index's Java-based technology stack,
which culminated in a compromise that didn't make anyone particularly happy:

> Defer making a decision regarding the introduction of Java to a later date: the introduction of Java is incompatible with our existing engineering strategy, but at this point we’ve also been unable to align stakeholders on how to address this decision. Further, we see attempting to address this issue as a distraction from our timely goal of launching a joint product within six months.
> 
> We will take up this discussion after launching the initial release.

That compromise is a good example of a difficult tradeoff:
although parties disagreed with the approach, everyone understood
the conflicting priorities that had to be addressed.

In other cases, though, there are policy choices that simply don't
make much sense, generally driven by poor judgment in your organization.
Sometimes it's not poor technical judgment, but poor judgment in choosing
to prioritize one's personal interests at the expense of the company's needs.
Calm's strategy to [focus on being a product-engineering organization](https://draftingstrategy.com/product-eng-strategy/)
dealt with some aspects of that, acknowledged in its diagnosis:

> We’re arguing a particularly large amount about adopting new technologies and rewrites. Most of our disagreements stem around adopting new technologies or rewriting existing components into new technology stacks. For example, can we extend this feature or do we have to migrate it to a service before extending it? Can we add this to our database or should we move it into a new Redis cache instead? Is JavaScript a sufficient programming language, or do we need to rewrite this functionality in Go?

In that situation, your strategy is an attempt to educate your colleagues
about the tradeoffs they are making, but ultimately sometimes folks will disagree with your
strategy.
In that case, remember that most interesting problems require iterative solutions.
Writing your strategy and sharing it will start to change the organization's mind.
Don’t get discouraged even if that change is initially slow.

### Dealing with missing strategies

The strategy for [dealing with new private equity ownership](https://draftingstrategy.com/private-equity-strategy/)
introduces a common problem: lack of clarity about what other parts of your own company
want. In that case, it seems likely there will be a layoff, but it's unclear how large
that layoff will be:

> Based on general practice, it seems likely that our new Private Equity ownership will expect us to reduce R&D headcount costs through a reduction.
> However, we don’t have any concrete details to make a structured decision on this, and our approach would vary significantly depending on the size of the reduction.

Many leaders encounter that sort of ambiguity and decide that they cannot move forward with
a strategy of their own until that decision is made.
While it's true that it's inconvenient not to know the details,
getting blocked by ambiguity is _always_ the wrong decision.

Instead you should do what the private equity strategy does: accept that ambiguity
as a fact to be worked around. Rather than giving up, it adopts a series of new policies
to start reducing cost growth by changing their [organization's seniority mix](https://draftingstrategy.com/private-equity-model/),
and recognizes that once there is clarity on reduction targets that there will be additional actions to be taken.

Whenever you're working on challenging problems, you can always find many reasons to justify not making progress.
Leadership is finding a way to move forward despite those issues. A missing strategy is always part of your
diagnosis, but never a reason that you can't do strategy.

## Who shouldn't do strategy

In my experience, there's almost never a reason why _you_ cannot do strategy,
but there are two particular scenarios where doing strategy probably doesn't make sense.
The first is not a who, but a [when problem](https://draftingstrategy.com/when-write-stratefy/):
sometimes there is so much strategy already happening, that doing more is a distraction.
If another part of your organization is already working on the same problem,
do your best to work with them directly rather than generating competing work.

The other time to avoid strategy is when you're trying to satisfy an emotional need to make a direct, immediate impact.
Sharing a thoughtful strategy always drives progress, though it's often the slow, incremental progress of changing your organization's beliefs.
Even definitive, top-down strategies from executives are often ignored in pockets of an organization,
and bottoms-up strategy spread slowly as they are modeled, documented and shared.
Embarking on strategy work requires a tolerance for winning in the long-run,
even when there's little progress this week or this quarter.

## Summary

As you finish reading this chapter, my hope is that you also believe
that you can work on strategy in your organization, whether you're
an engineer or an executive.
I also hope that you appreciate that the tools you use vary greatly
depending on who you are within your organization and the culture in which you work.
Whether you need to model or can mandate, there's a mechanism
that will work for you.