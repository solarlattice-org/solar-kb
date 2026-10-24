---
id: concept:power-factor-penalty
type: Concept
name: Utility power factor penalty
aliases:
- low power factor penalty
- power factor charge
- power factor penalties
- utility-reactive energy fee
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:power-factor
  note: The penalty is charged when the customer's power factor is low.
  cite:
  - src: src:book-electric-power-system-basics
    loc: sec=h209
    h: 63df79f32c05
  - src: src:sma-kb-low-power-factor-with-solar-in-operation
    loc: sec=h1
    h: e55db763231e
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-integrated-volt-var
    loc: sec=h1
    h: 43c4cc3004db
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:reactive-power
  note: Utilities bill only real power, so penalties cover the reactive power they supply; penalties scale
    with that reactive power.
  cite:
  - src: src:book-electric-power-system-basics
    loc: sec=h209
    h: 63df79f32c05
  - src: src:sma-kb-low-power-factor-with-solar-in-operation
    loc: sec=h1
    h: e55db763231e
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-integrated-volt-var
    loc: sec=h1
    h: 43c4cc3004db
  review: drafted
- claim_id: c3
  rel: related_to
  target: meas:low-meter-power-factor
  note: With PV feeding at unity power factor, grid active power falls while reactive draw stays the same,
    so the grid-point meter records a lower power factor and the customer can be penalized.
  cite:
  - src: src:sma-kb-low-power-factor-with-solar-in-operation
    loc: sec=h1
    h: e55db763231e
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:constant-power-factor
  note: 'One fix: set the inverter power factor to the plant''s no-solar value, with the direction opposite
    to the plant power factor.'
  cite:
  - src: src:sma-kb-low-power-factor-with-solar-in-operation
    loc: sec=h1
    h: e55db763231e
  review: drafted
  review_note: 'support check: partial - u16 says set inverter PF equal to the no-solar value with opposite
    direction, but doesn''t name constant power factor mode explicitly; core is stated.'
- claim_id: c5
  rel: related_to
  target: concept:harmonic-distortion
  note: Harmonics from non-linear loads lower the true power factor even more.
  cite:
  - src: src:sma-kb-low-power-factor-with-solar-in-operation
    loc: sec=h1
    h: e55db763231e
  review: drafted
- claim_id: c6
  rel: related_to
  target: proto:modbus
  note: An external controller can adjust inverter PF and Q setpoints over Modbus as conditions change.
  cite:
  - src: src:sma-kb-low-power-factor-with-solar-in-operation
    loc: sec=h1
    h: e55db763231e
  review: drafted
- claim_id: c7
  rel: related_to
  target: comp:energy-meter
  note: The meter at the grid connection point measures power factor; a billing meter can compute an average
    power factor over the billing period.
  cite:
  - src: src:book-electric-power-system-basics
    loc: sec=h209
    h: 63df79f32c05
  - src: src:sma-kb-low-power-factor-with-solar-in-operation
    loc: sec=h1
    h: e55db763231e
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285a
    loc: sec=6.1
    h: 9cf8a5029258
  review: drafted
  review_note: 'support check: partial - Grid-connection-point meter PF is supported (u16) and billing-period
    average PF by KV2C (u28), but u28 doesn''t link to penalties and ''billing meter'' framing is loose.'
---
A power factor penalty is an extra charge some utilities add to a customer's bill when the site has a low power factor or draws a lot of reactive power. Utilities have to supply both real and reactive power but bill customers only for real power, so penalties recover the cost of the reactive power. The penalty grows with the amount of reactive power supplied. Inductive loads such as motors, transformers, pumps and air conditioners need reactive power, and that pulls the power factor down. Adding PV can make the problem worse. An inverter running at unity power factor reduces the active power taken from the grid, but the reactive power drawn stays the same, so the meter at the grid connection point reads a lower power factor. The penalty can also come from PV output that bypasses the feedback of an automatic power factor correction panel, or from harmonic distortion caused by non-linear loads. Fixes include capacitors installed on the customer side of the meter, sending PV output through the correction feedback, and setting a power factor on the inverters. An external controller can also adjust inverter PF and reactive power over Modbus. Not every utility charges for low power factor. Where the utility installs the capacitors itself, the customer still pays a reactive energy fee.
