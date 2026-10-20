---
id: fc:yaskawa-solectria-pvi-23-36tl-spicommerr
type: FaultCode
name: Yaskawa Solectria PVI-TL SPICommErr
aliases:
- SPICommErr
- spicommerr
- Yaskawa Solectria SPICommErr
- Inverter's internal communication failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: SPICommErr
code_key: spicommerr
display_message: Inverter's internal communication failure
vendor_severity: Alarm
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r3
    h: 212b80f52fcc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r3
    h: 212b80f52fcc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r3
    h: 212b80f52fcc
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r3
    h: 212b80f52fcc
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: May clear on its own; otherwise restart via disconnects, then contact customer service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r3
    h: 212b80f52fcc
  review: drafted
---
