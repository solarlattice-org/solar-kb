---
id: prod:sma-stp-tl-10
type: Product
name: Sunny Tripower 8000-17000TL-10
aliases:
- STP 8000-17000TL-10
- STP xx000TL-10
- STP TL-10
- STP8-17000TL-10
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-sunny-tripower-manuals
    loc: sec=h1
    h: b48a3498e573
  - src: src:sma-kb-sunny-tripower-stp-tl-10-is-beeping
    loc: sec=h1
    h: 07995d0deb78
  review: drafted
  review_note: 'support check: partial - Passages are SMA service articles listing Sunny Tripower 8000-17000TL-10
    manuals, implying SMA makes it, but they never explicitly say ''made by SMA''.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:sma-doc-278405
    loc: tbl=39.r14
    h: 5e7a773094cc
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:speedwire
  scope:
    products:
    - prod:sma-stp-tl-10
  note: Listed for the STP 17000TL-10 as an inverter with multifunction relay, communication standard
    Speedwire.
  cite:
  - src: src:sma-doc-278405
    loc: tbl=39.r14
    h: 5e7a773094cc
  review: drafted
- claim_id: c4
  rel: has_hazard
  target: hazard:dc-arc-flash
  conditions: While the electronic string fuse has short-circuited the PV array and the inverter is beeping
  note: Do not pull the DC connectors or the ESS while the inverter beeps; risk of an electric arc.
  cite:
  - src: src:sma-kb-sunny-tripower-stp-tl-10-is-beeping
    loc: sec=h1
    h: 07995d0deb78
  - src: src:sma-kb-event-82-and-varistor-faulty-on-stp8-17000tl-10
    loc: sec=h1
    h: '105213e62164'
  review: drafted
- claim_id: c5
  rel: has_hazard
  target: hazard:fire
  conditions: If the ESS is pulled during a short-circuit/reverse-current event
  note: The whole reverse current would then flow through the faulty string and could start a fire.
  cite:
  - src: src:sma-kb-sunny-tripower-stp-tl-10-is-beeping
    loc: sec=h1
    h: 07995d0deb78
  review: drafted
- claim_id: c6
  rel: has_hazard
  target: hazard:disconnecting-under-load
  conditions: Disconnecting DC connectors while the inverter beeps
  note: Disconnect only once beeping stops after dark.
  cite:
  - src: src:sma-kb-sunny-tripower-stp-tl-10-is-beeping
    loc: sec=h1
    h: 07995d0deb78
  review: drafted
---
The Sunny Tripower 8000-17000TL-10 is an SMA three-phase PV inverter family made up of the STP 8000TL-10, 10000TL-10, 12000TL-10, 15000TL-10 and 17000TL-10; SMA now files its manuals as archived. These inverters contain an electronic string fuse that stops dangerous reverse currents in the PV array. It is a separate part from the Electronic Solar Switch (ESS) handle, which is used to disconnect the DC strings without load. If a string is connected with reversed polarity, strings with different module counts are mixed, or a string is defective, the inverter short-circuits the PV array and beeps. While it beeps, do not pull the DC connectors or the ESS, because this risks an arc or a fire. Wait until it goes quiet after dark before you disconnect and fix the string. Event 82, 8201 or 8203 with a red LED, a beep and the message that the device is short-circuited can come before event 7401 (varistor faulty). On existing plants, check the varistors and their thermal fuses and replace them if needed. The STP 17000TL-10 is listed as an inverter with a multifunction relay that communicates over Speedwire. SMA sells spare-part sets for this family: a power assembly, an AC assembly and a DC filter assembly. A DC surge protection device retrofit manual uses this family as its example installation.

<!-- review notes
- sentence 1: support check: partial - Passages list the five models as archived manuals from SMA, but 'three-phase' is not stated.
- sentence 6: support check: partial - Spare-part sets for power, AC and DC filter assemblies and an SPD figure using the STP XX000TL-10 family are present, but the passages don't say SMA sells them or that it is a retrofit manual.
-->
