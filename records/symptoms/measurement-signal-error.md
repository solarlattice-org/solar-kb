---
id: symptom:measurement-signal-error
type: Symptom
name: Measurement signal error
aliases:
- Measurement error
- Error Meas V
- Error Meas F
- Error Meas Ileak
- Error during measuring signal detection
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Displayed as status or event codes, e.g. Fronius 458/459 (measuring signal detection, including
    for the insulation test), SMA SC-CP-XT 6441/6453, and SMA event messages labelled 'Measurement error'
    (grid current sensor offset, grid voltage measurement offset or deviation, DC voltage measurement
    deviation, insulation resistance sensor, temperature sensors).
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r15
    h: eebb84ba551d
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r28
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r29
    h: 528be01c279e
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r30
    h: 8e524a6224d5
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r7
    h: 34f3ba16cfab
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r1
    h: 785d03abb123
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: FIMER UNO-DM inverters light the Alarm LED for E027 Error Meas V, E028 Error Meas F and E030 Error
    Meas Ileak, which flag a mismatch between two redundant internal measurement circuits.
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r9
    h: 0911c8537c35
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r1
    h: a5a70a4f9522
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r9
    h: 0911c8537c35
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r3
    h: 14bb49350fa0
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: observed_as
  target: meas:zero-ac-output
  note: For Fronius Symo code 458, the inverter stops feeding current into the grid.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r29
    h: 528be01c279e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Code 458 stopping feed-in is stated, but the passage doesn''t
    state that power or current fall to zero, nor the signal behaviour.'
- claim_id: c4
  rel: observed_as
  target: meas:analog-input-error-led
  note: On an analog input terminal, a red channel error LED means a wire break or a value outside the
    allowed measurement range.
  cite:
  - src: src:sma-doc-edmm-wago-io-ia-en-11
    loc: tbl=17
    h: ef66b5f50a63
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
A measurement signal error means the inverter could not get a valid internal reading. It shows up as a status or event code on the inverter display or in the event log. On Fronius units, code 458 means the measuring signal could not be detected, and the inverter stops feeding into the grid. Code 459 means the same failure during the insulation test. On SMA units, events marked as measurement errors point to the sensing chain. Examples are an offset on the grid current sensor, an offset or deviation in grid voltage or DC voltage measurement, or a fault in the insulation resistance or temperature sensors. On FIMER inverters, the Alarm LED lights with Error Meas V, F or Ileak. These codes mean two redundant internal circuits disagree on grid voltage, grid frequency or DC leakage current. Use the code text to tell the likely cause apart: a voltage sensor fault, a current sensor fault or a temperature sensor fault inside the inverter. For external analog inputs, a red channel LED means a wire break or a value outside the allowed range, so check the sensor wiring first. Internal measurement errors cannot be checked from outside. Switch the inverter off and on again, and if the error comes back, contact the manufacturer's service.

<!-- review notes
- sentence 1: support check: partial - Codes shown as status or event messages are supported, but the claim that the inverter 'could not get a valid internal reading' is a generalisation the passages don't state as such.
- sentence 5: support check: partial - The code texts do name voltage sensor, current sensor and temperature sensor faults, but the passages don't state that the text can be used to tell the likely cause apart.
- sentence 6: support check: partial - The red LED meaning is stated, but the advice to check sensor wiring first is not in the passage.
- sentence 1: review: partial - The passages show these errors as status or event codes, but nothing says they mean the inverter could not get a valid internal reading; that wording is a generalisation.
-->
