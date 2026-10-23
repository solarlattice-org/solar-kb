---
id: meas:ct-calibration-event
type: Measurement
name: CT calibration event code
aliases:
- ct cal
---
This signature is a 'ct cal' event that the inverter logs during automatic current transformer detection. It appears in the Generac PWRcell troubleshooting table. Codes 0x8061 to 0x8067 mean that one or more lines (Line 1, 2 or 3, alone or in combination) do not have a valid CT calibration. Codes 0x8069 to 0x806F mean that a line has more than one CT, a CT is missing, or a CT has been placed on the neutral wire. The suffix after 'ct cal' (1 to 7, or 9 and A to F) shows which line or lines are affected, so you can tell which CT to check. These codes point to an incorrect current transformer installation, such as a missing CT, a duplicated CT or a CT on the neutral. The 'ct cal success' event, code 0x8070, confirms that calibration worked. Look for it after you correct the CT placement.

<!-- review notes
- sentence 3: support check: partial - Codes 0x8069–0x806F cover multiple CTs, missing CTs (only for the combined-line codes B, D, E, F) and CT on neutral; 0x8069 and others don't say missing, and 0x8068 is absent, so the blanket range wording is slightly overgeneral.
- sentence 5: support check: partial - Codes 0x8069–0x806F describe multiple/missing CTs or CT on neutral, but 0x8061–0x8067 only say invalid calibration, not an incorrect installation, so 'these codes' overstates.
- sentence 6: support check: partial - The passages state 0x8070 'ct cal success' means calibration was successful, but nothing says to look for it after correcting CT placement.
-->
