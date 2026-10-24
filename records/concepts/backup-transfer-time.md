---
id: concept:backup-transfer-time
type: Concept
name: Backup transfer time
aliases:
- switchover time
- transfer time
- UPS vs backup
- Switching time
- Backup switching time
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: func:backup-transfer
  note: Switching time is the gap in load supply while the automatic transfer switch separates the backup
    grid from the utility grid and the inverter forms the backup grid.
  cite:
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=4.1.1
    h: 89de86fd5ec6
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=40
    h: 56793e77f46e
  - src: src:sma-doc-244194
    loc: sec=3.4
    h: e74f4f0530f0
  review: drafted
- claim_id: c2
  rel: related_to
  target: state:backup-operation
  note: Switchover times apply both when entering backup operation and when returning to feed-in operation.
  cite:
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=20.r3
    h: f26a3697f795
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=h85
    h: d64eb21249a5
  review: drafted
  review_note: 'support check: partial - Passages give switchover parameters for both entering backup
    (BckSwOnDl) and returning to feed-in, but do not explicitly state that switchover times apply to both
    directions as a general note.'
- claim_id: c3
  rel: related_to
  target: prod:sma-multicluster-box
  note: To get the whole-system switchover time, add the switchover time of the transfer device or Multicluster-Box
    to the inverter's own switchover time.
  cite:
  - src: src:sma-doc-278742
    loc: sec=16.11
    h: 8699661c89e9
  review: drafted
- claim_id: c4
  rel: related_to
  target: std:ieee-1547-2018
  note: Selecting this grid standard affects the backup switching time on some hybrid inverters.
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: sec=h241
    h: 419d413841b9
  review: drafted
---
Backup transfer time, also called switching time, is how long a battery-backup system takes to restore supply to the loads after the grid fails. When the grid fails, an automatic transfer switch separates the household grid and the PV system from the utility grid. A battery or hybrid inverter then forms a backup grid, and the loads go unsupplied until that backup grid is in place. The gap depends on the system design. One SMA Sunny Island system leaves the loads unsupplied for about five to seven seconds. A Solis hybrid inverter switches in about 80 ms under IEEE 1547-2018, or 10 ms with the IG Follow setting turned on. The longer Solis switching time comes from a conflict with low-voltage ride-through requirements. Turning on IG Follow gives up some of that ride-through behaviour in exchange for a faster changeover. Some inverter datasheets give separate switchover times for high-impedance and low-impedance switching. For the whole system, you must also add the switchover time of the transfer device or Multicluster-Box. Load supply is also interrupted when the system switches back from backup to feed-in operation. On one SMA system this interruption is adjustable, with a default of 5 s. Switching time is different from bridging time, which is the whole period from grid failure until the utility grid comes back, covered by the backup system. A UPS used for control power typically transfers in a few milliseconds; one example lists 5 ms typical.

<!-- review notes
- sentence 4: support check: partial - The LVRT conflict is stated and IG Follow is for when faster switching matters more than LVRT, but 'Solis' isn't named and giving up ride-through behaviour is only implied.
- sentence 6: support check: partial - The adjustable interruption with 5 s default for automatic backup to feed-in is stated, but not as a general statement of load supply interruption or explicitly SMA.
- sentence 8: support check: partial - Eaton 5S lists 5 ms typical transfer time, but the passage doesn't mention control power use or a general claim about UPS typically transferring in a few ms.
-->
