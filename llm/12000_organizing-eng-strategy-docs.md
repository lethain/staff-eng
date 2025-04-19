# Making engineering strategies more readable
url: https://draftingstrategy.com/readable-strategy

As discussed in [Components of engineering strategy](https://draftingstrategy.com/strategy-steps/),
a complete engineering strategy has five components: explore, diagnose, refine (map & model), policy, and operation.
However, it's actually quite challenging to read a strategy document written that way.
That's an effective sequence for *creating* a strategy, but it's a challenging sequence
for those trying to quickly *read and apply* a strategy without necessarily wanting to understand
the complete thinking behind each decision.

This post covers:

* Why the order for writing a strategy is hard to read
* How to organize a strategy document for reading
* How to refactor and merge components for improved readability
* Additional tips for effective strategy documents

After reading it, you should be able to take a written strategy and
rework it into a version that's much easier for others to read.

---

*This is an exploratory, draft chapter for a book on engineering strategy that I'm brainstorming in [#eng-strategy-book](https://lethain.com/tags/eng-strategy-book/).*
*As such, some of the links go to other draft chapters, both published drafts and very early, unpublished drafts.*

## Why writing structure inhibits reading

Most software engineers learn to structure documents early in their lives as
students writing academic essays. Academic essays are focused on presenting evidence
to support a clear thesis, and generally build forward towards their conclusion.
Some business consultancies explicitly train their new hires in business writing,
such as McKinsey teaching
Barbara Minto's *[The Pyramid Principle](https://www.amazon.com/Pyramid-Principle-Logic-Writing-Thinking/dp/0273710516)*,
but that's the exception.

While academic essays want to develop an argument, professional writing is a bit different.
Professional writing typically has one of three distinct goals:

* **Refining thinking about a given approach** ("how do we select databases for our new products?") -- this is an area where the academic structure can be useful,
    because it focuses on the thinking behind the proposal rather than the proposal itself
* **Seeking approval from stakeholders or executives** ("what database have we selected for our new analytics product?") -- this is an area where the academic structure
    creates a great deal of confusion, because it focuses on the thinking rather than the specific proposal,
    but stakeholders view the specific proposal as the primary topic to review
* **Communicating a policy to your organization** ("databases allowed for new products") -- helping engineers at your company
    understand the permitted options for a given problem, and also explaining the rationale behind the decision for
    the subset who may want to understand or challenge the current policy

The ideal format for the first case is generally at odds with the other two, which is a frequent cause of
strategy documents which struggle to graduate from brainstorm to policy.
I find that most strategy writers are resistant to the idea that it's worth their time to restructure their
initial documents, so let me expand on challenges I've encountered when I've personally tried to make
progress without restructuring:

* **Too long, didn't read.** Thinking-oriented structures leave policy recommendations at the very bottom,
    but the vast majority of strategy readers are simply trying to understand that policy so they can
    apply it to their specific problem at hand. Many of those readers, in my experience a majority of them,
    will simply give up before reading the sections that answer their questions and assume that the
    document doesn't provide clear direction because finding that direction took too long.

    This is very much akin to the core lesson of Steve Krug's [Don't Make Me Think](https://www.amazon.com/Dont-Make-Think-Revisited-Usability/dp/0321965515):
    users (and readers) don't understand, they muddle through.
    Assuming readers will invest significant time to deeply understand your document is an act of hubris.
* **Approval meeting to nowhere.** There are roughly three types of approval meetings. The first, you go in and no one has any feedback.
    Maybe someone gripes that it could have been done asynchronously instead of a meeting, but your document is approved.
    The second, there are two sets of stakeholders with incompatible goals, and you need a senior decision-maker to
    mediate between them. This is a very useful meeting, because you generally can't make progress without that
    senior decision-maker breaking the tie.
    
    The third sort of meeting is when you get derailed early with questions about the research, whether you'd considered
    another option, and whether this is even relevant. You might think this is because your strategy is wrong, but
    in my experience it's usually because you failed to structure the document to present the policy upfront.
    Stakeholders might disagree with many elements of your thinking but still agree with your ultimate policy,
    but it's only useful to dig into your rationale if they actually disagree with the policy itself.
    Avoid getting stuck debating details when you agree on the overarching approach by presenting the
    policy *first*, and only digging into those details when there's disagreement.
* **Transient alignment.** Sometimes you'll see two distinct strategy documents, with the first covering
    the full thinking, and the second only including the policy and operations sections.
    This tends to work quite well initially, but over time existing members of the team depart
    and new members are hired. At some point, a new member will challenge the thinking behind
    the strategy as obviously wrong, generally because it's a different set of policies than
    they used at the previous employer. If you omit the diagnosis and exploration sections entirely,
    then they can't trace through the decision making to understand the reasoning,
    which will often cause them to leap to simplistic conclusions like the
    ever popular, "I guess the previous engineers here were just dumb."

As annoying as each of these challenges is, the solution is simple:
use the writing structure for writing, and invert that structure for reading.

## Invert structure for reading

Reiterating a point from [Components of engineering strategy](https://draftingstrategy.com/strategy-steps/):
it's always appropriate to change the structure that you use to develop or present a strategy,
as long as you are making a deliberate, informed decision.

While I've generally found explore, diagnose, refine, policy, and operation to work well for
writing policy, I've consistently found it a poor format for presenting strategy.
Whether I'm presenting a strategy for review or rolling the strategy out to be followed by
the wider organization, I recommend an inverted structure:

* **Policy**: what does the strategy require or allow?
* **Operation**: how is the strategy enforced and carried out, how do I get exceptions for the policy?
* **Refine**: what were the load-bearing details that informed the strategy?
* **Diagnose**: what are the more generalized trends and observations that steered the thinking?
* **Explore**: what is the high-level, wide-ranging context that we brought into creating this strategy?

When seeking approval, you'll probably focus on the **Policy** section.
When rolling it out to your organization, you'll probably focus on the **Operation** section more.
In both cases, those are the critical components and you want them upfront.
Very few strategy readers want to understand the full thinking behind your strategy, instead they just
want to understand how it impacts the specific decision they are trying to answer.

The vast majority of strategy readers want the answer, not to understand the thinking behind the answer,
and these are your least motivated readers. Someone who wants to really understand the thinking will
invest time reading through the document, even if it isn't perfectly structured for them.
Someone who just wants an answer will frequently give up and make up an answer rather than reading all
the way through to where the document does in fact answer their question.

Zooming out a bit, this is a classic "lack of user empathy" problem. Folks authoring the document
are so deep in the details that they can't put themselves in the readers' mindset to think about
how overwhelming the document would be if you were simply trying to pop in, get an answer, and then pop out.
This lack of empathy also means that most strategy writers refuse to structure their documents to
support the large population of answer seekers over the tiny population of strategy authors,
but just try it a few times and I think you'll see it helps a great deal.
Even faster, go read someone else's strategy document that you aren't familiar with, and
you'll quickly appreciate how challenging it can be to identify the actual proposal
if they follow the academic structure.

## Strategy refactoring

Inverting the structure is the first step of optimizing a document
for readability, but you don't have to stop there. Often you'll
find that even the inverted strategy structure is somewhat confusing to read
for a given document. I think of this process as "strategy refactoring."

For example, [How should you adopt LLMs?](https://draftingstrategy.com/llm-adoption-strategy/) makes two refactors
to the inverted format. First, it merges *Refine* into *Diagnose*, which keeps
the map and models closer to the specific topics that are explored.
Second, it discards the *Operation* section entirely, and includes the relevant
details with the policies they apply to in the *Policy* section.

Strategy refactoring is about discarding structure where it interferes with usability.
The strategy structure is very effective at separating concerns while reasoning through
decision making, but most readers benefit more from engaging with the full implications at once.
Once you're done thinking, refactor away the thinking tools: don't let the best tools for
one workflow mislead you into thinking they're the best for an entirely different one.

## Additional tips for effective strategy docs

In addition to the above advice, there are a handful of smaller tips
that I've found helpful for creating readable strategy documents:

* Before releasing a document widely, find someone entirely uninvolved with the
    strategy thus far and have them point out areas that are difficult to understand.
    Anyone who's been thinking about the strategy is going to gloss over areas that might
    be inscrutinable to those who are approaching it with fresh eyes.
* Every strategy document should be rolled out with an explicit commenting period where you
    invite discussion, as well as office hours where you are available to explain how to apply
    the strategy correctly. These steps help with adoption, but even more importantly they
    help you identify dissenters who disagree with the strategy such that you can follow up
    to better understand their concerns.    
* Every company should maintain its own internal engineering strategy
    template, incorporating the notes in [making readable engineering strategies](https://draftingstrategy.com/readable-strategy/)
* Your template should include consistent metadata, particularly when it was created,
    the current approval status, and where to ask questions.
    Of these, a clear, durable place to ask questions is the most important,
    as it slows the rate that these documents rot.
* After you release your strategy, disable in-document commenting. This isn't intended to prevent further discussion,
    but rather to move the discussion outside of the document.
    Nothing creates the impression of an unapproved, unfinished strategy document
    faster than a long string of open comments. Open comments also make it difficult
    to read the strategy document, as often the reader will get distracted from reading
    the document to read the comments.

## Summary

After reading this chapter, you know how to escape the rigid structures imposed during the
creation of a strategy to create a readable document that is easier for others to both approve and apply.
Beyond initially inverting the structure for easier reading, you also understand how to refactor sections
away entirely that may have been essential for creation but interfere with understanding how to apply the strategy,
which is by far the most common task for strategy readers.

Most importantly, I hope you finish this chapter agreeing that it's worth your time to
rework your thinking-optimized draft rather than leaving it as is. The deliberate refusal
to structure documents for readers is the root cause of a surprising number of good strategies
that utterly fail to have their intended impact.