---
id: concept:soc-estimation
type: Concept
name: SoC estimation methods
aliases:
- coulomb counting
- ampere-hour counting
- open-circuit voltage method
- Voltage recalibration
- OCV
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: explains
  target: concept:state-of-charge
  note: SoC cannot be measured directly; it is estimated from measurable values, algorithms and parameter
    settings.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h8
    h: 039ffcdcd5a7
  - src: src:sma-doc-260329
    loc: sec=1.2
    h: 0872223561b6
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  review: drafted
- claim_id: c2
  rel: related_to
  target: method:soc-error-monitoring
  note: SMA reports the estimated SoC error as parameter BatSocErr; it is lowest after a full or equalization
    charge.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h8
    h: 039ffcdcd5a7
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=25.r3
    h: 58efa1b1df44
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=123.r2
    h: 97cdadc0f4ec
  review: drafted
- claim_id: c3
  rel: related_to
  target: mit:battery-soc-recalibration
  note: Voltage recalibration corrects the counted SoC using battery voltage; an expert-mode option recalibrates
    on open-circuit voltage only.
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=179.r2
    h: 7349a31dd4f3
  - src: src:sma-doc-260329
    loc: sec=1.2
    h: 0872223561b6
  - src: src:sma-kb-battery-state-of-charge-soc-for-valve-regulated-lead-acid-vrla-batteries-and-how-it
    loc: sec=h1
    h: 97975a361947
  review: drafted
- claim_id: c4
  rel: related_to
  target: symptom:soc-jump
  note: Small jumps come from normal recalibration; large or fast jumps point to wrong settings, early
    battery aging or battery errors.
  cite:
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  review: drafted
- claim_id: c5
  rel: related_to
  target: mit:equalization-charge
  note: Recommended first action when SoC deviations occur; also resets the estimated SoC error to its
    minimum.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h8
    h: 039ffcdcd5a7
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  review: drafted
- claim_id: c6
  rel: related_to
  target: method:battery-capacity-test
  note: Only capacity tests give actual SoC and SoH, but most field applications cannot perform them.
  cite:
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:state-of-health
  cite:
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:lead-acid-battery
  note: Full-charge detection relies on the typical charging characteristic of lead-acid batteries.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h8
    h: 039ffcdcd5a7
  - src: src:sma-kb-battery-state-of-charge-soc-for-valve-regulated-lead-acid-vrla-batteries-and-how-it
    loc: sec=h1
    h: 97975a361947
  review: drafted
- claim_id: c9
  rel: related_to
  target: concept:lithium-iron-phosphate
  note: A LiFePO4 tracker controller battery uses OCV plus Coulomb counting for SoC.
  cite:
  - src: src:eq-equip-trackers-solar-flexrack-solar-flexrack-self-powered-solution-for-tdp-solar-trackers-040918
    loc: tbl=1
    h: 9f6135bdf6e8
  review: drafted
- claim_id: c10
  rel: related_to
  target: prod:sma-sunny-island
  note: Sunny Island acts as BMS for VRLA batteries and combines ampere-hour counting with voltage recalibration.
  cite:
  - src: src:sma-doc-260329
    loc: sec=1.2
    h: 0872223561b6
  - src: src:sma-kb-battery-state-of-charge-soc-for-valve-regulated-lead-acid-vrla-batteries-and-how-it
    loc: sec=h1
    h: 97975a361947
  review: drafted
- claim_id: c11
  rel: related_to
  target: prod:solar-flexrack-tdp
  cite:
  - src: src:eq-equip-trackers-solar-flexrack-solar-flexrack-self-powered-solution-for-tdp-solar-trackers-040918
    loc: tbl=1.r6
    h: b18e054d9fb2
  - src: src:eq-equip-trackers-solar-flexrack-solar-flexrack-self-powered-solution-for-tdp-solar-trackers-040918
    loc: tbl=1
    h: 9f6135bdf6e8
  review: drafted
---
SoC estimation methods are the algorithms a battery inverter or BMS uses to work out how full a battery is, because state of charge cannot be measured directly. Ampere-hour counting, also called Coulomb counting, integrates the battery current over time. On its own it drifts, because the starting SoC is usually unknown and the DC current measurement is not accurate enough. To limit this drift, SMA's version also estimates the battery's internal leakage current and uses full-charge detection, which looks at temperature, voltage, charging current and time and lets the algorithm learn and adjust its parameters. The Sunny Island reports its estimated SoC error as BatSocErr. The error is lowest right after a full or equalization charge and grows again over the following cycles. Small SoC jumps during recalibration are normal. Large or fast jumps suggest wrong settings, early battery aging or a battery error, and the first step SMA recommends is an equalization charge. Wrong installation or parameter settings make SoC and state of health estimates less accurate. Only a capacity test gives the true values, and most field sites cannot run one.
