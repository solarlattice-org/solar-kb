---
id: fc:fronius-galvo-245
type: FaultCode
name: Fronius Galvo 245
aliases:
- '245'
- Fronius 245
- Arc detector self test failed
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '245'
code_key: '245'
display_message: Arc detector self test failed
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r8
    h: 19024dbb3bbd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r10
    h: 40b54395aa42
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r8
    h: 19024dbb3bbd
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r10
    h: 40b54395aa42
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r8
    h: 19024dbb3bbd
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:arc-fault-self-test
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r10
    h: 40b54395aa42
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r8
    h: 19024dbb3bbd
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  note: AC reset repeats the test; contact service if it persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r10
    h: 40b54395aa42
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r8
    h: 19024dbb3bbd
  review: drafted
  review_note: 'support check: partial - The passages say to carry out an AC reset (which repeats the
    test) and to contact service if the code…'
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r10
    h: 40b54395aa42
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r8
    h: 19024dbb3bbd
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r10
    h: 40b54395aa42
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r8
    h: 19024dbb3bbd
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Escalate to trained service technician if code persists after AC reset.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r10
    h: 40b54395aa42
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r8
    h: 19024dbb3bbd
  review: drafted
---
