import React from "react"

const GuideChapter = ({ chapter }) => {
  const Sections = chapter.sections.map(section => {
    if (section.slug) {
      return (
        <li key={section.title}>
          <a href={"/guides/" + section.slug}>{section.title}</a>
        </li>
      )
    } else if (section.draft) {
      return (
        <li key={section.title}>
          {section.title}{" "}
          <a href={section.draft} target={" _blank"}>
            DRAFT
          </a>
        </li>
      )
    } else {
      return <li key={section.title}>{section.title}</li>
    }
  })

  return (
    <li key={chapter.title}>
      <a name={chapter.title} />
      <strong>{chapter.title}</strong>
      <ol>{Sections}</ol>
    </li>
  )
}

export default GuideChapter
