# How to resource Engineering-driven projects at Calm? (2020)
url: https://draftingstrategy.com/project-resourcing-strategy

One of the recurring challenges in any organization is how to split your attention
across long-term and short-term problems. Your software might be struggling to scale
with ramping user load while also knowing that you have a series of meaningful security vulnerabilities
that need to be closed sooner than later. How do you balance across them?

These sorts of balance questions occur at every level of an organization.
A particularly frequent format is the debate between Product and Engineering
about how much time goes towards developing new functionality versus improving
what's already been implemented.
In 2020, Calm was growing rapidly as we navigated the COVID-19 pandemic,
and the team was struggling to make improvements, as they felt saturated by incoming new requests.
This strategy for resourcing Engineering-driven projects was our attempt to
solve that problem.

## Reading this document

To apply this strategy, start at the top with _Policy_. To understand the thinking behind this strategy, read sections in reverse order, starting with _Explore_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy & Operation

Our policies for resourcing Engineering-driven projects are:

* We will protect one Eng-driven project per product engineering team, per quarter.
    These projects should represent a maximum of 20% of the team's bandwidth.
    Each project must advance a measurable metric,
    and execution must be designed to show progress on that metric within 4 weeks.
* These projects must adhere to [Calm's existing Engineering strategies](https://draftingstrategy.com/product-eng-strategy/).
* We resource these projects first in the team's planning, rather than last.
    However, only concrete projects are resourced.
    If there are no concrete proposals, then the team won't have time budgeted for Engineering-driven work.
* Team's engineering manager is responsible for deciding on the project,
    ensuring the project is valuable,
    and pushing back on attempts to defund the project.
* Project selection does not require CTO approval, but you should escalate to the CTO if there's friction
    or disagreement.
* CTO will review Engineering-driven projects each quarter
    to summarize their impact and provide feedback to teams' engineering managers
    on project selection and execution.
    They will also review teams that did _not_ perform a project to understand why not.

As we've communicated this strategy, we've frequently gotten conceptual alignment
that this sounds reasonable, coupled with uncertainty about what sort of projects
should actually be selected. At some level, this ambiguity is an acknowledgment
that we believe teams will identify the best opportunities bottoms-up.
However, we also wanted to give two concrete examples of projects we're greenlighting in the
first batch:

* *Code-free media release*: historically, we've needed to make a number of pull requests
    to add, organize, and release new pieces of media. This is high urgency work,
    but Engineering doesn't exercise much judgment while doing it, and
    manual steps often create errors. We aim to track and eliminate these pull requests,
    while also increasing the number of releases that can be facilitated without
    scaling the content release team.
* *Machine-learning content placement*: developing new pieces of media is often a multi-week or month
    process. After content is ready to release, there's generally a debate on where to place the content.
    This matters for the company, as this drives engagement with our users,
    but it matters even more to the content creator, who is generally evaluated in terms of their content's
    performance.

    This often leads to Product and Engineering getting caught up in debates about how to
    surface particular pieces of content. This project aims to improve user engagement
    by surfacing the best content for their interests, while also giving the Content team
    several explicit positions to highlight content without Product and Engineering involvement.

Although these projects are similar, it's not intended that _all_
Engineering-driven projects are of this variety.
Instead it's happenstance based on what the teams view as
their biggest opportunities today.

## Diagnosis

Our assessment of the current situation at Calm is:

* We are spending a high percentage of our time on urgent but low engineering value tasks.
    Most significantly, about one-third of our time is going into launching, debugging,
    and changing content that we release into our product.
    Engineering is involved due to implementation limitations, not because our involvement adds inherent value
    (We mostly just make releases slowly and inadvertently introduce bugs of our own.)
* We have a bunch of fairly clear ideas around improving the platform
    to empower the Content team to speed up releases, and to eliminate the Engineering involvement.
    However, we've struggled to find time to implement them, or to validate that these ideas will work.
* If we don't find a way to prioritize, and succeed at implementing, a project
    to reduce Engineering involvement in Content releases, we will struggle to support
    our goals to release more content and to develop more product functionality this year
* Our Infrastructure team has been able to plan and make these kinds of investments stick.
    However, when we attempt these projects within our Product Engineering teams,
    things don't go that well.
    We are good at getting them onto the initial roadmap, but then
    they get deprioritized due to pressure to complete other projects.
* Our Engineering team of 20 engineers is not very fungible, largely due to
    specialization across roles like iOS, Android, Backend, Frontend, Infrastructure, and QA.
    We would like to staff these kinds of projects onto the Infrastructure team,
    but in practice that team does not have the product development experience to implement
    this kind of project.
* We've discussed spinning up a Platform team, or moving product engineers onto Infrastructure,
    but that would either (1) break our goal to maintain joint pairs between Product Managers and Engineering Managers,
    or (2) be indistinguishable from prioritizing within the existing team because it would still have
    the same Product Manager and Engineering Manager pair.
* Company planning is organic, occurring in many discussions and limited structured process.
    If we make a decision to invest in one project, it's easy for that project to get
    deprioritized in a side discussion missing context on why the project is important.

    These reprioritization discussions happen both in executive forums and in
    team-specific forums. There's imperfect awareness across these two sorts of forums.

## Explore

Prioritization is a deep topic with a wide variety of [popular solutions](https://en.wikipedia.org/wiki/Requirement_prioritization).
For example, many software companies rely on "RICE" scoring, calculating priority as (Reach times Impact times Confidence) divided by Effort.
At the other extreme are complex methodologies like [Scaled Agile Framework](https://en.wikipedia.org/wiki/Scaled_agile_framework).

In addition to generalized planning solutions, many companies carve out special mechanisms
to solve for particular prioritization gaps.
Google historically offered [20% time](https://en.wikipedia.org/wiki/Side_project_time) to allow
individuals to work on experimental projects that didn't align directly with top-down priorities.
Stripe's Foundation Engineering organization developed the concept of Foundational Initiatives
to prioritize cross-pillar projects with long-term implications, 
which otherwise struggled to get prioritized within the team-led planning process.

All these methods have clear examples of succeeding, and equally clear examples of struggling.
Where these initiatives have succeeded, they had an engaged executive sponsoring the practice's rollout,
including triaging escalations when the rollout inconvenienced supporters of the prior method.
Where they lacked a sponsor, or were misaligned with the company's culture, these methods
have consistently failed despite the fact that they've previously succeeded elsewhere.