# Bridging theory and practice in engineering strategy.
url: https://draftingstrategy.com/theory-and-practice

Some people I've worked with have lost hope that engineering strategy
actually exists within _any_ engineering organizations.
I imagine that they, reading through the
[steps to build engineering strategy](https://draftingstrategy.com/strategy-steps/),
or the [strategy for resourcing Engineering-driven projects](https://draftingstrategy.com/project-resourcing-strategy/),
are not impressed. Instead, these ideas probably come across as theoretical at best.
In less polite company, they might describe these ideas as fake constructs.

Let's talk about it! Because they're right. In fact, they're right in two different ways.
First, this book is focused on explaining how to create clean, refined, and definitive strategy documents,
where initially most real strategy artifacts look rather messy.
Second, applying these techniques in practice can require a fair amount of creativity.
It might sound easy, but it's quite difficult in practice.

This chapter will cover:

* Why strategy documents need to be clear and definitive,
    especially when strategy development has been messy
* How to iterate on strategy when there are demands for unrealistic timelines
* Using strategy as non-executives, where others might override your strategy
* Handling dynamic, quickly changing environments where diagnosis can change frequently
* Working with indecisive stakeholders who don't provide clarity on approach
* Surviving other people's bad strategy work

Alright, let's dive into the many ways that praxis doesn't quite line up with theory.

## Clear and definitive documents

As explored in [Making engineering strategies more readable](https://draftingstrategy.com/readable-strategy/),
documents that feel intuitive to write are often fairly difficult to read. That's because thinking tends
to be a linear-ish journey from a problem to a solution. Most readers, on the other hand, usually just
want to know the solution and then move on. That's because good strategies are read for direction
(e.g. when a team wants to understand how they're supposed to solve a specific issue at hand)
far more frequently than they're read to build agreement (e.g. building stakeholder alignment
during the initial development of the strategy).

However, many organizations only produce writer-oriented strategy documents,
and may not have any reader-oriented documents at all.
If you've predominantly worked in those sorts of organizations,
then the first reader-oriented documents you encounter will seem artificial.

There are also organizations that have many reader-oriented documents,
but omit the rationale behind those documents. Those documents feel prescriptive
and heavy-handed, because the infrequent reader who _does_ want to understand
the thinking can't find it. Further, when they want to propose an alternative,
they have to do so without the rationale behind the current policies:
the absence of that context often transforms what was a collaborative problem-solving
opportunity into a political conflict.

With that in mind, I'd encourage you to see the frequent absence of these documents
as a major opportunity to drive strategy within your organization, rather than
evidence that these documents don't work. My experience is that they do.

## Doing strategy despite unrealistic timelines

The most frequent failure mode I see for strategy is when it's rushed,
and its authors accept that thinking must stop when the artificial deadline is reached.
Taking annual planning at Stripe as an example,
[Claire Hughes Johnson](https://www.amazon.com/Scaling-People-Tactics-Management-Building/dp/1953953212/)
argued that planning expands to fit any timeline, and consequently set a short planning timeline of
several weeks. Some teams accepted that as a fixed timeline and _stopped planning_ when the timeline
ended, whereas effective teams never stopped planning before or after the planning window.

When strategy work is given an artificial or unrealistic timeline,
you should deliver the best draft you can.
Afterwards, rather than being finished, you should view yourself as
[starting the refinement process](https://draftingstrategy.com/refine/).
An open strategy secret is that many strategies never leave
the refinement phase, and continue to be tweaked throughout their
lifespan. Why should a strategy with an early deadline be any different?

Well, there is one important problem to acknowledge:
I've often found that the executive who initially provided the
unrealistic timeline intended it as a forcing function to inspire action and quick thinking.
If you have a discussion with them directly, they're usually quite open to adjusting the approach.
However, the intermediate layers of leadership between that executive and you often calcify
on a particular approach which they claim that the executive insists on precisely following.

Sometimes having the conversation with the responsible executive is quite difficult.
In that case, you do have to work with individuals taking the strategy literally and as unalterable
until either you can have the conversation or something goes wrong enough that the executive
starts paying attention again. Usually, though, you can find someone who has a communication path,
as long as you can articulate the issue clearly.

## Using strategy as non-executives

Some engineers will argue that the only valid [strategy altitude](https://draftingstrategy.com/when-write-stratefy/)
is the highest one defined by executives, because any other strategy can be invalidated by
a new, higher altitude strategy.
They would claim that teams simply _cannot_ do strategy, because executives might invalidate it.
Some engineering executives would argue the same thing, instead claiming that they can't work on an engineering strategy
because the missing product strategy or business strategy might introduce new constraints.

I don't agree with this line of thinking at all.
To do strategy at any altitude, you have to come to terms with the certainty that
new information will show up, and you'll need to revise your strategy to deal with that.

The strategy for [controlling access to user data](https://draftingstrategy.com/user-data-strategy/) is a good counterexample
against the premise that effective strategy requires executive support.
The lack of progress had been framed as the result of limited executive engagement on the topic,
which had led to a disengaged team. However, as we started to work on the ergonomics of the problem,
we came to realize that we could significantly reduce unnecessary access to user data without
any top-down support at all.

When it comes to using strategy, effective diagnosis trumps authority.
At least as many executives' strategies are ravaged by reality's pervasive details as are overridden by higher altitude strategies.
The only way to be certain your strategy will fail is waiting until you're certain that
no new information might show up and require it changing.

## Doing strategy in chaotic environments

[How should you adopt LLMs?](https://draftingstrategy.com/llm-adoption-strategy/) discusses how a company should plot a path
through the rapidly evolving LLM ecosystem.
Periods of rapid technology evolution are one reason why your strategy might encounter a pocket of chaos,
but there are many others. Pockets of rapid hiring, as well as layoffs, create chaos.
The departure of load-bearing senior leaders can change a company quickly.
Slowing revenue in a company's core business can also initiate chaotic actions
in pursuit of a new business.

Strategies don't require stable environments. Instead, strategies require awareness of
the environment that they're operating in. In a stable period, a strategy might expect
to run for several years and expect relatively little deviation from the initial approach.
In a dynamic period, the strategy might know you can only protect capacity in two-week chunks
before a new critical initiative pops up.
It's possible to execute good strategy in either scenario, but it's impossible to execute good strategy
if you don't diagnose the context effectively.

## Unreliable information

Oftentimes, the way forward is very obvious if a few key decisions were made.
You know who is supposed to make those decisions, but you simply cannot get them
to decide.
My most visceral experience of this was conducting a layoff where the CEO wouldn't
define a target cost reduction or a thesis of how much various functions (e.g. engineering, marketing, sales)
should contribute to those reductions.
With those two decisions, engineering's approach would be obvious, and without that clarity
things felt impossible.

Although I was frustrated at the time,
I've since come to appreciate that missing decisions are the norm rather than the exception.
The strategy on [Navigating Private Equity ownership](https://draftingstrategy.com/private-equity-strategy/) deals with
this problem by acknowledging a missing decision, and expressly blocking one part of its execution
on that decision being made.
Other parts of its plan, like changing how roles are backfilled, went ahead to address
the broader cost problem.

Rather than blocking on missing information, your strategy should acknowledge what's
missing and move forward where you can. Sometimes that's moving forward by taking risk,
sometimes that's delaying for clarity, but it's never accepting that you're stuck
without options other than pointing a finger.

## Surviving other people's bad strategy work

Sometimes you will be told to follow something which is described as a strategy,
but is really just a policy without any strategic thinking behind it.
This is an unavoidable element of working in organizations and happens for all sorts of reasons.
Sometimes, your organization's leader doesn't believe it's valuable to explain their thinking to others,
because they see themselves as the one important decision maker.

Other times, your leader doesn't agree with a policy they've been instructed to roll out.
Adoption of "high hype" technologies like blockchain technologies during the crypto boom
was often top-down direction from company leadership that engineering disagreed with,
but was obligated to align with. In this case, your leader is finding that it's hard
to explain a strategy that they themselves don't understand either.

This is a frustrating situation. What I've found most effective is writing a strategy of my own,
one that acknowledges the broader strategy I disagree with in its diagnosis as a static, unavoidable truth.
From there, I've been able to make practical decisions that recognize the context, even if it's not
a context I'd have selected for myself.

## Summary

I started this chapter by acknowledging that the [steps to building engineering strategy](https://draftingstrategy.com/strategy-steps/)
are a theory of strategy, and one that can get quite messy in practice.
Now you know why strategy documents often come across as overly pristine--because they're trying to communicate clearly
about a complex topic.

You also know how to navigate the many ways reality pulls you away from perfect strategy,
such as unrealistic timelines, higher altitude strategies invalidating your own strategy work,
working in a chaotic environment, and dealing with stakeholders who refuse to align with your strategy.
Finally, we acknowledged that sometimes strategy work done by others is not what we'd consider strategy.
It's often unsupported policy with neither a diagnosis nor an approach to operating the policy.

That's all stuff you're going to run into, and it's all stuff you're going to overcome
on the path to doing good strategy work.