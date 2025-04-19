# Modeling impact of LLMs on Developer Experience.
url: https://draftingstrategy.com/llm-adoption-model

In [How should you adopt Large Language Models?](https://draftingstrategy.com/llm-adoption-strategy/) (LLMs), we considered how
LLMs might impact a company's developer experience. To support that exploration, I've developed a [system model](https://draftingstrategy.com/systems-modeling/)
of the software development process at the company.

In this chapter, we'll work through:

1. Summary results from this model
2. How the model was developed, both sketching and building the model in a spreadsheet.
    (As discussed in [the overview of systems modeling](https://draftingstrategy.com/systems-modeling/),
    I generally would recommend against using spreadsheets to develop most models,
    but it's educational to attempt doing so once or twice.)
3. Exercise the model to see what it has to teach us

Let's get into it.

---

*This is an exploratory, draft chapter for a book on engineering strategy that I’m brainstorming in*
*[#eng-strategy-book](https://lethain.com/tags/eng-strategy-book/).*
*As such, some of the links go to other draft chapters, both published drafts and very early, unpublished drafts.*

## Learnings

This model's insights can be summarized in three charts.
First, the baseline chart, which shows an eventual equilibrium between errors discovered
in production and tickets that we've closed by shipping to production.
This equilibrium is visible because tickets continue to get opened, but the total number of
closed tickets stops increasing.

**Image Description:** The image is a line chart titled "Started Coding, Tested Code, Deployed Code and Closed Ticket." It tracks the progress of five different categories over time, which are represented by different colored lines. Here's a detailed breakdown:

1. **Open Tickets (Blue Line):**
   - The line starts at around 10 on the y-axis and increases steadily to reach 25.
   - It indicates a continuous increase in the number of open tickets.

2. **Started Coding (Red Line):**
   - The line progresses straight from the origin up to 5, where it remains constant.
   - This shows that after an initial phase, the number of tickets where coding started stabilizes.

3. **Tested Code (Yellow Line):**
   - It is not visible on the chart, indicating it might be overlapping with the x-axis (value of 0).

4. **Deployed Code (Green Line):**
   - This line is flat just above the x-axis, suggesting no notable change and possibly representing a value close to 1.

5. **Closed Ticket (Orange Line):**
   - It rises quickly to 5 and stays constant.
   - This suggests a quick closure of some tickets, followed by stability.

The chart visually represents how different stages of the process progress over time, highlighting the backlog or accumulation of open tickets compared to other stages.

<p class="img-desc i tc f6">Baseline chart where closed tickets quickly stops increasing</p>

Second, we show that we can shift that equilibrium by reducing the error rate in production.
Specifically, the first chart models 25% of closed tickets in production experiencing an error,
whereas the second chart models only a 10% error rate.
The equilibrium returns, but at a higher value of shipped tickets.

**Image Description:** The image is a line graph titled "Started Coding, Tested Code, Deployed Code and Closed Ticket." It tracks the progress of these activities over time with the following color-coded lines:

1. **Open Tickets (Blue Line)**: Starts at 10, increases slightly, and then rises sharply to reach around 18.

2. **Started Coding (Red Line)**: Begins at 0, climbs steadily, and plateaus at 12.

3. **Tested Code (Yellow Line)**: Remains constant throughout at a value of 5.

4. **Deployed Code (Green Line)**: Remains constant at a value close to 1.

5. **Closed Ticket (Orange Line)**: Starts at 0, steadily increases to reach 12, then maintains that value.

The graph displays an increase in open tickets and continued activity in started coding and closed tickets over time, with tested and deployed code remaining static.

<p class="img-desc i tc f6">Reduced error rates delay, but don't prevent, reaching equilibrium of closed tickets</p>

Finally, we can see that even tripling the rate that we start and test tickets
doesn't meaningfully change the total number of completed tickets,
as modeled in this third chart.

**Image Description:** The image is a line graph titled "Started Coding, Tested Code, Deployed Code and Closed Ticket" and it displays five different data series over time:

1. **Open Tickets (Blue Line)**: This line fluctuates above 10, decreasing and increasing over time.

2. **Started Coding (Red Line)**: This line starts at zero, rises to a peak close to 5, and then displays a zigzag pattern with multiple ups and downs, staying below 5.

3. **Tested Code (Yellow Line)**: This line remains flat at zero, indicating no activity.

4. **Deployed Code (Green Line)**: This line is consistent and flat at zero, showing no movement or change.

5. **Closed Ticket (Orange Line)**: This line starts at zero and gradually increases to just over 5 where it flattens out and remains constant.

The graph depicts the activity and progression of different stages of a workflow, such as coding and ticket handling, with blue showing the most variance and green/yellow showing none.

<p class="img-desc i tc f6">Starting or testing tickets faster creates noise but not progress</p>

The constraint on this system is errors discovered in production,
and any technique that changes something else doesn't make much of an impact.
Of course, this is just _a model_, not reality. There are many nuances
that models miss, but this helps us focus on what probably matters the most,
and in particular highlights that any approach that increases development velocity
while also increasing production error rate is likely net-negative.

With that summary out of the way, now we can get into developing the model itself.

## Sketch

Modeling in a spreadsheet is labor intensive, so we want to iterate as much as possible
in the sketching phase, before we move to the spreadsheet.
In this case, we're working with [Excalidraw](https://excalidraw.com/).

**Image Description:** The image is a flowchart illustrating a software development process with various stages:

1. **Open Tickets**: The process starts here. This stage feeds into the "Start Coding" phase. 

2. **Start Coding**: This is the second stage where coding begins. It leads to the "Tested Code" stage. If testing finds an error at this stage, the process loops back to "Open Tickets."

3. **Tested Code**: This is the third stage where the code is tested. If testing uncovers issues, it goes back to "Start Coding." 

4. **Deployed Code**: Once testing is successful, the code is deployed. If deployment exposes an error, it cycles back to "Open Tickets."

5. **Closed Ticket**: This final stage is reached when everything is functioning correctly. However, if an error is found in production, it goes back to "Open Tickets."

Arrows indicate the flow between stages, and additional arrows represent the feedback loops when errors are found at different stages of the process.

<p class="img-desc i tc f6">Five stages of development, with errors causing backwards movement</p>

I sketched five stocks to represent a developer's workflow:

1. `Open Tickets` is tickets opened for an engineer to work on
2. `Start Coding` is tickets that an engineer is working on
3. `Tested Code` is tickets that have been tested
4. `Deployed Code` is tickets than have been deployed
5. `Closed Ticket` is tickets that are closed after reaching production

There are four flows representing tickets progressing through this development process from left to right.
Additionally, there are three exception flows that move from right to left:

1. `Testing found error` represents a ticket where testing finds an error, moving the ticket backwards to `Start Coding`
2. `Deployment exposed error` represents a ticket encountering an error during deployment, where it's moved backwards to `Start Coding`
3. `Error found in production` represents a ticket encountering a production error, which causes it to move all the way back to the beginning as a new ticket

One of your first concerns seeing this model might be that it's embarrassingly simple.
To be honest, that was my reaction when I first looked at it, too.
However, it's important to recognize that feeling and then dig into whether it matters.

This model is quite simple, but in the next section we'll find that it reveals several
counter-intuitive insights into the problem that will help us avoid erroneously viewing the
tooling as a failure if time spent testing increases.
The value of a model is in refining our thinking, and simple models are usually more effective
at refining thinking across a group than complex models, simply because complex models are fairly
difficult to align a group around.

## Reason

As we start to look at this sketch, the first question to ask is how might LLM-based tooling show an improvement?
The most obvious options are:

1. Increasing the rate that tasks flow from `Starting coding` to `Tested code`.
    Presumably these tools might reduce the amount of time spent on implementation.
2. Increasing the rate that `Tested code` follows `Testing found errors` to return to `Starting code`
    because more comprehensive tests are more likely to detect errors.
    This is probably the first interesting learning from this model: if the adopted tool works well, it's likely that we'll spend
    _more_ time in the testing loop, with a long-term payoff of spending less time solving problems in production where it's more expensive.
    This means that slower testing might be a successful outcome rather than a failure as it might first appear.

    A skeptic of these tools might argue the opposite, that LLM-based tooling will cause more issues to be identified "late"
    after deployment rather than early in the testing phase. In either case, we now have a clear goal to measure to evaluate
    the effectiveness of the tool: reducing the `Error found in production` flow. We also know _not_ to focus on the
    `Testing found error` flow, which should probably increase.
3. Finally, we can also zoom out and measure the overall time from `Start Coding` to `Closed Ticket` for tasks
    that don't experience the `Error found in production` flow for at least the first 90 days after being completed.

These observations capture what I find remarkable about systems modeling: even a very simple model
can expose counter-intuitive insights. In particular, the sort of insights that build conviction to push
back on places where intuition might lead you astray.

## Model

For this model, we'll be modeling it directly in a spreadsheet, specifically Google Sheets.
The completed spreadsheet model [is available here](https://docs.google.com/spreadsheets/d/1YAego3JiNCUE15GeL_3GQfYmrE1jG9dVF6yzu-mAxLw/edit?gid=1325089804#gid=1325089804).
As discussed in [Systems modeling to refine strategy](https://draftingstrategy.com/systems-modeling/), spreadsheet modeling
is brittle, slow and hard to iterate on. I generally recommend that folks attempt to model something in a spreadsheet
to get an intuitive sense of the math happening in their models, but I would almost always choose any tool other
than a spreadsheet for a complex model.

This example is fairly tedious to follow, and you're entirely excused if you decide to pull open the sheet itself,
look around a bit, and then skip the remainder of this section.
If you are hanging around, it's time to get started.

The spreadsheet we're creating has three important worksheets:

* *Model* represents the model itself
* *Charts* holds charts of the model
* *Config* holds configuration values separately from the model to ease exercising the model after we've built it

Going to the model worksheet, we want to start out by initializing each of the columns to the starting value.

**Image Description:** The image shows a table with two rows and five columns. 

- The columns are titled: "Open Tickets," "Started Coding," "Tested Code," "Deployed Code," and "Closed Ticket."
- In the first row, these are the column headers, styled in bold text.
- The second row contains numeric data:
  - "Open Tickets": 10
  - "Started Coding": 0
  - "Tested Code": 0
  - "Deployed Code": 0
  - "Closed Ticket": 0

The table appears to be tracking the status and progress of coding tasks or projects.

<p class="img-desc i tc f6">Initial values of a systems model</p>

While we'll use formulae for subsequent rows, the first row should contain literal values. I often start with
a positive value in the first column and zeros in the other columns, but that isn't required.
You can start with whatever starting values are more useful for studying the model that you're building.

With the initial values set, we're now going to implement the model in two passes.
First, we'll model the left-to-right flows, which represent the standard development process.
Second, we'll model the right-to-left flows, which represent exceptions in the process.

### Modeling left-to-right

We'll start by modeling the interaction between the first two nodes: `Open Tickets` and `Started Coding`.
We want to have open tickets increased over time at a fixed rate, so let's add a value in the config worksheet
for `TicketOpenRate`, starting with `1`.

Moving to the second stock, we want to start work on open tickets as long as we have at most `MaxConcurrentCodingNum` open tickets.
If we have more than `MaxConcurrentCodingNum` tickets that we're working on, then we don't start working on any new tickets.
To do this, we actually need to create an intermediate value (represented using an italics column name) to determine how
many should be created by checking if the current in started tickets is at maximum (another value in the config sheet)
or if we should increment that by one.

That looks like:

    // Config!$B$3 is max started tickets
    // Config!$B$2 is rate to increment started tickets
    // $ before a row or column, e.g. $B$3 means that the row or column
    //   always stays the same -- not incrementing -- even when filled
    //   to other cells
    = IF(C2 >= Config!$B$3, 0, Config!$B$2)

This also means that our first column, for `Open Tickets` is decremented by the number of tickets that
we're started coding:

    // This is the definition of `Open Tickets`
    =A2 + Config!$B$1 - B2

Leaving us with these values.

**Image Description:** The image displays a spreadsheet with columns titled: "Open Tickets," "StartCodingMore?" "Started Coding," "Tested Code," "Deployed Code," and "Closed Ticket."

- Rows are numbered from 2 to 20.
- "Open Tickets" column has values increasing sequentially from 10 to 28.
- "StartCodingMore?" column mostly has 0s, except for rows 3, 4, and 5, which have 1s.
- "Started Coding" column matches "StartCodingMore?" with corresponding values: 1s for rows 3, 4, and 5, otherwise 0s.
- "Tested Code" column starts with a 0 for row 2, then increases from 1 to 3 for rows 3 to 5, with 3 continuing through row 20.
- "Deployed Code" and "Closed Ticket" columns remain at 0 throughout.

The overall structure seems to track the progress of coding tasks from open tickets to closure.

<p class="img-desc i tc f6">Open tickets, StartCodingMore?, and Started Coding columns in spreadsheet model</p>

Now we want to determine the number of tickets being tested at each step in the model.
To do this, we create a calculation column, `NumToTest?` which is defined as:

    // Config$B$4 is the rate we can start testing tickets
    // Note that we can only start testing tickets if there are tickets
    // in `Started Coding` that we're able to start testing
    =MIN(Config!$B$4, C3)

We then add that value to the previous number of tickets being tested.

    // E2 is prior size of the Tested Code stock
    // D3 is the value of `NumToTest?`
    // F2 is the number of tested tickets to deploy
    =E2 + D3 - F2

**Image Description:** The image is a spreadsheet with six columns and 21 rows, including headers. Here's a detailed description of each column:

1. **Open Tickets**: 
   - Rows 2 to 20 have the value 11.
   - Row 1 (header) is labeled "Open Tickets."

2. **Started Coding**: 
   - Row 2 has the value 0.
   - Rows 3 to 20 have the value 1.
   - Row 1 (header) is labeled "Started Coding."

3. **NumToTest?**: 
   - Row 2 has the value 0.
   - Rows 3 to 20 have the value 1.
   - Row 1 (header) is labeled "NumToTest?"

4. **Tested Code**: 
   - Values in rows 2 to 20 increment sequentially from 0 to 18.
   - Row 1 (header) is labeled "Tested Code."

5. **Deployed Code**:
   - All cells from rows 2 to 20 are empty.
   - Row 1 (header) is labeled "Deployed Code."

6. **Closed Ticket**:
   - All cells from rows 2 to 20 are empty.
   - Row 1 (header) is labeled "Closed Ticket."

The rows alternate between filled and shaded in gray, primarily in the first column, to enhance readability.

<p class="img-desc i tc f6">Started Coding, NumToTest?, and Tested Code columns in spreadsheet model</p>

Spreadsheet showing three columns of systems modeling

Moving on to deploying code, let's keep things simple and start out by assuming that every tested change
is going to get deployed. That means the calculation for `NumToDeploy?` is quite simple:

    // E3 is the number of tested changes
    =E3

Then the value for the `Deployed Code` stock is simple as well:

    // G2 is the prior size of Deployed Code
    // F3 is NumToDeploy?
    // H2 is the number of deployed changes in prior round
    =G2+F3-H2

**Image Description:** The image is a spreadsheet displaying data related to a software development workflow, with columns titled as follows:

1. **Open Tickets**: Shows the number of open tickets, starting at 10 and then consistently listed as 11.
2. **Started Coding**: Has binary values, indicating if coding has started, with most values being 1.
3. **Tested Code**: Also contains binary values, with most entries being 1.
4. **NumToDeploy?**: Incrementing values starting from 0 up to 17.
5. **Deployed Code**: Has consistently increasing values from 0 to 18.
6. **NumToClose?**: Mirrors the **NumToDeploy?** column, with values increasing from 0 to 17.
7. **Closed Ticket**: Consistent values of 0 across all entries.

Columns are shaded gray and white alternately, with gray being predominant.

<p class="img-desc i tc f6">NumToDeploy? and Deployed Code columns in spreadsheet model</p>

Now we're on to the final stock.
We add the `NumToClose?` calculation, which assumes that all deployed changes are now closed.

    // G3 is the number of deployed changes
    =G3

This makes the calculation for the `Closed Tickets` stock:

    // I2 is the prior value of Closed Tickets
    // H3 is the NumToClose?
    =I2 + H3

With that, we've now modeled the entire left-to-right flows.

**Image Description:** The image shows a spreadsheet with six columns and twenty rows of data. The columns are labeled: "Open Tickets," "Started Coding," "Tested Code," "Deployed Code," "NumToClose?," and "Closed Ticket."

Here's the structure of the data:

- **Open Tickets:** Row 2 starts with 10, and from row 3 onward, each entry is 11.
- **Started Coding:** Row 2 begins with 0, and from row 3 onward, each entry is 1.
- **Tested Code:** Row 2 starts with 0, transitioning to 1 from row 3 onward.
- **Deployed Code:** Row 2 is 0, with 1s starting from row 3 onward.
- **NumToClose?:** Row 2 begins with 0, changing to 1 from row 3 onward.
- **Closed Ticket:** Row 2 starts at 0 and increases by 1 in each subsequent row until row 20, ending at 18.

The pattern suggests a progression in ticket handling, coding, testing, deploying, and closing processes.

<p class="img-desc i tc f6">Entirety of left-to-right flows in spreadsheet model</p>

The left-to-right flows are simple, with a few constrained flows and a very scalable flows, but overall we see things
progressing through the pipeline evenly.
All that is about to change!

### Modeling right-to-left

We've now finished modeling the happy path from left to right.
Next we need to model all the exception paths where things flow right to left.
For example, an issue found in production would cause a flow from `Closed Ticket`
back to `Open Ticket`.
This tends to be where models get interesting.

There are three right-to-left flows that we need to model:

1. `Closed Ticket` to `Open Ticket` represents a bug discovered in production.
2. `Deployed Code` to `Start Coding` represents a bug discovered during deployment.
3 `Tested Code` to `Start Coding` represents a bug discovered in testing.

To start, we're going to add configurations defining the rates of those flows.
These are going to be percentage flows, with a certain percentage of the target stock
triggering the error condition rather than proceeding. For example, perhaps 25% of the
`Closed Tickets` are discovered to have a bug each round.

**Image Description:** The image is a screenshot of a spreadsheet consisting of a single sheet. The spreadsheet contains data in two columns, A and B, spanning seven rows. 

- **Column A** lists different metrics with these entries:
  1. TicketOpenRate
  2. StartCodingRate
  3. MaxConcurrentCodingNum
  4. TicketTestRate
  5. ErrorsInProd
  6. ErrorsInDeploy
  7. ErrorsInTest

- **Column B** contains numerical values corresponding to each metric in column A:
  1. 1
  2. 1
  3. 3
  4. 1
  5. 0.25
  6. 0.25
  7. 0.25

- Rows 1 through 4 and columns A through E are shaded in gray, suggesting those cells are formatted differently. Rows 5 through 7, specifically in column A, have a white background.

There are no entries in columns C, D, or E.

<p class="img-desc i tc f6">Introducing three additional values in model configuration</p>

These are fine starter values, and we'll experiment with how adjusting them changes the model in the *Exercise* section below.

Now we'll start by modeling errors discovered in production, by adding a column
to model the flow from `Closed Tickets` to `Open Tickets`, the `ErrorsFoundInProd?` column.

    // I3 is the number of Closed Tickets
    // Config!$B$5 is the rate of errors
    =FLOOR(I3 * Config!$B$5)

Note the usage of `FLOOR` to avoid moving partial tickets.
Feel free to skip that entirely if you're comfortable with the concept of fractional tickets, fractional deploys, and so on.
This is an aesthetic consideration, and generally only impacts your model if you choose overly small starting values.

This means that our calculation for `Closed Ticket` needs to be
updated as well to reduce by the prior row's result for `ErrorsFoundInProd?`:

    // I2 is the prior value of ClosedTicket
    // H3 is the current value of NumToClose?
    // J2 is the prior value of ErrorsFoundInProd?
    =I2 + H3 - J2

We're not quite done, because we _also_ need to add the prior row's value of `ErrorsInProd?`
into `Open Tickets`, which represents the errors' flow from closed to open tickets.
Based on this change, the calculation for `Open Tickets` becomes:

    // A2 is the prior value of Open Tickets
    // Config!$B$1 is the base rate of ticket opening
    // B2 is prior row's StartCodingMore?
    // J2 is prior row's ErrorsFoundInProd?
    =A2 + Config!$B$1 - B2 + J2

Now we have the full errors in production flow represented in our model.

**Image Description:** The image is a spreadsheet containing data related to a ticket processing workflow. It has columns labeled as follows:

- Column A: "Open Tickets" with values ranging from 10 to 25.
- Column B: "StartCodingMore?" with binary values (0 or 1).
- Column C: "Started Coding" with binary values.
- Column E: "Tested Code" with binary values.
- Column G: "Deployed Code" with binary values.
- Column I: "Closed Ticket" with numeric values starting from 0 and increasing to 4.
- Column J: "ErrorsFoundInProd?" with binary values.

Each row seems to represent an instance of ticket processing, describing the state of tickets as they progress through coding, testing, deployment, and closing phases, along with error detection.

<p class="img-desc i tc f6">Modeling ErrorsFoundInProd? in spreadsheet model</p>

Next, it's time to add the `Deployed Code` to `Start Coding` flow.
Start by adding the `ErrorsFoundInProd?` calculation:

    // G3 is deployed code
    // Config!$B$6 is deployed error rate
    =FLOOR(G3 * Config!$B$6)

Then we need to update the calculation for `Deployed Code` to decrease by the
calculated value in `ErrorsFoundInProd?`:

    // G2 is the prior value of Deployed Code
    // F3 is NumToDeploy?
    // H2 is prior row's NumToClose?
    // I2 is ErrorsFoundInDeploy?
    =G2 + F3 - H2 - I2

Finally, we need to increase the size of `Started Coding` by the same value,
representing the flow of errors discovered in deployment:

    // C2 is the prior value of Started Coding
    // B3 is StartCodingMore?
    // D2 is prior value of NumToTest?
    // I2 is prior value of ErrorsFoundInDeploy?
    =C2 + B3 - D2 + I2

We now have the working flow representing errors in production.

**Image Description:** The image is a screenshot of a spreadsheet with a table comprising 9 columns and 20 rows (including headers). Here are the detailed columns and their contents:

1. **Open Tickets (Column A):** 
   - Numeric values ranging from 10 to 25, increasing incrementally by 1 with each row.

2. **Started Coding (Column C):**
   - The first row has a value of 0.
   - All remaining rows have a value of 1.

3. **Tested Code (Column E):**
   - The first row has a value of 0.
   - All remaining rows are filled with the value 1.

4. **Deployed Code (Column G):**
   - The first row has a value of 0.
   - All other cells contain the value 1.

5. **NumToClose? (Column H):**
   - The first row has a value of 0.
   - The rest have the value 1.

6. **ErrorsFoundInDeploy? (Column I):**
   - All rows have a value of 0.

7. **Closed Ticket (Column J):**
   - The first row has a value of 0, then increments by 1 for a few rows.
   - Starting from the fifth row, it remains constant at a value of 4 through the rest of the rows.

Columns B, D, and F are hidden. The table is organized, displaying a

<p class="img-desc i tc f6">DeployedCode, NumToClose?, and ErrorsFoundInDeploy? columns in spreadsheet model</p>

Finally, we can added the `Tested Code` to `Started Coding` flow.
This is pretty much the same as the prior flow we added,
starting with adding a `ErrorsFoundInTest?` calculation:

    // E3 is tested code
    // Config!$B$7 is the testing error rate
    =FLOOR(E3 * Config!$B$7)

Then we update `Tested Code` to reduce by this value:

    // E2 is prior value of Tested Code
    // D3 is NumToTest?
    // G2 is prior value of NumToDeploy?
    // F2 is prior value of ErrorsFoundInTest?
    =E2 + D3 - G2 - F2

And update `Started Coding` to increase by this value:

    // C2 is prior value of Started Coding
    // B3 is StartCodingMore?
    // D2 is prior value of NumToTest?
    // J2 is prior value of ErrorsFoundInDeploy?
    // F2 is prior value of ErrorsFoundInTest?
    = C2 + B3 - D2 + J2 + F2

Now this last flow is instrumented.

**Image Description:** The image is a screenshot of a spreadsheet with columns labeled from A to K, and rows numbered from 1 to 20. Here's a detailed breakdown:

### Column Headers:
- **A**: "Open Tickets"
- **B**: "StartCodingMore?"
- **C**: "Started Coding"
- **D**: "NumToTest?"
- **E**: "Tested Code"
- **F**: "ErrorsFoundInTest?"
- **H**: "Deployed Code"
- **K**: "Closed Ticket"

### Row Details:
- **Row 1** contains the headers.
- **Rows 2 to 20** contain integer values.

### Data Details:
- "Open Tickets" starts from 10 at row 2 and incrementally increases to 25 at row 20.
- Columns B, C, D, E, F, and H mostly contain binary values (0 or 1):
  - B: Starts with 0, then all 1s.
  - C, D, E, and H: All 1s.
  - F: All 0s.
- "Closed Ticket" in column K generally contains the value 4 from row 5 to 20, starting from 0 at row 2.

### Formatting:
- The spreadsheet has a simple, grid-like appearance with no additional formatting or colors highlighted.

<p class="img-desc i tc f6">Modeling ErrorsFoundInTest? in spreadsheet model</p>

With that, we now have a complete model that we can start exercising!
This exercise demonstrated both that it's _quite possible_ to represent
a meaningful model in a spreadsheet, but also the challenges of doing so.

While developing this model, a number of errors became evident. Some of them
I was able to fix relatively easily, and even more I left unfixed because fixing
them makes the model _even harder_ to reason about. This is a good example of why
I encourage developing one or two models in a spreadsheet, but I ultimately don't
believe it's the right mechanism to work in for most people:
even very smart people make errors in their spreadsheets, and catching those errors
is exceptionally challenging.

## Exercise

Now that we're done building this model, we can finally start the fun part: exercising it.
We'll start by creating a simple bar chart showing the size of each stock at each step.
We are going to expressly _not_ show the intermediate calculation columns such as `NumToTest?`,
because those are implementation details rather than particularly interesting.

Before we start tweaking the values , let's look at the baseline chart.

**Image Description:** The image is a line graph titled "Started Coding, Tested Code, Deployed Code and Closed Ticket." It displays data trends for five categories over an unspecified time period. 

- **Open Tickets (Blue Line):** Starts at around 11, remains constant, then increases continuously, reaching 25.
- **Started Coding (Red Line):** Starts at 0, sharply rises to 5, and remains constant.
- **Tested Code (Yellow Line):** Not visible, assumed to be 0 throughout.
- **Deployed Code (Green Line):** Starts and remains at 0.
- **Closed Ticket (Orange Line):** Starts at 0, sharply rises to 5, and remains constant.

The y-axis represents the number of tickets, ranging from 0 to 25. The x-axis probably represents time increments. The legend on the right indicates which color corresponds to each category.

<p class="img-desc i tc f6">Baseline chart where closed tickets quickly stops increasing</p>

The most interesting thing to notice is that our current model doesn't actually increase the number of closed
tickets over time. We actually just get further and further behind over time, which isn't too exciting.

So let's start modeling the first way that LLMs might help, reducing the error rate in production.
Let's shift `ErrorsInProd` from `0.25` down to `0.1`, and see how that impacts the chart.

**Image Description:** The image is a line graph titled "Started Coding, Tested Code, Deployed Code and Closed Ticket." It displays data for various stages of coding and ticket management over a period.

- **Axes**: The y-axis represents numerical values, ranging from 0 to 20. The x-axis is not labeled with specific time intervals or categories.

- **Legend**: There are five color-coded categories:
  - **Blue**: Open Tickets
  - **Red**: Started Coding
  - **Yellow**: Tested Code
  - **Green**: Deployed Code
  - **Orange**: Closed Ticket

- **Lines**:
  - The blue line for Open Tickets starts slightly above 10 and increases steadily.
  - The red line for Started Coding is not visible.
  - The yellow line for Tested Code is not visible.
  - The green line for Deployed Code is flat at a low level, starting just above zero and remaining constant.
  - The orange line for Closed Ticket starts at 0, increases linearly, and reaches 10, where it then remains constant.

The graph suggests a tracking of tickets and coding stages, with notable increases in open and closed tickets, while other stages remain constant or low.

<p class="img-desc i tc f6">Reduced error rates delays, but doesn't prevent, reaching equilibrium of closed tickets</p>

We can see that this allows us to make more progress on closing tickets, although
at some point equilibrium is established between closed tickets and the error rate in production,
preventing further progress. This does validate that reducing error rate in production matters.
It also suggests that as long as error rate is a function of everything we've previously shipped,
we are eventually in trouble.

Next let's experiment with the idea that LLMs allow us to test more quickly,
tripling `TicketTestRate` from `1` to `3`. It turns out, increasing testing rate doesn't change anything at all,
because the current constraint is in starting tickets.

**Image Description:** The image is a line graph titled "Started Coding, Tested Code, Deployed Code and Closed Ticket." It tracks multiple metrics over some time on the horizontal axis (not labeled with specific timeframes) and a range from 0 to 20 on the vertical axis representing the number of tickets or instances.

- There are five colored lines, each representing a different metric as indicated by the legend on the right:
  - **Blue Line (Open Tickets):** Starts at 10, remains constant, then slightly increases towards the end, reaching about 16.
  - **Red Line (Started Coding):** Starts and remains constant at 10.
  - **Yellow Line (Tested Code):** Not visible on the graph, possibly overlapped or missing.
  - **Green Line (Deployed Code):** Starts and remains constant at about 1 throughout the graph.
  - **Orange Line (Closed Ticket):** Starts from 0, rises sharply to 10, and remains constant.

The graph lacks labels for the horizontal axis, making it difficult to discern the specific timeframe for these activities.

<p class="img-desc i tc f6">Changing testing rate doesn't model's behavior</p>

So, let's test that. Maybe LLMs make us faster in starting tickets because _overall_ speed of development goes down.
Let's model that by increasing `StartCodingRate` from `1` to `3` as well.

**Image Description:** The image is a line graph titled "Started Coding, Tested Code, Deployed Code and Closed Ticket." It represents different stages in a development process with five color-coded lines:

1. **Open Tickets (Blue Line):** 
   - This line shows fluctuations between 10 and 15, indicating variability in the number of open tickets over time.

2. **Started Coding (Red Line):** 
   - Shows an up-and-down pattern, starting at 0, peaking slightly above 5, and fluctuating around that level.

3. **Tested Code (Yellow Line):**
   - This line remains at 0, indicating that no data points are available or recorded for tested code.

4. **Deployed Code (Green Line):**
   - A flat line at 0, similar to the Tested Code, indicating no deployments.

5. **Closed Ticket (Orange Line):**
   - Starts at 0 and rises steadily, maintaining around 5, showing an upward trend and stabilization over time.

The graph suggests open tickets are actively changing, while coding starts and closures vary more steadily, with no recorded progress in testing or deployment.

<p class="img-desc i tc f6">Starting or testing tickets faster creates noise but not progress</p>

This is a fascinating result, because tripling development and testing velocity has changed how much work we start,
but ultimately the real constraint in our system is the error discovery rate in production.

By exercising this model, we find an interesting result. To the extent that our error rate is a function of the volume
of things we've shipped in production, shipping faster doesn't increase our velocity at all.
The only meaningful way to increase productivity in this model is to reduce the error rate in production.

Models are imperfect representations of reality, but this one gives us a clear sense of what matters the most:
if we want to increase our velocity, we have to reduce the rate that we discover errors in production.
That might be reducing the error rate as implied in this model, or it might be ideas that exist outside of this model.
For example, the model doesn't represent this well, but perhaps we'd be better off iterating more on fewer things to avoid this scenario.
If we make multiple changes to one area, it still just represents one implemented feature, not many implemented features, and the overall error
rate wouldn't increase.