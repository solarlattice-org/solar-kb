---
id: method:fan-function-check
type: DetectionMethod
name: Fan function check
aliases:
- Fan test
- FanTst
claims:
- claim_id: c1
  rel: produces
  target: meas:fan-fail-message
  note: The check includes looking for a fan alarm or warning in the app or on the LCD. On the Conext
    CL125, a fan event bit of 1 means an event was detected and 0 means the fan is healthy.
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r1
    h: fb5c20da466e
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r1
    h: fb5c20da466e
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=56.r2
    h: 3801937c2610
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=37.r2
    h: 4216ca4152cf
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=37.r2
    h: 4216ca4152cf
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=42.r2
    h: 3801937c2610
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: sec=h209
    h: b97079dca965
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: sec=h52
    h: eaf382949197
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:fan-abnormal-noise
  note: Listen for unusual noise while the fan runs or during a fan test triggered by a parameter.
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=59.r2
    h: 8f01a62bad52
  - src: src:sungrow-sungrow-sg3150ud-mv-us-sg4400ud-mv-us-user-manual-ver23
    loc: tbl=56.r3
    h: 14025d468fe0
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=56.r2
    h: 3801937c2610
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=37.r2
    h: 4216ca4152cf
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=37.r2
    h: 4216ca4152cf
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h205
    h: 62645edcd77e
  review: drafted
- claim_id: c3
  rel: produces
  target: meas:no-fan-airflow
  note: During the fan test, air should be drawn in at the bottom and leave through the upper ventilation
    grids. No airflow suggests the fans were installed improperly.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h205
    h: 62645edcd77e
  review: drafted
---
A fan function check confirms that the inverter cooling fans run properly. It is used when the inverter reports a fan alarm, an over-temperature event, or derating caused by overheating. Look for a fan alarm in the app or on the display. Check that the fans turn freely and are not blocked by debris, and listen for abnormal noise. Some manufacturers schedule this check once a year. Many inverters can start a fan test from a menu or parameter. You then confirm by sound and feel that the fan runs and that air is drawn in at the bottom and leaves through the upper grids. On some inverters, the display does not report whether the fan is good. Only listening and feeling can confirm that it works. If the fans do not start, measure the voltage at the fan connector. Replace the fans if voltage is present. If there is no voltage, isolate the inverter at once and inspect it for damage, debris or burnt smells. The check detects fan failure, which can lead to inverter overheating and lower operating efficiency. Before replacing a fan, shut down and disconnect the inverter. If the fans work, also check the cause of the heat: the installation clearances, direct sunlight, ventilation and the condition of the air ducts.

<!-- review notes
- sentence 2: support check: partial - App/LCD alarm check, abnormal noise, yearly period and blockage by debris are stated, but 'turn freely' is only approximated by 'rotates smoothly' and the blockage check is in the alarm row rather than the same routine.
- sentence 3: support check: partial - Parameter/menu-started fan tests and checking airflow in at bottom and out of upper grids are stated, but 'sound and feel' is stated only for the display-menu case and 'many inverters' is a generalization.
- sentence 6: support check: partial - Fan failure causing reduced cooling/efficiency and shutting down and disconnecting before replacement are stated, but overheating is only implied ('may not be cooled down') and the check 'detects' failure is loosely supported.
-->
