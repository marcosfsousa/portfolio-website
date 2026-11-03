# Decisions

Why the site's styling and markup are the way they are: what was decided, what was measured, and what breaks if it changes. Site-level rules live in `CLAUDE.md`. Code comments stay short and name the entry here when the code needs one.

Each entry carries its date and issue. A changed decision is edited in place and gets the new date beside the old one.

## Layout

### Shared header and footer (03.11.2026, #18)

- Every page carries byte-identical `<header>` and `<footer>` markup. Nav and footer both carry `lang="de"` on every page. It is needed on the English pages and does nothing on the German ones, so the markup can stay identical.
- No `aria-current` on the nav: it would make the markup differ per page.
- The homepage aligns header and footer with its reading column through `body.home`, not through different markup.
  - Below 62rem the grid is one column, 55rem wide with 1.5rem side padding, so header and footer take `max-width: 55rem`.
  - From 62rem the reading column starts at 50% − 27.5rem (half the row) + 1.5rem (row gutter) + 14.5rem (margin column + gap) = **50% − 11.5rem**. There the box becomes the column exactly: 37rem wide, no side padding. That puts the footer's hairline on the same span as the `.entry` hairlines. With the subpage padding kept, it would start 1.5rem to their left.
  - Measured at 1280px in headless Chrome: nav, h1, footer text and all hairlines start at x=456, and the hairlines span 456–1047.
  - `.home > header` outranks `body > header` on specificity, so source order does not matter between them.
- Spacing absorbs the nav. `.top` and `main` top padding went from 3.5rem to 2.5rem (2rem on mobile), so the first heading sits about where it did before. `.end` lost its 8rem bottom padding because the footer below brings its own.
- **Open:** below 62rem the homepage footer's hairline runs wider than the `.entry` hairlines, edge to edge on a phone. Cosmetic. Raised in the review of #24 and not fixed there.

## Padding collisions

### `code`, `pre` and `blockquote` never share an element with a padding rule (#15, restated 03.11.2026, #24)

The collision the top of `style.css` warns about needs two padding rules on the same element. #15's three rules are safe from it because of two properties:

- No rule that sets padding or margin targets `code`, `pre` or `blockquote`, apart from those elements' own rules.
- No `code`, `pre` or `blockquote` on a served page carries a class.

So the three always land on descendants of the padding-setters, never on the same element.

Check it by pulling every rule from `site/style.css` that sets `padding*` or `margin*` and confirming that none outside the `code`/`pre`/`blockquote` rules matches those elements. Earlier versions of this note listed the selectors instead. The list went stale as rules were added, which is why it is now a property.

### The `pre code` reset (#15)

`code` is an element selector, so it also reaches the `code` inside `pre`. Without the `pre code` reset, every line of a code block would get the inline 0.15em padding and the 500 weight. The reason for `inherit` in that rule is in the comment above `pre`.
