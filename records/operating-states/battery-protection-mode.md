---
id: state:battery-protection-mode
type: OperatingState
name: Battery protection mode
aliases:
- battery protection
- battery-preservation mode
- LBM
category: Storage
product: prod:sma-sunny-island
---
Battery protection mode is a normal Sunny Island function that protects the battery when its state of charge falls below set thresholds. The mode has three levels, and each level has its own state of charge threshold. Levels 1 and 2 also have start and end times, so they depend on the time of day. At level 1, the Sunny Island goes into energy-saving mode during the set time window. At level 2, it goes into energy-saving mode and, outside the window, starts up every two hours to try to charge the battery. At level 3, the Sunny Island switches itself off to protect the battery from deep discharge. It must then be switched on and started manually before the battery can be charged. At every level, the unit only changes state after no charging current has flowed into the battery for a minimum time. The manuals give this as at least five minutes, and the expert parameter BatProTmm sets it. The default thresholds are 20 percent for level 1, 15 percent for level 2 and 10 percent for level 3. Each threshold can be set from 0 to 70 percent. The thresholds and time windows are set in the Battery > Protection mode menu or through the BatPro parameters on the Sunny Remote Control. An event reports that battery protection mode 1, 2 or 3 is active. On US models, level 3 appears as display message W757. If this happens often, a technician should check battery charging and the threshold settings.

<!-- review notes
- sentence 7: support check: partial - Battery > Protection mode menu is stated and BatPro SOC parameters on the Sunny Remote Control are shown, but the time-window parameters on the Remote Control are only listed as parameters, not explicitly stated as set there; menu is for communication product, not named as such.
- sentence 8: support check: partial - Event text and W757 as battery-preservation mode 3 are present, but 'US models' and the advice for a technician to check charging and thresholds are not in the passages.
-->
