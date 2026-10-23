---
id: meas:unequal-phase-voltages
type: Measurement
name: Unequal phase voltages
aliases:
- voltage imbalance
- DIFERENT VOLTAGE BETWEEN PHASES
- Unbalance rate of grid voltage
- Grid Voltage Balance
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: large spread between the three measured phase voltages
---
This signature shows up when the three phase-to-neutral voltages (A, B and C to neutral) are not the same size, or when the phase-to-phase voltages differ from one another. On a four-wire wye connection, each phase-to-neutral voltage is taken against a shared neutral lead, so you need that neutral to read each phase separately. A healthy positive-sequence system has phases of equal magnitude spaced 120 degrees apart, so any departure from equal magnitudes points to imbalance. Power quality meters report imbalance as percent negative-sequence and percent zero-sequence voltage imbalance, plus a three-phase average voltage. Recorders can aggregate these values over 3-second, 10-minute and 2-hour windows. String inverters may have a grid voltage unbalance-rate setting that sets how much imbalance they tolerate. When voltages differ between phases, one troubleshooting guide says to check that the supply is not in low voltage and that the load type is not variable. On distribution feeders, zero-sequence voltage imbalance is usually below 2 percent. Imbalance drives a steady-state neutral current through grounding banks.

<!-- review notes
- sentence 1: support check: partial - Passages only define the phase-to-neutral and phase-to-phase voltage measurements; they never say unequal values constitute a signature of imbalance.
- sentence 3: support check: partial - Positive-sequence is defined as equal magnitude and 120° displacement, but the passage does not state that departures from equal magnitude indicate imbalance.
- sentence 5: support check: partial - A GridVoltUnbalance parameter ('Unbalance rate of grid voltage') with a range is listed, but nothing says it is a tolerance setting or that it applies to string inverters.
- sentence 7: support check: partial - The passage says zero-sequence voltage is usually less than 2% in a distribution line and that imbalance causes steady-state zero-sequence current, but it does not explicitly say the current flows through grounding banks as stated in general (it is a worst-case estimate for the grounding bank rating).
- sentence 1: review: partial - The passages define the phase-to-neutral and phase-to-phase voltage quantities, but they never say that unequal values make up the signature.
-->
