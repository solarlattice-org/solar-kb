---
id: fc:generac-pwrcell-inverter-0x806c
type: FaultCode
name: Generac PWRcell Inverter 0x806C
aliases:
- '0x806C'
- '0x806c'
- Generac 0x806C
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: '0x806C'
code_key: '0x806c'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r11
    h: 46554694b404
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:generac-generac-pwrcell-inverter-x7602-installation-manual
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r11
    h: 46554694b404
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ct-installation-error
  note: Multiple CTs on line 3 or a CT on neutral
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r11
    h: 46554694b404
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r11
    h: 46554694b404
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r11
    h: 46554694b404
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r11
    h: 46554694b404
  review: drafted
---
