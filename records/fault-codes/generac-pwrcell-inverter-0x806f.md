---
id: fc:generac-pwrcell-inverter-0x806f
type: FaultCode
name: Generac PWRcell Inverter 0x806F
aliases:
- '0x806F'
- '0x806f'
- Generac 0x806F
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: '0x806F'
code_key: '0x806f'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r14
    h: ffcdec86c85c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:generac-generac-pwrcell-inverter-x7602-installation-manual
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r14
    h: ffcdec86c85c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ct-installation-error
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r14
    h: ffcdec86c85c
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r14
    h: ffcdec86c85c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:current-sensor
  note: Current transformers on all three lines, or one placed on neutral.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r14
    h: ffcdec86c85c
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r14
    h: ffcdec86c85c
  review: drafted
  review_note: 'review: partial - The CT/current-sensor link is supported, but the note says CTs are ''on
    all three lines'', while the row says Lines 1, 2…'
---
