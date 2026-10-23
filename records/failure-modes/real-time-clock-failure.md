---
id: fm:real-time-clock-failure
type: FailureMode
name: Real-time clock failure
claims:
- claim_id: c1
  rel: affects
  target: comp:real-time-clock
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r15
    h: '761e75330970'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r24
    h: 5ab079e92f2b
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r15
    h: '761e75330970'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r13
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r13
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r20
    h: 2ee634d10a9c
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:inverter-shutdown
  note: With a hardware error in the clock module, the inverter shows an error and stops feeding current
    into the grid.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:inaccurate-clock-time
  note: When the clock module runs in emergency mode, the time is inaccurate but grid feed-in continues
    as normal.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r15
    h: '761e75330970'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r24
    h: 5ab079e92f2b
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r15
    h: '761e75330970'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  - src: src:eaton-eaton-spd
    loc: tbl=9.r7
    h: a4d4792734d8
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:clock-time-lost
  note: Emergency mode of the clock module may lose the time.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r15
    h: '761e75330970'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r24
    h: 5ab079e92f2b
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r15
    h: '761e75330970'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:internal-communication-failure
  note: Reported as a communication error with the real-time clock module.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r13
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r13
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r20
    h: 2ee634d10a9c
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:inverter-display-check
  note: The inverter display shows an error message for the clock module hardware error.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:extended-power-loss
  note: In one device, the supercapacitor that backs up the clock drained during an extended power loss,
    leaving time stamps inaccurate.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=9.r7
    h: a4d4792734d8
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:clock-reset
  note: Reset the time and date when the clock module is in emergency mode or time stamps are wrong.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r24
    h: 5ab079e92f2b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  - src: src:eaton-eaton-spd
    loc: tbl=9.r7
    h: a4d4792734d8
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:ntp-configuration-check
  note: Using the SNTP feature keeps time stamps accurate.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=9.r7
    h: a4d4792734d8
  review: drafted
  review_note: 'support check: partial - SNTP use to keep time stamps accurate is stated, but it is not
    a ''configuration check'' per se; mostly matches though.'
- claim_id: c10
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Call a trained service technician if the hardware error persists, or when the clock has not initialized.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r4
    h: d440ab114d46
  review: drafted
---
A real-time clock failure is a fault in the inverter's internal clock module, the part that keeps time and date. If the clock module has a hardware error, the display shows an error message and the inverter stops feeding current into the grid. If the clock module is in emergency mode, the time can drift or be lost, but the inverter keeps feeding the grid normally. Some inverters also report a communication error with the clock module. Wrong time stamps can also follow a long power outage that drains the clock's backup supply, or a clock that has not been synchronized. For time problems, reset the time and date on the inverter, and use network time sync where it is available to keep the clock accurate. If the hardware error stays active or the clock does not initialize, call a manufacturer-trained service technician.
