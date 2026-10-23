---
id: symptom:high-battery-temperature
type: Symptom
name: High battery temperature
aliases:
- Battery overtemperature
- BatTmpHiWarn
- BatTmpHi
- Battery temperature high
- Battery temperature too high
- Overtemperature fault in battery
claims:
- claim_id: c1
  rel: observed_as
  target: meas:battery-overtemperature-message
  note: Sunny Island shows W212 (BatTmpHiWarn) as a warning, W939/W941 as SiCom warnings, and F923/F925
    as level-3 SiCom errors (overtemperature, or overtemperature in charge mode). Event 9314 is the matching
    event number.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r10
    h: a344b97f0e70
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r8
    h: 77807e4cd828
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r5
    h: 38660ed0c7e2
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r6
    h: bf8df6cc3b95
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r7
    h: ac7237545e71
  - src: src:sma-kb-event-9314-or-w212-on-sunny-island-or-sunny-backup
    loc: sec=h1
    h: 6ccc03e38aec
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: sec=h95
    h: 78f493bfce00
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=53.r6
    h: 853ace770d3b
  - src: src:sma-kb-event-9314
    loc: sec=h1
    h: ef9bfbf8c5eb
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:battery-temperature-status-high
  note: The battery temperature symbol on the display goes from normal to high, meaning a critical range
    where battery function may be impaired. It then goes to too high, meaning the maximum was exceeded
    and the battery was shut down.
  cite:
  - src: src:sma-doc-279088
    loc: tbl=15.r2
    h: e6f8c4e927cd
  - src: src:sma-doc-279088
    loc: tbl=15.r3
    h: 79d3bc9c7302
  - src: src:sma-doc-279088
    loc: tbl=15
    h: d520339f6a3b
  review: drafted
---
The Sunny Island battery inverter watches battery temperature all the time through its battery temperature sensor. It flags high battery temperature with codes such as W212, W939, W941, F923 and F925, or with event 9314. A warning appears when the battery is within 5°C of the maximum permissible temperature. If the maximum is exceeded, the Sunny Island switches off and restarts once the battery has cooled to a set start temperature. On the display, the battery temperature symbol changes from normal to high and then to too high. Too high means the battery has been shut down. The usual cause is an ambient temperature outside the battery manufacturer's limits. A high ambient temperature can also reduce the battery's charging power. A faulty temperature sensor can give a false reading. Check that the sensor reads roughly 2000 Ω at 20°C to 25°C, and replace it if the value is far off. In a cluster, only the master measures battery temperature, so the sensor must be connected to the master. If the sensor is missing or defective, the unit assumes a fixed temperature, which can lead to deep discharge over time. First, let the battery cool down and check its ventilation and surroundings. Keeping the battery below 25°C helps prevent early aging.

<!-- review notes
- sentence 4: support check: partial - The passages say the manufacturer's ambient conditions must be met and that a high ambient temperature may limit charging, but they don't call ambient temperature the usual cause of the fault. The charging remark is also about a different question.
- sentence 7: support check: partial - Waiting for the battery to cool and keeping it below 25°C to prevent premature aging are stated. Checking ventilation and surroundings is not stated, though the manufacturer's ambient conditions are mentioned elsewhere.
- sentence 4: review: partial - The passages tell the user to make sure the manufacturer's ambient conditions are met and say high ambient temperature may limit charging power, but nowhere call ambient temperature the usual cause.
- sentence 7: review: partial - Waiting for the battery to cool and protecting it above 25°C to prevent premature aging are stated, but checking ventilation and surroundings is not.
-->
