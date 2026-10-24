---
id: concept:open-and-closed-loop-control
type: Concept
name: Open-loop and closed-loop control
aliases:
- closed-loop control
- open-loop control
- open loop vs closed loop
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: func:closed-loop-plant-control
  note: Tesla System Controller corrects Megapack power commands using real and reactive power feedback
    from the meter.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.3.4
    h: 3b39d623a8e7
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=2.5.5
    h: 54730bb896f4
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.5.4
    h: a5508dbc6f2f
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:point-of-interconnection
  note: Closed-loop control uses measured values fed back from the point of interconnection.
  cite:
  - src: src:sma-kb-when-do-i-use-the-operating-mode-closed-loop-control-and-when-open-loop-control-in
    loc: sec=h1
    h: 92b23ebd81e8
  - src: src:sma-doc-275857
    loc: tbl=6.r6
    h: eb6b0a239b8d
  review: drafted
- claim_id: c3
  rel: related_to
  target: comp:energy-meter
  note: The meter provides the feedback signal for closed-loop control.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.3.4
    h: 3b39d623a8e7
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=2.5.5
    h: 54730bb896f4
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.5.4
    h: a5508dbc6f2f
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:export-limitation
  note: Open-loop control is enough to limit active power feed-in in pure feed-in systems. Systems with
    self-consumption need closed-loop control.
  cite:
  - src: src:sma-kb-when-do-i-use-the-operating-mode-closed-loop-control-and-when-open-loop-control-in
    loc: sec=h1
    h: 92b23ebd81e8
  - src: src:sma-doc-240154
    loc: sec=h201
    h: 41daf4831d8d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  rel: related_to
  target: concept:self-consumption
  note: With self-consumption, closed-loop control is used so that the power at the interconnection point
    still meets the grid operator's limit.
  cite:
  - src: src:sma-kb-when-do-i-use-the-operating-mode-closed-loop-control-and-when-open-loop-control-in
    loc: sec=h1
    h: 92b23ebd81e8
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:reactive-power
  note: SMA recommends closed-loop control for reactive power setpoints so line and transformer effects
    are compensated.
  cite:
  - src: src:sma-kb-when-do-i-use-the-operating-mode-closed-loop-control-and-when-open-loop-control-in
    loc: sec=h1
    h: 92b23ebd81e8
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:active-power
  cite:
  - src: src:sma-kb-when-do-i-use-the-operating-mode-closed-loop-control-and-when-open-loop-control-in
    loc: sec=h1
    h: 92b23ebd81e8
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.3.4
    h: 3b39d623a8e7
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: related_to
  target: stressor:reactive-power-demand
  note: With high self-consumption and high reactive demand, inverters may fail to hold the setpoints,
    so open-loop control is recommended.
  cite:
  - src: src:sma-kb-when-do-i-use-the-operating-mode-closed-loop-control-and-when-open-loop-control-in
    loc: sec=h1
    h: 92b23ebd81e8
  review: drafted
- claim_id: c9
  rel: related_to
  target: func:system-manager
  note: A System Manager can take over closed-loop control at the point of interconnection.
  cite:
  - src: src:sma-doc-275857
    loc: tbl=6.r6
    h: eb6b0a239b8d
  review: drafted
- claim_id: c10
  rel: related_to
  target: prod:sma-data-manager-m
  note: The Data Manager offers both operating modes for active and reactive power.
  cite:
  - src: src:sma-kb-when-do-i-use-the-operating-mode-closed-loop-control-and-when-open-loop-control-in
    loc: sec=h1
    h: 92b23ebd81e8
  review: drafted
- claim_id: c11
  rel: related_to
  target: prod:sma-cluster-controller
  note: Uses open-loop control in systems with no self-consumption and direct limitation of feed-in.
  cite:
  - src: src:sma-doc-240154
    loc: sec=h201
    h: 41daf4831d8d
  review: drafted
- claim_id: c12
  rel: related_to
  target: prod:tesla-megapack-platform
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.3.4
    h: 3b39d623a8e7
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=2.5.5
    h: 54730bb896f4
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.5.4
    h: a5508dbc6f2f
  review: drafted
- claim_id: c13
  rel: related_to
  target: proto:modbus
  note: Closed Loop Control Enable is a read/write boolean at Modbus register 21401.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=97.r1
    h: 44c528c5141f
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=109.r1
    h: 44c528c5141f
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=97
    h: 45b9d99a7b8b
  review: drafted
---
Open-loop control sends power setpoints to the inverters without any feedback of the actual value. Closed-loop control feeds back the values measured at the point of interconnection and corrects the commands. In closed-loop operation, the controller compares the real and reactive power read by the meter against the total command. It then adds a correction so that the target is actually met at the meter. For active power limits, open-loop control is enough in a pure feed-in system. A system with self-consumption should use closed-loop control so that surplus PV goes to local loads and the interconnection point still meets the grid operator's limit. For reactive power, closed-loop control is normally recommended because it compensates for the effects of the line and any transformer. One exception is a site with high self-consumption and a large reactive demand, such as electrical machines without compensation equipment. There the inverters may produce almost only reactive power and still miss the setpoint, so open-loop control is advised. On Tesla Megapack systems, closed-loop control is turned off by default at commissioning. This prevents wind-up if the meter's current transformer or potential transformer wiring is wrong. It should be switched on only after the meter readings are confirmed to match the applied command. In SMA systems, a device with the System Manager function can take over closed-loop control at the point of interconnection.

<!-- review notes
- sentence 1: support check: partial - Definitions of feedback vs no feedback are stated, but 'corrects the commands' is from Tesla, not the SMA article cited, and 'sends setpoints to inverters' is not stated.
- sentence 2: support check: partial - Meter feedback and adjustment added to command are stated, but an explicit comparison against the total command is only implied.
- sentence 1: review: partial - The SMA passage defines open-loop as without feedback and closed-loop as with feedback of the values measured at the point of interconnection, but it does not say that setpoints are sent to inverters or that commands are corrected.
-->
