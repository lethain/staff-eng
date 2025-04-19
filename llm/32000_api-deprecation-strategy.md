# How should Stripe deprecate APIs? (~2016)
url: https://draftingstrategy.com/api-deprecation-strategy

While Stripe is a widely admired company for things like its
creation of the [Sorbet typer project](https://draftingstrategy.com/stripe-sorbet-strategy/), I personally
think that Stripe's most interesting strategy work is also among its most subtle:
its willingness to significantly prioritize API stability.

This strategy is almost invisible externally.
Internally, discussions around it were frequent and detailed, but mostly confined to dedicated API design conversations.
API stability isn't just a technical design quirk, it's a foundational decision in an API-driven business,
and I believe it is one of the unsung heroes of Stripe's business success.

## Reading this document

To apply this strategy, start at the top with _Policy_. To understand the thinking behind this strategy, read sections in reverse order, starting with _Explore_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy & Operation

Our policies for managing API changes are:

* **Design for long API lifetime.**
    APIs are not inherently durable. Instead we have to design thoughtfully
    to ensure they can support change.
    When designing a new API, build a test application that doesn't use this API,
    then migrate to the new API.
    Consider how integrations might evolve as applications change. Perform these migrations yourself to understand potential friction with your API.
    Then think about the future changes that _we_ might want to implement on our end.
    How would those changes impact the API, and how would they impact the application you've developed.

    At this point, take your API to API Review for initial approval as described below.
    Following that approval, identify a handful of early adopter companies
    who can place additional pressure on your API design, and test with them
    before releasing the final, stable API.
* **All new and modified APIs must be approved by API Review.**
    API changes may not be enabled for customers prior to API Review approval.
    Change requests should be sent to `api-review` email group.
    For examples of prior art, review the `api-review` archive for prior requests
    and the feedback they received.

    All requests must include a written proposal.
    Most requests will be approved asynchronously by a member of API Review.
    Complex or controversial proposals will require live discussions to ensure API Review members
    have sufficient context before making a decision.
* **We never deprecate APIs without an unavoidable requirement to do so.**
    Even if it's technically expensive to maintain support, we incur that support cost.
    To be explicit, we define API deprecation as _any_ change that would require customers to
    modify an existing integration.

    If such a change were to be approved as an exception to this policy,
    it must first be approved by the API Review, followed by our CEO.
    One example where we granted an exception was the deprecation of TLS 1.2 support due to PCI compliance obligations.
* **When significant new functionality is required, we add a new API.**
    For example, we created [`/v1/subscriptions`](https://docs.stripe.com/api/subscriptions) to
    support those workflows
    rather than extending [`/v1/charges`](https://docs.stripe.com/api/charges) to add subscriptions support.

<div class="bg-light-gray br4 ph3 pv1">

With the benefit of hindsight, a good example of this policy in action was the introduction of the Payment Intents APIs to maintain
compliance with [Europe's Strong Customer Authentication](https://support.stripe.com/questions/payment-intents-api-requirement-for-strong-customer-authentication-%28sca%29-compliance)
requirements. Even in that case the `charge` API continued to work as it did previously,
albeit only for non-European Union payments.

</div>

* **We manage this policy's implied technical debt via an API translation layer.**
    We release changed APIs into versions, tracked in our [API version changelog](https://docs.stripe.com/changelog).
    However, we only maintain one implementation internally, which is the implementation of the latest
    version of the API.
    On top of that implementation, a series of version transformations are maintained,
    which allow us to support prior versions without maintaining them directly.
    While this approach doesn't _eliminate_ the overhead of supporting multiple API versions,
    it significantly reduces complexity by enabling us to maintain just a single, modern implementation internally.
    
    All API modifications _must_ also update the version transformation layers to allow the new
    version to coexist peacefully with prior versions.
* **In the future, SDKs may allow us to soften this policy.**
    While a significant number of our customers have direct integrations with our APIs,
    that number has dropped significantly over time.
    Instead, most new integrations are performed via one of our official API SDKs.

    We believe that in the future, it may be possible for us to make more backwards
    incompatible changes because we can absorb the complexity of migrations into
    the SDKs we provide. That is certainly _not_ the case yet today.

## Diagnosis

Our diagnosis of the impact on API changes and deprecation on our business is:

* If you are a small startup composed of mostly engineers, integrating a new payments API seems easy.
    However, for a small business without dedicated engineers—or a larger
    enterprise involving numerous stakeholders—handling external API changes can be particularly challenging.

    Even if this is only marginally true, [we've modeled the impact of minimizing API changes](https://draftingstrategy.com/api-deprecation-model/)
    on long-term revenue growth, and it has a significant impact, unlocking our ability to benefit from
    other churn reduction work.
* While we believe API instability directly creates churn, we also believe that API stability
    directly retains customers by increasing the migration overhead even if they wanted to change providers.
    Without an API change forcing them to change their integration, we believe that hypergrowth customers
    are particularly unlikely to change payments API providers absent a concrete motivation like an
    API change or a payment plan change.
* We are aware of relatively few companies that provide long-term API stability in general,
    and particularly few for complex, dynamic areas like payments APIs.
    We can't assume that companies that make API changes are ill-informed.
    Rather it appears that they experience a meaningful technical debt tradeoff between the API provider and API consumers,
    and aren't willing to consistently absorb that technical debt internally.
* Future compliance or security requirements—along the lines of our upgrade from TLS 1.2 to TLS 1.3 for PCI—may necessitate API changes.
    There may also be new tradeoffs exposed as we enter new markets with their own compliance regimes.
    However, we have limited ability to predict these changes at this point.