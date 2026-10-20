---
id: method:spd-alarm-contact-monitoring
type: DetectionMethod
name: SPD alarm contact monitoring
aliases:
- form C relay contact
claims:
- claim_id: c1
  rel: produces
  target: meas:spd-alarm-status-active
  note: The SPD status menu shows the alarm as either 'Protected' or 'Active Alarm Replace SPD'. On the
    Power Xpert SPD, the alarm status is also available as a readable register that indicates protection
    status.
  cite:
  - src: src:eaton-eaton-spd
    loc: sec=4.1.1
    h: f78545235f4a
  - src: src:eaton-eaton-spd
    loc: tbl=16.r17
    h: d7bbaba2d6d8
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:spd-red-status-led
  note: When a phase or neutral-ground green LED turns off and the red LED comes on, usually with the
    audible alarm, the troubleshooting tables point to a significant surge event or lost protection. The
    listed action is to replace the SPD.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:eaton-eaton-spd
    loc: tbl=8.r3
    h: 6ac33fcf20dc
  - src: src:eaton-eaton-spd
    loc: tbl=7.r7
    h: '019039e56176'
  - src: src:eaton-eaton-spd
    loc: tbl=8
    h: ae87417107b0
  review: drafted
- claim_id: c3
  rel: produces
  target: meas:inverter-fault-code-display
  note: 'In the CPS inverter, an SPD alarm appears as Warn0100 (AC SPD). The technician then checks the
    SPD indicator: red means replace the module, green means reseat it.'
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=32
    h: a2000b30847e
  review: drafted
  review_note: 'support check: partial - Warn0100 (AC SPD) and red/green indicator actions are stated,
    but the passage refers to a DC SPD check and does not link it to alarm contact monitoring.'
---
Some surge protection devices have a form C relay contact that reports SPD status remotely, so a monitoring system can see whether the device is still protecting. The contact wires connect through a three-terminal connector. In normal operation the audible alarm is off and the normally closed contact stays closed. Apart from this remote status signal, the device needs no operator action other than watching its display panel for status. On some models you can read the alarm status from the display or over communications. It shows either Protected or Active Alarm Replace SPD, and the display also shows how much protection remains on each phase. A red phase or neutral-ground LED, often with the audible alarm, means a significant surge event or lost protection, which indicates an exhausted surge protector that should be replaced. If every phase alarms at once, the cause can also be an extended temporary overvoltage or an SPD rated below the system voltage, so check the electrical system before fitting a replacement. If the alarm has been silenced, a red LED can still show a fault. If all LEDs and the display are off, the SPD may simply have no power, so check the system voltage at its connection. Some inverters raise their own SPD warning. For this alarm, a red indicator means replace the SPD module, and a green indicator means remove and reinstall it in its socket.

<!-- review notes
- sentence 4: support check: partial - The display menu shows the Protected/Active Alarm states and per-phase protection level, but the register passage does not list those values, and 'some models' is not stated.
- sentence 8: support check: partial - Red means replace and green means remove and reinstall in the socket, but the passage says 'DC' SPD under Warn0100 (AC SPD) and does not say 'some inverters' generally.
-->
