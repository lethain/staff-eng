---
title: "Silvia Botros - Senior Principal Engineer at Twilio Inc."
url: "/stories/silvia-botros"
date: "2020-04-23"
name: "Silvia Botros"
role: "Senior Principal Engineer at Twilio Inc."
weight: 38000
---

<span class="date fr">April, 2020</span>
[blog](https://blog.dbsmasher.com/),
[twitter](https://twitter.com/dbsmasher),
[linkedin](https://www.linkedin.com/in/silviabotros/)

**_Tell us a little about your current role: where do you work, your title and generally the sort of work do you and your team do._**

I work at Twilio and my title is Senior Principal Engineer. I’m part of the Architecture Team, one of the architects reporting to the Chief Architect. We’re also not the only architects at Twilio, typically every Business Unit is led by a General Manager and GMs have architects who report to them and are focused on their particular product.

I joined Twilio through the acquisition of SendGrid, and Twilio’s Chief Architect came forward from SendGrid as well, and formed this architecture team after the acquisition. Since our team is new we don’t have our goals or KPIs super formalized yet, some of our work is very hard to measure, but this is an area we’re thinking about, along with our longer-term vision.

Personally, I am focused on databases at large, and tend to jump around to help out with projects that touch our databases. My coworkers are in similar roles in different areas. Steve Kinney is the architect for frontend. Josh Barratt focuses on our platform, looking for commonalities across products that could be centralized in a useful way. We are what we call ‘horizontal’ architects, working along the specific product architects.

**_What do typical Staff-plus engineers do at Twilio?_**

Twilio doesn’t actually have a Staff Engineer title, for us it goes from Senior Engineer to Principal Engineer. “What do Principal Engineers do?” is a fascinating question. Before the acquisition there was a big effort to align titles between SendGrid and Twilio, and while we did do that, some of the underlying parts still haven’t coalesced entirely, and maybe they’ll never totally align depending on the Business Unit and product.

There’s always going to be details of the role that vary wildly depending on what you’re specifically doing. For example, Twilio has already bifurcated the role, where you can either be a Principal who spends most of your time writing software or an Architect who focuses more on strategy and less on coding.

<div class="pull">
<p><strong>More from and about Silvia</strong></p>
<ul>
<li><a href="https://blog.dbsmasher.com/2019/01/28/on-being-a-principal-engineer.html">On Being A Principal Engineer</a></li>
<li><a href="https://www.arresteddevops.com/principal-engineer/">Principal Engineering with Silvia Botros on Arrested DevOps</a></li>
<li><a href="https://www.learningfromincidents.io/blog/teaching-the-smell">Teaching "the smell"</a></li>
<li><a href="https://blog.dbsmasher.com/2020/04/08/high-performance-mysql.html">High Performance MySQL</a></li>
</ul>
</div>

**_How do you spend your time day-to-day?_**

For me specifically, it's a lot of being on Slack and email to answer questions, along with tons and tons of Google documents. The documents I collaborate on will vary from strategy plans to blueprints. I also spend a lot of time reading other people’s documents. If someone is testing a new tool and writes up their findings, I’ll review that. If someone is writing a proposal that changes how we deliver software or how to tackle a new and emerging business need, I will review that and provide feedback.

I don’t do coding for the business anymore. I think the last time I had to pull up my terminal it was to refactor my dot files. This is an intentional decision by my boss, the Chief Architect. He’ll check in with us every quarter to make sure we didn’t contribute any code that goes into production. Part of that is his vision for the architect role, and another part of that is purely related to classifying our work for the Finance organization.

Our philosophy is that our job isn’t to do the code, but to help others do it with growth and the long-term in mind.

**_One of the challenges I've seen as people stop writing software is they lose empathy for how things actually work on the ground. How do you maintain that awareness if you aren't frequently writing software?_**

I spend a lot of time maintaining empathy. If I have an empty slot between meetings I’ll look through the rooms in Slack to see what issues are cropping up. I’ll also reach out to folks and have one-on-ones to understand their pain points. It’s a challenge and I’m not entirely sure how I’ll be able to keep up with it long-term.

We did an engineering survey before the acquisition and also recently the Platform Group did one for a team offsite. We got feedback on how to provision infrastructure, deploying changes to production, CI/CD, and so on. The thing that always surprises me is that we’ll often have an existing solution but a lot of people within engineering won’t know it exists. This means the baseline isn’t always getting feedback to improve the tool, but instead it’s getting folks to know it exists at all.

Similarly, I also find that I need to spend time explaining the glue work required to integrate vendors and tools effectively into our infrastructure. Sometimes it can seem like you just install a new enterprise tool and it all works, and folks will propose dropping in a new tool because an existing one has some issues, but there’s a lot of hidden work to do that. The current tool might not be great, but it’s probably one of the better ones and we’ve probably already spent a lot of time making it work as well as it does.

**_Where do you feel most impactful as a Staff-plus engineer?_**

Often the most impactful things I do is convince someone not to write a new thing. I often find myself asking people, “Why are you doing that?”, genuinely asking to understand how they got here and try to steer them towards an existing solution.

I joined SendGrid back when it was roughly thirty engineers, maybe sixty in the whole company. We grew to about five hundred before we got acquired by Twilio, and I’ve watched over that period how the overhead of communication costs have increased, and noticed that they’re often underinvested in relative to our technical systems. Some of my most impactful work is noticing similar approaches across groups and facilitating communication so they don’t find themselves running almost identical systems in a year.

**_Can you think of anything you’ve done as a Staff-plus engineer that you weren’t able to or wouldn’t have done before reaching that title?_**

This was less noticeable when I reached Principal Engineer, but it’s definitely the case as a Senior Principal Engineer. We consider Senior Principals to be at the Director level, and that’s not just a verbal acknowledgement but also getting included in certain private email groups, being invited to performance calibration meetings, and so on. Calibration meetings are particularly important, because you can bring feedback that might not otherwise surface in a room of managers.

My opinion is more respected with the title. I don’t subscribe to the idea that titles don’t matter. I think only a certain demographic gets to say that, and that’s not my demographic.

**_Do you spend time advocating for technology, practice, process or architectural change?_**

I spend a lot of my time advocating for technology and architecture decisions. If it were up to me, yeah, I’d love to specify the one or two patterns for all applications to access the database, but it doesn’t really work out that way. There is always a team that has a business case that doesn’t work with what you thought was a reasonable solution for everyone. There will always be a prioritization conversation where you make imperfect tradeoffs.

Once you reach the Principal and Senior Principal level, you start getting into the room for the prioritization and dependency meetings, and you see the long list of other projects on the roadmap for the teams you’re asking to make changes. The obvious decisions aren’t so obvious after that.

There’s a misconception that as an architect you’re a manager without reports and can simply tell people what to do, but no, it means that you’re exposed to the full details of the sausage making and that makes things much more complex. In some ways, I’ve had it relatively easy because I’ve had a specific focus on databases most of my entire time at SendGrid and now at Twilio. Compared to databases, the business side’s complexity is much larger, and their decisions carry more complex consequences.

Early on, I also had the unfair advantage of being the only full-time employee working on databases, because the only other people working on databases for a long time at SendGrid were contractors. This made it easy for me to make a bunch of decisions around database architecture. Now my challenge is having influence at a much larger and more complex org with a lot more stakeholders and no direct impact on the code.

**_How have you sponsored other engineers? Is sponsoring other engineers an important aspect of your role?_**

I don’t think that sponsoring others is specifically called out in my role because I don’t have direct reports, but I do some strategic sponsorship work. For example, I pushed to expand our database team and pushed to make sure we hired a diverse team.

Since then, my contributions have been things like bringing my voice to calibration meetings, particularly around raising visibility around how bias can impact underrepresented people. This is the sort of work you can’t do until you’re in the room, which is why becoming Principal has been important.

**_You first got the title Principal engineer at Sendgrid. What was the process of getting promoted to Principal?_**

I got the Principal title at SendGrid and then 18 months later I got the Senior Principal title. The move to Senior Principal technically happened after the Twilio acquisition, but the performance cycle was still using the SendGrid system since we hadn’t fully integrated HR processes yet at that point. So take this as a disclaimer that i did not get through a promotion process at Twilio :)

For the first promotion, I had to get heavily involved, document all my work, and then show how it matched with the career development framework we had. Although, really my work started even earlier! Early on at SendGrid we didn’t even have a career ladder defined, and I grabbed Camille Fournier’s career ladder for [Rent the Runway](https://dresscode.renttherunway.com/blog/ladder), and used that to get the Senior Engineer title.

Going back to the Principal Engineer promotion, I put the materials together myself and gave that to my manager. I was expecting to do the same thing for the Senior Principal promotion, but actually I didn’t do anything that time. I had a new manager and he surprised me: he’d already been talking with the Chief Architect about the promotion because I would report to the Chief Architect if the promotion went through, and it all happened without me preparing anything.

What I learned from that is that it’s really a function of who the people are and the circumstances they’re in. My manager when I went from Senior to Principal was incredibly oversubscribed. He had something like twenty direct reports and he was doing all these projects in addition to managing the team.

But later, having a manager who was invested in my progress, advocated for me and worked with the right people to make the case for promoting me to Senior Principal meant all the difference in how and when it happened.

**_What two or three factors were most important in you reaching Staff?_**

 Writing and speaking externally helped, as did joining early so I know where all the bodies are in the infrastructure and the code. I wrote my first blog post more than five years ago, not with a clear goal but more because we were doing all this cool stuff and I thought people would find it interesting. It definitely wasn’t to get a promotion, but it snowballed from there.

My first blog post got noticed by Baron Schwartz, who’s pretty well known in the database community, and he reached out for me to create a case study with his new company. Then I became more involved in the emerging database community, and from that I got to do a couple of conference speaking slots. All of this built into more visibility for me and my work.

**_Do you feel that it’s important to continue speaking and writing in public? Or have you already established your credibility and don’t feel the need to do more?_**

I don’t think of it this way, it’s more that if I’m passionate about something then I really enjoy speaking and writing about it. I’ve spoken at about three conferences and stepped back a bit since it’s logistically difficult with younger children. I might get back into speaking more in a few years.

I have found that I prefer blog posts more than speaking. I’ve done some writing on company blogs, but most of my writing has been on my personal blog. Often I’ll have a strong opinion and it might be one that the company doesn’t share, so I’ve found that’s easier.

My blog post that’s gotten the most traction was [On Being A Principal Engineer](https://blog.dbsmasher.com/2019/01/28/on-being-a-principal-engineer.html), which I’m still having people reach out about frequently.

**_There is a popular idea that becoming a Staff engineer requires completing a “Staff Project.” Did you have a Staff Project, and if so what was it?_**

I don't know if other engineers who are trying to get to Principal have had explicit “Staff Projects” where they had to complete this specific project to get promoted, but I did not have one. Most of my promotions have come from work that I’ve been doing for many months and we can see the results.

**_Can you remember any piece of advice on reaching Staff that was particularly helpful for you?_**

The most valuable advice I got is that it’s not always about being right. If you roll back five or six years ago, I was bad at this. I would dig in when I felt I was right. It didn’t matter to me if there was a business deliverable or something was burning, I would still try to stop someone from taking approaches I disagreed with. I wouldn’t take the time to understand the alternatives or the product priorities that were creating tension with doing the right thing.

Eventually our former VP of Engineering gave me feedback on this. He was kind of Yoda-like, a man of few words, but when he said something you would listen. When he started at SendGrid, I was incredibly burned out and jaded, getting increasingly frustrated as the product grew. I was five years into the job and felt like people kept throwing problems over the wall for me to deal with.

He helped me turn that around, helped me understand what the product teams were having to deal with, why their concerns mattered, and how to use my knowledge to help them get to the right tradeoff instead of being antagonistic.  He was incredibly helpful, and this advice changed my career.

**_What about a piece of advice for someone who is trying to reach Staff engineer?_**

The advice I’d give is so different for every company, it would even vary a lot between SendGrid and Twilio. You have to understand “what does Staff mean?” for your company, and to realize that you might not like it when you find it. That doesn’t necessarily mean you have to change your company, like when I had to bring in Rent the Runway’s career ladder to establish the idea of having a career ladder.

It took the company a while to make that change, but ultimately leadership also saw why the change was necessary and it happened. But you’ve got to go into it with eyes wide open, it can be a long haul if your view of the job is not aligned with the company. Be aware it may never align and moving on might become the only path.

On the other hand, if I was giving advice to someone who had just started as a Staff Engineer, I’d tell them to not to focus so much on the code and to be prepared not to write nearly as much code as they’re used to. Instead focus on getting to know the people and the business as well as you can. Your job now is not to be the producer of the value, your job is to be the force multiplier that helps everyone around you deliver better, more sustainable, products. And it is not a job you can measure in points or sprints. It is a job with quarters and even years of ROI.

**_Did you ever consider engineering management, and if so how did you decide to pursue the staff engineer path?_**

I was offered the opportunity to move into engineering management around the time when I reached Senior Engineer. You hear a lot of stories where women are told to go into management because they have social skills. I was super opposed to making the switch, and I’m grateful I wasn’t pushed into it. I also think at the time I would have been a terrible micromanager. I was hyper aware of what damage I could do to other people’s careers if I made that move without being fully ready to take its emotional toll.

Granted, now in my current role I do a ton of manager things, but it’s a completely different mindset than operating as a people manager.

**_What are some resources (books, blogs, people, etc) you’ve learned from? Who are your role models in the field?_**

Definitely Camille Fournier’s book, [The Manager’s Path](https://www.amazon.com/dp/B06XP3GJ7F/). Shortly after I read her book, I also read Dr. Nicole Forsgren’s [Accelerate](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations-ebook/dp/B07B9F83WM/), which I like because it connects what we do in software with business impact. I still nerd out on the [DORA report](https://cloud.google.com/devops) every year.

Most of the books out there are about how to write code as a senior engineer and don’t reflect the kind of work I do. For these roles that are about doing more than turning out code, the details for doing that role still don’t exist. I keep saying that I wish there was a counterpart to _The Manager’s Path_ for engineers in roles like mine.

**_How did you build out your network of other Principals? Was it something that happened organically or was it more deliberate?_**

My network of Principals really all started with that one blog post, [On Being A Principal Engineer](https://blog.dbsmasher.com/2019/01/28/on-being-a-principal-engineer.html). After I wrote that, I got invited to all these private Slacks and got to meet a bunch of people. Part of that was timing, as it was around the time that everyone was out there creating a hundred new Slacks for everything. I don’t travel very much, so this was really what worked for me.