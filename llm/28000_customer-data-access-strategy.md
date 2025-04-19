# How should we control access to user data?
url: https://draftingstrategy.com/user-data-strategy

At some point in a startup's lifecycle, they decide that they
need to be ready to go public in 18 months, and a flurry of IPO-readiness
activity kicks off.
This strategy focuses on a company working on IPO readiness,
which has identified a gap in internal controls for managing user data access.
It's a company that _wants_ to meaningfully
improve their security posture around user data access, but which has
had a number of failed security initiatives over the years.

Most of those initiatives have failed because they significantly
degraded internal workflows for teams like customer support,
such that the initial progress was reverted and subverted over time,
to little long-term effect.
This strategy represents the Chief Information Security Officer's (CISO) attempt to acknowledge and overcome those historical
challenges while meeting their IPO readiness obligations, and--most importantly--doing
right by their users.

## Reading this document

To apply this strategy, start at the top with _Policy_. To understand the thinking behind this strategy, read sections in reverse order, starting with _Explore_, then _Diagnose_ and so on.
Relative to the default structure, this document has been refactored in two ways
to improve readability:
first, _Operation_ has been folded into _Policy_;
second, _Refine_ has been embedded in _Diagnose_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy & Operations

Our new policies, and the mechanisms to operate them are:

* **Controls for accessing user data must be significantly stronger prior to our IPO.**
    Senior leadership, legal, compliance and security have decided that we are not comfortable accepting the status quo
    of our user data access controls as a public company.
    We must meaningfully improve the quality of resource-level access controls
    (e.g. how we determine which rows, rather than tables, a user has permission to access)
    as part of our pre-IPO readiness efforts.
    
    Our Security team is accountable for the exact mechanisms and approach to addressing this risk.
* **We will continue to prioritize a hybrid solution to resource-access controls.**
    This has been our approach thus far, and the fastest available option.
* **Directly expose the log of our resource-level accesses to our users.**
    We will build towards a user-accessible log of all company accesses of user data,
    and ensure we are comfortable explaining each and every access.
    In addition, it means that each rationale for access must be comprehensible and reasonable
    from a user perspective.

    This is important because it aligns our approach with our users' perspectives.
    They will be able to evaluate how we access their data, and make decisions about
    continuing to use our product based on whether they agree with our use.
