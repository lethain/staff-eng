---
title: "Amy Unger - Principal Engineer at Heroku/Salesforce"
name: "Amy Unger"
role: "Formerly Principal Engineer at Heroku/Salesforce"
slug: "/drafts/template"
date: "2020-07-15"
kind: "draft"
---

### Checklist for submitting your staff eng story

1. If you have questions, please review this template at `src/markdown/drafts/template.md` and [the Share page](/share/) first.
    At that point, it's best to ask them in your pull request, and
    you're also welcome to email `lethain@gmail.com` with questions.
2. Make a copy of this template and put it into `src/markdown/stories/firstname-lastname.md`.
3. Within your copy, please delete `omit: true` from the top of the 
4. Please add your story as a standalone pull request. Please do
    not make template or other changes within the that pull request.
5. Dont' worry about the date. We'll select a date based on
    when we complete editing.
6. The slug should be `/stories/firstname-lastname`
7. You're welcome to change any of the questions, including
    adding your own questions or removing some.
8. You're welcome to inline images by creating a sub directory
    of your firstname-lastname within `static/` and then including
    any images there. Please do not add any non-image content
    such as JavaScript, etc.
9. Update the profile links at the top of the template (e.g. `[blog](...)`
    to point to whatever resources you prefer. This can be your Twitter, blog,
    Instagram, YouTube, etc.
10. Note that by submitting your story, you're agreeing to the
    [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).
    If you are not comfortable with this license, we understand but unfortunately won't be
    able to host your story at this time.

Checklist ends here!

---

<span class="date">July, 2020</span>
[twitter](https://twitter.com/cdwort),
[linkedin](https://www.linkedin.com/in/amy-unger-9a07b59b/)


**_Tell us a little about your current role: where do you work, your title and generally the sort of work do you and your team do._**

Until recently, I was a Principal engineer at Salesforce, working for their Heroku acquisition. I joined almost five years ago, working on the Heroku Add-ons product, and then transferred to the API team. For the last year and a half, I worked on the API team for the Salesforce Functions product, which runs on top of Heroku infrastructure.

The API team is at the center of defining how the Salesforce Functions product will work, so there are a lot of different tasks our team does. First and foremost, we write the code to store the state that the customer *intends* their infrastructure to converge to and then push that down into the infrastructure layer. If you're interacting with Salesforce Functions, you're going through our code. We also do a lot of reconciling what the infrastructure can do with the hopes and dreams of product. I did a balance of work, but more towards the latter end of the spectrum. 

**_What does a “normal” Staff-plus engineer do at your company? Does your role look that way or does it differ?_**

There is really no "normal" Staff engineer at Salesforce. I usually talk about four different approaches I see in the company, some of which line up with Will's archetypes and some which don't. A lot of folks are a mix of these and rotate through them over a long career. 

Team(s) Lead/Right Hand
You are the primary technical point of contact for 10-20 engineers, across one or more teams. You are typically reporting to a manager of managers. Responsibilities vary based on individuals' strengths and the strengths of their manager, but there are some common things you *must* do. If you're not making your delivery timelines and this is a surprise to your organization, you and your manager have a problem. If product has a dream and no one knows what it would take to build it (time, resources, architecture), you have a problem. If you can't answer "Why are we building this in this way?" then you have a problem.

Product Architect
If it's on TechCrunch or promoted at our corporate conferences, there is an Architect for it. If the project (40+ engineers) fails to be a success, you share responsibility along with the (typically) VP+ engineering manager and Product owner. If you have any type of personal presence, you will be put on a stage and in front of customers. This is the level where you're helping advocate with your VP for major initiatives to go after certain markets. If we made the wrong bet, some blame is with product, but it's also on you, and the manager probably won't look great.

Deep Diver
You have a lot of deep technical expertise on a particular component or system. You tend to stay on a single team or a single area of the organization. If you work in our legacy codebases, which are the core of our profitability, you are basically unfireable because you know so much. You may write code for some of the gnarliest problems of the legacy system you're being kept around for, but you'll often find yourself spending more time interfacing with other teams to explain why your system can't do what they want and how we can work around it to deliver on a reasonable timeline. You will work closely with your Team Lead on a daily/weekly basis and occasionally have your entire day/week blown up because the Product Architect has identified a need for your expertise and all of a sudden you're being trotted out to present to some team you've never heard of.

The Management
There are two variants. First, you're pendulum'ing over to a line manager role, but since your IC title is the same grade as Director or VP, making you a manager would result in a massive pay cut. You're likely managing a smaller team, given Salesforce targets 12-15 reports. In the second variant, you're roughly an extension of a VP+ leader. Maybe you're working on how we keep our many thousands of engineers communicating well. Maybe you're advising an SVP on where to make technical investments - does our company really have enough of a competitive advantage to go after that market? Sure, the SVP/C-suite person is being told by Product that if you only give us $100 million we can do a ton. Is that true? Hey, we just bought a multi-billion dollar business (or we're about to): Can you figure out what we should do with them? Many, including Will, call this fire-fighting, but that's too narrow a view of how these roles really deliver value to large companies: it's fast-paced opportunity scouting and truth-telling. That being said, you'll most likely be looking for opportunities and the real truth within the more challenged parts of the business, so I see the fire-fighting analogy.

**_How do you define success in your role?_**

First, I am successful if the folks I work with understand how business decisions tie into their day-to-day work. Translating down, championing up. Risk, embracing being wrong. 

What does that look like?

Conversations about code, when to build the right abstraction. Conversations about timeline and priorities between ICs start from a shared background -- there's no major blow ups about "this is a hack", instead "we're currently low on staff compared to our product ambitions, but is this the right place to simplify?" We're all on the same page about the quality and resiliency of code that we're writing. Other ICs feel confident advocating for changes in direction since they see our team making technical decisions with a consistent goal in mind. When I talk with ICs in 1:1s, there's no "I'm not sure why I'm doing X" when it comes to code, infrastructure and incidents. "I don't know why Product is asking us to do X" isn't an out for me. 

Second, I am successful if I'm aligned with my manager *and* course correcting.

Finally, I'm successful if my organization has a healthy engineering culture.

No one person owns culture, but that doesn't mean we all don't equally share the burden of building a world-class engineering organization. 


**_How do you spend your time day-to-day?_**

I spend my time split between the four following functions.

*Information gathering* - In order to help my team understand the context within which we're building a thing, I need a lot of information. I almost unfailingly start my day with a list of longer emails and docs of all varieties to digest. I also spend a fair amount of time in cross-org chats with assorted managers & ICs, whose purpose is a combination of information gathering and the coaching I mention below. 

*Planning* - Knowing a bunch of stuff isn't helpful unless we actually do something with it, so I also spend a lot of time in planning activities. This is a lot of writing docs and running meetings. Planning activities are usually very collaborative -- I rarely know the most on any one thing, but I can knit them all together into a plan.

*Context sharing* - Knowing what we want to do isn't helpful unless a lot of people understand the plan, so the final category of work that's execution oriented is sharing all that context. I attending meetings with other teams to share what we are doing, I review PRs to make sure we're making small decisions in-line with larger goals, and hold standing team 1:1s to make sure each person feels confident in the direction we're headed. 

*Coaching & Culture* - The final category of work isn't oriented towards delivering a product, but it's still critically important to our organization's long-term health to invest in our engineers. My personal approach is far more on invest in people not process. Given how much I love calendars and spreadsheets in my personal life, I'd say this approach is very much a reaction to working primarily in large corporate environments which can be a little dehumanizing. I spend a fair amount of time in 1:1s, doing some mentoring of juniors but mostly focusing on coaching our senior engineers who actually have fewer opportunities for advice. Every once in a while, I'll dip my toes into our formal processes, as I did in helping reformat our VAT team after our ~120 person org merged in closer to Salesforce.

I also end up being the RACI enforcer for external folks coming into our team slack channels, PRs and doc comment threads. For managers with fewer reports, it maybe possible to keep up with all that on the daily. I have a lighter meeting load and can jump in with variants of "Thanks for that opinion, we'll keep that in mind. My understanding is that your team doesn't share responsibility for that decision." I confidently trade on my manager's authority in ways my teammates may struggle with. Because of my time and my deeper involvement in the technical details being discussed, it is my responsibility to step in and deescalate if a technical conversation is starting to circle the drain. Most times I can resolve it, very rarely I need to pull in my manager or skip-level in between their meetings to help navigate some strange cross team dynamic that is resulting in someone unintentionally being a bit of an ass to our ICs. This means that most of the small moments in between meetings (and during the more boring ones) are filled with cycling through tab upon tab of docs, PRs and threads, watching how communication is going today.


**_Do you spend time advocating for technology, practice, process or architectural change? What’s something you’ve advocated for? Can you share a story of influencing your organization?_**

As someone who's role is directly tied to execution, architectural change is my responsibility. Team members may be the ones pushing for it, but my role is where the rubber meets the road in terms of finding out how to move forward. Who needs to sign off. 

I have advocated for technology changes and process changes as I see fit, but those are more occasional passion projects than things I feel fall directly under my responsibilities as someone who most closely fit's Will's "Team Lead" archetype.

**_How do you keep in touch with how things really work as you spend less time on hands-on development?_**

This is something I struggle with and has been my goal for the year to work on. I'm starting with saying "I don't know" or "I'm not sure, let me check" a lot more. 

**_How have you sponsored other engineers? Is sponsoring other engineers an important aspect of your role?_**

Yes. Everybody wants to hire senior engineers, nobody wants to make them. That's eff'ed up. Technical communication backup. Watch from the shadows. Get people in meetings, just add them so they can see how conversations happen. And then give them a project. 

Sponsorship is a key way to resolve the problem of loss of time. You can get so underwater that you don't actually have the time to coach & mentor enough to get someone to the point where you can sponsor them for a something that takes it off your plate. Investing early in sponsorship starts opening your eyes to delegation in a healthy way that's not just dumping something on someone.

**_How do you build a network at a remote company?_**

Reach out after meetings. Meet and greet. Tell me your story. Who should I talk to? Get over it being weird. Stay quiet.

Provide information and value. Lend your network -- listen to what someone is doing/challenges and share context about why they might be seeing that. As you get more and more established at an organization, you may find it's easier and easier. "Oh, that's because so-and-so hates this acquisition". Beware of that state though -- you're likely leaning heavily on notions of your organization that are year(s) out of date. Really, really invest in new folks as a counterbalance. 

If you're new, really bring your outside perspective as a bonus. Try to find the most experienced person who will still speak honestly with you. This often involves going higher ranks than you might expect. 

**_You first got the title Staff Engineer at your current company. Were you hired as a Staff Engineer? If not, what was the process of getting promoted to Staff?_**

Staff doesn't map neatly to any one rank at Salesforce. My current role is on paper the same level as a Director, but we have a ton more Principals than we do Directors. I got my current promotion because I was the tech lead on an important project and then we had a change in Product owner. I had great support from my people manager, but people management doesn't always mean technical management and certainly doesn't mean product management. As the remaining source of engineering and product context, my role grew and I advocated for a promotion. 

**_What two or three factors were most important in you reaching Staff? How have the companies you joined, your location, or your education impacted your path?_**

* Business awareness - as a staff engineer, you are a part of the company's leadership. You need to have some awareness of why the company is making the choices it is so that you can better contextualize those decisions for those that you're working with. 
* Cross team connections - pulse on the org, opportunities to fix problems small and large for the business. Tell me the story of X org, X project. Tell me the story of my project.
* Writing - making a point, knowing when to push on something, when you're getting a little too logical, what to drop.


**_Can you remember any piece of advice on reaching Staff that was particularly helpful for you?_**

Making Staff doesn't happen if you get run out of tech.

The specifics are a little too grim for a public piece like this, but I got a lot of advice on how to stay in tech as a URM. Things have gotten better, but they're not great. I was lucky enough to get some really strong guidance on how to keep quiet and smile through all sorts of things to protect my career. I give more nuanced advice these days than the advice I got, mostly because I worry the strong advice I got perpetuates a limited view of what being a woman in tech can be. But, lordy, there are absolutely days when I am thankful for the strong dose of reality I got early in my career and I wonder if it might be better to scare the heck out of folks coming in so they have a few years to prepare themselves for when things can get tough.

**_What about a piece of advice for someone who has just started as a Staff Engineer?_**

Everybody looks different! Figure out your leadership style. You're a leader, so you have one. Read some management books.

<div class="pull">
<p><strong>Some of YOURNAME's writing</strong></p>
<ul>
<li><a href="#">A blog post or something</a></li>
<li><a href="#">A blog post or something</a></li>
<li><a href="#">A blog post or something</a></li>
</ul>
</div>
