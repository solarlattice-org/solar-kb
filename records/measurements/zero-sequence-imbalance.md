---
id: meas:zero-sequence-imbalance
type: Measurement
name: Zero-sequence imbalance
aliases:
- V0_IMB
- I0_IMB
- V0_IMB_n
- I0_IMB_n
- Zero-sequence voltage imbalance
- Zero-sequence current imbalance
---
Zero-sequence imbalance is a revenue meter quantity, given in percent, that compares the zero-sequence component of the three phase voltages or currents with their positive-sequence component. The meter reports it separately for voltage and for current, and it updates both values every 10/12 cycles. Aggregated versions of both values are also available, and they update at a rate set by the chosen aggregation period. The meter also calculates negative-sequence imbalance, so read the two signatures side by side when checking a phase imbalance. On delta-connected voltage inputs, the zero-sequence voltage cannot be calculated, so a zero reading there does not mean the phases are balanced. Form 5 meters always report zero for the zero-sequence voltage imbalance because the quantity is undefined for delta connections.

<!-- review notes
- sentence 4: support check: partial - Passages confirm the meter also calculates negative-sequence imbalance, but the advice to read the two side by side when checking phase imbalance is not stated.
- sentence 5: support check: partial - Passages say V0 cannot be calculated for delta voltages and Form 5 reports zero, but the inference that a zero reading doesn't mean balanced is not explicitly stated, and 'delta-connected inputs' generally vs Form 5 is slightly broader.
-->
