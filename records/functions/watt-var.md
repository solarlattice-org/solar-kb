---
id: func:watt-var
type: Function
name: Watt-VAr
aliases:
- active power-reactive power mode
- Q(P)
- DWVR
- Power-Q
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: requires
  target: proto:modbus
  note: In the Tesla commercial controls manuals the Watt-Var curve can be written in real time through
    Modbus points, with the enable flag starting at register 22001 and the output starting at register
    22028. Setting the curve during commissioning is the alternative.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=2.5.11
    h: 32adf53ae693
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.5.10
    h: 0dd588efe269
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=105
    h: 8802260dcf9d
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=116
    h: 05034e72671c
  review: drafted
- claim_id: c2
  rel: requires
  target: proto:dnp3
  note: Tesla also lets the Watt-Var curve be set in real time through DNP3 points. This is an alternative
    to Modbus or to setting it at commissioning.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=2.5.11
    h: 32adf53ae693
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.5.10
    h: 0dd588efe269
  review: drafted
---
Watt-VAr makes the inverter or battery absorb or inject reactive power according to its own real power output, following a programmable curve. In the default IEEE 1547-2018 settings table, the Watt/VAR function is switched off by default. On Tesla commercial systems, Watt-Var is an open-loop response to real power measured at the POI meter. The reactive power it adds is summed with any Direct Reactive Power command. The Tesla curve has an enable flag, six per-unit real power points and six per-unit reactive power points, plus a response time constant for reaching 95% of the requested reactive power. A read-only output register shows the added reactive power. On Tesla systems, the real power points are scaled to the battery's nominal discharge power and the reactive power points to its nominal reactive power. The Yaskawa Solectria PVI 25TL-208, PVI-36TL-480-V2, PVI 50TL-480 and PVI 60TL-480 list Watt-VAr among their functions. The smart-grid feature list of the CPS SCA25KTL-DO-US-208 does not include it.

<!-- review notes
- sentence 1: support check: partial - Passages say the response follows a programmable curve based on real power measured at the POI meter, not the inverter's own output.
-->
