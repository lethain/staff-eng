import React from "react";
import { Link } from "gatsby";

const GuideLink = ({ post }) => (
  <li>
    <Link to={post.frontmatter.slug}>
      {post.frontmatter.chapter} - {post.frontmatter.title}
    </Link>
  </li>
);

export default GuideLink;
