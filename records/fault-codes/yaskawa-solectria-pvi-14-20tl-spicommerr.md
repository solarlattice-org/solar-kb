---
id: fc:yaskawa-solectria-pvi-14-20tl-spicommerr
type: FaultCode
name: Yaskawa Solectria PVI-14-20TL SPICommErr
aliases:
- SPICommErr
- spicommerr
- Yaskawa Solectria SPICommErr
- Inverters internal communication failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-14-20tl
family_name: Solectria PVI 14/20TL
code: SPICommErr
code_key: spicommerr
display_message: Inverters internal communication failure
vendor_severity: Alarm
page: 47
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r5
    h: 7d1bf3da26db
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r6
    h: 3a1c8ce5d364
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r7
    h: d98c5f0c72f2
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r8
    h: e312e5d62cb1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r5
    h: 7d1bf3da26db
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r6
    h: 3a1c8ce5d364
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r7
    h: d98c5f0c72f2
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r8
    h: e312e5d62cb1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r3
    h: 212b80f52fcc
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r5
    h: 7d1bf3da26db
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Observe for automatic clearing first; then power cycle, then contact service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r3
    h: 212b80f52fcc
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=10.r5
    h: 7d1bf3da26db
  review: drafted
  review_note: 'support check: partial - The row says to observe for 5 minutes to see whether the alarm
    clears automatically, but a power cycle and…'
---