* **Good security discussions don't frame decisions as a compromise between security and usability.**
    We will pursue [multi-dimensional tradeoffs](https://lethain.com/multi-dimensional-tradeoffs/) to simultaneously improve security and efficiency.
    Whenever we frame a discussion on trading off between security and utility,
    it's a sign that we are having the wrong discussion, and that we should rethink our approach.

    We will prioritize mechanisms that can both automatically authorize _and_ document the rationale
    for accesses to customer data. The most obvious example
    of this is automatically granting access to a customer support agent for users who have an open support ticket
    assigned to that agent. (And removing that access when that ticket is reassigned or resolved.)
* **Measure progress on percentage of customer data access requests justified by a user-comprehensible, automated rationale.**
    This will anchor our approach on simultaneously improving the security of user data and the usability of our colleagues' internal tools.
    If we only expand requirements for accessing customer data, we won't view this as progress because it's
    not automated (and consequently is likely to encourage workarounds as teams try to solve problems quickly).
    Similarly, if we only improve usability, charts won't represent this as progress, because we won't
    have increased the number of supported requests.

    As part of this effort, we will create a private channel where the security and compliance
    team has visibility into all manual rationales for user data access, and will
    notify the manager of anyone who repeatedly uses a manual justification
    for accessing user data.
* **Expire unused roles to move towards principle of least privilege.**
    Today we have a number of roles granted in our role-based access control (RBAC) system
    to users who do not use the granted permissions.
    To address that issue, we will automatically remove roles from colleagues after 90 days of not using the role's permissions.
    
    Engineers in an active on-call rotation are the exception to this automated permission pruning.
* **Weekly reviews until we see progress; monthly access reviews in perpetuity.**
    Starting now, there will be a weekly sync between the security engineering team,
    teams working on customer data access initiatives, and the CISO. This meeting will
    focus on rapid iteration and problem solving.

    This is explicitly a forum for ongoing [strategy testing](https://draftingstrategy.com/strategy-testing/),
    with the CISO serving as the meeting's sponsor, and their Principal Security Engineer serving as the
    meeting's guide.
    It will continue until we have clarity
    on the path to 100% coverage of user-comprehensible, automated rationales for access to customer data.

    Separately, we are also starting a monthly review of sampled accesses to customer data to ensure
    the proper usage and function of the rationale-creation mechanisms we build.
    This meeting's goal is to review access rationales for quality and appropriateness,
    both by reviewing sampled rationales in the short-term, and identifying more automated mechanisms
    for identifying high-risk accesses to review in the future.
* **Exceptions must be granted in writing by CISO.**
    While our overarching Engineering Strategy states that we follow
    an advisory architecture process as described in _[Facilitating Software Architecture](https://www.amazon.com/Facilitating-Software-Architecture-Empowering-Architectural-ebook/dp/B0DMHGWCPN/)_,
    the customer data access policy is an exception and must be explicitly approved, with documentation,
    by the CISO. Start that process in the `#ciso` channel.

## Diagnose

* We have a strong baseline of role-based access controls (RBAC) and audit logging.
    However, we have limited mechanisms for ensuring assigned roles follow
    the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).
    This is particularly true in cases where individuals change teams or roles over the course
    of their tenure at the company: some individuals have collected numerous unused roles
    over five-plus years at the company.
    
    Similarly, our audit logs are durable and pervasive, but we have limited proactive mechanisms
    for identifying anomalous usage. Instead they are typically used to understand what occurred after
    an incident is identified by other mechanisms.
* For resource-level access controls, we rely on a hybrid approach between a 3rd-party platform
    for incoming user requests, and approval mechanisms within our own product.
    Providing a rationale for access across these two systems requires manual work,
    and those rationales are later manually reviewed for appropriateness in a batch fashion.
    
    There are two major ongoing problems with our current approach to resource-level access controls.
    First, the teams making requests view them as a burdensome obligation without much benefit to
    them or on behalf of the user.
    Second, because the rationale review steps are manual, there is no verifiable evidence of the quality
    of the review.
* We've found no evidence of misuse of user data.
    When colleagues do access user data, we have uniformly and consistently found that there
    is a clear, and reasonable rationale for that access. For example, a ticket in the user
    support system where the user has raised an issue.
    
    However, the quality of our documented rationales is consistently low because it depends on
    busy people manually copying over significant information many times a day.
    Because the rationales are of low quality, the verification of these rationales is somewhat arbitrary.
    From a literal compliance perspective, we do provide rationales and auditing of these rationales, but
    it's unclear if the majority of these audits increase the security of our users' data.
* Historically, we've made significant security investments that caused temporary spikes in our security posture.
    However, looking at those initiatives a year later, in many cases we see a pattern of increased scrutiny,
    followed by a gradual repeal or avoidance of the new mechanisms.
    
    We have found that most of them involved increased friction for
    essential work performed by other internal teams. In the natural order of performing work, those teams
    would subtly subvert the improvements because it interfered with their immediate goals
    (e.g. supporting customer requests).
* As such, we have high conviction from our track record that our historical approach can
    create optical wins internally. We have limited conviction that it can create long-term
    improvements outside of significant, unlikely internal changes (e.g. colleagues are markedly
    less busy a year from now than they are today).
    It seems likely we need a new approach to meaningfully shift our stance on these kinds of problems.

## Explore

Our experience is that best practices around managing internal access to user data
are [widely available through our networks](https://draftingstrategy.com/explore/),
and otherwise hard to find. The exact rationale for this is hard to determine,
but it seems possible that it's a topic that folks are generally uncomfortable
discussing in public on account of potential future liability and compliance
issues.

In our exploration, we found two standardized dimensions (role-based access controls, audit logs),
and one highly divergent dimension (resource-specific access controls):

* **Role-based access controls** (RBAC) are a highly standardized approach at this point.
    The core premise is that users are mapped to one or more roles, and each role
    is granted a certain set of permissions. For example, a role representing the customer support agent
    might be granted permission to deactivate an account, whereas a role representing the sales engineer might be able
    to configure a new account.
* **Audit logs** are similarly standardized. All access and mutation of resources should be
    tied in a durable log to the human who performed the action. These logs should be
    accumulated in a centralized, queryable solution.

    One of the core challenges is determining how to utilize these logs proactively
    to detect issues rather than reactively when an issue has already been flagged.
* **Resource-level access controls** are significantly less standardized than RBAC
    or audit logs. We found three distinct patterns adopted by companies, with
    little consistency across companies on which is adopted.

Those three patterns for resource-level access control were:

1. **3rd-party enrichment** where access to resources is managed in a 3rd-party system
    such as Zendesk.
    This requires enriching objects within those systems with data and metadata from
    the product(s) where those objects live.
    It also requires implementing actions on the platform, such as archiving or configuration,
    allowing them to live entirely in that platform's permission structure.

    The downside of this approach is tight coupling with the platform vendor,
    any limitations inherent to that platform, and the overhead of maintaining
    engineering teams familiar with both your internal technology stack and the
    platform vendor's technology stack.
2. **1st-party tool implementation** where all activity, including creation and management of user issues,
    is managed within the core product itself. This pattern is most common in earlier stage companies
    or companies whose customer support leadership "grew up" within the organization without much
    exposure to the approach taken by peer companies.
    
    The advantage of this approach is that there is a single, tightly integrated
    and infinitely extensible platform for managing interactions.
    The downside is that you have to build and maintain all of that work internally
    rather than pushing it to a vendor that ought to be able to invest more heavily
    into their tooling.
3. **Hybrid solutions** where a 3rd-party platform is used for most actions,
    and is also used to permit resource-level access within the 1st-party system.
    For example, you might be able to access a user's data only while there is an open
    ticket created by that user, and assigned to you, in the 3rd-party platform.

    The advantage of this approach is that it allows supporting complex workflows
    that don't fit within the platform's limitations, and allows you to avoid complex coupling
    between your product and the vendor platform.

Generally, our experience is that all companies implement RBAC, audit logs, and one of the resource-level access control mechanisms.
Most companies pursue either 3rd-party enrichment with a sizable, long-standing team owning the platform implementation,
or rely on a hybrid solution where they are able to avoid a long-standing dedicated team by lumping that work into existing teams.