---
id: symptom:no-output-voltage
type: Symptom
name: No output voltage measured
aliases:
- McNoVtgSv1
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Sunny Island multicluster systems report it as F758 (level 2) when the main cluster has no output
    voltage, and as W759, W760 or W761 (level 1) for slaves 1, 2 and 3 of the main cluster.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r15
    h: 09ced55720ef
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r16
    h: b1b634784393
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r18
    h: 731e075d37e3
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r17
    h: 6f2bac753cf5
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152
    h: f038146b9de5
  review: drafted
---
This symptom appears on SMA Sunny Island battery inverters running as a multicluster system: the device reports that it cannot measure the output voltage of the main cluster. Code F758 is a level 2 event for the main cluster as a whole. Codes W759, W760 and W761 are level 1 warnings for slave 1, slave 2 and slave 3 of the main cluster. Another SMA manual names W759 as McNoVtgSv1 and says the main cluster voltage cannot be measured on line conductor L2, which slave 1 handles. The code number tells you which unit and line conductor to look at: a slave code points to one slave and its phase, while F758 covers the whole main cluster. The same event table also lists other multicluster faults on slaves: interrupted internal CAN communication, missing sync pulse, DSP reset and grid monitoring failure. Note any of these that appear alongside, but the source does not link them to this symptom.

<!-- review notes
- sentence 1: support check: partial - F758 says no output voltage measured from main cluster, but 'Sunny Island' brand and 'battery inverters' identification are not in the passages (only multicluster context implied).
- sentence 3: support check: partial - Levels 1 and slave assignments are stated, but the passages never call them 'warnings' (though W prefix is only implied).
- sentence 4: support check: partial - Name McNoVtgSv1 and L2 (slave 1) are stated, but that slave 1 'handles' L2 is roughly implied; 'another SMA manual' is source detail not shown, mostly fine.
- sentence 5: support check: partial - Slave codes pointing to a slave and F758 to whole main cluster are supported, and W759 maps to L2, but phase mapping for slaves 2 and 3 is not stated.
-->
