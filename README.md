
This repository is a Gatsby script that is built into [staffeng.com](https://staffeng.com).
The built assets live in the `ghpage` branch.

## Submitting your story?

Read the instructions at [staffeng.com/share](https://staffeng.com/share),
but it's basically submitting a story to `src/markdown` in the same format
as the existing stories!
    

## Development

Install this somehow.


Then run:

    gatsby develop

Your site is now running at `http://localhost:8000`!

Run prettier before merging your code:

    npm install prettier

This project is using the default prettier settings, line length and all.
Personally, I'm using `prettier-js-mode` as [described here](https://patrickskiba.com/emacs/2019/09/07/emacs-for-react-dev.html).

##  Deploy

Roughly following [these instructions](https://www.gatsbyjs.org/docs/how-gatsby-works-with-github-pages/):

    npm install gh-pages --save-dev
    npm run deploy

Longer term I'd like to figure out how to get CI/CD setup using [Github Actions](https://help.github.com/en/actions/creating-actions)
and these [gatsby deploy instructions](https://www.gatsbyjs.org/docs/how-gatsby-works-with-github-pages/).
Or maybe [this github action](https://github.com/enriikke/gatsby-gh-pages-action)? Although I think that one assumes a different
branch structure, which is fine.