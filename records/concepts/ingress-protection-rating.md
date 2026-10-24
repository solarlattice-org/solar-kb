---
id: concept:ingress-protection-rating
type: Concept
name: Enclosure protection rating
aliases:
- IP rating
- IP65
- IP54
- NEMA 3R
- NEMA 4X
- enclosure rating
- Ingress Protection (IP) Ratings
- Degree of protection
- Enclosure Protection Degree
- Enclosure protection class
- Ingress Rating
- Enclosure IP Rating
category: Enclosures
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: std:iec-60529
  note: IEC 60529 defines the IP code; a rating at a given numeral also implies compliance with all lower
    numerals, for the water digit up to 6.
  cite:
  - src: src:sma-doc-275752
    loc: tbl=44.r10
    h: b78a71310257
  - src: src:sma-doc-259761
    loc: tbl=90.r12
    h: b1ebf310652f
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=47.r13
    h: 9792455e2b87
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h227
    h: 16bb690c871e
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h226
    h: 3cfbf1a84eb1
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:nema-250
  note: NEMA Publication 250 is the source for converting NEMA enclosure types to IP designations; the
    conversion only works in one direction.
  cite:
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h226
    h: 3cfbf1a84eb1
  review: drafted
- claim_id: c3
  rel: related_to
  target: prod:sma-sbse-us-50
  note: Electronics are rated IP65 per IEC 60529.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=47.r13
    h: 9792455e2b87
  review: drafted
- claim_id: c4
  rel: related_to
  target: prod:sma-sunny-island
  note: Rated IP54 per IEC 60529.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=90.r12
    h: b1ebf310652f
  - src: src:sma-doc-278742
    loc: tbl=94.r2
    h: fe6881faa9c0
  review: drafted
---
An enclosure protection rating tells you how well a housing keeps out solid objects and water. It is given either as an IEC IP code or as a NEMA enclosure type. In an IP code, the first digit covers protection against solid objects and dust, from non-protected up to dust tight. The second digit covers protection against moisture, from non-protected up to submersion. For example, IP65 means dust tight and protected against water jets. IP54 means interior dust deposits and splashing water from any direction are kept out. Under IEC 60529, a rating also covers all lower levels, up to water numeral 6. An enclosure rated only 7 or 8 is not considered suitable for water jets unless it is dual coded. NEMA types can be converted to IP equivalents, but not the other way round. NEMA adds tests that IEC does not require, such as corrosion, gasket aging and external icing. PV and storage equipment datasheets list these ratings, for example NEMA 4X on string inverters and NEMA 3R or IP54 on battery and power-conversion equipment. On site, the installer has to keep the enclosure rating intact. One inverter manual says that losing the NEMA 4X rating voids the warranty.

<!-- review notes
- sentence 6: support check: partial - The passages show NEMA 4X, NEMA 3R and IP54, but they do not say which are string inverters versus battery or power-conversion equipment.
-->
