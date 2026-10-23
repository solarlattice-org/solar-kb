---
id: symptom:external-short-circuit
type: Symptom
name: External short circuit
aliases:
- ExtScirDet
---
An external short circuit makes the Sunny Island disconnect from the external source, either the utility grid or a generator. It is reported as warnings W351 to W354. The fault sits at connection AC2. W351 points to line conductor L1 at the master, W352 to L2 at slave 1, and W353 to L3 at slave 2. W851 and W861 are a different case. They mean either a reversed battery connection or a short circuit on Sunny Island Charger 1 or Charger 2, so check the battery wiring polarity there first. A short circuit on the load side of a stand-alone grid can also drop the supply voltage. This can cut the supply to contactor Q10/Q110 of the Multicluster-Box. On SI6.0H, SI8.0H, SI3.0M and SI4.4M units in on-grid systems, update the firmware before anything else. Next, find and remove the short circuit on the phase that was reported. If the message is still there afterwards, contact SMA Service.

<!-- review notes
- sentence 3: support check: partial - W851/W861 are battery reversed or short circuit on Charger 1/2, but the passages give no instruction to check battery polarity first.
- sentence 5: support check: partial - The article says to update firmware for those models in on-grid systems as step 1, but it doesn't say to do it 'before anything else'; also it lists the models as a condition, so mostly supported.
-->
