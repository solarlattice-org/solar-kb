---
id: symptom:inverter-undervoltage
type: Symptom
name: Inverter undervoltage
aliases:
- Event 1710
- F141
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'On the Sunny Island the code depends on which unit sees it: F141 on the master (level 2), and
    W142, W143 or W144 on slaves 1 to 3 (level 1 warnings).'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r22
    h: 0e4bac8ce3b9
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r24
    h: a2a22e9bca7c
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r23
    h: 015c2a9367f7
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r21
    h: 4ed6fc38abf6
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142
    h: e91eeb5e5e1c
  - src: src:sma-kb-event-number-1710-f141-w142-w143-w144
    loc: sec=h1
    h: e6f6981b6981
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:ac-terminal-voltage-low
  note: The voltage at connection AC1 or AC2 of the master or slave is too low on line conductor L1, L2
    or L3.
  quote: The voltage at connection AC1 or AC2 of the master / slave is too low due to AC sources respectively
    large loads in the system.
  cite:
  - src: src:sma-kb-event-number-1710-f141-w142-w143-w144
    loc: sec=h1
    h: e6f6981b6981
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Sunny Island and Sunny Backup battery inverters report inverter undervoltage when the voltage on line conductor L1, L2 or L3 is too low. The master logs F141 or event 1710, and slaves 1, 2 and 3 log the warnings W142, W143 and W144. It means the voltage at the AC1 or AC2 terminal of that unit is too low, usually because of AC sources or large loads connected to the system. Check first that the battery type is not programmed as Other, because that setting alone causes F141. Next, de-energize the AC cables, disconnect all AC sources and loads from AC1 and AC2, and restart the unit with the lid mounted. If the unit starts, the likely cause is too much load or an installation error such as a short circuit; find it by measuring while you reconnect sources and loads one at a time. If the unit does not start with nothing connected, the device itself has failed and must be replaced.

<!-- review notes
- sentence 4: support check: partial - Article says to ensure battery type isn't 'Other' as it causes F141, but doesn't say to check it first or that it alone causes it (not stated as first step).
-->
