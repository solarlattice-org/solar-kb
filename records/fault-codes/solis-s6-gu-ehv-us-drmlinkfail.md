---
id: fc:solis-s6-gu-ehv-us-drmlinkfail
type: FaultCode
name: Solis S6-GU DRM LINK Fail
aliases:
- DRM LINK Fail
- drmlinkfail
- Solis DRM LINK Fail
- DRM link failed
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: DRM LINK Fail
code_key: drmlinkfail
display_message: DRM link failed
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r7
    h: d4b37f841572
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r7
    h: d4b37f841572
  review: drafted
  review_note: 'support check: partial - DRM link failed is stated, but this is a link failure for a demand
    response interface, and communication loss is…'
- claim_id: c3
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r7
    h: d4b37f841572
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r7
    h: d4b37f841572
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r7
    h: d4b37f841572
  review: drafted
  review_note: 'support check: partial - Fault class is not explicit in the row.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; then check DRM cabling and signal state.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r7
    h: d4b37f841572
  review: drafted
  review_note: 'support check: partial - Steps are listed, but manual reset clearing is not explicit.'
---
