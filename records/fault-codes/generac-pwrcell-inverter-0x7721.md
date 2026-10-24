---
id: fc:generac-pwrcell-inverter-0x7721
type: FaultCode
name: Generac PWRcell Inverter 0X7721
aliases:
- 0X7721
- '0x7721'
- Generac 0X7721
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: 0X7721
code_key: '0x7721'
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r2
    h: b2428ee70596
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  note: Transfer switch detected but none configured
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r2
    h: b2428ee70596
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r2
    h: b2428ee70596
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: applies_to
  target: prod:generac-pwrcell-inverter
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r2
    h: b2428ee70596
  review: drafted
---
