---
id: fm:inverter-clipping
type: FailureMode
name: Inverter clipping
aliases:
- Clipping
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.4
    h: 69ccb977fc01
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.4.2
    h: c3122621e051
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:high-dc-ac-ratio
  note: Happens when the array's DC power is larger than the inverter's rated AC output. Designers sometimes
    oversize the array on purpose to get more energy in the morning and evening.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.4
    h: 69ccb977fc01
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h12
    h: 66cfaabb55b0
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.4.2
    h: c3122621e051
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:flat-capped-output
  note: The inverter holds output at its maximum rating, which acts as a power ceiling. Most of the lost
    energy falls on the sunnier days.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.4
    h: 69ccb977fc01
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.4.2
    h: c3122621e051
  review: drafted
  review_note: 'support check: partial - Passages say the inverter limits output to its maximum (a power
    ceiling) and that losses fall mainly on sunnier days, but never describe a flat capped output signature
    explicitly.'
- claim_id: c4
  rel: detected_by
  target: method:performance-monitoring
  note: Monitoring algorithms work out the DC size and AC capacity, then calculate the clipped energy
    wherever the AC limit caps the expected output.
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h12
    h: 66cfaabb55b0
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.4.2
    h: c3122621e051
  - src: src:alsoenergy-kb-modeling-derates
    loc: sec=front
    h: 20177852b365
  review: drafted
- claim_id: c5
  rel: distinguished_from
  target: fm:inverter-voltage-floor-losses
  by: method:iv-curve-tracing
  note: 'Clipping is a power ceiling. Voltage flooring is an MPPT limit set by the DC voltage window:
    the operating voltage stays above the Vmp from the IV curve, and the power stays below the Pmp from
    the IV curve.'
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
- claim_id: c6
  rel: distinguished_from
  target: fm:tracker-wind-stow-losses
  by: method:tracker-command-log-review
  note: Line up the timestamps of tracker stow commands and wind data with SCADA production, irradiance
    and inverter status. Stow dips follow wind events. Clipping follows the inverter's AC limit.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h6
    h: 733de3a75bd0
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  review: drafted
  review_note: 'support check: partial - Passages say to align stow commands, wind data with SCADA production,
    irradiance and inverter status to separate stow loss from clipping, and stow follows wind; but the
    claim that clipping follows the AC limit is not stated in that passage, and the method is log review
    rather than a named differentiator.'
---
Inverter clipping happens when the array's DC power is more than the inverter's rated AC output, so the inverter limits production to its own maximum. It is not always a fault, because some systems are designed to clip so they produce more in the morning and evening. In monitoring data, output is held flat at the inverter's power ceiling, and most of the lost energy falls on the sunnier days. Performance monitoring tools can estimate the clipped energy by working out the DC size and AC capacity and finding the periods when the AC limit caps output. Do not mix it up with voltage flooring, which is an MPPT limit caused by the DC voltage window. To tell them apart, check DC voltage, AC voltage and reactive power against the Vmp from the IV curve. Also check tracker stow logs and wind data against production so that stow dips are not counted as clipping.

<!-- review notes
- sentence 3: support check: partial - Passages support output limited at the inverter's maximum and more loss on sunnier days, but 'held flat' as a monitoring signature is not explicitly stated.
-->
