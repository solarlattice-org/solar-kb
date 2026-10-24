---
id: prod:accuenergy-acuct
type: Product
name: Accuenergy AcuCT current transformers
aliases:
- AcuCT
- ACUCT
- AcuSplitCT
- AcuCT R
- AcuCT S77
category: Metering
make: accuenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:accuenergy
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-ct-acuct-5170r
    loc: sec=h1
    h: 2cef19b2c164
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: sec=h2
    h: 9f1ed6d1e945
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-hinged-split-core-333mv-output-current-tranformer
    loc: sec=h2
    h: cf97094b9e2e
  - src: src:eq-equip-bess-stem-metering-procurement-guidance
    loc: sec=h19
    h: 120632d7fb14
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:current-sensor
  note: Split-core and hinged split-core current transformers
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-ct-acuct-5170r
    loc: sec=h1
    h: 2cef19b2c164
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: sec=h2
    h: 9f1ed6d1e945
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-hinged-split-core-333mv-output-current-tranformer
    loc: sec=h2
    h: cf97094b9e2e
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:sel-735
  scope:
    products:
    - prod:sel-735
  note: A metering procurement guide recommends only the AcuCT S77 solid-core and AcuCT R split-core CTs
    for use with SEL-735 meters.
  cite:
  - src: src:eq-equip-bess-stem-metering-procurement-guidance
    loc: sec=h19
    h: 120632d7fb14
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: certified_to
  target: std:iec-60044-1
  note: Stated standard for the 400-1600 A split-core series with 5 A/1 A secondary
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=3
    h: 2702441126f5
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=5
    h: 6fe0ff89afd0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The datasheets list IEC 60044-1 as the standard for the 400-1600
    A series, but they don''t say it is certified; they list it only as a ''Standard''.'
- claim_id: c5
  rel: certified_to
  target: std:ce-marking
  note: The datasheets also list UR approval and RoHS compliance.
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-hinged-split-core-333mv-output-current-tranformer
    loc: tbl=1.r10
    h: 7ab672823c45
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-hinged-split-core-333mv-output-current-tranformer
    loc: tbl=5.r2
    h: 7ab672823c45
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-hinged-split-core-333mv-output-current-tranformer
    loc: tbl=7.r9
    h: 7ab672823c45
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=3
    h: 2702441126f5
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=5
    h: 6fe0ff89afd0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  attr: frequency
  value:
    min: 50
    max: 400
    unit: unit:HZ
  conditions: Frequency range, AcuSplitCT 400/600/800/1000 A split-core series with 5 A/1 A secondary
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=3
    h: 2702441126f5
  review: drafted
- claim_id: c7
  attr: frequency
  value:
    min: 50
    max: 400
    unit: unit:HZ
  conditions: Frequency range, AcuSplitCT 1000/1200/1600 A split-core series with 5 A/1 A secondary
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=5
    h: 6fe0ff89afd0
  review: drafted
- claim_id: c8
  attr: operating_temperature
  value:
    min: -15
    max: 60
    unit: unit:DEG_C
  conditions: AcuSplitCT 400/600/800/1000 A split-core series
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=3
    h: 2702441126f5
  review: drafted
- claim_id: c9
  attr: operating_temperature
  value:
    min: -15
    max: 60
    unit: unit:DEG_C
  conditions: AcuSplitCT 1000/1200/1600 A split-core series
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=5
    h: 6fe0ff89afd0
  review: drafted
- claim_id: c10
  attr: rated_output_current
  value:
    nominal: 5
    unit: unit:A
  conditions: Rated secondary current, 5 A output option of the 400-1600 A split-core series
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=3
    h: 2702441126f5
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=5
    h: 6fe0ff89afd0
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions)
- claim_id: c11
  attr: rated_output_current
  value:
    nominal: 1
    unit: unit:A
  conditions: Rated secondary current, 1 A output option of the 400-1600 A split-core series
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=3
    h: 2702441126f5
  - src: src:eq-equip-cts-pts-accuenergy-docs-split-core-acuct-split-core-5a-1a-output-current-tranformer-brochur
    loc: tbl=5
    h: 6fe0ff89afd0
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
---
AcuCT is Accuenergy's family of current transformers. It includes split-core, hinged split-core and solid-core types, sold under series names such as AcuSplitCT. The split-core CTs are compact, low-cost and highly accurate. You can install them without disconnecting the cables. The hinged versions close with a single click and are small enough for panels with limited space. The 400 A to 1600 A split-core series come with a 5 A or 1 A secondary. They work over 50 to 400 Hz and operate from -15 to 60 degrees C. One metering procurement guide recommends only the AcuCT S77 solid-core and AcuCT R split-core CTs for use with SEL-735 revenue meters.

<!-- review notes
- sentence 1: support check: partial - Split-core, hinged split-core and the AcuCT S77 solid-core are supported, but the passages don't call AcuCT the whole family, and AcuSplitCT is named only for split-core series.
- sentence 3: support check: partial - Single-click installation and a compact size for limited-space panels are stated, but 'close with a single click' is a mild paraphrase.
- sentence 1: review: partial - Split-core (AcuSplitCT), hinged split-core and AcuCT S77 solid-core CTs appear, but no passage calls AcuCT Accuenergy's overall CT family or names the hinged type as AcuCT.
-->
