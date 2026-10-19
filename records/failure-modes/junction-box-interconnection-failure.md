---
id: fm:junction-box-interconnection-failure
type: FailureMode
name: Junction Box Interconnection Failure
aliases:
- PVFS 1-14
category: Modules
claims:
- claim_id: c1
  rel: affects
  target: comp:junction-box
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r1
    h: 3aa67d44d717
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:bypass-diode
  note: Faulty parts in the box can include bypass diodes or the connections to them.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r1
    h: 3aa67d44d717
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cell-interconnect-ribbon
  note: Tabbing ribbons inside the junction box can be involved.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r1
    h: 3aa67d44d717
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:solder-bond-defect
  note: Cold solder joints from low soldering temperature, or chemical residues on the joints.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r3
    h: 69aa96116e44
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Chemical residues left on solder joints by the earlier production process.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r3
    h: 69aa96116e44
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:thermal-cycling
  note: Day-night and seasonal cycles loosen mechanical clamped or screwed contacts.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r3
    h: 69aa96116e44
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:moisture-exposure
  note: Water gets into bad or damaged boxes (adhesion loss, cracks, missing seal) and corrodes the contacts.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r3
    h: 69aa96116e44
  review: drafted
- claim_id: c8
  rel: caused_by
  target: fm:delamination
  note: Delamination near the box can loosen it, which puts mechanical stress on the internal contacts
    and breaks them.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r3
    h: 69aa96116e44
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:mechanical-stress
  note: A loosened junction box puts stress on its internal contacts.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r3
    h: 69aa96116e44
  review: drafted
- claim_id: c10
  rel: caused_by
  target: fm:junction-box-failure
  note: In the worst case, junction box failures result in short-circuited or open-circuited module or
    cell strings.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
  review_note: 'support check: partial - u14 says junction box failures cause interconnection failure
    in the worst case, but this reverses the direction, since the interconnection failure is the subject,
    not an effect of the box failure as a cause.'
- claim_id: c11
  rel: presents_as
  target: symptom:contact-corrosion
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r1
    h: 3aa67d44d717
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:burn-marks
  note: Resistive heating can burn the encapsulant or backsheet behind and around the box.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:yellow-brown-discoloration
  note: Potting material, encapsulant or backsheet can yellow or brown from heat.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r1
    h: 3aa67d44d717
  review: drafted
  review_note: 'support check: partial - The potting material is said to appear yellowed/browned from
    heat, but the encapsulant or backsheet is described only as discoloured, not specifically yellow or
    brown.'
- claim_id: c14
  rel: presents_as
  target: symptom:hotspot-ir-image
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c15
  rel: presents_as
  target: symptom:open-circuit
  note: Depends on whether the bad contact is resistive, open, shorted or arcing.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: drafted
  review_note: 'support check: partial - Open circuit is mentioned as one possible character depending
    on the contact, but an open string circuit is not a firmly stated symptom.'
- claim_id: c16
  rel: leads_to
  target: fm:glass-breakage
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: drafted
- claim_id: c17
  rel: leads_to
  target: fm:arc-fault
  note: Internal arcing in the box can start a fire.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: drafted
- claim_id: c18
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c19
  rel: detected_by
  target: method:el-imaging
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: drafted
- claim_id: c20
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: drafted
- claim_id: c21
  rel: detected_by
  target: method:iv-curve-tracing
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c22
  rel: detected_by
  target: method:voc-measurement
  note: Shorts can be found with an open-circuit measurement.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c23
  rel: detected_by
  target: method:junction-box-inspection
  note: The fault may be hidden under potting material and only show once the potting is removed.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r1
    h: 3aa67d44d717
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:module-replacement
  note: Repairing junction boxes can easily cause new fires.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c25
  rel: mitigated_by
  target: mit:junction-box-sealing
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c26
  rel: mitigated_by
  target: mit:safety-isolation
  note: Give priority to isolation when there is evidence of arcing or burning.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  review: drafted
  review_note: 'support check: partial - u10 advises prioritizing safety isolation for arcing or burn
    evidence, but it concerns junction-box failures generally rather than this interconnection failure
    specifically.'
---
This failure is a bad connection inside the module junction box. Solder joints, wires, bypass diodes or tabbing ribbons can be disconnected, broken, burned, corroded or shorted. Typical causes are cold solder joints, residues on the joints, clamps or screws loosened by thermal cycling, and moisture getting into damaged boxes and corroding the contacts. Delamination that loosens the box can also break the contacts. Look for yellowed, browned, burned or bubbled potting, and for burn marks or discoloration behind and around the box. The fault itself may only be visible after the potting is removed. An IR camera shows the box as a hot spot. IV curves or open-circuit voltage measurements can confirm shorts, and the module may lose power or lose its protection against shading. Arcing in the box can start a fire, so treat any burn evidence as a safety issue and isolate the module first. Replace the module rather than repair the box, because repairs can easily lead to new fires. Good sealing of the junction box helps prevent the fault.
