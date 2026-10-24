---
id: func:grid-forming
type: Function
name: Grid forming
aliases:
- island mode
- voltage-source operation
- stand-alone grid formation
- Grid-Forming mode
- Stand-alone grid
- grid-forming PV
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  rel: requires
  target: prod:enphase-iq-meter-collar
  note: Listed in every Enphase grid-forming (with backup) configuration supported by IQ Gateway 8.3.5566,
    together with IQ Battery 10C and IQ Combiner 6C.
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
- claim_id: c2
  rel: requires
  target: prod:enphase-iq-battery
  note: The IQ Battery 10C appears in all listed Enphase grid-forming (with backup) configurations, including
    battery-only systems.
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
- claim_id: c3
  rel: requires
  target: prod:enphase-iq-combiner
  note: The IQ Combiner 6C appears in all listed Enphase grid-forming (with backup) configurations.
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
---
Grid forming lets a battery inverter run as a standalone voltage and frequency source. It can then supply loads on weak grids, or on grids with no conventional generation and no other inverters. On Tesla Megapack systems, the Mode Request parameter selects the mode: 1 is grid-following and 2 is grid-forming. Grid forming is only available on systems designed for it, and Tesla must enable it at commissioning. Tesla's grid forming can run off-grid (islanded), or on-grid to add virtual inertia. Tesla's design uses two parallel paths. A Virtual Machine behind a current-limiting impedance follows the voltage and frequency references, and a Power Dispatcher follows the real and reactive power setpoints. Compared with grid-following mode, it reaches power commands more slowly but reacts much faster to voltage and frequency changes. Enphase grid-forming (with backup) systems pair the IQ Battery 10C, IQ Combiner 6C and IQ Meter Collar with IQ9N, IQ8, IQ7 or IQ6 microinverters, or run as battery-only systems. IQ8 grid forming works only on 240 V AC interconnections, and the IQ8H-208 has no grid-forming function. A mix of IQ7 with IQ8 or IQ9N microinverters loses the Sunlight Jump Start (grid-forming PV) feature.

<!-- review notes
- sentence 6: support check: partial - IQ8 240 V only and IQ8H-208 lacking grid-forming are stated, but the passage says a mixed IQ7 with IQ8/IQ9N system doesn't support IQ8- or IQ9N-specific Sunlight Jump Start, which is narrower than 'loses the feature' generally.
-->
