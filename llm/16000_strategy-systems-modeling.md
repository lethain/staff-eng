# Using systems modeling to refine strategy.
url: https://draftingstrategy.com/systems-modeling

While I was probably late to learn the concept
of [strategy testing](https://draftingstrategy.com/strategy-testing/),
I might have learned about systems modeling too early in my career,
stumbling on Donella Meadows' _[Thinking in Systems: A Primer](https://www.amazon.com/Thinking-Systems-Donella-H-Meadows-ebook/dp/B005VSRFEA/)_
before I began my career in software.
Over the years, I've discovered a number of ways to misuse systems modeling,
but it remains the most effective, flexible tool I've found to debugging complex problems.

In this chapter, we'll work through:

* a two-minute primer on the basics of systems modeling, along with resources for those looking for a deeper exploration
    of the foundational topics
* when systems modeling is a useful technique, and when it's better to
    rely on other refinement techniques like Wardley mapping or strategy testing instead
* a discussion on systems modeling tooling, why there's no perfect systems modeling tool out there,
    and how I recommend picking the tool that you build proficiency with
* the steps to build a systems model for a problem you're engaging with
* how to document your learnings from a systems model to maximize the
    chance that others will pay attention to it rather than ignoring
    it due to the unfamiliarity or complexity of the tooling
* what systems modeling can't do, even if you really want to believe it can

After working through this chapter's overview of systems modeling,
you can see the approaches implemented in a number of system models created
to refine the strategies throughout this book.
The theory of systems modeling is certainly interesting, but hopefully
seeing real models in support of concrete engineering strategies will
be even more useful.

## Two-minute primer

If you want an exceptional introduction to systems thinking, there's no better place to go than
Donella Meadows' [Thinking in Systems](https://www.amazon.com/dp/1603580557).
If you want a worse, but shorter, introduction, I wrote a short [Introduction to systems thinking](https://lethain.com/systems-thinking/)
available online and in _An Elegant Puzzle_.

If you want something _even shorter_, then here's the briefest that I can manage.

**Image Description:** The image is a flowchart depicting a process for handling requests through a load balancer and server, with possible outcomes for success and failure.

1. **Requests**: The process begins with incoming requests.
2. **Load Balancer**: 
   - If a request is successful, it goes from "Requests" to "Load Balancer" and is marked "OK."
   - If there is an error in the load balancer or DNS resolution fails, the request is directed back to "Requests" for a retry with a "Retry (529 HTTP)" label.
3. **Server**:
   - From the load balancer, the request goes to the "Server" labeled "OK."
   - If there's an error in the server, the request is directed to "Failed Requests."
4. **Successful Requests**: If the server processes the request successfully, it moves to "Successful Requests."
5. **Failed Requests**: Any request failure at the server or load balancer level is ultimately directed to "Failed Requests."

The chart uses purple boxes for each step and gray arrows for error paths. Regular paths are indicated with purple arrows labeled "OK."

<p class="img-desc i tc f6">Requests succeeding and failing between a user, load balancer, and server</p>

Accumulations are called _stocks_. For example, each of the boxes (`Requests`, `Server`, etc)
in the above diagram is a stock. Changes to stocks are called `flows`. Every arrow (`OK`, `Error in server`, etc)
between stocks in the diagram is a a flow.

Systems modeling is the practice of using various configurations of stocks and flows
to understand circumstances that might otherwise have surprising behavior or are too slow
to understand from measurement. 

For example, we can use the above model to explore the tradeoffs between a load balancer that does and does not cap throughput
to a load-sensitive service behind it.

**Image Description:** The image is a line graph titled "SuccessfulRequests," which depicts the number of requests over time. The x-axis represents time, while the y-axis represents the number of successful requests.

There are four lines on the graph:

1. **Unbounded SuccessfulRequests**: A blue horizontal line, indicating a consistent number of successful requests over time.

2. **Unbounded FailedRequests**: An orange line that rises steeply and then levels off, showing an initial increase in failed requests before reaching a plateau.

3. **Bounded SuccessfulRequests**: A green line that rises quickly and then levels off, indicating an initial increase in successful requests which then stabilizes.

4. **Bounded FailedRequests**: A red line with a similar pattern to the green line, rising sharply and then leveling off.

A legend in the upper left corner identifies each line by color and description. The graph illustrates how successful and failed requests evolve over time under bounded and unbounded conditions.

<p class="img-desc i tc f6">Successful and errored requests in two different scenarios</p>

Without a model, you might get into a philosophical debate about how ridiculous it is that the downstream server
is load-sensitive. With the model, it's immediately obvious that it's worthwhile protecting it, even if it certainly
is concerning that it is so sensitive. This is what models do: they create a cheap way to understand reality when
fully understanding reality is cumbersome.

<div class="bg-light-gray br4 ph3 pv1">

**More systems thinking resources**

*[Thinking in Systems: A Primer](https://www.amazon.com/Thinking-Systems-Donella-H-Meadows-ebook/dp/B005VSRFEA/)* by Donella Meadows

*[Business Dynamics: Systems Thinking and Modeling for a Complex World](https://www.amazon.com/Business-Dynamics-Systems-Thinking-Modeling/dp/007238915X)* by John D. Sterman

*[An Introduction to Systems Thinking](https://www.amazon.com/Introduction-Systems-Thinking-Richmond-2004-11-15/dp/B01FGPA45Y/)* by Barry Richmond

</div>

## When is systems modeling useful?

Although [refinement](https://draftingstrategy.com/refine/) is an important step of developing any strategy,
some refinement techniques work better for any given strategy.
Systems modeling is extremely useful in three distinct scenarios:

1. When you're unsure where leverage points might be in a complex system,
    modeling allows you to cheaply test which levers might be meaningful.
    For example, [modeling onboarding drivers in a ride-sharing app](https://draftingstrategy.com/llm-onboarding-model/)
    showed that improving onboarding was less important than reengaging departed drivers.
2. When you have significant data to compare against,
    which allows you to focus in on the places where the real data and your model are in tensions.
    For example, I was able to [model the impact of hiring on Uber's engineering productivity](https://lethain.com/productivity-in-the-age-of-hypergrowth/),
    and then compare that with internal data.
3. When stakeholder disagreements are based in their unstated intuitions,
    models can turns those intuitions into something structured that can be debated more effectively.

In all three categories, modeling makes it possible iterate your thinking much faster than running a live process or technology experiment
with your team. I sometimes hear concerns that modeling slows things down, but this is just an issue of familiarity.
The more you practice, modeling can be faster than asking for advice from industry peers.
The models I've developed for this book took less than an hour. (With one notable exception: [modeling Large Language Models (LLMs) impacts on developer experience](https://draftingstrategy.com/llm-adoption-model/),
which took much longer because I deliberately used an impractical tool to reveal the importance of good tooling).

Additionally, systems modeling will often expose counter-intuitive dimensions to the problem you're working on.
For example, the model I mentioned above on LLMs' impact on developer experience suggests that effective LLMs
might cause us to spend _more_ time writing and testing code (but less fixing issues discovered post-production).
This is a bit unexpected, as you might imagine they'd reduce testing time, but reducing testing time is only valuable
to the extent that issues identified in production remains--at worst--constant; if issues found in production increases,
then reduced testing time does not contribute to increased productivity.

Modeling without praxis creates unsubstantiated conviction.
However, in combination with praxis, I've encountered few other techniques that can similar accelerate learning.

That doesn't mean that it's always the ideal refinement technique.
If you already have conviction on the general approach, and want to refine the narrow details,
then [strategy testing](https://draftingstrategy.com/strategy-testing/) is a better option.
If you're trying to understand the evolution of a wider ecosystem, then you may prefer
Wardley mapping.

## Tooling

For an idea that's quite intuitive, the tools of systems modeling are a real obstacle to wider adoption.
Perhaps a downstream consequence of many early, popular systems modeling tools being quite expensive,
the tooling ecosystems for systems modeling has remained fragmented for some time.
There also appears to be a mix of complex requirements, patent consolidation, and perceived small market size
that's discouraged a modern solution from consolidating the tooling market.

Earlier, I mentioned that system modeling is extremely quick, but that many folks find it a slow, laborious process.
Part of that is an issue of practice, but I suspect that the quality of modeling tooling is at least as big a part of the challenge.
In the [LLMs impact on developer experience model](https://draftingstrategy.com/llm-adoption-model/), I go about the steps of building the model in an increasingly messy spreadsheet.
This was slow, challenging, and extremely brittle. Even after finishing the model, I couldn't extend it effectively to test new ideas,
and I inadvertently introduced a number of bugs into the implementation.

Going in the opposite direction, I explored using a handful of tools, such as [Sagemodeler](https://sagemodeler.concord.org/)
or [InsightMaker](https://insightmaker.com/), which seemed like a potentially simpler toolchain
than the one I typically rely on. There are so many of these introductory toolchains for systems modeling,
but I generally find that they're either constrained in their capabilities, have a fairly high learning curve,
or make it difficult to share your model with others.

In the end, I wound up back at the toolchain that I use,
which happens to be one that I wrote some years ago,[lethain/systems](https://github.com/lethain/systems).
This is far from a perfect toolchain, but I think it's a relatively effective mechanism for demonstrating
systems modeling for a few reasons:

1. quick to create models and iterate on those models
2. easy to share those models with others for inspection and their own exploration
3. relatively low surface area for bugs in your models
4. free, open-source, self-hosted toolchain that integrates well with Jupyter ecosystem
    for diagramming, modeling and so on

You should absolutely pick _any_ tool that feels right to you, and practice with it until you feel confident
quickly modeling scenarios. Afterwards, I wouldn't recommend spending too much time thinking about tools at all:
the most important thing is to build models and learn from them quickly, and almost any tool will be sufficient
to that goal with some deliberate practice.

## How to model

Learning to system model takes some practice, so we'll approach the details of learning to
model from two directions.
First, by documenting a general structure for approaching modeling,
and second by providing breadcrumbs to the models
developed in this book for deeper exploration of particular modeling ideas.

The structure to systems modeling that I find effective is:

1. **Sketch** the stocks and flows on paper or a diagramming application (e.g.
    [Excalidraw](https://excalidraw.com/), Figma, Whimsical, etc).
    Use whatever you're comfortable with.
2. **Reason** about how you would expect a potential change to shift the flows through the diagram.
    Which flows do you expect to go up, and which down, and how would that movement help you
    evaluate whether your strategy is working?
3. **Model** the stocks and flows in your spreadsheet tool of choice.
    Start by modeling the flows from left to right (e.g. the happy path flows). Once you have that fully working,
    then start modeling the right to left flows (e.g. the exception path flows).

    See the [Modeling impact of LLMs on Developer Experience](https://draftingstrategy.com/llm-adoption-model/) model
    for a deep dive into the particulars of creating a model.
4. **Exercise** the model by experimenting with a number of different starting values
    and determining how the rates influence the model's values.
    This is essentially performing [sensitivity analysis](https://www.investopedia.com/terms/s/sensitivityanalysis.asp)
5. **Document** the work done in the above sections into a standalone writeup.
    You can then link to that writeup from strategies that benefit from a given model's insights.
    You might link to any [section of your strategy](https://draftingstrategy.com/strategy-steps/), depending on what
    topic the particular model explores.
    I recommend decoupling models from specific strategies, as _generally_ the details of any given
    model are a distraction from understanding a strategy, and it's best to avoid that distraction unless
    a reader is surprised by the conclusion, in which case, the link out supports drilling into the details.

As always, this is the sequence of steps that I'd encourage you to follow,
and the sequence that I generally follow, but you should adapt them to solve
the particular problems at hand.
Over time, my experience is that most of these steps--excluding documentation--turn into a single
iterative process, and that I document everything after several iterations.

## Breadcrumbs for deeper exploration

Now that we've covered the overarching approach to system modeling,
here are the breadcrumbs to specific models that go deeper on particular elements:

* [Modeling driver onboarding](https://draftingstrategy.com/llm-onboarding-model/)
    explores how the driver lifecycle at Theoretical Ride Sharing might be improved
    with LLMs,
    and introduces using the [lethain/systems](https://github.com/lethain/systems) library
    for modeling
* [Modeling impact of LLMs on Developer Experience](https://draftingstrategy.com/llm-adoption-model/)
    looks at how LLMs might impact developer experience at Theoretical Ride Sharing,
    and demonstrates (the downsides of) modeling with a spreadsheet
* [Modeling engineering backfill strategy](https://draftingstrategy.com/private-equity-model/)
    studies the financial consequences of various policies for how we backfill departed
    engineers in an engineering organization, and introduces further [lethain/systems](https://github.com/lethain/systems) features
* [Modeling service provisioning at Uber](https://draftingstrategy.com/uber-strategy-model/)
    determines whether it's possible to optimize an existing service provisioning
    workflow or if it instead needs to be replaced with a self-service workflow

Beyond these models, you can find other systems models that I've written
on my blog's [systems-thinking category](https://lethain.com/tags/systems-thinking/), and there
are numerous, great examples in the materials references in the systems modeling primer
section above.

## How to document a model

Much like [documenting strategy is challenging](https://draftingstrategy.com/readable-strategy/),
communicating with models in a professional setting is challenging.
The core problems is that there are many distinct groups of model readers.
Some will lack familiarity with the tooling you use to develop models.
Others will try to refine, or invalidate, your model by digging into the details.

I navigate those mismatches by focusing first on the audience who
is least likely to dig into the model. I still want to keep all the details
handy, ideally in the rawest form possible to allow others to manipulate the model
themselves, but it's very much my second goal when documenting a model.

From experience, I recommended this order (it's also the order used in the models
in this book, so you'll see it in practice a number of times):

* start with learning section, with charts showing what model has taught you
* sketch and explaining the stocks and flows
* reason about what the sketch itself teaches you
* explain how you developed the model, with an emphasis on any particularly complex portions
* exercise the model by testing how changing the flows and stocks leads to different outcomes

If you remember nothing else, your document should reflect the reality that
most people don't care how you built the model, and just want the insights.
Give them the insights early, and assume no one will trust your model nearly as much as you do.
Models are an input into the strategy, never a reliable sole backer for a strategy.

## What systems modeling isn't

Although I find systems modeling a uniquely powerful way to accelerate learning,
I've also encountered many practitioners who believe that their models *are* reality
rather than *reflecting* reality.
Over time, I've developed a short list of cautions to help
would-be modelers avoid overcommitting to their model's insights:

1. **When your model and reality conflict, reality is always right.**
    At Stripe, we developed [a model to guide our reliability strategy](https://lethain.com/modeling-reliability/).
    The model was intuitively quite good, but its real-world results were mixed.
    Attachment to our early model distracted us (too much time on collecting and classifying data)
    and we were slow to engage with the most important problems (maximizing impact of scarce mitigation bandwidth, and growing mitigation bandwidth).
    We’d have been more impactful if we engaged directly with what reality was teaching us rather than looking for reasons to disregard reality’s lessons.
2. **Models are immutable, but reality isn’t.**
    I once joined an organization investing tremendous energy into hiring but nonetheless struggling to hire.
    Their intuitive model pushed them to spend years investing into top of funnel optimization,
    and later steered them to improving the closing process.
    What they weren’t able to detect was that [misalignment in interviewer expectations](https://lethain.com/getting-to-yes/) was the largest hurdle in hiring.
3. **Every model omits information; some omit critical information.**
    The service migration at Uber is a great example: modeling clarified that we _had_ to adopt a more aggressive
    approach to our service migration in order to succeed. Subsequently, we did succeed at the migration,
    but the model didn't study the consequences of completing the migration, which were a very challenging development environment.
    The model captured everything my team cared about, as the team responsible for running the migration,
    but did nothing to evaluate whether the migration was a good idea overall.

In each of those situations, two things are true: the model was extremely valuable, and the model subtly led us astray.
We would have been led astray even without a model, so the key thing to remember isn't that models are inherently misleading,
instead the risk is being overly confident about your model. A powerful tool to use in tandem with judgment, not a replacement.

## Summary

Systems modeling isn't perfect.
If you've already determined your strategy and want to refine the details,
then strategy testing is probably a better choice.
If you're trying to understand the dynamics of an evolving ecosystem,
then Wardley mapping is a more appropriate tool.

However, if you have the general shape, but lack conviction on how
the pieces fit together, systems modeling is a remarkable tool.
After this chapter, you know how to select appropriate tooling,
and how to use that tooling to model your problem at hand.
Next, we'll work through systems modeling [a handful of detailed problems](https://lethain.com/tags/systems-thinking/)
to provide concrete examples of applying this technique.