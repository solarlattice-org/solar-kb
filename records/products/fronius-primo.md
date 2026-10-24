---
id: prod:fronius-primo
type: Product
name: Fronius Primo 208-240
aliases:
- Primo 208-240
category: Inverters
make: fronius
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  note: Certified as a permanently connected, transformerless utility-interactive inverter
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: sec=h425
    h: 9dd6f27cca31
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: sec=h429
    h: b9d9da5b4afd
  review: drafted
- claim_id: c2
  rel: implements
  target: func:reverse-polarity-protection
  note: Listed as integrated in the technical data
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=16.r5
    h: 795ffe655357
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=35.r15
    h: 86dff7217b89
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=51.r12
    h: e6dc6cf31763
  review: drafted
- claim_id: c3
  rel: implements
  target: func:anti-islanding
  note: Listed as integrated stand-alone operation protection
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=16.r4
    h: c9e2468f5e69
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=13.r22
    h: bf981d97f2ff
  review: drafted
- claim_id: c4
  rel: implements
  target: func:insulation-monitoring
  note: Listed as integrated for the 8.2-1 and 10.0-1 models
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=35.r13
    h: d235890cc219
  review: drafted
- claim_id: c5
  attr: max_input_voltage
  value:
    nominal: 1000
    unit: unit:V
  conditions: Open-circuit at 14 °C (57.2 °F); models 3.8-1, 5.0-1 and 6.0-1 208-240
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49
    h: 808b571b3676
  review: drafted
- claim_id: c6
  attr: mppt_voltage_range
  value:
    min: 200
    max: 800
    unit: unit:V
  conditions: Model 3.8-1 208-240
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49.r2
    h: 2c9bc24620cc
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49
    h: 808b571b3676
  review: drafted
- claim_id: c7
  attr: mppt_voltage_range
  value:
    min: 240
    max: 800
    unit: unit:V
  conditions: Models 5.0-1 and 6.0-1 208-240
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49.r2
    h: 2c9bc24620cc
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49
    h: 808b571b3676
  review: drafted
- claim_id: c8
  attr: max_input_current
  value:
    nominal: 18
    unit: unit:A
  conditions: Per MPPT (MPPT1/MPPT2); models 3.8-1, 5.0-1 and 6.0-1 208-240
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49
    h: 808b571b3676
  review: drafted
- claim_id: c9
  attr: rated_power
  value:
    nominal: 3800
    unit: unit:W
  conditions: Model 3.8-1 208-240, nominal output power at 208, 220 and 240 V
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49
    h: 808b571b3676
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions)
- claim_id: c10
  attr: rated_power
  value:
    nominal: 5000
    unit: unit:W
  conditions: Model 5.0-1 208-240, nominal output power at 208, 220 and 240 V
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49
    h: 808b571b3676
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c11
    (same source; check the conditions)
- claim_id: c11
  attr: rated_power
  value:
    nominal: 6000
    unit: unit:W
  conditions: Model 6.0-1 208-240, nominal output power at 208, 220 and 240 V
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=49
    h: 808b571b3676
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions)
- claim_id: c12
  attr: nominal_voltage
  value:
    nominal: 208
    unit: unit:V
  conditions: Nominal grid voltage option (208 V/220 V/240 V)
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=14.r16
    h: d7a34512a909
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=12.r15
    h: f34f097068bb
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=53.r11
    h: 850aa8d77113
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions)
- claim_id: c13
  attr: nominal_voltage
  value:
    nominal: 220
    unit: unit:V
  conditions: Nominal grid voltage option (208 V/220 V/240 V)
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=14.r16
    h: d7a34512a909
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=12.r15
    h: f34f097068bb
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=53.r11
    h: 850aa8d77113
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions)
- claim_id: c14
  attr: nominal_voltage
  value:
    nominal: 240
    unit: unit:V
  conditions: Nominal grid voltage option (208 V/220 V/240 V)
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=14.r16
    h: d7a34512a909
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=12.r15
    h: f34f097068bb
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=53.r11
    h: 850aa8d77113
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions)
- claim_id: c15
  attr: efficiency
  value:
    nominal: 96
    unit: unit:PERCENT
  conditions: CEC efficiency, model 3.8-1 208-240 at 208 V
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=13.r11
    h: 132b609e3ee5
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c18 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)
- claim_id: c16
  attr: efficiency
  value:
    nominal: 95.5
    unit: unit:PERCENT
  conditions: CEC efficiency, model 3.8-1 208-240 at 220 V and 240 V
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=13.r11
    h: 132b609e3ee5
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c18 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)
- claim_id: c17
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: CEC efficiency, models 5.0-1 and 6.0-1 208-240 at 208, 220 and 240 V
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=13.r11
    h: 132b609e3ee5
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c18 (same source; check the conditions)
- claim_id: c18
  attr: efficiency
  value:
    nominal: 97
    unit: unit:PERCENT
  conditions: CEC efficiency, models 7.6-1 and 8.2-1 208-240 at 208, 220 and 240 V
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=15.r14
    h: ef2e362a7d8a
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c17 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)
- claim_id: c19
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: CEC efficiency, model 10.0-1 208-240 at 208, 220 and 240 V
  cite:
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: tbl=15.r14
    h: ef2e362a7d8a
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c18 (same source; check the conditions)
---
The Fronius Primo 208-240 is a family of transformerless, utility-interactive inverters for permanent connection. CSA lists it as certified to U.S. standards. The certified models are 3.8-1, 5.0-1, 6.0-1, 7.6-1, 8.2-1, 10.0-1, 11.4-1, 12.5-1 and 15.0-1. The inverter connects to a 208 V, 220 V or 240 V nominal grid. The grid voltage tolerance is -12 % to +10 %. CEC efficiency ranges from 95.5 % to 97.0 %, depending on the model and the grid voltage. Reverse polarity protection and stand-alone operation (anti-islanding) protection are built in. Insulation monitoring is listed as built in on the 8.2-1 and 10.0-1 models. At high temperature the inverter protects itself by shifting its operating point and using active cooling.
