import React from "react";
import { graphql } from "gatsby";

import Layout from "../components/layout";
import StoryLink from "../components/storylink";
import SEO from "../components/seo";

const IndexPage = (
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
      <SEO title="Home" />
      <p>
        At most technology companies, you'll reach Senior Software Engineer,
        the{" "}
        <a href="https://lethain.com/mailbag-beyond-career-level/">
          career level
        </a>
        ,

        in five to eight years. At that point your path branches, and you have the


        opportunity to pursue engineering management or continue down the path of


        technical excellence to become a Staff Engineer.
      </p>
      <p>
        Over the past few years we've seen a flurry of books unlocking the engineering manager


        career path, like Camille Fournier's

        <a
          href="https://www.amazon.com/Managers-Path-Leaders-Navigating-Growth/dp/1491973897"
        >
          The Manager's Path
        </a>
        ,

        Julie Zhuo's{" "}
        <a
          href="https://www.amazon.com/Making-Manager-What-Everyone-Looks/dp/0735219567/"
        >
          The Making of a Manager
        </a>

        and my own{" "}
        <a
          href="https://www.amazon.com/Elegant-Puzzle-Systems-Engineering-Management/dp/1732265186"
        >
          An Elegant Puzzle
        </a>
        .

        The management career isn't an easy one, but increasingly there is a map available.
      </p>

      <div class="pull">
        <p><strong>Recent stories</strong></p>
        <ul>
          {Stories}
        </ul>
      </div>
      <p>
        The transition into Staff Engineer, and its further evolutions
        like Principal Engineer,
        remains particularly challenging and undocumented. What are the
        skills you need to develop to reach Staff Engineer?

        What skills do you need to succeed <em>after</em> you've reached it?
        How do most folks reach this role? What can companies do to streamline
        the path to Staff Engineer?

        Will you{" "}<em>enjoy</em>{" "}
        being a Staff Engineer or toil for years for a role that
        doesn't suit you?
      </p>
      <p>
        The{" "}<strong>StaffEng</strong>{" "}
        project aims to collect the stories of folks who are operating in Staff,
        Principal or Distinguished Engineer roles. How did you get there?
        What were your lucky breaks?
        How did you learn to be effective? As more of these stories are collected,


        I hope to build a dataset
        that helps folks draw their own map to Staff Engineer.
      </p>
    </Layout>
  );
};

export default IndexPage;

export const stories = graphql`
query {
allMarkdownRemark(
  sort: {order: ASC, fields: [frontmatter___date]}
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
