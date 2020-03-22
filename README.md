# StaffEng

Repository of folks stories of reaching staff engineer level.

## Installation

Assuming you have Git and Python3 installed, installation should
be as simple as:

    git clone git@github.com:lethain/staff-eng.git
    cd staff-eng
    python3 -m virtualenv env
    . ./env/bin/activate
    pip install -r requirements.txt
    python src/app.py

## Working in the codebase

Stories and chapters are stored as Markdown files in `src/stories/*.md`
and `src/chapters/*.md` respectively. These are lazily cached after initial
load, so updates to the Markdown files requires a reload.
(Yes, I know this is jank.)

## Deployment

staffeng.com is automatically deployed whenever a commit is pushed to `master` branch,
and usually takes 2-5 minutes to update.
There are... no safeguards on it actually working though, but if it fails
you can just git a revert commit and push that to master and it'll recover.