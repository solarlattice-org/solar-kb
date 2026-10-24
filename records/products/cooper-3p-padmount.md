---
id: prod:cooper-3p-padmount
type: Product
name: Cooper three-phase pad-mounted compartmental transformer
aliases:
- 3P Pad Mount Compartmental
- Cooper pad-mounted
- three-phase pad-mounted transformers
category: Transformers
make: cooper
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:cooper
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h43
    h: 2b82d9eecf4c
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h45
    h: 34c38ff4492c
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h2
    h: 09e9ac97bfe2
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    min: 45
    max: 12000
    unit: unit:KiloV-A
  conditions: Standard three-phase kVA ratings listed for 50 or 60 Hz; custom ratings also available
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: tbl=2
    h: 75803a3f98e3
  review: drafted
  review_note: 'review: partial - Table 2 lists standard three-phase 50 or 60 Hz ratings from 45 to 12000
    kVA, but the passage says nothing about custom ratings (the footnote marker 1 is not quoted).'
- claim_id: c3
  attr: frequency
  value:
    nominal: 50
    unit: unit:HZ
  conditions: 50 Hz three-phase ratings
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: tbl=2
    h: 75803a3f98e3
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: 60 Hz three-phase ratings
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: tbl=2
    h: 75803a3f98e3
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c5
  attr: nominal_voltage
  value:
    min: 2400
    unit: unit:V
  conditions: Lower end of the available high-voltage (primary) range
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h2
    h: 09e9ac97bfe2
  review: drafted
- claim_id: c6
  attr: nominal_voltage
  value:
    max: 46
    unit: unit:KiloV
  conditions: Upper end of the available high-voltage (primary) range
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h2
    h: 09e9ac97bfe2
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c7
  rel: certified_to
  target: std:doe-10-cfr-431-2010
  note: Applicable transformers are designed to meet or exceed DOE 2010 final rule efficiency values
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h38
    h: 50f5446d1009
  review: drafted
  review_note: 'support check: partial - Passages say units are designed to meet or exceed DOE 2010 efficiency
    under 10 CFR 431, but not that they are certified.'
- claim_id: c8
  rel: certified_to
  target: std:iso-9001
  note: The manufacturer's transformer products are stated to be ISO 9001 compliant
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h2
    h: 09e9ac97bfe2
  review: drafted
  review_note: 'support check: partial - Passage says products are ISO 9001 compliant, not certified;
    the note itself reflects compliance only.'
- claim_id: c9
  rel: compatible_with
  target: prod:cargill-envirotemp-fr3
  note: Offered with either electrical grade mineral oil or Envirotemp FR3 fluid
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h2
    h: 09e9ac97bfe2
  review: drafted
---
This is Cooper Power Systems' family of three-phase pad-mounted, compartmental-type distribution transformers, built in the United States. Standard ratings run from 45 kVA up to 12000 kVA at 50 or 60 Hz, and custom ratings can be ordered. High-voltage ratings range from 2400 V to 46 kV. Units are filled with either electrical grade mineral oil or Envirotemp FR3, a less-flammable, biodegradable fluid suited to fire-sensitive sites. Applicable units are designed to meet or exceed the DOE 2010 efficiency values under 10 CFR Part 431, and the transformer products are ISO 9001 compliant. A VFI version pairs the transformer with a resettable vacuum fault interrupter that gang-trips all three phases on a fault or overload, so three-phase loads are never left single-phased. An optional sealed visible break window lets the operator check whether the loadbreak switch contacts are open or closed before starting maintenance.

<!-- review notes
- sentence 1: review: partial - The passages support Cooper Power Systems three-phase pad-mounted compartmental transformers made in the USA, but the word 'distribution' is not in the cited passages.
-->
