---
id: fc:abb-uno-dm-6-0-plus-us-e36
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E036
aliases:
- E036
- e36
- ABB / FIMER E036
- Vout Avg error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E036
code_key: e36
display_message: Vout Avg error
vendor_severity: Error
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r9
    h: 7f3fd1cd002b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4cf089ad2e99
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r9
    h: 7f3fd1cd002b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4cf089ad2e99
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:grid-overvoltage
  note: 10-minute average grid voltage out of range
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r4
    h: 583e72fc7b36
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r9
    h: 7f3fd1cd002b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4cf089ad2e99
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r7
    h: 921158d765d7
  review: drafted
  review_note: 'support check: partial - 10-minute average grid voltage too high is stated, but ''overvoltage''
    is phrased as out of range/too high; broadly supported though…'
- claim_id: c5
  rel: reports
  target: symptom:grid-impedance-high
  note: Stated as possible cause
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r4
    h: 583e72fc7b36
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r9
    h: 7f3fd1cd002b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4cf089ad2e99
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r7
    h: 921158d765d7
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r4
    h: 583e72fc7b36
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r9
    h: 7f3fd1cd002b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4cf089ad2e99
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r7
    h: 921158d765d7
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r4
    h: 583e72fc7b36
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r9
    h: 7f3fd1cd002b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4cf089ad2e99
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r7
    h: 921158d765d7
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only if grid operator authorises new limits
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r4
    h: 583e72fc7b36
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r9
    h: 7f3fd1cd002b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4cf089ad2e99
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r7
    h: 921158d765d7
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:derate
  note: Limits power first, disconnects if voltage does not stabilise; no single limit value stated
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r4
    h: 583e72fc7b36
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r9
    h: 7f3fd1cd002b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4cf089ad2e99
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r7
    h: 921158d765d7
  review: drafted
---
