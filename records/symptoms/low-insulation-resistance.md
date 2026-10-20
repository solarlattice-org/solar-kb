---
id: symptom:low-insulation-resistance
type: Symptom
name: Low insulation resistance
aliases:
- IsolationErr
- Insulation resistance low
- low insulation fault
- isolation fault
- PV ISO-PRO
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-insulation-resistance-alarm
  note: Inverters report it as an isolation or ground-protection alarm when PV positive or negative to
    ground resistance is out of range. The inverter may switch off, often after rain or when modules are
    wet with morning dew.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=37.r1
    h: 616d37333b43
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=61.r1
    h: 616d37333b43
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=41.r8
    h: c4ccc7f4e8ae
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=36.r3
    h: 3b5bf80701b2
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r1
    h: 6d164bcc8c14
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=21.r1
    h: 1cbe041ab521
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=40.r1
    h: cc361fe4da0b
  review: drafted
  review_note: 'support check: partial - Passages support the isolation alarm, out-of-range resistance,
    and rain/dew switch-off, but nothing says AC power (W) falls to zero during the trip.'
---
The inverter raises an insulation alarm, such as IsolationErr, when the resistance from PV positive or PV negative to ground is outside the allowed range. It often shows up after rain or early in the morning when modules are wet with dew, and the inverter may switch off until the resistance recovers. Possible causes include module insulation failure, which you usually cannot see by eye, and damaged insulation on cables or connectors. To find the faulty string, isolate all strings at the fuse holders, then reconnect them one at a time and restart the inverter each time until the alarm returns. Then trace that string for any leakage to earth. Measure the insulation resistance of the string and its DC cables. If the reading is normal, repeat it in the same weather as when the alarm occurred. Also check that the inverter's insulation protection setting is not set too high and that it meets local rules. Treat the array as a shock hazard: an insulation fault can put dangerous voltage on conductive parts, and damaged cables can cause arcs and fire.

<!-- review notes
- sentence 2: support check: partial - After-rain and early-morning dew occurrence and inverter switching off are stated, but not that it stays off until resistance recovers (only 'wait for inverter to return to normal' in one row).
-->
