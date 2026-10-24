---
id: prod:sungrow-sg125hv
type: Product
name: Sungrow SG125HV
aliases:
- SG125HV
category: Inverters
make: sungrow
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sungrow
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h37
    h: 309269bc71a4
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h8
    h: f515d5276f50
  review: drafted
  review_note: 'support check: partial - The passages show a Sungrow white paper about the SG125HV, which
    implies Sungrow makes it, but they never state manufacture explicitly.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Described in a Sungrow white paper as a grid-tied PV inverter acting as a balanced three-phase
    current source.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h8
    h: f515d5276f50
  review: drafted
---
The SG125HV is a Sungrow grid-tied PV inverter that Sungrow covers in a white paper on its neutral, safety and grid connections. According to that white paper, the SG125HV does not need a neutral connection. It works as a balanced three-phase current source, and no single-phase loads connect directly to the inverter. Engineers have cited this white paper as a source when looking at neutral connections and effective grounding for inverter interconnections. The evidence gives no ratings, protocols or certifications for this product, so check the Sungrow datasheet for them.

<!-- review notes
- sentence 3: support check: partial - The white paper is listed as a source in a neutral connections and effective grounding section, but nothing says engineers cited it for inverter interconnections.
-->
