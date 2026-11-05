# Decisions

Why the site's styling and markup are the way they are: what was decided, what was measured, and what breaks if it changes. Site-level rules live in `CLAUDE.md`. Code comments stay short and name the entry here when the code needs one.

Each entry carries its date and issue. A changed decision is edited in place and gets the new date beside the old one.

## Layout

### Shared header and footer (03.11.2026, #18)

- Every page carries byte-identical `<header>` and `<footer>` markup. Nav and footer both carry `lang="de"` on every page. It is needed on the English pages and does nothing on the German ones, so the markup can stay identical.
- No `aria-current` on the nav: it would make the markup differ per page.
- The homepage aligns header and footer with its reading column through `body.home`, not through different markup.
  - Below 62rem the grid is one column, 55rem wide with 1.5rem side padding, so header and footer take `max-width: 55rem`.
  - From 62rem the reading column starts at 50% − 27.5rem (half the row) + 1.5rem (row gutter) + 14.5rem (margin column + gap) = **50% − 11.5rem**. There the box becomes the column exactly: 37rem wide, no side padding. That puts the footer's hairline on the same span as the hairlines between the homepage cards (`.entry` before 04.11.2026, #22). Keeping the subpage padding would have needed the box 1.5rem further left to line the text up, and its hairline would then start 1.5rem left of theirs.
  - Measured at 1280px in headless Chrome: nav, h1, footer text and all hairlines start at x=456, and the hairlines span 456–1047.
  - Re-measured 04.11.2026 (#22) in headless Chrome at a 1243px layout width: nav, hero `h1`, every section's text column, the cards and the footer all start at x=438 (= 50% − 11.5rem) and end at 1030.
  - `.home > header` outranks `body > header` on specificity, so source order does not matter between them.
- Spacing with the nav. `.top` and `main` top padding went from 3.5rem to 2.5rem, and on mobile from 2.5rem to 2rem. The nav is its top padding plus one 0.9rem line at line-height 1.7 (≈24.5px). That's ≈48.5px on desktop (1.5rem padding) and ≈40.5px on mobile (1rem). So the first heading sits about 2rem (≈32px) lower than before on both. That was kept on purpose (option (a) in the review of #24).
- `.end` lost its 8rem bottom padding because the footer below brings its own.
- **Open:** below 62rem the homepage footer's hairline runs wider than the card hairlines, edge to edge on a phone. Cosmetic. Raised in the review of #24 and not fixed there.

### Name in the header (04.11.2026, #22)

- „Marcos Sousa“ sits on the left of the shared header and links to `/`. The nav stays as it was, on the right. Decided by Marcos so that the homepage, which `/karte` now points to, never goes live without the name: the hero `h1` is the hero sentence alone.
- The name is outside `nav`. It is not a navigation entry, and it does not need the nav's `lang="de"`.
- The header is a wrapping flex row: `justify-content: space-between`, `align-items: baseline`. When name and nav do not fit on one line, the nav wraps below the name. No media query is needed for that.
- Same size and face as the nav (inherited from the header). Weight 600, the step Marcos asked for ("one weight heavier than the nav"). The serif faces in the stack have no intermediate weight (#4), so 600 is the next step up from the nav's 400.
- Ink colour and no underline. These were my choices, not specified: they keep the name from reading as a fifth nav link.

### Campaign pages: header without nav (05.11.2026, #29)

- `/ki-check/`, `/ki-check/danke/` and `/ki-check/bestaetigt/` carry the shared `<header>` with the name link „Marcos Sousa“ → `/` only, and no `<nav>`. Decided by Marcos. CLAUDE.md asks for the same header on every page and for no main navigation on campaign pages. The name keeps the page attributable; dropping the nav keeps it to one goal.
- These pages are therefore the one exception to byte-identical header markup (Shared header and footer, above). The footer stays byte-identical.

### Opt-in form (05.11.2026, #29)

- The form on `/ki-check/` is our own markup carrying the field names, hidden inputs and `action` of Brevo's „Simple HTML“ embed. None of Brevo's classes, inline styles, SVG or `sib-styles.css` (CLAUDE.md, Footprint).
- The honeypot `email_address_check` is `display: none`. Brevo's own stylesheet did this through `.input--hidden`; without it, the field would show.
  - The rule sits after the text-field rule. Both are one class, one element and one attribute, so the later one wins. Placed before it, the field rule's `display: block` showed the honeypot: seen in the first render, 05.11.2026.
- The honeypot also carries `tabindex="-1"` and `autocomplete="off"`, so that if the stylesheet fails to load, keyboard users and autofill skip it (review of #31).
- The „Datenschutzerklärung“ link in the consent label opens in a new tab (`target="_blank" rel="noopener"`), so reading it mid-form does not lose the input (review of #31).
- Labels sit above the fields, at full column width. Fields have a 1px `--quiet` border and the page background, so they hold in both colour schemes without new tokens.
- Each checkbox is a two-column grid row, box and label, `align-items: baseline`. The long consent text then wraps under itself, not under the box.
- The button inverts ink and background. It is the page's one goal, so it is the one filled element on the site.
- `autocomplete` carries the standard tokens (`given-name`, `family-name`, `organization`, `email`, `tel`); Brevo's embed had `off`.

### Project cards (03.11.2026, #19)

- A card is a `div.card`: an `h2` title, its paragraphs, then the „Details (englisch)“ link. Cards are separated by a 1px hairline in `--hair`, as the footer is, with no box or background.
- It is a new class rather than `.entry`. `.entry p` dropped paragraph margins, which suited a single sentence, but a card has several paragraphs and needs the normal paragraph rhythm. `.entry` was removed with the old homepage (04.11.2026, #22).
- `.card h2` resets `main h2`'s top margin, because the card's own top padding already separates it from the card above. `.card h2` outranks `main h2` on specificity.
- The class works in both layouts. The homepage „Projekte“ section reuses it (04.11.2026, #22). There the card title is an `h3`, because the section heading is the `h2`. `h3` has the same size as `h2` (1.14rem), so a card looks the same on both pages.
- On the homepage the first card drops its top padding (`.col > .card:first-child`), so its title lines up with the „Projekte“ label beside it.

### Homepage sections (04.11.2026, #22)

- The homepage keeps the two-column grid from #4 (variant D, "Marginalia"): a margin column beside a 37rem reading column, one `.row` per section. Subpages use one reading column in `main`, without the grid.
- `.row` has `max-width: 55rem`: margin column 12rem + gap 2.5rem + reading column 37rem + side padding 2 × 1.5rem = 54.5rem, rounded up (#4, moved here from `style.css` 05.11.2026, #25).
- Each section heading, exactly as supplied („Typische Ansatzpunkte“, „So fangen wir an“, „Über mich“, „Projekte“, „Kontakt“), is an `h2.side` in the margin column. It replaces the old English margin labels (Exhibit, Portfolio, Writing, Contact), so the label is the heading and the text is not repeated in the reading column. `h2.side` resets `h2`'s weight and margin, and `.side` supplies the label type.
- The hero row has an empty margin cell (`.side.empty`) rather than the `h1` placed into column 2. Every row then has the same two children, so the tracks cannot disagree. The cell stays empty on purpose.
- The hero `h1` is the hero sentence alone, in the existing `h1` style.
- The bold subheadings in „Typische Ansatzpunkte“ are `h3`. Before #22, `h3` was a smaller, grey heading for the old portfolio block. It now has ink colour and `h2`'s size, because at 1rem it was smaller than the 18.5px body text it heads.
- Kontakt (`id="kontakt"`) is the `.end` row. `.end` no longer sets a smaller, grey type: the contact text is a call to action, not a footnote.
- Removed with the old homepage: `.capability`, `.entry`, the old `h3` style.
- Checked 04.11.2026 in headless Chrome at a 1243px layout width and at 390px (iframe, because headless Chrome clamps the window width). At 390px there is no horizontal scroll, the labels stack above their text, and nothing overlaps.

### No `.tail` (03.11.2026)

`.block.tail` styled the homepage row that linked to the German PDF. The PDF and that row were removed (see `CLAUDE.md`, Structure), and the rule went with them.

## Type

### Measure: 37rem (#4, moved here from `style.css` 05.11.2026, #25)

The reading column is 37rem wide. It is the only width where every face in the serif stack lands inside 65–75 characters per line at 18.5px: Sitka Text 67, Cambria 74, Georgia 71. Measured in the browser: 67.3.

### Inline `code` weight (#15, moved here from `style.css` 05.11.2026, #25)

- Inline `code` is set apart from the prose by spacing and weight, never by a tinted box. The write-ups use inline code densely, often several spans in one paragraph. At that density a background reads as noise across the page rather than as emphasis inside a sentence.
- A background would also break. An inline span that wraps gets its padding on the first and last fragment only, so a background renders as a visibly broken box, where padding alone is invisible.
- What `font-weight: 500` returns was measured, not predicted, because the prediction was wrong. On the Windows desktop it was verified on, the stack reaches "Cascadia Mono", which precedes Consolas and ships with Windows Terminal. There a requested 500 renders as the family's SemiBold, one step heavier than the value names. Two mechanisms agree: DevTools reports the face on the Keycloak post's first paragraph as CascadiaMonoRoman-SemiBold, and a canvas ink test gives 500 and 600 byte-identical coverage, both about 17% above 400.
- The CSS font-matching rules predict the opposite. For a requested 500 with no 500 in the family, matching checks 500 and then descends, which should reach Regular 400. Chrome does not do that for this local family. Do not reason about the rendered weight from the algorithm here; look at it.
- Where Cascadia Mono is absent the stack falls to Consolas, which has Regular and Bold only. That case is predicted to land on 400 and degrade to padding alone. It stays a prediction: nothing has been rendered on such a machine.
- On a handset neither family exists and the stack falls through to the generic monospace, a third case. The Keycloak post was read there in Chrome and Firefox with nothing flagrant seen. The face was not identified.
- 500 stays, decided against the rendering rather than against the value's name: the result of 500 was looked at on both surfaces, the desktop and a handset, and accepted. Do not go above it. Asked for 500, this stack went up a step rather than down, so a request above 500 has further to climb, with a real Bold at the top of both families. Full bold on inline code this dense is heavier than the prose it sits in.
- #15 gave "600+ synthesises" as the reason. Synthesis is the wrong worry for a family that ships a real Bold: the face would be genuine and still too heavy. The ruling stands; only its reason was replaced.

## Padding collisions

### `.row` owns the horizontal padding (#4, moved here from `style.css` 04.11.2026, #22)

`.row { padding: 0 1.5rem }` is where the homepage's horizontal padding comes from. `.top`, `.block` and `.end` land on the same elements as `.row`, so they set vertical padding as longhand. A `padding` shorthand on any of them silently resets `.row`'s horizontal padding. On desktop that drifts the text out of the column, and on a phone it puts text against the viewport edge. One bug, two symptoms that look unrelated.

The rule is about that collision, not about shorthands as such. `.side.empty { padding: 0 }` is correct, because that element inherits none of `.row`'s padding. A new shorthand is safe only if you can say which rule it would override.

### `code`, `pre` and `blockquote` never share an element with a padding rule (#15, restated 03.11.2026, #24)

The collision described under "`.row` owns the horizontal padding" needs two padding rules on the same element. #15's three rules are safe from it because of two properties:

- No rule that sets padding or margin targets `code`, `pre` or `blockquote`, apart from those elements' own rules.
- No `code`, `pre` or `blockquote` on a served page carries a class.

So the three always land on descendants of the padding-setters, never on the same element.

Check it by pulling every rule from `site/style.css` that sets `padding*` or `margin*` and confirming that none outside the `code`/`pre`/`blockquote` rules matches those elements. Earlier versions of this note listed the selectors instead. The list went stale as rules were added, which is why it is now a property.

### The `pre code` reset (#15)

`code` is an element selector, so it also reaches the `code` inside `pre`. Without the `pre code` reset, every line of a code block would get the inline 0.15em padding and the 500 weight. In `pre code`, `inherit` does specific work in both places. `font-size: inherit` takes `pre`'s already-computed size, where `0.84em` would multiply against it and give 0.71em. `font-weight: inherit` reaches past `code` to `pre`, which sets none, so the weight is the body's.

### `pre` and `blockquote` (#15, moved here from `style.css` 04.11.2026, #22; edited 05.11.2026, #25)

- `pre` scrolls itself rather than the page, so a long line never widens the viewport. Its left hairline is the site's `--hair`, like the footer and the cards.
- No background under `pre` or `blockquote`. No downloaded code face and no highlighter library: condition 8 and the stack rule out Prism, highlight.js and every `@font-face` code face permanently.
- Both were written for the write-ups before any page used them.

## Mobile

### The media query stays last (#4, moved here from `style.css` 04.11.2026, #22)

The `max-width: 40rem` query stays last in `style.css`. Written earlier, a later base rule overrides it with no error anywhere.

### Section spacing (#4)

On a phone the margin labels stack above their text instead of sitting beside it, and section gaps of 2.6rem are too generous on a 390px screen. So `.top`, `.block` and `main` take less top padding, and `.side` a tighter line height. Measured in #4 with `prototype/visual-form/align-check.html`, which is on the branch `prototype/issue-4-visual-form` (commit `a83f1f8`), not on `main`.

### Type size stays 18.5px (#4, #15)

At 390px the measure is about 39 characters, below the comfortable minimum of about 45. #4 costed the two ways out: 17px buys about 43, 16.5px about 45. The type size stays 18.5px. Rendered at a true 390px and read, the longest paragraph then on the homepage held its rag, with nothing orphaned. Shrinking the body face to buy six characters costs more than the short measure does. Still worth confirming on a real handset, which no headless render can stand in for.

#15 gave `code` 0.15em padding on each side, so the earlier reading that inline code spans do not break was re-read on a handset, in Chrome and Firefox, on the Keycloak post's opening paragraph and its PKCEEnforcerExecutor paragraph. Nothing flagrant was seen. Read, not measured.

### `blockquote` drops its indent and hairline (#15)

At 390px the reading column is 342px and the measure is already about 39 characters. A 1.1rem indent takes it to about 37, and trimming the indent instead of removing it buys back well under one character. Colour and paragraph rhythm carry the quotation on a phone. `pre` keeps its indent: its lines scroll rather than wrap, so measure does not constrain it.
