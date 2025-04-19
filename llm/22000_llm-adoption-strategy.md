# How should you adopt LLMs?
url: https://draftingstrategy.com/llm-adoption-strategy

Whether you’re a product engineer, a product manager, or an engineering executive, you’ve probably been pushed to consider using Large Language Models (LLMs) to extend your product or enhance your processes. 2023-2024 is an interesting era for LLM adoption, where these capabilities have transitioned into the mainstream, with many companies worrying that they’re falling behind despite the fact that most integrations appear superficial.

That context makes LLM adoption a great topic for a strategy case study. This document is an engineering strategy document determining how a hypothetical company, Theoretical Ride Sharing, could adopt LLMs.

Building out the scenario a bit before diving into the strategy: Theoretical has 2,000 employees, 300 of which are software engineers. They’ve raised $400m, are doing $50m in annual revenue, and are operating in 200 cities across North America and Europe.
They are a ride sharing business, similar to Uber or Lyft. However, they’ve innovated by using larger vehicles—essentially reinventing public transit.

## Reading this document

To apply this strategy, start at the top with _Policy_. To understand the thinking behind this strategy, read sections in reserve order, starting with _Explore_, then _Diagnose_ and so on.
Relative to the default structure, this document has been refactored in two ways
to improve readability:
first, _Operation_ has been folded into _Policy_;
second, _Refine_ has been embedded in _Diagnose_.

