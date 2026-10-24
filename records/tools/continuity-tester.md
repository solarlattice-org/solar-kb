---
id: tool:continuity-tester
type: Tool
name: Continuity tester
aliases:
- continuity test
- earth-bond continuity
- Earth Continuity Resistance Measurement
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  attr: accuracy
  value:
    nominal: 2
    unit: unit:PERCENT
  scope:
    products:
    - prod:seaward-pv200-210
  conditions: Earth continuity resistance function of the Seaward PV200 on 4 mm terminals; specified as
    plus or minus 2% plus 5 digits, measuring range 0.05 to 199 ohm per EN 61557-4
  cite:
  - src: src:test-testing-tools-seaward-pv200-seaward-pv200-specs
    loc: sec=h10
    h: b72ac2ba5822
  review: drafted
---
A continuity tester checks that a conductor or bond forms an unbroken electrical path, which in practice shows you are connected to both ends of the same cable. In PV work it is mainly used to check grounding and bonding: module frames, racking, enclosures, raceways and the grounding electrode conductor all have to be bonded to the earthing system. You can use a low-resistance ohmmeter or the continuity function of a digital multimeter, which gives a pass or fail result such as an audible beep. Some PV testers show a red backlight and an X when a test fails. Null or zero the test lead resistance before measuring, and make sure the leads clip onto clean surfaces. Extra-long leads are often needed because PV components can be far apart. A simple 2-wire continuity test picks up lead and contact resistance. For a rigorous proof of a bond, use a dedicated low-resistance ohmmeter with high test current, because that can reveal corrosion and loose joints. Only test circuits and conductors that are de-energized. Some instruments warn you and block the test when 30 V or more is present at the inputs.

<!-- review notes
- sentence 5: support check: partial - Passages support 2-wire sensitivity to lead/contact resistance and dedicated low-resistance ohmmeter (10 A or more) revealing corrosion and loose connections, but they say the 4-wire low-resistance test reveals joint issues, not the 2-wire claim in exactly these terms; high current is stated, though 'picks up lead and contact resistance' is implied.
-->
