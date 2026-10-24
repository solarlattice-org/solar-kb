---
id: fc:abb-uno-dm-3-3-5-0-plus-us-e21
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS E021
aliases:
- E021
- e21
- ABB / FIMER E021
- Self Test Error 2
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: E021
code_key: e21
display_message: Self Test Error 2
vendor_severity: Error
page: 130
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 24b72e3809f1
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r4
    h: c94caf9a5bcc
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 24b72e3809f1
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r4
    h: c94caf9a5bcc
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r5
    h: 6a71fb7b8854
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r8
    h: c70575f41d54
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 24b72e3809f1
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r4
    h: c94caf9a5bcc
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r1
    h: f7c812f235a0
  review: drafted
- claim_id: c5
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r5
    h: 6a71fb7b8854
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r8
    h: c70575f41d54
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 24b72e3809f1
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:grid-relay
  note: Relay of the DC-AC inverter stage.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r5
    h: 6a71fb7b8854
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r8
    h: c70575f41d54
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 24b72e3809f1
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Occurs only before grid connection, so the inverter does not connect.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r5
    h: 6a71fb7b8854
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r8
    h: c70575f41d54
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 24b72e3809f1
  review: drafted
  review_note: 'support check: partial - The passages say the alarm occurs only before grid connection,
    but they do not state that production stops or that…'
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r5
    h: 6a71fb7b8854
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r8
    h: c70575f41d54
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r5
    h: 6a71fb7b8854
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r8
    h: c70575f41d54
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the fault persists afterwards.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r5
    h: 6a71fb7b8854
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r8
    h: c70575f41d54
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 24b72e3809f1
  review: drafted
  review_note: 'support check: partial - A power cycle is advised, but the passages never say the fault
    clears by manual reset.'
- claim_id: c11
  rel: applies_to
  target: prod:abb-uno-dm-3-3-5-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r3
    h: 24b72e3809f1
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=54.r4
    h: c94caf9a5bcc
  review: drafted
---
