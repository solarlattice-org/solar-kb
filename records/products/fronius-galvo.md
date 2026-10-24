---
id: prod:fronius-galvo
type: Product
name: Fronius Galvo 208-240
aliases:
- Fronius Galvo
- Galvo 208-240
- Fronius Galvo Series
category: Inverters
make: fronius
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fronius
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-installation-emanual
    loc: sec=front
    h: c05dac2856ae
  review: drafted
- claim_id: c2
  rel: implements
  target: func:dc-arc-fault-protection
  note: Arc fault circuit interrupter listed as integrated on all four models.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=10
    h: 415190ef3287
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=13
    h: 1de42085b4ce
  review: drafted
- claim_id: c3
  rel: implements
  target: func:ground-fault-protection
  note: Internal GFDI (ground fault detector/interrupter).
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=13
    h: 1de42085b4ce
  review: drafted
- claim_id: c4
  rel: implements
  target: func:anti-islanding
  note: Listed as integrated stand-alone operation protection.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=13
    h: 1de42085b4ce
  review: drafted
  review_note: 'support check: partial - Stand-alone operation protection is listed as integrated, which
    is islanding protection in effect, but the passages never say anti-islanding explicitly.'
- claim_id: c5
  rel: implements
  target: func:reverse-polarity-protection
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=13.r7
    h: bf007f1a7e9e
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9.r25
    h: 7ba75aac603a
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=13
    h: 1de42085b4ce
  review: drafted
- claim_id: c6
  rel: implements
  target: func:constant-power-factor
  note: Power factor adjustable from 0.85 inductive to 0.85 capacitive.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=39.r2
    h: df9af9061fd0
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
- claim_id: c7
  rel: implements
  target: func:frequency-trip
  note: Adjustable frequency limits with settable tolerance time.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
- claim_id: c8
  rel: implements
  target: func:voltage-trip
  note: Adjustable grid voltage limits with settable tolerance time (2.5-1 and 3.1-1 table).
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
- claim_id: c9
  attr: max_input_voltage
  value:
    nominal: 420
    unit: unit:V
  conditions: Fronius Galvo 1.5-1 and 2.0-1 208-240
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=38.r2
    h: 1ff9754543aa
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=38
    h: 144c2ad9a782
  review: drafted
- claim_id: c10
  attr: max_input_current
  value:
    nominal: 13.4
    unit: unit:A
  conditions: Fronius Galvo 1.5-1 208-240, DC input
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=38.r4
    h: 5062bc20506a
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=38
    h: 144c2ad9a782
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
- claim_id: c11
  attr: max_input_current
  value:
    nominal: 17
    unit: unit:A
  conditions: Fronius Galvo 2.0-1 208-240, DC input, 208 V column
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=38.r4
    h: 5062bc20506a
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=38
    h: 144c2ad9a782
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
- claim_id: c12
  attr: max_input_current
  value:
    nominal: 16.1
    unit: unit:A
  conditions: Fronius Galvo 2.5-1 208-240, DC input
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r1
    h: d2d068477ac3
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
- claim_id: c13
  attr: max_input_current
  value:
    nominal: 18.7
    unit: unit:A
  conditions: Fronius Galvo 3.1-1 208-240, DC input, 208 V column
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r1
    h: d2d068477ac3
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions); possible conflict with c12 (same source; check the conditions)
- claim_id: c14
  attr: rated_power
  value:
    nominal: 2500
    unit: unit:W
  conditions: Fronius Galvo 2.5-1 208-240, maximum continuous output power at 40 or 45 °C at nominal DC
    voltage, all grid voltages
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r14
    h: e320af602976
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r15
    h: 2898526ce85c
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions)
- claim_id: c15
  attr: rated_power
  value:
    nominal: 2930
    unit: unit:W
  conditions: Fronius Galvo 3.1-1 208-240 at 208 V, maximum continuous output power at 40 or 45 °C at
    nominal DC voltage
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r14
    h: e320af602976
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r15
    h: 2898526ce85c
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions)
- claim_id: c16
  attr: rated_output_current
  value:
    nominal: 12
    unit: unit:A
  conditions: Fronius Galvo 2.5-1 208-240, nominal output current at 208 V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c18 (same source; check the conditions); possible conflict with c19 (same source; check the conditions);
    possible conflict with c20 (same source; check the conditions)
- claim_id: c17
  attr: rated_output_current
  value:
    nominal: 11.4
    unit: unit:A
  conditions: Fronius Galvo 2.5-1 208-240, nominal output current at 220 V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c18 (same source; check the conditions); possible conflict with c19 (same source; check the conditions);
    possible conflict with c20 (same source; check the conditions)
- claim_id: c18
  attr: rated_output_current
  value:
    nominal: 10.4
    unit: unit:A
  conditions: Fronius Galvo 2.5-1 208-240, nominal output current at 240 V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c19 (same source; check the conditions);
    possible conflict with c20 (same source; check the conditions)
- claim_id: c19
  attr: rated_output_current
  value:
    nominal: 14.1
    unit: unit:A
  conditions: Fronius Galvo 3.1-1 208-240, nominal output current at 208 V and 220 V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c18 (same source; check the conditions);
    possible conflict with c20 (same source; check the conditions)
- claim_id: c20
  attr: rated_output_current
  value:
    nominal: 12.9
    unit: unit:A
  conditions: Fronius Galvo 3.1-1 208-240, nominal output current at 240 V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c18 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)
- claim_id: c21
  attr: nominal_voltage
  value:
    nominal: 208
    unit: unit:V
  conditions: Nominal AC output voltage, line-to-line setting
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=39.r6
    h: d33047951005
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r4
    h: 50b8d5c2df29
  review: drafted
  review_note: possible conflict with c22 (same source; check the conditions); possible conflict with
    c23 (same source; check the conditions)
