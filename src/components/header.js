
import { useStaticQuery, graphql, Link } from "gatsby";
import PropTypes from "prop-types";
import React from "react";

const Header = ({ siteTitle }) => {
  const data = useStaticQuery(
    graphql`
    query MailingListQuery {
      site {
        siteMetadata {
          mailingListURL
        }
      }
    }
`
  );
    
    return (
  <nav>
    <h2><a href="/">{siteTitle}</a></h2>
    <ul>
      <li><Link to="/stories">Stories</Link></li>
        <li><Link to="/share">Share your story</Link></li>
        <li><a href={data.site.siteMetadata.mailingListURL}>Subscribe</a></li>
    </ul>
            </nav>
    )
};

Header.propTypes = {
  siteTitle: PropTypes.string
};

Header.defaultProps = {
  siteTitle: ``
};

export default Header;
