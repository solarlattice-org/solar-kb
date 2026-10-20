---
id: fc:yaskawa-solectria-pvi-23-36tl-gfcierr
type: FaultCode
name: Yaskawa Solectria PVI-TL GFCI.Err
aliases:
- GFCI.Err
- gfcierr
- Yaskawa Solectria GFCI.Err
- DC leakage current is above recommended value
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: GFCI.Err
code_key: gfcierr
display_message: DC leakage current is above recommended value
vendor_severity: Protection
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r4
    h: 63914b12252c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r4
    h: 63914b12252c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r4
    h: 63914b12252c
  review: drafted
  review_note: 'support check: partial - The DC leakage current is above the recommended value, with a
    possible ground fault check, but ''ground fault alarm or…'
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  note: When caused by module insulation failure
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  review: drafted
  review_note: 'support check: partial - Passages mention PV module insulation failure as cause, but don''t
    explicitly state the PV array is affected.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears on its own; then installer ground fault check, then service
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r4
    h: 63914b12252c
  review: drafted
---
