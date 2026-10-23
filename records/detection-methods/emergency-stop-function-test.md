---
id: method:emergency-stop-function-test
type: DetectionMethod
name: Emergency stop functional test
claims:
- claim_id: c1
  rel: produces
  target: meas:estop-relay-lights-off
  note: In normal operation both signal lights of the emergency switch relay are lit. When a switch is
    pressed during the test, the relay indicator lights should change to OFF.
  cite:
  - src: src:sma-sc-wa-en-31
    loc: sec=h77
    h: db5684d202c6
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:inverter-fault-code-display
  note: On the Sunny Central, activating the emergency switch should bring up error 206 on the controller.
    The error must be acknowledged manually.
  cite:
  - src: src:sma-sc-wa-en-31
    loc: sec=h77
    h: db5684d202c6
  review: drafted
---
The emergency stop functional test checks each emergency switch in turn: the ones on the cabinet, the ones in the stations and any external emergency stop switches. Before testing, set the inverter to Stop, open the doors, and make sure control voltage is present. Also check that the external emergency stop is not activated, and tape the door contact switches in the On position. In normal operation both relay signal lights are on. When a switch is pressed, the relay lights should change to OFF and the controller should show error 206, which needs manual acknowledgement. Where several inverters work in a Team configuration, the emergency stop relay must switch in every cabinet. On some inverters, pressing the emergency stop opens the DC load switches and AC circuit breakers. The button stays locked until it is released with a key. Afterwards, unlock the switch, acknowledge the error, remove the tape from the door contacts and close the cabinet doors. The cabinet is live during the test and there is a risk of fatal electric shock or burns, so touch only the parts named in the instructions.

<!-- review notes
- sentence 7: support check: partial - Passage warns of danger to life from touching live components and to touch only described parts, and implies control voltage is on, but doesn't explicitly say the cabinet is live during the test.
-->
