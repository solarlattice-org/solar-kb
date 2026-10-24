---
id: fc:yaskawa-solectria-pvi-14-20tl-intfaultao
type: FaultCode
name: Yaskawa Solectria PVI-14-20TL IntFaultA~O
aliases:
- IntFaultA~O
- intfaultao
- Yaskawa Solectria IntFaultA~O
- Internal noncritical fault within the inverter
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-14-20tl
family_name: Solectria PVI 14/20TL
code: IntFaultA~O
code_key: intfaultao
display_message: Internal noncritical fault within the inverter
vendor_severity: Fault
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r7
    h: ebf5185427b9
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r8
    h: a48c7bedc73f
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r7
    h: ebf5185427b9
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r8
    h: a48c7bedc73f
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r7
    h: ebf5185427b9
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r8
    h: a48c7bedc73f
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r7
    h: ebf5185427b9
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Restarts once the fault clears; if it persists, contact service
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r7
    h: ebf5185427b9
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r8
    h: a48c7bedc73f
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the fault persists
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r8
    h: a48c7bedc73f
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-14-20tl
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r7
    h: ebf5185427b9
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r8
    h: a48c7bedc73f
  review: drafted
---
