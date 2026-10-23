---
id: meas:battery-soc-reading-low
type: Measurement
name: Low battery SOC reading
aliases:
- SOC
- BatSoc
- State of Charge
---
The battery state of charge is shown as a percentage, for example in the BatSoc parameter on the inverter display or user interface. SOC cannot be measured directly; it is estimated from ampere-hour counting combined with recalibration against battery voltage, so wrong installation or parameter settings make the reading less accurate. If the battery voltage falls more sharply than expected while discharging, the SOC is reset to 20% to protect against deep discharge, and messages E224 and W222 flag the recalibration and any jump of more than 10%. Frequent resets to 20%, fast SOC changes and large jumps point to incorrect settings, premature battery aging, poor battery maintenance, installation errors or battery faults. A low SOC can also result from a battery with less capacity than the rated figure, or from a system that is sized too small to recharge the battery. Check the first case with a capacity test. When SOC reaches the lower threshold, the loads are disconnected by the load contactor and a grid request for low state of charge is logged as event 1609. With a newly connected battery, the SOC reading can deviate strongly from the true value in the first two operating hours and trigger load shedding. A lithium battery left at low charge for a long time gives an inaccurate SOC reading, which a battery healing charge is meant to correct.

<!-- review notes
- sentence 5: support check: partial - Both causes and the capacity test for the first are stated, but the passages do not explicitly say these cause a low SOC (the cause rows lack the symptom context), and 'undersized to recharge' is only implied.
- sentence 6: support check: partial - The load contactor opening at the lower SOC threshold is stated, and event 1609 exists as a grid request for low SOC, but the passages do not link the two or say the event is logged at that point.
-->
