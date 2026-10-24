---
id: method:communication-bus-voltage-test
type: DetectionMethod
name: Communication bus voltage test
aliases:
- RS485 A-B voltage check
- CAN H / CAN L voltage check
- BMS bus test
- BMS BUS testing
- CAN Bus voltage
- COM port pin voltage test
- Battery CAN bus voltage test
- BUS test
- Testing CAN Bus Voltage
- Voltage Level Check
- Voltage Testing
claims:
- claim_id: c1
  rel: produces
  target: meas:comm-bus-voltage-absent
  note: On CAN, no voltage on CAN H or CAN L to ground suggests the bus is disconnected or faulty. On
    RS485, 0 V between A and B can mean the transmitter or driver has no power or is inactive, the wiring
    is wrong, or the cable is broken.
  cite:
  - src: src:kb-solis-44002632655-can-communication-port-testing
    loc: sec=h1
    h: 0e75ab24f321
  - src: src:kb-solis-44002632838-rs485-communication-port-testing
    loc: sec=h1
    h: 5807d6d717d8
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: produces
  target: meas:comm-bus-voltage-high
  note: On the S5-GC(50-60)K 16-pin COM port, more than 5 V between pins 3 and 4 points to the COM plug
    fix.
  cite:
  - src: src:kb-solis-44002632838-rs485-communication-port-testing
    loc: sec=h1
    h: 5807d6d717d8
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
A communication bus voltage test uses a multimeter on DC voltage mode to check that the CAN or RS485 lines between the inverter and devices such as the battery BMS, meters or dataloggers carry voltage. First confirm the BMS is wired correctly and the right battery model is set on the inverter, then run the test if alarms such as CAN COM Fail or No Battery do not clear. Find the bus pins and wire colours from the port pin assignment, strip and tin the wire ends, switch the inverter on, and measure CAN H and CAN L each against ground, or RS485 A against B. For RS485 links, test both the device port and the cable plug on each device, with the device powered and any other COM ports left empty. A reading in the expected range shows the inverter should be able to talk to the BMS. No voltage points to a disconnected, broken or miswired bus, which fits a communication bus wiring fault or an inverter-BMS communication fault. Expected values depend on the port and model, so always check the model manual. A normal voltage does not rule out wrong baud rate, parity or address settings, which can still block communication. Bus activity can make RS485 readings jump around. Checking for signals with an oscilloscope or a USB-to-CAN adapter goes further than this voltage check.

<!-- review notes
- sentence 5: support check: partial - The passages support that a normal reading means the inverter should be able to talk to the BMS, and that no voltage points to a disconnected, broken or miswired bus. They don't state the mapping to the specific fault concepts, though that is implied.
- sentence 6: support check: partial - The passages say pin assignment varies, to consult the model manual, and that wrong baud rate or settings can block communication even if wiring is correct. They don't say that expected voltage values depend on port and model, or that normal voltage doesn't rule out settings issues.
- sentence 7: support check: partial - u17 says RS485 readings can jump around during communication, and u8 lists an oscilloscope and USB-to-CAN adapter as communication tests. They don't state that these go further than the voltage check.
- sentence 7: review: partial - The passages support RS485 readings jumping around during communication, and they list USB-to-CAN and oscilloscope signal checks as a separate communication test, but they never say these go further than the voltage check.
-->
