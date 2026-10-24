---
id: state:sma-arc-fault-operation-inhibition
type: OperatingState
name: Operation inhibition after arc fault
aliases:
- arc fault lockout
- operation inhibition after arc detection
- operation inhibition
- immediate operation inhibition
category: Inverters
make: sma
claims:
- claim_id: c1
  rel: part_of
  target: func:dc-arc-fault-protection
  note: Operation inhibition is the latched response of the SMA arc-fault circuit interrupter (AFCI) when
    it is enabled with operation inhibition (parameter AFCI switched on / AfciIsOn set to Yes).
  cite:
  - src: src:kb-sma-stptl-10-us-activating-or-deactivating-the-arc-fault-circuit-interrupter-afci
    loc: sec=h3
    h: 4a3bcf8292c1
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: tbl=2
    h: 5001dc1211fe
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  review: drafted
---
Operation inhibition is a latched stop. The SMA inverter enters it when the arc-fault circuit interrupter is enabled with operation inhibition and detects an electric arc, and it stops feeding into the grid. The red LED glows and event 4301 appears on the display, in the inverter's event list or in a communication product such as Sunny Portal. Some three-phase models also report event 4302. The inverter does not restart by itself. Someone has to reset the inhibition manually before it will feed in again. On Sunny Tripower TL-US units the reset needs a communication product that matches the type of communication in use. If the AFCI is instead set to run without operation inhibition, no lockout happens. The inverter waits, restarts automatically and checks whether the arc is still there. Some models can also be set to lock out only after 5 arc detections within 24 hours.

<!-- review notes
- sentence 2: support check: partial - 4301 with red LED on display, event list and Sunny Portal is stated, and 4302 appears in an event list, but 'some three-phase models' is not stated.
- sentence 4: support check: partial - The communication-product requirement is stated, but the passage doesn't name Sunny Tripower TL-US or say it applies to those units.
- sentence 6: support check: partial - The option of operation inhibition after 5 detections within 24 hours is stated, but 'some models' scope is not specified in the passage.
-->
