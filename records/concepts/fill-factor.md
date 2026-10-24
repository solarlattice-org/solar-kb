---
id: concept:fill-factor
type: Concept
name: Fill factor
aliases:
- FF
category: Modules
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:iv-curve
  note: Fill factor describes how square the I-V curve is; a higher value means the curve is closer to
    a rectangle.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h24
    h: 69690a32e377
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4.r6
    h: 2a6a61fd1bde
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h34
    h: 10af29999ece
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-expansion-fittings-sunspec
    loc: sec=h34
    h: 10af29999ece
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:maximum-power-point
  note: FF = Pmpp / (Voc x Isc).
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h24
    h: 69690a32e377
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h34
    h: 10af29999ece
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-expansion-fittings-sunspec
    loc: sec=h34
    h: 10af29999ece
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:open-circuit-voltage
  note: Voc is in the denominator of the fill factor formula. The ratio Vmp/Voc is one of its sub-factors.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h24
    h: 69690a32e377
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h34
    h: 10af29999ece
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-expansion-fittings-sunspec
    loc: sec=h34
    h: 10af29999ece
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:short-circuit-current
  note: Isc is in the denominator of the fill factor formula. The ratio Imp/Isc is one of its sub-factors.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h24
    h: 69690a32e377
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h34
    h: 10af29999ece
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-expansion-fittings-sunspec
    loc: sec=h34
    h: 10af29999ece
  review: drafted
- claim_id: c5
  rel: related_to
  target: method:iv-curve-tracing
  note: All I-V curve tracers report the fill factor. It is used to troubleshoot underperforming strings.
  cite:
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h34
    h: 10af29999ece
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-expansion-fittings-sunspec
    loc: sec=h34
    h: 10af29999ece
  review: drafted
- claim_id: c6
  rel: related_to
  target: tool:iv-curve-tracer
  cite:
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h34
    h: 10af29999ece
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-expansion-fittings-sunspec
    loc: sec=h34
    h: 10af29999ece
  review: drafted
- claim_id: c7
  rel: related_to
  target: symptom:fill-factor-reduction
  note: A fill factor well below the datasheet value at nominal conditions can point to faults that cause
    yield loss.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h24
    h: 69690a32e377
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h34
    h: 10af29999ece
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-expansion-fittings-sunspec
    loc: sec=h34
    h: 10af29999ece
  review: drafted
---
Fill factor (FF) is a characteristic value that describes the shape of a PV source's I-V curve. It tells you how square the curve is. It equals the maximum power divided by the product of open-circuit voltage and short-circuit current, so Pmax equals FF times Isc times Voc. The higher the fill factor, the closer the I-V curve is to a rectangle. Any degradation in the curve shape lowers the fill factor and the power output. Compare a string's fill factor with the module datasheet value and with other strings that use the same module type. A value well below the datasheet at nominal conditions may point to faults that cause yield loss. The sub-factors Imp/Isc and Vmp/Voc show changes in the slope of the horizontal and vertical legs of the I-V curve. This helps when diagnosing underperforming strings. Fill factor works well for comparing strings because it is calculated only from the measured I-V curve. It is also fairly independent of irradiance at high irradiance, so errors in the irradiance or temperature sensors do not affect it. All I-V curve tracers report fill factor. Typical cell values are 0.75 to 0.80 for polycrystalline silicon and 0.80 to 0.85 for monocrystalline silicon.

<!-- review notes
- sentence 5: support check: partial - Sub-factors give insight into slope variations of the legs, but the passages do not explicitly say this helps diagnose underperforming strings (only FF is tied to troubleshooting).
-->
