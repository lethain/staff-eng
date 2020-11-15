import React from "react"
import { graphql, useStaticQuery } from "gatsby"

import GuideLink from "../components/guidelink"

const RecentGuides = () => {
  const data = useStaticQuery(
    graphql`
      query {
        allMarkdownRemark(
          sort: { order: DESC, fields: [frontmatter___date] }
          filter: { frontmatter: { kind: { eq: "guide" } } }
          limit: 2
        ) {
          edges {
            node {
              id
              frontmatter {
                title
                slug
                date
              }
            }
          }
        }
      }
    `
  )
  const Guides = data.allMarkdownRemark.edges.map(edge => (
    <GuideLink post={edge.node} />
  ))
  return Guides
}

export default RecentGuides
