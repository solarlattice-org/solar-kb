---
id: meas:negative-sequence-voltage-imbalance
type: Measurement
name: Negative-sequence voltage imbalance
aliases:
- V_IMB
- V_IMB_n
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: phase voltage deviates from the other phases instead of tracking them
---
Negative-sequence voltage imbalance is a three-phase power quality value that a revenue meter reports as a percentage. The meter works it out from the ratio of the negative-sequence voltage component to the positive-sequence component. The instantaneous value is refreshed every 10/12 cycles, and the meter can also record an aggregated version whose update rate depends on the aggregation period. If the positive-sequence voltage is very low, the meter reports the imbalance as zero, so a zero reading during an outage does not mean the phases are balanced. The meter also reports the negative-sequence voltage magnitude in volts, updated every half-cycle, which helps you read the percentage in context. Negative sequence means a set of equal three-phase quantities rotating in the opposite order to the normal sequence, so a rising percentage shows the phase voltages are moving away from a balanced set.

<!-- review notes
- sentence 2: support check: partial - The passage says the calculation uses X1 and X2 components but the equation is missing; the ratio of V2 to V1 is implied, not explicitly stated.
- sentence 4: support check: partial - Passage states V_IMB is zero when V1 is below 13 V, but the outage example and that zero doesn't imply balance are inferred, and 'very low' is specifically 13 V.
- sentence 5: support check: partial - V2_MAG is negative-sequence voltage in volts at half-cycle update, but the 'helps read percentage in context' claim is not stated.
- sentence 6: support check: partial - Definition of negative sequence (equal magnitude, 120° displacement, reversed order ACB) is given, but the interpretation that a rising percentage shows moving away from balance is not stated.
-->
