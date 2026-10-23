---
id: symptom:insufficient-irradiance
type: Symptom
name: Insufficient solar irradiance
aliases:
- Insufficient solar irradiation
- low irradiance
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-poa-irradiance
  note: Typical of night, dawn, dusk and low-light periods. Performance-loss analyses usually filter these
    periods out with a low irradiance cutoff. One inverter manual lists insufficient irradiation at dawn
    or dusk as a cause of the LED being red or off.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.2.1
    h: 25d44e243a86
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=46.r17
    h: 8f65368e048e
  review: drafted
---
Insufficient irradiance means too little sunlight reaches the array, typically at night, dawn, dusk or in other low-light periods. On some string inverters it shows up as a status LED that is red or off at dawn or dusk, which is normal behaviour, not a fault. In monitoring data, low irradiance periods are usually filtered out before performance loss is assessed, with low cutoffs generally around 100-200 W/m2. Low power during low irradiance is expected, but low power while irradiance is high points to an outage or a real fault instead. If an IV curve trace deviates from the model, first check whether irradiance was too low, the sun was near the horizon, or the irradiance sensor is out of plane or out of calibration. Under low irradiance, IR thermography may not reveal disconnected strings, PID, shunted cells or shorted bypass diodes, because the temperature difference scales with irradiance. For IR inspections, wait for irradiance above 600 W/m2 and stable, cloud-free conditions.

<!-- review notes
- sentence 1: support check: partial - Passages mention night and low irradiance periods and dawn/dusk, but do not define insufficient irradiance as too little sunlight reaching the array in those terms; 'other low-light' is loosely implied.
- sentence 2: support check: partial - The LED red/off with insufficient irradiation at dawn/dusk is stated, but nothing says it is normal behaviour rather than a fault (it is labelled 'Fault correction') or that it is specific to string inverters.
- sentence 4: support check: partial - The passage says power is low during outages even when irradiance is high, but does not state that low power at low irradiance is expected or that high-irradiance low power indicates a 'real fault'; outage part is supported.
-->
