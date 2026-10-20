---
id: mit:soiling-model-calibration
type: Mitigation
name: Soiling model calibration
---
Soiling model calibration means tuning the assumed soiling model against the plant's own operating data. It is a listed mitigation for granular dust soiling losses. Calibrate when the modeled soiling rate does not match the recovery seen after rain or cleaning. In that case, update the local dust build-up and wash-off assumptions before using the model to decide on cleaning. Start from normalized production in dry periods. Rule out availability problems, clipping, curtailment and irradiance sensor faults, then compare the trend with soiling station data, rainfall, cleaning logs and reference blocks. Do not size dust losses from a single dirty irradiance sensor. Sensor drift, poor cleaning practice or a local obstruction can look like soiling that the array does not actually have. Rain-based models need a minimum rain amount that cleans the modules and a grace period after rain before dust starts building up again. Different choices for these values give different soiling results. Ground-measured particulate data usually gives better soiling estimates than satellite-derived data. The value chosen for the dust deposition velocity also changes the result. There is still no universally valid soiling model. In one multi-site comparison, models agreed poorly at sites with average losses below 5 percent. A calibrated model supports choosing the best time to clean, which weighs the cost of cleaning against the value of the energy lost to soiling.

<!-- review notes
- sentence 1: support check: partial - Calibrating the soiling model with operational data is listed as a mitigation, but the passages do not define calibration as tuning the model against plant data beyond that wording.
- sentence 8: support check: partial - The passages say best time to clean balances cleaning cost against the cost of lost energy and needs a good soiling model or real-time data, but they don't say a calibrated model specifically supports it.
-->
