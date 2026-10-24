---
id: fm:rapid-shutdown-keepalive-loss
type: FailureMode
name: Loss of rapid shutdown keep-alive signal
aliases:
- permission-to-operate signal not received
- heartbeat signal absent
- SunSpec signal loss
- RSD deactivated
- PLC keep-alive loss
- AC signal circuit not energized
- module switches in standby
- unintended rapid shutdown
- Transmitter signal is absent
- heart-beat signal
- keep alive signal
- permission to operate signal
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:power-supply-interruption
  note: The transmitter is powered from the inverter AC side. Opening the AC disconnect or breaker, or
    a grid outage, removes its power and the keep-alive stops.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: sec=2.11
    h: 1e0cace0bb9d
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: sec=h46
    h: 9ab0be8a47a5
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=h20
    h: a4fea290e8bc
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=h177
    h: a2dd61033bf5
  review: drafted
- claim_id: c2
  rel: caused_by
  target: fm:plc-signal-crosstalk
  note: With parallel DC lines, another inverter's SunSpec signal can overwrite this inverter's signal.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h1
    h: b48d859b0cfc
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h435
    h: 0f9623b7f0ff
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h627
    h: 0f9623b7f0ff
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h743
    h: 0f9623b7f0ff
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:multiple-plc-transmitters
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h1
    h: b48d859b0cfc
  review: drafted
  review_note: 'support check: partial - Passage says multiple transmitters create crosstalk reducing
    receiver functionality, but doesn''t explicitly say keep-alive signal is lost.'
- claim_id: c4
  rel: caused_by
  target: stressor:dc-conductor-proximity
  note: DC lines run in parallel with lines from another inverter.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h435
    h: 0f9623b7f0ff
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h627
    h: 0f9623b7f0ff
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h743
    h: 0f9623b7f0ff
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:rapid-shutdown-device
  cite:
  - src: src:abb-fimer-apsmart-rsd-field-install
    loc: sec=h3
    h: c392ffc1e53e
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: sec=2.11
    h: 1e0cace0bb9d
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: sec=h46
    h: 9ab0be8a47a5
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=h177
    h: a2dd61033bf5
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:rapid-shutdown-transmitter
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: sec=2.11
    h: 1e0cace0bb9d
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: sec=h46
    h: 9ab0be8a47a5
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=h177
    h: a2dd61033bf5
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:ac-disconnect
  note: The open or closed position of the AC disconnect shows the rapid shutdown status.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: sec=2.11
    h: 1e0cace0bb9d
  - src: src:kb-sma-stpxxus50-rapid-shutdown-equipment
    loc: sec=h1
    h: 46538d48fa94
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: sec=h46
    h: 9ab0be8a47a5
  review: drafted
  review_note: 'support check: partial - Passages tie AC disconnect opening to stopping the signal and
    say its position indicates rapid shutdown status, but loss of signal affecting the disconnect is not
    really stated.'
- claim_id: c8
  rel: affects
  target: comp:pv-disconnect-switch
  note: An external DC switch left open stops the PLC signal from reaching the receivers.
  cite:
  - src: src:kb-sma-stpxxus50-rapid-shutdown-equipment
    loc: sec=h1
    h: 46538d48fa94
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=h147
    h: e0881a339d61
  review: drafted
  review_note: 'support check: partial - Passage says an external DC switch off prevents receivers getting
    the PLC signal, but it''s the switch causing the loss rather than the loss affecting the switch.'
- claim_id: c9
  rel: presents_as
  target: symptom:rapid-shutdown
  cite:
  - src: src:abb-fimer-apsmart-rsd-field-install
    loc: sec=h3
    h: c392ffc1e53e
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: sec=h46
    h: 9ab0be8a47a5
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=h177
    h: a2dd61033bf5
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:low-shutdown-string-voltage
  quote: With rapid shutdown receivers installed, the PV string voltages should be very low.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=h177
    h: a2dd61033bf5
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=h147
    h: e0881a339d61
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Per-module string voltage around the receiver standby level shows the receivers are off.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=h147
    h: e0881a339d61
  review: drafted
  review_note: 'support check: partial - Passages give low per-module voltage (0.6-0.7 V) as expected
    with receivers and a check when voltages are low, but don''t explicitly frame it as detecting signal
    loss.'
- claim_id: c12
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h436
    h: ab549348ae54
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h628
    h: ab549348ae54
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h744
    h: ab549348ae54
  review: drafted
  review_note: 'support check: partial - Passages list checking rapid shutdown settings as a corrective
    measure, not as detecting loss of keep-alive signal.'
- claim_id: c13
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Make sure the AC breaker is on so the inverter and its transmitter get AC voltage.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=h147
    h: e0881a339d61
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:rapid-shutdown-initiator-check
  note: Make sure the rapid shutdown switch is popped out by twisting it clockwise.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=h147
    h: e0881a339d61
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:pv-switch-function-check
  note: Make sure any external DC switch is turned on so the PLC signal can reach the receivers.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=h147
    h: e0881a339d61
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Set the rapid shutdown operating mode to match the DC disconnection unit used.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h436
    h: ab549348ae54
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h628
    h: ab549348ae54
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h744
    h: ab549348ae54
  review: drafted
---
Module-level rapid shutdown receivers only stay on while they keep receiving a heartbeat or keep-alive signal from a power line transmitter. When that signal stops, they shut the PV modules down. The transmitter runs on the inverter's AC power. Opening the AC disconnect or breaker, or losing the grid, stops the signal and puts the array into rapid shutdown. The signal can also be overwritten or weakened by crosstalk from another inverter's transmitter when DC lines run in parallel. In the field the strings show only a very low voltage, a fraction of a volt per module, and the array produces nothing. If string voltages are low, check that the AC breaker is on, that the rapid shutdown switch is popped out, and that any external DC switch is closed so the signal can reach the receivers. Also check that the inverter's rapid shutdown mode matches the module switches used, and that the module switches work. IV curves taken with rapid shutdown devices installed can show steps and kinks caused by the devices switching. Interpret them with care.

<!-- review notes
- sentence 4: support check: partial - Low voltage under 1 V per module is stated, but array producing nothing is not explicitly stated.
- sentence 4: review: partial - Very low string voltage (under 1 V, or 0.6-0.7 V per module) is stated, but no passage says the array produces nothing.
-->
