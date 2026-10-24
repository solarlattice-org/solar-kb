---
id: fm:ac-wiring-error
type: FailureMode
name: AC wiring error
aliases:
- Check L-N-PE
- L and N swapped
- second line conductor connected to N
- incorrect AC installation
- disturbance in the AC cabling
- L / N swapped
- 2nd phase connected to N
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:installation-error
  note: Event texts describe incorrect installation of the L/N connection or a second line conductor landed
    on the N terminal.
  cite:
  - src: src:kb-sma-stpxxus50-event-messages
    loc: sec=h14
    h: ce626927b150
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h18
    h: ce626927b150
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h16
    h: ce626927b150
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h19
    h: e07f8c85653c
  - src: src:kb-sma-stpxxus50-event-messages
    loc: sec=h15
    h: e07f8c85653c
  review: drafted
- claim_id: c2
  rel: caused_by
  target: fm:inadequate-earthing
  note: SMA lists a poor ground electrode design, for example a lance that is too short, and a large distance
    between the local electrode and the transformer electrode in a TT grid. Both create potential differences
    between N and PE.
  cite:
  - src: src:sma-kb-error-message-check-l-n-pe-l-n
    loc: sec=h1
    h: 441690eadc5b
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:grid-connection-failure
  note: The inverter detects a disturbance in the AC cabling and will not connect to the grid.
  cite:
  - src: src:sma-kb-error-message-check-l-n-pe-l-n
    loc: sec=h1
    h: 441690eadc5b
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:ac-polarity-reversed
  note: The inverter reports that L and N are swapped.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h191
    h: adf6db4a4ed9
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: tbl=1.r11
    h: 29c7a1adea3f
  - src: src:kb-sma-sbx1spus40-event-messages
    loc: tbl=1.r7
    h: 29c7a1adea3f
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-kb-error-message-check-l-n-pe-l-n
    loc: sec=h1
    h: 441690eadc5b
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-kb-error-message-check-l-n-pe-l-n
    loc: sec=h1
    h: 441690eadc5b
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:grid-voltage-measurement
  note: Measure the AC voltages at the inverter's AC connection.
  cite:
  - src: src:sma-kb-error-message-check-l-n-pe-l-n
    loc: sec=h1
    h: 441690eadc5b
  - src: src:kb-sma-stpxxus50-event-messages
    loc: sec=h14
    h: ce626927b150
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h18
    h: ce626927b150
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h16
    h: ce626927b150
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:fuse-check
  cite:
  - src: src:sma-kb-error-message-check-l-n-pe-l-n
    loc: sec=h1
    h: 441690eadc5b
  review: drafted
  review_note: 'support check: partial - The passage says to check the fuses as part of the corrective
    steps, but it does not present this as a detection method that identifies the error.'
- claim_id: c9
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Move the neutral conductor to the N terminal where a second line conductor was landed there.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: tbl=1.r12
    h: ca2062a0b2d4
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h19
    h: e07f8c85653c
  - src: src:kb-sma-stpxxus50-event-messages
    loc: sec=h15
    h: e07f8c85653c
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:sma-kb-error-message-check-l-n-pe-l-n
    loc: sec=h1
    h: 441690eadc5b
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Do this if the message is still shown after the wiring has been checked.
  cite:
  - src: src:kb-sma-stpxxus50-event-messages
    loc: sec=h14
    h: ce626927b150
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h18
    h: ce626927b150
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h16
    h: ce626927b150
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the error remains after the AC wiring, the fuses and the AC voltage have been checked
    and corrected.
  cite:
  - src: src:sma-kb-error-message-check-l-n-pe-l-n
    loc: sec=h1
    h: 441690eadc5b
  review: drafted
---
An AC wiring error means the inverter's AC side is connected wrongly: line and neutral swapped, a second line conductor landed on the N terminal, or loose L or N conductors. An incorrectly connected grounding conductor can cause it too, as can poor earthing such as a weak ground electrode or a TT grid whose local electrode is far from the transformer electrode. The inverter flags a disturbance in the AC cabling, often as a Check L-N-PE or L/N swapped message, and will not connect to the grid. Check the whole AC run from the inverter to the feed-in meter, make sure the cable is intact, and confirm that L and N are on the correct terminals as the installation manual shows. If a second line conductor is sitting on N, move the neutral conductor to the N terminal. Also check the fuses and measure the AC voltages at the inverter connection. If the message stays after these checks and fixes, contact service, because a component or the whole inverter may need replacing.
