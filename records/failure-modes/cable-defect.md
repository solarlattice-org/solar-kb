---
id: fm:cable-defect
type: FailureMode
name: Cable Defect
claims:
- claim_id: c1
  rel: affects
  target: comp:dc-cable
  note: Cables run across the whole array and connect its elements.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h3
    h: 24187737e6d1
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:undersized-component
  note: Undersized cables chosen at the design stage.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:low-quality-material
  note: Poor insulation material or copper wire used in cable production.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:installation-error
  note: Improper handling or fixing during installation, e.g. cables hanging near connections or missing
    fixings.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:mechanical-stress
  note: Routing over sharp or abrading edges and bending too tightly.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:uv-exposure
  note: Design choices with inadequate UV protection or IP class; exposed wiring needs UV protection.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r3
    h: 091be96f279b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r3
    h: 091be96f279b
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  review: drafted
  review_note: 'support check: partial - Inadequate UV protection in design is cited as a cause, but UV
    exposure as a stressor is only implied.'
- claim_id: c7
  rel: caused_by
  target: stressor:animal-activity
  note: Animal bites on cables are shown.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: fig=1
    h: 7ede5cd7e80d
  review: drafted
- claim_id: c8
  rel: leads_to
  target: fm:insulation-loss
  note: Insulation fault is a main cable defect; it can be intermittent depending on humidity, and if
    leakage stays below protection-device ratings it can go undetected.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  review: drafted
- claim_id: c9
  rel: leads_to
  target: fm:arc-fault
  note: Damaged cables can produce electric arcs that may cause fire.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:ground-fault
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:open-circuit
  note: An open wiring circuit causes significant string-level power loss.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:string-current-low
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  review: drafted
  review_note: 'support check: partial - String-level power losses and string current comparison are mentioned,
    but reduced string current output isn''t explicitly stated.'
- claim_id: c13
  rel: presents_as
  target: symptom:series-resistance-increase
  note: Early corrosion raises series resistance, so more power is dissipated as heat.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  review: drafted
- claim_id: c14
  rel: presents_as
  target: symptom:visible-corrosion
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: fig=1
    h: 7ede5cd7e80d
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  review: drafted
  review_note: 'support check: partial - A corroded cable is shown in the figure, but corrosion as a visible
    symptom is not explicitly stated for cables.'
- claim_id: c15
  rel: presents_as
  target: symptom:melted-component
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c16
  rel: presents_as
  target: symptom:burn-marks
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c17
  rel: presents_as
  target: symptom:cracked-insulation
  note: Damaged cables may look brittle, broken or cracked.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c18
  rel: presents_as
  target: symptom:whitened-insulation
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c19
  rel: presents_as
  target: symptom:hotspot-ir-image
  note: Overheating, often visible early in thermography.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c20
  rel: detected_by
  target: method:visual-inspection
  note: Lets you scan for cable defects quickly.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r2
    h: a141b04a3d40
  review: drafted
- claim_id: c21
  rel: detected_by
  target: method:ir-thermography
  note: Helps detect early symptoms.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r2
    h: a141b04a3d40
  review: drafted
- claim_id: c22
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c23
  rel: detected_by
  target: method:string-current-measurement
  note: Compare string currents.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c24
  rel: detected_by
  target: method:fault-localization
  note: Done on isolated circuits.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c25
  rel: mitigated_by
  target: mit:cable-replacement
  note: Replace damaged cable runs.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c26
  rel: mitigated_by
  target: mit:proper-cable-routing
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c27
  rel: mitigated_by
  target: mit:cable-strain-relief
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c28
  rel: mitigated_by
  target: mit:cable-protection
  note: Shield exposed wiring from UV and mechanical damage.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c29
  rel: mitigated_by
  target: mit:post-repair-verification
  note: Confirm insulation integrity after the repair.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
  review_note: 'support check: partial - Confirming insulation integrity after repair is stated, but not
    a full post-repair string verification.'
---
A cable defect is damage to the DC cabling that connects the parts of a PV array, and it is rated as a high-severity failure. Common causes are poor cable materials, undersized cables or weak UV protection chosen at the design stage, and poor installation, such as routing over sharp edges or bending cables too tightly. Damaged cables can look melted, burned, brittle, cracked or whitened, and they may show corrosion or animal bites. The defect can cause insulation and ground faults, open string circuits with large power loss, higher series resistance with extra heat, and arcs that can start a fire. Insulation faults may come and go with humidity, and they can stay hidden if the leakage current is below what the protection devices react to. To confirm the fault, do a visual inspection and an infrared inspection, test insulation resistance, compare string currents, and locate the fault on isolated circuits.
