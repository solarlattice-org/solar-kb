---
id: state:self-test
type: OperatingState
name: Self-test
aliases:
- grid protection self-test
- autotest
- insulation self-test
- Self-diagnosis
category: Inverters
---
A self-test is a routine in which the device checks that a critical subsystem or protective function works and reports any condition found to be out of tolerance. On inverters set to the Italian CEI 0-21 grid standard, the autotest is started from the display menu or over an RS485/USB converter with Aurora Communicator software. During the test the device needs a stable network connection and must not be touched. On some SMA inverters the autotest must run at least once every 24 hours. Status message 280 reports this 24-hour timeout and needs no action. The display or LED shows the state differently by product: an SMA I/O module flashes red and green with no corrective action needed, while a Solectria inverter keeps its green LED on and shows Self-test as limited operation. During the Fronius arc detection self-test, the inverter simulates an arc. A successful test disconnects the inverter from the grid and stops feed-in, and the display shows Self-test completed and Start AFCI, which the technician confirms with Enter. For the Generac PVRSS self-test, the PV Link must first be disabled. The display then reads Testing PVRSS for up to three minutes and changes to Test Success when the test passes, after which the PV Link turns itself back on. If the Italy-only self-test is aborted (SMA event 9007), check that the AC connection is correct and restart the test. If a fault occurs during a self-test, the device reports a self-test error and an authorised electrician should be notified.

<!-- review notes
- sentence 3: support check: partial - Message 280 and the 24-hour requirement with no action are stated, but 'on some SMA inverters' is not stated; the passages don't name the device as SMA.
- sentence 4: support check: partial - Flashing red/green Self-test with no corrective measures is shown and Solectria-like green LED limited operation is shown, but the passages don't name SMA I/O module or Solectria.
-->
