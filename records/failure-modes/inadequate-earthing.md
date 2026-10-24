---
id: fm:inadequate-earthing
type: FailureMode
name: Inadequate earthing
aliases:
- poor ground electrode
- high earth resistance
- neutral not grounded
- PE connection missing
- N-PE voltage too high
- PE conn. missing
- Grounding connection missing
- poor ground
claims:
- claim_id: c1
  rel: presents_as
  target: symptom:missing-ground-connection
  note: SMA inverters report event 901, 'PE connection missing / Check connection', when the grounding
    conductor is not connected correctly.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: tbl=1.r10
    h: d67daffd8f90
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h498
    h: 57e11449fc02
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h17
    h: a776ad38d235
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h257
    h: 260925fde74a
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r3
    h: 933298c8de4f
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:inverter
  note: The inverter detects that its grounding conductor is not connected correctly and raises an event.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: tbl=1.r10
    h: d67daffd8f90
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h17
    h: a776ad38d235
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r3
    h: 933298c8de4f
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:surge-protection-device
  note: A poor ground or a grounding/bonding violation can stop the SPD from performing as specified.
  cite:
  - src: src:eaton-eaton-spd
    loc: sec=h12
    h: 7768f76527f9
  - src: src:eaton-eaton-spd
    loc: sec=h23
    h: 84a3285351fa
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:installation-error
  note: The cause given is a grounding conductor that was not connected correctly.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: tbl=1.r10
    h: d67daffd8f90
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h17
    h: a776ad38d235
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h257
    h: 260925fde74a
  review: drafted
  review_note: 'support check: partial - Passages say the conductor is not correctly connected but do
    not label it an installation error as cause, though it is implied.'
- claim_id: c5
  rel: detected_by
  target: method:startup-commissioning-verification
  note: Commissioning checklists confirm that the grounding conductor is connected to ground, for example
    to a grounding busbar or foundation electrode.
  cite:
  - src: src:sma-doc-278742
    loc: tbl=34.r6
    h: b010e3b02b6a
  - src: src:sma-doc-259761
    loc: tbl=28.r6
    h: 58747d8b069f
  - src: src:sma-doc-278742
    loc: tbl=35
    h: 9ed1a06c22bb
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:neutral-ground-continuity-measurement
  note: In TN systems, a measurement confirms that the neutral and grounding conductors are conductively
    connected.
  cite:
  - src: src:sma-doc-278742
    loc: tbl=35
    h: 9ed1a06c22bb
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:ground-conductor-check
  note: 'Corrective measure: make sure the grounding conductor is connected correctly.'
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: tbl=1.r10
    h: d67daffd8f90
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h17
    h: a776ad38d235
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r3
    h: 933298c8de4f
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:earthing-system-verification
  note: Check that the facility's grounding and bonding meet NEC, CEC and local codes, and confirm the
    site's earthing system before installation.
  cite:
  - src: src:eaton-eaton-spd
    loc: sec=h12
    h: 7768f76527f9
  - src: src:eaton-eaton-spd
    loc: sec=h23
    h: 84a3285351fa
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h14
    h: a99e703fbd5d
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:earth-conductor-last-to-break
  note: For cord-connected equipment, the earthing cable must be longer than the AC grid conductors so
    that it is the last one to break if strain relief fails.
  cite:
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=h157
    h: 7328e7f1c8c7
  review: drafted
  review_note: 'support check: partial - Passage says the earth conductor must be last to be interrupted
    on strain-relief failure and longer than AC conductors, but doesn''t tie it to mitigating inadequate
    earthing explicitly.'
---
Inadequate earthing means the protective grounding conductor is missing, not connected correctly, or the site grounding does not meet code. Some inverters report it as an event saying the PE connection is missing and asking you to check the connection. A poor ground or a bonding violation can also stop surge protection devices from working as specified. At commissioning, confirm that the grounding conductor is tied to ground, for example at a grounding busbar or foundation electrode. On TN systems, measure to confirm that the neutral and grounding conductors are conductively connected. To fix it, make sure the grounding conductor is connected correctly, and check that all grounding and bonding meet NEC, CEC and local rules. Do not change earthing arrangements without approval from the electrical authority or a qualified engineer.
