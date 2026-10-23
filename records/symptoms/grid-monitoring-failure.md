---
id: symptom:grid-monitoring-failure
type: Symptom
name: Grid monitoring failure
aliases:
- Failure of the grid monitoring
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Sunny Island displays F782 (level 4) when grid monitoring fails, and W797, W798 or W799 (level
    1) when grid monitoring fails on slave 1, 2 or 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r20
    h: c640e534dffe
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r28
    h: d81e3dc1d08e
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r29
    h: ae70d7a84271
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r30
    h: 525853dc4d98
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
On SMA Sunny Island units, a failure of the grid monitoring function shows as display code F782, which is a level 4 message. In a cluster, warnings W797, W798 and W799 are level 1 messages that point to a grid monitoring failure on slave 1, slave 2 or slave 3, so the code tells you which device to check. In SMA devices, grid monitoring covers grid-related parameters, some of which are protected by the SMA Grid Guard code. Do not confuse this with a grid failure, which SMA defines as a utility grid outage or voltage and frequency moving outside the country-specific limits. A grid fault is logged when the voltage or frequency monitoring trips, while a monitoring failure means the monitoring function itself has failed. If grid failure events come back several times a day, SMA advises contacting the responsible grid operator.

<!-- review notes
- sentence 5: support check: partial - Grid fault definition (voltage or frequency monitoring triggered) is stated, and F782 is a failure of grid monitoring, but 'the monitoring function itself has failed' and the contrast are only implied; 'logged' is not stated.
-->
