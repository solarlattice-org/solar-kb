---
id: func:inverter-paralleling
type: Function
name: Inverter parallel operation
aliases:
- parallel operation
- cluster operation
- master/slave inverters
- Parallel Mode
- parallel function
- Parallel System
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: requires
  target: proto:can-bus
  note: Solis S6 hybrids link through the Parallel A and Parallel B RJ45 ports using the CAN protocol,
    wired as a daisy chain.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: sec=h1
    h: 6bb2915b40c3
  review: drafted
- claim_id: c2
  rel: requires
  target: tool:solis-soliscloud
  note: The parallel settings are configured over Bluetooth in the SolisCloud app.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: sec=h1
    h: 6bb2915b40c3
  review: drafted
  review_note: 'support check: partial - Parallel settings are configured via Bluetooth in the SolisCloud
    app, but the passages don''t say SolisCloud is required for parallel operation (monitoring is optional).'
- claim_id: c3
  attr: setting_range
  value:
    min: 2
    max: 6
    unit: unit:NUM
  conditions: Total number of hybrid inverters connected in a parallel system
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: sec=h1
    h: 6bb2915b40c3
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h70
    h: 5ba06a5a0a4d
  review: drafted
- claim_id: c4
  attr: setting_range
  value:
    min: 1
    max: 99
    unit: unit:NUM
  conditions: Physical address ID of each inverter in Solis parallel settings. The master must be 1 and
    0 is not allowed.
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h70
    h: 5ba06a5a0a4d
  review: drafted
- claim_id: c5
  attr: setting_range
  value:
    min: 2
    max: 6
    unit: unit:NUM
  scope:
    products:
    - prod:solis-s6-eh2p-l-us
  conditions: ID addresses for slave (follower) inverters. The master keeps address 1.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: sec=h1
    h: 6bb2915b40c3
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=6.4.12
    h: fc9ef5e461f2
  review: drafted
  review_note: 'support check: partial - Followers numbered 2-6 with leader 1 is stated, but the passages
    don''t tie it to the S6-EH2P-L-US product specifically.'
---
Inverter paralleling lets several hybrid inverters run as one coordinated system. One master manages the output power of the slave units. On Solis S6 hybrids, you switch Parallel Mode from Single to Parallel, give the master address 1 and number the slaves 2, 3 and so on, and set the total inverter count. Configure the slaves first and the master last. Turn on Parallel Sync only at the end, slaves before master. After that, the master pushes work modes and other settings to the slaves. Wiring: daisy-chain the units with CAT5/6 cable between the Parallel A and B ports, which use CAN. Set DIP switches 1 and 2 to ON only on the first and last inverter. Connect the meter to the master only, and bond all units to the same ground point. All units need the same firmware version and same-size inverters and batteries. Each battery's BMS must connect to its own inverter. Solis S6 inverters built before January 2023 cannot be paralleled, and unbalanced grid-side loads are not yet supported. If the master has a non-critical fault, the slaves keep running. A critical fault stops all inverters. Slave alarms are forwarded to the master's alarm log. Some products do not allow it. The Solis RHI series does not support parallel operation on its AC-BACKUP port, and doing so voids the warranty. Generac PWRcell Whole Home Backup does not support parallel operation with other storage systems.

<!-- review notes
- sentence 7: support check: partial - RHI AC-BACKUP parallel and warranty void are stated, and Whole Home Backup lacks parallel with other storage, but the Generac statement is about the configuration 'at this time', not the product generally.
-->
