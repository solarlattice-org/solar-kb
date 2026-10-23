---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-protect30
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Protect0030
aliases:
- Protect0030
- protect30
- Yaskawa Solectria Protect0030
- Inverter Over Current
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Protect0030
code_key: protect30
display_message: Inverter Over Current
vendor_severity: Protection
page: 80
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r3
    h: 0ea62c5cf5f4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r3
    h: 0ea62c5cf5f4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:overcurrent
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r3
    h: 0ea62c5cf5f4
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r3
    h: 0ea62c5cf5f4
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; replace the inverter if the fault persists
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r3
    h: 0ea62c5cf5f4
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the restart does not clear it
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r3
    h: 0ea62c5cf5f4
  review: drafted
---
