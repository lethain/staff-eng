import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const AboutPage = () => (
  <Layout>
    <SEO title="About StaffEng" />
    <p>
      <em>
        Questions? Reach out to{" "}
        <a href="https://twitter.com/lethain">@lethain</a> on twitter.
      </em>
    </p>

    <h3>Why?</h3>

    <p>
      At most technology companies, you'll reach Senior Software Engineer, the{" "}
      <a href="https://lethain.com/mailbag-beyond-career-level/">
        career level
      </a>
      , in five to eight years. At that point your path branches, and you have
      the opportunity to pursue engineering management or continue down the path
      of technical excellence to become a Staff Engineer.
    </p>
    <p>
      Over the past few years we've seen a flurry of books unlocking the
      engineering manager career path, like Camille Fournier's
      <a href="https://www.amazon.com/Managers-Path-Leaders-Navigating-Growth/dp/1491973897">
        The Manager's Path
      </a>
      , Julie Zhuo's{" "}
      <a href="https://www.amazon.com/Making-Manager-What-Everyone-Looks/dp/0735219567/">
        The Making of a Manager
      </a>{" "}
      and my own{" "}
      <a href="https://www.amazon.com/Elegant-Puzzle-Systems-Engineering-Management/dp/1732265186">
        An Elegant Puzzle
      </a>
      . The management career isn't an easy one, but increasingly there is a map
      available.
    </p>
    <p>
      The transition into Staff Engineer, and its further evolutions like
      Principal Engineer, remains particularly challenging and undocumented.
      What are the skills you need to develop to reach Staff Engineer? What
      skills do you need to succeed <em>after</em> you've reached it? How do
      most folks reach this role? What can companies do to streamline the path
      to Staff Engineer? Will you <em>enjoy</em> being a Staff Engineer or toil
      for years for a role that doesn't suit you?
    </p>
    <h3>What?</h3>
    <p>
      The <strong>StaffEng</strong> project aims to collect the stories of folks
      who are operating in Staff, Principal or Distinguished Engineer roles. How
      did you get there? What were your lucky breaks? How did you learn to be
      effective?
    </p>
    <p>
      These stories will establish role models for folks hoping to become Staff
      Engineers. Further, the "metadata" around these stories will help create
      transparency into the most effective ways to navigate this career path.
    </p>
    <p>
      Finally, I hope to use those learnings to craft a small number of
      resources to help others draft their own map to Staff Engineer. What
      should you do in the first ninety days as a Staff Engineer? What are the
      highest leverage activities? What should you stop doing? What are the
      resources you can rely upon? Hopefully we can provide good resources for
      all of this.
    </p>

    <h3>Who am I?</h3>
    <p>
      I'm <a href="https://linkedin.com/in/will-larson-a44b543">Will Larson</a>,
      also known as <Link to="https://twitter.com/Lethain">@lethain</Link> on
      Twitter. I serve as CTO at <a href="https://calm.com">Calm</a>, blog at{" "}
      <a href="https://lethain.com">Irrational Exuberance</a>, and wrote{" "}
      <a href="https://www.amazon.com/Elegant-Puzzle-Systems-Engineering-Management/dp/1732265186">
        An Elegant Puzzle
      </a>
      .
    </p>
    <p>
      I've been fortunate to work with and coach a number of wonderful
      Staff-plus engineers, but I've always been a bit uncertain whether my
      advice was any good. I knew what I thought I needed from the team I was
      supporting, but was my approach effective? Was I helping their careers or
      guiding them towards submerged rocks that I couldn't quite see?
    </p>
    <p>
      This project came out of the desire to have a clearer understanding of the
      Staff-plus role, to ensure organizations I work with or support create
      room for those roles, and to make me a better coach to the Staff-plus
      engineers I'm fortunate enough to work with.
    </p>
    <p>
      Somewhat orthogonally, I also really enjoyed the pull arc of publishing{" "}
      <a href="https://www.amazon.com/Elegant-Puzzle-Systems-Engineering-Management/dp/1732265186">
        An Elegant Puzzle
      </a>
      , and wanted to start on a new project that could eventually lead to
      another book while addressing some of the areas I felt my first work could
      have been better in. Particularly, a more cohesive structure and moving
      beyond my own experiences to operate through a broader lens.
    </p>

    <h3>Want to help?</h3>
    <p>
      The best ways to help are <a href="/share">sharing your story</a> or
      simply sharing these stories out to folks who would benefit from them.
    </p>
    <p>
      When I started working on this project, I wrote up some notes on how I'd
      determine this project's success, and a big part of that is the number of
      folks who reach out to say that these stories have helped them. If they've
      helped you, please let me know on Twitter at{" "}
      <a href="https://twitter.com/Lethain">@lethain</a>, or via email at
      lethain[at]gmail.
    </p>
  </Layout>
)

export default AboutPage
