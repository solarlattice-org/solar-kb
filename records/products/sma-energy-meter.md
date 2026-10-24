---
id: prod:sma-energy-meter
type: Product
name: SMA Energy Meter
aliases:
- EMETER-20
- Energy Meter 2.0
- EMETER-10
- EMETER-US-50
- SMA Energy Meter-US
- SMA Energy Meter 10
- SMA Energy Meter 20
- SMA Energy Meter CT
- Energy Meter
category: Metering
make: sma
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:energy-meter
  cite:
  - src: src:sma-doc-259463
    loc: sec=6.3
    h: 10a341f53711
  review: drafted
- claim_id: c2
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-doc-259463
    loc: sec=h127
    h: 813b8ab76473
  review: drafted
  review_note: 'support check: partial - The passage mentions SMA Solar Technology AG only as the company
    that recommends current transformers; it never says SMA makes the meter, though the ''SMA'' naming
    and context imply it.'
- claim_id: c3
  rel: uses_protocol
  target: proto:speedwire
  note: Measured values at the connection point are made available over Speedwire.
  cite:
  - src: src:sma-doc-259463
    loc: sec=6.3
    h: 10a341f53711
  review: drafted
- claim_id: c4
  rel: certified_to
  target: std:eu-mid-2004-22
  negated: true
  note: Not a MID-compliant consumption meter and must not be used for billing.
  cite:
  - src: src:sma-doc-259463
    loc: sec=6.3
    h: 10a341f53711
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:sma-sunny-home-manager-2
  scope:
    firmware_min: 2.0.4.R
  conditions: SMA Energy Meter 20 from firmware 2.0.4.R
  cite:
  - src: src:sma-doc-278405
    loc: sec=2.1.1.1
    h: 99414370801c
  - src: src:sma-doc-278405
    loc: tbl=3.r2
    h: 1cfca60057fe
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:sma-sunny-tripower-smart-energy
  note: With the energy meter, grid management services via Modbus (e.g. active power limitation) are
    available; intelligent load control is not.
  cite:
  - src: src:sma-doc-259463
    loc: tbl=10.r2
    h: 3c43e3fe37ce
  - src: src:sma-doc-259463
    loc: tbl=10.r6
    h: b8b799bf78ab
  review: drafted
---
The SMA Energy Meter is SMA's family of energy meters. Variants include EMETER-10, EMETER-20, the Energy Meter CT and the US variant EMETER-US-50. It measures electrical values at the connection point, records energy flowing in both directions, can be wired single-phase or three-phase, and publishes its data over SMA Speedwire. It is not a MID-compliant consumption meter, so do not use it for billing. The Sunny Home Manager 2.0 works with the Energy Meter 10 from firmware 1.0.4.R, the Energy Meter 20 from firmware 2.0.4.R and the Energy Meter CT from the start of series production. In systems using Speedwire encrypted communication, every Speedwire device except the energy meter must support encryption. To reset the meter, press its reset button for 2 to 6 seconds; to restart it, hold the button for 9 seconds. Afterwards, check the meter's serial number in the inverter or communication product. You can update the firmware manually by uploading a file through the meter's user interface, under Device Configuration and then Settings.

<!-- review notes
- sentence 1: support check: partial - The passages list EMETER-10, EMETER-20, Energy Meter CT and EMETER-US-50, but they don't call these a family of SMA meters, and the model-to-variant mapping is only implied.
- sentence 6: support check: partial - The 2–6 s reset and 9 s restart are stated, but the passage says to adjust the meter's serial number in the inverter or communication product, not merely 'check' it.
- sentence 4: review: partial - The table gives the firmware versions for Energy Meter 10, 20 and CT, but the quoted passage never says these are the versions the Sunny Home Manager 2.0 works with.
-->
