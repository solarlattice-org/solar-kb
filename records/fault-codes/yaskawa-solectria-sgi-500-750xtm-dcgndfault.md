---
id: fc:yaskawa-solectria-sgi-500-750xtm-dcgndfault
type: FaultCode
name: Yaskawa Solectria SGI-XTM DC GND Fault
aliases:
- DC GND Fault
- dcgndfault
- Yaskawa Solectria DC GND Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: DC GND Fault
code_key: dcgndfault
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  review: drafted
  review_note: 'support check: partial - The passage says to locate the source of the ground fault, but
    doesn''t say the fault is detected by a…'
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  note: Qualified person must locate and repair the ground fault.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  review: drafted
---
