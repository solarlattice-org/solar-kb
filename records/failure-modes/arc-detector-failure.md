---
id: fm:arc-detector-failure
type: FailureMode
name: Arc detection board failure
aliases:
- Arcboard Err
- arc board err
- Arc Board Error
- Arcboard error
claims:
- claim_id: c1
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=39.r3
    h: 99d70367a788
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=42.r6
    h: 4ea475188b04
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.4
    h: 50f6c0ff2497
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.4
    h: f90171d02e8b
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:inverter
  note: The arc detection board sits inside the inverter and passes arc signals to the control board DSP.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.4
    h: 50f6c0ff2497
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.4
    h: f90171d02e8b
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:poor-connector-contact
  note: The listed possible cause is poor contact at the arc board or damage to the board.
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=42.r6
    h: 4ea475188b04
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=42
    h: 2a25ca716edf
  review: drafted
  review_note: 'support check: partial - Poor contact or damage of Arcboard is a listed cause, but the
    statement attributes it to generic poor connector contact, which is only partly the same (damage is
    another cause).'
- claim_id: c4
  rel: presents_as
  target: symptom:self-test-failure
  note: Reported as an internal arc board self-check error or an abnormal reading inside the arc board.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r3
    h: c279ec78fba0
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:inverter-shutdown
  note: The inverter stays off the grid until the arc board is working again.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.4
    h: 50f6c0ff2497
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.4
    h: f90171d02e8b
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:inverter-display-check
  note: The LCD shows 'arc board err'.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.4
    h: 50f6c0ff2497
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.4
    h: f90171d02e8b
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:arc-fault-self-test
  note: Run the Arc Fault Test from the Settings menu. If the alarm comes back, the board is faulty.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=39.r3
    h: 99d70367a788
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=63.r3
    h: 99d70367a788
  review: drafted
  review_note: 'support check: partial - Run Arc Fault Test and if alarm re-occurs contact service is
    stated, but not explicitly that the test is a detection method or that a recurrence means the board
    is faulty.'
- claim_id: c8
  rel: mitigated_by
  target: mit:arc-board-connector-check
  note: Make sure the logic connector to the arc board is secure and the board is in good condition.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=39.r3
    h: 99d70367a788
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=63.r3
    h: 99d70367a788
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=42.r7
    h: efe8b49b988f
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:arc-board-replacement
  note: CPS Service replaces the arc board or the wiring box if the alarm comes back.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=39.r3
    h: 99d70367a788
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r3
    h: 99d70367a788
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=63.r3
    h: 99d70367a788
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=39.r3
    h: 99d70367a788
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=42.r7
    h: efe8b49b988f
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r3
    h: c279ec78fba0
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:inverter-restart
  note: Switch the inverter back on. If the error stays, contact customer service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r3
    h: c279ec78fba0
  review: drafted
- claim_id: c12
  rel: distinguished_from
  target: fm:arc-fault
  by: method:inverter-display-check
  note: '''ARC Protect'' means the board detected an actual arc in the PV input, and that fault is cleared
    manually. ''Arcboard Err'' means the detection board itself has poor contact or is damaged.'
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=42
    h: 2a25ca716edf
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.4
    h: 50f6c0ff2497
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.4
    h: f90171d02e8b
  review: drafted
---
This fault is in the inverter's arc detection board, which watches the PV lines for arcing and signals the control board to take the inverter off the grid. When the board fails, the display shows an arc board error and the inverter will not connect to the grid until the board works again. Likely causes are poor contact at the arc board or a damaged board. Some models also report it as a failed internal self-check of the board. First make sure the logic connector to the arc board is secure and the board looks to be in good condition. Then run the Arc Fault Test from the Settings menu, or clear the fault with the ARCFaultClear command. If the alarm comes back, contact the manufacturer's service team to replace the arc board or the wiring box. Do not mix this up with the ARC Protect alarm. That alarm means an actual arc was detected in the PV input.
