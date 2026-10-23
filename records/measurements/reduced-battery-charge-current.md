---
id: meas:reduced-battery-charge-current
type: Measurement
name: Reduced battery charging current
aliases:
- low charging current
---
The signature is a battery that charges at a low current instead of its maximum charging current or power. Cold is a common cause. At low temperatures the battery goes into temperature derating: on SMA Homestorage the charging current is reduced step by step between 15°C and 0°C, and charging stops below 0°C. An ambient temperature that is too high can also limit charging, and with lithium-ion batteries the battery management system may cap the charging power itself. If the inverter overheats, it logs a derating message and lowers the battery charging current. On the Sunny Island, the charging current is also held below the configured AC and DC charging current limits, and it drops once the battery voltage reaches the charging voltage target. In the Sunny Island battery current readings, negative values mean charging, so this signature appears as a negative current that is smaller in magnitude than expected. Before you blame the battery, check the maximum AC charging current setting. If the battery current sensor was reinstalled, recalibrate it so the maximum charging current is calculated correctly.

<!-- review notes
- sentence 2: support check: partial - Temperature derating details are stated in u2, but "cold is a common cause" is not stated; the passage only says charging current depends on ambient temperature, among other things.
- sentence 4: support check: partial - The passages say the inverter reduces battery charging current due to overheating under a "Derating occurred" message, but they don't say it logs the message when it overheats beyond that wording.
- sentence 6: support check: partial - Negative values meaning charging are stated, but the claim that this signature appears as a smaller-magnitude negative current than expected is an inference not in the passages.
- sentence 7: support check: partial - The passages support recalibrating the current sensor after reinstallation and the AC charging current setting influencing charging, but not the advice to check it before blaming the battery.
-->
