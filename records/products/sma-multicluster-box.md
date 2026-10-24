---
id: prod:sma-multicluster-box
type: Product
name: SMA Multicluster-Box
aliases:
- MC-Box
- Multicluster-Box
- Multicluster-Box 6
- MULTICLUSTER-BOX 6.3-11
- Multicluster-Box 12
- MC-BOX-12.3-20
- Multicluster-Box 36
category: Protection and BOS
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-multicluster-box-connection-and-circuitry-overview-downloads
    loc: sec=h1
    h: c7bf7b2a7b99
  review: drafted
  review_note: 'support check: partial - Passages are SMA service articles about the Multicluster Box
    but never explicitly state SMA makes it, though it is strongly implied by SMA branding.'
- claim_id: c2
  rel: compatible_with
  target: prod:sma-sunny-island-us
  note: The Sunny Island US units have an MC-Box setting for multicluster operation.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h34
    h: f903ae707c75
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=22.r7
    h: 9eaf71f47a00
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=107.r16
    h: 72b60b880ee6
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: arch:battery-inverter-cluster
  note: Connects several Sunny Island clusters into one multicluster system.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h34
    h: f903ae707c75
  - src: src:sma-doc-259761
    loc: sec=6.5.7.6
    h: 2e32da1c753c
  - src: src:sma-doc-259761
    loc: sec=6.5.7.5
    h: c89ce07c40d8
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: arch:off-grid-system
  scope:
    applications:
    - off-grid
  conditions: Multicluster systems with a stand-alone grid
  cite:
  - src: src:sma-doc-278742
    loc: sec=16.1
    h: e1735293496c
  - src: src:sma-doc-278742
    loc: tbl=11
    h: 104d61ee0c21
  review: drafted
  review_note: 'support check: partial - Multicluster systems with stand-alone grid are mentioned alongside
    the Multicluster-Box, but explicit compatibility with an off-grid system is only implied.'
- claim_id: c5
  rel: requires
  target: prod:sma-si-syscan-bgx
  conditions: One installed in each cluster master when a Multicluster-Box is used
  cite:
  - src: src:sma-doc-259761
    loc: sec=6.5.7.6
    h: 2e32da1c753c
  - src: src:sma-doc-278742
    loc: sec=6.5.7.6
    h: 2e32da1c753c
  - src: src:sma-doc-259761
    loc: tbl=91.r1
    h: d77dd6c5aeeb
  review: drafted
- claim_id: c6
  attr: rated_power
  value:
    max: 100
    unit: unit:KiloW
  scope:
    products:
    - prod:sma-sunny-island-us
  conditions: Power of an SMA multicluster system with Sunny Island 4548-US/6048-US
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h34
    h: f903ae707c75
  review: drafted
---
The SMA Multicluster-Box is an AC distribution box that combines several Sunny Island battery inverter clusters into a single multicluster system. The family includes the Multicluster-Box 6 (6.3-11), the Multicluster-Box 12 (MC-BOX-12.3-20) and the Multicluster-Box 36, and each has its own connection and circuit diagrams. The Sunny Island US manual says SMA multicluster technology supports up to twelve Sunny Island inverters and up to 100 kW. US units need the Multicluster Piggy-Back interface to talk to the box. With the MC-BOX-12.3-20, some multifunction relays in the main cluster master and slave 1 are fixed and cannot be reassigned. The two Sunny Island manuals disagree on whether slave 1 uses relay 1 or relay 2, so check the box documentation. Sunny Island firmware 3.5 works in multicluster systems only with the MC-BOX-12.3-20. A newer Sunny Island firmware table allows only version 1.04.00.R for multicluster systems with the MC-Box-12.3-20, with or without a Grid Connect Box. In stand-alone grid systems, the Multicluster-Box sets the maximum PV inverter output that can be connected. Sunny Island event F 801 means the contactor plausibility check in the Multicluster-Box failed, and the fix is to contact SMA Service.

<!-- review notes
- sentence 1: support check: partial - The passages say the box links clusters and is an AC subdistribution, but do not explicitly say it combines clusters as an AC distribution box.
- sentence 3: support check: partial - Up to twelve inverters and 100 kW is stated, and the Piggy-Back is an interface between Sunny Island and the box, but the passages don't say US units need it.
- sentence 6: support check: partial - The passage says the Multicluster-Box specifies the maximum connectable PV inverter output in multicluster systems, in a stand-alone grid section, which is close but not explicitly limited to stand-alone grid.
- sentence 1: review: partial - The passages call the Multicluster-Box an AC subdistribution and describe cluster masters talking to each other in a multicluster system, but they never say outright that it combines several clusters into one system.
- sentence 4: review: partial - The fixed relays and the relay 1 vs relay 2 conflict for slave 1 are supported, but both passages come from sections of the same manual (sma-doc-259761), not two different Sunny Island manuals.
-->
