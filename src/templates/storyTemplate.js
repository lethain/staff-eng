import React from "react"
import { graphql } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

export default function Template({
  data, // this prop will be injected by the GraphQL query below.
}) {
  const { markdownRemark } = data // data.markdownRemark holds your post data
  const { frontmatter, html } = markdownRemark
  if (frontmatter.kind == "guide") {
    return (
      <Layout>
        <SEO title={frontmatter.title} content="article" />
        <h4 className="quiet">
          <a href={"/guides"}>Guides</a>
          {" / "}
          <a href={frontmatter.slug}>{frontmatter.title}</a>
        </h4>
        <div
          className="blog-post-content"
          dangerouslySetInnerHTML={{ __html: html }}
        />
        <p class="center">
          <em>
            <a href="/guides">Read another guide?</a>
          </em>{" "}
          or{" "}
          <em>
            <a href="/stories">Back to the stories?</a>
          </em>
        </p>
      </Layout>
    )
  } else if (frontmatter.kind == "story") {
    return (
      <Layout>
        <SEO
          title={frontmatter.name + " - " + frontmatter.role}
          content="article"
        />
        <h2 className="lead">{frontmatter.name}</h2>
        <h4 className="quiet">{frontmatter.role}</h4>
        <div
          className="blog-post-content"
          dangerouslySetInnerHTML={{ __html: html }}
        />
        <p class="center">
          <em>
            <a href="/stories">Ready to read another story?</a>
          </em>
        </p>
      </Layout>
    )
  } else {
    return (
      <Layout>
        <SEO title={frontmatter.title} />
        <div
          className="blog-post-content"
          dangerouslySetInnerHTML={{ __html: html }}
        />
      </Layout>
    )
  }
}

export const pageQuery = graphql`
  query($slug: String!) {
    markdownRemark(frontmatter: { slug: { eq: $slug } }) {
      html
      frontmatter {
        date(formatString: "MMMM DD, YYYY")
        slug
        name
        role
        kind
        title
      }
    }
  }
`
