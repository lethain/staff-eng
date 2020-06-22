import React from "react";
import { Link } from "gatsby";

const StoryLink = ({ post }) => (
  <li>
    <Link to={post.frontmatter.slug}>
      {post.frontmatter.name} - {post.frontmatter.role}
    </Link>
  </li>
);

const GuideLink = ({ post }) => (
  <li>
    <Link to={post.frontmatter.slug}>
      {post.frontmatter.chapter} - {post.frontmatter.title}
    </Link>
  </li>
);

export default StoryLink;
