---
id: symptom:reconnection-limits-not-met
type: Symptom
name: Grid reconnection conditions not met
aliases:
- Grid frequency or voltage outside the permissible range for reconnection
- FrqCtl.ReconMax
- VolCtl.ReconMax
- Event 15 or 1501
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grid-frequency-reading-out-of-limit
  note: After a disturbance some country standards apply stricter reconnection limits than the trip limits.
    The frequency is usually above the upper reconnection limit.
  cite:
  - src: src:sma-kb-event-number-15-1501
    loc: sec=h1
    h: 417ad29c4b85
  - src: src:sma-doc-275857
    loc: sec=h124
    h: 0b18bf5abdd3
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=34.r7
    h: d7c037fa0427
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=34.r6
    h: 3bc448523e3b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Passages support frequency outside reconnection limits (ReconMax/ReconMin,
    usually too high), but the signal details like W staying at zero until frequency returns are not stated.'
- claim_id: c2
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: Grid voltage falls right after feed-in stops, so a reading taken after the trip may rarely show
    a value above the set limits.
  cite:
  - src: src:sma-kb-event-number-15-1501
    loc: sec=h1
    h: 417ad29c4b85
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=34.r5
    h: cc5affb264c2
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=42
    h: a2be9cdcfbaf
  - src: src:sma-kb-reading-out-the-current-grid-voltage-and-the-grid-voltage-limit-value-set-in-the-in
    loc: sec=h1
    h: 51012ad6c878
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: observed_as
  target: meas:grid-ok-flag-false
  note: Islanding controller output that is true only when grid voltage and frequency are within the reconnect
    thresholds.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=60.r10
    h: dac1f80151b8
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA reports this condition as event 15 or 1501.
  cite:
  - src: src:sma-kb-event-number-15-1501
    loc: sec=h1
    h: 417ad29c4b85
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=34.r1
    h: 20455651a3a5
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=53.r1
    h: 20455651a3a5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
After a grid fault the inverter stays off the grid because the measured grid frequency or voltage is outside the allowed range for reconnection. Some country standards use tighter limits for reconnection than for normal operation, for example an upper reconnection frequency of 50.05 Hz under VDE AR-N 4105, and the most common cause is a frequency that is too high. The inverter itself is not faulty and switches back on by itself once frequency and voltage have stayed inside the range for the grid monitoring time. First, read out the live grid frequency and voltage, the country standard and the reconnection limits over the communication interface, then compare them with your own grid measurement. A voltage reading taken after the trip may look normal, because grid voltage at the inverter drops as soon as feed-in stops. Look for large local loads such as machines that make the grid fluctuate. If the grid itself is out of range, the grid operator decides on fixes or on allowing changed inverter settings. In rare cases the cause is an incorrect or edited country data set (grid code misconfiguration). Reloading the original data set for the installation country fixes this.

<!-- review notes
- sentence 3: support check: partial - The inverter not being faulty and automatic switch-on after the grid monitoring time once values are in range are stated, but 'stayed inside for the monitoring time' is only loosely implied.
- sentence 4: support check: partial - Reading out frequency, voltage, country standard and limits via communication and using grid measurements to determine too high/low is stated, but the explicit 'compare with your own grid measurement' and the 'first' ordering are not.
-->
