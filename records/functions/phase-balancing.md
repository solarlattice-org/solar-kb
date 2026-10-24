---
id: func:phase-balancing
type: Function
name: Phase balancing
aliases:
- unbalanced load limitation
- Power Balancer
- phase symmetry
- SMA Power Balancer
- Automatic unbalanced load limitation
- Avoiding Unbalanced Load
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: requires
  target: role:grid-guard-code-holder
  scope:
    products:
    - prod:sma-sunny-mini-central
  note: Changing the PowerBalancer parameter requires a personal SMA Grid Guard Code; it is set through
    a communication device.
  cite:
  - src: src:sma-kb-configuration-options-sma-power-balancer
    loc: sec=h1
    h: 83dff055fd96
  review: drafted
- claim_id: c2
  attr: trip_time
  value:
    nominal: 5
    unit: unit:MIN
  scope:
    products:
    - prod:sma-sunny-mini-central
  conditions: 'Fault Guard mode: delay after one of the three grouped inverters reports a device fault
    and stops feeding in, before the other two also disconnect from the grid'
  cite:
  - src: src:sma-kb-configuration-options-sma-power-balancer
    loc: sec=h1
    h: 83dff055fd96
  review: drafted
---
Phase balancing groups three single-phase Sunny Mini Central inverters into one three-phase feed-in system, with each inverter on a different phase conductor (L1, L2 or L3). The SMA Power Balancer that does this comes as standard on the Sunny Mini Central. The PowerBalancer parameter is off at the factory. It can only be turned on and set up through a communication device, and you need a personal SMA Grid Guard Code to change it. The parameter has four settings: Fault Guard, Phase Guard, Power Guard and Off. Each one sets how the other two inverters react when the third has a device fault or a grid voltage fault on its phase. In Fault Guard, a grid voltage fault on one inverter disconnects the other two immediately, and a device fault disconnects them 5 minutes later. In Phase Guard, only grid voltage faults make the other two disconnect, and they keep running at full power after a device fault. Power Guard is for plants made up of only three Sunny Mini Central inverters. After a failure, the other two limit their power so the unbalanced load stays at 5 kVA over a 10-minute average. For the SMC 6000TL-IT, 7000TL-IT and 8000TL-IT models in Italy, the limit is 6 kVA. With the function Off, only the faulted inverter disconnects and the other two keep running at full power. The network operator's local connection rules must always be followed when choosing a setting. SMA also lists automatic unbalanced load limitation as a Sunny Island function, including setups with the Sunny Home Manager. Utility service rules can require balanced loading. For example, NSTAR requires customer load to normally stay balanced within 10 percent between phases on three-phase services.

<!-- review notes
- sentence 1: support check: partial - Passage supports grouping 3 SMCs on different phases L1-L3 with standard Power Balancer, but does not say the inverters are single-phase.
- sentence 5: support check: partial - Passage says unbalanced load limited to 5 kVA (6 kVA for Italy models) but the others limit power to 5 kVA over 10-minute average; the 6 kVA Italy detail is there, though the phrasing about other two limiting to 6 kVA is slightly differently stated.
-->
