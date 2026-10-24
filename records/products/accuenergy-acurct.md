---
id: prod:accuenergy-acurct
type: Product
name: Accuenergy AcuRCT / AcuCT-Flex Rogowski coils
aliases:
- AcuCT-Flex
- AcuRCT
- AcuCT Flex Series
- AccuCT Flex Series
- RCT16
- RCT24
- RCT36
- RCT47
category: Metering
make: accuenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:accuenergy
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-rog-coils-acuct-flex-series-rogowski-coil-ct-datasheet
    loc: sec=h1
    h: 3f37ab3be2f4
  - src: src:eq-equip-cts-pts-accuenergy-docs-rog-coils-acuct-flex-series-rogowski-coil-ct-datasheet
    loc: sec=h13
    h: 279f5674a613
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:current-sensor
  note: Flexible Rogowski coil current transformers for AC current measurement.
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-rog-coils-acuct-flex-series-rogowski-coil-ct-datasheet
    loc: sec=h1
    h: 3f37ab3be2f4
  review: drafted
- claim_id: c3
  rel: certified_to
  target: std:ce-marking
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-rog-coils-acuct-flex-series-rogowski-coil-ct-datasheet
    loc: tbl=4.r3
    h: c95e01f8be16
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: certified_to
  target: std:eu-rohs
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-rog-coils-acuct-flex-series-rogowski-coil-ct-datasheet
    loc: tbl=4.r3
    h: c95e01f8be16
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:ul-listing-curus
  note: Datasheet lists cURus with file number E359521.
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-rog-coils-acuct-flex-series-rogowski-coil-ct-datasheet
    loc: tbl=4.r3
    h: c95e01f8be16
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ieee-c57-13
  note: Accuracy stated as 0.5%, IEEE C57.13 class 0.6, over a 5A-50,000A current range.
  cite:
  - src: src:eq-equip-cts-pts-accuenergy-docs-rog-coils-acuct-flex-series-rogowski-coil-ct-datasheet
    loc: tbl=1
    h: 03090b2177f4
  review: drafted
  review_note: 'support check: partial - Accuracy and range are stated, but the passage doesn''t say the
    product is certified to IEEE C57.13, only accuracy class reference.'
---
The Accuenergy AcuCT Flex series is a family of flexible Rogowski coil current transformers for accurate AC current measurement. The rope-like coil wraps around odd-shaped conductors in crowded panels or switchgear where rigid CTs will not fit, and suits power metering, power quality analysis and energy monitoring. The datasheet gives a current range of 5A to 50,000A and an accuracy of 0.5%, matching IEEE C57.13 class 0.6. Part numbers RCT16, RCT24, RCT36 and RCT47 come in different coil lengths and window sizes, with a choice of lead lengths. The coils carry CE, RoHS and cURus markings.
