---
id: fc:generac-pwrcell-inverter-0x806b
type: FaultCode
name: Generac PWRcell Inverter 0x806B
aliases:
- '0x806B'
- '0x806b'
- Generac 0x806B
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: '0x806B'
code_key: '0x806b'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r10
    h: 8f968d5d6b07
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:generac-generac-pwrcell-inverter-x7602-installation-manual
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r10
    h: 8f968d5d6b07
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ct-installation-error
  note: Multiple or missing CTs on lines 1 and 2, or a CT on neutral
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r10
    h: 8f968d5d6b07
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r10
    h: 8f968d5d6b07
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r10
    h: 8f968d5d6b07
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r10
    h: 8f968d5d6b07
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: applies_to
  target: prod:generac-pwrcell-inverter
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r10
    h: 8f968d5d6b07
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r10
    h: 8f968d5d6b07
  review: drafted
---
