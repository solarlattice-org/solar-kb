---
id: concept:electromagnetic-compatibility
type: Concept
name: Electromagnetic compatibility
aliases:
- EMC
- EMI
- electromagnetic interference
- Electro-Magnetic Compatibility
category: Inverters
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: std:eu-emc-2014-30
  note: Equipment datasheets state EMC conformance with this EU directive.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-power-supply-phoenix-contact-84w-2904945
    loc: tbl=19.r2
    h: 9bcabc7cfafa
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=15.r5
    h: e2b282856fa3
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:iec-61000-6-2
  note: Generic EMC immunity standard for industrial environments.
  cite:
  - src: src:eq-equip-meters-sel-735-sel-735-manual-735-im-20250711
    loc: sec=h101
    h: 6719e03eb80b
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: tbl=15
    h: 2526f3c7ae3c
  review: drafted
- claim_id: c3
  rel: related_to
  target: std:en-55022
  note: Listed among inverter-related standards for radio disturbance limits and measurement.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: tbl=15
    h: 2526f3c7ae3c
  review: drafted
- claim_id: c4
  rel: related_to
  target: symptom:radio-frequency-interference
  note: EMC-related problems in PV installations often stem from installation characteristics rather than
    defective equipment.
  cite:
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h5
    h: 315f2eccd25d
  review: drafted
  review_note: 'support check: partial - Passage says EMC issues originate from installation rather than
    equipment defects, but doesn''t mention radio frequency interference specifically.'
- claim_id: c5
  rel: related_to
  target: concept:power-quality
  note: IEC 61000-4-30 is an EMC standard defining power quality measurement methods.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=G.6
    h: eff0f3de5fd9
  review: drafted
- claim_id: c6
  rel: related_to
  target: comp:inverter
  note: PV inverters must meet EMC emission and immunity standards.
  cite:
  - src: src:sma-kb-electromagnetic-compatibility-emc-of-sma-inverters
    loc: sec=h1
    h: cdcfe414d5fd
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: tbl=15
    h: 2526f3c7ae3c
  review: drafted
---
Electromagnetic compatibility (EMC) covers how electrical devices affect each other through the electromagnetic fields they produce. Devices should not keep interfering with one another on the AC side. PV inverters are held to the same EMC standards as household appliances such as hair dryers and refrigerators. EMC standards cover two things: emission, meaning how much interference a device gives off, and immunity, meaning how well it resists interference from outside. Each has separate versions for residential and commercial settings and for industrial settings. Equipment sold in Europe declares conformance with the EMC Directive 2014/30/EU. SMA lists the EMC standards each inverter meets in the EC declaration of conformity that ships with it. In the field, many EMC problems, such as radio frequency interference, come from how the system was installed rather than from faulty equipment, so check the installation first.

<!-- review notes
- sentence 4: support check: partial - Directive conformance and SMA's EC declaration listing standards are stated, but 'equipment sold in Europe' declaring conformance is a generalization not stated.
- sentence 5: support check: partial - Passage supports many EMC issues stemming from installation not defects, but not the RFI example or the advice to check installation first.
-->
