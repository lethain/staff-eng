# Systems model of API deprecation
url: https://draftingstrategy.com/api-deprecation-model

In [How should Stripe deprecate APIs?](https://draftingstrategy.com/api-deprecation-strategy/), the diagnosis
depends on the claim that deprecating APIs is a significant cause of customer churn.
While there is internal data that can be used to correlate deprecation with churn,
it's also valuable to build a model to help us decide if we believe that
correlation and causation are aligned in this case.

In this chapter, we'll cover:

1. What we learn from modeling API deprecation's impact on user retention
2. Developing a system model using the [lethain/systems](https://github.com/lethain/systems) package on GitHub.
    That model [is available in the lethain/eng-strategy-models](https://github.com/lethain/eng-strategy-models/blob/main/APIDeprecationModel.ipynb)
    repository
3. Exercising that model to learn from it

Time to investigate whether it's reasonable to believe that API deprecation
is a major influence on user retention and churn.

## Learnings

In an initial model that has 10% baseline for customer churn per round,
reducing customers experiencing API deprecation from 50% to 10% per round only increases
the steady state of integrated customers by about 5%.

**Image Description:** The image is a line graph titled "Customer Integration & Churn Over Time." It displays data of four different customer categories over 100 rounds. 

**Axes:**
- The x-axis represents the number of rounds, ranging from 0 to 100.
- The y-axis represents the size of stock, ranging from 0 to 1000.

**Lines:**
1. **Blue Line**: Represents "Initial IntegratedCustomers," starting at zero and rising sharply before starting to level off at just over 800.
2. **Orange Line**: Represents "Initial DeprecationImpactedCustomers," starting at zero and rising to around 200.
3. **Green Line**: Represents "LessDeprecation IntegratedCustomers," starting at zero and rising above 900, eventually leveling off.
4. **Red Line**: Represents "LessDeprecation DeprecationImpactedCustomers," starting at zero and remaining below 100.

**General Observations:**
- All lines begin at zero, indicating a starting point with no customers.
- The "LessDeprecation IntegratedCustomers" (green) has the highest final value, suggesting a successful integration strategy.
- The "Initial DeprecationImpactedCustomers" (orange) levels off early and remains stable, indicating limited growth.
- The "LessDeprecation DeprecationImpactedCustomers" (red) exhibits minimal growth, remaining the lowest throughout.

The graph includes a legend, which identifies each line by color and

<p class="img-desc i tc f6">Impact of 10% and 50% API deprecation on integrated customers</p>

However, if we eliminate the baseline for customer churn entirely, then we see a massive
difference between a 10% and 50% rate of API deprecation.

**Image Description:** The image is a line graph titled "Customer Integration & Churn Over Time." It plots the "Size of Stock" on the y-axis against "Rounds" on the x-axis, which ranges from 0 to 100. There are four lines representing different scenarios:

1. **Blue Line**: "LowDeprecationNoBaseline IntegratedCustomers" - This line starts at zero and increases sharply, indicating a rapid growth in customer stock over time.

2. **Orange Line**: "LowDeprecationNoBaseline DeprecationImpactedCustomers" - This line has a slight upward curve, starting at zero and increasing gradually, representing a slower growth.

3. **Green Line**: "NoBaselineChurn IntegratedCustomers" - This line also starts at zero and shows moderate growth, positioned between the blue and red lines.

4. **Red Line**: "NoBaselineChurn DeprecationImpactedCustomers" - The line starts at zero and shows a gradual increase, similar to the orange line but slightly higher.

Overall, the graph visualizes how different strategies can impact customer stock growth and retention over time.

<p class="img-desc i tc f6">Impact of rates of API deprecation with zero baseline churn</p>

The biggest takeaway from this model is that eliminating API-deprecation churn alone
won't significantly increase the number of integrated customers.
However, we also can't fully benefit from reducing baseline churn without simultaneously reducing API deprecations.
Meaningfully increasing the number of integrated customers requires lowering both sorts of churn in tandem.

## Sketch

We'll start by sketching the model's happiest path: potential customers flowing into
engaged customers and then becoming integrated customers. This represents a customer
who decides to integrate with Stripe's APIs, and successfully completes that integration
process.

**Image Description:** The image is a simple flowchart consisting of three rounded rectangular boxes connected by arrows, illustrating a customer journey. 

1. **First Box: "Potential Customers"**
   - Positioned on the left.
   - Contains the text "potential customers."
   - Connected to the next box by a rightward arrow.

2. **Second Box: "Engaged Customers"**
   - Located in the center.
   - Contains the text "engaged customers."
   - Connected from the first box by an arrow and to the third box by another rightward arrow.

3. **Third Box: "Integrated Customers"**
   - Positioned on the right.
   - Contains the text "integrated customers."
   - Represents the final stage in the flowchart.

The flowchart depicts the progression of potential customers into engaged customers and finally into integrated customers, showcasing a customer development or conversion process.

<p class="img-desc i tc f6">Happiest path for Stripe API integration</p>

Business would be good if that were the entire problem space.
Unfortunately, customers do occasionally churn.
This churn is represented in two ways:

1. `baseline churn` where integrated customers leave Stripe for any number of reasons,
    including things like dissolution of their company
2. `experience deprecation` followed by `deprecation-influenced churn`, which represent
    the scenario where a customer decides to leave after an API they use is deprecated

There is also a flow for `reintegration`, where a customer impacted by API deprecation
can choose to update their integration to comply with the API changes.

Pulling things together, the final sketch shows five stocks and six flows.

**Image Description:** The image is a flowchart depicting the journey of customers through different phases.

1. **Potential Customers**: The process begins with potential customers, indicated by a rounded rectangle on the left. An arrow points from here to the next stage.

2. **Engaged Customers**: Potential customers transition into engaged customers, shown by another rounded rectangle. An "initial integration" label is attached to the arrow pointing to the next stage.

3. **Integrated Customers**: Engaged customers become integrated customers. From this stage, there's a "baseline churn" arrow leading to "churned customers."

4. **Churned Customers**: Integrated customers that leave are marked as churned customers, depicted by another rectangle on the right.

5. **Experience Deprecation**: This process affects integrated customers, leading to "deprecation-impacted customers." An arrow flows downward, labeled "experience deprecation."

6. **Deprecation-Impacted Customers**: These customers are impacted by deprecation. They can either be reintegrated back to integrated customers or lead to "deprecation-influenced churn," moving them to churned customers.

Arrows clearly map out the customer journey and various transitions between states, with some processes highlighted in red for emphasis.

<p class="img-desc i tc f6">Final version of systems model for API deprecation</p>

You could imagine modeling additional dynamics, such as recovery of churned customers,
but it seems unlikely that would significantly influence our understanding of how API deprecation
impacts churn.

## Reason

In terms of acquiring customers, the most important flows
are customer acquisition and initial integration with the API.
Optimizing those flows will increase the number of existing integrations.

The flows driving churn are baseline churn, and
the combination of API deprecation and deprecation-influenced churn.
It's difficult to move baseline churn for a payments API, as many churning
customers leave due to company dissolution.  From a revenue-weighted perspective,
baseline churn is largely driven by non-technical factors, primarily pricing.
In either case, it's challenging to impact this flow without significantly lowering margin.

Engineering decisions, on the other hand, have a significant impact on both the number of API deprecations,
and on the ease of reintegration after a migration.
Because the same work to support reintegration also supports the initial integration experience,
that's a promising opportunity for investment.

## Model

You can find the [full implementation of this model on GitHub](https://github.com/lethain/eng-strategy-models/blob/main/APIDeprecationModel.ipynb)
if you want to see the full model rather than these emphasized snippets.

Now that we have identified the most interesting avenues for experimentation,
it's time to develop the model to evaluate which flows are most impactful.

Our initial model specification is:

    # User Acquisition Flow
    [PotentialCustomers] > EngagedCustomers @ 100
    # Initial Integration Flow
    EngagedCustomers > IntegratedCustomers @ Leak(0.5)
    # Baseline Churn Flow
    IntegratedCustomers > ChurnedCustomers @ Leak(0.1)
    # Experience Deprecation Flow
    IntegratedCustomers > DeprecationImpactedCustomers @ Leak(0.5)
    # Reintegrated Flow
    DeprecationImpactedCustomers > IntegratedCustomers @ Leak(0.9)
    # Deprecation-Influenced Churn
    DeprecationImpactedCustomers  > ChurnedCustomers @ Leak(0.1)

Whether these are _reasonable_ values depends largely on how we think about the
length of each round. If a round was a month, then assuming half of integrated customers
would experience an API deprecation would be quite extreme. If we assumed it was a year,
then it would still be high, but there are certainly some API providers that routinely deprecate
at that rate. (From my personal experience, I can say with confidence that Facebook's Ads API deprecated
at least one important field on a quarterly basis in the 2012-2014 period.)

Admittedly, for a payments API this would be a high rate, and is intended primarily as a
contrast with more reasonable values in the exercise section below.

## Exercise

Our goal with exercising this model is to understand how much API deprecation impacts customer churn.
We'll start by charting the initial baseline, then move to compare it with a variety of scenarios
until we build an intuition for how the lines move.

**Image Description:** The image is a line graph titled "Customer Integration & Churn Over Time" and it illustrates the changes in customer stock size over 100 rounds.

- **X-axis (horizontal):** Represents the "Rounds," ranging from 0 to 100.
- **Y-axis (vertical):** Represents the "Size of Stock," ranging from 0 to 1000.

There are two lines on the graph:

1. **Blue Line ("Initial IntegratedCustomers"):**
   - Starts at zero and increases rapidly, showing a steep rise, indicating rapid customer integration.
   - The growth rate slows over time and levels off near the top of the graph, close to a size of 1000.

2. **Orange Line ("Initial DeprecationImpactedCustomers"):**
   - Also starts at zero, follows an initial steep rise, but at a slower pace compared to the blue line.
   - It levels off at a lower point, around 400, indicating the impact of deprecation on this group is less extensive than the integration growth.

The legend in the bottom right explains the color coding of the lines. The graph illustrates how two different customer groups change over time in terms of stock size, with integration being more extensive than the deprecation impact.

<p class="img-desc i tc f6">Initial model stabilizing integrated customers around 1,000 customers</p>

The initial chart stabilizes in about forty rounds, maintaining about 1,000 integrated customers
and 400 customers dealing with deprecated APIs.
Now let's change the experience deprecation flow to impact significantly fewer
customers:

    # Initial setting with 50% experiencing deprecation per round
    IntegratedCustomers > DeprecationImpactedCustomers @ Leak(0.5)
    
    # Less deprecation, only 10% experiencing per round
    IntegratedCustomers > DeprecationImpactedCustomers @ Leak(0.1)

After those changes, we can compare the two scenarios.

**Image Description:** The image is a line graph titled "Customer Integration & Churn Over Time." It displays data over 100 rounds on the x-axis, with the "Size of Stock" measured on the y-axis, which ranges from 0 to 1000.

There are four lines on the graph:

1. **Blue Line (Initial Integrated Customers):**
   - Shows a steady increase and levels off around 800.

2. **Orange Line (Initial Deprecation Impacted Customers):**
   - Rises initially and stabilizes around 400.

3. **Green Line (Less Deprecation Integrated Customers):**
   - Increases rapidly and flattens near 1000.

4. **Red Line (Less Deprecation Deprecation Impacted Customers):**
   - Has a slight initial rise and settles close to 200.

The legend in the bottom right identifies each line by color and the corresponding customer group it represents. The graph illustrates how different customer segments grow or stabilize over time and in the context of deprecation impact.

<p class="img-desc i tc f6">Impact of 10% and 50% API deprecation on integrated customers</p>

Lowering the deprecation rate significantly reduces the number of companies dealing with deprecations
at any given time, but it has a relatively small impact on increasing the steady state for integrated customers.
This must mean that another flow is significantly impacting the size of the integrated customers stock.

Since there's only one other flow impacting that stock, baseline churn, that's the one to exercise next.
Let's set the baseline churn flow to zero to compare that with the initial model:

    # Initial Baseline Churn Flow
    IntegratedCustomers > ChurnedCustomers @ Leak(0.1)
    
    # Zeroed out Baseline Churn Flow
    IntegratedCustomers > ChurnedCustomers @ Leak(0.0)

These results make a compelling case that baseline churn is
dominating the impact of deprecation. With no baseline churn, the number of integrated customers
stabilizes at around 1,750, as opposed to around 1,000 for the initial model.

**Image Description:** The image is a line graph titled "Customer Integration & Churn Over Time." It depicts four different data series, each representing customer stock size across 100 rounds. The x-axis represents "Rounds," ranging from 0 to 100, and the y-axis represents "Size of Stock," ranging from 0 to 2000.

1. **Blue Line**: Represents "Initial Integrated Customers," rising steadily and plateauing around 1250.
2. **Orange Line**: Represents "Initial Deprecation Impacted Customers," increasing initially, then stabilizing around 250.
3. **Green Line**: Represents "No Baseline Churn Integrated Customers," showing a sharp increase, then leveling off near 1800.
4. **Red Line**: Represents "No Baseline Churn Deprecation Impacted Customers," following a similar pattern to the blue line, plateauing near 500.

The legend is placed in the lower right quadrant of the graph, identifying each line by color.

<p class="img-desc i tc f6">Impact of eliminating baseline churn from model</p>

Next, let's compare two scenarios without baseline churn, where one has high API deprecation (50%)
and the other has low API deprecation (10%).

**Image Description:** The image is a line graph titled "Customer Integration & Churn Over Time." The x-axis is labeled "Rounds," ranging from 0 to 100. The y-axis is labeled "Size of Stock," with values from 0 to 6000.

There are four lines on the graph, each representing different customer metrics over time:

1. **Blue Line**: "LowDeprecationNoBaseline IntegratedCustomers." This line shows a steep upward trend, reaching about 6000 by the 100th round.
2. **Orange Line**: "LowDeprecationNoBaseline DeprecationImpactedCustomers." This line starts low and increases slowly, reaching just under 1000 by the end.
3. **Green Line**: "NoBaselineChurn IntegratedCustomers." This line rises steadily but not as sharply as the blue line, peaking around 2000.
4. **Red Line**: "NoBaselineChurn DeprecationImpactedCustomers." This line starts similar to the orange line but trends slightly higher, ending just over 1000.

The legend indicating the lines is located at the top center of the graph.

<p class="img-desc i tc f6">Impact of rates of API deprecation with zero baseline churn</p>

In the case of two scenarios without baseline churn, we can see having an API deprecation rate of
10% leads to about 6,000 integrated customers, as opposed to 1,750 for a 50% rate of API deprecation.
More importantly, in the 10% scenario, the integrated customers line shows no sign of flattening, and
continues to grow over time rather than stabilizing.

The takeaway here is that significantly reducing either baseline churn or API deprecation magnifies the benefits of reducing the other.
These results also reinforce the value of treating churn reduction as a system-level optimization,
not merely a collection of discrete improvements.