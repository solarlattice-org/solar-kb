# Contributing

- **Code** changes: open a PR; CI must pass (`pytest`, `solar-kb validate`, `solar-kb build`).
- **Records** are produced by the compiler and reviewed by humans in PRs labeled `compiler`.
  Review a claim by reading it next to its cited source. On merge, claims still `drafted` become
  `verified` unless marked `keep: drafted`. To dispute a claim, set `review: disputed` and add a
  `review_note`.
- Never paste source text into a record beyond a `quote:` of at most 25 words.
- Never cite a private source from a public record.
