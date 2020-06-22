import React from "react";
import { graphql } from "gatsby";

import Layout from "../components/layout";
import StoryLink from "../components/storylink";
import SEO from "../components/seo";

const StoriesPage = (
  {
    data: {
      allMarkdownRemark: { edges }
    }
  }
) => {
  const Stories = edges.map(edge => (
    <StoryLink slug={edge.node.id} post={edge.node} />
  ));

  return (
    <Layout>
      <SEO title="StaffEng Stories" />
      <p>
        Folks who have shared their stories of reaching Staff-plus engineer roles:
      </p>
      <ul>
        {Stories}
      </ul>
    </Layout>
  );
};

export default StoriesPage;

export const storyList = graphql`
query {
allMarkdownRemark(
  sort: {order: DESC, fields: [frontmatter___date]}
  filter: {frontmatter: {kind: {eq: "story"}}}

     
) {
  edges {
    node {
      id
      frontmatter {
        name
        role
        slug
        date
      }
    }
  }
}
}
`;
