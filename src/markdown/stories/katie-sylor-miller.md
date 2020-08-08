---
title: "Katie Sylor-Miller - Frontend Architect at Etsy"
name: "Katie Sylor-Miller"
role: "Frontend Architect at Etsy"
slug: "/stories/katie-sylor-miller"
date: "2020-08-09"
kind: "story"
---

<span class="date">August, 2020</span>
[website](https://sylormiller.com/),
[linkedin](https://www.linkedin.com/in/ksylor/),
[twitter](https://twitter.com/ksylor)

**_Tell us a little about your current role: where do you work, your title and generally the sort of work do you and your team do._**

I work at Etsy, which is the world's leading online marketplace for sellers of handmade goods. We let sellers put their items up for sale and sell them to folks all around the world. We really focus on providing people with unique, special or handmade goods that are an alternative to kind of the facelessness of big box stores.

I'm currently on the Frontend Systems team, which is a product infrastructure team that’s responsible for our frontend architecture - including our PHP view rendering framework, although I'm not super actively participating in the work that the team is doing right now. For the last several months I’ve been focusing on web performance - functioning in an advisory capacity for all things performance - improving our monitoring and reporting systems, identifying areas for improvement, and being available to product teams for help with performance related questions.

Web Performance is something that I think many companies either ignore or don’t focus on. When I started at Etsy, we had a great performance culture thanks to folks like Lara Hogan, but due to organizational changes a few years ago, we no longer had a web performance team, and I think that as an organization, we rested on our laurels and deprioritized web performance. Now, we’re bringing it back to the forefront because there have been a lot of changes in the industry around how “good” performance is defined and measured, particularly for SEO. Google is really pushing for web performance being a criteria that companies focus on as part of their search ranking. So it’s very much a top of mind area, especially for retailers.

**_What does a “normal” Staff-plus engineer do at your company? Does your role look that way or does it differ?_**

The interesting thing to me about how we think about the role of a “staff engineer” is that we take two different ways that a person can be senior and we put all of those people into one bucket called staff engineer. But really, there are two different buckets.

Someone can become really senior in their role by being an expert in a particular subject area, by really taking on the role of tech lead, where they are driving their team or org’s technical approach and roadmap. Then there's this other way to be a senior engineer, which are the folks who broaden their scope of work and their focus such that they're thinking about problems that are cross cutting, they're driving the creation of systems and practices that operate across multiple teams. That second bucket is what I think of as an architect. It’s not that you aren't a subject matter expert, but it's just that the scope of influence that you have is greater than operating as a tech lead for a particular team.

At Etsy we have a few levels of seniority: Senior Engineer I and II, then Staff I and II, then Senior Staff which is considered equivalent to a Director level role. I'm technically a Staff Engineer II, and that’s how I think of myself, but my specific role is as the frontend architect. That means instead of being responsible for just what my team is doing, I’m responsible for looking at what all of Etsy is doing in the frontend space. What does the future look like? What are the problems we need to solve? How are we going to get there? I think about all that, and advocate for the technical approaches that will get us there at the company level.

**_In your role as an architect, do you spend much time doing software development?_**

Yeah, it's funny. I’m a frontend architect, but by far the main thing I've been writing lately is SQL, because I'm doing a lot of data analysis. I’ve been looking at our performance metrics to figure out where the areas for improvement are, and what would be the most impactful issues to fix to improve performance and business metrics. I will write little bits of JS or PHP here and there, but it's mostly to help unblock teams or to run small performance-related experiments, or if there is something important that needs to be done but other folks don’t have time for.

I’ve definitely found that I'm moving slower, and it's taking me longer to actually find the dedicated focus time to write code as my calendar fills up with meetings. So I don't think you want me to write much code anymore! I’m much more focused on identifying areas for opportunity and then trying to sell that as work that my team or other teams should be doing.

**_How do you spend your time day-to-day?_**

I would say 50% meetings, and the rest of the time it varies pretty widely from day to day. Sometimes I spend the other 50% writing docs, sometimes I'm in SQL doing a lot of data analysis, sometimes I'm in slack talking to people across multiple teams and roles. At times my meeting load will spike a bit as projects come into my lap where I'm reaching out to other teams to learn more about what they're working on, or trying to influence them to make changes. It varies pretty widely.

**_I’ve found that folks in these roles often struggle to quantify their work, have you found any useful ways to measure your impact?_**

I'm glad to hear that because it is something that I really, really struggle with. I always have a bunch of different projects and discussions happening at any given time, and I have a bad tendency to get caught up in the newest thing or let my focus wander, so I have to be really thoughtful and cognizant about how I organize my work and my notes. I'm always looking at everything that I could potentially be doing and picking what is the most impactful or the most important thing for me to do that day, and that can be really hard.

I didn't realize, until I moved into the architect role, how much I relied on sprints and JIRA boards and the ritual of completing a ticket and moving it to the “done” column as a way to check in with myself and know that I am accomplishing the things that I need to accomplish. Now that I don’t have that kind of team context to help me organize my day, I've had to rely much more on my own to-do lists and I’m still working to improve my systems for that.

One thing that has definitely been helpful is making sure that I’m keeping track of all of the different tasks I complete every day - logging meetings, emails, slack discussions, etc. Then, when I have my official quarterly goals check-in with my manager, I review all of my notes and realize, wow, I helped engineers fix performance issues on six different experiments, or I influenced this team to take a better direction with their new feature, or I gave that engineer feedback that helped them. These are all little things that in the moment don’t feel like much, but taken together show real impact.

**_Where do you feel most impactful as a Staff-plus Engineer?_**

What I absolutely love to do the most is to identify a new or unique problem that hasn’t been tackled before, come up with a wild idea to solve the problem, and then my brilliant coworkers take that idea and really run with it to build something awesome. It starts with taking in a ton of input from the work folks are doing - seeing that this team has a problem doing x, and another team has a problem doing y. Then you mix all that input up with your experience and what’s happening in the industry as a whole and let it sit in your brain for a while, until finally it all clicks and you realize that the deeper cause underlying both problems is z, so you come up with a plan to fix that problem which is really hard to fix.

An example of this process from before I moved into the Architect role was when my team owned our Design System components. Making changes or fixing issues with our shared components was really difficult because we didn't have a single source of truth for the markup and the templates for each component. Rather than everyone in the company reusing the same template file, folks were copying and pasting the HTML into a bunch of different places. So when we had to make changes to a component, it was hard to find all the places to update because the pieces of the component were spread out and managed in different places - sometimes in JavaScript, sometimes in Mustache, sometimes in PHP logic.

So I had this wild idea: what if we extended our custom PHP framework to enable reusable template blocks in mustache that represented all of our components, and we were able to easily compose them together the way that you would in a React application. I went out and made a proof of concept and wrote up a proposal for the project and brought that to the team. Then the team really took the ball and ran with it, they built the infrastructure to support this component system and it turned out far better and more robust than anything I could have done on my own.

The part that I really enjoyed was identifying the problem and thinking creatively about how we can solve it, then shopping the proposal around and getting other people engaged with the work to execute it.

**_Can people doing frontend work create leverage for a company similarly to folks in developer productivity or infrastructure roles?_**

Yes, most definitely. I personally only know a handful of other Frontend-specific staff engineers, and I think that frontend as a skillset is not valued in the industry as much as I think that it should be. I'm very lucky that I got my foot in the door at a place like Etsy, which tends to hire “full stack” engineers, by having computer science fundamentals in my background - I went to school for Computer Science, and I have experience working in and understanding the whole stack. But really, my passion and my focus has always been the frontend because it’s what’s in front of your users. I'd love to see more companies value the frontend, because I believe we bring valuable skills and a unique way of thinking to the table.

As far as becoming a staff engineer, I think that the qualities of a good Staff Engineer transcend what stack you're working in. Ultimately, staff engineers need to be able to think about engineering decisions as a series of tradeoffs, and articulating those tradeoffs is a skill that you can have from any perspective within the stack.

I also think that Staff Engineers should have a broad understanding of all of the adjacent fields of work to their own specialty. For me, working in the frontend, I put a lot of time and effort into understanding marketing, business goals, user experience, visual design, the view and business logic layers on the server, how we ship code the browser, how browsers take all that code and turn it into a website, and then how users interact with it. Having expertise in all of these different areas makes it easier for me to see the broader impact of my technical decisions and understand those tradeoffs better.

Having empathy for your users, in particular, is an important skill for all types of engineers to develop, and I think it can be undervalued in many infrastructure or developer support orgs that don’t understand that yes, they actually do have users! I work in Frontend Infrastructure, and we really try to see ourselves as product engineers - it’s just that the products we're building are systems for other engineers to use. So we have customers. We have users. When we think about the API for the systems that we build, we're designing our APIs for users, and we need to understand our users - aka product engineers - to do that well.

So I personally think that frontend-leaning folks make great Staff Engineers, because they're so used to constantly thinking about users and how users are going to interact with what they build. User empathy is a superpower that frontend people bring to the table.

**_How do you maintain empathy and awareness of the realities of developing at your company when you do less development yourself?_**

Networking, networking, networking, networking. One-on-ones are particularly important because I'm a full-time remote. Obviously, everyone's remote right now, but as a remote on a not-completely-distributed team, you have to be really cognizant of who you're talking to, and make sure that you have connections across multiple teams and multiple groups to leverage those networks.

At Etsy, we are really lucky that we have a few different Employee Resource Groups for folks to connect across the company. I’m fairly active in the ERG for marginalized gender identities in tech (MAGIC), and it's great because there are folks who are part of that community who work in every single department in engineering. The same is true with the community of remote employees. I make time to mentor more junior folks, have regular 1:1’s, and participate in slack discussions to foster and grow these connections, because it helps so much to have a finger on the pulse of what’s happening broadly in the org. I also try to make sure that I'm talking to engineers throughout product engineering in particular, because product engineers are our customer base.

Something I'm working on getting better about is connecting a lot more with managers. For a long time I've had really good networks inside the Individual Contributor track and I've been working a lot in the last few months on broadening the reach of my network to include more engineering managers. A lot of times the work that I do requires “influence without authority”, I’m not making the decisions myself, but trying to influence the decisions that others are making, and a lot of times, managers are the ones who make the final decisions on things.

**_How have you sponsored other engineers? Is sponsoring other engineers an important aspect of your role?_**

I was very lucky to work with Laura Hogan for a few years at Etsy and she's talked a ton about sponsorship and as a woman in tech I've benefited from and seen the value of sponsorship myself. I definitely put a lot of time and energy into that.

About a year and a half ago, my colleague Andy Yaco-Mink, another Staff Engineer, and I noticed there wasn’t really a good method of communication for product teams to share what they are working on with each other, or to connect with teams working on product infrastructure. To try and fix that, we proposed and started up a monthly meeting that we call the Product Engineering Confab. It’s an open forum for folks to bring up questions, share their work, celebrate wins, and for us folks in infra to share what we’re working on.

Something that I don’t think we fully anticipated is that it's also been a really great way to create opportunities for sponsorship . Every month Andy and I have to figure out what folks are doing that would be interesting to share more broadly. What are experiments that have run that have gotten interesting results? Who’s out there doing cool stuff that should be shared? Then we’ll reach out to engineers on those teams and say, “You should come and talk about what you've been working on at the confab!” It's really easy. It's five minutes. It's super informal, but it's a good way to get public speaking experience.

Since then, we've had a couple of folks who've come and spoken at the meeting, and then went on to speak at company all-hands meetings or local meetups. At least one person ended up giving an expanded version of their talk at a big conference. We’ve also heard from folks that giving a talk at the confab was something they used as evidence of leadership in their promotion packet, which is an amazing feeling!

**_You first got the title Staff Engineer at your current company. What was the process of getting promoted to Staff?_**

I was hired as a Senior Engineer because at the time we didn’t hire into the Staff title, although we’ve since changed that policy. I was working in the industry for almost ten years before I joined Etsy, but largely at smaller and lesser known companies. I’d been serving as a frontend tech lead for more than five years before I came to Etsy. Because of that, I was already extremely comfortable in the role of being a mentor and a leader. I’d already spent a lot of time working closely with management, product and design, as well as figuring out roadmaps and execution. Altogether, I felt like I had the tech lead role down pat.

But, when I came to Etsy the scope was much bigger than what I’d seen previously. The engineering department was many magnitudes bigger than any engineering department I’d worked at before. I had a lot to learn about operating at a really big scale and how that’s very different than when you’re at a smaller company. I learned to be more cognizant of looking at data: I had to go out and teach myself basic statistics to understand the experimentation framework.

From the beginning, though, I was always looking around for places we could improve. I came in and said, “Oh hey, we’re not doing this thing. We should be doing this thing.” For example, I noticed that folks had been writing the design system JavaScript components any old way, so I said “Let’s come up with a framework and a standard boilerplate for that.” It was such a small thing and it felt obvious to me, but it was a big improvement in our practices. I think a lot of what gets someone to Staff is noticing problems and acting on solving them proactively, instead of letting them go.

Altogether, I had been at Etsy for a little less than two years when the promotion to Staff came. My manager at the time was brand new and didn’t know my track record, so we worked really closely and collaboratively on putting together my packet. I’ve heard experiences on both ends of the spectrum of manager-driven versus IC-driven, and I’m glad that I ended up being a big part of the promotion process. Especially being a remote, I think that unless you’re proactive a lot of your work can go unnoticed because it happens over Slack, in pull requests or documents, and not out in the open where managers tend to operate. You’re always going to be your best advocate, but that’s even more true as a remote. You have to put a lot of effort into making sure your accomplishments are out there and they’re known.

**_What two or three factors were most important in you reaching Staff? How have the companies you joined, your location, or your education impacted your path?_**

I’ve discussed a few things in this vein already: creativity, proactiveness, empathy, etc. Something I haven’t talked about enough is communication and transparency. A big part of being promoted to Staff is making sure that your work is visible, that people know your name and you have a good reputation.

I’m lucky to be on a team that builds frontend infrastructure because we naturally write a lot of emails to everyone in engineering about the work we do, so we get a lot of visibility. But a bigger part of being in infrastructure is customer service - helping folks who come into your Slack channel with questions or issues to be solved. I worked in the service industry for several years before going back to school to finish my degree in computer science, and I always try to model the lessons I learned about customer service from that experience in every interaction I have with folks at work: be available, be humble, and focus on really hearing and understanding people’s needs. When you truly care about helping our colleagues it shows.

**Do you think some companies are particularly good at growing Staff engineers?**

To be perfectly honest, I don’t really know how Staff engineering works at companies other than Etsy, so I am totally biased! I think Etsy is good at growing Staff Engineers because we have a strong internal culture that values technical excellence combined with a culture of blamelessness and a desire to do good in the larger world. I think that leads to really smart and kind people working at Etsy, and that combination of intelligence and humbleness makes folks great staff engineers. This kind of environment feeds on itself, creating good role models and people who want to emulate those role models in order to get promoted. So I think that on the whole, we have a great cohort of folks who work or have worked at Etsy and model good practices for Staff Engineers.

I think it’s important to remember, though, that there are lots of smaller and less-well-known companies with amazing people who do Staff engineering type work, but aren’t called staff engineers, they’re acknowledged as technical-track leaders in other ways. In many companies people who are strong technical leads become managers, and might not even have the idea of something like a Staff engineer role. It’s easy in a big name company to get stuck on this title of Staff as the end-all be-all, but remember that there are as many different ways of growing your career.

**_Can you remember any piece of advice on reaching Staff that was particularly helpful for you?_**

One of the best pieces of advice that someone gave me, and that I make sure to pass on to other staff engineers, is that there's a misconception that you become a Staff Engineer and then you’ll be in control of the work you do, and everyone will listen to you and do what you want them to do. That's absolutely the opposite of what happens! You have this really tangible goal of getting a promotion for so long, and then you become a Staff Engineer, and all of a sudden, everything is vague and ambiguous. You transition from solving somewhat clear-cut problems, to being responsible for finding the right problems, and then figuring out how to convince people that it’s important to solve them. You are going to be challenged in a completely different way than you have been in your career thus far.

**_What’s your advice to people pursuing a Staff role?_**

I was nominated for the Staff Engineer promotion twice before I got promoted; the third time was the charm. I think what finally pushed it forward for me was that I had a good sponsor in my Director. So my advice is to make sure that you develop your network and start meeting with your Director or your VP, because those are the people who are in the room making the decision about whether you’re getting promoted or not. It’s not your peers and it’s not really your manager, it’s this other group of people, so you want them to know your name and your work. During that promotion discussion, you want them to think, “Oh, she sent that engineering-wide email about this project.” or “I see him in Slack answering people’s questions all the time.” or “They spoke at that conference, didn’t they?”

When folks, particularly women and non-binary people, come to me for advice, I think they expect me to talk about how to grow as a technical leader, and are surprised when I say “You’ve probably already got the technical chops, what you need to do is work on your reputation at the company.” For better or for worse, you can’t get to Staff without a good reputation. I think people want or expect it to be a meritocracy, when it’s really not. There are so many factors that go into getting a Staff-level role.

**_Advice for navigating uncertainty and ambiguity that comes with more senior roles?_**

It’s important to develop a lot of self-knowledge to see when you’re pursuing something because it’s what you want and not because it’s going to be beneficial for the organization. That can be really hard to do. You have to be ready to kill your darlings, pivot, and try something new. If an approach you’re taking doesn’t work, don’t try to force it.

I also really love [Dan Na’s talk about pushing through friction](https://blog.danielna.com/talks/pushing-through-friction/), because that’s something you experience constantly when you’re growing as a technical leader. I think about this concept of “influence without authority” a lot, because when you’re a Staff Engineer then your job is to figure out what the team or organization needs to do, align the organization around that goal, and figure out how to get people to do that when you have no authority over staffing or final decision making. It takes a lot of tenacity and you have to flex a whole bunch of quote-unquote non technical skills to push things forward.

**_What are some resources (books, blogs, people, etc) you’ve learned from? Who are your role models in the field?_**

A lot of names that I’ve already said, especially [Lara Hogan](https://larahogan.me/), [Daniel Na](https://danielna.com/). I just love everything that [Julia Evans](https://jvns.ca/) does and I am really lucky that I got to collaborate with her on a project. [Ryn Daniels](https://www.ryn.works/) who used to work at Etsy blogs a lot on career progression. [Tanya Reilly](https://noidea.dog/) is a big inspiration to me as another badass working Mom who is also a respected technical leader. In the frontend space, [Nicole Sullivan](http://www.stubbornella.org/content/), [Jen Simmons](https://jensimmons.com/), and [Ethan Marcotte ](https://ethanmarcotte.com/)are huge inspirations to me to name just a few. I really enjoyed reading Camille Fournier’s [The Manager’s Path](https://www.amazon.com/dp/B06XP3GJ7F/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1). I’ve never done the management track so it was a bit of a black box and anything that gives you insight into the world of management is helpful because as a Staff Engineer you’re  almost like a manager without the people aspect.
