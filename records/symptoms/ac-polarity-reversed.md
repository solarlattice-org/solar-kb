---
id: symptom:ac-polarity-reversed
type: Symptom
name: AC polarity reversed
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Primo and Symo show status code 463 for reversed AC polarity, which the manuals put down
    to an incorrectly plugged AC connector.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r32
    h: 2014e3ab07d3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r34
    h: 2014e3ab07d3
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
Fronius Primo and Symo inverters show status code 463 when they detect reversed AC polarity. Both manuals give the cause as an AC connector that was plugged in incorrectly, so this points to a wiring or installation fault on the AC side, not a failed part. Check first how the AC connector at the inverter is plugged in and which way it faces, then reconnect it correctly. Do not confuse this with reversed DC string polarity: the Fronius Symo reports that under its own status code, 311.

<!-- review notes
- sentence 2: support check: partial - Cause (incorrectly plugged AC connector) is stated, but the inference that it is an installation fault and not a failed part is not stated.
- sentence 3: support check: partial - Passages only state the connector was plugged in incorrectly; the check-and-reconnect instruction and 'which way it faces' are not stated.
- sentence 4: support check: partial - Code 311 is DC strings polarity reversed, but the passage doesn't specify Fronius Symo only or the 'don't confuse' advice.
-->
