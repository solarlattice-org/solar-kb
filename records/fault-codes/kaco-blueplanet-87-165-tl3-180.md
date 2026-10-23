---
id: fc:kaco-blueplanet-87-165-tl3-180
type: FaultCode
name: KACO new energy blueplanet TL3 180
aliases:
- '180'
- KACO new energy 180
- Pre-synchronisation not pos-sible
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '180'
code_key: '180'
display_message: Pre-synchronisation not pos-sible
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r16
    h: 5d516de2e9c4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-sync-failure
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r16
    h: 5d516de2e9c4
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r16
    h: 5d516de2e9c4
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r16
    h: 5d516de2e9c4
  review: drafted
  review_note: 'support check: partial - Not explicitly classed; implied only weakly by the need for intervention.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Without pre-synchronisation to the grid, the device cannot connect.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r16
    h: 5d516de2e9c4
  review: drafted
  review_note: 'support check: partial - Pre-synchronisation not possible implies no connection, but no
    trip or stop is stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r16
    h: 5d516de2e9c4
  review: drafted
---
