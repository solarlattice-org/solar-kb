---
id: fc:generac-pwrcell-inverter-0x770b
type: FaultCode
name: Generac PWRcell Inverter 0X770B
aliases:
- 0X770B
- '0x770b'
- Generac 0X770B
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: 0X770B
code_key: '0x770b'
page: 68
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r12
    h: b74bb5fb4273
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  note: Transfer switch configured but islanding not enabled
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r12
    h: b74bb5fb4273
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r12
    h: b74bb5fb4273
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:generac-pwrcell-inverter
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r12
    h: b74bb5fb4273
  review: drafted
---
