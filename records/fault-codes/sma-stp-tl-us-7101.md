---
id: fc:sma-stp-tl-us-7101
type: FaultCode
name: SMA STP-TL-US 7101
aliases:
- '7101'
- SMA 7101
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '7101'
code_key: '7101'
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r5
    h: fd0b0630be23
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:memory-card-unwritable
  note: Memory card is unformatted
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r5
    h: fd0b0630be23
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:memory-card-reformat
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r5
    h: fd0b0630be23
  review: drafted
---
