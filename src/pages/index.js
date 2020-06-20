import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import Image from "../components/image"
import SEO from "../components/seo"

const IndexPage = () => (
  <Layout>
        <SEO title="Home" />
<p>
  At most technology companies, you'll reach Senior Software Engineer,
  the <a href="https://lethain.com/mailbag-beyond-career-level/">career level</a>,
  in five to eight years. At that point your path branches, and you have the
  opportunity to pursue engineering management or continue down the path of
  technical excellence to become a Staff Engineer.
</p>
<p>
  Over the past few years we've seen a flurry of books unlocking the engineering manager
  career path, like Camille Fournier's
  <a href="https://www.amazon.com/Managers-Path-Leaders-Navigating-Growth/dp/1491973897">The Manager's Path</a>,
  Julie Zhuo's <a href="https://www.amazon.com/Making-Manager-What-Everyone-Looks/dp/0735219567/">The Making of a Manager</a>
  and my own <a href="https://www.amazon.com/Elegant-Puzzle-Systems-Engineering-Management/dp/1732265186">An Elegant Puzzle</a>.
  The management career isn't an easy one, but increasingly there is a map available.
</p>
  </Layout>
)

export default IndexPage
