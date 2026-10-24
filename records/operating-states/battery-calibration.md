---
id: state:battery-calibration
type: OperatingState
name: Battery SoC calibration
aliases:
- SoC recalibration
- calibration charge
- 20 percent calibration
- 20% recalibration
- SoC calibration
category: Storage
---
SoC recalibration is a normal battery-management step. The Sunny Island finds that its calculated state of charge does not match the battery voltage and corrects it upward or downward. The Sunny Island works out the state of charge by combining ampere-hour counting, which includes full-charge detection, with this voltage-based recalibration. One type of recalibration runs when there is almost no load. It compares the state of charge read from the open-circuit voltage with the ampere-hour count. These corrections usually do not mean the battery has a problem. The other type watches the voltage while the battery discharges. If the voltage drops more sharply than expected, the state of charge is reset to 20% to protect the battery from deep discharge. This reset is inactive while the state of charge is above 70%. The Sunny Island logs E901 when a recalibration starts and E902 when it stops. A 20% recalibration shows E224, or event 9322 in some documents. W222 appears if the 20% recalibration made the value jump by more than 10%. With a healthy battery and correct settings, small jumps of less than 10% are normal. Repeated 20% recalibrations or bigger jumps point to poor battery maintenance, aged batteries, installation or terminal connection errors, or poor charging conditions. If recalibrations happen often, check that the battery capacity is set correctly. SMA also recommends running an equalization charge and watching how the system responds, then contacting SMA Service or the battery manufacturer if needed. On Enphase systems, IQ Gateway software releases have improved the SoC calibration algorithm for third-generation systems with IQ Battery 5P.

<!-- review notes
- sentence 8: support check: partial - Passages state improved SoC calibration algorithm for 3rd-gen systems with IQ Battery 5P, but nothing mentions IQ Gateway software releases.
-->
