---
id: fm:parallel-inverter-sync-fault
type: FailureMode
name: Parallel inverter synchronization fault
aliases:
- MulMasterErr
- Addr-Conflict
- HeartbeatLose
- MasterLoseErr
- SlaveLoseErr
- Mode Conflict
- SlavePrd-Err
- MasterPrd-Err
- ModeConflict
- MasterSyncLose
- SlaveSyncErr
- Master/Slave Synchronization Message Failure
- Follower Lost Fast Loop synchronization
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:unsuitable-communication-cable
  note: A parallel cable that is not the one supplied with the product, is missing cores of the 8-core
    wire, or has no shield can break communication between units.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r2
    h: 88075f629793
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r9
    h: ef2d54c4c3a4
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:installation-error
  note: A loose or wrongly connected parallel signal line between inverters.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r2
    h: 88075f629793
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r6
    h: cef65aa1799b
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r9
    h: ef2d54c4c3a4
  review: drafted
- claim_id: c3
  rel: caused_by
  target: fm:duplicate-communication-address
  note: Two or more machines in the parallel system set to the same address raise Addr-Conflict.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:inverter-settings
  note: Host address set to 0 (addresses must start at 1), or two or more units configured as master.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r6
    h: cef65aa1799b
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r8
    h: 0045ad23f8e3
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:poor-grid-quality
  note: Poor local grid quality can disturb the master or slave synchronization signal period.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r3
    h: b5096f21fbfc
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r4
    h: 1af8e948fb46
  review: drafted
- claim_id: c6
  rel: caused_by
  target: fm:communication-bus-fault
  note: Shielding, grounding and DIP switch settings of the parallel communication link are typical checks.
  cite:
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
  review_note: 'support check: partial - The passage lists DIP switch, shielded cabling and grounding
    as checks, but does not mention termination or tie them specifically to a bus wiring fault for sync.'
- claim_id: c7
  rel: affects
  target: comp:communication-cable
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r2
    h: 88075f629793
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r9
    h: ef2d54c4c3a4
  review: drafted
- claim_id: c8
  rel: affects
  target: comp:inverter
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r2
    h: 88075f629793
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r8
    h: 0045ad23f8e3
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:sync-pulse-missing
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r2
    h: 88075f629793
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=39.r25
    h: 4de1add07146
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=38.r23
    h: ec57b6718f37
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:address-conflict-alarm
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:communication-loss
  note: Heartbeat packet loss or no communication over the parallel line.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r6
    h: cef65aa1799b
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:configuration-error
  note: Multiple masters or other parallel configuration conflicts.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r8
    h: 0045ad23f8e3
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r2
    h: 88075f629793
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r6
    h: cef65aa1799b
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r9
    h: ef2d54c4c3a4
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Make sure each unit has a unique address starting from 1 and that only one master exists.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r6
    h: cef65aa1799b
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r8
    h: 0045ad23f8e3
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:communication-bus-termination
  note: Use shielded cabling with proper grounding and check DIP switch settings.
  cite:
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
  review_note: 'support check: partial - Shielded cabling, grounding and DIP switch checks are stated,
    but termination is not mentioned.'
- claim_id: c16
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r2
    h: 88075f629793
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r3
    h: b5096f21fbfc
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r6
    h: cef65aa1799b
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r8
    h: 0045ad23f8e3
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r4
    h: 1af8e948fb46
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r9
    h: ef2d54c4c3a4
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r1
    h: 826afc04ed93
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r2
    h: 88075f629793
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r3
    h: b5096f21fbfc
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r6
    h: cef65aa1799b
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r8
    h: 0045ad23f8e3
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r4
    h: 1af8e948fb46
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r9
    h: ef2d54c4c3a4
  review: drafted
---
In a system of inverters running in parallel, the master and slave units lose synchronization or cannot agree on their roles. The inverter shows alarms such as lost master or slave sync signal, an abnormal sync signal period, heartbeat loss, address conflict, multiple masters, or an on-grid/off-grid mode conflict. Common causes are a loose or wrongly connected parallel cable, a cable other than the one supplied, a cable with missing cores out of the 8, or a cable with no shield. Configuration causes include two units with the same address, a host address set to 0 (addresses must start at 1), or more than one unit set as master. Faults with the sync signal period can also come from poor local grid quality, so check the grid as well. Check the DIP switches, address settings, cable shielding and grounding, and firmware compatibility across all units. After you correct the wiring or settings, restart the inverter, and contact customer service if the fault does not clear.

<!-- review notes
- sentence 6: support check: partial - The listed items are stated, but 'across all units' is not stated in the passage.
-->
