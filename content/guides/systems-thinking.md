---
title: Introduction to systems thinking
url: /guides/systems-thinking
date: '2018-07-25'
weight: 95000
book_section: Resources
---

Many effective leaders I've worked with have the uncanny knack for working on [leveraged](https://lethain.com/building-technical-leverage/) problems. In some problem domains, the [product management skillset](https://lethain.com/intro-product-management/) is extraordinarily effective for identifying useful problems, but systems thinking is the most universally useful toolkit I've found.

If you really want a solid grasp on systems thinking fundamentals, you should read [Thinking in Systems: A Primer](https://www.amazon.com/Thinking-Systems-Donella-H-Meadows/dp/1603580557) by Donella Meadows, but I'll do my best to describe some of the basics and work through a recent scenario where I found the systems thinking approach to be exceptionally useful.

## Stocks and flows

The fundamental observation of systems thinking is that the links between events are often more subtle than they appear. We want to describe events causally--our managers are too busy because we're trying to ship our current project--but few events occur in a vacuum.

Big changes appear to happen in a moment, but if you look closely underneath the big change, there is usually
a slow accumulation of small changes.
In this example, perhaps the managers are busy because no one hired and trained the managers required to support this year's project deadlines. These accumulations are called _stocks_, and are the memory of changes over time. A stock might be the number of trained managers at your company.

Changes to stocks are called _flows_. These can be either _inflows_ or _outflows_. Training a new manager is an inflow, and a trained manager who departs the company is an outflow. Diagrams in this article represent flows with solid dark lines.

![System diagram for hiring and training new managers.](/static/systems/sys-loop-clouds.png)

The other relationship, represented in this article by a dashed line, is an _information link_. These indicate that the value of a stock is a factor in the size of a flow. Indicated in this diagram by a dashed line. The link here shows that the time available for developing features depends on the number of trained managers.

Often stocks outside of a diagrams scope will be represented as a cloud, indicating that there is something complex that happened there that we're not currently exploring. It's best practice to label every flow, and to keep in mind that every flow is a rate, whereas every stock is a quantity.


## Developer velocity

When I started thinking of a useful example of where systems thinking is useful, one came to mind immediately.
Since reading Forsgren's [Accelerate](https://lethain.com/accelerate-developer-productivity/) earlier this year, I've spent a lot of time pondering their definition of velocity.

They focus on four measures of developer velocity:

1. **Delivery lead time** is time from code being written to it being used in production.
1. **Deployment frequency** is how often you deploy code.
1. **Change fail rate** is how frequently changes fail.
1. **Time to restore service** is time spent recovering from defects.

The book uses surveys from tens of thousands of organizations to assess their
overall productivity and show how it correlates to their performance on those
four dimensions.

![System diagram for developer productivity.](/static/systems/dev-velocity-sys.png)

These kind of intuitively make sense as measures of productivity, but let's see if we can model these measures into a system we can use to reason about developer productivity:

* **_pull requests_** are converted into **ready commits** based on our _code review rate,_
* **ready commits** convert into **deployed commits** at _deploy rate,_
* **deployed commits** convert into **incidents** at _defect rate,_
* **incidents** are remediated into **reverted commits** at _recovery rate_,
* **reverted commits** are debugged into new **pull requests** at _debug rate_.

Linking these pieces together, we see a _feedback loop_, where the system's downstream behavior impacts its upstream behavior. With a sufficiently high _defect rate_ or slow _recovery rate_, you could easily see a world where each deploy leaves you even further behind.

If your model is a good one, opportunities for improvement should be immediately obvious, which I believe is true in this case. However, to truly identify where to invest, you need to identify the true values of these stocks and flows! For example, if you don't have a backlog of **ready commits**, then speeding up your _deploy rate_ may not be valuable. Likewise, if your _defect rate_ is very low, than reducing your _recovery time_ will have little impact on the system.

Creating an arena for quickly testing hypothesis about how things work, without having to do the underlying work beforehand, is the aspect of system thinking that I appreciate most.


## Model away

Once you start thinking about systems, you'll find it's hard to stop. Pretty much any difficult problem is worth trying to represent as a system, and even without numbers plugged in I find them powerful thinking aids.

If you do want the full experience, there are relatively few tools out there to support you. [Stella](https://www.iseesystems.com/) is the gold standard, but the price is quite steep, costing more than a new laptop for non-academic licenses. The best cheap alternative I've found is [InsightMaker](https://insightmaker.com/), which has some UI quirks but has a donation based payment model.
