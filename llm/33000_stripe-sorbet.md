# Why did Stripe build Sorbet? (~2017).
url: https://draftingstrategy.com/stripe-sorbet-strategy

Many hypergrowth companies of the 2010s battled increasing complexity in
their codebase by [decomposing their monoliths](https://draftingstrategy.com/monolith-decomposition-strategy/).
Stripe was somewhat of an exception, largely delaying decomposition until
it had grown beyond three thousand engineers and had accumulated a decade of development in its core Ruby monolith.
Even now, significant portions of their product are
maintained in the monolithic repository, and it's safe to say this was only possible
because of Sorbet's impact.

Sorbet is a custom static type checker for Ruby that was initially designed and implemented by Stripe engineers
on their Product Infrastructure team.
Stripe's Product Infrastructure had similar goals to other companies' Developer Experience or Developer Productivity teams,
but it focused on improving productivity through changes in the internal architecture of the codebase itself,
rather than relying solely on external tooling or processes.

This strategy explains why Stripe chose to delay decomposition for so long,
and how the Product Infrastructure team invested in developer productivity to deal with the challenges
of a large Ruby codebase managed by a large software engineering team with low average tenure caused by rapid hiring.

Before wrapping this introduction, I want to explicitly acknowledge that this
strategy was spearheaded by Stripe's Product Infrastructure team, not by me.
Although I ultimately became responsible for that team,
I can't take credit for this strategy's thinking.
Rather, I was initially skeptical, preferring an incremental migration to an existing
strongly-typed programming language, either Java for library coverage or Golang
for Stripe's existing familiarity.
Despite my initial doubts, the Sorbet project eventually won me over with its indisputable results.

## Reading this document

To apply this strategy, start at the top with _Policy_. To understand the thinking behind this strategy, read sections in reverse order, starting with _Explore_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy & Operation

The Product Infrastructure team is investing in Stripe's
developer experience by:

* Every six months, Product Infrastructure will select its three highest priority areas to focus,
    and invest a significant majority of its energy into those.
    We will provide minimal support for other areas.

    We commit to refreshing our priorities every half after running the developer productivity survey.
    We will further share our results, and priorities, in each Quarterly Business Review.
* Our three highest priority areas for this half are:
    1. Add static typing to the highest value portions of our Ruby codebase,
        such that we can run the type checker locally and on the test machines to identify
        errors more quickly.
    2. Support selective test execution such that engineers can quickly determine and run
        the most appropriate tests on their machine rather than delaying until tests run
        on the build server.
    3. Instrument test failures such that we have better data to prioritize
        future efforts.
* Static typing is not a typical solution to developer productivity, so it
    requires some explanation when we say this is our highest priority area
    for investment. Doubly so when we acknowledge that it will take us 12-24 months
    of much of the team's time to get our type checker to an effective place.

    Our type checker, which we plan to name Sorbet, will allow us to continue developing
    within our existing Ruby codebase. It will further allow our product engineers
    to remain focused on developing new functionality rather than migrating existing
    functionality to new services or programming languages.
    Instead, our Product Infrastructure team will centrally absorb both the development
    of the type checker and the initial rollout to our codebase.
    
    It's possible for Product Infrastructure to take on both, despite its fixed size.
    We'll rely on a hybrid approach of deep-dives to add typing to particularly complex areas,
    and scripts to rewrite our code's Abstract Syntax Trees (AST) for less complex portions.
    In the relatively unlikely event that this approach fails, the cost to Stripe is of a small, known size:
    approximately six months of half the Product Infrastructure team, which is what we anticipate
    requiring to determine if this approach is viable.

    Based on our knowledge of Facebook's [Hack](https://hacklang.org/)
    project, we believe we can build a static type checker
    that runs locally and significantly faster than our test suite.
    It's hard to make a precise guess now, but we think less than 30 seconds to type our entire codebase,
    despite it being quite large.
    This will allow for a highly productive local development experience, even if we are not able to
    speed up local testing. Even if we do speed up local testing, typing would help us eliminate
    one of the categories of errors that testing has been unable to eliminate, which is passing
    of unexpected types across code paths which have been tested for expected scenarios but not
    for entirely unexpected scenarios.
    
    Once the type checker has been validated, we can incrementally prioritize adding typing
    to the highest value places across the codebase. We do not need to wholly type
    our codebase before we can start getting meaningful value.
* In support of these static typing efforts, we will advocate for product engineers at Stripe to begin development
    using the [Command Query Responsibility Segregation](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation)
    (CQRS) design pattern, which we believe
    will provide high-leverage interfaces for incrementally introducing static typing into our codebase.
* Selective test execution will allow developers to quickly run appropriate tests locally.
    This will allow engineers to stay in a tight local development loop, speeding up development
    of high quality code.

    Given that our codebase is not currently statically typed, inferring which tests to run is rather challenging.
    With our very high test coverage, and the fact that all tests will still be run before deployment to the
    production environment,
    we believe that we can rely on statistically inferring which tests are likely to fail when a given file is modified.
* Instrumenting test failures is our third, and lowest priority, project for this half.
    Our focus this half is purely on annotating errors for which we have high conviction about their source, whether infrastructure or test issues.
* For escalations and issues, reach out in the #product-infra channel.

## Diagnose

In 2017, Stripe is a company of about 1,000 people, including 400 software engineers.
We aim to grow our organization by about 70% year-over-year to meet increasing demand
for a broader product portfolio and to scale our existing products and infrastructure to accommodate user growth.
As our production stability has improved over the past several years, we have now turned
our focus towards improving developer productivity.

Our current diagnosis of our developer productivity is:

* We primarily fund developer productivity for our Ruby-authoring software engineers  via our Product Infrastructure team.
    The Ruby-focused portion of that team has about ten engineers on it today, and is unlikely to significantly grow in the future.
    (If we do expand, we are likely to staff non-Ruby ecosystems like Scala or Golang.)
* We have two primary mechanisms for understanding our engineer's developer experience.
    The first is standard productivity metrics around deploy time, deploy stability, test coverage, test time, test flakiness, and so on.
    The second is a twice annual developer productivity survey.
* Looking at our productivity metrics, our test coverage remains extremely high, with coverage above 99% of lines,
    and tests are quite slow to run locally. They run quickly in our infrastructure because they are multiplexed
    across a large fleet of test runners.
* Tests have become slow enough to run locally that an increasing number of developers
    run an overly narrow subset of tests, or entirely skip running tests until after pushing their changes.
    They instead rely on our test servers to run against their pull request's branch,
    which works well enough, but significantly slows down developer iteration time because the
    merge, build, and test cycle takes twenty to thirty minutes to complete.

    By the time their build-test cycle completes, they've lost their focus and maybe take several hours
    to return to addressing the results.
* There is significant disagreement about whether tests are becoming flakier due to test infrastructure
    issues, or due to quality issues of the tests themselves. At this point, there is no trustworthy dataset
    that allows us to attribute between those two causes.
* Feedback from the twice annual developer productivity survey supports the above diagnosis,
    and adds some additional nuance.
    Most concerning, although long-tenured Stripe engineers find themselves highly productive in our codebase,
    we increasingly hear in the survey that newly hired engineers with long tenures at other companies
    find themselves unproductive in our codebase.
    Specifically, they find it very difficult to determine how to safely make changes in our codebase.
* Our product codebase is entirely implemented in a single Ruby monolith.
    There is one narrow exception, a Golang service handling payment tokenization,
    which we consider out of scope for two reasons.
    First, it is kept intentionally narrow in order to absorb our SOC1 compliance obligations.
    Second, developers in that environment have not raised concerns about their productivity.

    Our data infrastructure is implemented in Scala. While these developers have concerns--primarily
    slow build times--they manage their build and deployment infrastructure independently, and the group remains relatively small.
* Ruby is not a highly performant programming language, but we've found it sufficiently efficient
    for our needs. Similarly, other languages are more cost-efficient from a compute resources perspective,
    but a significant majority of our spend is on real-time storage and batch computation.
    For these reasons alone, we would not consider replacing Ruby as our core programming language.
* Our Product Infrastructure team is about ten engineers, supporting about 250 product engineers.
    We anticipate this group growing modestly over time, but certainly sublinearly
    to the overall growth of product engineers.
* Developers working in Golang and Scala routinely ask for more centralized support,
    but it's challenging to prioritize those requests as we're forced to consider the return
    on improving the experience for 240 product engineers working in Ruby vs 10 in Golang
    or 40 data engineers in Scala.

    If we introduced more programming languages, this prioritization problem would become
    increasingly difficult, and we are already failing to support additional languages.