# Should we decompose our monolith?

From their [first introduction in 2005](https://en.wikipedia.org/wiki/Microservices), the debate between adopting
a microservices architecture, a monolithic service architecture, or a hybrid between the two has become one of the
least-reversible decisions that most engineering organizations make.
Even migrating to a different database technology is _generally_ a less expensive change than moving from monolith
to microservices or from microservices to monolith.

The industry has in many ways gone full circle on that debate, from most hyperscalers in the 2010s partaking in
a multi-year monolith to microservices migration, to
[Kelsey Hightower's iconic tweet on the perils of distributed monoliths](https://x.com/kelseyhightower/status/940259898331238402):

> 2020 prediction: Monolithic applications will be back in style after people discover the drawbacks of distributed monolithic applications.
> \- @KelseyHightower

Even as popular sentiment has generally turned away from microservices, many engineering organizations have a bit of both,
often the remnants of one or more earlier but incomplete migration efforts. This strategy looks at a theoretical
organization stuck with a bit of both approaches, let's call it Theoretical Compliance Company,  which is looking to determine its path forward.

Here is Theoretical Compliance Company's service architecture strategy.

---

*This is an exploratory, draft chapter for a book on engineering strategy that I'm brainstorming in [#eng-strategy-book](https://lethain.com/tags/eng-strategy-book/).*
*As such, some of the links go to other draft chapters, both published drafts and very early, unpublished drafts.*

## Reading this document

To apply this strategy, start at the top with _Policy_. To understand the thinking behind this strategy, read sections in reverse order, starting with _Explore_, then _Diagnose_ and so on.
Relative to the default structure, this document has been refactored in two ways
to improve readability:
first, _Operation_ has been folded into _Policy_;
second, _Refine_ has been embedded in _Diagnose_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy

Our policy for service architecture is documented here.
All exceptions to this policy **must** escalate _to_ a local Staff-plus engineer for their
approval, and then escalate _with_ that Staff-plus engineer to the CTO.
If you have questions about the policies, ask in `#eng-strategy`.

Our policy is:

1. **Business units should always operate in their own code repository and monolith.**
    They should not provision many different services. They should rarely work in other business units monoliths.
    There are nuances in the details: make decisions that bring us closer to the preceding sentence being true.
2. **New integrations across business unit monoliths should be done using gRPC.**
    The emphasis here is on _new_ integrations;
    it's desirable but not urgent to migrate existing integrations that use other implementations (HTTP/JSON, etc).

    When the decision is subtle (e.g. changes to an existing endpoint), optimize for
    business velocity rather than technical purity. When the decision is far from subtle (e.g. brand new endpoint),
    comply with the policy.
3. **Except for new business unit monoliths, we don't allow new services.**
    You should work within the most appropriate business unit monolith or within the existing infrastructure repositories.
    Provisioning a new service, unless it corresponds with a new business unit, always
    requires approval from the CTO in `#eng-strategy`.

    That approval generally will *not* be granted, unless
    the new service requires significantly different non-functional requirements than an existing monolith.
    For example, if it requires significantly higher compliance review prior to changes such as our existing
    payments service, or if it requires radically higher requests per second, and so on.
4. **Merge existing services into business-unit monoliths where you can.**
    We believe that each choice to move existing services back into a monolith should
    be made "in the details" rather than from a top-down strategy perspective. Consequently,
    we generally encourage teams to wind down their existing services outside of their business unit's monolith,
    but defer to teams to make the right decision for their local context.

## Diagnose

Theoretical Compliance Company has a complex history with decomposing our monolith.
We are also increasing our number of business units, while limiting our investment into
our core business unit. These are complex times, with a lot of constraints to juggle.
To improve readability, we've split the diagnosis into
two sections: "business constraints" and "engineering constraints."

Our business constraints are:

1. We sell business-to-business compliance solutions to other companies on an annual subscription.
    There is one major, established business line, and two smaller partially validated business lines
    that are intended to attach to the established business line to increase average contract value.
2. There are 2,000 people at the company. About 500 of those are in the engineering organization
    Within that 500, about 150 work on the broadest definition of "infrastructure engineering,"
    things like developer tools, compute and orchestration, networking, security engineering, and so on.
3. The business is profitable, but revenue growth has been 10-20% YoY, creating persistent pressure on spend
    from our board, based on mild underperformance relative to public market comparables.
    **Unless we can increase YoY growth by 5-10%, they expect us to improve free cash flow by 5-10% each year**,
    which jeopardizes our ability to maintain long-term infrastructure investments.
4. **Growth in the primary business line is shrinking.**
    The company's strategy includes spinning up more adjacent business units to increase average contract value with new products.
    **We need to fund these business units without increasing our overall budget**,
    which means budget for the new business units must be pulled away from either our core business or our platform teams.
    
    In addition to needing to fund our new business units, **there's ongoing pressure to make our core business more efficient**,
    which means either accelerating growth or reducing investment. It's challenging to accelerate growth while reducing investment,
    which suggests that most improvement will come from reducing our investment
5. Our methodology to allocate platform costs against business units does so proportionately to
    the revenue created by each business unit. **Our core business generates the majority of our revenue, which means it is accountable for the majority of our platform costs**,
    even if those costs are motivated by new business lines.
    
    This means that, even as the burden placed on platform teams increases due to spinning up multiple business units,
    there's significant financial pressure to reduce our platform spend because it's primarily represented as a cost to the core business
    whose efficiency we have to improve.
    This means we have little tolerance for anything that increases infrastructure overhead.

Our engineering constraints are:

1. Our infrastructure engineering team is 150 engineers supporting 350 product engineers,
    and it's certain that **infrastructure will not grow significantly in the foreseeable future**.
2. We spun up two new business units in the past six months, and **plan to spin up an additional two new business units**
    in the next year. Each business unit is led by a general manager, with engineering and product within that business unit
    principally accountable to that general manager. Our CTO and CPO still set practice standards, but it's situationally-specific
    whether these practice standards or direction from general manager is the last word on any given debate.

    For example, one business unit has been unwilling to support an on-call rotation for their product, because their general
    manager insists it is a wasteful practice. Consequently, that team often doesn't respond to pages, even when their service
    is responsible for impacting the stability of shared functionality.
3. We've modeled [how services and monoliths create overhead for both product and infrastructure organizations over time](https://lethain.com/services-overhead-model/),
    and have conviction that, in general, **it's more overhead for infrastructure to support more services**.
    We also found that in our organization, the rate of service ownership changing due to team reorganizations counteracts much of the initial productivity
    gains from leaving the monolith.
4. There is some tension between the two preceding observations: it's generally more overhead to have more services,
    but it's _even more_ overhead to have irresponsible business units breaking a shared monolithic service.
    For example, we can much more easily rate limit usage from a misbehaving service than fix a misbehaving codepath
    within a shared service.
5. We also have a payments service that moves money from customers to us.
    **Our compliance and security requirements for changes to this service are significantly higher**
    than for the majority of our software, because the blast radius is essentially infinite.
6. Our primary programming language is Ruby, which generally relies on blocking IO,
    and service-oriented architectures generally spend more time on blocking IO than monoliths.
    Similarly, Ruby is _relatively_ inefficient at serializing and deserializing JSON payloads,
    which our service architecture requires as part of cross-service communication.
7. We've previously attempted to decompose, and have **a number of lingering partial migrations that don't align cleanly with our current business unit ownership structure**.
    The number of these new services continues to grow over time,
    creating more burden on both infrastructure today and product teams in the future as they try to 
    maintain these services through various team reorganizations.

## Explore

In the late 2010s, most large or scaling companies adopted services to some extent.
Few adopted microservices, with the majority of adopters opting for a [service-oriented architecture](https://aws.amazon.com/compare/the-difference-between-soa-microservices/) instead.
[Kelsey Hightower's iconic tweet on the perils of distributed monoliths](https://x.com/kelseyhightower/status/940259898331238402) in 2020
captured the beginning of a reversal, with more companies recognizing the burden of operating service-oriented architectures.

In addition to the wider recognition of those burdens, many of the cloud infrastructure challenges that originally motivated service architectures began
to mellow. Most infrastructure engineers today _only_ know how to operate with cloud-native patterns, rather than starting from machine oriented approaches.
Standard database technologies like PostgreSQL have significantly improved capabilities. Cloud providers have fast local caches for quickly retrieving verified upstream packages.
Supply and cost of cloud compute is affordable. Slow programming languages are faster than they were a decade ago. Untyped languages have reasonable incremental paths
to typed codebases.

As a result of this shift, if you look at a new, emerging company,  it's particularly likely to have a monolith in one backend and one frontend programming language.
However, if you look at a five-plus-year-old company, you might find almost anything. One particularly common case is a monolith with most functionality,
and an inconsistent constellation of team-scoped macroservices scattered across the organization.

The shift away from [zero interest-rate policy](https://en.wikipedia.org/wiki/Zero_interest-rate_policy) has also impacted trends,
as service-oriented architectures tend to require more infrastructure to operate efficiently, such as service meshes, service provisioning and deprovisioning, etc.
Properly tuned, service-oriented architectures ought to be cost competitive, and potentially superior in complex workloads, but it's
hard to maintain the required investment in infrastructure teams when in a cost-cutting environment.
This has encouraged new companies to restrict themselves to monolithic approaches, and pushed existing companies to
_attempt_ to reverse their efforts to decompose their prior monoliths, with mixed results.