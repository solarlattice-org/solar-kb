---
id: prod:yaskawa-solectria-sgi-500-750xtm
type: Product
name: Solectria SGI 500/750XTM
aliases:
- SGI 500 750 XTM
- SGI 500-750XTM
- SGI 500XTM
- SGI 750XTM
- SGI XTM
- SGI XTM Series
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:yaskawa-solectria
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=h2
    h: 87f1216fd14c
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=h2
    h: d6fcd6b2c8ae
  review: drafted
- claim_id: c2
  rel: implements
  target: func:ground-fault-protection
  note: Reports DC GND Fault when a ground fault is detected in the PV array.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  review: drafted
- claim_id: c3
  rel: has_hazard
  target: hazard:ground-fault-energized-conductor
  note: On a DC GND Fault the manual warns not to touch the inverter, disconnects, combiners, modules
    or racking.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r3
    h: a84c1c42aef2
  review: drafted
  review_note: 'support check: partial - The passage warns not to touch equipment on a ground fault, which
    implies a shock hazard, but it never says conductors are energized.'
- claim_id: c4
  attr: rated_power
  value:
    nominal: 500
    unit: unit:KiloW
  conditions: SGI 500XTM, continuous power at nominal operating voltage and power factor 1.0
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=36.r1
    h: 10e3319bbc33
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=35.r9
    h: 5ce5e62443b5
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c5
  attr: rated_power
  value:
    nominal: 750
    unit: unit:KiloW
  conditions: SGI 750XTM, continuous power at nominal operating voltage and power factor 1.0
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=36.r1
    h: 10e3319bbc33
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=35.r9
    h: 5ce5e62443b5
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c6
  attr: rated_output_current
  value:
    max: 760
    unit: unit:A
  conditions: SGI 500XTM, maximum continuous AC current
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=36.r2
    h: c993301dea6f
  review: drafted
- claim_id: c7
  attr: rated_output_current
  value:
    max: 1140
    unit: unit:A
  conditions: SGI 750XTM, maximum continuous AC current
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=36.r2
    h: c993301dea6f
  review: drafted
- claim_id: c8
  attr: nominal_voltage
  value:
    nominal: 380
    unit: unit:V
  conditions: Nominal AC operating voltage, both SGI 500XTM and SGI 750XTM
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=36.r3
    h: ad2e3f9bff90
  review: drafted
- claim_id: c9
  attr: max_input_voltage
  value:
    max: 1000
    unit: unit:V
  conditions: Absolute maximum DC voltage, both models
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=35.r1
    h: a633607836f0
  review: drafted
- claim_id: c10
  attr: max_input_current
  value:
    max: 965
    unit: unit:A
  conditions: SGI 500XTM, maximum DC operating current (total DC input)
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=35.r4
    h: 02143691d29f
  review: drafted
- claim_id: c11
  attr: max_input_current
  value:
    max: 1445
    unit: unit:A
  conditions: SGI 750XTM, maximum DC operating current (total DC input)
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=35.r4
    h: 02143691d29f
  review: drafted
---
The Solectria SGI 500/750XTM is a utility-scale grid-tied central inverter family from Yaskawa Solectria Solar, made up of the SGI 500XTM and SGI 750XTM. The SGI 500XTM delivers 500 kW continuous and the SGI 750XTM 750 kW, at a nominal AC voltage of 380 V with an operating range of 335 to 418 VAC. Both models accept up to 1000 VDC and operate on the DC side from 545 to 1000 VDC. The inverter connects through an external isolation transformer, and the manual points to a separate transformer specification. Output current is limited so it matches nameplate power at nominal AC voltage, so full power is not reached when grid voltage is low; current and power limiting behaviour can be configured. Cooling is automatic forced convection, and the default power factor is 1.0. Fault messages include DC GND Fault, Contactor Fail, CT Failure and DC Cont. Err. If you see a ground fault, do not touch any equipment and call a qualified person.

<!-- review notes
- sentence 1: support check: partial - The passages support the two models and the maker, but 'utility-scale' and 'central inverter' are not stated in them.
- sentence 4: support check: partial - The passages point to an isolation transformer specification, but they do not say the inverter connects through an external transformer. The datasheet URL contains 'externaltransformer', which only hints at this.
-->
