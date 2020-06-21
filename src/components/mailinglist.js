import PropTypes from "prop-types";
import React from "react";

const MailingList = ({ url }) => (
  <div class="pull" id="mc_embed_signup">
    <form
      action={url}
      method="post"
      id="mc-embedded-subscribe-form"
      name="mc-embedded-subscribe-form"
      className="validate form-inline"
      target="_blank"
      noValidate
    >
      <div id="mc_embed_signup_scroll">
        <div className="mc-field-group">
          <p>
            <strong>
              Would you like an email when new stories are posted?
            </strong>
          </p>
          <div className="form-group">
            <label htmlFor={"mce-EMAIL"}>Email</label>
            <input
              type="email"
              value=""
              placeholder="your email address"
              name="EMAIL"
              className="required email"
              id={"mce-EMAIL"}
            />
            <input
              type="submit"
              value="Subscribe"
              name="subscribe"
              id="mc-embedded-subscribe"
              className="button"
            />
          </div>
        </div>
        <div
          style={{ position: "absolute", left: "-5000px" }}
          aria-hidden="true"
        >
          <input
            type="text"
            name="b_f7003ed301623a88fab7cf783_5d17ea270b"
            tabindex="-1"
            value=""
          />
        </div>
      </div>
    </form>
  </div>
);

MailingList.propTypes = {
  url: PropTypes.string
};

MailingList.defaultProps = {
  url: ``
};

export default MailingList;