- claim_id: c22
  attr: nominal_voltage
  value:
    nominal: 220
    unit: unit:V
  conditions: Nominal AC output voltage, line-to-line setting
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=39.r6
    h: d33047951005
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r4
    h: 50b8d5c2df29
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c23 (same source; check the conditions)
- claim_id: c23
  attr: nominal_voltage
  value:
    nominal: 240
    unit: unit:V
  conditions: Nominal AC output voltage, line-to-line setting
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=39.r6
    h: d33047951005
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=41.r4
    h: 50b8d5c2df29
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions)
- claim_id: c24
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Nominal output frequency, all models
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=39.r7
    h: b92254fe1a72
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
- claim_id: c25
  attr: frequency
  value:
    min: 45
    max: 65
    unit: unit:HZ
  conditions: Operating frequency range, all models
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
- claim_id: c26
  attr: efficiency
  value:
    nominal: 95.8
    unit: unit:PERCENT
  conditions: Maximum efficiency, Fronius Galvo 1.5-1 and 2.0-1 208-240
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  review: drafted
  review_note: possible conflict with c27 (same source; check the conditions); possible conflict with
    c28 (same source; check the conditions); possible conflict with c29 (same source; check the conditions);
    possible conflict with c30 (same source; check the conditions); possible conflict with c31 (same source;
    check the conditions)
- claim_id: c27
  attr: efficiency
  value:
    nominal: 96
    unit: unit:PERCENT
  conditions: Maximum efficiency, Fronius Galvo 2.5-1 and 3.1-1 208-240
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
  review_note: possible conflict with c26 (same source; check the conditions); possible conflict with
    c28 (same source; check the conditions); possible conflict with c29 (same source; check the conditions);
    possible conflict with c30 (same source; check the conditions); possible conflict with c31 (same source;
    check the conditions)
- claim_id: c28
  attr: efficiency
  value:
    nominal: 94
    unit: unit:PERCENT
  conditions: CEC efficiency, Fronius Galvo 1.5-1 208-240 at 208 V and 220 V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  review: drafted
  review_note: possible conflict with c26 (same source; check the conditions); possible conflict with
    c27 (same source; check the conditions); possible conflict with c29 (same source; check the conditions);
    possible conflict with c30 (same source; check the conditions); possible conflict with c31 (same source;
    check the conditions)
- claim_id: c29
  attr: efficiency
  value:
    nominal: 94.5
    unit: unit:PERCENT
  conditions: CEC efficiency, Fronius Galvo 1.5-1 at 240 V and Fronius Galvo 2.0-1 at 208, 220 and 240
    V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  review: drafted
  review_note: possible conflict with c26 (same source; check the conditions); possible conflict with
    c27 (same source; check the conditions); possible conflict with c28 (same source; check the conditions);
    possible conflict with c30 (same source; check the conditions); possible conflict with c31 (same source;
    check the conditions)
- claim_id: c30
  attr: efficiency
  value:
    nominal: 95
    unit: unit:PERCENT
  conditions: CEC efficiency, Fronius Galvo 2.5-1 at all voltages and 3.1-1 at 208 V and 220 V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
  review_note: possible conflict with c26 (same source; check the conditions); possible conflict with
    c27 (same source; check the conditions); possible conflict with c28 (same source; check the conditions);
    possible conflict with c29 (same source; check the conditions); possible conflict with c31 (same source;
    check the conditions)
- claim_id: c31
  attr: efficiency
  value:
    nominal: 95.5
    unit: unit:PERCENT
  conditions: CEC efficiency, Fronius Galvo 3.1-1 208-240 at 240 V
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=12
    h: 3cc5f08e70f0
  review: drafted
  review_note: possible conflict with c26 (same source; check the conditions); possible conflict with
    c27 (same source; check the conditions); possible conflict with c28 (same source; check the conditions);
    possible conflict with c29 (same source; check the conditions); possible conflict with c30 (same source;
    check the conditions)
- claim_id: c32
  attr: operating_temperature
  value:
    min: -40
    max: 50
    unit: unit:DEG_C
  conditions: Permitted ambient temperature at 95% relative humidity, all models
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9
    h: 2d12e3c56e20
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=13
    h: 1de42085b4ce
  review: drafted
---
The Fronius Galvo 208-240 is a family of single-phase utility-interactive string inverters made by Fronius, covering the 1.5-1, 2.0-1, 2.5-1 and 3.1-1 models. The output connects line-to-line at 208, 220 or 240 V and 60 Hz, and the 3.1-1 delivers up to 3100 W at 220 V and 240 V. Maximum efficiency is 95.8% on the smaller models and 96.0% on the larger ones. All models are rated for ambient temperatures from -40 to +50 °C. Built-in protection includes an internal GFDI, arc fault circuit interruption, anti-islanding protection and reverse polarity protection. Power factor can be adjusted down to 0.85 inductive or capacitive, and the voltage and frequency trip limits are adjustable. The enclosure is rated NEMA 4X and the unit uses forced-air cooling. At high temperature it protects itself by shifting its operating point. CSA listed the family for Canada and the US as a utility interactive inverter in 2014, and later updates added firmware revisions and alternative components.

<!-- review notes
- sentence 1: support check: partial - The passages support Fronius make, the four models and utility interactive inverter, but single-phase and string inverter are not stated; Phases is given as 2.
- sentence 2: support check: partial - Output voltages, frequency and 3100 W for 3.1-1 are shown, but the 3100 W columns are inferred as 220/240 V from column order and the 'up to' phrasing is an assumption.
- sentence 4: support check: partial - Internal GFDI, AFCI and reverse polarity protection are listed, but anti-islanding appears only as stand-alone operation protection, and AFCI is shown for all four models only via combined tables.
-->
