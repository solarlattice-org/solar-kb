---
id: fc:generac-pwrcell-inverter-0x806e
type: FaultCode
name: Generac PWRcell Inverter 0x806E
aliases:
- '0x806E'
- '0x806e'
- Generac 0x806E
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: '0x806E'
code_key: '0x806e'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r13
    h: 90787148ab7a
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:generac-generac-pwrcell-inverter-x7602-installation-manual
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r13
    h: 90787148ab7a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ct-installation-error
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r13
    h: 90787148ab7a
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r13
    h: 90787148ab7a
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:current-sensor
  note: Current transformers on lines 2 and 3, or one placed on neutral.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r13
    h: 90787148ab7a
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r13
    h: 90787148ab7a
  review: drafted
---
