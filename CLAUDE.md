# marcossousa.de (repo portfolio-website)

Personal site of Marcos Sousa (Gewerbe: Marcos Sousa Software- und KI-Entwicklung).

This file is the home of the site's standing rules. Decisions made while working in this repo are recorded here, with their date. They are not mirrored anywhere else. Seeded 03.11.2026 from the decisions of 02.11.2026.

Work is tracked as GitHub issues in this repo, one issue per deliverable. Task briefings arrive in the session. They are not committed. If a briefing conflicts with this file, stop and ask.

## Hosting

Netlify, deployed on push to `main`. No build step.

## Footprint

- Hand-written static HTML and CSS. `/writing/` is the pattern for new pages.
- System font stack. No web fonts, remote or self-hosted.
- No client-side analytics, trackers or cookies. Netlify's server-side Web Analytics stays as configured in the Netlify dashboard; nothing else measures visits. (03.11.2026)
- No theme toggle. No photo.
- No external resources: no third-party scripts, embeds, fonts, form endpoints or Netlify Functions. Each one changes the Datenschutzerklärung and Marcos's provider list, so none is added to solve a task. Stop and ask.
- Keep it small. The result matters, not the machinery.

## Readers

Non-technical SME decision-makers first. Whoever lands on the site reads, in non-technical terms, what Marcos could do for them. Technical readers find the depth in `/portfolio/<slug>/` and `/writing/`.

## Language

- German: homepage, `/portfolio/` cards, campaign pages, Impressum, Datenschutzerklärung, and the navigation on every page.
- English: `/portfolio/<slug>/` pages and `/writing/`.
- Links in the page content from a German page to an English page are marked „(englisch)“. Navigation entries are not marked. (03.11.2026)
- Every page sets its own `<html lang>`.

## Structure

| Path | Content |
| -- | -- |
| `/` | Homepage, see below |
| `/portfolio/` | One short card per project, each with one German line on what it means for a business |
| `/portfolio/<slug>/` | Project page, English: one-line stack, then "What this project shows" (the key technical decisions), then the detail |
| `/writing/` | Articles, English |
| `/impressum/`, `/datenschutz/` | German |
| `/karte` | Redirect behind the QR code on Marcos's business cards. Target changes only on instruction |

Projects, in this order: ScienceQ (always labelled a demo), JobScout, the MCP authorization server.

Campaign pages (e.g. `/ki-check/`) are standalone: no main navigation, one goal, Impressum and Datenschutz in the footer.

## Homepage

- Hero, verbatim and alone: „Ich helfe Unternehmen, KI dort einzusetzen, wo sie sich lohnt.“
- Flow: Hero, „Wo sich KI lohnt“, „So fangen wir an“, Über mich, Projekte, Kontakt.
- Availability line „Remote, vor Ort nach Absprache.“ sits next to the Erstgespräch.

## Every page

- Same header and footer on every page. The footer links Impressum and Datenschutzerklärung.
- A change to the header or footer is made on every page in the same change.
- Before every push: check all pages for header, footer, both legal links, `lang`, and „(englisch)“ markers.
- After every deploy: check the served HTML of every page. It contains no `<script>` tags and nothing injected by Netlify. Checking the repo is not enough. (03.11.2026)

## Text

- German published text is supplied. Do not write or reword it; flag anything that looks wrong.
- English write-ups may be drafted here. They go live only after Marcos approves the text.
- The Datenschutzerklärung changes only with supplied text, in the same change as the feature that requires it.

## Rejected (do not propose)

- A static site generator (Eleventy, Hugo, Astro): no gain at this size.
- Web fonts, in particular from Google Fonts (visitor IPs to a third party without consent; LG München I, 20.01.2022).
- A language switcher (two versions of every page).
- A separate `/exhibit/` page: "What this project shows" is a section of each project page.
- A longer hero, or a second hero line.
- „vor Ort in Bayern“.

## Out of scope until decided

- What `/karte` points to, and whether it becomes the website.
- Whether `files/portfolio-referenzprojekte-de.pdf` is kept.

## Changing this file

Only on Marcos's instruction. A changed rule gets the date of the change next to it.
