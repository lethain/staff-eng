module.exports = {
  siteMetadata: {
    title: `StaffEng`,
    description: `Stories of folks reaching Staff Engineer roles.`,
    content: "website",
    author: `@lethain`,
    mailingListURL: (
      `https://lethain.us20.list-manage.com/subscribe/post?u=f7003ed301623a88fab7cf783&amp;id=9c7b745cce`
    ),
    siteUrl: `https://staffeng.com`,
    image: `https://staffeng.com/StaffEngSocialShare.jpg`,
  },
    plugins: [
        `gatsby-plugin-sitemap`,
	`gatsby-plugin-preload-fonts`,
        `gatsby-transformer-yaml`,
        {
            resolve: `gatsby-source-filesystem`,
            options: {
                path: `./src/data/`,

            }
        },
	{
	    resolve: 'gatsby-plugin-robots-txt',
	    options: {
		policy: [{ userAgent: '*', allow: '/' }]
	    }
	},
    {
      resolve: `gatsby-plugin-feed`,
      options: {
        query: `
          {
            site {
              siteMetadata {
                title
                description
                siteUrl
                site_url: siteUrl
              }
            }
          }
        `,
        feeds: [
          {
            serialize: ({ query: { site, allMarkdownRemark } }) => {
              return allMarkdownRemark.edges.map(edge => {
                return Object.assign({}, edge.node.frontmatter, {
                    description: edge.node.html,
                  date: edge.node.frontmatter.date,
                  url: site.siteMetadata.siteUrl + edge.node.frontmatter.slug,
                  guid: site.siteMetadata.siteUrl + edge.node.frontmatter.slug,
                  custom_elements: [{ "content:encoded": edge.node.html }]
                });
              });
            },
            query: (
              `
              {
                allMarkdownRemark(
                  sort: { order: DESC, fields: [frontmatter___date] },
                  filter: {frontmatter: {kind: {eq: "story"}}}
                ) {
                  edges {
                    node {
                      excerpt
                      html
                      frontmatter {
                        slug
                        title
                        date
                      }
                    }
                  }
                }
              }
            `
            ),
            output: "/rss",
            title: "StaffEng RSS"
          }
        ]
      }
    },
    `gatsby-plugin-react-helmet`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `images`,
        path: `${__dirname}/src/images`
      }
    },
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        path: `${__dirname}/src/markdown`,
        name: `markdown`
      }
    },
    `gatsby-transformer-remark`,
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `gatsby-starter-default`,
        short_name: `starter`,
        start_url: `/`,
        background_color: `#663399`,
        theme_color: `#663399`,
        display: `minimal-ui`,
        icon: `src/images/favicon-32x32.png`
      }
    }
    // this (optional) plugin enables Progressive Web App + Offline functionality
    // To learn more, visit: https://gatsby.dev/offline
    // `gatsby-plugin-offline`,
  ]
};
