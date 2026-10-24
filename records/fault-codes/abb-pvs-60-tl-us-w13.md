---
id: fc:abb-pvs-60-tl-us-w13
type: FaultCode
name: ABB / FIMER PVS-60-TL W013
aliases:
- W013
- w13
- ABB / FIMER W013
- Clock Fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: W013
code_key: w13
display_message: Clock Fail
vendor_severity: Warning
page: 153
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r2
    h: 88a78499bebd
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r2
    h: 88a78499bebd
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inaccurate-clock-time
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r2
    h: 88a78499bebd
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r3
    h: 521d4f5ca817
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r3
    h: 521d4f5ca817
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: 86ae0daffc97
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r3
    h: 86ae0daffc97
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:real-time-clock-failure
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r2
    h: 88a78499bebd
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r3
    h: 521d4f5ca817
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r3
    h: 521d4f5ca817
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: 86ae0daffc97
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r3
    h: 86ae0daffc97
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:real-time-clock
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r2
    h: 88a78499bebd
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r3
    h: 521d4f5ca817
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r3
    h: 521d4f5ca817
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: 86ae0daffc97
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r3
    h: 86ae0daffc97
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:backup-battery-replacement
  note: When date/time resets to default after power cycle
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r3
    h: 521d4f5ca817
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r3
    h: 521d4f5ca817
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: 86ae0daffc97
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r3
    h: 86ae0daffc97
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the alarm repeats persistently
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r2
    h: 88a78499bebd
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r3
    h: 521d4f5ca817
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r3
    h: 521d4f5ca817
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r3
    h: 86ae0daffc97
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r3
    h: 86ae0daffc97
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r2
    h: 88a78499bebd
  review: drafted
---
