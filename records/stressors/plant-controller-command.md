---
id: stressor:plant-controller-command
type: Stressor
name: Plant controller command
---
A plant controller command is a limit set by the power plant controller that holds plant export below the power the array could actually produce. The power plant controller is a control system that manages active power, reactive power and ramp rates. Its setpoints can be sent remotely or locally from the SCADA system. This stressor does not physically damage modules or inverters. It is one of several sources of grid curtailment yield losses, alongside grid operator dispatch, interconnection constraints, negative pricing and site export caps. In the field, output looks flat or held at a controlled level below what the irradiance supports, while inverter and tracker availability look normal. This makes it easy to mistake for underperformance. A low performance ratio during constrained hours may reflect control instructions more than the health of modules, inverters or trackers. To confirm it, reconstruct the available power and compare it with meter output and the plant controller limits. Then assign each constrained interval a cause, with plant controller behavior as a separate class. To limit the impact, track curtailment separately from equipment loss and use curtailment-aware performance metrics. At storage sites, tune battery charging so curtailed energy can be captured where possible. The control system should be password protected, log every executed command and send real-time notifications to the operations team.

<!-- review notes
- sentence 1: support check: partial - The passage lists plant controller command as one source of limitation where the plant can produce more than it may export, but does not define it as a limit set by the power plant controller.
- sentence 3: support check: partial - The list of curtailment sources is stated, but the passages never say that curtailment does not physically damage modules or inverters.
-->
