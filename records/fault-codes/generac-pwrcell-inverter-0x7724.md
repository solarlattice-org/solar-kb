---
id: fc:generac-pwrcell-inverter-0x7724
type: FaultCode
name: Generac PWRcell Inverter 0X7724
aliases:
- 0X7724
- '0x7724'
- Generac 0X7724
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: 0X7724
code_key: '0x7724'
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r4
    h: 5bae7206c17f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-sequence-error
  note: Line conductors swapped between transfer switch E terminals and protected loads
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r4
    h: 5bae7206c17f
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r4
    h: 5bae7206c17f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
  review_note: 'support check: partial - Phase wiring is implicated, but AC cable as the affected component
    is only implied, not stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:phase-sequence-correction
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r4
    h: 5bae7206c17f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: applies_to
  target: prod:generac-pwrcell-inverter
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r4
    h: 5bae7206c17f
  review: drafted
---
