---
id: concept:pq-capability-diagram
type: Concept
name: P-Q capability diagram
aliases:
- PQ diagram
- capability curve
- P/Q diagram
- P-Q curve capability
- P-Q Capability
- P-Q Curves
- P-Q Diagrams
- Reactive Capability Data
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:apparent-power
  note: Nominal apparent power at active power output and draw bounds the operating region in the P/Q
    diagram.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=8
    h: 18c2158c983f
  - src: src:sma-doc-275857
    loc: tbl=12
    h: 73660df576c9
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:reactive-power
  note: Maximum reactive power is defined separately for each quadrant Q1 to Q4.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=8
    h: 18c2158c983f
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:active-power
  note: Nominal active power limits for output and draw form boundaries of the diagram.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=8
    h: 18c2158c983f
  - src: src:sma-doc-275857
    loc: tbl=12
    h: 73660df576c9
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:reactive-power-sign-convention
  note: SMA draws the P/Q diagram in the generator reference-arrow system.
  cite:
  - src: src:sma-doc-275857
    loc: tbl=1.r12
    h: d6f0e9a4f343
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=8
    h: 18c2158c983f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Passages show the P/Q diagram is in the generator reference-arrow
    system, but do not attribute it to SMA specifically or discuss sign convention explicitly.'
- claim_id: c5
  rel: related_to
  target: concept:grid-code
  note: The published capability may be reduced to meet the applicable country grid standard.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h58
    h: 1fd128c2dedc
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=3.7.5
    h: baec1cd17f8e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: related_to
  target: concept:power-factor
  note: Vendor P-Q charts mark cos phi lines on the capability curve.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=3.8
    h: e03e98eb97db
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: related_to
  target: prod:abb-pvs-166-175-tl-us
  note: Manual publishes the maximum P-Q capability, with curves stated for ambient temperature limits.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=3.8
    h: e03e98eb97db
  review: drafted
---
A P-Q capability diagram plots an inverter's active power against its reactive power and shows the largest operating area the unit can deliver under stated operating conditions. The diagram is split into four quadrants, labelled Q1 to Q4. Manufacturers warn that the capability shown may be reduced to meet the grid code that applies in the country of installation. Vendor curves can depend on ambient temperature: one manual gives separate PVS-175 curves for operation up to 40°C and up to 30°C. These charts also mark power factor (cos phi) lines. Some manufacturers publish these charts as P-Q curves or reactive capability data for each inverter rating. Power-system textbooks describe a related idea, the circle diagram of apparent power, which plots receiving-end active and reactive power on P-Q coordinates.

<!-- review notes
- sentence 1: support check: partial - Passages state maximum P-Q capability under specified operating conditions with P and Q axes, but the explicit definition of plotting P against Q as an operating area is only implied.
- sentence 4: review: partial - The passage has PVS-175 curves labelled up to 40°C and up to 30°C and shows cosphi lines, but it never says the temperature is ambient, and the garbled labels do not clearly show the same model has both curves.
-->
