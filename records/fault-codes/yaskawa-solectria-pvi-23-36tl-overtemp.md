---
id: fc:yaskawa-solectria-pvi-23-36tl-overtemp
type: FaultCode
name: Yaskawa Solectria PVI-TL OverTemp
aliases:
- OverTemp
- overtemp
- Yaskawa Solectria OverTemp
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: OverTemp
code_key: overtemp
vendor_severity: Protection
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r5
    h: aabec9e33b25
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r6
    h: aa0995381f56
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r5
    h: aabec9e33b25
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r6
    h: aa0995381f56
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r5
    h: aabec9e33b25
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r6
    h: aa0995381f56
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r5
    h: aabec9e33b25
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  note: When air paths or fan are blocked
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r5
    h: aabec9e33b25
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:installation-clearance
  note: When cooling is poor due to installation spacing
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r6
    h: aa0995381f56
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Clears on its own once cooled; service if persistent
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r5
    h: aabec9e33b25
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r6
    h: aa0995381f56
  review: drafted
  review_note: 'support check: partial - Observe 30 min for auto-clear and then service are stated; ''once
    cooled'' is not stated.'
---
