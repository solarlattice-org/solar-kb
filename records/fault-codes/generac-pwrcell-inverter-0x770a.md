---
id: fc:generac-pwrcell-inverter-0x770a
type: FaultCode
name: Generac PWRcell Inverter 0X770A
aliases:
- 0X770A
- '0x770a'
- Generac 0X770A
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: 0X770A
code_key: '0x770a'
page: 68
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r11
    h: 9ef6cc81994a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  note: AC features enabled on an inverter set up for three-phase
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r11
    h: 9ef6cc81994a
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the site is a single-phase service
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r11
    h: 9ef6cc81994a
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: When the site is a three-phase service
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r11
    h: 9ef6cc81994a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
