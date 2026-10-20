---
id: fm:temperature-sensor-fault
type: FailureMode
name: Temperature sensor fault
aliases:
- TempSensorErr
- Warn0050
claims:
- claim_id: c1
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37.r2
    h: dc4f47acbe5f
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r2
    h: b4e0065cf5c2
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37
    h: 05f56b96dbac
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: affects
  target: comp:inverter
  note: The sensor involved is the inverter's internal temperature sensor.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - u16 mentions an internal temperature sensor with poor contact,
    but the passage doesn''t state the fault affects the inverter beyond raising an alarm.'
- claim_id: c3
  rel: caused_by
  target: stressor:poor-connector-contact
  note: Poor contact at the temperature sensor's socket connector.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37.r2
    h: dc4f47acbe5f
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r2
    h: b4e0065cf5c2
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37
    h: 05f56b96dbac
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: presents_as
  target: symptom:abnormal-temperature-reading
  note: Flagged as the TempSensorErr alarm. One manual lists a sensor reading of -25C as a possible cause.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r1
    h: 66f8fb7f8d7e
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r2
    h: b4e0065cf5c2
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37.r1
    h: 399835b0ff90
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37
    h: 05f56b96dbac
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:inverter-display-check
  note: Check the temperature value shown on the inverter display.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=32.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=56.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3
    h: a2000b30847e
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37
    h: 05f56b96dbac
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  note: Turn the external AC disconnect (or the working power supply) off and back on to reboot the system.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=32.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r1
    h: 66f8fb7f8d7e
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=56.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3
    h: a2000b30847e
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37
    h: 05f56b96dbac
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r1
    h: ff301fa218bd
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Use this step if a reboot does not clear the alarm.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=32.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=56.r1
    h: a1c35c144b4e
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3
    h: a2000b30847e
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37
    h: 05f56b96dbac
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=17.r2
    h: '498497530e79'
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The inverter raises a TempSensorErr alarm, also listed as Warn0050, when it detects an abnormal temperature reading. The usual causes are poor contact at the temperature sensor's socket connector or a damaged sensor. One manual also lists a sensor reading of -25C as a possible cause. To confirm it, look at the temperature value on the inverter display and check whether it makes sense. Turn the external AC disconnect off and back on to reboot the inverter, and see whether the alarm clears. If the alarm stays after the reboot, contact the manufacturer's service team.

<!-- review notes
- sentence 4: support check: partial - Passages say observe/verify the temperature display, but not explicitly to check whether it makes sense.
- sentence 5: support check: partial - Reboot via external AC disconnect is stated, but 'see whether the alarm clears' is only implied by the later contact-if-not-corrected step.
-->
