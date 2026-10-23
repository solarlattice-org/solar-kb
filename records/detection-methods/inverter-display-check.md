---
id: method:inverter-display-check
type: DetectionMethod
name: Inverter display check
claims:
- claim_id: c1
  rel: produces
  target: meas:inverter-fault-code-display
  note: In fault mode the LCD shows the most recent or current fault. Fault codes can also be read from
    the monitoring data log.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=34.r1
    h: 20455651a3a5
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=h77
    h: 2f19f3801ca4
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: produces
  target: meas:arc-board-error-message
  note: If the arc detection board fails, the LCD shows 'arc board err' and the inverter stays off the
    grid until the board is working again.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.4
    h: 50f6c0ff2497
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.4
    h: f90171d02e8b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: produces
  target: meas:arc-fault-alarm
  note: The arc fault stays latched and must be cleared by hand from the menu.
  quote: If an arc fault occurs "Arc Fault Detected!" will be displayed.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.4
    h: 50f6c0ff2497
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.4
    h: f90171d02e8b
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h120
    h: 96e96d3db561
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: produces
  target: meas:implausible-sensor-temperature
  note: For TempSensorErr the manuals say to read the temperature on the display first. One manual lists
    a sensor reading of -25C as a possible cause.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37
    h: 05f56b96dbac
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r2
    h: b4e0065cf5c2
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33
    h: 0eda47f20f8e
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17
    h: a32358438a00
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The passages support reading the display for TempSensorErr and
    the -25C cause, but they don''t mention a constant low reading pinned at a sensor floor for the signal.'
- claim_id: c5
  rel: produces
  target: meas:fan-fail-message
  note: The LCD shows a Fan Fail warning when the fan is not working properly.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=7.2
    h: 08034ea4d7bf
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: produces
  target: meas:grid-frequency-reading-out-of-limit
  note: Check the measured frequency on the LCD. If it is within limits, restart the inverter.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=46
    h: 7eec2ba102e5
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: produces
  target: meas:grid-voltage-reading-out-of-limit
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=46
    h: 7eec2ba102e5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The inverter display check means reading the fault codes, status messages and live measurements on the inverter LCD or in its menus. It helps you work out why the inverter has stopped or raised an alarm. When the inverter is in fault mode, the screen shows the most recent or current fault. The same codes can often be found in the data log of the monitoring system. An arc detection board failure appears as an arc board error, and the inverter will not reconnect to the grid until the board is working again. A real arc fault shows as a separate alarm that must be cleared by hand from the menu. For a temperature sensor fault, first read the temperature on the display. An implausible value, such as a sensor reading of -25C, points to a poorly connected or damaged sensor. A fan that is not working properly triggers a Fan Fail warning on the LCD. Internal power stage or other internal faults appear as internal fault or protection codes. Display readings of grid voltage, grid frequency and PV voltage should be checked against a meter reading, because the measurement circuit itself may be faulty. The display only points to a likely cause. Before touching the fan or other internal parts, switch off at the LCD, disconnect AC and DC, and wait for the stored energy to discharge.

<!-- review notes
- sentence 1: support check: partial - The passages support fault codes and live measurements shown on the display for diagnosing, but 'status messages' and 'menus' as a defined check are only loosely covered.
- sentence 3: support check: partial - The arc board error and not reconnecting until the board is OK are stated, and the arc fault is cleared manually, but 'a separate alarm' is not explicit (the arc fault is shown on the LCD, as 'Arc Fault Detected!' in u11).
- sentence 4: support check: partial - Reading the display first and -25C as a possible cause alongside poor contact or a damaged sensor is stated, but nothing calls -25C an implausible value that points to those causes.
- sentence 6: support check: partial - The passages say to compare the display with measured AC or DC voltage and note a possible bad measurement circuit for some grid voltage cases, but they don't cover frequency or PV voltage across the board as a general rule.
- sentence 7: support check: partial - u21 gives the switch-off, disconnect AC and DC, and wait 15 minutes steps for fan work, but the claim that the display only points to a likely cause isn't stated, and the 'stored energy' wording only appears in u2.
- sentence 1: review: partial - The passages support fault codes, operating-mode screens and live PV/grid measurements on the LCD for diagnosing a non-working inverter, but 'menus' and diagnosing a 'raised alarm' are not stated.
- sentence 4: review: partial - Observing the temperature display first and the poor-contact/damaged-sensor causes are supported, but the passages list a -25C reading as a separate possible cause rather than an implausible value that points to poor contact or damage.
- sentence 7: review: partial - For fan work the passages give switching off at the LCD, disconnecting AC and DC and waiting 15 minutes (and energy discharge appears for a restart), but 'the display only points to a likely cause' and extending this to other…
-->
