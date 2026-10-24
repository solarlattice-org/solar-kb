---
id: fc:fronius-primo-502
type: FaultCode
name: Fronius Primo 502
aliases:
- '502'
- Fronius 502
- Insulation fault on solar modules
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '502'
code_key: '502'
display_message: Insulation fault on solar modules
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: 7d45ec2e0255
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h21
    h: a6a4378aca92
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r1
    h: 69d75eb54160
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: 7d45ec2e0255
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r1
    h: 49ed787b3dfd
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r1
    h: 69d75eb54160
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: 7d45ec2e0255
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r1
    h: 49ed787b3dfd
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r1
    h: 69d75eb54160
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: 7d45ec2e0255
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r1
    h: 49ed787b3dfd
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r1
    h: 69d75eb54160
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: 7d45ec2e0255
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r1
    h: 49ed787b3dfd
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r1
    h: 69d75eb54160
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
  review_note: 'support check: partial - Class 5 generally doesn''t impair feed-in, but u18 doesn''t tie
    502 to class 5, and ''can lead to limitations''.'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-installer
  note: When the code keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: 7d45ec2e0255
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r1
    h: 49ed787b3dfd
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:fronius-primo
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: 7d45ec2e0255
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h21
    h: a6a4378aca92
  review: drafted
---
