import React from "react"
import Layout from "../components/layout"
import SEO from "../components/seo"

const SharePage = () => (
  <Layout>
    <SEO title="Share your StaffEng story" />
    <h3>Why collect stories?</h3>
    <p>
      There are so many different ways that folks reach Staff, Principal and
      Distinguished Engineer roles. As such, we often find that the best career
      advice for folks pursuing these roles{" "}
      <a href="https://lethain.com/share-stories-not-advice/">
        isn't advice at all
      </a>
      , but rather the stories of folks who've already done it. StaffEng
      collects folks' stories of reaching Staff-plus roles and succeeding once
      they're there.
    </p>

    <h3>Sharing your story</h3>

    <p>
      If you've reached a Staff-plus Engineer role, then we'd love to include
      your story in the collection. To share your story, please{" "}
      <a href="https://github.com/lethain/staff-eng/blob/master/src/markdown/drafts/template.md">
        create a copy of this template
      </a>{" "}
      and follow it's instructions.
    </p>
    <p>Before doing so, a few things to consider:</p>

    <ol>
      <li>
        Read some of the existing <a href="/stories">list of stories</a> to get
        a sense of what we're looking for.
      </li>
      <li>
        Review the{" "}
        <a href="https://creativecommons.org/licenses/by/4.0/">
          Creative Commons Attribution 4.0 License
        </a>
        . By submitting a story to StaffEng, you are agreeing to have it
        published under this license. If this isn't a license you're comfortable
        with, that's totally ok, but unfortunately we won't be including it on
        StaffEng.
      </li>
      <li>
        Your pull request should only include your story and any images you want
        to include in your story. It should not include any code changes to the
        site itself.
      </li>
      <li>
        After you submit your pull request, we'll review your story. If we
        believe your story would publish well as it stands, then we'll merge it.
        Otherwise we'll iterate together on the draft within the pull request.
      </li>
      <li>
        There is a small chance that we'll decline to add your story, primarily
        if it doesn't meet our requirements (Staff-plus title and five-plus
        years of experience), an overwhelmingly similar story already exists on
        StaffEng, or if it is in some way offensive.
      </li>
      <li>
        Once your story goes out, it will be sent to our mailing list the
        following morning, as well as shared on our RSS feed.
      </li>
    </ol>

    <p>
      This is all early. If you have suggestions for different questions, how
      the approach of the project can be improved, or what not, please send a note.
    </p>
  </Layout>
)

export default SharePage
