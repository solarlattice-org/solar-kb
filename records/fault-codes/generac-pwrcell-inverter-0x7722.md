---
id: fc:generac-pwrcell-inverter-0x7722
type: FaultCode
name: Generac PWRcell Inverter 0X7722
aliases:
- 0X7722
- '0x7722'
- Generac 0X7722
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: 0X7722
code_key: '0x7722'
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r3
    h: c1e9e2ea58e1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-sequence-error
  note: Line conductors swapped between transfer switch N terminals and protected loads
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r3
    h: c1e9e2ea58e1
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r3
    h: c1e9e2ea58e1
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:phase-sequence-correction
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r3
    h: c1e9e2ea58e1
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
