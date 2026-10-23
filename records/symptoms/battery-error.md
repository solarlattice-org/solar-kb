---
id: symptom:battery-error
type: Symptom
name: Battery error reported
aliases:
- Error in the battery
claims:
- claim_id: c1
  rel: observed_as
  target: meas:bms-error-message
  note: On Sunny Island, W945 (level 1 warning) and F929 (level 3 error) report an error in the battery
    that the external battery management sends over SiCom.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r12
    h: 0690c4cd2d74
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156
    h: c6b09b8dcebc
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155
    h: 9ec13aab83bd
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:battery-voltage-range-message
  note: A battery error can be raised when the battery voltage the Sunny Island measures is above or below
    the permissible measurement range.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h923
    h: 5d8212cb9c4f
  - src: src:sma-doc-278742
    loc: sec=h929
    h: da73424e5c91
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:battery-temperature-status-high
  note: A battery error can be raised when the battery goes above the upper temperature limit approved
    by the battery manufacturer.
  cite:
  - src: src:sma-doc-278742
    loc: tbl=76.r8
    h: 47c577197df0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The Sunny Island shows a battery error as warning W945, or as error F929 at the higher level, when the external battery management reports a fault over SiCom. For errors reported over SiCom, find and clear the cause in the external battery management system, following the battery manufacturer's documentation. Other causes of a battery error include a timeout of the battery management link, a temperature above the manufacturer's upper limit, and external battery management that was detected but never configured. A battery error can also mean the battery has worn: its current capacity (SOH) is below 70%, or its measured voltage is out of range, possibly because aging has left too little usable capacity. The error can also appear when a battery protection mode is active, or after a state-of-charge recalibration that made a large jump. Check first that the data cable to the external lithium-ion battery is connected correctly, and that the battery's ambient conditions are within the manufacturer's limits. Then check that the error message is plausible, and replace the battery if needed.

<!-- review notes
- sentence 2: support check: partial - The passage covers only F929 (error in the battery) and not all SiCom errors, though the corrective measure matches.
- sentence 6: support check: partial - Both corrective measures are stated, but they are separate fixes for different causes, and nothing says to check them first.
- sentence 7: support check: partial - Verifying plausibility and replacing the battery if necessary are stated, but the passages don't say this comes after the earlier checks or tie it to this battery error.
- sentence 4: review: partial - SOH below 70% and voltage above or below the measurement range are stated, but the passages tie aging only to the below-range case, while the sentence applies it to any out-of-range voltage and calls it all 'worn'.
- sentence 7: review: partial - Checking that the message is plausible and replacing the battery if needed are stated, but the order implied by 'Then', after the earlier checks, is not in the passages.
-->
