---
id: fm:energy-meter-failure
type: FailureMode
name: Energy meter measurement or communication failure
aliases:
- defective S0 meter counter
- continuous 0W grid feed-in measured
- communication with the meter is disrupted
- energy meter MIA
- Meter MIA
- Meter Invalid
- Communication fault with meter unit
- Meter-com-flt
- Communication disturbed
claims:
- claim_id: c1
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:sma-kb-sunny-home-manager-continuous-0w-watt-grid-feed-in-measured
    loc: sec=h1
    h: c24f2ca4ce92
  - src: src:sma-doc-246498
    loc: sec=h475
    h: b26580197ffc
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h235
    h: 881ad6c197f7
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r5
    h: fe9e6fc08424
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: affects
  target: comp:communication-cable
  note: Damaged or loose data cables and terminals between the meter and the metering board or inverter
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r5
    h: fe9e6fc08424
  - src: src:sma-doc-278742
    loc: tbl=73.r3
    h: 5c6dc8a588bd
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:low-pv-production
  note: With S0 meters, PV output below the meter's own consumption stops it from reporting; the message
    clears once PV power rises
  cite:
  - src: src:sma-kb-sunny-home-manager-continuous-0w-watt-grid-feed-in-measured
    loc: sec=h1
    h: c24f2ca4ce92
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: caused_by
  target: stressor:weak-wireless-signal
  cite:
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r42
    h: 949377f41b4f
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  review: drafted
  review_note: 'support check: partial - Passages advise improving Wi-Fi quality for 7619 but do not explicitly
    state weak signal as a cause.'
- claim_id: c5
  rel: caused_by
  target: stressor:installation-error
  note: Meter not placed in the same network as the inverter, or data cables installed wrongly
  cite:
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r41
    h: '51788795e531'
  - src: src:sma-doc-278742
    loc: tbl=73.r3
    h: 5c6dc8a588bd
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:meter-configuration-error
  note: An unsupported measurement interval, or an S0 meter that does not output values netted across
    the line conductors
  cite:
  - src: src:sma-doc-246498
    loc: tbl=84.r2
    h: 242db949bd9b
  - src: src:sma-doc-240154
    loc: tbl=88.r2
    h: 4e84e9c37de8
  review: drafted
- claim_id: c7
  rel: caused_by
  target: fm:monitoring-network-fault
  note: Unauthorized participants on a shared network can disrupt meter communication
  cite:
  - src: src:sma-doc-278742
    loc: sec=h1008
    h: ae13d6421050
  review: drafted
  review_note: 'support check: partial - Passage says a separate network prevents disruption by unauthorized
    participants, but doesn''t explicitly frame it as a network configuration fault cause of meter failure.'
- claim_id: c8
  rel: presents_as
  target: symptom:communication-loss
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h235
    h: 881ad6c197f7
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r41
    h: '51788795e531'
  - src: src:sma-doc-259761
    loc: tbl=69.r1
    h: 0abbf0ec280e
  - src: src:kb-sma-shpxxxus21-event-messages
    loc: sec=h27
    h: bbadf76af96c
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r5
    h: fe9e6fc08424
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=93
    h: 803db315ba27
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=15.r7
    h: c7515847f49b
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:zero-feed-in-reading
  note: The logbook message appears when an S0 feed-in meter has sent no feed-in data for 24 hours
  cite:
  - src: src:sma-kb-sunny-home-manager-continuous-0w-watt-grid-feed-in-measured
    loc: sec=h1
    h: c24f2ca4ce92
  - src: src:sma-doc-246498
    loc: sec=h475
    h: b26580197ffc
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:meter-invalid-alert
  note: Raised on loss of communication, out-of-bounds or unreasonable readings, or a PT/CT failure flag
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=16.r7
    h: 93406b4603cf
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=19.r5
    h: 93406b4603cf
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.3.5
    h: 95c425ad14fe
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=2.5.4
    h: f3201f99d347
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=16.r7
    h: 93406b4603cf
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:unrealistic-meter-values
  cite:
  - src: src:sma-doc-246498
    loc: tbl=84.r2
    h: 242db949bd9b
  - src: src:sma-doc-240154
    loc: tbl=88.r2
    h: 4e84e9c37de8
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:inverter-shutdown
  note: Loss of meter communication can stop the battery inverter and the PV inverters, depending on the
    control mode
  cite:
  - src: src:sma-doc-274308
    loc: sec=h22
    h: 3ca55ae20307
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: sec=11
    h: 9e5cf614be07
  review: drafted
