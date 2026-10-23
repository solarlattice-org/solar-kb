---
id: symptom:switch-status-fault
type: Symptom
name: Switching device status fault
aliases:
- Grid relay stuck
- Grid voltage relay error
- Faulty switching status
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-output
  note: With status code 457 (grid relay stuck or grid voltage relay error), the inverter stops feeding
    current into the grid.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r27
    h: a766ac648434
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r14
    h: ce38d6e2d197
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Central inverter error numbers report a faulty switching status for the DC switchgear (7704),
    the AC disconnection unit (7707) or the remote GFDI (7708).
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r18
    h: ead458af300d
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r15
    h: 6ba85e02f613
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r17
    h: a92baad361c0
  review: drafted
---
This symptom means the inverter reports that a switching device, such as a grid relay, DC switchgear, AC disconnection unit or remote GFDI, is not in the expected switching state. On string inverters it appears as a stuck grid relay or a grid voltage relay error, and the inverter stops feeding current into the grid, so AC output drops to zero. For a relay fault, check the AC cable first; if the code stays, a trained service technician is needed, which points to a relay failure inside the unit. On central inverters, a faulty DC switchgear status can show up just after a grid outage or early in the morning at start-up, and the DC switch may also fail to operate. For the DC switchgear fault, first look for mechanical problems, abnormal noise, burn marks or smoke, then check whether the switch spring is charged. If charging the spring by hand clears the error, the spring charging motor is faulty. A broken or damaged DC switch spindle means the switch must be replaced, and loose cables or connectors near the DC switch should be checked and tightened. When disconnecting the inverter, confirm that all motor-driven circuit breakers are in the OFF position. For AC disconnection unit or remote GFDI status faults, contact the manufacturer service line.

<!-- review notes
- sentence 2: support check: partial - Stuck grid relay/grid voltage relay error and no current feed-in are stated, but 'string inverters' (Fronius) and AC output dropping to zero are only implied.
- sentence 3: support check: partial - Check AC cable (for voltage relay error) and service technician (for stuck relay) are stated, but not as a sequence, and the relay failure inside the unit is an inference.
-->
