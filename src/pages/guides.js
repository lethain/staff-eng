import React from "react";
import { graphql } from "gatsby";

import Layout from "../components/layout";
import GuideChapter from "../components/guideChapter";
import GuideLink from "../components/guidelink";
import SEO from "../components/seo";

const GuidesPage = (
  {
    data: {
        allMarkdownRemark: { edges },
        dataYaml: { chapters }
    }
  }
) => {
    const Chapters = chapters.map(chapter => (
            <GuideChapter chapter={chapter} />
    ));
    
  const Guides = edges.map(edge => (
    <GuideLink slug={edge.node.id} post={edge.node} />
  ));
    console.log(chapters);

  return (
    <Layout>
      <SEO title="StaffEng Guides" />
      <p>
        Guides for reaching and succeeding at Staff-plus roles:
      </p>
          <ul>
          {Chapters}
      </ul>
      
      <ul>
        {Guides}
      </ul>         
    </Layout>
  );
};

export default GuidesPage;

export const storyList = graphql`
query {
dataYaml {
    id
    chapters {
      title
      sections {
        draft
        slug
        title
      }
    }
  }

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
