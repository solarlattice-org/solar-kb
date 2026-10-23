---
id: fc:sma-stp-tl-us-3401-3402
type: FaultCode
name: SMA STP-TL-US 3401-3402
aliases:
- 3401-3402
- SMA 3401-3402
- DC overvoltage > Disconnect generator
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 3401-3402
code_key: 3401-3402
code_from: 3401
code_to: 3402
display_message: DC overvoltage > Disconnect generator
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r2
    h: 07b02001f8ac
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r2
    h: 07b02001f8ac
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r2
    h: 07b02001f8ac
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15
    h: 08dd85b4e87f
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r2
    h: 07b02001f8ac
  review: drafted
  review_note: 'support check: partial - DC overvoltage is detected, and the DC voltage is compared with
    the maximum, but the measurement method is not explicitly stated.'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When DC voltage exceeds maximum input; contact installer, then Service if repeated.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r2
    h: 07b02001f8ac
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15
    h: 08dd85b4e87f
  review: drafted
  review_note: 'support check: partial - It advises checking that the PV array is correctly rated or contacting
    the installer, then Service if repeated, which is…'
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r2
    h: 07b02001f8ac
  review: drafted
  review_note: 'support check: partial - It is a serious overvoltage requiring disconnection, but no fault
    classification is stated.'
---
