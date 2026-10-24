---
id: concept:no-load-losses
type: Concept
name: No-load losses
aliases:
- standby consumption
- night consumption
- tare loss
- self-consumption of the inverter
- core loss
- iron loss
- no load watt losses
- Consumption at night
category: Inverters
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: comp:mv-transformer
  note: Transformer no-load loss is the power needed to keep the core energized whenever the unit is energized,
    independent of load.
  cite:
  - src: src:book-electric-power-transformer-engineering
    loc: sec=2.4.2
    h: 21cf4ce443a5
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h241
    h: 71e4ad8db85f
  - src: src:book-electric-power-transformer-engineering
    loc: sec=16.6.1.2
    h: 8abd2fa224c5
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=16.r2
    h: b194ac415d91
  review: drafted
- claim_id: c2
  rel: related_to
  target: state:standby
  note: Inverter datasheets list power drawn in standby or energy-saving mode.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=87.r1
    h: 0c711f48d1dd
  - src: src:sma-doc-278742
    loc: tbl=90.r1
    h: f2f0422b49f8
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=39.r6
    h: b09ca0df18f4
  review: drafted
- claim_id: c3
  rel: related_to
  target: state:sleep
  note: Inverters draw a small amount of power at night while disconnected from the grid.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=18
    h: f317d214c940
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=39.r6
    h: b09ca0df18f4
  review: drafted
- claim_id: c4
  rel: related_to
  target: prod:sma-sunny-island
  note: Manual lists consumption in no-load operation and in standby or energy-saving mode.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=87.r1
    h: 0c711f48d1dd
  - src: src:sma-doc-259761
    loc: tbl=87.r2
    h: bd43251586b4
  - src: src:sma-doc-278742
    loc: tbl=90.r1
    h: f2f0422b49f8
  review: drafted
---
No-load losses are the power a device draws just to stay energized, even when it delivers no load. In a transformer, this is mostly core loss, also called iron loss, made up of hysteresis and eddy-current losses in the core steel, plus small dielectric and excitation-current losses. These losses are present whenever the transformer is energized and depend mainly on voltage and frequency, so they stay nearly constant while load losses rise with the square of load current. Total transformer losses are the sum of no-load losses and load losses, and transformer loss tables give no-load figures such as 510 W to 1100 W for a 500 kVA unit, depending on loss class. For inverters, datasheets give the same idea as standby, night or no-load consumption, or as tare loss.

<!-- review notes
- sentence 4: support check: partial - Sum of no-load and load losses and the 510–1100 W values are given, but 'depending on loss class' is only implied by the A0–E0 labels; the table doesn't explicitly say loss class.
- sentence 1: review: partial - The passages define no-load loss only for transformers (the power to keep the core energized while not supplying load), so widening it to any device goes beyond them.
-->
