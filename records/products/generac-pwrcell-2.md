---
id: prod:generac-pwrcell-2
type: Product
name: Generac PWRcell 2
aliases:
- PWRcell 2
- PWRcell 2 System
- PWRcell 2 Inverter
category: Inverters
make: generac
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:generac
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h103
    h: 86448dd33040
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    nominal: 11500
    unit: unit:V-A
  conditions: Apparent power rating used as the basis for grid support function settings
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h103
    h: 86448dd33040
  review: drafted
  review_note: 'support check: partial - The footnote says settings are based on an apparent power rating
    of 11500 VA, but it doesn''t call this the rated power of the PWRcell 2 as a whole.'
- claim_id: c3
  attr: efficiency
  value:
    nominal: 85
    unit: unit:PERCENT
  conditions: Round-trip efficiency, AC to DC to AC
  cite:
  - src: src:generac-generac-pwrcell-2-inverter-installation-manual-a0008210358
    loc: tbl=3.r14
    h: 3e5fc67df64b
  review: drafted
- claim_id: c4
  rel: certified_to
  target: std:ieee-1547-2018
  note: 'PWRcell 2 SDS with PWRcell 2 Inverter: Normal Operating Performance Category B, Abnormal Operating
    Performance Category III'
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: tbl=4.r5
    h: 4d62a3bf02b1
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:ul-1741-sb
  note: Listed in the PWRcell 2 SDS compliance table; grid support function defaults evaluated on the
    PWRcell 2 Inverter
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: tbl=4.r4
    h: 5f11c5a20b6a
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h103
    h: 86448dd33040
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c6
  rel: certified_to
  target: std:ul-3141
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h88
    h: 6d1cda0ffb8e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: certified_to
  target: std:ul-1741-crd-pcs
  note: Listed for several PCS functions
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h88
    h: 6d1cda0ffb8e
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:nerc-prc-024-3
  note: Frequency and voltage protection settings for generating resources
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: tbl=4.r12
    h: 88f13318b9d1
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:iso-ne-bulk-system-area-settings
  note: Default New England bulk system area settings requirement
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: tbl=4.r11
    h: 225d8699e495
  review: drafted
- claim_id: c10
  rel: implements
  target: func:power-control-system
  note: 'PCS functions: Power Export Limit, Busbar Overload Control, Feeder Conductor Overload Control'
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h88
    h: 6d1cda0ffb8e
  review: drafted
- claim_id: c11
  rel: implements
  target: func:export-limitation
  note: Power Export Limit (PEL) PCS function
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h88
    h: 6d1cda0ffb8e
  review: drafted
  review_note: 'support check: partial - Power Export Limit is named as a PCS function, but the passage
    doesn''t describe it as export limitation in detail; this is a reasonable inference.'
- claim_id: c12
  rel: requires
  target: role:qualified-person
  note: Commissioning, where PCS functions are set, needs a qualified person and a password
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h88
    h: 6d1cda0ffb8e
  review: drafted
---
Generac PWRcell 2 is a Generac inverter system family that pairs the PWRcell 2 Inverter with the PWRcell 2 Smart Disconnect Switch and batteries. The PWRcell 2 Inverter is rated for 11.5 kW of maximum continuous AC power, and its grid support settings use an apparent power rating of 11500 VA. Its CEC weighted efficiency is 98.0 percent, and its AC-to-DC-to-AC round-trip efficiency is 85 percent. Used with the Smart Disconnect Switch, the inverter is certified to IEEE 1547-2018 for Normal Performance Category B and Abnormal Performance Category III, and to UL 1741 SB. The SDS compliance table also lists SunSpec CSIP, NERC PRC-024-3, the New England bulk system default settings, and FCC Part 15 Class B. The system is certified to UL 3141 and listed to the UL 1741 PCS CRD for three power control functions: Power Export Limit, Busbar Overload Control and Feeder Conductor Overload Control. PCS functions are set during commissioning, which needs a qualified person and a password. To recommission a system, contact Generac PWRcell technical support so they can reset it.

<!-- review notes
- sentence 1: support check: partial - The passages show a PWRcell 2 System figure, Inverter, and Battery Size, but not clearly that the family pairs the Inverter with a Smart Disconnect Switch and batteries; the SDS appears only elsewhere.
- sentence 5: support check: partial - All four standards are listed as certified standards, but the passages don't say they appear in the SDS compliance table specifically.
- sentence 6: support check: partial - The certification and the three named functions are in the passage, but it says 'several' functions rather than exactly three.
- sentence 1: review: partial - The passages only give a system figure title, an SDS manual and a battery size row; none of them says the family pairs the inverter with the Smart Disconnect Switch and batteries.
-->
