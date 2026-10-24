---
id: metric:performance-index
type: Metric
name: Performance index
aliases:
- PI
- Energy performance index
- EPI
category: Performance
claims:
- claim_id: c1
  rel: part_of
  target: std:iec-61724-3
  note: NREL O&M best practices state that the energy performance index is defined by IEC 61724-3; the
    power performance index variant is described in IEC 61724-2.
  cite:
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=6.1.1
    h: 581ffc57a0ee
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
The performance index compares the energy or power a PV plant actually delivered with what it was expected to deliver, given the measured weather and irradiance and a performance model the stakeholders have agreed on. In words, it is measured output divided by modeled output. In AlsoEnergy's platform it is the ratio of measured power to modeled power for a meter or an inverter. The energy version is defined in IEC 61724-3. The power version, described in IEC 61724-2, works the same way but uses power output instead of energy output. The energy index comes in two forms. The all-in form covers every hour and season of the year. The in-service form leaves out the energy that was expected while the system was not operating, which makes it a good companion to energy availability. A healthy plant should have a performance index close to unity. Because the index is based on modeled expectations, it stays more consistent than performance ratio across seasons, locations and unusual weather. In a short-term capacity test, the index is measured average power divided by predicted average power. This is a spot check of instantaneous performance and does not include downtime. In AlsoEnergy's LocusNOC platform, a PI alert is raised when the hourly PI stays below a value threshold (default 0.8, allowed range 0.0 to 1.0) for longer than a set number of hours. Only daylight hours count, trimmed by an optional buffer after sunrise and before sunset.

<!-- review notes
- sentence 7: support check: partial - The passages support the hourly PI threshold, the 0.8 default, the 0.0–1.0 range, the daylight-only counting and the buffer. The statement calls the time threshold a number of hours, but the passage only says 'time threshold' or 'threshold hours', so the unit is not clearly stated. The buffer range is 0–4 hours, which the statement does not mention.
-->
