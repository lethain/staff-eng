import { Link } from "gatsby";
import PropTypes from "prop-types";
import React from "react";

const Header = ({ siteTitle }) => (
  <nav>
    <h2><a href="/">{siteTitle}</a></h2>
    <ul>
      <li><Link to="/">Stories</Link></li>
      <li><Link to="/share">Share your story</Link></li>
    </ul>
  </nav>
);

Header.propTypes = {
  siteTitle: PropTypes.string
};

Header.defaultProps = {
  siteTitle: ``
};

export default Header;
