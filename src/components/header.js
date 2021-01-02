import { useStaticQuery, graphql, Link } from "gatsby"
import PropTypes from "prop-types"
import React from "react"

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
  )

  return (
    <div>
      <img src="/banner.png" alt="StaffEng Banner" />
      <nav>
        <h2>
          <a href="/">{siteTitle}</a>
        </h2>
        <ul>
          <li>
            <Link to="/stories">Stories</Link>
          </li>
          <li>
            <Link to="/guides">Guides</Link>
          </li>
          <li>
            <a
              href={data.site.siteMetadata.mailingListURL}
              rel="noreferrer"
              target={"_blank"}
            >
              Subscribe
            </a>
          </li>
          <li>
            <Link to="/book">Book</Link>
          </li>	    
        </ul>
      </nav>
    </div>
  )
}

Header.propTypes = {
  siteTitle: PropTypes.string,
}

Header.defaultProps = {
  siteTitle: `StaffEng`,
}

export default Header
