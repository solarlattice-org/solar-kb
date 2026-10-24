---
id: metric:availability
type: Metric
name: Availability
aliases:
- time-based availability
- plant availability
- uptime
- Technical Availability
- inherent availability
category: Performance
---
Availability is the share of time that a device, subsystem or plant runs normally, out of the total time it is expected to run. For a PV plant, technical availability divides the plant's operating time by the useful time. Useful time counts only the periods when irradiance is above a minimum irradiance threshold, which is typically 50 or 70 W/m^2. No exclusions are applied. Inverter-level data are the recommended input. The time window can be set either by an irradiance threshold (often at least 30 W/m²) or by a fixed range of hours, and the irradiance threshold is preferred because seasons and weather do not skew it. Contractual availability is technical availability with agreed exclusions applied, for example for maintenance. Energy-based availability weights downtime by the energy lost instead of the hours lost. Availability is usually reported as a percentage. O&M contracts commonly guarantee a minimum plant availability, such as 98% contractual availability over a year or at least 99% plant availability. Monitoring platforms may decide whether a device is available from the presence of power data, from power data with no fault, or from power above zero. Results are averaged over 15-minute bins. Technical availability is covered by IEC TS 63019, and a time-based value suits component-level reporting, for example the fraction of days per year a tracker or inverter was available.

<!-- review notes
- sentence 3: support check: partial - u31 supports inverter-level data and the irradiance versus hour-range windows. It says the irradiance approach is preferred because seasonality and weather don't affect it. It gives a minimum of 30 W/m² as 'usually a good approach', not 'often at least', and calls inverter-level data a requirement, not a recommendation.
- sentence 6: support check: partial - u10 supports the three condition options. It says 15-minute availability is the base and that bins of 1 hour and above are weighted averages of the 15-minute values, but it does not say that all results are averaged over 15-minute bins.
-->
