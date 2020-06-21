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
    <div class="core">
      <Header siteTitle={data.site.siteMetadata.title} />
      <div class="content">
        <section>{children}</section>
        <MailingList url={data.site.siteMetadata.mailingListURL} />
      </div>
      <footer>
        ©{" "}
        <Link to="/https://lethain.com">Will Larson</Link>
        ,{" "}
        {new Date().getFullYear()}
        .

        {` `}
        <Link to="/about">About.</Link>
        {` `}
        <Link to="/rss">RSS.</Link>
      </footer>
    </div>
  );
};

Layout.propTypes = {
  children: PropTypes.node.isRequired
};

export default Layout;
