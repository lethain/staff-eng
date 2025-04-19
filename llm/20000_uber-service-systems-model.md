# Service onboarding model for Uber (2014).
url: https://draftingstrategy.com/uber-strategy-model

At the core of
[Uber's service migration strategy (2014)](https://draftingstrategy.com/uber-strategy/)
is understanding the service onboarding process, and identifying the levers
to speed up that process. Here we'll develop a
[system model](https://draftingstrategy.com/systems-modeling/)
representing that onboarding process, and exercise the model to test a number
of hypotheses about how to best speed up provisioning.

In this chapter, we'll cover:

1. Where the model of service onboarding suggested we focus on efforts
2. Developing a system model using the [lethain/systems](https://github.com/lethain/systems) package on Github.
    That model [is available in the lethain/eng-strategy-models](https://github.com/lethain/eng-strategy-models/blob/main/UberServiceOnboarding.ipynb)
    repository
3. Exercising that model to learn from it

Let's figure out what this model can teach us.

## Learnings

Even if we model this problem with a 100% success rate (e.g. no errors at all),
the backlog of requested new services continues to increase over time.
This clarifies that the problem to be solved is not the service provisioning team's efficiency
in running their current process,
but rather that the fundamental approach is not working.

**Image Description:** The image is a line graph titled "Service Provisioning Pipeline," which tracks the size of stock over several rounds. The x-axis represents "Rounds," ranging from 0 to 100, while the y-axis represents the "Size of Stock," ranging from 0 to 14,000.

The graph includes four lines:

1. **Initial Requested Services (Blue Line):** This line shows a steep upward curve, indicating a significant increase over the rounds. It starts at zero and rises to 14,000 by round 100.
   
2. **Initial Product Engineers (Orange Line):** This line is nearly flat, with a slight upward trend. It starts around 500 and rises just slightly across the rounds.

3. **Initial Inflight Services (Green Line):** This line shows a very slight increase, maintaining a nearly straight line, starting around 400 and increasing slightly.

4. **Initial Server Capacity Allocated (Red Line):** Similar to the green line, this red line is almost flat, starting at about 350 and increasing very slightly by the end of the rounds.

A legend in the upper portion of the graph identifies the lines by color corresponding to their descriptions.

<p class="img-desc i tc f6">Service provisioning model without error states</p>

Although hiring is tempting as a solution, our model suggests it is not a particularly valuable approach in this scenario.
Even increasing the Service Provisioning team's staff allocated to manually provisioning services by 500%
doesn't solve the backlog of incoming requests.

**Image Description:** The image is a line graph titled "Service Provisioning Pipeline." It depicts the growth of stock sizes across different rounds, ranging from 0 to 100 on the x-axis labeled "Rounds" and 0 to 14,000 on the y-axis labeled "Size of Stock."

There are four lines shown in the graph:

1. **Blue Line (Initial RequestedServices)** - This line starts at a low value and increases steeply, reaching above 14,000 by the 100th round.
2. **Orange Line (Initial ServerCapacityAllocated)** - Starting at a slightly higher value than zero, this line rises gradually, reaching just above 2,000 by the 100th round.
3. **Green Line (MoreInfraEng RequestedServices)** - This line starts at a higher value than the initial requested services but follows a similar slope, reaching close to 12,000 by the 100th round.
4. **Red Line (MoreInfraEng ServerCapacityAllocated)** - This line starts close to the same point as the green line and rises steadily, reaching around 4,000 by the 100th round.

The lines represent different aspects of service requests and server capacity allocation, showing how each expands through the rounds. The blue and green lines have the steepest increase, while the orange and red lines show a more moderate growth.

<p class="img-desc i tc f6">Impact of infrastructure engineering hiring on service provisioning</p>

If reducing errors doesn't solve the problem, and increased hiring for the team doesn't solve the problem,
then we have to find a way to eliminate manual service provisioning entirely.
The most promising candidate is moving to a self-service provisioning model,
which our model shows solves the backlog problem effectively.

**Image Description:** The image is a line graph titled "Service Provisioning Pipeline," depicting the size of stock over a series of rounds. The x-axis represents the number of rounds, ranging from 0 to 100, while the y-axis represents the size of stock, ranging from 0 to 14,000.

There are four lines on the graph:

1. **Blue Line (Initial RequestedServices)**: This line starts at a low point and increases steadily, with a steeper incline than the others, reaching the highest point at around 14,000 by round 100.

2. **Orange Line (Initial ServerCapacityAllocated)**: This line also starts low and shows a slight increase, remaining below 2,000 for all rounds. It stays relatively flat compared to the blue and red lines.

3. **Green Line (SelfService RequestedServices)**: Starting similarly to the other lines, it has a very minimal incline and remains under 2,000, indicating little change over the rounds.

4. **Red Line (SelfService ServerCapacityAllocated)**: Beginning at a similar level as the others, it increases steadily but at a lesser rate than the blue line, following a path parallel to it and reaching slightly above 12,000 by round 100.

The graph demonstrates different rates and scales of service requests and capacity allocations over multiple rounds.

<p class="img-desc i tc f6">Impact of self-service provisioning on provisioning rate</p>

Refining our earlier statement, additional hiring may benefit the team if we are able to focus those
hires on building self-service provisioning, and we're able to
[ramp their productivity](https://lethain.com/productivity-in-the-age-of-hypergrowth/)
faster than the increase of incoming service provisioning requests.

## Sketch

Our initial sketch of service provisioning is a simple pipeline starting with
`requested services` and moving step by step through to `server capacity allocated`.
Some of these steps are likely much slower than others, but it gives a sense of the
stages and where things might go wrong. It also gives us a sense of what we can measure
to evaluate if our approach to provisioning is working well.

**Image Description:** The image is a flowchart diagram illustrating a process for provisioning services. Here's a detailed description:

1. **Flow Start:**
   - The process begins with a box labeled "requested services." An arrow points to the right, leading to the next step.

2. **Provisioning Services:**
   - The next box is labeled "in-flight provisioning services." An arrow leads to the right towards the next step labeled "unique port and name assigned."

3. **Configuration Steps:**
   - From "unique port and name assigned," arrows lead to three sequential steps:
     - "Puppet configuration generated"
     - "Puppet configuration tested & merged"
     - "Server capacity allocated to service in Clusto"

4. **Additional Inputs:**
   - On the left side, dotted lines connect two boxes vertically, labeled "product engineers" and "hiring rate," indicating additional influences or inputs to the process.

The flowchart uses simple shapes and lines to convey the progression of tasks and influences within a service provisioning system.

<p class="img-desc i tc f6">Systems model of provisioning services</p>

One element worth mentioning is the dotted lines from `hiring rate` to `product engineers` and
from `product engineers` to `requested services`. These are called _links_, which are stocks that
influence another stock, but don't flow directly into them.

<div class="bg-light-gray br4 ph3 pv1">

A purist would correctly note that links should connect to flows rather than stocks.
That is true! However, as we'll encounter when we convert this sketch into a model,
there are actually several counterintuitive elements here that are necessary to model
this system but make the sketch less readable.
As a modeler, you'll frequently encounter these sorts of tradeoffs,
and you'll have to decide what choices serve your needs best in the moment.

</div>

The biggest missing element the initial model is error flows,
where things can sometimes go wrong in addition to sometimes going right.
There are many ways things can go wrong, but we're going to focus on modeling
three error flows in particular:

1. `Missing/incorrect information` occurs twice in this model, and throws
    a provisioning request back into the initial provisioning phase where information is collected.
    
    When this occurs during port assignment, this is a relatively small trip backwards.
    However, when it occurs in Puppet configuration, this is a significantly larger
    step backwards.
2. `Puppet error` occurs in the second to final stock, `Puppet configuration tested & merged`.
    This sends requests back one step in the provisioning flow.

Updating our sketch to reflect these flows, we get a fairly complete and somewhat nuanced,
view of the service provisioning flow.

**Image Description:** The image is a flowchart illustrating a process with potential issues highlighted. Here's a detailed description:

1. **Processes and Steps**:
   - The flowchart begins with "requested services" at the top.
   - An arrow leads to "in-flight provisioning services."
   - From there, another arrow points to "unique port and name assigned."
   - This continues to "Puppet configuration generated."
   - Then to "Puppet configuration tested & merged."
   - Finally, it leads to "Server capacity allocated to service in Clusto."

2. **Potential Issues**:
   - Between "in-flight provisioning services" and "unique port and name assigned," there is a note indicating "Missing/incorrect info" in red.
   - Between "in-flight provisioning services" and "Puppet configuration generated," there's another note for "Missing/incorrect info."
   - Between "Puppet configuration generated" and "Puppet configuration tested & merged," a red note points out a "Puppet error."

3. **External Factors**:
   - To the left, parallel to the main process, there is a dotted line with "product engineers" and "hiring rate" listed vertically.
  
The flowchart highlights where incorrect or missing information and errors might occur in the provisioning and configuration process.

<p class="img-desc i tc f6">Model of provisioning services with error transitions</p>

Note that the combination of these two flows introduces the possibility of a service
being almost fully provisioned, but then traveling from Puppet testing back to Puppet configuration
due to `Puppet error`, and then backwards again to the initial step due to `Missing/incorrect information`.
This means nearly all provisioning progress can be lost if things go wrong.

There are more nuances we could introduce here, but there's already enough complexity here for us
to learn quite a bit from this model.

## Reason

Studying our sketches, a few things stand out:

1. The hiring of product engineers is going to drive up service provisioning requests
    over time, but there's no counterbalancing hiring of infrastructure engineers to
    work on service provisioning. This means there's an implicit, but very real,
    deadline to scale this process independently of the size of the infrastructure
    engineering team.

    Even without building the full model, it's clear that we have to either stop hiring product engineers,
    turn this into a self-service solution, or find a new mechanism to discourage
    service provisioning.
2. The size of error rates are going to influence results a great deal,
    particularly those for `Missing/incorrect information`.
    This is probably the most valuable place to start looking for efficiency improvements.
3. Missing information errors are more expensive than the model implies,
    because they require coordination across teams to resolve.
    Conversely, Puppet testing errors are probably cheaper than the model
    implies, because they should be solvable within the same team and
    consequently benefit from a quick iteration loop.

Now we need to build a model that helps guide our inquiry into those questions.

## Model

You can find the [full implementation of this model on Github](https://github.com/lethain/eng-strategy-models/blob/main/UberServiceOnboarding.ipynb)
if you want to see the entirety rather than these emphasized snippets.

First, let's get the success states working:

    HiringRate(10)
    ProductEngineers(1000)
    [PotentialHires] > ProductEngineers @ HiringRate

    [PotentialServices] > RequestedServices(10) @ ProductEngineers / 10
    RequestedServices > InflightServices(0, 10) @ Leak(1.0)
    InflightServices > PortNameAssigned @ Leak(1.0)
    PortNameAssigned > PuppetGenerated @ Leak(1.0)
    PuppetGenerated > PuppetConfigMerged @ Leak(1.0)
    PuppetConfigMerged > ServerCapacityAllocated @ Leak(1.0)

As we run this model, we can see that the number of requested services grows significantly over
time. This makes sense, as we're only able to provision a maximum of ten services per round.

**Image Description:** The image is a line graph titled "Service Provisioning Pipeline." 

- **Axes**: 
  - The x-axis is labeled "Rounds" and ranges from 0 to 100.
  - The y-axis is labeled "Size of Stock" and ranges from 0 to 14,000.

- **Legend**: 
  - The graph includes four lines:
    1. **Initial Requested Services (blue line)**: Shows an upward curve, starting near the origin and increasing significantly, reaching around 14,000 by the 100th round.
    2. **Initial Product Engineers (orange line)**: Shows a steady, slight upward trend, starting just below 2,000 and slightly increasing over the rounds.
    3. **Initial Inflight Services (green line)**: Appears relatively flat, starting just above 0 and remaining almost constant throughout the rounds.
    4. **Initial Server Capacity Allocated (red line)**: Shows a slight upward trend, starting below 1,000 and gradually increasing.

The graph illustrates different stock sizes over a series of rounds, with the "Initial Requested Services" increasing dramatically compared to the other categories.

<p class="img-desc i tc f6">Service provisioning model without error states</p>

However, it's also the best case, because we're not capturing the three error states:

1. Unique port and name assignment can fail because of missing or incorrect information
2. Puppet configuration can also fail due to missing or incorrect information.
3. Puppet configurations can have errors in them, requiring rework.

Let's update the model to include these failure modes, starting with unique port and name assignment.
The error-free version looks like this:

    InflightServices > PortNameAssigned @ Leak(1.0)

Now let's add in an error rate, where 20% of requests are missing information
and return to inflight services stock.

    PortNameAssigned > PuppetGenerated @ Leak(0.8)
    PortNameAssigned > RequestedServices @ Leak(0.2)

Then let's do the same thing for puppet configuration errors:

    # original version
    PuppetGenerated > PuppetConfigMerged @ Leak(1.0)

    # updated version with errors
    PuppetGenerated > PuppetConfigMerged @ Leak(0.8)
    PuppetGenerated > InflightServices @ Leak(0.2)

Finally, we'll make a similar change to represent errors
made in the Puppet templates themselves:

    # original version
    PuppetConfigMerged > ServerCapacityAllocated @ Leak(1.0)

    # updated version with errors
    PuppetConfigMerged > ServerCapacityAllocated @ Leak(0.8)
    PuppetConfigMerged > PuppetGenerated @ Leak(0.2)

Even with relatively low error rates, we can see that the throughput of the system
overall has been meaningfully impacted by introducing these errors.

**Image Description:** The image is a line graph titled "Service Provisioning Pipeline". It depicts changes in the "Size of Stock" over "Rounds".

### Axes:
- **X-axis**: Labeled "Rounds", ranging from 0 to 100.
- **Y-axis**: Labeled "Size of Stock", ranging from 0 to 1000.

### Lines:
1. **Blue Line (Initial InflightServices)**: Starts at the origin and remains consistently flat, indicating no change in the size over the rounds.
2. **Orange Line (Initial ServerCapacityAllocated)**: Rises steadily from the origin, showing linear growth.
3. **Green Line (Errors InflightServices)**: Lies flat along the X-axis, indicating consistent zero values.
4. **Red Line (Errors ServerCapacityAllocated)**: Also rises steadily, parallel to the orange line, but starts at slightly lower values.

### Legend:
The legend is located in the top-left corner of the graph, identifying each line by color and description.

Overall, the graph illustrates comparative trends of initial service allocations and error rates across multiple rounds, with capacities increasing over time, while errors remain minimal or unchanged.

<p class="img-desc i tc f6">Service provisioning model with error states</p>

Now that we have the foundation of the model built, it's time to start
exercising the model to understand the problem space a bit better.

## Exercise

We already know the errors are impacting throughput, but let's start by
narrowing down which of errors matter most by increasing the error rate
for each of them independently and comparing the impact.

To model this, we'll create three new specifications, each of which increases
one error from from 20% error rate to 50% error rate, and see how the overall
throughput of the system is affected:

    # test 1: port assignment errors increased
    PortNameAssigned > PuppetGenerated @ Leak(0.5)
    PortNameAssigned > RequestedServices @ Leak(0.5)

    # test 2: puppet generated errors increased
    PuppetGenerated > PuppetConfigMerged @ Leak(0.5)
    PuppetGenerated > InflightServices @ Leak(0.5)

    # test 3: puppet merged errors increased
    PuppetConfigMerged > ServerCapacityAllocated @ Leak(0.5)
    PuppetConfigMerged > PuppetGenerated @ Leak(0.5)

Comparing the impact of increasing the error rates from 20% to 50% in each
of the three error loops, we can get a sense of the model's sensitivity to each error.

**Image Description:** This image is a line graph titled "Impact of Error Rates on Provisioning Pipeline." It visually represents how different error rates affect the size of stock over a series of rounds, specifically from 0 to 100.

### Axes:
- **X-Axis:** Represents the number of rounds, ranging from 0 to 100.
- **Y-Axis:** Represents the size of stock, ranging from 0 to 800.

### Lines:
There are three lines, each representing a different server capacity allocation method:
1. **Blue Line (PortErrors ServerCapacityAllocated):** 
   - Starts at zero and increases steadily, showing a linear growth pattern.
2. **Orange Line (PuppetGenerated ServerCapacityAllocated):** 
   - Starts similarly low and grows rapidly, surpassing the others and reaching approximately 750 at round 100.
3. **Green Line (PuppetMerged ServerCapacityAllocated):** 
   - Begins slightly higher than the blue line and follows a trajectory similar to the orange line but remains slightly lower.

### Legend:
- Located at the top left within the graph, indicating the color association for each method.

Overall, the graph demonstrates different growth rates in server capacity allocation related to error rates, with the orange line indicating the highest growth in stock size over time.

<p class="img-desc i tc f6">Impact of error rates across stages of provisioning</p>

This chart captures why exercising is so impactful: we'd assumed during sketching that
errors in puppet generation would matter the most because they caused a long trip backwards,
but it turns out a very high error rate early in the process matters even more because
there are still multiple other potential errors later on that compound on its increase.

Next we can get a sense of the impact of hiring more people onto the service
provisioning team to manually provision more services, which we can model by
increasing the maximum size of the inflight services stock from `10` to `50`.

    # initial model
    RequestedServices > InflightServices(0, 10) @ Leak(1.0)

    # with 5x capacity!
    RequestedServices > InflightServices(0, 50) @ Leak(1.0)

Unfortunately, we can see that even increasing the team's capacity by 500% doesn't solve the backlog of requested services.

**Image Description:** The image is a line graph titled "Service Provisioning Pipeline." It plots the "Size of Stock" against "Rounds," which are marked on the x-axis ranging from 0 to 100.

There are four lines representing different data sets:

1. **Blue Line (Initial RequestedServices):** It shows a steep upward trajectory, starting from just above zero and reaching above 14,000 by the end of the rounds.

2. **Orange Line (Initial ServerCapacityAllocated):** It rises gradually, starting close to zero and reaching around 3,000 by the end.

3. **Green Line (MoreInfraEng RequestedServices):** This line climbs steadily, starting from just above zero and approaching 12,000 by the end.

4. **Red Line (MoreInfraEng ServerCapacityAllocated):** It starts near zero and rises steadily, reaching over 5,000 by the end.

The legend is located in the upper right, identifying each line by its color and description. The graph shows a comparison between initial and more infrastructure-engineered requests and allocations over multiple rounds.

<p class="img-desc i tc f6">Impact of infrastructure engineering hiring on service provisioning</p>

There's some impact, but that much, and the backlog of requested services remains extremely high.
We can conclude that more infrastructure hiring isn't the solution we need, but let's
see if moving to self-service is a plausible solution.

We can simulate the impact of moving to self-service by removing the maximum size from
inflight services entirely:

    # initial model
    RequestedServices > InflightServices(0, 10) @ Leak(1.0)

    # simulating self-service
    RequestedServices > InflightServices(0) @ Leak(1.0)

We can see this finally solves the backlog.

**Image Description:** The image is a line graph titled "Service Provisioning Pipeline." It displays data over 100 rounds on the x-axis, with the y-axis labeled as "Size of Stock," ranging from 0 to 14,000.

The graph consists of four lines:

1. **Blue Line (Initial RequestedServices):** This line starts at the origin and shows a steep linear increase, reaching around 14,000 by the 100th round.

2. **Orange Line (Initial ServerCapacityAllocated):** This line starts near the origin, showing a gentle linear slope upwards, leveling off around 2,000.

3. **Green Line (SelfService RequestedServices):** This line starts slightly above 0, with a very slight linear increase, reaching just above 1,000.

4. **Red Line (SelfService ServerCapacityAllocated):** This line starts near the origin and shows a consistent increase, reaching approximately 11,000 by the 100th round.

The lines are labeled in a legend at the upper left corner inside the graph, with each line having a distinct color for easy distinction. The blue and red lines show significant growth over the rounds, compared to the orange and green lines, which increase at a much slower rate.

<p class="img-desc i tc f6">Impact of self-service provisioning on provisioning rate</p>

At this point, we've exercised the model a fair amount and have a good sense of what it wants to tell us.
We know which errors matter the most to invest in early, and we also know that we need to make the
move to a self-service platform sometime soon.