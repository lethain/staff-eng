# Wardley mapping the service orchestration ecosystem (2014).
url: https://draftingstrategy.com/uber-strategy-wardley

In [Uber's 2014 service migration strategy](https://draftingstrategy.com/uber-strategy/),
we explore how to navigate the move from a Python monolith to a services-oriented
architecture while also scaling with user traffic that doubled every six months.

This [Wardley map](https://draftingstrategy.com/wardley-mapping/) explores how orchestration frameworks were evolving
during that period to be used as an input into determining the most effective path forward
for Uber's Infrastructure Engineering team.

## Reading this map

To quickly understand this Wardley Map, read from top to bottom.
If you want to review how this map was _written_, then you should
read section by section from the bottom up, starting with Users, then Value Chains, and so on.

More detail on this structure in [Refining strategy with Wardley Mapping](https://draftingstrategy.com/wardley-mapping/).

## How things work today

There are three primary internal teams involved in service provisioning.
The Service Provisioning Team abstracts applications developed by Product Engineering from servers managed by the Server Operations Team.
As more servers are added to support application scaling, this is invisible to the
applications themselves, freeing Product Engineers to focus on what the company
values the most: developing more application functionality.

**Image Description:** The image is a Wardley Map, which is a visual representation of the value chain within an organization, mapped against the stages of evolution. The map includes various components and their interactions, laid out in a grid format with two main axes:

1. **Vertical Axis (Value Chain):** 
   - Ranges from "Invisible" at the bottom to "Visible" at the top.
   - Represents the visibility of components to the end-user.

2. **Horizontal Axis (Evolution):** 
   - Divided into stages: "Genesis," "Custom," "Product (+rental)," and "Commodity (+utility)."
   - Shows the maturity and evolution of components over time.

**Components and Connections:**
- **Components (represented as nodes):** 
  - **Product Engineer:** Visible and in the Custom stage.
  - **Service Provisioning Team:** Visible and in the Product (+rental) stage.
  - **Server Operations Team:** Visible and in the Commodity (+utility) stage.
  - **Provision New Service, Route Traffic to Service, Add Capacity to Provisioned Service, Add Server Capacity to Cluster:** All located between Product (+rental) and Commodity (+utility).
  - **Service Provision Request Workflow, Cluster Metadata, Request Routing Infrastructure, Server, Server Vendor, Datacenter Contract:** Less visible components located across various evolution stages.

- **Connections (represented as lines):** 
  - Show dependencies and interactions between components, illustrating how each element supports the function

<p class="img-desc i tc f6">Wardley map for service orchestration</p>

The challenges within the current value chain are cost-efficient scaling, reliable deployment,
and fast deployment. All three of those problems anchor on the same underlying problem of
resource scheduling. We want to make a significant investment into improving our resource
scheduling, and believe that understanding the industry's trend for resource scheduling
underpins making an effective choice.

## Transition to future state

Most interesting cluster orchestration problems are anchored in
cluster metadata and resource scheduling.
Request routing, whether through DNS entries or allocated ports, depends on cluster metadata.
Mapping services to a fleet of servers depends on resource scheduling managing cluster metadata.
Deployment and autoscaling both depend on cluster metadata.

**Image Description:** The image is a Wardley Map that visualizes the components of a service provisioning system. Here's a detailed description:

1. **Axes**:
   - The vertical axis represents visibility in the value chain, ranging from "Invisible" at the bottom to "Visible" at the top.
   - The horizontal axis represents the evolution of components, from "Genesis" on the left to "Industrialized" on the right.

2. **Components**:
   - The map includes various components, each represented by circles, with lines connecting related elements.
   - Key visible components include "Product Engineer," "Service Provisioning Team," and "Server Operations Team."
   - Other components like "Service provision request workflow," "Service orchestration pipeline," "Provision new service," and "Add capacity to provisioned service" are connected throughout the map.
   
3. **Technical Components**:
   - Specific technologies mentioned include "Mesos/Aurora On-prem," "Mesos/Aurora (or Kubernetes) in cloud," and "Serverless in cloud."
   - "Puppet & Clusto On-prem" are noted at the bottom, linked to infrastructure orchestration.

4. **Infrastructure Layer**:
   - "Request routing infrastructure," "Server vendor," "Datacenter Contract," and "Add server capacity to cluster" are mentioned as underlying components essential for service delivery.

5. **Flow and Progression**:
   - The map shows the progression from custom solutions to more industrialized, utility

<p class="img-desc i tc f6">Pipeline showing progression of service orchestration over time</p>

This is also an area where we see significant changes occurring in 2014.

Uber initially solved this problem using Clusto, an open-source tool released by Digg
with goals similar to Hashicorp's [Consul](https://www.consul.io/)
but with limited adoption. We also used [Puppet](https://www.puppet.com/) for configuring servers, alongside custom scripting.
This has worked, but has required custom, ongoing support for scheduling.
The key question we're confronted with is whether to build our own scheduling algorithms (e.g. [bin packing](https://en.wikipedia.org/wiki/Bin_packing_problem))
or adopt a different approach.
It seems clear that the industry intends to directly solve this problem via two paths:
relying on Cloud providers for orchestration (Amazon Web Services, Google Cloud Platform, etc)
and through open-source scheduling frameworks such as Mesos and Kubernetes.

Industry peers with more than five years of infrastructure experience are almost unanimously
adopting open-source scheduling frameworks to better support their physical infrastructure.
This will give them a tool to perform a bridged migration from physical infrastructure to cloud infrastructure.

Newer companies with less existing infrastructure are moving directly to the cloud, and avoiding the orchestration problem entirely.
The only companies not adopting one of these two approaches are extraordinarily large and complex
(think Google or Microsoft) or allergic to making any technical change at all.

From this analysis, it's clear that continuing our reliance on Clusto and Puppet is going to
be an expensive investment that's not particularly aligned with the industry's evolution.

## User & Value Chains

This map focuses on the orchestration ecosystem within a single company,
with a focus on what did, and did not, stay the same from roughly
2008 to 2014. It focuses in particular on three users:

1. **Product Engineers** are focused on provisioning new services,
    and then deploying new versions of that service as they make changes.
    They are wholly focused on their own service, and entirely unaware of anything beneath the orchestration layer
    (including any servers).
2. **Service Provisioning Team**
    focuses on provisioning new services, orchestrating resources for those services,
    and routing traffic to those services.
    This team acts as the bridge between the Product Engineers and the Server Operations Team.
3. **Server Operations Team** is focused on adding server capacity to be used for orchestration.
    They work closely with the Service Provisioning Team, and have no contact with the Product Engineers.

It's worth acknowledging that, in practice, these are artificial aggregates of multiple underlying teams.
For example, routing traffic between services and servers is typically handled by a Traffic or Service Networking team.
However, these omissions are intended to clarify the distinctions relevant to the evolution of orchestration tooling.