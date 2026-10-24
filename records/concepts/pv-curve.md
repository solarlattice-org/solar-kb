---
id: concept:pv-curve
type: Concept
name: P-V characteristic curve
aliases:
- P-V curve
- power-voltage curve
- PV curve
- PV characteristic curve
- power/voltage characteristic curve
- power curve
category: Modules
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:iv-curve
  note: The same inverter measurement can be shown either as an I-V curve or as a P-V curve; the power
    curve is drawn alongside the I-V curve.
  cite:
  - src: src:kb-sungrow-what-is-the-meaning-of-iv-characteristic-curve-and-pv-characteristic-curve
    loc: sec=h1
    h: 32a2ae9cb80b
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=2
    h: 166627579edc
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h69
    h: 25e4829a371e
  review: drafted
- claim_id: c2
  rel: related_to
  target: func:iv-curve-scan
  note: The inverter's diagnostic function can show its measurement results as a P-V characteristic curve.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h69
    h: 25e4829a371e
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:mppt
  note: MPPT looks for the voltage operating point that gives the most energy from the array. Inverters
    use this same capability to measure the curve.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=2
    h: 166627579edc
  review: drafted
  review_note: 'support check: partial - Passages link MPPT to I-V measurement and the power curve is
    shown with it, but no passage directly ties the P-V curve to MPPT.'
- claim_id: c4
  rel: related_to
  target: method:iv-curve-tracing
  note: Problems in the array can be found by comparing a measured curve with the ideal curve or with
    earlier measurements.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=2
    h: 166627579edc
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h69
    h: 25e4829a371e
  review: drafted
---
The P-V characteristic curve plots the output power of a PV module or string against its operating voltage. One manufacturer FAQ describes the PV curve as the output power of a PV module under different light intensities. It describes the I-V curve as the relationship between output current and output voltage. To get the curve, the string is run at a series of voltages and the current is measured at each one. The result is shown as an I-V curve, and the matching power curve is often drawn with it. Inverters that perform maximum power point tracking look for the voltage operating point that gives the most energy, and they can use this same capability to measure the curve during operation. Some inverters have a diagnostic function that can show the measured data either as an I-V curve or as a P-V curve. Comparing a measured curve with the ideal curve, or with earlier measurements taken in similar conditions, shows deviations that point to array problems at an early stage. This diagnosis suits commissioning, periodic maintenance checks and fault finding.

<!-- review notes
- sentence 1: support check: partial - P-V is called a power/voltage curve, but the passages don't explicitly say it plots power against operating voltage of a module or string; u8 describes power under different light intensities.
-->
