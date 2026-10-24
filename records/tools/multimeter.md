---
id: tool:multimeter
type: Tool
name: Digital multimeter
aliases:
- multimeter
- DMM
- voltmeter
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  attr: max_input_voltage
  value:
    min: 1000
    unit: unit:V
  conditions: Required DC voltage measurement range of the multimeter listed as an installation tool in
    a Huawei string inverter manual
  cite:
  - src: src:eq-equip-inverters-huawei-huawei-sun2000-33-36-40ktl-us-manual
    loc: tbl=19.r4
    h: 681947f37a33
  review: drafted
- claim_id: c2
  attr: max_input_voltage
  value:
    min: 1000
    unit: unit:V
  conditions: Required DC voltage rating of the multimeter for PV string ground-fault testing, to avoid
    overvoltage damage to the meter
  cite:
  - src: src:kb-solis-44002645683-how-to-detect-ground-faults-in-your-pv-system
    loc: sec=h2
    h: dffafac970e7
  review: drafted
- claim_id: c3
  attr: max_input_voltage
  value:
    min: 600
    unit: unit:V
  conditions: Alternative DC rating for ground-fault testing, only where a 600 V rating is specified
  cite:
  - src: src:kb-solis-44002645683-how-to-detect-ground-faults-in-your-pv-system
    loc: sec=h2
    h: dffafac970e7
  review: drafted
- claim_id: c4
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: CAT III digital multimeter rating required in Yaskawa Solectria service instructions
  cite:
  - src: src:yaskawa-solectria-yaskawa-customer-facing-instructions-full
    loc: sec=3.2
    h: ca6596a3c9ea
  review: drafted
---
A digital multimeter is a handheld test instrument. Inverter manuals list it as an installation tool for measuring cable voltages and AC or DC current. It is used for string polarity measurement on energized circuits before disconnects are closed for the first time. The display shows a plus or minus sign depending on how the leads are connected, and analog voltmeters should not be used for this test. In the PV-to-ground voltage test, it reads positive-to-ground and negative-to-ground voltage on an isolated string to confirm a ground fault and estimate where it is. Using two identical meters as a voltage divider gives a more precise location. Generac SnapRS devices cannot be function-tested in the field, but simple multimeter resistance checks can confirm their general health. Use a meter rated for the system voltage. Manuals call for at least 1000 V DC, or a 1500 V rated CAT III meter, because overvoltage can damage the meter and make its housing live. A standard multimeter cannot pick up very small differences in cable resistance. It read 0.00 ohm on good and bad cables that a milliohm meter could tell apart. Some models, such as insulation multimeters, combine a multimeter and an insulation tester in one handheld unit. Only qualified staff should do these tests. Wear proper PPE, isolate the string from the inverter and wait about 5 minutes for capacitive discharge before touching anything.

<!-- review notes
- sentence 1: support check: partial - Manuals list multimeters for measuring voltages and AC/DC amps, but 'handheld' is not stated in these passages.
- sentence 4: support check: partial - No functional field tests and DMM checks confirm general health are stated, but only a voltage-free resistance reading (~12 MΩ) appears, 'resistance checks' is mostly implied.
- sentence 5: support check: partial - Passages support ≥1000 V DC, 1500 V CAT III, and overvoltage damaging meter and energizing enclosure, but 'manuals call for at least 1000 V or 1500 V CAT III' conflates; mostly fine though 'make its housing live' matches; system-voltage rating generalization is inferred.
-->
