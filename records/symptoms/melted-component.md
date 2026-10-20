---
id: symptom:melted-component
type: Symptom
name: Melted component
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-connection
  note: Damaged DC connectors often show overheating or hot spots in thermography at an early stage, before
    melting is visible.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:visible-burn-marks
  note: Melted connectors, cables and terminals often appear together with burned or charred material;
    in combiner boxes, cable interconnections or fuses appear discoloured or burned.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h74
    h: 148d5765d67c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=29.r1
    h: c0df59a521bc
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
Melted plastic is seen on DC connectors and cables, often together with burned, brittle, cracked or whitened material. The same signs can show up at combiner box terminals and fuses, and on the junction box housing or lid on the back of the module. Damaged connectors often run hot before they melt, so an IR scan under load can find them early. Melting at a connector or a cable points to a Connector Defect or a Cable Defect, and both can lead to arcing, ground faults and fire. If the melting is on the junction box housing, suspect a junction box defect instead. Check the housing, the lid and the seals. Start with a visual inspection, then take IR images. Open connectors only after the circuit has been safely isolated, and look for corrosion inside. Compare string currents and run an insulation resistance test to check whether the damage has caused an insulation fault or lost production.

<!-- review notes
- sentence 1: support check: partial - Melted, burned, brittle, cracked, whitened appearance is stated, but 'plastic' and 'often together' co-occurrence are not explicitly stated.
- sentence 3: support check: partial - Early hot spots in thermography are stated and IR under load appears in the connector defect row, but 'before they melt' is implied rather than stated.
- sentence 4: support check: partial - Connector and cable defects causing arcing, ground faults and fire hazards are stated, but melting pointing to these causes is only implied, and cable defect does not mention arcing.
- sentence 5: support check: partial - Junction box housing melted and checking housing, lid and seals is described, but 'suspect instead' of connector defect is not stated.
- sentence 6: support check: partial - VI then IRT, safe isolation and corrosion in opened connectors are present, but the order and opening only after isolation are loosely combined.
-->
