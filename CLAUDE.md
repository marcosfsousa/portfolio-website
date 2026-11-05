# marcossousa.de (repo portfolio-website)

Personal site of Marcos Sousa (Gewerbe: Marcos Sousa Software- und KI-Entwicklung).

This file is the home of the site's standing rules. Decisions made while working in this repo are recorded here, with their date. Styling and markup decisions, with their reasons, live in `docs/DECISIONS.md`; site-level rules stay here. Neither is mirrored in the other. (03.11.2026) Seeded 03.11.2026 from the decisions of 02.11.2026.

Work is tracked as GitHub issues in this repo, one issue per deliverable. Task briefings arrive in the session. They are not committed. If a briefing conflicts with this file, stop and ask.

## Hosting

Netlify, deployed on push to `main`. No build step.

- Every push to `main` that changes a watched path triggers a production deploy, which costs 15 of the 300 credits a month on the Free plan. (05.11.2026)
- Refactors and checks are done on a branch and verified on its Deploy Preview. Merge to `main` only when Marcos approves a finished batch. (05.11.2026)
- Netlify skips a build, production or Deploy Preview, when nothing under the paths watched by `ignore` in `netlify.toml` changed. Any new file that affects the deployed output must be added to that path list. (05.11.2026)

## Footprint

- Hand-written static HTML and CSS. `/writing/` is the pattern for new pages.
- System font stack. No web fonts, remote or self-hosted.
- No client-side analytics, trackers or cookies. Netlify's server-side Web Analytics stays as configured in the Netlify dashboard; nothing else measures visits. (03.11.2026)
- No theme toggle. No photo.
- No external resources: no third-party scripts, embeds, fonts, form endpoints or Netlify Functions. Each one changes the Datenschutzerklärung and Marcos's provider list, so none is added to solve a task. Stop and ask.
- Exception (decided 03.11.2026, recorded 04.11.2026): the opt-in page `/ki-check/` may submit one form to Brevo (Brevo SAS, Paris). This applies to that page only.
  - The form is Brevo's "Simple HTML" embed: a plain HTML form that posts directly to Brevo. No Brevo scripts, fonts or stylesheets (`sib-styles.css` removed), no other external resources on page load, no cookies. Loading the page makes no request to Brevo.
  - Styling is the site's own CSS. The honeypot field `email_address_check` is hidden by our CSS.
  - The form validates the email itself (`type="email"`, `required`, a `pattern` that requires a dot in the domain), because Brevo answers invalid input with raw JSON on its own domain.
  - `locale` is set to `de`.
  - After submit, Brevo redirects to our own thank-you page. The link in the confirmation email leads to our own confirmation page.
  - Rejected: Brevo's embed with scripts (loads third-party resources on page view) and a Netlify Function (own code, and Netlify would then process the form data).
  - Any other form, endpoint or external resource still falls under the general rule: stop and ask.
- Netlify publishes only `site/` (`publish = "site"` in `netlify.toml`). Everything served lives under `site/`; files outside it, such as `CLAUDE.md` and `README.md`, are never served. (03.11.2026)
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
| `/portfolio/<slug>/` | Project page, English: one-line stack, then "What this project shows" (the key technical decisions), then the detail, under a heading of its own (03.11.2026) |
| `/writing/` | Articles, English |
| `/impressum/`, `/datenschutz/` | German |
| `/karte` | Redirect behind the QR code on Marcos's business cards, to `/` (302) (decided 03.11.2026, recorded 04.11.2026). Target changes only on instruction |

Projects, in this order: ScienceQ, JobScout, the MCP authorization server. ScienceQ and the MCP authorization server are always labelled demos. (03.11.2026)

No PDF project overview on the site. The `/portfolio/` cards and project pages replace `portfolio-referenzprojekte-de.pdf`, which was removed. (03.11.2026)

Campaign pages (e.g. `/ki-check/`) are standalone: no main navigation, one goal, Impressum and Datenschutz in the footer.

## Homepage

- Hero, verbatim and alone: „Ich helfe Unternehmen, KI dort einzusetzen, wo sie sich lohnt.“
- Flow: Hero, „Typische Ansatzpunkte“, „So fangen wir an“, Über mich, Projekte, Kontakt (heading changed 04.11.2026).
- Availability line „Remote, vor Ort nach Absprache.“ sits next to the Erstgespräch.

## Every page

- Same header and footer on every page. The footer links Impressum and Datenschutzerklärung.
- A change to the header or footer is made on every page in the same change.
- Before every push: check all pages for header, footer, both legal links, `lang`, and „(englisch)“ markers.
- After every production deploy: check the served HTML of every page on marcossousa.de. It contains no `<script>` tags and nothing injected by Netlify. Checking the repo is not enough. (03.11.2026)

## Text

- German published text is supplied. Do not write or reword it; flag anything that looks wrong.
- English write-ups may be drafted here. They go live only after Marcos approves the text.
- The Datenschutzerklärung changes only with supplied text, in the same change as the feature that requires it.

## Changes and PRs

- A comment explains only the code immediately after it, in at most 150 characters. Before writing one, ask whether the code needs it at all. No lists or counts of things elsewhere in the code. The reason behind a styling or markup choice goes in `docs/DECISIONS.md`, and the comment names the entry when the code needs it. Applies to new and changed comments. (03.11.2026)
- Commit, push, opening a PR, running `/review-pr` and posting its review each wait for Marcos's go-ahead, asked for each time. Approving a plan is not a go-ahead for any of them. (03.11.2026)
- Every PR gets a `/review-pr` run after it is opened, under the rule above. (03.11.2026)

## Rejected (do not propose)

- A static site generator (Eleventy, Hugo, Astro): no gain at this size.
- Web fonts, in particular from Google Fonts (visitor IPs to a third party without consent; LG München I, 20.01.2022).
- A language switcher (two versions of every page).
- A separate `/exhibit/` page: "What this project shows" is a section of each project page.
- A longer hero, or a second hero line.
- „vor Ort in Bayern“.

## Changing this file

Only on Marcos's instruction. A changed rule gets the date of the change next to it.
