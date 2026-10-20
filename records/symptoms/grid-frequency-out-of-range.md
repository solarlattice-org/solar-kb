---
id: symptom:grid-frequency-out-of-range
type: Symptom
name: Grid frequency out of range
aliases:
- GridF.OutLim
- Grid incident
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grid-frequency-reading-out-of-limit
  note: The CPS manuals say to compare the frequency shown on the inverter LCD with the limits. Solis
    notes that a bad LCD reading can come from a faulty measurement circuit, so check it against a test-point
    measurement.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=35.r5
    h: 37a70970837e
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=59.r5
    h: 37a70970837e
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r4
    h: 63914b12252c
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=40
    h: 5fe6e4e2d7ff
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:zero-power-at-irradiance
  note: The inverter disconnects or cannot connect to the grid while frequency is out of range. The same
    alarm can also be raised when no grid is detected.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h162
    h: bd3d762be238
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=49.r1
    h: 3f4642d9acdb
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=35.r2
    h: 2814ecbc7c19
  review: drafted
---
The inverter has found that the grid frequency is outside its allowed protection range, or it cannot detect the grid at all, so it trips off the grid. In the data, AC output stops and the measured grid frequency sits above the upper limit or below the lower limit. On CPS units at their IEEE1547-2018 defaults, the level 1 limits are 61.2 Hz on the high side and 58.5 Hz on the low side. The usual causes are a real frequency problem on the utility grid or a poor or loose AC connection between the inverter and the grid. First, watch the inverter for about 10 minutes to see if the alarm clears by itself. Inverters normally reconnect once the grid is back to normal. Next, read the measured frequency on the LCD. If it is within the limits, restart the inverter. If not, check that the AC wiring and the cable to the grid are secure and not damaged. If the actual grid frequency is outside the set range, contact the local utility. Also check that the frequency protection settings are set correctly. If an independent measurement shows a normal frequency but the inverter still reports it out of range, the inverter's measurement circuit may be faulty. Contact manufacturer service if the alarm keeps coming back.

<!-- review notes
- sentence 1: support check: partial - Definition (frequency abnormal or grid not detected) and disconnection are stated, but 'allowed protection range' and 'trips' classification are only implied.
- sentence 5: support check: partial - LCD check and restart if within limit are stated, but the 'if not, check AC wiring' branching and cable damage check are only loosely supported since sources list wiring checks as separate steps.
- sentence 7: support check: partial - Bad measurement circuit via LCD check is stated and contacting service if unresolved appears, but 'independent measurement normal yet reports out of range' and 'keeps coming back' are not exactly stated.
-->
