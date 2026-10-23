---
id: symptom:supply-voltage-invalid
type: Symptom
name: Invalid internal supply voltage
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA Sunny Central CP XT reports error 6410 when the 24 V supply voltage is invalid and error 6417
    when the 15 V supply voltage is invalid.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r14
    h: 13a490385233
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r13
    h: 29a79d604337
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
On SMA Sunny Central CP XT inverters, this symptom appears as error 6410 when the 24 V internal supply voltage is invalid, and as error 6417 when the 15 V supply voltage is invalid. For both errors, the inverter behavior table gives a 5 min entry in the S1 and S2 columns. SMA systems with a Multicluster Box have a related event, 6466, which reports a system failure because the 15 V or 24 V voltage supply in the box is defective. These messages point to a defect in the device's own low-voltage supply, which suggests an internal power supply fault rather than a PV array or grid problem. The documentation gives no field repair: write down the error number and contact the SMA Service Line.

<!-- review notes
- sentence 4: support check: partial - Passages show the supply voltage is invalid or defective, but they do not say it is an internal fault rather than a PV array or grid problem; that is an inference.
- sentence 5: support check: partial - Passages say to contact Service and give no other corrective measure, but they do not say to write down the error number.
- sentence 4: review: partial - The rows show the 15 V and 24 V supplies are invalid or defective, but the contrast with a PV array or grid problem is an inference the passages do not state.
-->
