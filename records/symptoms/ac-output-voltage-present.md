---
id: symptom:ac-output-voltage-present
type: Symptom
name: Voltage on AC output
aliases:
- Voltage on output AC1
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On the SMA Sunny Island, voltage on output AC1 shows as display number F158 (level 2) for the
    unit itself. For slave units 1, 2 and 3 it shows as W159, W160 and W161 (level 1).
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r25
    h: ecc2d6d1e845
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r26
    h: aba34289cbdc
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r28
    h: dd346c648cd6
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=142.r27
    h: e1cb27a345d0
  review: drafted
---
On SMA Sunny Island battery inverters, this event means the inverter has found voltage on its AC1 output. The display shows it as F158 (level 2) when the event belongs to the unit itself. When a slave unit in a cluster reports it, the display shows warning W159, W160 or W161 (level 1) for slave 1, 2 or 3. The code number tells you which unit to check. The sources do not name a root cause for this event, so do not assume a failure mode from the code alone. Before you work on the AC terminals, do an absence-of-voltage check between each pair of AC phases with a meter, as the inverter instructions show.

<!-- review notes
- sentence 1: support check: partial - Passage says only 'Voltage on output AC1'; interpretation as the inverter having found voltage on its output is a mild paraphrase, with no further meaning given.
- sentence 5: support check: partial - Figures show absence-of-AC-voltage checks between phase pairs, but passages don't state doing it before working on AC terminals or that it's required by the instructions.
-->
