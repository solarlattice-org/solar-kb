---
id: symptom:contact-corrosion
type: Symptom
name: Corroded contacts
aliases:
- corrosion of the contacts
claims:
- claim_id: c1
  rel: observed_as
  target: meas:jbox-terminal-corrosion
  note: Corroded parts inside the junction box may involve solder joints, wires, bypass diodes or tabbing
    ribbons, and may be hidden under the potting material, so they can only be seen once the potting is
    removed.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r1
    h: 3aa67d44d717
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
  review_note: 'support check: partial - Passages state corroded parts in the junction box (solder joints,
    wires, diodes, ribbons) and that potting can hide them until removed, but ''loose or corroded terminals''
    as a visible observation is only loosely matched.'
- claim_id: c2
  rel: observed_as
  target: meas:ir-hot-connection
  note: Corrosion raises the internal resistance and heats the junction box. An IR camera shows the heat
    as a hot spot.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: drafted
---
Corroded contacts are mostly found inside the module junction box, on solder joints, wires, bypass diode connections or tabbing ribbons. The usual cause is moisture getting into a poor or damaged junction box, for example through lost adhesion, a cracked or brittle housing, or a missing seal where the wires enter. A defective or detached junction box lets humidity in, and the corroded interconnections that follow cause performance losses and raise the risk of arcing and fire. Delamination near the junction box can let water in and speed up corrosion. In humid periods it can even cause an insulation fault. Corrosion raises the contact resistance, so the junction box heats up. An IR camera under load shows this as a hot spot. Corrosion may point to junction box failure or junction box interconnection failure. If connectors or cables outside the box are affected, suspect a connector defect, which is checked by visual inspection and IR. Isolate the circuit safely first. Then inspect the box and connectors by eye for corrosion, burn marks or a damaged seal. Remember that the potting material can hide the defect.

<!-- review notes
- sentence 1: support check: partial - Passages list corroded parts within the junction box involving solder joints, wires, bypass diodes, ribbons, but 'mostly found' and 'diode connections' are slight extrapolations.
- sentence 2: support check: partial - Moisture ingress in bad/damaged boxes (adhesion loss, cracked, missing seal) leading to corrosion is stated, but passages list it as one of several causes (cold solder, loose clamping), not 'the usual cause'.
- sentence 5: support check: partial - Corrosion raising resistance and heating the box, and IR detecting the heat as a hot spot, are stated, but 'under load' for the IR camera is not stated in the junction box passages (only in the connector passage).
- sentence 6: support check: partial - Corrosion linked to junction box and interconnection failure is stated, and connector defect uses visual and IR detection, but the passages do not say corroded external connectors or cables should lead to suspecting a connector defect.
- sentence 7: support check: partial - Safe isolation and visual inspection are in the connector passage and potting hiding the defect is in the junction box passage, but the combined procedure for the box (inspect for corrosion, burn marks, damaged seal) is not stated as such.
-->
