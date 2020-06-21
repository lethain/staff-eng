import React from "react";
import { Link } from "gatsby";

const StoryLink = ({ post }) => (
  <li>
    <Link to={post.frontmatter.slug}>
      {post.frontmatter.title}
    </Link>
  </li>
);

export default StoryLink;
