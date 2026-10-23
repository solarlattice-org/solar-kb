---
id: fc:kaco-blueplanet-87-165-tl3-207
type: FaultCode
name: KACO new energy blueplanet TL3 207
aliases:
- '207'
- KACO new energy 207
- 'Detection of hardware de-tection failed: Control card'
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '207'
code_key: '207'
display_message: 'Detection of hardware de-tection failed: Control card'
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r5
    h: cdc55dca3e33
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:memory-error
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r5
    h: cdc55dca3e33
  review: drafted
  review_note: 'support check: partial - Data saved on the control card is erroneous, which is memory-related,
    but ''memory error'' is not stated literally.'
- claim_id: c3
  rel: affects
  target: comp:control-board
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r5
    h: cdc55dca3e33
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r5
    h: cdc55dca3e33
  review: drafted
  review_note: 'support check: partial - Hardware detection failure implies a fault but no explicit classification;
    it needs a power cycle.'
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r5
    h: cdc55dca3e33
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r5
    h: cdc55dca3e33
  review: drafted
---
