---
id: symptom:ac-dc-power-deviation
type: Symptom
name: AC DC power deviation
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ac-dc-power-mismatch
  note: Reported by Sunny Central CP XT as error 6486 when the deviation between AC power and DC power
    exceeds what the inverter allows. The behavior columns S1 and S2 are both marked W; the source gives
    no corrective measure.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r15
    h: 5978a17eb8a1
  review: drafted
---
This symptom means the central inverter has found that its measured AC output power and DC input power differ by more than it allows. On the Sunny Central CP XT it shows up as error number 6486, and both inverter behavior columns, S1 and S2, are marked W. The manufacturer table gives no corrective measure for this error, and the sources name no specific failure mode behind it. Inverter AC power and DC power are standard monitoring channels, so comparing the two trends is how the mismatch is seen in the data.

<!-- review notes
- sentence 2: support check: partial - Error 6486 and S1/S2 = W are stated, but the passage doesn't name the Sunny Central CP XT model.
- sentence 4: review: partial - The IEA table lists AC power and DC power as monitoring parameters, but neither passage says that comparing their trends is how the mismatch shows up in the data.
-->
