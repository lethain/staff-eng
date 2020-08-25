/**
 * Layout component that queries for data
 * with Gatsby's useStaticQuery component
 *
 * See: https://www.gatsbyjs.org/docs/use-static-query/
 */

import React from "react";
import PropTypes from "prop-types";
import { useStaticQuery, graphql, Link } from "gatsby";

import Header from "./header";
import MailingList from "./mailinglist";
import "../styles/normalize.css";
import "../styles/milligram.css";
import "../styles/base2.css";

const Layout = ({ children }) => {
  const data = useStaticQuery(
    graphql`
    query SiteTitleQuery {
      site {
        siteMetadata {
          title
          mailingListURL
        }
      }
    }
  `
  );

  return (
    <div className="core">
      <Header siteTitle={data.site.siteMetadata.title} />
      <div className="content">
        <section>{children}</section>
        <MailingList url={data.site.siteMetadata.mailingListURL} />
      </div>
      <footer>
        ©{" "}
        <a href="https://lethain.com">Will Larson</a>
        ,{" "}
        {new Date().getFullYear()}.
        {` `}
        <Link to="/about">About</Link>.
        {` `}
        <Link to="/rss">RSS</Link>.
	{` `}
        <a href="https://github.com/lethain/staff-eng">Edit on GitHub</a>.
      </footer>
    </div>
  );
};

Layout.propTypes = {
  children: PropTypes.node.isRequired
};

export default Layout;
