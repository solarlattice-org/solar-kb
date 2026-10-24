---
id: mit:rcd-type-selection
type: Mitigation
name: Residual-current device type selection
aliases:
- type A RCD
- type B RCD
- RCD selection
- operational differential currents
---
A transformerless inverter produces operational differential currents through the insulation resistance and capacitance of the PV array. To stop unwanted tripping, use only a residual-current device that the inverter manual lists as compatible. Under DIN VDE 0100-712, the AC circuit needs a type B device unless the inverter manufacturer approves other RCD types. Many SMA inverters are approved for type A. For example, the SBSE9.6-US-50 and SBSE11.5-US-50 are listed as compatible with both Type A and Type B devices. For several of its single-phase models, Solis recommends an external Type A RCD rated at 100mA. It gives 300mA as the maximum continuous residual current under IEC 62109. In SMA backup systems that need an external device, choose one that trips at a residual current of 100 mA or higher. A grid operator's technical connection requirements may call for an RCD, and in that case they set the type and use conditions. Do not use RCDs in TN-C systems. In TT systems, an RCD is required as the primary fault protection. Where no other circuit breaker can provide fault protection, a type A device with a 500 mA rated residual current meets the automatic disconnection requirement.

<!-- review notes
- sentence 5: support check: partial - Passage gives the 100 mA or higher trip requirement when an external RCD is required, but does not say it applies to backup systems specifically.
-->