More detail on this structure in [Making a readable Engineering Strategy document](https://lethain.com/readable-engineering-strategy-documents).

## Policy

Our combined policy for using LLMs at Theoretical Ride Sharing are:

* **Develop an LLM-backed process for reactivating departed and suspended drivers in mature markets.**
    Through modeling [our driver lifecycle](https://draftingstrategy.com/llm-onboarding-model/), we determined that improving onboarding time
    will have little impact on the total number of active drivers. Instead, we are focusing on mechanisms to reactivate
    departed and suspended drivers, which is the only opportunity to meaningfully impact active drivers.

    Report on progress monthly in _Exec Weekly Meeting_, coordinated in #exec-weekly
* **Start with Anthropic.**
    We use Anthropic models, which are available through our existing cloud provider via [AWS Bedrock](https://aws.amazon.com/bedrock/). To avoid maintaining multiple implementations, where we view the underlying foundational model quality to be somewhat undifferentiated, we are not looking to adopt a broad set of LLMs at this point.
    This is anchored in our [Wardley map of the LLM ecosystem](https://draftingstrategy.com/wardley-llm-ecosystem/).

    Exceptions will be reviewed by the _Machine Learning Review_ in #ml-review
* **Developer experience team (DX) must offer at least one LLM-backed developer productivity tool.**
    This tool should enhance the experience, speed, or quality of writing software in TypeScript. This tool should help us develop our thinking for next year, such that we have conviction increasing (or decreasing!) our investment. This tool should be available to all engineers. Adopting one tool is the required baseline, if DX identifies further interesting tools, e.g. Github Copilot, they are empowered to bring the request to the _Engineering Exec_ team for review. Review will focus on balancing our rate of learning, vendor cost, and data security.
    We've [modeled options for measuring LLMs' impact on developer experience](https://draftingstrategy.com/llm-adoption-model/).

    Vendor approvals to be reviewed in #cto
* **Internal Tools team (INT) must offer at least one LLM-backed ad-hoc prompting tool.**
    This tool should support arbitrary non-engineering use cases for LLMs, such as text extraction, rewriting notes, and so on. It must be usable with customer data while also honoring our existing data processing commitments. This tool should be available to all employees.

    Vendor approvals to be reviewed in #coo
* **Refresh policy in six months.**
    Our primary goal is to quickly learn about this unfamiliar domain where we have limited internal expertise,
    then review whether we should increase our investment afterwards.

    Flag questions and suggestions in #cto

## Diagnose

Here’s a summary of the challenges we face in adopting LLMs at Theoretical Ride Sharing:

1. There are, at minimum, **three distinct needs** that folks internally are asking us to solve (either separately or with a shared solution):
    1. _productivity tools for non-engineers_, e.g. ad-hoc document rewriting, document summarization
    2. _productivity tools for engineers_, e.g. advanced autocomplete tooling like Github Copilot
    3. _product extensions_, e.g. high-quality document extraction in driver onboarding workflows
2. Of the above, **we see product extensions are potential strategic differentiation**, and the other two as workflow optimizations that improve our productivity but don’t necessarily differentiate us from the broader industry. Some of the opportunities for strategic differentiation we see are:
    1. *Reactivating the departed and suspended drivers* is our largest lever to increasing active drivers,
        as explored in our [model of the driver lifecycle](https://draftingstrategy.com/llm-onboarding-model/)
    2. *Faster driver onboarding* with less human involvement will not increase active drivers, but we see a clear opportunity for LLMs to reduce operating
        costs, which may be worthwhile even if it doesn't address the core problem of active drivers
    3. *Improved customer support* by increasing the response speed and quality of our responses to customer inquiries
3. **We currently have limited experience or expertise in using LLMs in the company and in the industry.** Prolific thought leadership to the contrary, there are very few companies or products using LLMs in scaled, differentiated ways. That’s currently true for us as well
4. **We want to develop our expertise without making an irreversible commitment.** We think that our internal expertise is a limiter for effective problem selection and utilization of LLMs, and that developing our expertise will help us become more effective in iterative future decisions on this topic. Conversely, we believe that making a major investment now, prior to developing our in-house expertise, would be relatively high risk and low reward given no other industry players appear to have identified a meaningful advantage at this point
5. **Switching across foundational models and foundational model providers is cheap**. This is true both economically (low financial commitment) and from an integration cost perspective (APIs and usage is largely consistent across providers)
6. **Foundational models and providers are evolving rapidly, and it’s unclear how the space will evolve.** It’s likely that current foundational model providers will train one or two additional generations of foundational models with larger datasets, but at some point they will become cost prohibitive to train (e.g. the next major version of OpenAI or Anthropic models seem likely to cost $500m+ to train). Differentiation might move into developer-experience at that point. Open source models like LLaMa might become significantly cost-advantaged. Or something else entirely. The future is wide open.

    We've built a Wardley map to understand the [possible evolution of the foundational model ecosystem](https://draftingstrategy.com/wardley-llm-ecosystem/).
7. **Training a foundational model is prohibitively expensive for our needs.** We’ve raised $400m, and training a competitive foundational model would cost somewhere between $3m to $100m to match the general models provided by Anthropic or OpenAI

## Explore

Large Language Models operate on top of a foundational model. Training these foundational models is exceptionally expensive, and growing more expensive over time as competition for more sophisticated models accelerates. [Meta allegedly spent $20-30m training LLaMa 2](https://www.cnbc.com/2023/10/16/metas-open-source-approach-to-ai-puzzles-wall-street-techies-love-it.html), up from about $3m training costs for LLaMa 1. OpenAI’s GPT-4 [allegedly cost $100m to train](https://www.wired.com/story/openai-ceo-sam-altman-the-age-of-giant-ai-models-is-already-over/). With some nuance related to the quality of corpus and its relevance to the task at hand, [larger models outperform smaller models](https://arxiv.org/abs/2309.16583), so there’s not much incentive to train a smaller foundational model unless you have a large, unique dataset to train against, and even in that case you might be better off fine-tuning or in-context learning (ICL).

[Anthropic charges](https://www.anthropic.com/api) between $0.25 and $15 per million tokens of input, and a bit more for output tokens. [OpenAI charges](https://openai.com/api/pricing) between $0.50 and $60 per million tokens of input, and a bit more for output tokens. The average English word is about 1.3 tokens, which means you can do a significant amount of LLM work while spending less than most venture funded startups spend on snacks.

There’s [significant debate on whether LLMs have reached a point where their performance improvements will slow](https://garymarcus.substack.com/p/evidence-that-llms-are-reaching-a). Much like the ongoing debate around whether Moore’s Law has died, it’s unclear how much LLM performance will improving going forward. From a cost to train perspective, it’s unlikely that companies can continue to improve foundational models merely by spending more money on compute. Few companies can tolerate a $1B training cost, and fewer will tolerate a $10B training cost, but it’s hard to imagine a world where any companies are building $100B models. However, algorithmic improvements and investment in datasets may well drive improvements without driving up compute costs. The only high confidence prediction you can make in this space is that it’s likely model improvement will double one or two more times over the next 3 years, after which it _might_ continue doubling at that rate or it _might_ plateau at that level of performance: either outcome is plausible.

For some decisions, there’s a strategic imperative to get it right from the beginning. For example, migrating from AWS to Azure is very expensive due to the degree of customization and lock-in. However, LLMs don’t appear to be in this category. Talking with industry peers, the majority of companies are experimenting with a variety of models from Anthropic, OpenAI and elsewhere (e.g. [Mistral](https://mistral.ai/)). Behaviors do vary across models, but it’s also true that behavior of existing models varies over time (e.g. [GPT 3.5 allegedly got “lazier” over time](https://arstechnica.com/information-technology/2023/12/is-chatgpt-becoming-lazier-because-its-december-people-run-tests-to-find-out/)), which means the overhead of dealing with model differences is unavoidable even if you only adopt one.
Vendor lock-in for models is low from a technical perspective.
However, regulatory requirements--like updating Data Processing Agreements--introduce some friction when switching providers.

Although there’s an ongoing investment boom in artificial intelligence, most scaled technology companies are still looking for ways to leverage these capabilities beyond the obvious, widespread practices like adopting [Github Copilot](https://github.com/features/copilot). For example, [Stripe is investing heavily in LLMs for internal productivity](https://podcasts.apple.com/us/podcast/build-ai-products-at-on-ai-companies-with-emily/id1668002688?i=1000644619725), including presumably relying on them to perform some internal tasks that would have previously been performed by an employee such as verifying a company’s website matches details the company supplied in their onboarding application, but it’s less clear that they have yet found an approach to  meaningfully shift their product, or their product’s user experience, using LLMs.

Looking at ridesharing companies more specifically, there don’t appear to be any breakout industry-specific approaches either. Uber is similarly adopting LLMs for internal productivity, and some operational efficiency improvements as documented in their [August, 2023 post describing their internal developer and operations productivity investments using LLMs](https://www.uber.com/blog/the-transformative-power-of-generative-ai/) and [May, 2024 post describing those efforts in more detail](https://www.uber.com/blog/from-predictive-to-generative-ai/).