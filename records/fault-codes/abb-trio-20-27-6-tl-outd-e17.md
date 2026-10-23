---
id: fc:abb-trio-20-27-6-tl-outd-e17
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL E017
aliases:
- E017
- e17
- ABB / FIMER E017
- Start Timeout
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: E017
code_key: e17
display_message: Start Timeout
vendor_severity: Error
page: 111
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r5
    h: 8478cbe5ee15
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r5
    h: 8478cbe5ee15
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-startup-timeout
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r1
    h: 4c1a1c90dfed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r4
    h: cc02a26edb78
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r10
    h: aa5b2ce3dc90
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r5
    h: 8478cbe5ee15
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:insufficient-dc-power
  note: External cause when input voltage is just above activation with limited irradiation.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r1
    h: 4c1a1c90dfed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r4
    h: cc02a26edb78
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r10
    h: aa5b2ce3dc90
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r1
    h: 4c1a1c90dfed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r4
    h: cc02a26edb78
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when it recurs systematically under high irradiation and ample input voltage.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=54.r1
    h: 4c1a1c90dfed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r4
    h: cc02a26edb78
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r5
    h: 8478cbe5ee15
  review: drafted
---
