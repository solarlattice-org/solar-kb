---
id: concept:iv-curve
type: Concept
name: I-V characteristic curve
aliases:
- I-V curve
- current-voltage curve
- IV curve
- IV characteristic curve
- current/voltage characteristic curve
category: Modules
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:pv-curve
  note: Measured I-V data can also be shown as a power/voltage curve.
  cite:
  - src: src:kb-sungrow-what-is-the-meaning-of-iv-characteristic-curve-and-pv-characteristic-curve
    loc: sec=h1
    h: 32a2ae9cb80b
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h69
    h: 25e4829a371e
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:open-circuit-voltage
  note: The curve is bounded at one end by the open-circuit voltage.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=2
    h: 166627579edc
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4
    h: dbeab86d1089
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:short-circuit-current
  note: The curve is bounded at the other end by the short-circuit current.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=2
    h: 166627579edc
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4
    h: dbeab86d1089
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: related_to
  target: concept:fill-factor
  note: Fill factor is reported as a value describing the curve shape.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4.r6
    h: 2a6a61fd1bde
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4
    h: dbeab86d1089
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:maximum-power-point
  note: Vmpp, Impp and Pmpp are read from the curve.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4
    h: dbeab86d1089
  review: drafted
  review_note: 'support check: partial - Vmpp, Impp and Pmpp are listed as values, but the passages don''t
    say they are read from the curve or name the MPP concept explicitly.'
- claim_id: c6
  rel: related_to
  target: func:mppt
  note: Inverter MPPT capability can be used to sweep the string and record the curve.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=2
    h: 166627579edc
  review: drafted
- claim_id: c7
  rel: related_to
  target: func:iv-curve-scan
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: sec=7.5.15
    h: d9fa214a8ed0
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: sec=h220
    h: 8d3ed00abf39
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=1
    h: d6abe34d5bd9
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h69
    h: 25e4829a371e
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h68
    h: 2c8709ba1cf9
  review: drafted
- claim_id: c8
  rel: related_to
  target: method:iv-curve-tracing
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=2
    h: 166627579edc
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=1
    h: d6abe34d5bd9
  review: drafted
---
The I-V characteristic curve describes how the output current of a PV module or string relates to its output voltage. To measure it, the string is held at a range of voltages and the current at each voltage is recorded. The curve runs from the short-circuit current at one end to the open-circuit voltage at the other. Values read from the curve include maximum power voltage, current and power, open-circuit voltage, short-circuit current, and the fill factor, which describes the shape of the curve. Some inverters use their built-in MPPT to trace the curve for each MPP tracker or string. This avoids the time and cost of a separate measuring instrument. The same data can be plotted as a P-V characteristic curve, which shows power against voltage. Compare the measured curve with the ideal curve, or with earlier curves taken in similar conditions. Deviations can point to installation errors, faults or damage in the array. This makes I-V curve checks useful at commissioning, during scheduled maintenance and when diagnosing faults.

<!-- review notes
- sentence 2: support check: partial - The sweep at different voltages and the bounds are stated, but not the specific direction (short-circuit current at one end, open-circuit voltage at the other), nor that the string is 'held' at each voltage.
- sentence 4: support check: partial - Inverter MPPT is used to measure the curve and it replaces expensive specialized devices, but 'some inverters' and the per-tracker or per-string scope are only loosely stated, and 'time and cost' is stated as the traditional drawback rather than explicitly avoided.
-->
