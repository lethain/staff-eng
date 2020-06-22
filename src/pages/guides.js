import React from "react";
import { graphql } from "gatsby";

import Layout from "../components/layout";
import GuideLink from "../components/guidelink";
import SEO from "../components/seo";

const GuidesPage = (
  {
    data: {
      allMarkdownRemark: { edges }
    }
  }
) => {
  const Guides = edges.map(edge => (
    <GuideLink slug={edge.node.id} post={edge.node} />
  ));

  return (
    <Layout>
      <SEO title="StaffEng Guides" />
      <p>
          Guides for reaching and succeeding at Staff-plus roles:
      </p>
      <ul>
        {Guides}
      </ul>
    </Layout>
  );
};

export default GuidesPage;

export const storyList = graphql`
query {
allMarkdownRemark(
  sort: {order: DESC, fields: [frontmatter___date]}
  filter: {frontmatter: {kind: {eq: "guide"}}}
     
) {
  edges {
    node {
      id
      frontmatter {
        title
        chapter
        slug
        date
      }
    }
  }
}
}
`;
