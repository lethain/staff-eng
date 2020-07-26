import React from "react";
import { graphql } from "gatsby";

import Layout from "../components/layout";
import GuideChapter from "../components/guideChapter";
import SEO from "../components/seo";

const GuidesPage = (
  {
    data: {
      dataYaml: { chapters }
    }
  }
) => {
  const Chapters = chapters.map(chapter => <GuideChapter chapter={chapter} />);

  return (
    <Layout>
      <SEO title="Guides for reaching Staff-plus engineering roles - StaffEng" />
      <p>
        Guides for reaching and succeeding at Staff-plus roles.
        We'll fill these in over time, with the goal of providing
        a comprehensive resource for folks pursuing or operating
        in Staff-plus roles.
      </p>
      <ul>
        {Chapters}
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
}
`;
