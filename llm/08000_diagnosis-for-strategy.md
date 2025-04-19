# Diagnosis
url: https://draftingstrategy.com/diagnosis

Once you've written your [strategy's exploration](https://draftingstrategy.com/explore/),
the next step is working on its diagnosis.
Diagnosis is understanding the constraints and challenges your strategy needs to address.
In particular, it’s about slowing yourself down from jumping to solutions
before fully understanding the nuances and constraints of the problem.

If you ever find yourself wanting to skip the diagnosis phase--let's get to the solution already!--then
maybe it's worth acknowledging that every strategy that I've seen fail, did so due to a lazy or inaccurate diagnoses.
It's very challenging to fail with a proper diagnosis, and almost impossible to succeed without one.

The topics this chapter will cover are:

* Why diagnosis forms the foundation of an effective strategy, and how effective policies depend upon it.
    Conversely, how skipping the diagnosis phase consistently ruins strategies
* A step-by-step approach to diagnosing your strategy's circumstances
* How to incorporate data into your diagnosis effectively,
    and where to focus on adding data
* Dealing with controversial elements of your diagnosis,
    such as pointing out that your own executive is one
    of the challenges to solve
* Why it's more effective to view difficulties as part
    of the problem to be solved, rather than a blocking
    issue that prevents making forward progress
* The near impossibility of an effective diagnosis
    if you don't bring humility and self-awareness
    to the process

Into the details we go!

## Diagnosis is strategy's foundation

One of the challenges in evaluating strategy is that, after the fact,
many effective strategies are so obvious that they're pretty boring.
Similarly, most ineffective strategies are so clearly flawed that their
authors look lazy.
That's because, as a strategy is operated, the reality around it becomes clear.
When you're writing your strategy, you don't know if you can convince your colleagues
to adopt a new approach to specifying APIs, but a year later you know very definitively
whether it's possible.

Building your strategy's diagnosis is your attempt to correctly recognize the context that
the strategy needs to solve before deciding on the policies to address that context.
Done well, the subsequent steps of writing strategy often feel like an afterthought,
which is why I think of diagnosis as strategy's foundation.

Where [exploration](https://draftingstrategy.com/explore/) was an evaluation-free activity,
diagnosis is all about evaluation. How do teams feel today? Why did that project fail?
Why did the last strategy go poorly? What will be the distractions to overcome to make
this new strategy successful?

That said, not all evaluation is equal. If you state your judgment directly, it's easy to dispute.
An effective diagnosis is hard to argue against, because it's
a web of interconnected observations, facts, and data.
Even for folks who dislike your conclusions, the weight of evidence
should be hard to shift.

<div class="bg-light-gray br4 ph3 pv1">

[Strategy testing](https://draftingstrategy.com/strategy-testing/), explored in the Refinement section,
takes advantage of the reality that it's easier to diagnose by doing than by speculating.
It proposes a recursive diagnosis process until you have real-world evidence that the strategy is working.

</div>

## How to develop your diagnosis

Your strategy is almost certain to fail unless you start from an effective diagnosis,
but how to build a diagnosis is often left unspecified.
That's because, for most folks, building the diagnosis is indeed a dark art: unspecified,
undiscussed, and uncontrollable.
I've been guilty of this as well; _The Engineering Executive's Primer_'s
[chapter on strategy](https://lethain.com/eng-strategies/) is notably silent on how to perform diagnosis.

So, yes, there is some truth to the idea that forming your diagnosis is an emergent, organic process rather
than a structured, mechanical one.
However, over time I've come to adopt a fairly structured approach:

1. **Braindump**, starting from a blank sheet of paper, write down your best understanding of the circumstances that
    inform your current strategy. Then set that piece of paper aside for the moment.
1. **Summarize exploration** on a new piece of paper, review the contents of your [exploration](https://draftingstrategy.com/explore/).
    Pull in every piece of diagnosis from similar situations that resonates with you.
    This is true for both internal and external works!
    For each diagnosis, tag whether it fits perfectly, or needs to be adjusted for your current circumstances.
    Then, once again, set the piece of paper aside.

3. **Mine for distinct perspectives** on yet another blank page, talking to different stakeholders
    and colleagues who you know are likely to disagree with your early thinking.
    Your goal is not to agree with this feedback. Instead, it's to understand their view.

    _[The Crux](https://www.amazon.com/Crux-How-Leaders-Become-Strategists-ebook/dp/B09G2QXXWX)_
    by Richard Rumelt anchors diagnosis in this approach, emphasizing the importance of "testing, adjusting, and changing the frame, or point of view."
4. **Synthesize views into one internally consistent perspective.**
    Sometimes the different perspectives you've gathered don't mesh well.
    They might well explicitly differ in what they believe the underlying problem
    is, as is typical in tension between platform and product engineering teams.
    The goal is to competently represent each of these perspectives in the diagnosis,
    even the ones you disagree with, so that later on you can evaluate your proposed approach
    against each of them.

    When synthesizing feedback goes poorly, it tends to fail in one of two ways.
    First, the author's opinion shines through so strongly that it renders the author
    suspect.
    Your goal isn’t to agree with every perspective, nor should your diagnosis crown one viewpoint as correct.
    The reader should see detailed perspectives without clearly sensing the author's biases.

    The second common issue is when a group tries to jointly own the synthesis,
    but creates fractured perspectives  rather than a unified one.
    I generally find that having one author who is accountable for representing all views
    works best to address both of these issues.
5. **Test drafts across perspectives.**
    Once you've written your initial diagnosis,
    you want to sit down with the people who you expect to disagree
    most fervently. Iterate with them until they agree that you've
    accurately captured their perspective.
    
    It might be that they
    disagree with some other viewpoints, but they should be able
    to agree that others hold those views. They might argue that
    the data you've included doesn't capture their full reality,
    in which case you can caveat the data by saying that their
    team disagrees that it's a comprehensive lens.
6. **Don't worry about getting the details perfectly right in your initial diagnosis.**
    You're trying to get the right crumbs to feed into the next phase,
    [strategy refinement](https://draftingstrategy.com/refine/).
    Allowing yourself to be directionally correct, rather than perfectly correct,
    makes it possible to cover a broad territory quickly.
    Getting caught up in perfecting details is an easy way to anchor yourself into one perspective
    prematurely.

At this point, I hope you're starting to predict how I'll conclude any recipe for
strategy creation:
if these steps feel overly mechanical to you, adjust them to something that feels
more natural and authentic. There's no perfect way to understand complex problems.
That said, if you feel uncertain, or are skeptical of your own track record,
I do encourage you to start with the above approach as a launching point.

## Incorporating data into your diagnosis

The diagnosis behind [Stripe's creation of Sorbet](https://draftingstrategy.com/stripe-sorbet-strategy/)
includes a number of pieces of data to help readers understand their reasoning.
For example, it covers staffing numbers of relevant teams, and the extent of test coverage in the Ruby code base.

If everyone has the same data, and the same assumptions about how that data is likely to change going forward,
then evaluating the strategy becomes vastly simpler.
Data is also your mechanism for supporting or critiquing the various views that
you've gathered when drafting your diagnosis; to an impartial reader, data will speak louder than passion.
If you're confident that a perspective is true, then include a data narrative that
supports it. If you believe another perspective is overstated, then include data that the reader
will require to come to the same conclusion.

Do your best to include data analysis with a link out to the full data,
rather than requiring readers to interpret the data themselves while they are reading.
As your strategy document travels further, there will be inevitable requests for
different cuts of data to help readers understand your thinking, and this is somewhat
preventable by linking to your original sources.

If much of the data you want doesn't exist today,
that's a fairly common scenario for strategy work: if the data to make the decision
easy already existed, you probably would have already made a decision rather than needing to
run a structured thinking process.
The next chapter [on refining strategy](https://draftingstrategy.com/refine/) covers a number of tools
that are useful for building confidence in low-data environments.

## Whisper the controversial parts

At one time, the company I worked at rolled out a bar raiser program styled after Amazon's,
where there was an interviewer from outside the team that had to approve every hire.
I spent some time arguing against adding this additional step as I didn't understand
what we were solving for, and I was surprised at how disinterested management was
about knowing if the new process actually improved outcomes.

What I didn't realize until much later was that most of the senior leadership distrusted one
of their peers, and had rolled out the bar raiser program solely to create
a mechanism to control that manager's hiring bar when the CTO was disinterested holding
that leader accountable.
(I also learned that these leaders didn't care much about implementing this policy,
resulting in bar raiser rejections being frequently ignored,
but that's a discussion for the [Operations for strategy chapter](https://draftingstrategy.com/operations/).)

This is a good example of a strategy that _does_ make sense with the full diagnosis,
but makes little sense without it, and where stating part of the diagnosis out loud is
nearly impossible. Even senior leaders are not generally allowed to write a document
that says, "The Director of Product Engineering is a bad hiring manager."

When you're writing a strategy, you'll often find yourself trying to choose between
two awkward options:

1. Say something awkward or uncomfortable about your company or someone working within it
2. Omit a critical piece of your diagnosis that's necessary to understand the wider thinking

Whenever you encounter this sort of debate, my advice is to find a way to include the diagnosis,
but to reframe it into a palatable statement that avoids casting blame too narrowly.
I think it's helpful to discuss a few concrete examples of this,
starting with the strategy for [navigating private equity](https://draftingstrategy.com/private-equity-strategy/),
whose diagnosis includes:

> Based on general practice, it seems likely that our new Private Equity ownership will expect us to reduce R&D headcount costs through a reduction. However, we don’t have any concrete details to make a structured decision on this, and our approach would vary significantly depending on the size of the reduction.

There are many things the authors of this strategy likely feel about their state of reality.
First, they are probably upset about the fact that their new private equity ownership is likely
to eliminate colleagues. Second, they are likely upset that there is no clear plan around what
they need to do, so they are stuck preparing for a wide range of potential outcomes.
However they feel, they stick to precise, factual statements.

For a second example, we can look to the [Uber service migration strategy](https://draftingstrategy.com/uber-strategy/):

> Within infrastructure engineering, there is a team of four engineers responsible for service provisioning today. While our organization is growing at a similar rate as product engineering, none of that additional headcount is being allocated directly to the team working on service provisioning. We do not anticipate this changing.

The team didn't _agree_ that their headcount should not be growing,
but it was the reality they were operating in. They acknowledged their reality
as a factual statement, without any additional commentary about that statement.

In both of these examples, they found a professional, non-judgmental way to acknowledge
the circumstances they were solving. The authors would have preferred that the leaders
behind those decisions take explicit accountability for them, but it would have undermined
the strategy work had they attempted to do it within their strategy writeup.

Excluding critical parts of your diagnosis makes your strategies particularly
hard to evaluate, copy or recreate.
Find a way to say things politely to make the strategy effective.
As always, strategies are much more about realities than ideals.

## Reframe blockers as part of diagnosis

When I work on strategy with early-career leaders,
an idea that comes up a lot is that an identified problem
means that strategy is not possible. For example, they might
argue that doing strategy work is impossible at their current
company because the executive team changes their mind too often.

That core insight is almost certainly true, but it's much more
powerful to reframe that as a diagnosis: if we don't find a way
to show concrete progress quickly, and use that to excite the executive team,
our strategy is likely to fail.
This transforms the thing preventing your strategy into a condition
your strategy needs to address.

Whenever you run into a reason why your strategy seems unlikely to work,
or why strategy overall seems difficult, you've found an important piece
of your diagnosis to include. There are never reasons why strategy simply
cannot succeed, only diagnoses you've failed to recognize.

For example, in [Calm's approach to resourcing Engineering-driven projects](https://draftingstrategy.com/project-resourcing-strategy/),
we knew that the company's informal approach to prioritization wasn't going to change.
Even if we convinced our peers in product management to change how _they_ planned,
we'd still be impacted by the executive team's informal planning which wasn't going to change.
Rather than preventing us from implementing a strategy,
those dynamics clarified what sort of approach could actually succeed.

## The role of self-awareness

Every problem of today is partially rooted in the decisions of yesterday.
If you've been with your organization for any duration at all,
this means that _you_ are directly or indirectly responsible for
a portion of the problems that your diagnosis ought to recognize.

This means that recognizing the impact of your prior actions in your diagnosis is a powerful demonstration
of self-awareness. It also suggests that your next strategy's success is rooted
in your self-awareness about your prior choices.
Don't be afraid to recognize the failures in your past work.
While changing your mind _without_ new data is a sign of chaotic leadership,
changing your mind _with_ new data is a sign of thoughtful leadership.

## Summary

Because diagnosis is the foundation of effective strategy,
I've always found it the most intimidating phase of strategy work.
While I think that's a somewhat unavoidable reality, my hope is
that this chapter has somewhat prepared you for that challenge.

The four most important things to remember are simply:

1. form your diagnosis before deciding how to solve it,
2. try especially hard to capture perspectives you initially disagree with,
3. supplement intuition with data where you can, and
4. accept that sometimes you're missing the data you need to fully understand.

The last piece in particular, is why many good strategies never get shared,
and the topic we'll address in the next chapter on [strategy refinement](https://draftingstrategy.com/refine/).