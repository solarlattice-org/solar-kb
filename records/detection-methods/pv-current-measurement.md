---
id: method:pv-current-measurement
type: DetectionMethod
name: PV input current measurement
aliases:
- PV string current measurement
- PV string current monitoring
---
When CPS string inverters raise a PV Over current protection code, the first step is to check the PV input current. Compare the measured current with the inverter's rated maximum PV input current. On the CPS units this rating is based on module Isc multiplied by 1.25. Sungrow SG200HX and SG350HX inverters have built-in PV string current monitoring, so the input currents can be read from the inverter. Also check the current against the maximum rating of the input connectors. Inverter-level measurement of DC input voltage and current is recommended to be accurate within plus or minus 2 percent. If the current checks out but the fault stays, power cycle both the AC and DC switches and wait one minute between off and on so stored energy can discharge. Replace the inverter if the fault still does not clear.

<!-- review notes
- sentence 2: support check: partial - Passages show Max PV Isc x 1.25 = 275A for the SCH125KTL model, but not the instruction to compare measured current, and only one CPS model is covered.
- sentence 4: support check: partial - Passages give a max input connector current (30 A, 40 A optional) but only as a spec, not as a troubleshooting step for this fault, and they're not CPS-specific.
- sentence 5: support check: partial - The passage shows a ±2% value for inverter-level DC measurement but doesn't say it is a recommendation (it appears to be a table of accuracy requirements).
-->
