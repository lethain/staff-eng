# Steps to build an engineering strategy.
url: https://draftingstrategy.com/strategy-steps

Often you'll see a disorganized collection of ideas labeled as a "strategy."
Even when they're dense with ideas, such documents can be hard to parse, and are a major
reason why most engineers will claim their company doesn't have a clear strategy
even though in my experience, *all* companies follow some strategy, even if it's undocumented.

This chapter lays out a repeatable, structured approach to drafting strategy.
It introduces each step of that approach, which are then detailed further in their respective chapters.
Here we'll cover:

* How these five steps fit together to facilitate creating strategy,
    especially by preventing practitioners from skipping steps that feel awkward or challenging.
* Step 1: Exploring the wider industry's ideas and practices around the strategy you're working on.
    Exploration is understanding what recent research might change your approach,
    and how the state of the art has changed since you last tackled a similar problem.
* Step 2: Diagnosing the details of your problem.
    It's hard to slow down to understand your problem clearly before attempting
    to solve it, but it's even more difficult to solve anything well without
    a clear diagnosis.
* Step 3: Refinement is taking a raw, unproven set of ideas and testing them
    against reality. Three techniques are introduced to support this validation process:
    strategy testing, systems modeling, and Wardley mapping.
* Step 4: Policy makes the tradeoffs and decisions to solve your diagnosis.
    These can range from specifying how software is architected, to how pull requests are reviewed,
    to how headcount is allocated within an organization.
* Step 5: Operations are the concrete mechanisms that translate policy into an active force
    within your organization.
    These can be nudges that remind you about code changes without associated tests,
    or weekly meetings where you study progress on a migration.
* Whether these steps are sacred or are open to adaptation and experimentation,
    including when you personally should persevere in attempting steps that don't
    feel effective.

From this chapter's starting point,
you'll have a high-level summary of each step in strategy creation,
and can decide where you want to read further.

## How the steps become strategy

Creating effective strategy is not the rote incantation of a formula. You can’t merely follow these steps to guarantee that you'll create a great strategy.
However, what I’ve consistently found is that strategies fail more often due to avoidable errors than
from fundamentally unsound thinking.
Busy people skip steps. Especially steps they dislike or have failed at before.

These steps are the scaffolding to avoid those errors.
By practicing routinely, you'll build
powerful habits and intuition around which approach is most appropriate for the current strategy you're working on.
They also help turn strategy into a community practice that you, your colleagues,
and the wider engineering ecosystem can participate in together.

Each step is an input that flows into the next step. Your exploration is the foundation
of a solid diagnosis.
Your diagnosis helps you search the infinite space of policy for what you currently need.
Operational mechanisms help you turn policy into an active force supporting your
strategy rather than an abstract treatise.

