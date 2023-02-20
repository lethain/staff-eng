import React from "react"
import { Helmet } from "react-helmet"

function PlausibleTag() {
    return <Helmet>
        <script defer data-domain="staffeng.com" src="https://plausible.io/js/script.js"/>
    </Helmet>
}

export default PlausibleTag
