---
id: fm:communication-bus-fault
type: FailureMode
name: Communication bus wiring or termination fault
aliases:
- missing terminating resistor
- terminating resistor missing
- missing terminator
- RS485-all-fail
- signal reflections
- RJ45 crimp fault
- cross-wired signal wiring
- terminator not inserted
- RS485 AllFail
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:installation-error
  note: A terminating resistor that is missing or wrong at a bus end node disturbs data transmission.
  cite:
  - src: src:enphase-enphase-troubleshooting-energy-systems-with-iq-battery-5p
    loc: sec=h48
    h: 21e245e5e474
  - src: src:sma-doc-275752
    loc: sec=h162
    h: 398aa158ed89
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:poor-connector-contact
  note: CommErr alarm is attributed to poor contact at the terminal block connectors of the internal communication
    wires.
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37.r5
    h: ba3a944e3c4f
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r2
    h: 8a49e69e6164
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-cable
  cite:
  - src: src:enphase-enphase-troubleshooting-energy-systems-with-iq-battery-5p
    loc: sec=h48
    h: 21e245e5e474
  - src: src:sma-doc-278742
    loc: tbl=73.r6
    h: e21d8d120311
  - src: src:sma-doc-259761
    loc: tbl=69.r6
    h: 62365a359481
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:internal-communication-cable
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37.r5
    h: ba3a944e3c4f
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r2
    h: 8a49e69e6164
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:communication-loss
  note: Examples include loss of communication with one or all inverters, with a Multicluster Box, or
    with the master device.
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=h109
    h: 7de92bdd095c
  - src: src:sma-doc-259761
    loc: tbl=69.r6
    h: 62365a359481
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=68.r8
    h: e3fb0c52c01d
  - src: src:sma-doc-259761
    loc: sec=h818
    h: c02dfb4d0c55
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:internal-communication-failure
  cite:
  - src: src:sma-doc-278742
    loc: tbl=73.r6
    h: e21d8d120311
  - src: src:sma-doc-259761
    loc: tbl=69.r7
    h: c63c963a8783
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=37.r5
    h: ba3a944e3c4f
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r2
    h: 8a49e69e6164
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:sync-pulse-missing
  note: The device-internal communication pulse is missing on at least one device in the cluster.
  cite:
  - src: src:sma-doc-278742
    loc: tbl=73.r6
    h: e21d8d120311
  - src: src:sma-doc-259761
    loc: tbl=69.r7
    h: c63c963a8783
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:bus-termination-resistance-check
  cite:
  - src: src:enphase-enphase-troubleshooting-energy-systems-with-iq-battery-5p
    loc: sec=h47
    h: 9ef4538d56bd
  - src: src:sma-doc-259761
    loc: sec=h309
    h: 255d449d5cb8
  - src: src:sma-doc-278742
    loc: sec=h322
    h: acd141cd00e5
  review: drafted
  review_note: 'support check: partial - Passages mention testing the terminating resistor and checking
    bus termination, but don''t state it detects the fault or describe a resistance check.'
- claim_id: c9
  rel: mitigated_by
  target: mit:communication-bus-termination
  note: Fit a terminator at both ends of the bus, for example 120 ohm between CAN_H and CAN_L, or set
    the RS485 termination switch to ON on end devices.
  cite:
  - src: src:sma-doc-275752
    loc: sec=h162
    h: 398aa158ed89
  - src: src:sma-doc-278742
    loc: tbl=73.r6
    h: e21d8d120311
  - src: src:sma-doc-278742
    loc: sec=h893
    h: 759302c4d7ce
  - src: src:sma-doc-259761
    loc: sec=h779
    h: 759302c4d7ce
  - src: src:sma-doc-278742
    loc: sec=h909
    h: 759302c4d7ce
  - src: src:sma-doc-259761
    loc: sec=h793
    h: 759302c4d7ce
  - src: src:sma-doc-259761
    loc: tbl=69.r6
    h: 62365a359481
  - src: src:sma-doc-259761
    loc: tbl=69.r7
    h: c63c963a8783
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=68.r8
    h: e3fb0c52c01d
  - src: src:sma-doc-259761
    loc: tbl=72.r7
    h: 76e35eccb4ba
  - src: src:sma-doc-278303
    loc: sec=h83
    h: 79df67d51bdf
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=16
    h: 659fb2d59198
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=16.r2
    h: 05240a992756
  review: drafted
  review_note: 'support check: partial - Terminator at both ends and the RS485 termination switch ON are
    supported, but 120 ohm between CAN_H and CAN_L is only via pin descriptions; broadly supported though
    RS485 ''end devices'' is not stated.'
- claim_id: c10
  rel: mitigated_by
  target: mit:communication-cable-check
  note: Use undamaged CAT5e cables and make sure they are plugged in correctly.
  cite:
  - src: src:sma-doc-278742
    loc: tbl=73.r6
    h: e21d8d120311
  - src: src:sma-doc-278742
    loc: sec=h893
    h: 759302c4d7ce
  - src: src:sma-doc-259761
    loc: sec=h779
    h: 759302c4d7ce
  - src: src:sma-doc-278742
    loc: sec=h909
    h: 759302c4d7ce
  - src: src:sma-doc-259761
    loc: sec=h793
    h: 759302c4d7ce
  - src: src:sma-doc-259761
    loc: tbl=69.r6
    h: 62365a359481
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=68.r8
    h: e3fb0c52c01d
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:correct-crimping
  note: Crimp the RJ45 connectors on RS485 and Ethernet cables per TIA/EIA 568B using a standard crimping
    tool.
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: sec=h82
    h: eb4c9cdfb4c4
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: fig=136
    h: d288dcc3b1ab
  - src: src:chint-cps-36kw-user-manual-2024
    loc: fig=137
    h: ca464ba707e4
  review: drafted
---
On an RS485 line with no termination, signals reflect back from the open ends, and the terminator absorbs them when it matches the cable impedance. The fault shows up as lost communication with some or all inverters, a master, or a Multicluster Box, or as faulty CAN communication with a missing internal communication pulse. Poor contact at the terminal blocks of internal communication wires can also raise a communication error alarm. To confirm it, test the terminating resistor and check the termination and wiring of the communication buses. Fix it by fitting a terminator at both ends of the bus or turning on the termination switch on the end devices, and by using undamaged, correctly plugged CAT5e cables. Termination is not always needed: at low baud rates it may be unnecessary, and it adds load to the line, so decide site by site.

<!-- review notes
- sentence 4: support check: partial - Passages list testing the terminating resistor and checking communication bus termination, but give no detail on confirming the fault.
-->
