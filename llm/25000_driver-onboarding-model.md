# Modeling driving onboarding.
url: https://draftingstrategy.com/llm-onboarding-model

The [How should you adopt LLMs?](https://draftingstrategy.com/llm-adoption-strategy/) strategy explores how Theoretical Ride Sharing
might adopt LLMs. It builds on several models, the first is about [LLMs impact on Developer Experience](https://draftingstrategy.com/llm-adoption-model/).
The second model, documented here, looks at whether LLMs might improve a core product and business problem: maximizing
active drivers on their ridesharing platform.

In this chapter, we'll cover:

1. Where the model of ridesharing drivers identifies opportunities for LLMs
2. How the model was sketched and developed using [lethain/systems](https://github.com/lethain/systems) package on Github
3. Exercising this model to learn from it

Let's get started.

## Learnings

An obvious assumption is making driver onboarding faster would increase the long-term number
of drivers in a market. However, this model shows that even doubling the rate that we qualify applicant drivers
as eligible has little impact on active drivers over time.

**Image Description:** The image is a line graph titled "ActiveDrivers Over Time." It compares two datasets: "Base" and "FastOnboarding," represented by blue and orange lines, respectively. 

### Axes:
- **X-Axis (Time):** Ranges from 0 to 250.
- **Y-Axis (# ActiveDrivers):** Ranges from 0 to 1400.

### Data Trends:
- Both lines start at similar low values around the beginning of the time period.
- The orange "FastOnboarding" line rises slightly quicker than the blue "Base" line, indicating a faster increase in active drivers.
- Both lines peak around the same time, with a maximum of approximately 1400 active drivers.
- After the peak, both lines decline at similar rates, gradually leveling off towards the end of the timeline.

### Legend:
- Located in the upper-right corner.
- Identifies the blue line as "Base" and the orange line as "FastOnboarding."

The graph illustrates the impact of different onboarding strategies on the number of active drivers over time, showing initial rapid growth followed by a decline to stability.

<p class="img-desc i tc f6">Speeding up onboarding doesn't impact active drivers in the long-term</p>

Conversely, it's clear that efforts to reengage departed drivers has a significant impact
on active drivers. We believe that there are potential LLM applications that could encourage
departed drivers to return to active driving, for example mapping their rationale for departing
against our recent product changes and driver retention promotions could generate high quality,
personalized emails.

**Image Description:** The image is a line graph titled "ActiveDrivers Over Time." It displays two lines representing different data sets over a period. The x-axis is labeled "Time," and the y-axis is labeled "# ActiveDrivers."

1. **Data Sets:**
   - **Base (Blue Line):** Starts at the origin, gradually increases until around time 110, where it peaks just above 1200 active drivers. It then declines and stabilizes around 800 active drivers by time 250.
   - **LLM_Reengage (Orange Line):** Also starts at the origin but rises more sharply than the blue line, reaching a peak of about 1600 active drivers. It begins to decline just past time 75, and levels off around 950 active drivers by time 250.

2. **Comparison:**
   - The orange line generally shows higher active driver counts than the blue line throughout the period.
   - The peaks for both lines occur at different times, with the orange line peaking earlier.

3. **Legend:** Located in the top right corner, identifying the blue line as "Base" and the orange line as "LLM_Reengage."

Overall, the graph compares the number of active drivers over time between a base model and a reengagement model, with the reengagement model showing higher engagement.

<p class="img-desc i tc f6">Improving driver reengagement does increase active drivers</p>

Finally, the model shows that increasing either reactivation of departed or suspended drivers is significantly
less impactful than increasing both. If either rate is low, we lose an increasingly large number of drivers over time.

**Image Description:** The image is a line graph titled "ActiveDrivers Over Time." It displays the number of active drivers on the y-axis and time on the x-axis. The graph compares three lines representing different scenarios:

1. **Base** (Blue Line): Starts at 0, gradually rises to almost 1000, peaks around time 80, and then slowly decreases and levels off.

2. **LLM_Reengage** (Orange Line): Starts near 0, increases to about 1500, peaks around time 80, and then declines, stabilizing above the Base line.

3. **LLM_Unsuspend** (Green Line): Begins near 0, rises steeply to over 2000, peaking around time 50, and then gradually decreases, leveling off well above the other two lines.

The legend in the top right indicates the color corresponding to each line. The curves show different rates and durations for the increase and stabilization of active drivers over time.

<p class="img-desc i tc f6">Increasing reactivation rate of suspend drivers has highest impact</p>

The only meaningful opportunities for us to increase active drivers with LLMs are improving those two reactivation rates.

## Sketch

The first step in modeling a system is sketching it (using [Excalidraw](https://excalidraw.com/) here).
Here we're developing a model for onboarding and retaining drivers for a ridesharing application in one city.

**Image Description:** The image is a flowchart depicting the process of transitioning drivers from the general population to active drivers, with paths for re-engagement and suspension. 

1. **City Population**:
   - This is the starting point from which "Applied Drivers" emerge.

2. **Applied Drivers**:
   - Arrows go from "City Population" to "Applied Drivers."
   - If there is missing information, drivers are sent back to this stage as indicated by the "Request missing Information" arrow.

3. **Eligible Drivers**:
   - Arrows lead from "Applied Drivers" to "Eligible Drivers."

4. **Onboarded Drivers**:
   - Eligible drivers move to "Onboarded Drivers."

5. **Active Drivers**:
   - Onboarded drivers then become "Active Drivers."
   - Arrows also lead away to and from this stage to other parts of the process.

6. **Departed Drivers**:
   - "Active Drivers" can become "Departed Drivers."
   - There is a "Re-engage" arrow back to "Active Drivers."

7. **Suspended Drivers**:
   - "Active Drivers" can become "Suspended Drivers."
   - There is a "Remove suspension" arrow that leads back to "Active Drivers."

The flowchart neatly outlines the progression and potential changes in status for drivers in the network.

<p class="img-desc i tc f6">Sketch of onboarding drivers onto a ride-sharing application</p>

The stocks are:

1. `City Population` is the total population of a city
2. `Applied Drivers` are the number of people who've applied to be drivers
3. `Eligible Drivers` are the number of applied drivers who meet eligibility criteria (e.g. provided a current drivers license, etc)
4. `Onboarded Drivers` are eligible drivers who have successfully gone through an onboarding program
5. `Active Drivers` are onboarded drivers who are actually performing trips on a weekly basis
6. `Departed Drivers` were active drivers, but voluntarily stopped performing trips (e.g. took a different job)
7. `Suspended Drivers` were active drivers, but involuntarily stopped performing trips (e.g. are no longer allowed to drive on platform)

Looking at the left-to-right flows, there is a flow from each of those stocks to the following stock in the pipeline.
These are all simple one-to-one flows, with the exception of those coming from
`Active Drivers` leads to two distinct stocks: `Departed Drivers` and `Suspended Drivers`.
These represent voluntary and involuntary departures.

There are a handful of right-to-left, exception path flows to consider as well:

1. `Request missing information` represents a driver who can't be moved from `Applied Drivers` to `Eligible Drivers`
    because their provided information proved insufficient in a review process
2. `Re-engage` tracks `Departed Drivers` who have decided to start driving again, perhaps
    because of a bonus program for drivers who start driving again
3. `Remove suspension` refers to drivers who were involuntarily removed, but who are now
    allowed to return to driving

This is a fairly basic model, but let's see what we can learn from it.

## Reason

Now that we've sketched the system, we can start thinking about which flows are going to have the largest impact,
and where an LLM might increase those flows. Some observations from reasoning about it:

1. If a city's population is infinite, then what really matters in this model
    is how many new drivers we can encourage to join the system.
    On the other hand, if a city's population is finite,
    then onboarding new drivers will be essential in the early stages of coming
    online in any particular city, but long-term reengaging departed drivers
    is probably at least as important.
2. LLMs tooling could speed up validating eligible drivers. If we speed that process up enough,
    we could greatly reduce the rate of the `Request missing information` flow by identifying
    missing information in real-time rather than requiring a human to review the information later.
3. We could potentially develop LLM tooling to craft personalized messaging to `Departed Drivers`,
    that explains which of our changes since their departure might be most relevant to their reasons
    for stopping. This could increase the rate of the `Re-engage` flow
4. While we likely wouldn't want an LLM approving the removal of suspensions, we could have it look
    at requests to be revalidated, and identify promising requests to focus human attention on
    the highest potential for approval.
5. We could build LLM-powered tooling that helps a city resident decide whether they should apply
    to become a driver by answering questions they might have.

As we exercise the model later, we know that our assumptions about whether this city has already exhausted
potential drivers will quickly steer us towards a specific subset of these potential options.
If all potential drivers are already tapped, only work to reactivate prior drivers that will matter.
If there are more potential drivers, then likely activating them will be a better focus.

## Model

For this model, we'll be modeling it using the [lethain/systems](https://github.com/lethain/systems) library that I wrote.
For a more detailed introduction, I recommend working through [the tutorial in the repository](https://github.com/lethain/systems/blob/master/README.md),
but I'll introduce the basics here as well.
While `systems` is far from a perfect tool, as you experiment with different modeling techniques
like [spreadsheet-based modeling](https://draftingstrategy.com/llm-adoption-model/) and [SageModeler](https://sagemodeler.concord.org/),
I think this approach's emphasis on rapid development and reproducible, sharable models is somewhat unique.

If you want to see the finished model,
you can find the model and visualizations in [the Jupyterhub notebook in lethain:eng-strategy-models](https://github.com/lethain/eng-strategy-models/blob/main/DriverOnboarding.ipynb).
Here we'll work through the steps behind implementing that model.

We'll start by creating a stock for the city's population,
with an initial size of 10,000.

```
# City population is 10,000
CityPop(10000)
```

Next, we want to initialize the applied drivers stock,
and specify a constant rate of 100 people in the city applying
to become drivers each round. This will only happen until
the 10,000 potential drivers in the city are exhausted,
at which point there will be no one left to apply.

```
# 100 folks apply to become drivers per round
# the @ 100 format is called a "rate" flow
CityPop > AppliedDrivers @ 100
```

Now we want to initialize the eligible drivers stock,
and specify that 25% of the folks in applied drivers
will advance to become eligible each round.

Before we used `@ 100` to specify a fixed rate.
Here we're using `@ Leak(0.25)` to specify the idea
of 25% of the folks in applied drivers advancing into eligible driver.

```
# 25% of applied drivers become eligible each round
AppliedDrivers > EligibleDrivers @ Leak(0.25)
```
You could write this as `@ 0.25`, but you'd actually get different behavior,
That's because `@ 0.25` is actually short-hand for `@ Conversion(0.25)`,
which is similar to a leak but destroys the unconverted portion.

Using an example to show the difference, let's imagine that
we have 100 applied drivers and 100 eligible drivers, and then
see the consequences of applying a leak versus a conversion:

* `Leak(0.25)` would end with 75 applied drivers and 125 eligible drivers
* `Conversion(0.25)` would end with 0 applied drivers and 125 eligible drivers

Depending on what you are modeling, you might need leaks, conversions or both.

Moving on, next we model out first right-to-left flow.
Specifically, the request missing information flow where some eligible drivers end up
not being eligible because they need to provide more information.

```
# This is "Request missing information", with 10%
# of folks moving backwards each round
EligibleDrivers > AppliedDrivers @ Leak(0.1)
```

Note that the syntax for left-to-right and right-to-left flows
is identical, without making a distinction.

Now, 25% of eligible drivers become onboarded drivers each round.

```
# 25% of eligible drivers onboard each round
EligibleDrivers > OnboardedDrivers @ Leak(0.25)
```

Then 50% of onboarded drivers become active drivers,
actually providing rides.

```
# 50% of onboarded drivers become active
OnboardedDrivers > ActiveDrivers @ Leak(0.50)
```

The active drivers stock is drained by two flows:
drivers who voluntarily depart become departed drivers,
and drivers who are suspended become suspended drivers.
Both flows take 10% of active drivers each round.

```
# 10% of active drivers depart voluntarily and involuntarily
ActiveDrivers > DepartedDrivers @ Leak(0.10)
ActiveDrivers > SuspendedDrivers @ Leak(0.10)
```

Finally, we also see 5% of departed drivers returning to driving
each round. Similarly, we unsuspend 1% of suspended drivers.

```
# 5% of DepartedDrivers become active
DepartedDrivers > ActiveDrivers @ Leak(0.05)
# 1% of SuspendedDrivers are reactivated
SuspendedDrivers > ActiveDrivers @ Leak(0.01)
```

We already sketched this model out earlier, but it's worth noting
that `systems` will allow you to export models via [Graphviz](https://graphviz.org/).
These diagrams are generally harder to read than a custom drawn one,
but it's certainly possible to use this toolchain to combine sketching
and modeling into a single step.

**Image Description:** The image is a flowchart diagram representing a process involving drivers. Here's a detailed description:

1. **CityPop** (Oval): The starting point, labeled "CityPop."

2. **AppliedDrivers** (Oval): Linked from "CityPop" with an arrow pointing to it, indicating the flow from city population to applied drivers.

3. **EligibleDrivers** (Oval): An arrow goes from "AppliedDrivers" to "EligibleDrivers," showing the process of selecting eligible drivers. An additional arrow loops back from "EligibleDrivers" to "AppliedDrivers," indicating a feedback or reapplication process.

4. **OnboardedDrivers** (Oval): Connected to "EligibleDrivers" with an arrow, representing the onboarding of eligible drivers.

5. **ActiveDrivers** (Oval): Linked from "OnboardedDrivers" with an arrow pointing to it, signifying the activation of onboarded drivers.

6. **DepartedDrivers** (Oval): "ActiveDrivers" has an arrow pointing to "DepartedDrivers," showing the transition from active to departed drivers.

7. **SuspendedDrivers** (Oval): Another arrow from "ActiveDrivers" points to "SuspendedDrivers," indicating a path where active drivers can become suspended.

Overall, the diagram outlines a sequence from city population, application, eligibility, onboarding, activation, and then diverges into either departure or suspension of drivers.

<p class="img-desc i tc f6">GraphViz representation of systems model</p>

Now that we have the model, we can get to exercise it to learn its secrets.

## Exercise

Our base model acquires initial drivers quickly, then slows as city population is exhausted.

**Image Description:** The image is a line graph titled "ActiveDrivers Over Time." It represents the number of active drivers on the y-axis, labeled "# ActiveDrivers," against time on the x-axis, labeled "Time." 

Key observations from the graph:

- The number of active drivers starts at around 0 and begins to increase rapidly.
- There is a steep incline, with the number of active drivers reaching a peak of about 1,400 around the x-axis value of 90.
- After the peak, the number of active drivers declines sharply.
- Eventually, the decline slows and stabilizes, leveling off to a steady value just above 600.
- The line follows an S-shape, with an initial rapid growth, a peak, and then a gradual decline and stabilization.

<p class="img-desc i tc f6">Base onboarding model stabilizing around 800 active drivers</p>

Now let's imagine that our LLM-powered tool can speed up eligible drivers, doubling the speed that we move
applied drivers to eligible drivers. Instead of 25% of applied drivers becoming eligible each round,
we'll instead see 50%.

```
# old
AppliedDrivers > EligibleDrivers @ Leak(0.25)

# new
AppliedDrivers > EligibleDrivers @ Leak(0.50)
```

Unfortunately, we can see that even doubling the speed at which we're onboarding drivers to eligible
has a minimal impact.

**Image Description:** The image is a line graph titled "ActiveDrivers Over Time." It shows two lines representing the number of active drivers over a timeline, comparing two scenarios: "Base" and "FastOnboarding."

- **Axes**: 
  - The x-axis is labeled "Time" and appears to display a range from 0 to 250.
  - The y-axis is labeled "# ActiveDrivers" and spans from 0 to 1400.

- **Lines**:
  - The "Base" scenario is depicted with a blue line.
  - The "FastOnboarding" scenario is shown with an orange line.

- **Trends**:
  - Both lines start close to zero at the beginning of the timeline.
  - They both rise steadily, with the "FastOnboarding" line climbing slightly faster than the "Base."
  - Both lines peak just above 1300 active drivers.
  - After the peak, both lines decline before leveling out at around 800 active drivers.

- **Legend**: The legend on the top right differentiates the scenarios, marking the blue line as "Base" and the orange line as "FastOnboarding." 

Overall, the graph illustrates how the number of active drivers changes over time under two different conditions, with "FastOnboarding" initially increasing faster than "Base" but converging over time.

<p class="img-desc i tc f6">Speeding up onboarding doesn't impact active drivers in the long-term</p>

To finish testing this hypothesis, we can eliminate the `Request missing information` flow entirely
and see if this changes things meaningfully, commenting out that line.

**Image Description:** The image is a line graph titled "ActiveDrivers Over Time." It presents data comparing the number of active drivers over a period labeled as "Time." The vertical axis represents the number of active drivers, ranging from 0 to 1400.

Three lines are depicted on the graph:

1. **Base (Blue line):** It starts low, rises steeply to around 1300 active drivers, and then declines before stabilizing.
   
2. **FastOnboarding (Orange line):** Similar to the blue line, it starts low, rises sharply to near 1300, and then declines slightly before stabilizing. It runs slightly above the blue line during the initial growth phase.

3. **NoMissingInfo (Green line):** Follows a path similar to the other two lines, reaching a peak around the same level as the others and stabilizing thereafter. It overlaps with the other lines.

The legend in the top right identifies each line with its corresponding label. The graph indicates a growth, peak, and subsequent decline in the number of active drivers over time for each scenario, eventually stabilizing around 1000 drivers.

<p class="img-desc i tc f6">Eliminating request missing information error doesn't impact active drivers long-term</p>

Unfortunately, even eliminating the missing information rate has little impact on the number of active drivers.
So it seems like the opportunity for our LLM solutions to increase active drivers are going to need to focus
on reactivating existing drivers.

Specifically, let's go from 5% of departed drivers reactivating to 20%.

```
# 20% of DepartedDrivers become active
# DepartedDrivers > ActiveDrivers @ Leak(0.05)
# DepartedDrivers > ActiveDrivers @ Leak(0.2)
```

For the first time, we're seeing a significant shift in impact.
We reach a much higher percentage of drivers at peak, and even after we
exhaust all drivers in a city, the total number of active reaches a higher
equilibrium.

**Image Description:** The image is a line graph titled "ActiveDrivers Over Time," illustrating the number of active drivers over a period. 

- The x-axis represents "Time," and the y-axis shows the "# ActiveDrivers."
- There are two lines on the graph: a blue line labeled "Base" and an orange line labeled "LLM_Reengage."
- Both lines start at zero and rise to a peak before declining.
- The orange line ("LLM_Reengage") shows a steeper rise, reaches a higher peak of around 1600 active drivers, and eventually levels out at a higher number than the blue line.
- The blue line ("Base") has a similar pattern but peaks at a lower value, around 1200 active drivers, and flattens out at a lower level.
- Both lines show a general trend of rapid growth, peaking, and then a decline before stabilizing.

<p class="img-desc i tc f6">Improving driver reengagement does increase active drivers</p>

Presumably increasing the rate that we reactivate suspended drivers from 1% to 2.5% would
have a similar, meaningful but smaller impact on active drivers over time.
So let's model that change.

```
# 2.5% of SuspendedDrivers are reactivated
#SuspendedDrivers > ActiveDrivers @ Leak(0.01)
SuspendedDrivers > ActiveDrivers @ Leak(0.025)
```

However, surprisingly, the impact of increasing the reactivation rate of suspended drivers is
actually much higher than reengaging departed drivers.

**Image Description:** The image is a line graph titled "ActiveDrivers Over Time." It presents data on the number of active drivers over a period, depicted on the y-axis as "# ActiveDrivers," while the x-axis shows "Time."

There are three lines representing different scenarios:

1. **Blue Line (Base)**: This line represents the base scenario. It shows a gradual increase in active drivers, peaking around 1,000 before decreasing and stabilizing below that point over time.

2. **Orange Line (LLM_Reengage)**: This scenario shows a similar trend to the base but begins to diverge around time 50. It peaks at a higher point, over 1,500 active drivers, before decreasing and leveling out significantly higher than the base scenario.

3. **Green Line (LLM_Unsuspend)**: This line increases more rapidly than the others, peaking around 2,000 active drivers. After peaking, it decreases sharply before stabilizing above 1,500 active drivers, maintaining a consistently higher level than the other two lines.

The legend is located in the upper right corner, identifying the scenarios corresponding to each colored line. The graph indicates differences in driver engagement over time under various conditions.

<p class="img-desc i tc f6">Increasing reactivation rate of suspend drivers has highest impact</p>

This is an interesting, and somewhat counter-intuitive result.
Increasing the rate for both suspended and departed rates is more impactful
than increasing either, because ultimately there's a growing population of drivers
in the slower deflating stock.
This means, surprisingly, that a tool that helps us quickly determine which drivers
could be unsuspended might matter more than the small size of the flow indicates.

At this point, we've probably found the primary story that this model wants to tell us:
we should focus efforts on reactivating departed and suspended drivers.
Changes elsewhere might reduce operational costs of our business, but they won't
solve the problem of increasing active drivers.