If you're skeptical of the steps, you should certainly maintain your skepticism,
but do give them a few tries before discarding them entirely.
You may also appreciate the discussion in the chapter on
[bridging between theory and practice when doing strategy](https://draftingstrategy.com/theory-and-practice/).

## Explore

Exploration is the deliberate practice of searching through a strategy’s problem and solution spaces before allowing yourself to commit to a given approach.
It's understanding how other companies and teams have approached similar questions, and whether their approaches
might also work well for you. It's also learning why what brought you so much success at your former employer
isn't necessarily the best solution for your current organization.

The [Uber service migration strategy](https://draftingstrategy.com/uber-strategy/) used exploration
to understand the service ecosystem by reading industry literature:

> As a starting point, we find it valuable to read
> [Large-scale cluster management at Google with Borg](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf)
> which informed some elements of the approach to Kubernetes, and
> [Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center](https://people.eecs.berkeley.edu/~alig/papers/mesos.pdf)
> which describes the Mesos/Aurora approach.

It also used a [Wardley map](https://draftingstrategy.com/wardley-mapping/) to explore the cloud compute ecosystem.

**Image Description:** This image is a Wardley Map, which is used to visualize the components of a system and their stages of evolution. Here's a detailed breakdown:

1. **Axes:**
   - The vertical axis represents the visibility of components in the value chain, ranging from invisible (bottom) to visible (top).
   - The horizontal axis represents the evolution of components, from Genesis through Custom, Product (+rental), to Commodity (+utility).

2. **Components:**
   - The visible components include "Product Engineer," "Service Provisioning Team," "Server Operations Team," and activities like "Provision new service," "Route traffic to service," "Add capacity to provisioned service," and "Add server capacity to cluster."
   - Invisible components include "Service provision request workflow," "Service orchestration pipeline," "Request routing infrastructure," "Server vendor," and "Datacenter Contract."

3. **Evolution Line:**
   - Components like "Puppet & Clusto On-prem" are placed in the Custom stage.
   - "Mesos/Aurora On-prem" is in the transition between Custom and Product.
   - "Mesos/Aurora (or Kubernetes) in cloud" transitions from Product to Commodity.
   - "Serverless in cloud" falls into the Commodity stage, indicating it's a well-established and widely used component.

4. **Connections:**
   - Lines connect various components, illustrating their dependencies and interactions. For example, "Provision new service" is connected to the "

<p class="img-desc i tc f6">Evolution of service orchestration in 2014</p>

For more detail, read the [Exploration chapter](https://draftingstrategy.com/explore/).

## Diagnose

Diagnosis is your attempt to correctly recognize the context that the strategy needs to solve before deciding on the policies to address that context.
Starting from your exploration's learnings, and your understanding of your current circumstances,
building a diagnosis forces you to delay thinking about solutions until you fully understand your problem's nuances.

A diagnosis can be largely data driven, such as
the [navigating a Private Equity ownership transition strategy](https://draftingstrategy.com/private-equity-strategy/):

> Our Engineering headcount costs have grown by 15% YoY this year, and 18% YoY the prior year.
> Headcount grew 7% and 9% respectively, with the difference between headcount and headcount costs explained by salary band adjustments (4%),
> a focus on hiring senior roles (3%), and increased hiring in higher cost geographic regions (1%).

It can also be less data driven, instead aiming to summarize a problem,
such as the [Index acquisition strategy](https://draftingstrategy.com/index-acquisition-strategy/)'s
summary of the known and unknown elements of the technical integration
prior to the acquisition closing:

> We will need to rapidly integrate the acquired startup to meet this timeline. We only know a small number of details about what this will entail. We do know that point-of-sale devices directly operate on payment details (e.g. the point-of-sale device knows the credit card details of the card it reads).
> 
> Our compliance obligations restrict such activity to our “tokenization environment”, a highly secured and isolated environment with direct access to payment details. This environment converts payment details into a unique token that other environments can utilize to operate against payment details without the compliance overhead of having direct access to the underlying payment details.

The approach, and challenges, of developing a diagnosis are
detailed in the [Diagnosis chapter](https://draftingstrategy.com/diagnosis/).

## Refine (Test, Map & Model)

Strategy refinement is a toolkit of methods to identify which parts of your diagnosis
are most important, and verify that your approach to solving the diagnosis actually works.
This chapter delves into the details of using three methods in particular:
[strategy testing](https://draftingstrategy.com/strategy-testing/),
[systems modeling](https://draftingstrategy.com/systems-modeling/),
and [Wardley mapping](https://draftingstrategy.com/wardley-mapping/).

**Image Description:** The image is a flowchart depicting a request handling process involving a load balancer and a server. Here's a detailed description:

1. **Requests:**
   - Starts at the "Requests" block on the left.

2. **Load Balancer:**
   - Requests flow to the "Load Balancer" with a label "OK" indicating successful passage.
   - If there's an error in the load balancer, the flow diverts to "Failed Requests."

3. **Server:**
   - From the load balancer, requests move to the "Server," again marked "OK."
   - If there's an error in the server, the flow also diverts to "Failed Requests."

4. **Successful Requests:**
   - If the server processes requests successfully, they are routed to "Successful Requests."

5. **Failed Requests:**
   - They can originate from errors in either the load balancer or server.
   - In case of failed DNS resolution, requests flow directly to "Failed Requests."
   - A retry mechanism for failed requests is indicated by a loop back to "Requests" with a "Retry (529 HTTP)" label.

6. **Errors:**
   - Errors cause a deviation from the normal flow to "Failed Requests."
   - Specific error scenario lines include "Error in load balancer," "Error in server," and "DNS resolution failed."

The elements in the flowchart are displayed in purple, and the flow lines use different colors for clarity: purple

<p class="img-desc i tc f6">Requests succeeding and failing between a user, load balancer, and server</p>
<p class="tc"><em>An example of a systems modeling diagram.</em></p>

These techniques are also demonstrated in the strategy case studies,
such as the [Wardley map of the LLM ecosystem](https://draftingstrategy.com/wardley-llm-ecosystem/),
or the [systems model of backfilling roles without downleveling them](https://draftingstrategy.com/private-equity-model/).

For more detail, read the [Refinement chapter](https://draftingstrategy.com/refine/).

<div class="bg-light-gray br4 ph3 pv1">

### Why isn't refinement earlier (or later)?

A frequent point of disagreement is that refinement should occur before
the diagnosis. Another is that mapping and modeling are two distinct steps,
and mapping should occur before diagnosis, and modeling should occur
after policy.
A third is that refinement ought to be the final step of strategy,
turning the steps into a looping cycle.
These are all reasonable observations, so let me unpack
my rationale for this structure.

By _far_ the biggest risk for most strategies is not that you
model too early, or map too late, but instead that you simply skip
both steps entirely. My foremost concern is minimizing the required
investment into mapping and modeling such that more folks do these steps at all.
Refining after exploring and diagnosing allows you to concentrate your efforts
on a smaller number of load-bearing areas.

That said, it's common to refine many places in your strategy creation.
You're just as likely to have three small refinement steps as one bigger one.

</div>

## Policy

Policy is interpreting your diagnosis into a concrete plan.
This plan also needs to work, which requires careful study
of what's worked within your company, and what new ideas you've
discovered while exploring the current problem.

Policies can range from providing directional guidance,
such as the [user data controls strategy](https://draftingstrategy.com/user-data-strategy/)'s
guidance:

> **Good security discussions don’t frame decisions as a compromise between security and usability.** We will pursue multi-dimensional tradeoffs to simultaneously improve security and efficiency. Whenever we frame a discussion on trading off between security and utility, it’s a sign that we are having the wrong discussion, and that we should rethink our approach.
>
> We will prioritize mechanisms that can both automatically authorize and automatically document the rationale for accesses to customer data. The most obvious example of this is automatically granting access to a customer support agent for users who have an open support ticket assigned to that agent. (And removing that access when that ticket is reassigned or resolved.)

To committing not to make a decision until later,
as practiced in the [Index acquisition strategy](https://draftingstrategy.com/index-acquisition-strategy/):

> Defer making a decision regarding the introduction of Java to a later date: the introduction of Java is incompatible with our existing engineering strategy, but at this point we’ve also been unable to align stakeholders on how to address this decision. Further, we see attempting to address this issue as a distraction from our timely goal of launching a joint product within six months.
> 
> We will take up this discussion after launching the initial release.

This chapter further goes into evaluating policies,
overcoming ambiguous circumstances that make it difficult
to decide on an approach, and developing novel policies.

For full detail, read the [Policy chapter](https://draftingstrategy.com/policy/).

## Operations

Even the best policies have to be interpreted. There will be new circumstances
their authors never imagined, and the policies may be in effect long after their authors have left
the organization. Operational mechanisms are the concrete implementation of your policy.

The simplest mechanisms are an explicit escalation path,
as shown in [Calm's product engineering strategy](https://draftingstrategy.com/product-eng-strategy/):

> Exceptions are granted by the CTO, and must be in writing. The above policies are deliberately restrictive. Sometimes they may be wrong, and we will make exceptions to them. However, each exception should be deliberate and grounded in concrete problems we are aligned both on solving and how we solve them. If we all scatter towards our preferred solution, then we’ll create negative leverage for Calm rather than serving as the engine that advances our product.

From that starting point, the mechanisms can get far more complex.
This chapter works through evaluating mechanisms, composing an operational plan,
and the most common sorts of operational mechanisms that I've seen across strategies.

For more detail, read the [Operations chapter](https://draftingstrategy.com/operations/).

## Is the structure sacrosanct?

When someone's struggling to write a strategy document,
one of the first tools someone will often recommend is a strategy template.
Templates are great: they reduce the ambiguity in an already broad project
into something more tractable.
If you're wondering if you should use a template to craft strategy:
sure, go ahead!

However, I find that well-meaning, thoughtful templates often
turn into lumbering, callous documents that serve no one well.
The secret to good templates is that someone has to own it,
and that person has to care about the template writer first and foremost,
rather than the various constituencies that want to insert requirements
into the strategy creation process.
The security, compliance and cost of your plans matter a great deal,
but many organizations start to layer in more and more requirements
into these sorts of documents until the idea of writing them
becomes prohibitively painful.

The best advice I can give someone attempting to write
strategy, is that you should discard every element of strategy
that gets in your way *as long as* you can explain what that element
was intended to accomplish.
For example, if you're drafting a strategy and you don't find any
operational mechanisms that fit. That's fine, discard that section.
Ultimately, the structure is not sacrosanct, it's the thinking
behind the sections that really matter.

This topic is explored in more detail in the chapter on
[Making engineering strategies more readable](https://draftingstrategy.com/readable-strategy/).

## Summary

Now, you know the foundational steps to conducting strategy.
From here, you can dive into the details with the strategy case studies
like [How should you adopt LLMs?](https://draftingstrategy.com/llm-adoption-strategy/)
or you can maintain a high altitude starting with
how [exploration creates the foundation for an effective strategy](https://draftingstrategy.com/explore/).

Whichever you start with, I encourage you to eventually work through both
to get the full perspective.