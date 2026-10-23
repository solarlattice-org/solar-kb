---
id: symptom:hardware-incompatibility
type: Symptom
name: Hardware component incompatibility
aliases:
- Function incompatibility
- Compatibility error
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'Fronius inverters report it as a function incompatibility status code: one or more PC boards
    in the inverter do not match each other, for example after a board replacement. On some codes it appears
    only as a warning on the display.'
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r5
    h: aa4212975d39
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r14
    h: 15a8391e4e16
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r16
    h: 2711211cbc24
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r37
    h: 66d84777993b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r15
    h: fab751f5425a
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r17
    h: 99124dc8e3e3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:zero-ac-output
  note: With some incompatibility codes the inverter stops feeding current into the grid. With others
    it tries to reconnect by itself.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r37
    h: 66d84777993b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r19
    h: f3e2b584d37a
  review: drafted
  review_note: 'support check: partial - Codes 480/481 and 445 stop feed-in and 436/438 retry, but the
    passages don''t state AC power or current stays at zero as specific signal patterns.'
---
Hardware incompatibility shows up as an inverter status code saying that one or more PC boards inside the inverter do not work with each other. It is typically seen after a board has been replaced. How the inverter responds depends on the code. With codes 436 and 438 it retries and resumes feeding the grid if it can. With codes 480 and 481 it stops feeding current. Codes 558 and 559 only put a warning on the display. In monitoring data, a stopping code shows as zero AC output even though there is sun. A warning-only code may cause error displays or malfunctions without stopping production. On some units the same compatibility code can instead point to an invalid power module configuration. Check whether boards or modules were recently swapped. First, update the inverter firmware. If the code persists or keeps coming back, contact the system installer or a Fronius-trained service technician. Firmware updates can fix software-related inverter faults. If a restart does not help or the fault keeps returning, a service team usually has to find the origin.

<!-- review notes
- sentence 3: support check: partial - No feed-in for stopping codes is stated, and 558 mentions possible error displays or malfunctions, but 'zero AC output even though there is sun' and 'without stopping production' are not stated.
- sentence 4: support check: partial - Code 445 lists compatibility error and invalid power module configuration, but 'on some units the same code' and the advice to check recent swaps are not stated.
- sentence 5: support check: partial - Firmware update then contact a technician appears for 436/480, but 558 evidence only says contact the system installer without a firmware step.
-->
