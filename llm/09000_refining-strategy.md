# Refining
url: https://draftingstrategy.com/refine

In Jim Collins' _[Great by Choice](https://www.amazon.com/Great-Choice-Uncertainty-Thrive-Despite/dp/1847940889/)_,
he develops the concept of [Fire Bullets, Then Cannonballs](https://www.jimcollins.com/concepts/fire-bullets-then-cannonballs.html).
His premise is that you should cheaply test new ideas before fully committing to them.
Your organization can only afford firing a small number of cannonballs, but it can bankroll far more bullets.
Why not use bullets to derisk your cannonballs' trajectories?

This chapter presents a series of concrete techniques that I have personally
used to effectively refine strategies before reaching the cannonball stage.
We'll work through:

* An introduction to the practice of strategy refinement
* Why strategy refinement is the highest impact step of strategy creation
* How mixed incentives often cause refinement to be skipped, even though
    skipping leads to worse organizational outcomes
* Building your personal toolkit for refining strategy by picking from various
    refinement techniques like [strategy testing](https://draftingstrategy.com/strategy-testing/),
    [systems modeling](https://draftingstrategy.com/systems-modeling/),
    and [Wardley mapping](https://draftingstrategy.com/wardley-mapping/)
* Brief introductions to each of those refinement techniques. These provide enough context
    to pick which ones might be useful for the strategy that you're working on
* Survey of anti-patterns that skip refinement or manufacture consent to create the illusion
    of refinement without providing the benefits

Each of the refinement techniques, such as systems modeling, is covered in greater
detail--including concrete applications to specific engineering strategies--in the
refinement section of this book.

## What is strategy refinement?

Most strategies succeed because they properly address narrow problems within a broader strategy.
While fully implementing a strategy to validate it is possible, this approach is typically inefficient and slow.
Worse, it's easy to get so distracted by miscellaneous details that you lose sight
of the levers that will make your strategy impactful.

Strategy refinement is a toolkit of methods to identify those narrow problems that matter most,
and validate that your solutions to those problems will be effective.
The right tool within the toolkit will vary depending on the strategy you're working on.
It might be using Wardley mapping to understand how the ecosystem's evolution will impact your approach.
Or it might be systems modeling to determine which part of a migration is the most valuable lever.
In other cases, it's slowing down committing to your strategy until you've done a narrow test drive
to derisk the pieces you don't quite have conviction in yet.

Whatever tools you've relied on to refine strategy thus far in your work, there
are always new refinement tools to pick up. This book presents a workable introduction to several tools that I find reliably useful,
while providing a broader foundation for deploying other techniques that you
develop towards strategy refinement.

## Does refinement matter?

At Stripe, the head of engineering rolled out agile techniques in one meeting.
This change was aimed at our difficulties with planning in periods longer than a month,
which was becoming an increasing challenge as we started working with enterprise businesses who
wanted us to commit to specific functionality as part of signing their contracts.
On the other hand, the approach worked poorly, because it assumed that the issue was engineering managers
being generally unfamiliar with agile techniques.
The challenge of adoption wasn't awareness, but rather the difficulty of prioritizing asks from  numerous stakeholders
in an environment where saying no was frowned upon.

In this agile rollout, the lack of a shared planning paradigm was a real, apt problem.
However, the solution solved the easiest part of the problem, without addressing the
messier parts, and consequently failed to make meaningful progress.
This happens a surprising amount, and can be largely avoided with a small dose of refinement.

On the opposite end, we created Uber's service adoption strategy exclusively through refinement,
because the infrastructure engineering team didn't have any authority to mandate wider changes.
Instead, we relied on two different kinds of refinement to focus our iterative efforts.
First, we used systems modeling to understand what parts of adoption we needed to focus on.
Second, we used strategy testing to learn by migrating individual product engineering teams
over to the new platform.

In the agile adoption example, failure to refine turned a moderately challenging problem
into a strategy failure.
In the service migration example, focus on refinement translated an extremely difficult problem
into a success.
Refinement is, in my experience, the kernel of effective strategy.

## If it matters, why is it skipped?

When a small team creates a strategy,
a so-called [low-altitude strategies](https://draftingstrategy.com/when-write-stratefy/),
they almost always spend a great deal of time refining their strategy.
This isn't because most teams believe in refinement.
Rather it's because most teams lack the authority to force others to align with their strategy.
This lack of authority means they must incrementally prove out their approach until other teams or executives believe it's worth aligning with.

High-altitude strategy is typically the domain of executives, who generally have the ability to mandate adoption,
and routinely skip the refinement stage, even when it's inexpensive and is almost guaranteed to make them more successful.
Why is that?
When [executives start a new role](https://lethain.com/first-ninety-days-cto-vpe/), they know making an early impression matters.
They also, unfortunately, know that sounding ambitious often resonates more loudly
than doing good work. So, while they do hope to eventually be effective, early on they kick off
a few aspirational initiatives [like a massive overhaul of the codebase](https://lethain.com/grand-migration/),
believing it'll establish their reputation as an effective leader at the company.

This isn't uniquely an executive failure, it also happens frequently in
[permissive strategy organizations](https://draftingstrategy.com/when-write-stratefy/)
that require [an ambitious, high-leverage project to get promoted into senior engineering roles](https://staffeng.com/guides/staff-projects/).
For example, you might see a novel approach to networking or authorization implemented in a company, whose adoption fails after solving some easier proof points,
and trace its heritage back to promotion criteria.
In many cases, the promotion will come before the rollout stalls out, disincentivizing the would-be promoted engineer
from worrying too deeply about whether this was net-positive for the organization.
The executive responsible for the promotion rubric will eventually recognize the flaw,
but it's not the easiest tradeoff for them to pick between an organization that innovates too much while empowering individuals
or an organization with little waste but restricted room for creativity.

Another reason refinement can get skipped is that sometimes you're forced to urgently create and commit to a strategy,
usually because your boss tells you to. This doesn't actually prevent refinement--just say you're committed and refine anyway--but
often this interaction turns off the strategist's mind, tricking them into intellectually thinking
they can't change their approach because they've already committed to it.
This is never true, all decisions are up for review with proper evidence,
but it takes a certain courage to refine when those around you are asking
for weekly updates on completing the project.

There's one other important reason that strategy refinement gets skipped:
many people haven't built out a toolkit to perform strategy refinement,
and haven't worked with someone who has a toolkit.

## Building your toolkit

I'm eternally grateful to my father, a professor of economics,
who brought me to a systems modeling workshop in Boston one summer
when I was in high school. This opened my eyes to the wide world of
techniques for reasoning about problems, and systems modeling became
the first tool in my toolkit for strategy refinement.

The section on refinement will go into three refinement techniques in significant detail:
[strategy testing](https://draftingstrategy.com/strategy-testing/), 
[systems modeling](https://draftingstrategy.com/systems-modeling/), and
[Wardley mapping](https://draftingstrategy.com/wardley-mapping/),
as well as surveying a handful of other techniques more common to strategy consultants.
Systems modeling I adopted early, whereas Wardley mapping I only learned while
working on this book.
Few individuals are proficient users of many refinement tools, but it's extraordinarily
powerful to unlock your first tool, and worthwhile to slowly expand your experience
with other tools over time. All tools are flawed, and each is best at illuminating
certain types of problems.

If all of these are unfamiliar, then skim over all of them and pick one that seems
most applicable to a current problem you're working on.
You'll build expertise by trying a tool against many different problems,
and talking through the results with engaged peers.

As you practice, remember that the important thing to share is the learning
from these techniques, and try to avoid getting too caught up in sharing the techniques themselves.
I've seen these techniques meaningfully change strategies,
but I've never seen those changes successfully justified through
the inherent insight of the refinement techniques themselves.

## Strategy testing

Sometimes you'll need a strategy to solve an ambiguous problem,
or a problem where diagnosing the issues blocking progress are poorly understood.
At Carta, one strategy problem we worked on was improving code quality,
which is a good example of both of those. It's difficult to agree on
what code quality is, and it's equally difficult to agree on appropriate,
concrete steps to improve it.

To navigate that ambiguity, we spent relatively little time thinking
about the right initial solution, and a great deal of our time
deploying the [strategy testing](https://draftingstrategy.com/strategy-testing/) technique:

1. Identify the narrowest, deepest available slice of your strategy.
    Iterate on applying that slice until you see some evidence it's working.
2. As you iterate, identify metrics that help you verify the approach is working.
3. Operate from the belief that people are well-meaning,
    and strategy failures are due to excess friction and poor ergonomics.
4. Keep refining until you have conviction that your strategy’s details work in practice,
    or that the strategy needs to be approached from a new direction.

In this case, we achieved some small wins, funded a handful of specific bets that we believed would improve
the problem long-term, and ended the initiative early without making a large organizational commitment.
You could argue that's a failure, but my experience is quite different: having a problem doesn't mean you
have an elegant solution, and strategy testing helps you validate if the solution's efficiency and ergonomics
are viable.

If you're dealing with a deeply ambiguous problem and there's no agreement on
the nature of the reality you're operating in, strategy testing is a great technique to start with.

## Systems modeling

When you're unsure where leverage points might be in a complex system,
[systems modeling](https://draftingstrategy.com/systems-modeling/)
is an effective technique to cheaply determine which levers might be
effective. For example, the systems model for [onboarding drivers in a ride-share app](https://draftingstrategy.com/llm-onboarding-model/)
shows that reengaging drivers who've left the platform matters more than bringing on new drivers
in a mature market.

Similarly, in the Uber service migration example,
systems modeling helped us focus on eliminating upfront steps during service
onboarding, shifting to reasonable defaults and away from forcing teams
to learn the new service platform before it had shown any usefulness to them.

**Image Description:** The image is a flowchart illustrating the process of handling requests through a load balancer and a server, leading to either successful or failed requests.

1. **Requests**: The process starts with requests being made, represented by a purple box labeled "Requests."

2. **Load Balancer**: Requests pass through a "Load Balancer" if the conditions are okay ("OK"). The process moves from the "Requests" box to the "Load Balancer" box with a purple arrow labeled "OK".

3. **Server**: Once the load balancer processes the request successfully, it is sent to the "Server," again indicated by a purple arrow with "OK."

4. **Successful Requests**: If the server processes the request successfully, it leads to "Successful Requests," shown with a purple arrow leading to the corresponding box.

5. **Failed Requests**: Errors can occur in both the load balancer and the server:
   - If there is an "Error in server," a grey arrow leads the process to "Failed Requests."
   - An "Error in load balancer" also directs the flow to "Failed Requests."

6. **Retry Mechanism**: If a request receives a 529 HTTP status, indicating server overload, there is a retry mechanism. This is shown by a grey arrow looping from "Load Balancer" to "Requests" with "Retry (529 HTTP)."

7. **DNS Resolution Failure**: There is a pathway for when "DNS

<p class="img-desc i tc f6">Systems model of errors in a load balancer</p>

While you can certainly reach these insights without modeling, modeling tends to make
the insights immediately visible.
In cases where your model doesn't immediately illuminate what matters most,
studying how your model's projections conflict with real-world data will guide you
to understand where your assumptions are contorting your understanding of the problem.

If you generally understand a problem, but need to determine where to focus
efforts to make the largest impact, then systems modeling is a valuable technique
to deploy.

## Wardley mapping

Many engineering strategies implicitly make the assumption that the ecosystem we're operating
within is static. However, that's certainly false. Many experienced engineers and engineering leaders
have great judgment, and great intuition, but nonetheless deploy a flawed strategy because they've
anchored on their memory of how things work rather than noticing how things have changed over time.

If, rather than being hit over the head by them, you
want to incorporate these changes into your strategy,
[Wardley mapping](https://draftingstrategy.com/wardley-mapping/) is a great tool to add to your kit.

Wardley maps allow you to plot users, their needs, and then study how
the solutions to those needs will shift over time.
For example, today there is a proliferation of narrow platforms built on
recent advances in large language models, but [studying a Wardley map of the LLM ecosystem](https://draftingstrategy.com/wardley-llm-ecosystem/)
suggests that it's likely that this ecosystem will consolidate to fewer, broader platforms
rather than remaining so widely scattered across distinct vendors.

**Image Description:** The image is a value chain map with the following features:

**Axes:**
- **Vertical Axis (Value Chain):** Ranges from "Invisible" at the bottom to "Visible" at the top.
- **Horizontal Axis (Genesis to Commodity):** Divided into sections: Genesis, Custom, Product (+rental), and Commodity (+utility).

**Nodes and Components:**
- The map includes various nodes representing components and activities involved in the process, such as:
  - **Product Engineer**
  - **Machine Learning Infrastructure**
  - **Security & Compliance**
  - **Run evals to maintain product quality**
  - **Support for agents**
  - **Visibility into what is sent to models**
  - **Provide search index to support RAG**
  - **Access to latest models**

- Some nodes have connections to others, indicating relationships and dependencies.

**Components in Different Sections:**
- **Genesis:** Includes components like "Eval repository," "Eval runner," and "Indexing Pipeline."
- **Custom:** Features components like "Provide search index to support RAG" and "Search Index."
- **Product (+rental):** Includes "Access to latest models" and "Visibility into what is sent to models."
- **Commodity (+utility):** Contains "LLM vendor contract."

**Connections:**
- Various lines connect these nodes, illustrating workflows or dependencies between components.

This map provides a visual representation of the processes and relationships in a product development or business context

<p class="img-desc i tc f6">Wardley map of Large Language Model ecosystem</p>

If your strategy involves adopting a highly dynamic technology
such as observability in the 2010s, or if your strategy is intended
to span five-plus years, then Wardley mapping will help
surface how industry evolution will impact your approach.

## Anti-patterns in refinement

We've already discussed why **refinement is often skipped**, which is
the most frequent and most damning refinement anti-pattern.
At Calm, we cargo-culted adoption of decomposing our monolithic codebase
into microservices; we had no reason to believe this was improving developer productivity,
but we continued to pursue this strategy for a year before recognizing that we were suffering
from skipping refinement.

The second most common anti-pattern is creating the impression of strategy refinement
through **manufactured consent**. A new senior leader joined Uber and mandated a complete technical re-achitecture,
justifying this in part through the evidence that a number of internal leaders had adopted the same techniques
successfully on their teams. Speaking with those internal leaders, they themselves were skeptical that the
proposal made sense, despite the fact that their surface-level agreement was being used to convince the wider
organization that they believed in the new approach.

Finally, refinement often occurs, but counter-evidence is discarded because the refining team
is **optimizing for a side-goal** of some sort.
My first team at Yahoo adopted Erlang for a key component of [Yahoo! Build Your Own Search Service](https://lethain.com/datahub/),
which proved to be an excellent solution to our problem of wanting to use Erlang,
but a questionable solution to the core problem at hand.
Only three of the engineers on our fifteen person team were willing to touch the Erlang codebase,
but that counter-evidence was ignored because it was in conflict with the side-goal.

## Summary

This chapter has introduced the concept of strategy refinement, surveyed three common
refinement techniques--strategy testing, systems modeling, and Wardley mapping--and provided
a framework for building your personal toolkit for refinement.
When you're ready to get into more detail,
further in the book there's a section dedicated to the details of applying
these techniques, starting with [strategy testing](https://draftingstrategy.com/strategy-testing/).