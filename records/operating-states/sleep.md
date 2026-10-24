---
id: state:sleep
type: OperatingState
name: Night mode
aliases:
- sleep mode
- sleep
- night time switch-off mode
- Sleeping (auto-shutdown)
- I_STATUS_SLEEPING
- overnight shutdown
category: Inverters
---
Night mode means the inverter has switched itself off automatically because there is not enough PV input, usually after dark. On ABB and FIMER string inverters the inverter goes into night mode when the input voltage falls below 70% of the set start-up voltage, and the front-panel LEDs show this state. On Fronius inverters, Night Mode is a display setting. It controls how the Fronius DATCOM and the inverter display behave at night or when DC voltage is too low. Over SunSpec, SolarEdge inverters report this state as status value 2, I_STATUS_SLEEPING, which means sleeping (auto-shutdown) or night mode. On the Sunny Island, sleep mode is controlled by parameter 250.10 SleepEna, which is enabled by default. The master can then switch off the slaves in single-phase systems when the power level allows. A Sunny Island slave in sleep mode shows display number E107. The default start time for overnight shutdown is 20:00:00.

<!-- review notes
- sentence 1: support check: partial - Passages say automatic night-time switch-off when input voltage is under 70% of start-up voltage; 'usually after dark' and 'not enough PV input' are only loosely implied.
- sentence 2: support check: partial - The 70% threshold and LED display of night mode are stated, but the passages do not name ABB or FIMER string inverters, and the LED display is shown only generically.
- sentence 3: support check: partial - Passages say night mode controls DATCOM and display operation at night or low DC voltage, but do not explicitly call it a display setting (u15 only lists it among settings); the Fronius attribution is implicit.
- sentence 4: support check: partial - Status value 2 I_STATUS_SLEEPING with the sleeping/night mode description is stated, but SolarEdge and SunSpec are not named in the passage.
-->
