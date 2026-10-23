---
id: method:dc-voltage-measurement
type: DetectionMethod
name: DC voltage measurement
claims:
- claim_id: c1
  rel: produces
  target: meas:high-dc-input-voltage
  note: Measured at the inverter test points with the DC switch off; a high reading points to the string
    configuration.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14
    h: 050063b1c3a4
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: produces
  target: meas:meter-display-mismatch
  note: When the meter reading differs from the inverter LCD value, the inverter's measurement circuit
    may be faulty. Applies to OV-DC, OV-BUS and UN-BUS.
  quote: Check LCD reading, may be a bad measurement circuit
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14
    h: 050063b1c3a4
  review: drafted
  review_note: 'review: partial - Only OV-DC links the LCD reading to a possible bad measurement circuit;
    OV-BUS and UN-BUS just say to compare with the LCD and replace the inverter, so the note''s ''applies
    to OV-DC, OV-BUS and UN-BUS'' scope goes beyond the passages.'
- claim_id: c3
  rel: produces
  target: meas:zero-dc-voltage
  note: If the DC voltage reads zero with the DC switch on, the guidance is to replace the inverter.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13
    h: e3da18e1612c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
For an OV-DC alarm, first check the DC voltage at the inverter test points with the DC switch off. If the reading is high, check the string configuration. Next, turn the DC switch on and compare your reading with the inverter LCD. If the two disagree, the inverter's measurement circuit may be bad and the inverter may need replacing. For OV-BUS and UN-BUS bus voltage alarms, measure both DC and AC voltages and compare them with the LCD. Possible causes are internal damage or a wire that came loose during shipping. To verify the DC configuration, note how many panels are in each string and record the string voltage. Inverter-level measurements of DC input voltage are typically accurate to within ±2%, so treat small differences with care. Safety: on units with the automatic PID function, the PID module applies 450 Vdc between PV negative and ground when the DC bus voltage drops below 50 Vdc.

<!-- review notes
- sentence 4: support check: partial - Passage says to note panels per string and string voltage; 'record' is a mild paraphrase but fine, though the statement is essentially stated—minor wording difference only.
- sentence 5: support check: partial - The passage gives ±2% for inverter-level DC voltage measurement, but 'typically' and the advice to treat small differences with care are not stated.
-->
