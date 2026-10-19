---
id: method:iv-curve-tracing
type: DetectionMethod
name: IV curve tracing
aliases:
- I-V curve tracing
- I-V curve test
- IV curve tracer data
- string-level IV sweeps
- IV tracing
claims:
- claim_id: c1
  rel: produces
  target: meas:iv-rounded-knee
  note: A cell interconnection failure on redundant interconnects raises series resistance, which shows
    as a rounder knee in the IV curve.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:iv-curve-step
  note: When several interconnection failures block current, the bypass diode activates and the IV curve
    shows it.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c3
  rel: produces
  target: meas:low-voc
  note: A short-circuited bypass diode gives a lower Voc than expected. A Voc check during string tests
    also catches a missing module or shorted diodes.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  - src: src:iec-62446-1
    loc: sec=7.2.3
    h: 05b5aab93844
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c4
  rel: produces
  target: meas:fill-factor-reduction
  note: A gap in power or fill factor versus the sum of the individual module curves helps locate the
    problem.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=9.11.2
    h: 0244595bad9b
  - src: src:iea-pvps-t13-25-2022
    loc: tbl=8.r3
    h: 7631a4db55e2
  review: drafted
- claim_id: c5
  rel: produces
  target: meas:pmax-below-rated
  note: Measured maximum power is compared with the nameplate rating or with a modeled expected curve.
  cite:
  - src: src:iec-62446-1
    loc: sec=7.2.3
    h: 05b5aab93844
  - src: src:iea-pvps-t13-07-2017
    loc: sec=5.3.2
    h: 5cd9bad228fd
  review: drafted
  review_note: 'support check: partial - Comparison with nameplate rating is stated, and a modeled (GPR)
    expected curve is used in another passage, but it is not framed as the same Pmax comparison.'
- claim_id: c6
  rel: produces
  target: meas:operating-voltage-above-iv-vmp
  note: Supports a voltage-floor diagnosis when the inverter operating voltage stays above the IV-derived
    Vmp and the operating power is below the IV-derived Pmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
- claim_id: c7
  attr: typical_power_loss
  value:
    nominal: 38
    unit: unit:W
  conditions: One faulted string in a statistical I-V curve study. The fault was found by comparing the
    measured curve with a Gaussian Process estimate of the normal curve.
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=5.3.2
    h: 5cd9bad228fd
  review: drafted
  review_note: 'support check: partial - The 38 W loss for string 2 found via GPR comparison is stated,
    but ''typical'' is not supported since it is a single instance.'
---
IV curve tracing sweeps a module or string from zero volts up to open-circuit voltage while recording current under a known irradiance. From the curve you get power, short-circuit current, open-circuit voltage, fill factor, and shunt and series resistance. The curve shape points to the cause of a power loss and lets you calculate how much is lost. Before testing, shut the system down and make sure no current is flowing. Then isolate the string, connect it to the tracer, and mount the irradiance sensor in the array plane with no shade or reflected light on it. Test only under stable irradiance of at least 400 W/m2 in the array plane, because low light or an oblique sun angle gives poor results. IV curve tracing helps detect bypass diode failure, cell interconnection failure, junction box failure and cell cracks. It also checks for inverter voltage floor losses by comparing the inverter operating voltage with the Vmp taken from the curve. A shorted bypass diode shows up as low Voc, but an open diode is hard to spot unless the module has significant mismatch. Tracing single modules means disconnecting the whole string, which costs production and labour, so try visual inspection and IR imaging first.

<!-- review notes
- sentence 5: support check: partial - Passages support bypass diode, interconnection failure, and inverter voltage floor use; junction box only mentions short-circuits via open-circuit measurement or IV curve, and cell cracks only has a figure caption.
-->
