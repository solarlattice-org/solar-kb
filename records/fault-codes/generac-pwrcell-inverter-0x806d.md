---
id: fc:generac-pwrcell-inverter-0x806d
type: FaultCode
name: Generac PWRcell Inverter 0x806D
aliases:
- '0x806D'
- '0x806d'
- Generac 0x806D
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: '0x806D'
code_key: '0x806d'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r12
    h: 571d21a567a0
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:generac-generac-pwrcell-inverter-x7602-installation-manual
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r12
    h: 571d21a567a0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ct-installation-error
  note: Multiple or missing CTs on lines 1 and 3, or a CT on neutral
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r12
    h: 571d21a567a0
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r12
    h: 571d21a567a0
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r12
    h: 571d21a567a0
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r12
    h: 571d21a567a0
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:generac-pwrcell-inverter
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r12
    h: 571d21a567a0
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r12
    h: 571d21a567a0
  review: drafted
---
