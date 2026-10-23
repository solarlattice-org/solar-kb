---
id: fc:abb-pvs-166-175-tl-us-w11
type: FaultCode
name: ABB / FIMER PVS-166-175-TL W011
aliases:
- W011
- w11
- ABB / FIMER W011
- Bulk UV
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: W011
code_key: w11
display_message: Bulk UV
vendor_severity: Warning
page: 137
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r6
    h: 8a9103a443c1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r6
    h: 8a9103a443c1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-undervoltage
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r6
    h: 8a9103a443c1
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r7
    h: 50beac5758a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r1
    h: 125c191e96cf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r1
    h: 125c191e96cf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4ec28b122b41
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r1
    h: 4ec28b122b41
  review: drafted
  review_note: 'support check: partial - W011 is low bulk voltage in the DC-DC circuit, which is DC bus
    undervoltage by paraphrase, but this is not…'
- claim_id: c4
  rel: affects
  target: comp:dc-link-capacitor
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r6
    h: 8a9103a443c1
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r7
    h: 50beac5758a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r1
    h: 125c191e96cf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r1
    h: 125c191e96cf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4ec28b122b41
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r1
    h: 4ec28b122b41
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:boost-converter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r6
    h: 8a9103a443c1
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r7
    h: 50beac5758a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r1
    h: 125c191e96cf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r1
    h: 125c191e96cf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4ec28b122b41
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r1
    h: 4ec28b122b41
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r6
    h: 8a9103a443c1
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r7
    h: 50beac5758a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r1
    h: 125c191e96cf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r1
    h: 125c191e96cf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4ec28b122b41
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r1
    h: 4ec28b122b41
  review: drafted
  review_note: 'support check: partial - Input voltage is checked against Vstart, but detection by DC
    voltage measurement is only implied.'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise activation voltage Vstart; contact service if input exceeds Vstart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r6
    h: 8a9103a443c1
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r7
    h: 50beac5758a5
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r1
    h: 125c191e96cf
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r1
    h: 125c191e96cf
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r1
    h: 4ec28b122b41
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r1
    h: 4ec28b122b41
  review: drafted
---
