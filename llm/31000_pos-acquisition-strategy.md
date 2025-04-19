# How to integrate Stripe's acquisition of Index? (2018)

While discussions around acquisitions often focus on
[technical diligence](https://lethain.com/engineering-in-mergers-and-acquisition/) and
deciding whether to make the acquisition, the integration that follows
afterwards can be even more complex.
There are few irreversible trapdoor decisions in engineering,
but decisions made early in an integration tend to be surprisingly durable.

This engineering strategy explores Stripe's approach to integrating
[their 2018 acquisition of Index](https://www.pymnts.com/news/partnerships-acquisitions/2018/stripe-pos-software-startup-index-acquisition/).
While a business book would focus on the rationale for the acquisition itself,
here that rationale is merely part of the diagnosis that defines
the integration tradeoffs. The integration itself is the area of focus.

Like most acquisitions, the team responsible for the integration has
only learned about the project after the deal closed,
which means early efforts are
a scramble to apply [strategy testing](/strategy-testing/)
to distinguish between optimistic dates and technical realities.

## Reading this document

To apply this strategy, start at the top with _Policy & Operation_. To understand the thinking behind this strategy, read sections in reserve order, starting with _Explore_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy & Operation

We're starting with little shared context between the acquired and acquiring engineering
teams, and have a six month timeline to launch a joint product.
So our starting policy is a mix of a commitment to joint refinement and several
provisional architectural policies:

1. **Meet at least weekly until the initial release is complete**:
    the involved leadership from Stripe and Index will hold a weekly sync meeting
    to refine our approach until we fulfill our initial release timeline.

    This meeting is jointly owned by Stripe's Head of Traffic Engineering and
    Index's Head of Engineering.
1. **Minimize changes to tokenization environment**: because point-of-sale devices directly work with
     customer payment details, the API that directly supports the point-of-sale device
    must live within our secured environment where payment details are stored.

    However, any other functionality _must not_ be added to our tokenization environment.
2. **All other functionality must exist in standard environments**: except for the minimum necessary
    functionality moving into the tokenization environment, everything else must be operated in
    our standard, non-tokenization environments.
    In particular, any software that requires frequent changes, or introduces complex external dependencies,
    should exist in the standard environments.
3. **Defer making a decision regarding the introduction of Java to a later date**: the introduction of Java is incompatible
    with our existing engineering strategy, but at this point we've also been unable to align stakeholders on
    how to address this decision. Further, we see attempting to address this issue as a distraction
    from our timely goal of launching a joint product within six months.

    We will take up this discussion after launching the initial release.
1. **Escalations come to paired leads**: given our limited shared context across teams,
    all escalations must come to both Stripe's Head of Traffic Engineering and
    Index's Head of Engineering.
2. **Security review of changes impacting tokenization environment**: we need to move quickly to launch
    the combined point-of-sale and payments product, but we _must not_ cut corners on
    security to launch faster. Security must be included and explicitly sign off
    on any integration decisions that involve our tokenization environment

## Diagnose

There are generally four categories of acquisitions: talent acquisitions to bring on a talented team,
business acquisitions to buy a company's revenue and product, technology acquisitions to add a differentiated
capability that would be challenging to develop internally, and time-to-market acquisitions where you
could develop the capability internally but can develop it meaningfully faster by acquiring a company.

While most acquisitions have a flavor of several of these dimensions, this acquisition
is primarily a time-to-market acquisition aimed to address these constraints:

* Several of our largest customers are pushing for us to provide a point-of-sale device integrated
    with our API-driven payments ecosystem. At least one has implied that we either provide this
    functionality on a committed timeline or they may churn to a competitor.
* We currently have no homegrown expertise in developing or integrating with hardware such
    as point-of-sale devices.
    Based on other zero-to-one efforts internally, we believe it would take about a year to
    hire the team, develop and launch a minimum-viable product for a point-of-sale device integrated into our platform.
* Where we've taken a horizontal approach to supporting web payments via an API,
    at least one of our competitors, Square, has taken a vertically integrated approach.
    While their API ecosystem is less developed than ours, they are a plausible destination
    for customers threatening to churn.    
* We believe that at least one of our enterprise customers will churn if our best commitment is
    launching a point-of-sale solution 12 months from now.
* We've decided to acquire a small point-of-sale startup, which we will use to commit
    to a six month timeframe for supporting an integrated point-of-sale device with
    our API ecosystem.
* We will need to rapidly integrate the acquired startup to meet this timeline.
    We only know a small number of details about what this will entail.
    We _do_ know that point-of-sale devices directly operate on payment details
    (e.g. the point-of-sale device knows the credit card details of the card it reads).
    
    Our compliance obligations restrict such activity to our "tokenization environment",
    a highly secured and isolated environment with direct access to payment details.
    This environment converts payment details into a unique token that other environments
    can utilize to operate against payment details without the compliance overhead of
    having direct access to the underlying payment details.
* Going into this technical integration, we have few details about the acquired company's
    technology stack. We do know that they are primarily a Java shop running on AWS, where
    we are primarily a Ruby (with some Go) shop running on AWS.

## Explore

Prior to this acquisition, we have done several small acquisitions.
None of those acquisitions had a meaningful product to integrate with ours,
so we don't have much of an internal playbook to anchor our approach in.

We do have limited experience in integrating technical acquisitions from
prior companies we've worked in, along with talking to peers at other
companies to mine their experience.
Synthesizing those experiences, the recurring patterns are:

1. Usually deal teams have made certain commitments,
    or the acquired team has understood certain commitments,
    that will be challenging to facilitate.
    This is doubly true when you are unaware of what those commitments might be.

    If folks seem to be behaving oddly, it might be one such misunderstanding,
    and it's worth engaging directly to debug the confusion.
2. There should be an executive sponsor for the acquisition,
    and the sponsor is typically the best person to ask about the company's intentions.
    If you can't find the executive sponsor, or they are not engaged,
    try to recruit a new executive sponsor rather than trying to make
    things work without one.
2. Close the culture gap quickly where there's little friction,
    and cautiously where there's little trust.

    We do need to bring the acquired company into our culture,
    but we have years to do that. The most successful stories of doing this
    leaned on a mix of moving folks into and out of the acquired team rather than
    applying force.
3. The long-term cost of supporting a new technology stack is
    high, and in conflict with our technology strategy of consolidating on
    as few programming languages as possible.

    This is not the place to be flexible, as each additional feature
    in the new stack will
    take you further from your desired outcome.
4. Finally, find a way to derisk key departures. Things can go wrong
    quickly. One of the easiest starting points is consolidating
    infrastructure immediately, even if the product or software takes
    longer.

Altogether, this was not the most reassuring exploration: it was a bit
abstract, and much of our research returned strongly-held, conflicting perspectives.
Perhaps acquisitions, like starting a new company, is one of those places
where there's simply no right way to do it well.