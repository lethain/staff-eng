# "We're a product engineering company!" — Engineering strategy at Calm.
url: https://draftingstrategy.com/product-eng-strategy

In my career, the majority of the strategy work I've done has been in non-executive roles,
things like [Uber's service migration](https://draftingstrategy.com/uber-strategy/).
Joining Calm was my first executive role, where I was able to not only propose but also mandate strategy.

Like almost all startups, the engineering team was scattered when I joined.
Was our most important work creating more scalable infrastructure?
Was our greatest risk the failure to adopt leading programming languages?
How did we rescue the stuck [service decomposition initiative](https://draftingstrategy.com/monolith-decomposition-strategy/)?

This strategy is where the engineering team and I aligned after numerous rounds of iteration,
debate, and inevitably some disagreement. As a strategy, it's both basic and also unambiguous
about what we valued, and I believe it's a reasonably good starting point for any [low scalability-complexity](https://lethain.com/quality/)
consumer product.

## Reading this document

To apply this strategy, start at the top with _Policy_. To understand the thinking behind this strategy, read sections in reverse order, starting with _Explore_, then _Diagnose_ and so on.
Relative to the default structure, this document has one tweak, folding the _Operation_ section in with _Policy_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy & Operation

Our new policies, and the mechanisms to operate them are:

* **We are a product engineering company.**
    Users write in every day to tell us that our product has changed their lives for the better.
    Our technical infrastructure doesn't get many user letters--and this is unlikely to change going forward
    as our infrastructure is relatively low-scale and low-complexity.
    Rather than attempting to change that, we want to devote the absolute maximum possible attention to product engineering.
* **We exclusively adopt new technologies to create valuable product capabilities.**
    We believe our technology stack as it exists today can solve the majority of our current and future product roadmaps.
    In the rare case where we adopt a new technology, we do so because a product capability is inherently impossible
    without adopting a new technology.
    
    We do not adopt new technologies for other reasons. For example, we would not adopt a new technology because
    someone is interested in learning about it. Nor would we adopt a technology because it is 30% _better suited_
    to a task.
* **We write all code in the monolith.**
    It has been ambiguous if new code (especially new application code) should be written in our JavaScript monolith,
    or if all new code _must_ be written in a new service outside of the monolith.
    This is no longer ambiguous: all new code must be written in the monolith.

    In the rare case that there is a functional requirement that makes writing in the monolith implausible,
    then you should request an exception as described below.
* **Exceptions are granted by the CTO, and must be in writing.**
    The above policies are deliberately restrictive. Sometimes they may be wrong, and we will
    make exceptions to them. However, each exception should be deliberate and grounded in concrete
    problems we are aligned both on solving and how we solve them.
    If we all scatter towards our preferred solution, then we'll create negative leverage for Calm
    rather than serving as the engine that advances our product.
    
    All exceptions must be written. If they are not written, then you should operate as if it has not been granted.
    Our goal is to avoid ambiguity around whether an exception has, or has not, been approved.
    If there's no written record that the CTO approved it, then it's not approved.

Proving the point about exceptions, there are two confirmed exceptions to the above strategy:

1. **We are incrementally migrating to TypeScript.**
    We have found that static typing can prevent a number of our user-facing bugs.
    TypeScript provides a clean, incremental migration path for our JavaScript codebase,
    and we aim to migrate the entirety over the next six months.

    Our Web engineering team is leading this migration.
2. **We are evaluating Postgres Aurora as our primary database.**
    Many of our recent production incidents are caused by index scans
    for tables with high write velocity such as tracking customer logins.
    We believe Aurora will perform better under these workloads.

    Our Infrastructure engineering team is leading this initiative.

## Diagnose

The current state of our engineering organization:

* **Our product is not limited by missing infrastructure capabilities.**
    Reviewing our roadmap, there's nothing that we are trying to build today
    or over the next year that is constrained by our technical infrastructure.
* **Our uptime, stability and latency are OK but not great.**
    We have semi-frequent stability and latency issues in our application,
    all of which are caused by one of two issues.
    First, deploying new code with a missing index because it performed well enough in a test environment.
    Second, writes to a small number of extremely large, skinny tables have become expensive in combination
    with scans over those tables' indexes.
* **Our infrastructure team is split between supporting monolith and service workflows.**
    One way to measure technical debt is to understand how much time the team is spending
    maintaining the current infrastructure. Today, that is meaningful but not overwhelming
    work for our team of three infrastructure engineers supporting 30 product engineers.

    However, we _are_ finding infrastructure engineers increasingly pulled into debugging
    incidents for components moved out of the central monolith into our service architecture.
    This is partially due to increased inherent complexity, but it's more due to exposing
    lack of monitoring and ambiguous accountability in services' production incidents.
* **Our product and executive stakeholders experience us as competing factions.**
    Engineering exists to build and operate software in the company.
    Part of that is being easy to work with. We should not necessarily support every ask from Product
    if we believe they are misaligned with Engineering's goals (e.g. maintaining security),
    but it should generally provide a consistent perspective across our team.

    Today, our stakeholders believe they will get radically different answers to basic
    questions of capabilities and approach depending on who they ask. If they try to
    get a group of engineers to agree on an approach, they often find we derail into
    debate about approach rather than articulating a clear point of view that allows
    the conversation to move forward.
* **We're spending an outsized amount of time debating technology adoptions and rewrites.**
    Most of our disagreements stem from adopting new technologies or rewriting existing
    components into new technology stacks. For example, can we extend this feature or
    do we have to migrate it to a service before extending it?
    Can we add this to our database or should we move it into a new Redis cache instead?
    Is JavaScript a sufficient programming language, or do we need to rewrite this functionality in Go?

    This is particularly relevant to next steps around the ongoing services migration,
    which has been in-flight for over a year, but is yet to move any core production code.
* **We are spending more time on infrastructure and platform work than product work.**
    This is the combination of all the above issues, from the stability issues we are
    encountering in our database design, to the lack of engineering alignment on execution.
    This places us at odds with stakeholders' expectations that we are predominantly focused
    on new product development.

## Explore

Calm is a mobile application that guides users to build and maintain either a meditation or sleep habit.
Recommendations and guidance across content are individual to the user, but the content is shared across
all customers and is amenable to caching on a content delivery network (CDN).
As long as the CDN is available, the mobile application can operate despite the inability to access servers
(e.g. the application remains usable from a user's perspective, even if the non-CDN production infrastructure
is unreachable).

In 2010, enabling a product of this complexity would have required significant bespoke infrastructure,
along with likely maintaining a physical presence in a series of datacenters to run your software.
In 2020, comparable applications are generally moving towards maintaining as little internal infrastructure as possible.
This perspective is summarized effectively in Intercom's [Run Less Software](https://www.intercom.com/blog/run-less-software/)
and Dan McKinley's [Choose Boring Technology](https://mcfunley.com/choose-boring-technology).

New companies founded in this space view essentially all infrastructure as a commodity bought off your cloud provider.
This even extends to areas of innovation, such as machine learning, where the training infrastructure is typically
run on an offering like AWS Bedrock, and the model infrastructure is provided by Anthropic or OpenAI.