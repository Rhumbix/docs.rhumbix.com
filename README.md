# docs.rhumbix.com

Where documentation for Rhumbix's Public API is posted.

## Getting Started

1) Make sure you have the `rmbx_django` repo already.
2) Clone this repository up a directory from `rmbx_django`. This step is not required. However, it does make it easier on you because the deploy script will infer certain things based on a structure like this:
```
/home --- /dev -+- /rmbx_django
                |- /docs.rhumbx.com
```

## Deployment

1) Render all swagger files - there is a completely separate document on how do use this here: https://goo.gl/mhVA6r
2) Run the `deploy-public` shell script. It does the following:
   * Cleans the rendered swagger to remove anything that doesn't need to be publicly visible
   * Discovers what environment (dev, rc, hf, prod) and what version this is
   * Creates any necessary folders and files for the docs and updates the applicable index.html, if necessary
   * Prints the git status for review before running git add, commit, push.