---
id: concept:single-line-diagram
type: Concept
name: Single-line diagram
aliases:
- SLD
- one-line diagram
- Single-line Drawing
- functional single-line diagram
category: Design
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:ansi-device-numbers
  note: Utility guidance says functional single-line diagram submittals must label devices with industry
    standard device numbers, referring to the latest edition of ANSI C37.2.
  quote: On functional single-line diagram submittals, industry standard device numbers are necessary.
  quote_source: National Grid ESB 756, Exhibit 6
  cite:
  - src: src:std-utilities-nat-grid-ma-ny-shared-constr-esb756
    loc: sec=h259
    h: 0d5b4a12b19e
  - src: src:std-utilities-nat-grid-ma-ny-shared-constr-esb756
    loc: sec=h173
    h: 4e46f59fc651
  review: drafted
- claim_id: c2
  rel: related_to
  target: arch:behind-the-meter
  note: A sample single-line and control system diagram covers a behind-the-meter solar plus storage system.
  cite:
  - src: src:eq-equip-bess-stem-mp1-stem-sample-sld-btm-v1-0
    loc: sec=h3
    h: aeaf80252434
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:point-of-interconnection
  note: The sample diagram shows a line-side tap point of interconnection.
  cite:
  - src: src:eq-equip-bess-stem-mp1-stem-sample-sld-btm-v1-0
    loc: sec=h3
    h: aeaf80252434
  review: drafted
---
A single-line diagram, also called a one-line diagram or SLD, is a simplified drawing that shows an electrical system using one line for its circuits. Utilities ask for a functional single-line diagram as part of interconnection submittals. On these submittals, each protective and switching device has to carry its standard ANSI device number, as listed in ANSI C37.2. For example, device number 89 is a line switch. For storage projects, sample single-line and control diagrams show how a behind-the-meter solar plus storage system ties in, including a line-side tap point of interconnection. Monitoring installation manuals include a typical single-line diagram, sometimes with a communication table, to show where meters and data equipment connect.

<!-- review notes
- sentence 1: support check: partial - Passages only show the names 'One-line diagram' and 'SLD | Single-line Drawing'; they give no definition of a simplified drawing using one line for circuits.
- sentence 2: support check: partial - Exhibit gives guidelines for functional SLD submittals, implying utilities want them, but doesn't explicitly say they are required in interconnection submittals.
- sentence 3: support check: partial - Passages say device numbers are necessary per ANSI C37.2 but don't say each protective and switching device must carry one.
- sentence 5: support check: partial - Sample diagram title shows behind-the-meter solar+storage with line-side tap POI, but nothing on 'storage projects' generally or showing how it ties in beyond the title.
- sentence 6: support check: partial - Passages show manuals with typical single-line diagrams and a communication table figure, but not their purpose of showing where meters and data equipment connect.
-->
