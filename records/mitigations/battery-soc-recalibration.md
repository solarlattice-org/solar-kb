---
id: mit:battery-soc-recalibration
type: Mitigation
name: Battery SOC recalibration
aliases:
- voltage recalibration
- recalibration
- full-charge detection
- full-charge calibration
- Ah counting recalibration
- relearn 100% SOC
- charge to upper limit at intervals
- SOC recalibration
---
Battery SOC recalibration corrects the estimated state of charge so that it matches the real battery condition. It addresses battery state-of-charge estimation drift, because SOC cannot be measured directly and is always an estimate. The Sunny Island estimates SOC by ampere-hour counting with full-charge detection and corrects the result against battery voltage. Under very low load, the SOC from open-circuit voltage is compared with the ampere-hour count, and the SOC is moved up or down if the two differ. These small corrections usually do not point to a battery problem. During discharge, an unexpectedly sharp voltage drop makes the inverter reset SOC to 20% to protect the battery from deep discharge. This reset does not run when SOC is above 70%. For lithium-ion batteries, charge to the upper limit now and then so the 100% point is relearned and the cells in series do not drift apart. If SOC stays below 100% after a full charge, set a longer full charge time. Frequent 20% recalibrations, or SOC jumps of more than 10%, point to wrong settings, aged batteries, poor maintenance, bad pole connections or installation errors. Recalibration does not fix these causes. First check that the battery capacity is entered correctly, then start an equalization charge and watch how the system responds. Contact the manufacturer if the problem continues.

<!-- review notes
- sentence 6: support check: partial - The causes are stated (wrong settings, aging, poor maintenance, pole connection problems, installation errors), but no passage says that recalibration does not fix these causes.
- sentence 7: support check: partial - The passages mention checking the battery capacity, an equalization charge with observation, and contacting the Service Line or the battery manufacturer, but they give no order, and the manufacturer step is only 'in some cases', not 'if the problem continues'.
-->
