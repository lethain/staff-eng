# Wardley mapping the LLM ecosystem.
url: https://draftingstrategy.com/wardley-llm-ecosystem

In [How should you adopt LLMs?](https://draftingstrategy.com/llm-adoption-strategy/), we explore how a theoretical ride sharing company,
Theoretical Ride Sharing, should adopt Large Language Models (LLMs).
Part of that strategy's diagnosis depends on understanding the expected evolution of 
the LLM ecosystem, which we've built a [Wardley map](https://draftingstrategy.com/wardley-mapping/) to better explore.

This map of the LLM space focuses on how product companies should address the
proliferation of model providers such as Anthropic, Google and OpenAI,
as well as the proliferation of LLM product patterns like agentic workflows, Retrieval Augmented Generation (RAG),
and running [evals to maintain performance as models change](https://github.com/openai/evals).

---

*This is an exploratory, draft chapter for a book on engineering strategy that I'm brainstorming in [#eng-strategy-book](https://lethain.com/tags/eng-strategy-book/).*
*As such, some of the links go to other draft chapters, both published drafts and very early, unpublished drafts.*

## Reading this document

To quickly understand the analysis within this Wardley Map,
read from top to bottom to understand this analysis.
If you want to understand how this map was _written_, then you should
read section by section from the bottom up, starting with Users, then Value Chains, and so on.

More detail on this structure in [Refining strategy with Wardley Mapping](https://draftingstrategy.com/wardley-mapping/).

## How things work today

If Retrieval Augmented Generation (RAG) was the trending LLM pattern of 2023,
and you could reasonably argue that agents--or agentic workflows--are the pattern of 2024,
then it's hard to guess what the patterns of tomorrow will be, but it's likely
that there are more, new patterns coming our way.
LLMs are a proven platform today, and now are being applied widely to discover new patterns.
It's a safe bet that validating these patterns will continue to drive product companies to support additional
infrastructure components (e.g. search indexes to support RAG).

**Image Description:** The image is a Wardley Map, which visually represents a value chain. The horizontal axis categorizes components from "Genesis" to "Commodity (+utility)," indicating their stage of evolution. The vertical axis represents the value chain from "Invisible" to "Visible."

### Components and Connections:

- **Visible Components:**
  - **Product Engineer:** Connected to several elements, including Machine Learning Infrastructure and Support for agents.
  - **Machine Learning Infrastructure:** Located between Custom and Product (+rental), it connects to many components, playing a central role.
  - **Security & Compliance:** Also between Custom and Product (+rental). 
  - **Access to latest models:** Part of the visible chain, positioned in Product (+rental).
  - **Support for agents:** Centrally located in Product (+rental), connecting to three other components.
  - **Visibility into what is sent to models:** Between Custom and Product (+rental), linked to multiple elements.
  - **LLM vendor contract:** Positioned as a Commodity (+utility) on the right, connected to Visibility into what is sent to models.

- **Less Visible Components:**
  - **Run evals to maintain product quality:** Near Product Engineer and Eval repository, in Custom.
  - **Provide search index to support RAG:** Connects to Support for agents.
  - **API Proxy:** Positioned in Product (+rental), linked with Support for agents and Visibility into what is sent to models.

- **Invisible Components

<p class="img-desc i tc f6">Current state of LLM ecosystem</p>

This proliferation of patterns has created a significant cost for these product companies,
a problem which market forces are likely to address as offerings evolve.

## Transition to future state

Looking at the evolution of the LLM ecosystem, there are two questions
that I believe will define the evolution of the space:

1. Will LLM framework platforms for agents, RAG, and so on, remain bundled with
    model providers such as OpenAI and Anthropic?
    Or will they, instead, split with models and platforms being offered separately?
2. Which elements of LLM frameworks will be productizable in the short-term?
    For example, running evals seems like a straightforward opportunity for bundling,
    as would providing _some_ degree of agent support.
    Conversely, bundling RAG might seem straightforward but most production use cases would
    require real-time updates, incurring the full complexity of operating scaled search clusters.

Depending on the answers to those questions, you might draw a very different map.
This map answers the first question by imagining that LLM platforms will decouple from model providers, while
also allowing you to license with that platform for model access rather than needing
to individually negotiate with each model provider.
It answers the second question by imagining that most non-RAG functionality will move into a bundled
platform provider. Given the richness of investment in the current space, it
seems safe to believe that every plausible combination will exist to some degree
until the ecosystem eventually stabilizes in one dominant configuration.

**Image Description:** The image is a value chain map charting various components and their interconnections within a system focused on machine learning and product engineering.

**Axes:**
- The vertical axis is labeled "Value Chain," ranging from "Invisible" at the bottom to "Visible" at the top.
- The horizontal axis categorizes elements from "Genesis" on the left, to "Custom," and then to "Product (+rental)" on the right.

**Components:**
- **Product Engineer** and **Machine Learning Infrastructure** are positioned towards the top, indicating high visibility and influence.
- **Security & Compliance** and **Access to latest models** are also highly visible.
- Mid-level visibility elements include "Run evals to maintain product quality," "Support for agents," and "Visibility into what is sent to models."
- Lower visibility/custom elements include "Indexing Pipeline" and "Search Index."
- Components like "Platform Bundling," "Agent workflow orchestrator," "Eval runner," "Eval repository," "API Proxy," and "LLM vendor contract" are placed within the "Product (+rental)" section.
  
**Connections:**
- Lines between the components illustrate their interdependence. Product Engineer and Machine Learning Infrastructure connect extensively with other components.
- A dashed arrow points from "Platform Bundling" to a red circle labeled "Bundled LLM platform," highlighting a particular focus or transition in the system.

This diagram visualizes both the development stages and hierarchical visibility of various elements in

<p class="img-desc i tc f6">Pipeline of LLM platform bundling</p>

The key drivers of this configuration are that the LLM ecosystem is investing
new patterns every year, and companies are spinning up haphazard internal solutions
to validate those patterns, but ultimately few product companies are able to effectively fund these
sorts of internal solutions in the long run.

If this map is correct, then it means eventual headwinds faced by both model providers (who are inherently
limited to providing their own subset of models) as well as narrow LLM platform providers (who
can only service a subset of LLM patterns). The likely best bet for a product company in this future
is adopting the broadest LLM pattern platforms today, and to explicitly decouple pattern platform from model provider.

## User & Value Chains

The LLM landscape is evolving rapidly, with some techniques getting introduced and reaching wide-spread adoption
within a single calendar year.
Sometimes those widely adopted techniques are _actually_ being adopted, and other times it's closer to "conference-talk driven development"
where folks with broad platforms inflate the maturity of industry adoption.

The three primary users attempting to navigate that dynamism are:

1. **Product Engineers** are looking for faster, easier solutions to deploying LLMs across
    the many, evolving parameters: new models, support for agents, solutions to offload the search
    dimensions of retrieval-augmented-generation (RAG), and so on.
1. **Machine Learning Infrastructure** team is responsible for the effective usage of the mechanisms,
    and steering product developers towards effective adoption of these tools.
    They are also, in tandem with other infrastructure engineering teams, responsible for supporting
    common elements for LLM solutions, such as search indexes to power RAG implementations.
1. **Security and Compliance** -- how to ensure models are hosted safely and securely,
    and that we're only sending approved information?
    how do we stay in alignment with rapidly evolving AI risks and requirements?

To keep the map focused on evolution rather than organizational dynamics,
I've consolidated a number of teams in slightly artificial ways,
and omitted a few teams that are certainly worth considering.
Finance needs to understand the cost and usage
of LLM usage. Security and Compliance are really different teams, with both overlapping and distinct requirements between them.
Machine Learning Infrastructure could be split into two distinct teams with somewhat conflicting perspectives
on who should own things like search infrastructure.

Depending on what _you_ want to learn from the map, you might prefer to combine, split and introduce
a different set of combinations than I've selected here.