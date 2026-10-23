---
id: fm:current-sensor-fault
type: FailureMode
name: Current sensor fault
aliases:
- Leakage current sensor fault
- RCMU sensor faulty
- AC current sensor fault
- Arc detector current sensor defective
- DC Sensor- err
- Ground Fault Current Sensor Abnormal
claims:
- claim_id: c1
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r9
    h: 7c86a47ed822
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r11
    h: 92dfee4f30a5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r14
    h: 5570c77a0245
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=38.r3
    h: 179e16e05f1a
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=53.r7
    h: 28449a15fb93
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: affects
  target: comp:arc-fault-detector
  note: The current sensor of the arc detector is reported as defective.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r9
    h: 7c86a47ed822
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r11
    h: 92dfee4f30a5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: affects
  target: comp:residual-current-monitor
  note: The RCMU sensor is reported as faulty.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r33
    h: 3844599424a2
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r35
    h: 520bba37bd00
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: affects
  target: comp:ground-fault-detector
  note: The ground fault current sensor is reported as abnormal.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: presents_as
  target: symptom:inverter-shutdown
  note: The inverter disconnects from the grid or stops feeding current.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r9
    h: 7c86a47ed822
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r33
    h: 3844599424a2
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r11
    h: 92dfee4f30a5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r35
    h: 520bba37bd00
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: presents_as
  target: symptom:current-sensor-offset
  note: Reported as a failed current sensor offset calibration.
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=38.r3
    h: 179e16e05f1a
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:current-sensor-calibration-timeout
  note: Feed-in is briefly interrupted and the inverter goes back to the startup phase.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: detected_by
  target: method:inverter-display-check
  note: A leakage current sensor fault is shown on the LCD as Protect0100.
  cite:
  - src: src:chint-cps-275kw-800v-modbus-map-2026-01-28
    loc: tbl=53.r1
    h: 20878cf5cc23
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  rel: mitigated_by
  target: mit:inverter-restart
  note: Switch both the AC and DC switches off, wait 1 minute so stored energy can discharge, then switch
    them back on.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r6
    h: 3d032117a152
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  rel: mitigated_by
  target: mit:filter-board-replacement
  note: Applies when a restart does not clear the leakage current sensor fault.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c11
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Applies when a restart does not clear the fault.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r3
    h: 6c5eaca7f93c
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r6
    h: 3d032117a152
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:current-sensor-replacement
  note: The manufacturer provides instructions for replacing the AC current sensor.
  cite:
  - src: src:yaskawa-solectria-yaskawa-customer-facing-instructions-full
    loc: sec=h187
    h: bcb5d1bfef6f
  review: drafted
  review_note: 'support check: partial - u33 is only a fragment, ''for AC Current Sensor Replacement'',
    which suggests replacement instructions but doesn''t say the manufacturer provides them.; review:
    partial - The passage is only the fragment ''for AC Current Sensor Replacement'', which suggests replacement
    instructions exist but does not clearly say the manufacturer provides them.'
- claim_id: c13
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Applies when the code persists.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r9
    h: 7c86a47ed822
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=53.r7
    h: 28449a15fb93
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c14
  rel: mitigated_by
  target: mit:contact-installer
  note: Applies when the status code keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r33
    h: 3844599424a2
  review: drafted
---
A current sensor fault means the inverter has found one of its internal current sensors to be defective or abnormal. The sensor at fault may be an AC or DC current sensor, the sensor on the arc detector, the RCMU sensor, or the sensor that measures leakage or ground fault current. The inverter usually disconnects from the grid or stops feeding current into it. A related fault code reports a failed sensor offset calibration or a calibration timeout, which briefly interrupts feed-in. To confirm the fault, read the fault code on the inverter display, for example Protect0100 for a leakage current sensor fault. First restart the inverter: switch both the AC and DC switches off, wait one minute for stored energy to discharge, then switch them back on. If the fault does not clear, replace the filter board, the current sensor or the whole inverter, depending on the model's instructions. If the code keeps returning, contact the installer or the manufacturer's service team.

<!-- review notes
- sentence 7: support check: partial - Filter board and inverter replacement are stated, and u33 only hints at current sensor replacement, so 'depending on the model's instructions' isn't established.
- sentence 4: review: partial - Both calibration codes are cited, but only the timeout code (314) says feed-in is briefly interrupted; the Yaskawa offset-calibration row gives no behavior.
- sentence 7: review: partial - The rows support replacing the filter board or the inverter, but current sensor replacement rests only on a bare heading fragment, and 'depending on the model's instructions' is inferred.
-->
