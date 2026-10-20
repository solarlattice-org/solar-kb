---
id: meas:phase-voltage-spread-alert
type: Measurement
name: Phase voltage spread alert
aliases:
- Meter Voltages
---
This alert fires when the measured phase voltages of a three-phase meter or inverter no longer match each other closely. One monitoring platform ships it as a default meter voltage alert that checks the phase voltages stay within 5% of each other. The inputs are the individual phase RMS voltages, or the line voltages between phase pairs such as A-B and B-C. Power meters can also report the spread as a percent negative-sequence or zero-sequence voltage imbalance, refreshed every 10 or 12 cycles. When phase voltages differ, one meter manual says to first check whether a low supply voltage is present. The same manual says to also check that the connected load type is not variable, because a variable load can cause unequal phase voltages. Some inverters have a configurable grid voltage imbalance threshold, so a large spread can also cause an inverter protection event.

<!-- review notes
- sentence 4: support check: partial - Table lists negative- and zero-sequence voltage imbalance in % at 10/12 cycles, but does not say they are for 'power meters' or that they report the phase spread, and the table says '10/12 cycles' (one or the other depending on frequency), not a choice.
- sentence 6: support check: partial - Passage says verify load type is not variable, but does not state that a variable load causes unequal phase voltages, nor that it is the same manual.
- sentence 7: support check: partial - A configurable grid voltage imbalance threshold exists, but passages do not state that exceeding it causes an inverter protection event.
-->
