---
id: fm:relay-failure
type: FailureMode
name: Relay failure
aliases:
- Grid relay fault
- Grid relay error
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  note: The grid relay is inside the inverter. If the fault does not clear, the whole inverter is replaced.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=35.r6
    h: 758dbe74639d
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=40.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=64.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=59.r6
    h: 758dbe74639d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passages say to replace the inverter if the fault doesn''t clear,
    but never state the grid relay is inside the inverter or that the whole unit is replaced because of
    that (it is implied only by the inverter-level codes).'
- claim_id: c2
  rel: presents_as
  target: symptom:internal-device-fault
  note: 'Logged as a Fault-type event: Fault0100, grid relay fault.'
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=40.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=64.r5
    h: 647e672a17f1
  review: drafted
  review_note: 'support check: partial - Fault0100 is listed as Type: Fault for the grid relay fault,
    but the passages do not say it presents as an ''internal device fault'' symptom.'
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  note: Turn both the AC and DC switches off and wait for stored energy to discharge before switching
    back on. The manual gives 1 minute for Protect0020 and 5 minutes for Fault0100.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=35.r6
    h: 758dbe74639d
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=40.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=64.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=59.r6
    h: 758dbe74639d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Needed when a restart does not clear the grid relay fault or error.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=35.r6
    h: 758dbe74639d
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=40.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=64.r5
    h: 647e672a17f1
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=59.r6
    h: 758dbe74639d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
A relay failure means the inverter's grid relay is not working properly, and the inverter reports it as an error or a fault. It can also show up as fault code Fault0100, grid relay fault. For Protect0020, turn both the AC and DC switches off, wait 1 minute for the energy to discharge, then turn both switches back on. For Fault0100, use the same restart but wait 5 minutes before turning the switches back on. If the restart does not clear the fault, replace the inverter.
