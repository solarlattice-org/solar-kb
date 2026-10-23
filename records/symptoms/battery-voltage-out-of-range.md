---
id: symptom:battery-voltage-out-of-range
type: Symptom
name: Battery voltage out of range
aliases:
- VBATMAX
- VBATMIN
- BatVtgHi
- Battery fault
- Battery error
- Battery Meter Out of Bounds
claims:
- claim_id: c1
  rel: observed_as
  target: meas:battery-voltage-range-message
  note: Sunny Island battery inverters log a message when measured battery voltage leaves the permissible
    measuring range, either above (VBATMAX series) or below (VBATMIN series), naming the master or slave
    device at L1, L2 or L3.
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=67.r9
    h: f0217b51cdf2
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=67.r11
    h: 1f3270bf9cd8
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=67.r10
    h: d2d24614ae74
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=52.r3
    h: 9a869ab40b54
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=52
    h: 3bf2f8a287b7
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r1
    h: 02a0d3b727a9
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r7
    h: b38c59b91b2c
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r8
    h: 95997e8228ae
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:battery-voltage-above-charge-target
  note: 'BatVtgHi: battery voltage is above the target charge voltage; check the configuration of all
    DC sources.'
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=53.r2
    h: 61b5b848cc5a
  review: drafted
  review_note: 'support check: partial - BatVtgHi is stated as voltage higher than target charge voltage
    with DC source configuration check, but the passage is cut off and the ''all DC sources'' check is
    only partly shown (fine) — core supported though.'
- claim_id: c3
  rel: observed_as
  target: meas:battery-meter-out-of-bounds-flag
  note: 'Tesla controller boolean status point: set when battery meter voltage or frequency stays outside
    acceptable bounds; it leads to a Meter Invalid status.'
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=159
    h: 3663c40c0406
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=120.r11
    h: a459655b5a41
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=133.r4
    h: a459655b5a41
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=133
    h: 3de05079823f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: observed_as
  target: meas:battery-voltage-spread
  note: In a bank of batteries in the same condition, voltage differences over time or between positions
    point to performance problems. Readings must be corrected for voltage level, temperature, discharge
    rate and cell age.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h184
    h: 0ed4b3344ea0
  review: drafted
---
The battery inverter reports that measured battery voltage is outside its permissible measuring range, either too high or too low, and names the master or slave device on the affected line. If voltage is too low, the usable battery capacity may be too small, for example because the battery has aged. A heavy load switching on can then make the battery voltage collapse. For low voltage, disconnect the DC loads and charge the battery, make sure all battery cells work, and add load shedding if DC loads are installed. If voltage is too high or above the target charge voltage, check that all DC sources are correctly connected and configured and that the battery capacity is sufficient. On some storage controllers, a battery meter out-of-bounds flag shows meter voltage or frequency outside acceptable bounds, and this makes the meter reading invalid. To find weak cells, compare voltages across the battery bank over time, after correcting for temperature, discharge rate and age. Infrared imaging shows high-resistance cells and corroded terminals as hot spots.

<!-- review notes
- sentence 4: support check: partial - DC source connection/configuration checks and battery capacity sufficiency are stated, but capacity check is only for VBATMAX with a 65 V condition; BatVtgHi text is truncated.
- c5 dropped at review: The NREL passage ties hot IR cells to high internal resistance and loose or corroded connections, not to battery voltage being out of range, so the claimed link between symptom and observation is not in the source.
- sentence 4: review: partial - The DC-source connection and configuration checks are stated for over-range and BatVtgHi, but the passages tie the battery-capacity check to the VBATMAX rows when parameter 120.02 BatVtg is above 65.0 V, and the sentence drops that condition.
-->
