---
id: fm:internal-power-supply-fault
type: FailureMode
name: Internal power supply fault
aliases:
- Power Supply Board
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  note: The 24 VDC supply that powers the inverter controls is a replaceable part inside the inverter.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h237
    h: 0c161ca0b681
  - src: src:yaskawa-solectria-power-supply-board
    loc: sec=h1
    h: c4863c26213d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - The service table lists replacing the 24 VDC power supply for
    inverter controls as an inverter repair, but nothing states an ''internal power supply fault'' affects
    the inverter as a fault relation.'
- claim_id: c2
  rel: presents_as
  target: symptom:inverter-leds-off
  note: 'When the POWER light is off, the power supply is not working. The RUN, GRID and FAULT lights
    can also go dark when the supply is down. A dark FAULT light alone is ambiguous: it can also mean
    there is no fault.'
  quote: Light off | Power supply not working
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=23
    h: 668ffb1b036a
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=23.r5
    h: e5ced9f311e0
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=26.r9
    h: 3baf059af7f2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: detected_by
  target: method:inverter-display-check
  note: Check the front-panel LEDs. If the POWER working light is off, the inverter's control supply is
    not energized.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=23
    h: 668ffb1b036a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: mitigated_by
  target: mit:power-supply-replacement
  note: Replace the 24 VDC power supply or power supply board for the inverter controls. An inverter specialist
    does this as needed, following the manufacturer's replacement instructions.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h237
    h: 0c161ca0b681
  - src: src:yaskawa-solectria-power-supply-board
    loc: sec=h1
    h: c4863c26213d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The service table shows an inverter specialist replaces the 24
    VDC supply as needed, and a power supply board replacement instruction is cited, but the passage doesn''t
    state it mitigates a fault or give the manufacturer instructions'' content.'
---
An internal power supply fault means the low-voltage supply that runs the inverter's control electronics has failed. On the front panel, the POWER working light is off, which the manual reads as the power supply not working. The RUN, GRID and FAULT lights can also stay dark, so a dark FAULT light does not prove the inverter is healthy. To confirm, check the LED panel and see whether the control panel powers up at all. The fix is to replace the power supply for the inverter controls. An inverter specialist does this, following the manufacturer's board replacement instructions.

<!-- review notes
- sentence 1: support check: partial - The passages mention a 24 VDC power supply for inverter controls being replaced, but do not define a fault as failure of that low-voltage supply.
- sentence 4: support check: partial - The LED table supports reading the POWER light as an indicator of whether the control panel is energized, but nothing explicitly says to check it to confirm this fault.
- sentence 5: support check: partial - The table shows an inverter specialist replaces the 24 VDC supply for inverter controls as needed, and a board replacement instruction is cited, but the content of the manufacturer's instructions is not shown.
-->
