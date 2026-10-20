---
id: meas:negative-sequence-current-imbalance
type: Measurement
name: Negative-sequence current imbalance
aliases:
- I_IMB
- I_IMB_n
- Aggregated negative-sequence current imbalance
signals:
- point: model_103.A
  unit: unit:A
  pattern: phase currents unequal at steady output
---
Negative-sequence current imbalance is a revenue meter quantity, labeled I_IMB and reported as a percentage, that shows how unbalanced the three phase currents are. The meter calculates it by comparing the negative-sequence current component with the positive-sequence component. A negative-sequence set is three equal-magnitude quantities 120 degrees apart that rotate in the opposite order to normal, so maxima occur as ACB instead of ABC. The meter updates the value every 10/12 cycles, and an aggregated version, I_IMB_n, updates once per configured aggregation period. If the positive-sequence current is below 10 mA, the meter reports this imbalance as zero, so a zero reading at very low load does not show the phases are balanced. Read it together with negative-sequence voltage imbalance and zero-sequence current imbalance, which the meter reports in the same table. A current transformer connected to the wrong tap is one wiring error that can be found by measuring negative-sequence current and comparing expected with measured current magnitudes.

<!-- review notes
- sentence 1: support check: partial - Name, description and % units are stated, but the passages never call it a 'revenue meter' quantity or say it shows how unbalanced the phase currents are beyond the name.
- sentence 2: support check: partial - The passage says the calculation uses X1 and X2 (positive and negative sequence components), but the equation is missing, so the comparison (ratio) is only implied.
- sentence 5: support check: partial - The 10 mA I1 threshold and zero reporting are stated, but the claim that a zero reading at low load does not indicate balanced phases is an inference not in the passages.
-->
