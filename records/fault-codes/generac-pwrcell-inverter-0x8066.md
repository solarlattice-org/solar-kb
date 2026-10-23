---
id: fc:generac-pwrcell-inverter-0x8066
type: FaultCode
name: Generac PWRcell Inverter 0x8066
aliases:
- '0x8066'
- Generac 0x8066
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: '0x8066'
code_key: '0x8066'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r6
    h: c493479c9b01
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:generac-generac-pwrcell-inverter-x7602-installation-manual
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r6
    h: c493479c9b01
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:calibration-failure
  note: CT calibration invalid on lines 2 and 3
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r6
    h: c493479c9b01
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r6
    h: c493479c9b01
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r6
    h: c493479c9b01
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r6
    h: c493479c9b01
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
