---
id: symptom:sync-pulse-missing
type: Symptom
name: Missing synchronization pulse
aliases:
- Syncpuls
- CANCom
- CANComSlv1
- CANComSlv2
- Follower Lost CAN synchronization
- Master/Slave Synchronization Message Failure
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'SMA Sunny Island: F783 (level 2) when the internal sync pulse is missing at the device on L1
    (master); W784, W785 and W786 (level 1) when slave 1, 2 or 3 (on L2, L3) misses it.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r21
    h: 7cbf6652d160
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r22
    h: 4932754af33a
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r23
    h: b2a2cf52a260
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r24
    h: 9c7b3b9312c6
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=71.r3
    h: 01cb52162a11
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=71.r1
    h: 8f738a1f2147
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=71.r2
    h: b506fe866f73
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=38.r23
    h: ec57b6718f37
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=39.r25
    h: 4de1add07146
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=38.r22
    h: ed363626a4da
  review: drafted
---
This event occurs in multi-device Sunny Island setups where a slave unit does not receive the synchronization pulse it needs. The display shows F783 when the sync pulse is missing at the master on L1, and W784, W785 or W786 when slave 1, 2 or 3 misses it. F783 is a level 2 event, while the slave messages W784 to W786 are level 1 warnings. The event names (CANCom, CANComSlv1, CANComSlv2) point to the internal communication link between the devices. Check first that the communication cables are undamaged CAT5e and plugged in correctly. Then confirm that the communication bus has a terminator at both ends. Yaskawa Solectria SGI XTM central inverters log similar faults when a follower loses CAN or fast-loop synchronization, or when a master/slave synchronization message fails.

<!-- review notes
- sentence 3: support check: partial - Levels 2 and 1 are stated, but the passages do not call F783 an event versus W-codes warnings beyond the F/W prefix; 'warnings' is only implied.
- sentence 4: support check: partial - Names CANCom etc. and the communication-bus corrective measures suggest an internal communication link, but the passages do not explicitly say so.
- sentence 5: support check: partial - The corrective measure is stated, but 'check first' ordering is not stated.
- sentence 6: support check: partial - Terminator at both ends is mentioned in a truncated fragment, and the ordering 'then' is not stated.
- sentence 4: review: partial - The names CANCom, CANComSlv1 and CANComSlv2 and the fixes for the communication cables and bus suggest a communication link, but the rows describe a 'device-internal' sync pulse and never state the interpretation in the sentence.
-->
