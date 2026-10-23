---
id: symptom:phase-sequence-error
type: Symptom
name: Incorrect phase sequence
aliases:
- Reverse Phase
- Left-hand rotating magnetic field
- A-C-B negative sequence
- CCW (ACB)
- Two crossed phases
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Reported as SGI-XTM 'Reverse Phase' or fault value 32 'Incorrect Phase Sequence', and as SMA SC-CP-XT
    error 1301 (left-hand rotating field connected).
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=38.r4
    h: 74a0eb6f0437
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r13
    h: 1e53ae5f741f
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r8
    h: 893caf77b61f
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=31.r1
    h: e3cf56a7121a
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:phase-sequence-register-acb
  note: The Yaskawa Modbus phase sequence register reads 0 for not locked, 1 for CW (ABC) and 2 for CCW
    (ACB); a reading of 2 means the rotation is reversed.
  cite:
  - src: src:yaskawa-modbus-level-8-sgi-xtm-docr-070522-b
    loc: sec=h20
    h: c4ec175d96a2
  - src: src:yaskawa-modbus-level-5-pvi-50-100kw-docr-070381-b
    loc: sec=h17
    h: bc3c5b332698
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:zero-ac-output
  note: With negative-sequence rotation the inverter will not run.
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h62
    h: 1315812c9671
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r13
    h: 1e53ae5f741f
  review: drafted
  review_note: 'support check: partial - Passages say the inverter will not run with negative sequence,
    but do not state the W zero reading while grid and DC are present.'
- claim_id: c4
  rel: observed_as
  target: meas:pll-lock-error
  note: A PLL error, or frequency and voltage readings that look wrong, is a reason to check the phase
    rotation.
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h62
    h: 1315812c9671
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:negative-sequence-current-imbalance
  note: Two crossed phases are found by measuring negative-sequence current.
  cite:
  - src: src:sel-acselerator-quickset-instruction-manual
    loc: tbl=47
    h: 6ad65973ecf9
  review: drafted
---
An incorrect phase sequence means the inverter's three-phase AC output is wired in A-C-B (negative or counter-clockwise) rotation instead of the A-B-C positive rotation the inverter needs. The inverter will not run in this state and reports a fault, for example Reverse Phase on SGI-XTM units or error 1301 for a left-hand rotating field on SMA Sunny Central CP-XT units. On Yaskawa units the Modbus phase sequence register shows the rotation directly: 1 means CW (ABC), 2 means CCW (ACB) and 0 means not locked. A phase lock loop error, or frequency and voltage readings that look wrong, can also point to reversed rotation. Check the rotation before you suspect a sensor fault. Crossed phases also show up as negative-sequence current. A Reverse Phase message is different from an Open Phase message, which means one phase is missing at the inverter. First check the phase position at the inverter AC terminals and make sure all fuses are switched on. To fix it, have an electrician swap any two AC phase conductors at the inverter output terminals, then restart the inverter. Where a site meter is used, its phase order should match the order at the inverter grid port.

<!-- review notes
- sentence 4: support check: partial - PLL error or odd readings pointing to rotation is stated, but the advice to check before suspecting a sensor fault is not in the passage.
- sentence 6: support check: partial - Check phase position and fuses switched on are stated in u9, but 'at the inverter AC terminals' and 'first' ordering are not stated.
-->
