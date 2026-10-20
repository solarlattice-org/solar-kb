---
id: symptom:high-leakage-current
type: Symptom
name: High leakage current
aliases:
- Excess Leakage Current
- Excessive leakage current
- GFCI.Err
claims:
- claim_id: c1
  rel: observed_as
  target: meas:high-leakage-current-alarm
  note: 'Inverters report this as a fault: Sungrow fault code 12 (Excess or Excessive Leakage Current),
    and CPS/Solectria GFCI.Err, which is defined as system leakage current being too high. The trip limit
    (LeakCurMax) can be set on the inverter, but it is a protection setting and not a measured value.'
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=35.r11
    h: 38690c952bd4
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=41.r5
    h: 38690c952bd4
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r4
    h: 8b79a5df44df
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
  review_note: 'support check: partial - Sungrow code 12 and GFCI.Err definitions are supported, but the
    claim that LeakCurMax is a settable protection limit rather than a measured value is not in the passages.'
---
High leakage current usually shows up as an inverter protection fault, such as Sungrow fault 12 or a GFCI error that means system leakage current is too high. Weak sunlight or a damp environment can trigger this fault, and the inverter normally reconnects to the grid once conditions improve. If the fault appears in normal conditions, first check that the AC and DC cables are well insulated, and contact the manufacturer if the fault continues. Poor insulation in a module lets current leak to the frame. That costs no power until the inverter faults, but anyone touching uninsulated parts of the string or frame can get an electric shock. High voltage between modules and ground can also drive the leakage current behind potential induced degradation, which cuts string and module power substantially. In some cases it comes with corrosion and delamination. System voltage, inverter topology, array polarity at night and the grounding concept all affect how much leakage current flows. To tell potential induced degradation apart from a plain insulation fault, look for its signatures with electroluminescence imaging, thermography, IV tracing and Voc checks.

<!-- review notes
- sentence 1: support check: partial - Passages show Sungrow 12 and GFCI.Err as leakage faults, but nothing says high leakage 'usually' shows up as an inverter protection fault.
- sentence 7: support check: partial - The detection methods (EL, thermography, IV tracing, Voc) are listed to confirm PID and separate it from other module defects, but 'plain insulation fault' is not specifically mentioned.
-->
