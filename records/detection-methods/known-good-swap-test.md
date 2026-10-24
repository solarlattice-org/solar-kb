---
id: method:known-good-swap-test
type: DetectionMethod
name: Known-good component swap test
aliases:
- swap with known good
- SWDM/display swap
- swap suspect TS4-R
- SWDM and Display swap
- swap the suspect TS4-R
claims:
- claim_id: c1
  rel: produces
  target: meas:fault-follows-swapped-part
  note: In the SMA STP-US-10 daisy-chain procedure, the faulty SWDM, display or inverter is identified
    by which inverter stops communicating after the suspect parts are moved to known-good positions.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - The STP-US-10 article identifies the faulty part by which inverter
    won''t communicate after swapping, and the TS4-R swap persists the fault, but the passages never state
    the generic ''fault follows swapped part'' result as such.'
---
A known-good swap test finds a faulty part by trading a suspect component with the same part from a unit that is working, then checking whether the fault moves with the part. On SMA STP-US-10 inverters on a daisy chain, the suspect SWDM data module and the suspect display are moved into two working inverters further down the chain, and those inverters' good parts go into the suspect inverter. Before swapping, power-cycle with both AC and DC off, reseat and inspect the ribbon cables, and check the Ethernet cables. A known-good Ethernet cable can be used for a while to rule out the site cabling. After powering back on, allow time for the inverters to re-sync. Then see which inverter breaks the chain or will not report; this tells you whether the SWDM, the display or the inverter itself is causing the daisy-chain communication break. For Tigo TS4-R rapid shutdown devices that fail detection, the suspect TS4-R is swapped with a known-good one from another module assembly and detection is run again. This confirms a rapid shutdown device failure, as opposed to a bad PV module. Only electrically qualified persons should do this work. The device must be de-energized (AC off, then DC off) before opening it. On PV strings, confirm zero current with a DC amp-clamp before mating or de-mating connectors. Even with rapid shutdown, cables from a PV panel can carry high DC voltage and current. Always connect the TS4-R to the panel before wiring the assembly into the string, or the device can be permanently damaged.

<!-- review notes
- sentence 5: support check: partial - The swap with a known-good TS4-R and re-running detection is stated, and the fault persisting indicates a faulty device, but the text does not describe confirming a device failure versus a bad module through the swap (the panel is checked separately by Voc measurement).
- sentence 7: support check: partial - The up-to-90 Vdc and 10 A warning and the connect-TS4-R-to-panel-first notice with permanent damage are stated, but the passages tie the voltage and current to mating or de-mating and inadvertent current to ground, not to 'even with rapid shutdown'.
- sentence 7: review: partial - The connect-to-panel-first notice and the permanent-damage warning are stated, but the passage ties the up-to-90 Vdc and 10 A warning to mating or de-mating with inadvertent current to ground, not to 'even with rapid shutdown' (it says no voltage should…
-->