- claim_id: c13
  rel: leads_to
  target: fm:export-control-fault
  note: Active power feed-in limitation cannot work while the feed-in meter is faulty
  cite:
  - src: src:sma-doc-246498
    loc: sec=h475
    h: b26580197ffc
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:communication-test
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h235
    h: 881ad6c197f7
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r41
    h: '51788795e531'
  - src: src:kb-sma-shpxxxus21-event-messages
    loc: sec=h27
    h: bbadf76af96c
  review: drafted
  review_note: 'support check: partial - Passages show inverter detecting no data from meter, but no explicit
    ''communication test'' method is named.'
- claim_id: c15
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r5
    h: fe9e6fc08424
  - src: src:sma-doc-278742
    loc: tbl=73.r3
    h: 5c6dc8a588bd
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r41
    h: '51788795e531'
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r42
    h: 949377f41b4f
  - src: src:kb-sma-shpxxxus21-event-messages
    loc: sec=h27
    h: bbadf76af96c
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:wireless-range-extension
  note: Use a Wi-Fi repeater, or connect the inverter to the router by Ethernet
  cite:
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r42
    h: 949377f41b4f
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:dedicated-communication-network
  cite:
  - src: src:sma-doc-278742
    loc: sec=h1008
    h: ae13d6421050
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Set the communication timeout for the point-of-interconnection meter
  cite:
  - src: src:sma-doc-274308
    loc: sec=h22
    h: 3ca55ae20307
  - src: src:sma-doc-278742
    loc: sec=h1008
    h: ae13d6421050
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:meter-configuration-correction
  cite:
  - src: src:sma-doc-246498
    loc: tbl=84.r2
    h: 242db949bd9b
  - src: src:sma-doc-240154
    loc: tbl=88.r2
    h: 4e84e9c37de8
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:energy-meter-replacement
  note: Replace a defective S0 counter with a supported energy meter
  cite:
  - src: src:sma-kb-sunny-home-manager-continuous-0w-watt-grid-feed-in-measured
    loc: sec=h1
    h: c24f2ca4ce92
  review: drafted
- claim_id: c22
  rel: distinguished_from
  target: fm:energy-meter-installation-error
  by: method:startup-commissioning-verification
  note: The meter invalid alert does not catch wiring faults such as reversed CT polarity, so those have
    to be checked at commissioning
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.3.5
    h: 95c425ad14fe
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=2.5.4
    h: f3201f99d347
  review: drafted
---
In this failure, the inverter, battery inverter or site controller stops getting usable data from the energy meter. Either the link is lost or the meter sends readings that make no sense. It shows up as a meter communication fault, a meter MIA or meter invalid flag, or a feed-in reading that stays at 0 W for a full day. While the meter is out, export limiting cannot work, and depending on the control mode the system may stop until communication returns. With an S0 meter, first wait for PV output to rise, because low production alone can keep the meter from reporting. If the message stays, the S0 counter is probably defective and should be replaced. Check that the meter is on the same network as the inverter, and that the data cables and terminals are undamaged and tight. On Wi-Fi links, improve the signal with a repeater or switch to Ethernet. If communication stays unstable, set up a separate network with its own router. The meter invalid flag does not catch reversed CT polarity, so check the meter wiring at commissioning.

<!-- review notes
- sentence 4: support check: partial - Wait for PV and defective counter are stated, but 'replaced' is only a recommendation to switch to SMA Energy Meter, and 'probably' is an inference.
-->
