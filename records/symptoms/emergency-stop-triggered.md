---
id: symptom:emergency-stop-triggered
type: Symptom
name: Emergency stop triggered
aliases:
- EmergencyStp
- E-Stop
- Fast stop
- emergent stop
claims:
- claim_id: c1
  rel: observed_as
  target: meas:estop-relay-lights-off
  note: Both signal lights of the emergency switch relay are lit in normal operation and switch to OFF
    when the emergency switch is activated.
  cite:
  - src: src:sma-sc-wa-en-31
    loc: sec=h77
    h: db5684d202c6
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:zero-ac-output
  note: The DC load switches and AC circuit breakers open and the inverter units disconnect from the grid.
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: sec=h204
    h: 4b5ad8ff436d
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=12.r2
    h: 680f73d02694
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: sec=10.12
    h: 33c2c840df3c
  - src: src:sungrow-sungrow-sg3150ud-mv-us-sg4400ud-mv-us-user-manual-ver23
    loc: sec=9.2
    h: 941dde951fd6
  review: drafted
  review_note: 'support check: partial - Passages say DC switches and AC breakers trip and units disconnect
    from the grid, but nothing states AC power/current readings drop to zero.'
---
An emergency stop puts the inverter into a stopped state. The DC load switches and AC circuit breakers open, and the inverter units disconnect from the grid. The usual cause is that someone pressed an emergency stop button. The CPS manual also lists an internal inverter fault as a possible cause. Check every emergency stop button first, on the cabinet, in the stations and any external switches. If one is pressed, release it. Some buttons stay locked and need a key to release. On Sunny Central units, the emergency switch relay has two signal lights that stay lit in normal operation and switch off when the stop is activated. In a team configuration the relay has to switch in every cabinet. To restart, release the button, switch the DC load switches back on, acknowledge the error where needed, and follow the normal start process. If the stop keeps coming back after the button has been released, contact the manufacturer's service center, because an internal fault may be the cause.

<!-- review notes
- sentence 2: support check: partial - Both causes are listed, but 'usual cause' ordering/frequency is not stated, only that button pressed is listed first.
- sentence 3: support check: partial - Check/restore button and key-release lock are stated, but checking cabinet, stations and external switches comes from a functional-test passage, and 'first' is only loosely implied.
- sentence 6: support check: partial - The manual says contact service if the problem persists and lists internal fault as a cause, but recurrence after release is only implied.
-->
