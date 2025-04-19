# Steps to build an engineering strategy.

**This is a work-in-progress draft!**

Often you'll see a disorganized collection of ideas labeled as a "strategy."
Even when they're dense with ideas, these can be hard to parse, and are a major
reason why most engineers will claim their company doesn't have a clear strategy
even though *all* companies follow some strategy, even if it's undocumented.

This chapter lays out a repeatable, structured approach to creating strategy, covering:

* Why structured steps are useful to developing strategy
* Explore
* Diagnose
* Refine
* Policy
* Operation
* How these five steps fit together into strategy
* Whether these steps are sacred or advisory

When you're done with this chapter, you'll have a structured approach for writing a strategy document.
(It won't necessarily be easy to read though,
if you want to make a readable strategy, read through
[Making engineering strategies more readable](/readable-engineering-strategy-documents/).)





## Why these steps are useful

Many strategies get lost in format issues, or process issues, or are just justifying something that's already decided


## Explore

Experts, experts, experts. Talk to experts.
Talk to peers.

peers. Pull some ideas from other writing on strategy.


For more detail, read the [Exploration chapter](/exploring-for-strategy/).


## Diagnose

Talk to stakeholders.
Assess reality.
Debug previous failures, successes.
Consider: Technical, social, financial, etc.


For more detail, read the [Diagnosis chapter](/diagnosis-for-strategy/).

## Refine (Test, Map & Model)


**INCORPORATE:** I've added the idea of testing to this, and I do think it's one of
the missing special tools. e.g. people usually skip testing and go directly into rollout
before they even pressure test their strategy. This is basically doomed to fail every time.

From organizing:

> Now that we have our initial diagnosis written, it’s useful to refine our understanding of a few of the load-bearing aspects.

Load-bearing is a really critical point, because you're trying to maximize
testing/modeling/mapping energy on the most important areas rather than spending
more time on less essential.


This book will go into a variety of mapping and modeling techniques:

* .
* .

the details of using each specific techniques will be covered individually in dedicated chapters.


Refine: Mapping and modeling to visualize Engineering Strategy
It's rarely written down
Examples from case studies of strategies and how you might see them
Mapping strategies
Intuitive mapping: writing what feels right
Talking to a bunch of people – how most new execs build their model
Wardley mapping
Systems thinking and modeling
Constraint optimization as one subset (e.g. Phoenix Project)
Techniques from Technology Strategy Patterns
Surveying – e.g. ask a bunch of folks

For more detail, read the [Refinement chapter](/refining-eng-strategy/).




## Policy

What are categories of policy?
Need to refer to previous writing to think about this.

Policy: common approaches to solving engineering problems
Overview of Engineering Strategies – what can we learn from the deep-dives
Evaluating policy proposals
Benchmarking & “How big things get done” concepts
Policy Transitions – ‘invalidations of diagnosis and how they lead to major policy transitions, perhaps unexpectedly: transition to GenAI, web to Mobile, web 2.0, …


For more detail, read the [Policy chapter](/policy-for-strategy/).

## Operate

Even the best policies have to be interpreted. There will be new circumstances
its authors never imagined, and you must decide on mechanisms for applying its ideas to new needs.

Good strategies explicitly explain how to operate them:

* what are examples of it being correctly applied?
* how to get exceptions?
* who to ask for advice?

Operation: how to make an engineering strategy real
Processes/mechanisms of operation in case studies
Enforcement mechanisms
CTO
Architects
“Navigators”
Navigators – drafting a blog post on this
https://lethain.com/navigators/ 

For more detail, read the [Operations chapter](/operations-for-strategy/).


## How the steps become strategy

Sections: Explore, Diagnose, Refine (Test, Map & Model), Policy, Operation

**TODO:** Look through these, which are directly copied from https://lethain.com/eng-strategies/ for anything major I missed?



## Is the structure sacrosanct?

TODO: add link to template

I will provide a template.
I think templates are very useful for setting a floor of document quality.
However, they also set an artificial ceiling for quality, because sometimes
the template is a bad fit for a specific problem.

So my advice is: ignore the template if it gets in your way, as long as you
understand the rationale behind each of the sections and the tradeoffs of modifying
the sections.

Here are a few particularly common variations:

* Collapsing _Policy_ and _Operations_ into a single, merged section on
    strategies that are operationally simple,
    for example (link to the LLM strategy sample)


Add link to [Making engineering strategies more readable](/readable-engineering-strategy-documents/)


Quote from: organizing for writing/reading:

> Reiterating a point from [Components of engineering strategy](/components-of-eng-strategy/):
> it's always appropriate to change the structure that you develop or present a strategy,
> as long as you are making a deliberate, informed decision.


## Summary

Now, you know the foundational components of strategy,
and can dive into either working down from specific examples to the details
by starting with template strategy examples like
[How should you adopt LLMs?](/llm-adoption-strategy/)
or you can work bottom up, starting with the details of
how [exploration creates the foundation for an effective strategy](/exploring-for-strategy/).

**todo**: mention See [Bridging theory and practice in engineering strategy](/bridging-eng-strategy-theory-and-practice/).