# Search and AI discoverability

RecallForge publishes a static [product guide and FAQ](https://dagerottdev.github.io/RecallForge/about.html), canonical URLs, descriptive titles, social preview metadata, factual WebApplication/FAQPage structured data, and a two-page sitemap. The guide is readable without JavaScript. The optional llms.txt file is a factual project index, not an OpenAI requirement or ranking signal guarantee.

The offline app remains a single HTML file with the same storage identifiers, consent boundaries and embedded samples. No search integration, AI API call or additional analytics is introduced.

## Crawling boundary

[OpenAI's crawler documentation](https://developers.openai.com/api/docs/bots) distinguishes OAI-SearchBot, which discovers content for ChatGPT search, from GPTBot, which concerns training. A training-policy change is not required for search discovery. Accessibility does not guarantee indexing, recommendations or ranking.

On 15 October 2026, the public app returned HTTP 200 with no X-Robots-Tag, and https://dagerottdev.github.io/robots.txt returned HTTP 404. No origin-root crawler exclusion was observed. A robots.txt under /RecallForge/ would not control this GitHub Pages origin, so this project does not publish a misleading project-level robots file. The owner must maintain any future origin-root policy separately. Actual OAI-SearchBot fetching and search inclusion have not been verified.

## Maintenance

Edit src/index.html, src/about.html, src/llms.txt and src/sitemap.xml, then run npm run build and npm run build:check. The build copies the public guide, shared stylesheet and approved logo into the Pages artifact alongside the offline viewer. CI deploys the whole distribution. Keep visible answers and FAQ structured data consistent; the deterministic discovery test checks that agreement. Do not add invented ratings, endorsements, usage statistics or search-placement promises.
