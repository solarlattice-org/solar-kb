---
id: fc:solis-s5-gc-us-inifault
type: FaultCode
name: Solis S5-GC INI-FAULT
aliases:
- INI-FAULT
- inifault
- Solis INI-FAULT
- Initialization Protect ion
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: INI-FAULT
code_key: inifault
display_message: Initialization Protect ion
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r1
    h: eed118aa3df4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r1
    h: eed118aa3df4
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:control-board
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r1
    h: eed118aa3df4
  review: drafted
  review_note: 'support check: partial - DSP mismatch implies control board, but the component is not
    named in the passage.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r1
    h: eed118aa3df4
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r1
    h: eed118aa3df4
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15
    h: cb7b6f9ed265
  review: drafted
  review_note: 'support check: partial - Listed under ''Fault messages'' table and requires intervention,
    but the row doesn''t explicitly classify it; reasonably implied.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replace inverter if it persists.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r1
    h: eed118aa3df4
  review: drafted
---
