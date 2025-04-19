# drafting-strategy


# Repomix

   ./scripts/llm.py
   repomix --style markdown --remove-empty-lines --include "llm/*.md" -o files/draftingstrategy_llm.md


# Scripts

    python3 -mvenv ./env
    . ./env/bin/activate
    pip install -r requirements.txt


## Copy Script

    ./scripts/import.py


1. Copy over all files from a specified repository
2. Load translate.yaml file
3. Translate slugs across them
4. Rewrite links to either go to lethain.com/ or to the new slugs on draftingstrategy.com
4. Identify static assets to copy over, and rewrite the paths
4. Rewrite the "this is a draft book" divs too
2. Move the current slug into 