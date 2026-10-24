---
id: hazard:ground-fault-energized-conductor
type: Hazard
name: Energized conductors during a ground fault
aliases:
- normally grounded conductors may be energized
- shock hazard during ground fault
category: Electrical
claims:
- claim_id: c1
  rel: subclass_of
  target: hazard:electric-shock
  note: A ground fault can leave conductors that are normally grounded ungrounded and live, so touching
    them can shock you.
  cite:
  - src: src:std-standards-nec-2011-2011-nec2011-690
    loc: sec=h9
    h: c0ef2aee7c7e
  - src: src:std-standards-nec-2014-nec2014-690
    loc: sec=h7
    h: 91246ea457d3
  - src: src:sma-sc-up-scs-up-eze-sg-en-10
    loc: sec=h28
    h: 13be58b020f3
  - src: src:yaskawa-solectria-dsp-yellowstone
    loc: sec=h21
    h: 07a3f3cfe72a
  - src: src:enphase-enphase-m190-m210-installation-and-operation-guide
    loc: sec=h15
    h: 4f4bd1150c08
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:ground-fault-warning-label
  scope:
    standard: std:nfpa-70-2014
  note: When the PV system has batteries, the installer must also put the same warning in a visible place
    at the batteries.
  quote: ELECTRIC SHOCK HAZARD IF A GROUND FAULT IS INDICATED, NORMALLY GROUNDED CONDUCTORS MAY BE UNGROUNDED
    AND ENERGIZED
  quote_source: NFPA 70 (NEC) 2014 Article 690
  cite:
  - src: src:std-standards-nec-2014-nec2014-690
    loc: sec=h7
    h: 91246ea457d3
  review: drafted
  review_note: 'support check: partial - u36 gives the label and battery requirement, but the NFPA 70-2014
    edition is not named in the passage.'
- claim_id: c3
  rel: controlled_by
  target: mit:ground-fault-warning-label
  scope:
    standard: std:nfpa-70-2011
  quote: ELECTRIC SHOCK HAZARD IF A GROUND FAULT IS INDICATED, NORMALLY GROUNDED CONDUCTORS MAY BE UNGROUNDED
    AND ENERGIZED
  quote_source: NFPA 70 (NEC) 2011 Article 690
  cite:
  - src: src:std-standards-nec-2011-2011-nec2011-690
    loc: sec=h9
    h: c0ef2aee7c7e
  review: drafted
  review_note: 'support check: partial - u1 gives the label, but the 2011 NEC edition is not stated in
    the passage.'
- claim_id: c4
  rel: controlled_by
  target: proc:verify-absence-of-voltage
  note: Check that no voltage is present before touching any PV equipment.
  cite:
  - src: src:yaskawa-solectria-dsp-yellowstone
    loc: sec=h21
    h: 07a3f3cfe72a
  - src: src:yaskawa-solectria-yaskawa-customer-facing-instructions-full
    loc: sec=h94
    h: 9930df551827
  - src: src:yaskawa-solectria-yaskawa-customer-facing-instructions-full
    loc: sec=h132
    h: 9930df551827
  - src: src:yaskawa-solectria-yaskawa-customer-facing-instructions-full
    loc: sec=h21
    h: f992f523e67d
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: tool:personal-protective-equipment
  note: SMA asks for PPE matched to the hazard risk category of each area whenever the power transmission
    path is connected.
  cite:
  - src: src:sma-sc-up-scs-up-eze-sg-en-10
    loc: sec=h28
    h: 13be58b020f3
  - src: src:yaskawa-solectria-dsp-yellowstone
    loc: sec=h21
    h: 07a3f3cfe72a
  - src: src:yaskawa-solectria-yaskawa-customer-facing-instructions-full
    loc: sec=h94
    h: 9930df551827
  review: drafted
- claim_id: c6
  rel: controlled_by
  target: mit:safety-isolation
  note: If the work does not need voltage, disconnect the inverter from both the power path and the control
    path. Also confirm that no ground fault is present before starting.
  cite:
  - src: src:sma-sc-up-scs-up-eze-sg-en-10
    loc: sec=h28
    h: 13be58b020f3
  review: drafted
- claim_id: c7
  rel: controlled_by
  target: mit:ground-fault-detection
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  note: The SGI 500/750XTM has DC ground fault protection per UL 1741. A yellow Ground Fault indicator
    warns that normally grounded conductors may be energized.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=37.r1
    h: 77f74a8e78e5
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=h81
    h: 9287ffb0935a
  review: drafted
  review_note: 'support check: partial - Passages give UL 1741 DC ground fault protection and the yellow
    Ground Fault indicator warning, but don''t tie them together as ''continuous detection'' control or
    say the indicator is for the XTM specifically.'
---
A ground fault can leave conductors that are normally grounded ungrounded and energized, so a part you expect to be at ground potential may give a shock. In a ground fault, parts that are supposed to be grounded may be live and parts that are normally ungrounded may become grounded; touching live parts can cause death or serious injury. The PV field is not grounded while the inverter is disconnected or while insulation resistance is being measured. In functionally grounded PV systems, conductors normally at ground potential may have voltage to ground under fault conditions. The NEC requires a warning label for this hazard, and in systems with batteries the same label must also go in a visible place at the batteries. Before touching PV equipment, verify the absence of voltage and make sure no ground fault is present, and wear suitable personal protective equipment. If the work does not need voltage, disconnect the inverter from both the power path and the control path.

<!-- review notes
- sentence 5: support check: partial - Passages show the warning and battery placement with 'shall', but 'NEC' is not named in the passages (u36 cites 110.21(B), implying code).
-->
