---
id: tool:clamp-meter
type: Tool
name: Clamp meter
aliases:
- AC/DC clamp meter
- current clamp
- clamp ammeter
- clamp-on ammeter
- AC/DC Current Clamp
- dc clamp meter
- current probe
- Ampèremeettang
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:bluetooth
  note: Some clamp meters send readings wirelessly to FLIR thermal cameras via Bluetooth MeterLink, which
    stores them in the thermal image.
  cite:
  - src: src:test-ir-thermography-t820264-en
    loc: sec=h56
    h: c7280fae6fb8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
A clamp meter measures current without breaking the circuit. Some models measure both AC and DC current, others measure AC only, and all but the cheapest give true RMS readings. Most clamp meters have their own display and also measure voltage. A clamp-on probe does the same job when connected to a standard digital multimeter. SMA inverter manuals list a current clamp as equipment for checking that no voltage is present before work. PV operations and maintenance guides include a DC clamp meter in the tool set for string and combiner box checks, along with an irradiance meter and PPE. A clamp-on ammeter is also used alongside an IR camera during thermal inspections. Connected through a 4 mm terminal, an AC/DC current clamp lets the Seaward PV200 measure operating current from 0.1 A to 40.0 A and, together with its PV terminals, DC operating power. Power clamp versions can be used on both the AC and DC sides of an operating inverter. They show true RMS current, voltage and power, and can analyse harmonics up to the 25th. Some thermal cameras receive clamp meter readings over Bluetooth and store them with the thermal image, so readings do not have to be written down by hand.

<!-- review notes
- sentence 1: support check: partial - AC/DC vs AC-only and true RMS are stated, but 'measures current without breaking the circuit' is not stated in the passage.
- sentence 3: support check: partial - SMA manuals list a current clamp for verifying absence of voltage, but the passages don't name SMA explicitly and cover only some manuals (generalizing to 'SMA inverter manuals').
- sentence 1: review: partial - The AC/DC vs AC-only and true RMS details are stated, but 'measures current without breaking the circuit' is not in the passage.
- sentence 4: review: partial - The tool lists name a DC clamp meter with PPE and an irradiance meter, and a clamp-on ammeter with an IR camera, but the passages never state the 'string and combiner box checks' purpose or the thermal-inspection context.
-->
