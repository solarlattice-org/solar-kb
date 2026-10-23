---
id: symptom:reverse-power-flow
type: Symptom
name: Reverse power flow
aliases:
- generator reverse power
- grid reverse current
- Backflow Power
- back-charge current
claims:
- claim_id: c1
  rel: observed_as
  target: meas:reverse-power-above-threshold
  note: Sunny Island measures current flowing back toward the grid or the active generator. It flags the
    event when the reverse power stays above the set value (GdRvPwr/GnRvPwr) for longer than the set time
    (GdRvTm/GnRvTm).
  cite:
  - src: src:sma-kb-w401
    loc: sec=h1
    h: 2f55a09c3626
  - src: src:sma-kb-event-number-1409-w501-w502-w503-w504
    loc: sec=h1
    h: e3e608152291
  - src: src:sma-kb-w501-in-sunny-backup-systems
    loc: sec=h1
    h: c22658b75db0
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Sunny Island shows W401 for generator reverse power protection. It shows W501 to W504 (event 1409)
    when grid reverse current is prevented by a quick grid disconnection, for the master and slaves 1
    to 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=147.r1
    h: fc5f1fabb9eb
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r1
    h: 7b71fe3480c9
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r2
    h: 7db3efd539ae
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r3
    h: e4c35145bbac
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=148.r4
    h: 255ce066f3fd
  - src: src:sma-kb-event-number-1409-w501-w502-w503-w504
    loc: sec=h1
    h: e3e608152291
  review: drafted
---
On Sunny Island systems, warning W401 means AC sources such as PV are driving the running generator, and the reverse power into it has gone on too long. Warnings W501 to W504 (event 1409) mean the inverter saw current flowing toward the utility grid and stopped it, because the settings do not allow feed-in. Common causes are a PV or wind inverter wired on the load side of the automatic switch box, loads too large for the control to react fast enough, or reverse-power limits set too low. By default the generator warning trips after 100 W for 30 seconds, and the grid warning after 100 W for 5 seconds. First check whether grid feed-in is allowed. If the grid operator agrees, set the grid mode to GridFeed. Otherwise compare the generator reverse-power settings with what the generator can handle and adjust them only with the manufacturer's or utility's agreement. An unstable external source can also cause this event, so check the source's stability. On older SI2012/SI2224 firmware the transfer relay wrongly stays closed after W401, and a firmware update is needed. Other inverter brands guard against the same condition with an adjustable back-charge current threshold and an anti-reverse power flow function that is on by default.

<!-- review notes
- sentence 5: support check: partial - Passages support GridFeed with grid operator agreement and adjusting generator settings with manufacturer agreement, but the 'Otherwise' flow and the general 'utility agreement' for adjustment is a reordered synthesis; the generator comparison isn't conditional on feed-in being disallowed.
- sentence 7: support check: partial - Passages show an adjustable back-charge current threshold and anti-reverse flow enabled by default, but don't identify them as other inverter brands' protection against the same condition.
-->
