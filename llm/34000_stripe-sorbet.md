# Why did Stripe build Sorbet? (~2017).

**This is a work in progress draft.**

Hi

Finally, I think it's intellectually important to recognize the limits of my own involvement in the Sorbet strategy.
While I ultimately led the organization that built Sorbet at Stripe,
my organization did not include the Developer Productivity team when they decided to build Sorbet.
Indeed, I initially disagreed with the approach: I preferred investing in a migration to a strongly-typed language
(specifically Golang), rather than spending time on creating and maintaining a typing framework for Ruby.

Ultimately, while both approaches _might_ have worked, the Sorbet strategy _did_ work,
and it was probably the better choice because it allowed us to concentrate the investment
into a small team rather than spreading the cost across every team within Stripe.

## Reading this document

To apply this strategy, start at the top with _Policy_. To understand the thinking behind this strategy, read sections in reserve order, starting with _Explore_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy & Operation

..

## Diagnose

* developer productivity surveys: Two stages – getting data, sitting with data ← imo this is how you learn; then picking a few specific projects and driving them; together this is the core DX team loop done on a one-off basis
    * imperfect: always something bad, so goal is sort of rotating what's bad
* migration of codebase will require many teams learning a new language
* adding ruby typing will allow a centralized team to make significant investments
* much of ruby typing can be done via the abstract syntax tree (AST)
* we can incrementally prioritize typing on highest value places
* ruby is not a high performance programing language, but it's generally good enough
    and we can get sufficient scale at a reasonable price