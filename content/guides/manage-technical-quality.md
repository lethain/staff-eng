---
title: Manage technical quality
url: /guides/manage-technical-quality
date: '2020-10-17'
weight: 7000
book_section: Operating at Staff
---

> I feel particularly impactful when I can help improve a proposal that's well-intentioned and solves a real need, but the team that drafted it lacks either experience or context to write a good plan to capture the opportunity. In such cases, having a well-structured plan can help substantially reduce the scope while getting to most of the value, and thus
> demonstrate impact sooner.  
> \- [Dmitry Petrashko](/stories/dmitry-petrashko)

If there's one thing that engineers, engineering managers, and technology executives are likely to agree on, it's that there's a crisis of technical quality. One diagnosis and cure is easy to identify: our engineers aren't prioritizing quality, and we need to hire better engineers or retrain the ones we have. Of course, you should feel free to replace "engineers" with "product managers" or "executives" if that feels more comfortable. It's a compelling narrative with a clear villain, and it conveniently shifts blame away from engineering leadership. Still, like most narratives that move accountability towards the folks with the least power, it's both unhelpful and wrong.

When you accept the premise that low technical quality results from poor decision-making, you start looking for bad judgment, and someone at the company must be the culprit. Is it the previous CTO? Is it that Staff engineer looking at you with a nervous smile? Is it everyone? What if it's none of those folks, and stranger yet isn't even your fault either?

In most cases, low technical quality isn't a crisis; it's the expected, normal state. Engineers generally make reasonable quality decisions when they make them, and successful companies raise their quality bar over time as they scale, pivot, or shift up-market towards enterprise users. At a well-run and successful company, most of your previous technical decisions won't meet your current quality threshold. Rather than a failure, closing the gap between your current and target technical quality is a routine, essential part of effective engineering leadership.


## The problem

As an engineering leadership team, your goal is to maintain an appropriate technical quality level while devoting as much energy as possible towards the core business. You must balance quality across multiple timeframes, and those timeframes generally have conflicting needs. For example, you'll do very different work getting that critical partnership out the door for next week's deadline versus building a platform that supports launching ten times faster next quarter.

Just as your company's technical quality bar will shift over time, your approach to managing technical quality will evolve in tandem:



1. fix the **hot spots** that are causing immediate problems
2. adopt **best practices** that are known to improve quality
3. prioritize **leverage points** that preserve quality as your software changes
4. align **technical vectors** in how your organization changes software
5. **measure technical quality** to guide deeper investment
6. spin up a **technical quality team** to create systems and tools for quality
7. run a **quality program** to measure, track and create accountability

As we dig into this toolkit of approaches, remember to pick the cheapest, most straightforward tool likely to work. Technical quality is a long-term game. There's no such thing as winning, only learning and earning the chance to keep playing.


## Ascending the staircase

There's a particular joy in drilling into the challenge at hand until you find a generalized problem worth solving. However, an equally important instinct is solving the current situation quickly and moving on to the next pressing issue.

As you think about the right quality improvements to make for your team and organization, it's generally most effective to start with the lightest weight solutions and only progress towards massive solutions as earlier efforts collapse under the pressure of scale. If you can't get teams to adopt proper code linting, your attempts to roll out a comprehensive quality program are doomed. Although the latter can be more effective at scale, they're much, much harder to execute.

So, do the quick stuff first!

Even if it doesn't work, you'll learn more and more quickly from failing to roll out the easy stuff than failing to roll out the hard stuff. Then you'll get to an improved second iteration sooner. Over time you will move towards comprehensive approaches, but there's no need to rush. Don't abandon the ease, joy, and innocence of early organizations for the perils of enterprise-scale coordination without proper need.

It's convenient to present these phases as a linear staircase to be ascended, but that's rarely how real organizations use them. You're more likely to fix a quality hot spot, roll out a best practice, start running an architecture review, abolish that architecture review, and go back to hot-spotting for a bit. Premature processes add more friction than value and are quick to expose themselves as ineffective. If something isn't working, try for a bit to make it work, and then celebrate its demise.


## Hot spots

When confronted by a quality problem, the first instinct is often to identify a process failure that necessarily requires a process solution. If a deployment causes an outage, it's because the author didn't correctly follow the code test process, so now we're going to require tests with every commit -- that'll teach those lazy developers!

