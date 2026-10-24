---
id: prod:fronius-smart-meter
type: Product
name: Fronius Smart Meter
aliases:
- Smart Meter TS
category: Metering
make: fronius
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fronius
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: sec=h43
    h: 6e676185d82b
  - src: src:fronius-fronius-us-gen24-firmware-changelog
    loc: sec=h10
    h: 625f68a6acf1
  review: drafted
  review_note: 'support check: partial - Passages refer to the ''Fronius Smart Meter'' and Fronius products,
    which implies Fronius naming, but never state that Fronius manufactures it.; review: partial - Fronius
    documents name the ''Fronius Smart Meter'' and the brand implies Fronius, but no passage says Fronius
    makes it.'
- claim_id: c2
  rel: compatible_with
  target: prod:fronius-datamanager
  note: Fronius Data Manager 2.0 monitoring can control the inverter based on a connected Fronius Smart
    Meter.
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: sec=h43
    h: 6e676185d82b
  review: drafted
---
The Fronius Smart Meter is a Fronius energy meter family. A Fronius inverter's monitoring system uses it to control the inverter. On the Fronius Primo, the built-in Data Manager 2.0 can control the inverter from a connected Fronius Smart Meter. The same Data Manager also offers dynamic power reduction that takes self-consumption into account.

<!-- review notes
- sentence 1: support check: partial - Monitoring uses the Smart Meter to control the inverter, but the passages don't state it is an energy meter family.
- sentence 2: support check: partial - The passage says the inverter has Data Manager 2.0 with meter control and dynamic power reduction, but it doesn't name the Primo specifically.
- sentence 1: review: partial - The passage says the monitoring system can control the inverter through connected meters (Fronius Smart Meter), but it never calls the Smart Meter an energy meter family.
-->
