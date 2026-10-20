---
id: meas:update-condition-test-failed
type: Measurement
name: Update condition test failed
aliases:
- Condition test failed
---
This signature is SMA inverter event number 7330, which appears in the event log with the message Condition test failed. It means the inverter checked the conditions for a firmware update and the check did not pass. According to the manual, the cause is a firmware update package that is not suitable for this inverter. The same part of the event table lists other update events: 7331 means the update file is being copied, and 7332 means the copy to the inverter's internal memory succeeded. A different update event, 7106, reports a defective update file. That update fails, but the inverter keeps feeding in. There is also a separate message for a failed bootloader update, so check which update step is actually reported.

<!-- review notes
- sentence 6: support check: partial - A 'Update Bootloader failed' message exists, but the passages give no event number or advice to check which update step is reported (advice is a minor inference).
-->
