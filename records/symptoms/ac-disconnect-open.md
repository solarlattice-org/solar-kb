---
id: symptom:ac-disconnect-open
type: Symptom
name: AC disconnect open
aliases:
- AC disconnection unit is open
- AC service disconnect switch
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ac-disconnect-open
  note: On the Sunny Central CP XT, the central switch indicator shows position B when the AC disconnection
    unit tripped and is open, and position C (switch off) when it is open.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=14.r2
    h: 01784f14b1f5
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=14.r3
    h: fdab1f5284e8
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA Sunny Central CP XT reports error 7706 when the AC disconnection unit is open or has tripped.
    The corrective measure is to contact the SMA Service Line.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r16
    h: c8e1d1ec82eb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
This symptom means the AC disconnection unit between the inverter and the grid is open, either because it was opened or because it tripped. On SMA Sunny Central CP XT inverters it is reported as error 7706, and the manual's corrective measure is to contact the SMA Service Line. Check the central switch indicator first: position B means the unit tripped and is open, and position C means the switch is in the off position. On the display, an open-switch symbol between the inverter data and AC side symbols means the AC contactor is open, while the same symbol on the DC side means the DC switchgear is open. Before treating it as a fault, confirm the disconnect was not left open on purpose after lockout and tagout for service or inspection. If the inverter enclosure is not level, the mechanism of an optional AC disconnect or breaker can be damaged, so check that the doors line up.

<!-- review notes
- sentence 1: support check: partial - Open or tripped is stated, but 'between the inverter and the grid' location is not in the passages.
- sentence 3: support check: partial - Positions B and C meanings are stated, but 'check first' ordering is not, and C is described as the AC disconnection unit open, which matches off-position.
- sentence 5: support check: partial - Passages show lockout/tagout procedures with AC disconnect opened for service, but do not state to confirm the disconnect wasn't left open on purpose before treating as a fault.
- sentence 1: review: partial - The passages say the AC disconnection unit is open or tripped, but none of them places it between the inverter and the grid.
-->