There's the old joke about Sarbanes-Oxley: it doesn't reduce risk; it just makes it clear who to blame when things go wrong. Unfortunately, that joke applies without humor to how many organizations roll out processes. Accountability has its role, but it's much more important to understand the problem at hand and try to fix it directly than to create process-driven accountability.

Process rollout requires humans to change how they work, which you shouldn't undertake lightly. Rather than reaching for process improvement, start by donning the performance engineer's mindset. Measure the problem at hand, identify where the bulk of the issue occurs, and focus on precisely that area.

The previous example of an untested deploy might benefit from giving direct feedback to the deploying engineer about changing their testing habits. Alternatively, maybe you're better served by acknowledging that your software design is error-prone and adopting the "define errors out of existence" approach described in [A Philosophy of Software Design](https://www.amazon.com/Philosophy-Software-Design-John-Ousterhout/dp/1732102201).

If you have a development velocity problem, it might be optimizing test runtimes, moving your Docker compile step onto a [RAM disk](https://en.wikipedia.org/wiki/RAM_drive), or using the techniques described in [Software Design X-Rays](https://www.amazon.com/Software-Design-X-Rays-Technical-Behavioral-ebook-dp-B07BVRLZ87/dp/B07BVRLZ87/) to find the specific files to improve.

[Systems thinking](https://lethain.com/systems-thinking/) is the most transformative thinking technique I've encountered in my career. Still, at times it can be a siren beckoning you towards fixing a current system you may be better discarding. Sure, you can roll out a new training program to teach your team how to write better tests, but alternatively, maybe you can just delete the one test file where 98% of test failures happen. That's the unreasonable effectiveness of prioritizing hot spots and why it should be the first technique you use to improve technical quality.

At some point, you're likely to find that your organization is creating quality problems faster than you're able to fix hot spots, and that's when it's time to move on to adopting best practices.


## Best practices

I once worked at a company that didn't have a team planning process. Over time the head of engineering was increasingly frustrated with the inability to project target dates and mandated that we use [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)). After the mandate, a manager wrote the Scrum process on a wiki. There was an announcement that we were using Scrum. Managers told their teams to use Scrum. Mission accomplished!

Of course, no one started to use Scrum. Everyone kept doing what they'd done before. It's awkward to acknowledge mistakes, so the head of engineering declared adoption a major win, and no one had the heart to say differently.

This sad tale mirrors how many companies try to roll out best practices, and it's one of the reasons why best practices have such a bad reputation. In theory, organizations would benefit from adopting best practices before fixing quality hot spots, but I recommend practices after hot spotting. Adopting best practices requires a level of organizational and leadership maturity that takes some time to develop.

When you're rolling out a new practice, remember that a [good process is evolved](https://lethain.com/good-process-is-evolved/) rather than mandated. Study how other companies adopt similar practices, document your intended approach, experiment with the practice with a few engaged teams, sand down the rough edges, improve the documentation based on the challenges, and only then roll it out further. A rushed process is a failed process.

Equally important is the idea of limiting concurrent process rollouts. If you try to get teams to adopt multiple new practices simultaneously, you're fighting for their attention with yourself. It also makes it harder to attribute impact later if you're considering reverting or modifying one of the new practices. It's a bit draconian, but I've come to believe that you ought to limit yourself to a single best practice rollout at any given time. Channel all your energy towards making one practice a success rather than splitting resources across a handful.

Adopting a single new practice at a time also forces you to think carefully about which to prioritize. Selecting your next process sounds easy, but it's often unclear which best practices are genuinely best practice and which are just familiar or famous. Genuine best practice has to be supported by research, and the best source of research on this topic is [Accelerate](https://www.amazon.com/dp/B07B9F83WM/).

While all of Accelerate's recommendations are data-driven and quite good, the handful that I've found most helpful to adopt early are version control, trunk-based development, CI/CD, and production observability (including developers on-call for the systems they write), and working in small, atomic changes. There are many other practices I'd love to advocate for (who hasn't spent a career era advocating for [better internal documentation](https://increment.com/documentation/why-investing-in-internal-docs-is-worth-it/)), but I don't trust my intuition like I once did.

The transition from fixing hot spots to adopting best practices comes when you're overwhelmed by too many hot spots to cool. The next transition, from best practices to leverage points, comes when you find yourself wanting to adopt a new best practice before your in-progress best practice is working. Rather than [increasing your best practice adoption-in-progress limit](https://lethain.com/limiting-wip/), move on to the next tool.

## Leverage points

In the Hotspotting section, we talked about using the performance engineer's mindset to identify the right problems to fix. Optimization works well for the issues you already have, but it's intentionally inapplicable to the future: the worst sin of performance engineering is applying effort to unproven problems.

However, as you look at how software changes over time, there are a small handful of places where extra investment preserves quality over time, both by preventing gross quality failures and reducing the cost of future quality investments.

I call those quality leverage points, and the three most impactful points are interfaces, stateful systems, and data models.

_Interfaces_ are contracts between systems. Effective interfaces decouple clients from the encapsulated implementation. Durable interfaces expose all the underlying essential complexity and none of the underlying accidental complexity. Delightful interfaces are [Eagerly discerning, discerningly eager](https://increment.com/apis/api-design-for-eager-discering-developers/).

_State_ is the hardest part of any system to change, and that resistance to change makes _stateful systems_ another critical leverage point.
State gets complex faster than other systems and has an inertia that makes it relatively expensive to improve later.
As you incorporate business obligations around security, privacy, and compliance, changing your stateful systems becomes even more challenging.

_Data models_ are the intersection of the interfaces and state, constraining your stateful system's capabilities down to what your application considers legal. A good data model is rigid: it only exposes what it genuinely supports and prevents invalid states' expression. A good data model is tolerant of evolution over time. Effective data models are not even slightly clever.

As you identify these leverage points in your work, take the extra time to approach them deliberately. If it's an interface, integrate half a dozen clients against the mocked implementation. If it's a data model, represent half a dozen real scenarios. If it's stateful, exercise the failure modes, check the consistency behaviors, and establish performance benchmarks resembling your production scenario.

Take everything you've learned, and pull it into a technical specification document that you socialize across your team. Gather industry feedback from peers. Even after you begin implementation, listen to reality's voice and remain open to changes.

One of the hidden powers of investing in leverage points is that you don't need total organizational alignment to do it. To write a technical vision or roll out a best practice, you need that sort of buy-in, which is why I recommend starting with leverage points. However, if you've exhausted the accessible impact from leverage points, it may be time to move on to driving broader organizational alignment.


## Technical vectors

Effective organizations marshal the majority of their efforts towards a shared vision. If you plot every technical decision as a vector on a grid, the more those vectors point in the same direction, the more you'll accomplish over time. Conversely, some of the most impressive engineers I've worked with created vectors with an extraordinary magnitude but a misaligned direction.
Ultimately those engineers harmed their organizations in their attempts to lead it.

One sure-fire solution to align technical direction is to route all related decisions to the same person with [Architect](https://staffeng.com/guides/staff-archetypes) somewhere in their title. This works well but is challenging to scale, and the quality of an architect's decisions degrade the further they get from doing real work on real code in the real process. On the other extreme, you can allow every team to make independent decisions. But an organization that allows any tool is an organization with uniformly unsupported tooling.

Your fundamental tools for aligning technical vectors are:



* **Give direct feedback.** When folks run into misalignment, the first answer is often process change, but instead, start with simply giving direct feedback to the individuals who you believe are misaligned. As much as they're missing your context, you're missing theirs, and a quick conversation can often prevent years of unnecessary process.
* **Refine your engineering strategy** from [tech spec, to strategy, to vision](/guides/engineering-strategy).
* **Encapsulate your approach in your workflows and tooling.** Documentation of a clear vision is helpful, but some folks simply won't study your document. Deliberate tools create workflows that nurture habits far better than training and documentation. For example, provisioning a new service might require going to a website that requires you to add a link to a technical spec for that service. Another approach might be blocking deploys to production if the service doesn't have an on-call setup established, with someone currently on-call, and that individual must also have their push notifications enabled.
* **Train new team members during their onboarding.** Changing folks' habits after they've formed is quite challenging, which is frustrating if you're attempting to get folks to adopt new practices. However, if you get folks pointed in the right direction when they join, then that habit-momentum will work in favor of remaining aligned.
* **Use _Conway’s Law_.** Conway's Law argues that organizations build software that reflects their structure. If your organization is poorly structured, this will lead to tightly coupled or tangled software. However, it's also a force for quality if your organization's design is an effective one.
* **Curate technology change** using [architecture reviews](https://lethain.com/scaling-consistency/), [investment strategies](https://lethain.com/magnitudes-of-exploration/), and [a structured process for adopting new tools](https://slack.engineering/how-big-technical-changes-happen-at-slack/). Most misalignment comes from missing context, and these are the organizational leverage points to inject context into decision-making. Many organizations start here, but it's the last box of tools that I recommend opening. How can you provide consistent architecture reviews without an articulated vision? Why tell folks your strategy after they've designed something rather than in their onboarding process?

Regardless of the approaches you use to align your technical vectors, this is work that tends to happen over months and years. There's no world where you write the vision document, and the org immediately aligns behind its brilliance. Much more likely is that it gathers dust until you invest in building support.

Most companies can combine the above techniques from hot-spot fixing to vector-alignment into a successful approach for managing technical quality, and hopefully, that's the case for you. However, many find that they're not enough and that you move towards heavier approaches. In that case, the first step is, as always, measurement.


## Measure technical quality

The desire to measure in software engineering has generally outpaced our state of measurement. [Accelerate](https://www.amazon.com/dp/B07B9F83WM/) identifies metrics to measure velocity, which are powerful for locating process and tooling problems, but these metrics start _after_ the code's been merged. How do you measure your codebase's quality such that you can identify gaps, propose a plan of action, and evaluate the impact of your efforts to improve?

There are some process measurements that correlate with effective changes. For example, you could measure the number of files changed in each pull request on the understanding that smaller pull requests are generally higher quality. You could also measure a codebase's lines of code per file, on the assumption that very large files are generally hard to extend. These could both be quite helpful, and I'd even recommend measuring them, but I think they are at best proxy measurements for code quality.

My experience is that it _is_ possible to usefully measure code quality, and it comes down to developing an extremely precise definition of quality. The more detailed you can get your definition of quality, the more useful it becomes to measure a codebase, and the more instructive it becomes to folks hoping to improve the quality of the area they're working on. This approach is described in some detail in [Building Evolutionary Architectures](https://www.amazon.com/Building-Evolutionary-Architectures-Support-Constant/dp/1491986360/) and [Reclaim unreasonable software](https://lethain.com/reclaim-unreasonable-software/).

Some representative components to consider including in your quality definition:



* What percentage of the code is statically typed?
* How many files have associated tests?
* What is test coverage within your codebase?
* How narrow are the public interfaces across modules?
* What percentage of files use the preferred HTTP library?
* Do endpoints respond to requests within 500ms after a cold start?
* How many functions have dangerous read-after-write behavior? Or perform unnecessary reads against the primary database instance?
* How many endpoints perform all state mutation within a single transaction?
* How many functions acquire low-granularity locks?
* How many hot files exist which are changed in more than half of pull requests?

You're welcome to disagree that some of these properties ought to exist in _your_ codebase's definition of quality: your definition should be specific to your codebase and your needs. The important thing is developing a precise, measurable definition. There will be disagreement in the development of that definition, and you will necessarily change the definition over time.

After you've developed the definition, this is an area where instrumentation can be genuinely challenging, and instrumentation is a requirement for useful metrics. Instrumentation complexity is the biggest friction point for adopting these techniques in practice, but if you can push through, you unlock something pretty phenomenal: a real, dynamic quality score that you can track over time and use to create a clarity of alignment in your approach that conceptual alignment cannot.

With quality defined and instrumented, your next step is deciding between investing in a _quality team_ or a _quality program_. A dedicated team is easy to coordinate and predictable in its bandwidth and is generally the easier place to start.


## Technical quality team

A _technical quality team_ is a software engineering team dedicated to creating quality in your codebase. You might call this team Developer Productivity, Developer Tools, or Product Infrastructure. In any case, the team's goal is to create and preserve quality across your company's software.

This is not what's sometimes called a quality assurance team. Although both teams make investments into tests, the technical quality team has a broader remit from workflow to build to test to interface design.

When you're bootstrapping such a team, start with a fixed team size of three to six folks. Having a small team forces you to relentlessly prioritize their roadmap on impact and ensures you'll maintain focus on the achievable. Over time this team will accumulate systems to maintain that require scaling investment, Jenkins clusters are a common example of this, and you'll want to [size the team](https://lethain.com/sizing-engineering-teams/) as a function of the broader engineering organization. Rules of thumb are tricky here, but maybe one engineer working on developer tooling for every fifteen product engineers, in addition to your infrastructure engineering investment.

It's rare for these teams to have a product manager, generally one-or-more Staff-plus engineers, and the engineering manager partner to fill that role. Sometimes they employ a Technical Program Manager, but typically that is after they cross into operating a _Quality program_ as described in the next section.

When spinning up and operating one of these teams, some fundamentals of success are:



1. **Trust metrics over intuition.** You should have a way to measure every project. Quality is a complex system, the sort of place where your intuition can easily deceive you. Similarly, as you become more senior at your company, your experience will no longer reflect most other folks' experiences. You already know about the rough edges, and you'll be the first person in line to get help if you find a new one, but most other folks don't. Metrics keep you honest.
2. **Keep your intuition fresh.** Code and process change over time, and your intuition is going stale every week you're away from building product features. Most folks find that team embedding and team rotations are the best way to keep your instincts relevant. Others monitor chat for problems, as well as a healthy schedule of 1:1 discussions with product developers. The best folks do both of those and keep their metrics dashboards handy.
3. **Listen to and learn from your users.** There is a popular idea of "taste level," which implies that some folks simply know what good looks like. There is a huge variance in folks who design effective quality investments, but it isn't an innate skill. The best folks focus on deeply understanding what their users are trying to accomplish _and_ prioritize user needs over implementation constraints.
    
    Adoption and usability of your tools are much more important than raw power. A powerful tool that's difficult to use will get a few power users, but most folks will pass it by. Slow down to get these details right. Hide all the [accidental complexity](https://en.wikipedia.org/wiki/No_Silver_Bullet). Watch an engineer try to use your tool for their first time without helping them with it. Improve the gaps. Do that ten more times! If you're not doing user research on your tools, then you are _doomed_ as a quality investment team.

4. **Do fewer things, but do them better.** When you're building for the entire engineering organization, anything you do well will accelerate the overall organization. Anything you do poorly, including something almost great with too many rough edges, will drag everyone down. Although it's almost always true that doing the few most important things will contribute more than many mediocre projects, this is even more true in cases where you're trying to roll out tools and workflows to your entire organization (the organizational process-in-progress limits still apply here!).

5. **Don't hoard impact.** There's a fundamental tension between centralized quality teams and the teams that they support. It's often the case that there's a globally optimal approach preferred by the centralized team, which grates heavily on a subset of teams that work on atypical domains or workloads. One representative example is a company writing its backend servers in JavaScript and not allowing their machine learning engineers to use the Python ecosystem because they don't want to support two ecosystems. Another case is a company standardized on using REST/HTTP2/JSON for all APIs where a particular team wants to use gRPC instead. There's no perfect answer here, but it's important to establish a thoughtful approach that [balances the benefits of exploration against the benefits of standardization](http://lethain.com/magnitudes-of-exploration/).

A successful technical quality team using the above approaches will be _unquestionably_ more productive than if the same number of engineers were directly doing product engineering work. Indeed, discounted developer productivity (in the spirit of [discounted cash flow](https://en.wikipedia.org/wiki/Discounted_cash_flow)) is the theoretically correct way to measure such a team's impact. Only theoretically, because such calculations are mostly an evaluation of your self-confidence.

Even if you're quite successful, you'll always have a backlog of high-impact work that you want to take on but don't have the bandwidth to complete. Organizations don't make purely rational team resourcing decisions, and you may find that you lack the bandwidth to complete important projects and likewise can't get approval to hire additional folks onto your team.

It's a good sign when your team has more available high-impact work than you can take on: if you aren't selective about which projects to take on, then you're not thinking broadly enough. This means you shouldn't necessarily try to grow your technical quality team if you have a backlog. However, if you find that there is critical quality work that you can't get to, then it may be time to explore starting a _quality program_.


## Quality program

A _quality program_ isn't computer code at all, but rather an initiative led by a dedicated team to maintain technical quality across an organization. A quality program takes on the broad remit of achieving the organization's target level of software quality. These are relatively uncommon, but something similar you've probably encountered is an incident program responsible for a company's incident retrospectives and remediations.

The technical components of running a quality program are the sorts of things discussed above, so here we'll focus on managing a program effectively. Your first step is to find a technical program manager who can co-lead the program and operate its mechanics. While you can make considerable progress on an organizational program's informational aspects without a technical program manager; however, it's a trap. You'll be crushed by the coordination overhead of solo-driving a program in a large organization.

Operating organizational programs is [a broad topic about which much has been written](https://lethain.com/programs-owning-the-unownable/), but the core approach is:

1. **Identify a program sponsor.** You can't change an organization's behavior without an empowered sponsor. Organizations behave the way they do because it's the optimal solution to their current constraints, and you can't shift those constraints without the advocacy of someone powerful.
2. **Generate sustainable, reproducible metrics.** It's common for folks running a program to spend four-plus hours a week maintaining their dataset by hand. This doesn't work. Your data will have holes in it, you won't be able to integrate your data with automation in later steps, and you'll run out of energy to do the work to effect real change; refreshing a metrics dashboard has no inherent value.
3. **Identify program goals for every impacted team and a clear path for them to accomplish those goals.** Your program has to identify specific goals for each impacted team. For example, reducing test flakiness in their tests or closing incident remediations more quickly. However, it's essential that you provide the map to success! So many programs demand participation from other teams without providing clear directions on how they can accomplish their part. The program owner is the subject matter expert, don't offload your strategy to every team to independently reinvent.
4. **Build the tools and documentation to support teams towards their goals.** Once you've identified a clear path for teams to accomplish your program goals, figure out how you can help them make those changes! This might be providing "golden examples" of what things ought to look like, or an example pull request refactoring a challenging section of code into the new pattern. It might be providing a test script to verify the migration worked correctly. It might be auto-generating the conversion commit to test, verify, and merge without having engineers write it themselves. Do as much as you possibly can to avoid every team having to deeply understand the problem space you're attempting to make progress in.
5. **Create a goal dashboard and share it widely.** Once you have your program goals communicated to each team, provide dashboards that help them understand their current state, their goal state, and that give reinforcing feedback on their (hopeful) progress along the way. The best dashboard is going to be both a scorecard for each team's work and also provide breadcrumbs for each team on where to focus their next efforts.
    
    There are three distinct zoom-levels that your dashboard should support. The fully zoomed-out level helps you evaluate your program's impact. The fully zoomed-in level helps an individual team understand their remaining work. A third level between the two helps organizational leaders hold their teams accountable (and supports your program sponsor in making concrete, specific asks to hold those leaders accountable).
 6. **Send programmatic nudges for folks behind on their goals.** Folks are busy. They won't always prioritize your program's goals. Alternatively, they might do an amazing job of making your requested improvements but backtrack later with deprecated practices. Use nudges to direct the attention of teams towards the next work they should take towards your program's goals. Remember, attention is a scarce resource! If you waste folks' time with a nudge email or ping, they won't pay attention to the next one.
 7. **Periodically review program status with your sponsor.** Programs are trying to make progress on an organizational priority that doesn't naturally align with the teams' goals. Many teams struggle to break from their local prioritization to accomplish global priorities. This is where it's essential to review your overall progress with your sponsor and point them towards the teams that prioritize program work. Effectively leveraging your sponsor to bridge misaligned prioritization will be essential to your success.

In a lot of ways, a program is just an endless migration, and [the techniques that apply to migrations work for programs as well](http://lethain.com/migrations/).

If you get all of those steps right, you're running a genuinely great program. This might feel like a lot of work, and wow, it is: a lot of programs go wrong. The three leading causes of failed programs are:

1. running it purely from a process perspective and becoming detached from the reality of what you're trying to accomplish,
2. running it purely from a technical perspective and thinking that you can skip the essential steps of advocating for your goal and listening to the folks you're trying to motivate,
3. trying to cover both perspectives as a single person--don't go it alone!

A bad program is a lot like an inefficient non-profit: the goal is right, but few funds reach the intended goal. No matter how you decide to measure technical quality, the most important thing to always remember when running your quality program is that the program isn't the goal. The goal is to create technical quality. Organizational programs are massive and build so much momentum that inertia propels them forward long after they've stopped working. Keep your program lean enough to cancel, and remain self-critical enough to cancel if it ceases driving quality creation.


## Start small and add slowly

When you realize your actual technical quality has fallen considerably behind your target technical quality, the natural first reaction is to panic and start rolling out a vast array of techniques and solutions. Dumping all your ingredients into the pot, inevitably, doesn't work well, and worse, you don't even know which parts to keep.

If you find yourself struggling with technical quality--and we all do, frequently--then start with something small, and iterate on it until it works. Then add another technique, and iterate on that too. Slowly build towards something that genuinely works, even if it means weathering accusations of not moving fast enough. When it comes to complex systems and interdependencies, moving quickly is just optics. It's methodical movement that gets the job done.
