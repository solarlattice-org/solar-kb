---
id: symptom:parameter-change-rejected
type: Symptom
name: Parameter change rejected
aliases:
- Grid parameter unchanged
- Grid parameters locked
- Grid parameter locked
- Parameter setting failed
- Grid parameters unchanged
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA events 29004 (grid parameter unchanged), 9003 (grid parameters locked) and 9005 (grid parameters
    cannot be changed) appear in the inverter event log.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=22.r5
    h: 4a55c0f1a1eb
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h108
    h: 51f339841114
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r100
    h: af220f5fb7bb
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r1
    h: dca11bb38795
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r3
    h: '7e7479893027'
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r3
    h: '7e7479893027'
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r3
    h: '7e7479893027'
  - src: src:kb-sma-stptl-10-us-event-messages
    loc: tbl=1.r53
    h: 64a8c31b6cca
  - src: src:sma-kb-event-9005
    loc: sec=h1
    h: ca7c94c2833d
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:parameter-setting-failed-event
  note: SMA events 10101 and 10103 report that the displayed parameter was not changed. Event 7105 reports
    that parameters could not be set from the memory card.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=74.r15
    h: e1de1d8e3b87
  - src: src:sma-doc-259761
    loc: tbl=75.r2
    h: 5a591799a86a
  - src: src:sma-doc-278742
    loc: tbl=78.r1
    h: 8b01e201fa8b
  - src: src:sma-doc-278742
    loc: tbl=78.r3
    h: 1c947c373ec9
  - src: src:sma-doc-278742
    loc: tbl=70.r4
    h: d6e3aad51be7
  - src: src:sma-doc-259761
    loc: tbl=65.r4
    h: 45a34d0b7def
  review: drafted
---
The inverter refuses a parameter change and logs an event saying the grid parameters cannot be changed or are locked, or that a parameter setting failed. On SMA string inverters this shows up as event 29004, 9003 or 9005 in the event log or user interface. Event 9005 can mean three things: the rotary switch position for the country setting is not programmed, the parameters are protected, or the DC input voltage is too low to run the main computer. Event 9003 means the grid parameters are now locked, so you must log in with the SMA Grid Guard code before you can change them. If the Grid Guard code you enter is wrong, the parameters stay protected and the change is still rejected. When a single parameter setting fails, check that the new value is within the allowed thresholds, then try the change again. Check first that the country data set is configured correctly, that the Grid Guard code has been entered, and that there is enough DC voltage, shown by the green LED glowing or flashing.

<!-- review notes
- sentence 2: support check: partial - Events 29004, 9003 and 9005 are in the passages, but the passages don't say they appear in the 'user interface' or specifically for string inverters beyond the 9005 article tag.
- sentence 7: support check: partial - The corrective measures list these three checks, but the passage doesn't say to check them 'first' or in any order.
-->
