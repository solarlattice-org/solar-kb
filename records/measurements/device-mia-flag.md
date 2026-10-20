---
id: meas:device-mia-flag
type: Measurement
name: Device communication MIA flag
aliases:
- MIA
- Battery Meter MIA
- BatteryMeter0.MIA
- Islanding Controller MIA
- Wind Meter MIA
- Generator Meter MIA
- Busway Meter MIA
---
The MIA flag is a true/false status point showing that the site controller (TSC) has lost communication with a connected device such as a meter. A meter is marked MIA once the external SEL-735 has sent no readings for longer than the configurable Meter MIA Time setting. The flag does not clear immediately when the link returns: the meter must keep communicating for the MIA Clear Time setting before the condition resets. The Islanding Controller MIA point goes true when communication between the TSC and the islanding controller has been lost for more than 2 seconds. Treat an MIA flag as a sign of communication loss, and check it apart from meter CT/PT failure flags, which report a different meter condition.

<!-- review notes
- sentence 5: support check: partial - Passages show MIA is communication loss and CT/PT failure is a separate flag, but the advice to check them separately is not stated.
-->
