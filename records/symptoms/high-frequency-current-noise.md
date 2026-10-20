---
id: symptom:high-frequency-current-noise
type: Symptom
name: High-frequency current noise
aliases:
- electrical noise
- high frequency noise pattern
claims:
- claim_id: c1
  rel: observed_as
  target: meas:arc-fault-alarm
  note: The inverter's arc fault sensor picks up the electrical noise that comes with a DC series arc
    and raises an arc fault (ARC Protect) condition. Some models then need a manual clear.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h15
    h: d574c58e979c
  - src: src:yaskawa-solectria-pvi-36tl
    loc: fig=131
    h: edb18b4cf3a2
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: fig=193
    h: fbb997e93cb2
  review: drafted
  review_note: 'support check: partial - Passages say the inverter detects arc noise and shuts down, and
    show ''ARC Protect'' fault and manual clear figures, but only as titles; ''some models need manual
    clear'' is only implied by figure titles.'
- claim_id: c2
  rel: observed_as
  target: meas:ac-power-step-drop
  note: The inverter shuts down when its arc fault sensor detects a series arc, so output stops suddenly.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h15
    h: d574c58e979c
  review: drafted
  review_note: 'support check: partial - Inverter shutdown on series arc detection is stated, implying
    output stops, but sudden drop to zero in AC power and DC current is not explicitly stated.'
---
High-frequency noise on the DC current and voltage is the signature of a burning DC arc. The arc's length and voltage keep changing because hot material evaporates and magnetic forces push on the arc. Inverters with arc fault detection sense this noise from a series arc and shut down. On site this usually appears as an ARC Protect fault and a sudden stop in production. On some inverters you must clear the arc fault manually or reset the operation inhibition before the unit will restart. Arcs come and go, so they are hard to catch. Analysing the spectrum of the current and voltage waveforms is one way to detect them. A series arc can start where every solder bond of a cell has broken, the bypass diode cannot carry the current, and the system runs at high voltage. Such an arc can start a fire. Before restarting, look for burn marks along the affected string. An infrared image will show whether a spot is still hot or whether current has stopped flowing in that part of the circuit. Arc fault circuit interrupters installed on individual strings can protect the system from arc faults.

<!-- review notes
- sentence 2: support check: partial - Shutdown on series arc detection and an ARC Protect Fault figure are present, but 'sudden stop in production' is not stated.
- sentence 5: support check: partial - Passage says that if all solder bonds of a cell break, current is blocked and an arc can result if the bypass diode can't bypass it at high voltage, causing fire; it says 'can result', and 'every' bond and 'starts' are slightly stronger, though largely consistent.
- sentence 6: support check: partial - Passage says burn marks are visually identifiable and IR imaging shows whether the area is still hot or current has stopped, but it doesn't advise inspecting before restarting after an arc fault.
-->
