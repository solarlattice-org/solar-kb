---
id: fc:fronius-galvo-401
type: FaultCode
name: Fronius Galvo 401
aliases:
- '401'
- Fronius 401
- No internal communication with power stage set.
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '401'
code_key: '401'
display_message: No internal communication with power stage set.
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: c066eceb8929
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r1
    h: 60dc19b5aa45
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: ec2e64e7fa7d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: c066eceb8929
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r1
    h: 60dc19b5aa45
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: ec2e64e7fa7d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: c066eceb8929
  review: drafted
  review_note: 'support check: partial - Passages show class 4 codes may need technician intervention
    and 401 auto-retries, but do not explicitly classify 401 as a fault.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Feed-in stops until communication is restored.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r1
    h: 60dc19b5aa45
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: ec2e64e7fa7d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: c066eceb8929
  review: drafted
  review_note: 'support check: partial - Passages say the inverter will attempt to reconnect and ''resume''
    grid feed, implying feed-in is interrupted, but this is not…'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Inverter reconnects automatically; service technician if persistent.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r1
    h: 60dc19b5aa45
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: ec2e64e7fa7d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: c066eceb8929
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r1
    h: 60dc19b5aa45
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: ec2e64e7fa7d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r1
    h: c066eceb8929
  review: drafted
---
