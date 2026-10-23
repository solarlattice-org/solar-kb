---
id: fc:abb-pvs-60-tl-us-e103
type: FaultCode
name: ABB / FIMER PVS-60-TL E103
aliases:
- E103
- e103
- ABB / FIMER E103
- RSD self-test fault
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E103
code_key: e103
display_message: RSD self-test fault
vendor_severity: Error
page: 159
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r10
    h: ef43f4334923
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r10
    h: ef43f4334923
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:rapid-shutdown-failure
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r10
    h: ef43f4334923
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r10
    h: ef43f4334923
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r10
    h: ef43f4334923
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the fault persists.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r10
    h: ef43f4334923
  review: drafted
  review_note: 'support check: partial - Power cycle then contact service is stated, but the passage doesn''t
    say the fault clears by manual reset.'
---
