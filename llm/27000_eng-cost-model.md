# Eng org seniority-mix model.
url: https://draftingstrategy.com/private-equity-model

One of the trademarks of private equity ownership is the expectation that either the company maintains their current margin
and grows revenue at 25-30%, or they instead grow slower and increase their free cash flow year over year.
In many organizations, engineering costs have a major impact on their free cash flow.
There are many costs to reduce, cloud hosting and such, but inevitably part of the discussion is
addressing engineering headcount costs directly.

One of the largest contributors to engineering headcount costs is your organization's seniority mix:
more senior engineers are paid quite a bit more than earlier career engineers.
This model looks at how various policies impact an organization's seniority mix.

In this chapter, we'll work to:

1. Summarize this model's learnings about policy impact on seniority mix
2. Sketch the model's stocks and flows
3. Use [lethain/systems](https://github.com/lethain/systems) to iteratively build and exercise the full model

Time to start modeling.

## Learnings

An organization without a "backfill at N-1" hiring policy, e.g. an organization that hires a SWE2 to replace a departed SWE2,
will have an increasingly top-heavy organization over time.

**Image Description:** The image is a line graph titled "SWEs Over Time." It displays the number of SWEs (Software Engineers) over a period of time. The x-axis represents time, ranging from 0 to 50, and the y-axis represents the number of SWEs, ranging from 0 to 250.

There are four lines on the graph, each representing a different category:

1. **AtSameLevel SWE1** - A blue line that starts at a low point and remains fairly steady throughout the timeframe.
   
2. **AtSameLevel SWE2** - An orange line that begins slightly higher than the blue line and remains relatively constant.

3. **AtSameLevel SWE3** - A green line that begins similarly to the others, shows slight increases, and stays fairly level.

4. **AtSameLevel SWE4** - A red line that starts at a similar point to the others but shows a strong, consistent upward trend, reaching the highest point among the four lines by the end.

The legend on the graph matches each line to its respective category. This visualization likely compares the growth or stability of different groups of software engineers over time.

<p class="img-desc i tc f6">Ratio of engineers at senior-most level becomes increasingly heavy over time</p>

However, even introducing the "backfill at N-1" hiring policy is insufficient, as our representation
in senior levels will become far too high, even if we stop hiring externally into our senior-most levels.

**Image Description:** The image is a line graph titled "SWEs Over Time." It has the following details:

- **X-axis**: Labeled "Time," showing increments from 0 to 50.
- **Y-axis**: Labeled "# SWEs," ranging from 0 to 100.

The graph contains four lines, each representing different data series:

1. **FlatHeadcount SWE1**: A blue line that starts at 100 SWEs and decreases rapidly before leveling out around 70.
2. **FlatHeadcount SWE2**: An orange line that starts at 100 SWEs, decreases, and then continues to decrease more gradually, stabilizing slightly above 70.
3. **FlatHeadcount SWE3**: A green line that starts at 100 SWEs, sharply decreases to about 60, then stabilizes.
4. **FlatHeadcount SWE4**: A red line starting at 0, which increases steadily, surpassing 60, and leveling off at this value.

A legend in the top-right corner labels the lines with their respective names. The graph shows various trends in the numbers of SWEs over time, with most lines showing a decrease while one shows an increase.

<p class="img-desc i tc f6">Implementing an N-1 backfill policy prevents unbounded increase of rate of senior-most engineers</p>

To fully accomplish our goal of a healthy seniority mix, we must stop hiring at senior-most levels,
implement a "backfill at N-1" policy, and cap the maximum number of individuals at the senior-most level.

**Image Description:** The image is a line graph titled "SWEs Over Time," which shows four data series labeled as CapSWE4 SWE1, SWE2, SWE3, and SWE4. The x-axis represents "Time," while the y-axis represents the number of SWEs.

1. **CapSWE4 SWE1 (Blue Line):**
   - Starts around 100 SWEs and rapidly decreases within the first few time units.
   - Stabilizes and remains constant slightly below 80 SWEs.

2. **CapSWE4 SWE2 (Orange Line):**
   - Begins just below SWE3 and experiences a quick decline.
   - Then stabilizes and remains constant between 80 and 90 SWEs.

3. **CapSWE4 SWE3 (Green Line):**
   - Starts above 90 SWEs, declines very slightly initially.
   - Quickly stabilizes and continues horizontally around 85 SWEs.

4. **CapSWE4 SWE4 (Red Line):**
   - Starts with a sharp increase from below 20 SWEs.
   - Stabilizes quickly and remains constant at a slightly higher level.

Overall, SWE1 shows the most significant initial decline, whereas SWE4 shows a quick rise and stabilization. The graph showcases constant stabilization over time for all four series after initial changes.

<p class="img-desc i tc f6">N-1 backfill policy and capping number of engineers at senior-most level</p>

Any collection of lower-powered policies simply will not impact the model's outcome.

## Sketch

We'll start by sketching this system in [Excalidraw](https://excalidraw.com/).
It's always fine to use whatever tool you prefer, but simpler sketching tools
generally help you focus on iterating the stocks and flows--without getting distracted
by tuning settings--much like a designer starting with messy wireframes rather than pixel-perfect designs.

We'll start with sketching the junior-most level: SWE1.

**Image Description:** The image is a flowchart illustrating a process related to the hiring and promotion of Software Engineers (SWE).

1. **Candidates Box**: On the left, there is a box labeled "Candidates."

2. **Arrows and Connections**:
   - An arrow labeled "Hire" points from "Candidates" to a box labeled "SWE1."
   - Another arrow labeled "Promote" points from "SWE1" to a box labeled "SWE2" below it.
   - An arrow labeled "Depart" points from "SWE1" to a box labeled "Departed SWE1" on the right.
   - An arrow labeled "Backfill" points from "Departed SWE1" back to "SWE1."

3. **Flow Explanation**:
   - Candidates are hired into the position of SWE1.
   - SWE1 employees can be promoted to SWE2.
   - SWE1 employees may depart, leading to a backfilling process to refill the SWE1 position.

Overall, this flowchart outlines the progression and transitions of employees through different stages within a software engineering role.

<p class="img-desc i tc f6">Hiring, departures and promotions for SWE1 engineers</p>

We hire external candidates to become SWE1s. We have some get promoted to SWE2, some depart, and then backfill those
departures with new SWE1s.

**Image Description:** The image is a flowchart illustrating a hiring and promotion process within a software engineering organization. It consists of several labeled boxes connected by arrows, representing different transitions and states.

1. **Candidates**: This box is at the top left and represents potential hires.

2. **SWE1**: To the right of the Candidates box, connected by a "Hire" arrow. It depicts the first level of software engineers.

3. **Departed SWE1**: To the right of the SWE1 box, connected by a "Depart" arrow, indicating when a SWE1 leaves the organization. There is also a "Backfill" arrow coming back from Departed SWE1 to SWE1.

4. **SWE2**: Below the SWE1 box, connected by a "Promote" arrow, representing a level-up from SWE1.

5. **Departed SWE2**: To the right of the SWE2 box, connected by a "Depart" arrow, indicating when a SWE2 leaves the organization.

6. **Backfill Arrows**: There are several arrows labeled "Backfill":
   - From "Backfill at N-1 level" going to Candidates and SWE1.
   - From "Backfill at level" pointing to SWE2.

The flowchart illustrates how candidates are hired into SWE1 or directly into SWE2, how promotion from SWE1 to SWE2 occurs, and how positions are backfilled when someone departs.

<p class="img-desc i tc f6">Hiring and promotion lifecycle for SWE1 and SWE2</p>

As we start sketching the full stocks and flows for SWE2, we also introduce the idea of backfilling
at the prior level. As we replicate this pattern for two more career levels--SWE3 and SWE4--we get the
complete model.

**Image Description:** The image is a flowchart depicting the progression, hiring, promotion, and departure process for software engineers. Here’s a detailed description:

1. **Nodes:**
   - **Candidates**: Entry point for hiring.
   - **SWE1, SWE2, SWE3, SWE4**: Different levels of software engineers.
   - **Departed SWE1, Departed SWE2, Departed SWE3, Departed SWE4**: Represents engineers who have left each level.

2. **Arrows and Labels:**
   - Arrows connect the nodes and are labeled to indicate transitions such as "Hire," "Promote," "Depart," "Backfill," and "Backfill at N-1 level."

3. **Transitions:**
   - **Hiring**: 
     - Candidates can be hired directly into SWE1, SWE2, SWE3, and SWE4.
   
   - **Promotion**: 
     - SWE1 can be promoted to SWE2.
     - SWE2 can be promoted to SWE3.
     - SWE3 can be promoted to SWE4.
   
   - **Departure**:
     - SWE1, SWE2, SWE3, and SWE4 have "Depart" arrows leading to their respective "Departed" nodes.
   
   - **Backfill**: 
     - When an engineer departs from SWE1, the position can be backfilled either at the level or backfilled at N-1 level, indicated by the

<p class="img-desc i tc f6">Hiring and promotion lifecycle for four levels of career ladder</p>

The final level, SWE4, is simplified relative to the prior levels, as it's no longer possible to get promoted to
a further level.
We could go further than this, but the model will simply get increasingly burdensome to work with,
so let's stop with four levels.

## Reason

When reviewing the sketched system, a few interesting conclusions emerge:

1. If promotion rates at any level exceed the rate of hiring at that level plus rate of N-1 backfill at that level,
    then the proportion of engineers at that level will grow over time
2. If you are not hiring much, then this problem simplifies to promotion rate versus departure rate.
    A company that does little hiring and has high retention cannot afford to promote frequently.
    Promotion into senior roles will become financially restrained, even if the policy is explained
    by some other mechanism
3. Many companies use the "[career level](https://lethain.com/career-levels-and-more/)" policy as the mechanism
    to identify a level where promotions _generally_ stop happening. 
    The rationale is often not explicitly described, but we can conclude it's likely a financial constraint
    that typically incentivizes this policy

With those starter insights, now we can get into modeling the details.

## Model & Exercise

We're going to build this model using [lethain/systems](https://github.com/lethain/systems).
The first version will be relatively simple, albeit with a number of stocks given the size
of the model, and then we'll layer on a number of additional features as we iteratively test
out a number of different scenarios.

I've chosen to combine the Model and Exercise steps to showcase how each version of the model
can inspire new learnings that prompt new questions, that require a new model to answer.

If you'd rather view the full model and visualizations, each iteration
is [available on github](https://github.com/lethain/eng-strategy-models/blob/main/BackfillPolicy.ipynb).

## Backfill-at-level

The first policy we're going to explore is backfilling a departure at the same level.
For example, if a SWE2 departs, then you go ahead and backfill them at SWE2. This intuitively
makes sense, because you needed a SWE2 before to perform the work, so why would you hire something
less senior?

There are two new `systems` concepts introduced in this model:

1. For easier iteration, we're going to use the systems modeling concept
    of an "information link", which is basically using a stock as a variable to define a flow,
    Specifically, we'll create a stock named `HiringRate` with a size of two.
    Then we'll use that stock's size to define hiring flows at each career level.
    In programming terms, you can think as defining a reusable variable,
    but you can use any stock's size to define flows.
2. There are effectively an infinite number of potential candidates for your company,
    so we're going to use an infinite stock, represented by initializing a new stock
    surrounded by `[` and `]`. Specifically in this case this is `[Candidates]`,
    if we wanted a fixed size stock with 100 people in it, we could have initialized it as `Candidates(100)`.
    Depending on what you're modeling both options are useful.

With those in mind, our initial model is defined as:

```
HiringRate(2)

[Candidates] > SWE1(10) @ HiringRate
SWE1 > DepartedSWE1 @ Leak(0.1)
DepartedSWE1 > SWE1 @ Leak(0.5)

Candidates > SWE2(10) @ HiringRate
SWE1 > SWE2 @ Leak(0.1)
SWE2 > DepartedSWE2 @ Leak(0.1)
DepartedSWE2 > SWE2 @ Leak(0.5)

Candidates > SWE3(10) @ HiringRate
SWE2 > SWE3 @ Leak(0.1)
SWE3 > DepartedSWE3 @ Leak(0.1)
DepartedSWE3 > SWE3 @ Leak(0.5)

Candidates > SWE4(0)  @ HiringRate
SWE3 > SWE4 @ Leak(0.1)
SWE4 > DepartedSWE4 @ Leak(0.1)
DepartedSWE4 > SWE4 @ Leak(0.5)
```

To confirm that we've done something reasonable, we can model this using Graphviz.

**Image Description:** The image is a flowchart or diagram depicting the relationship between different entities in a hiring or employee management context. It includes several oval-shaped nodes connected by arrows, indicating processes or flows between them. Here's a detailed description:

1. **Nodes (Entities):**
   - **Candidates**: Represents potential hires or applicants.
   - **HiringRate**: Could represent the speed or rate at which candidates are hired.
   - **SWE1, SWE2, SWE3, SWE4**: Likely represent Software Engineers at different levels or stages.
   - **DepartedSWE1, DepartedSWE2, DepartedSWE3, DepartedSWE4**: Represent software engineers who have left, corresponding to each SWE level.

2. **Connections (Arrows):**
   - Arrows flow from **Candidates** to each of the SWE nodes (SWE1, SWE2, SWE3, SWE4) indicating the process of hiring or assigning candidates to those roles.
   - Each SWE node (e.g., SWE1) has an arrow leading to its corresponding **DepartedSWE** node (e.g., DepartedSWE1), indicating the transition or flow of employees who depart from each role.
   - Additional arrows between SWE levels (e.g., from SWE1 to SWE2) could indicate promotions, transitions, or progressions through different levels.
   - The **HiringRate** node is not directly connected to any other node with an

<p class="img-desc i tc f6">GraphViz representation of systems model</p>

That looks like the same model we sketched before, without the downlevel backfill flows
that we haven't yet added to the model, so we're in a good spot.

With that confirmed, let's inspect the four distinct flows happening for the SWE2 stock.
In order they are:

1. External candidates being hired at the SWE2 level, at the fixed `HiringRate`
    defined here as 2 hires per round
2. SWE1s being promoted to SWE2 at a 10% rate. This is a leak because someone being promoted
    to SWE2 doesn't mean the other SWE1s disappear
3. SWE2s who are leaving the company at a 10% rate
4. Backfill hires of departed SWE2s, who are rehired at the same level

Running that model, we can see how the populations of the various levels grow over time.

**Image Description:** The image is a line graph titled "SWEs Over Time." It displays the number of SWEs (Software Engineers) over a period, with the x-axis labeled "Time" and the y-axis labeled "# SWEs."

There are four lines represented in the graph, each corresponding to a different category of SWEs:

1. **AtSameLevel SWE1**: This line is blue and remains relatively flat across the duration, indicating little to no growth.
2. **AtSameLevel SWE2**: This line is orange and shows a slight upward slope initially, then levels off, indicating minimal growth.
3. **AtSameLevel SWE3**: This line is green and shows a modest increase, then levels off, representing moderate growth.
4. **AtSameLevel SWE4**: This line is red and shows a significant upward trend over time, indicating substantial growth.

The red line (SWE4) stands out with the most growth, reaching approximately 250 SWEs by the end, while the others show much slower growth or stabilization. The legend is positioned at the top center inside the plot area.

<p class="img-desc i tc f6">Ratio of engineers at senior-most level becomes increasingly heavy over time</p>

Alright, so we can tell that this backfill at level policy is pretty inefficient, because our organization
just becomes more and more top-heavy with SWE4s over time. Something needs to change.

## Backfill at N-1

To reduce the number of SWE4s in our company, let's update the model to backfill all hires at the level
below the departed employee. For example, a departing SWE2 would cause hiring a SWE1.
This specifically means replacing all these lines:

```
DepartedSWE2 > SWE2 @ Leak(0.5)
```

To instead hire into the prior level.

```
DepartedSWE2 > SWE1 @ Leak(0.5)
```

The one exception is that SWE1s are still backfilled as SWE1s: as it's the junior-most level,
there's no lower level to backfill into.

Running this updated model, we get a better looking organization.

**Image Description:** The image is a line graph titled "SWEs Over Time." It displays four lines, each representing different categories: BackfillIN-1 SWE1, SWE2, SWE3, and SWE4. 

The x-axis is labeled "Time" with values ranging from 0 to 50. The y-axis is labeled "# SWEs" with values from 0 to 100.

- **Blue line**: Represents BackfillIN-1 SWE1. It begins at the lowest point and shows a steady upward trend.
- **Orange line**: Represents BackfillIN-1 SWE2. It starts slightly higher than BLUE and continues upwards at a consistent pace.
- **Green line**: Represents BackfillIN-1 SWE3. It starts near the beginning baseline, closely following the upward trajectory.
- **Red line**: Represents BackfillIN-1 SWE4. It starts above all other lines but ends near the same level as others.

All lines display a generally linear increase, showing that the number of SWEs increases consistently over time. The legend is located at the top of the graph.

<p class="img-desc i tc f6">N-1 backfill policy without overall hiring cap</p>

We're still top-heavy, but we've turned an exponential growth problem into a linear growth problem,
so that's an improvement. However, this is still a very expensive engineering organization to run,
and certainly _not_ an organization that's reducing costs.

## No hiring

One reason our model shows so many SWE4s is because we're hiring at an even rate across all levels,
which isn't particularly realistic. Also, it's unlikely that we're growing headcount at all to the extent
that we're aiming to reduce our engineering costs over time.

We can model this by setting a `HiringRate` of zero, and then setting more representative initial
values for each cohort of engineers (note that I'm only showing the changed lines,
check [on github](https://github.com/lethain/eng-strategy-models/blob/main/BackfillPolicy.ipynb)
for the full model):

```
HiringRate(0)

[Candidates] > SWE1(100) @ HiringRate
Candidates > SWE2(100) @ HiringRate
Candidates > SWE3(100) @ HiringRate
Candidates > SWE4(10)  @ HiringRate
```

Now we're starting out with 100 SWE1s, SWE2, and SWE3s.
We have a smaller cohort of SWE4s, with just ten initially.
Running the model gives us a updated perspective.

**Image Description:** The image is a line graph titled "SWEs Over Time," depicting the number of Software Engineers (SWEs) over a certain period. The x-axis represents "Time," ranging from 0 to 50, while the y-axis shows the "# SWEs" ranging from 0 to 100.

There are four distinct lines, each representing different groups labeled as follows:

1. **FlatHeadcount SWE1** (blue line): This line starts at 100 SWEs, declining sharply initially, and then stabilizing around 70 SWEs from approximately time 10 onwards.

2. **FlatHeadcount SWE2** (orange line): It also begins at 100 SWEs, decreases rapidly at first, then slows down and stabilizes around 80 SWEs from about time 20 onwards.

3. **FlatHeadcount SWE3** (green line): This line starts at 100 SWEs, with a sharp decline, then stabilizes around 60 SWEs from about time 10 onwards.

4. **FlatHeadcount SWE4** (red line): This line initially starts lower, around 10 SWEs, gradually increases over time, and stabilizes around 50 SWEs.

The legend on the right-hand side identifies the lines with their corresponding labels and colors. The graph shows trends in how the headcount of SWEs changes over time for different groups.

<p class="img-desc i tc f6">Implementing an N-1 backfill policy prevents unbounded increase of rate of senior-most engineers</p>

We can see that eliminating hiring _improves_ the ratio of SWE4s to the other levels, but it's still just too
high. We're ending up with roughly 1.25 SWE1s for each SWE4, when the ratio should be closer to five to one.

## Capped size of SWE4s

Finally, we're going to introduce a stock with a maximum size. No matter what flows _want_ to accomplish,
they cannot grow a flow over that maximum. In this case, we're defining `SWE4` as a stock with an initial
size of 10, and a maximum size of 20.

```
SWE4(10, 20)
Candidates > SWE4  @ HiringRate
```

This could also be combined into a one-liner, although it's potentially easy to miss in that case:

```
Candidates > SWE4(10, 20)  @ HiringRate
```

With that one change, we're getting close to an engineering organization that works how we want.

**Image Description:** This image is a line graph titled "SWEs Over Time" that displays the number of SWEs against time. The x-axis represents "Time," ranging from 0 to 50, while the y-axis represents "# SWEs," ranging from 0 to 100. There are four lines on the graph:

1. **Blue Line (CapSWE4 SWE1):** Starts at 100 SWEs and decreases rapidly, leveling off at about 70 SWEs.
2. **Orange Line (CapSWE4 SWE2):** Starts at 100 SWEs, decreases slightly, and stabilizes around 80 SWEs.
3. **Green Line (CapSWE4 SWE3):** Begins at 100 SWEs and quickly stabilizes around 90 SWEs.
4. **Red Line (CapSWE4 SWE4):** Starts at 20 SWEs and remains steady.

A legend on the right identifies the lines by their colors and labels.

<p class="img-desc i tc f6">N-1 backfill policy and capping number of engineers at senior-most level</p>

The ratio of SWE4s to other functions is right, although we can see that the backpressure means that we have
a surplus of SWE3s in this organization. You could imagine other policy work that might improve that as well,
e.g. presumably more SWE3s depart than SWE2s, because the SWE3s see their ability to be promoted is capped by
the departure rate of existing SWE4s. However, I think we've already learned quite a bit from this model,
so I'm going to end modeling here.