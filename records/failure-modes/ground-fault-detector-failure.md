---
id: fm:ground-fault-detector-failure
type: FailureMode
name: Ground fault detector failure
aliases:
- Leakage current sensor fault
- sensor fault of leakage current
- GFCI sensor abnormal
- GFCI sensor abnormality
- Ground Fault Current Sensor Abnormal
claims:
- claim_id: c1
  rel: affects
  target: comp:ground-fault-detector
  note: The fault is in the leakage current (GFCI) sensor of the inverter's ground fault detection circuit.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-200-250kw-k-t-modbus-map-2026-01-30
    loc: tbl=42.r25
    h: 9af6f5661234
  - src: src:chint-cps-sca100k-t-sca50k-t-modbus-map-2026-02-05
    loc: tbl=48.r9
    h: c39682b30c21
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  - src: src:chint-cps-275kw-800v-modbus-map-2026-01-28
    loc: tbl=53.r1
    h: 20878cf5cc23
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:filter-board
  note: CPS manuals name the filter board as a replacement part for this fault, so the sensor may sit
    on it.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:internal-device-fault
  note: The inverter reports it as protection code Protect0100 (leakage current sensor fault) or Protect0310
    (GFCI sensor abnormal), depending on the model.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-200-250kw-k-t-modbus-map-2026-01-30
    loc: tbl=42.r25
    h: 9af6f5661234
  - src: src:chint-cps-sca100k-t-sca50k-t-modbus-map-2026-02-05
    loc: tbl=48.r9
    h: c39682b30c21
  - src: src:chint-cps-275kw-800v-modbus-map-2026-01-28
    loc: tbl=53.r1
    h: 20878cf5cc23
  review: drafted
  review_note: 'support check: partial - Codes Protect0100/Protect0310 are stated, but ''depending on
    the model'' and the classification as an internal device fault are not explicit.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  note: Turn both AC and DC switches off, wait one minute for the energy to discharge, then turn them
    back on.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:filter-board-replacement
  note: Do this if a restart does not clear the fault.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Do this if a restart does not clear the fault.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r6
    h: 3e8e43bfd3f4
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=33.r1
    h: 62a7b29ff982
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r6
    h: a24a0da56dc8
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Contact after-sales or CPS service if the fault stays after a restart.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r5
    h: fe0ca2913a14
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r2
    h: ae5777d7a0a3
  review: drafted
---
The inverter has a residual current circuit, required by UL 1741, that detects leakage from ground faults in the PV array, raises an alarm and stops the inverter. This failure mode means the leakage current (GFCI) sensor in that circuit has failed. It does not mean there is a ground fault in the array. Depending on the model, the inverter shows protection code Protect0100 or Protect0310. You can see the code on the inverter display. It is also flagged in the Modbus fault register. First, turn both the AC and DC switches off, wait one minute for the energy to discharge, and turn them back on. If the fault does not clear, contact the manufacturer's service team to replace the filter board or the whole inverter.

<!-- review notes
- sentence 1: support check: partial - UL1741 residual current detection, alarm and ceasing operation are stated, but only in some passages and with a leakage threshold condition in others.
- sentence 2: support check: partial - Passages say sensor abnormal/fault, but nowhere state that it does not indicate an array ground fault.
- sentence 3: support check: partial - Both codes appear for the sensor fault, but the passages do not tie them to model differences.
- sentence 4: support check: partial - The Modbus register bit and LCD display are shown, but the LCD display appears only for Protect0100, and the register is a fault register with Fault1 storage.
-->
