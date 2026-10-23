---
id: fc:abb-pvs-166-175-tl-us-e22
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E022
aliases:
- E022
- e22
- ABB / FIMER E022
- Internal error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E022
code_key: e22
display_message: Internal error
vendor_severity: Error
page: 141
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r6
    h: 16c6168ef8a6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r6
    h: 16c6168ef8a6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  note: Relay self-test execution time exceeded.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r6
    h: 16c6168ef8a6
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r9
    h: 8d661a7f9a76
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r4
    h: 6bbf5a194778
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r5
    h: 35a7c8008f4b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r2
    h: ea2013540e1e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r6
    h: 16c6168ef8a6
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r9
    h: 8d661a7f9a76
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r4
    h: 6bbf5a194778
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r6
    h: 16c6168ef8a6
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r9
    h: 8d661a7f9a76
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r6
    h: 16c6168ef8a6
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r9
    h: 8d661a7f9a76
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the fault persists afterwards.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r6
    h: 16c6168ef8a6
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r9
    h: 8d661a7f9a76
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r4
    h: 6bbf5a194778
  review: drafted
  review_note: 'support check: partial - A power cycle is advised, but the passages never say the fault
    clears by manual reset.'
---
