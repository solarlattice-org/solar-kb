---
id: symptom:burnt-junction-box
type: Symptom
name: Deformed or burnt junction box
aliases:
- Burnt (box)
claims:
- claim_id: c1
  rel: observed_as
  target: meas:visible-burn-marks
  note: The junction box housing or lid looks burnt, melted or warped. Discolored cells or burn marks
    may also show on the module area above the hot junction box.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: fig=2
    h: c93b4815ec6c
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:ir-hot-connection
  note: An IR camera shows the junction box hotter than the rest of the module. Loose connections inside
    the box, bad contacts or corrosion raise the resistance and cause the heat.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:jbox-terminal-corrosion
  note: Bad contacts or corrosion inside the box raise internal resistance and heat the box. Moisture
    getting in is one cause of the corrosion.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
Look on the back of the module for a junction box whose housing or lid is warped, melted or burnt. One common cause is a failed bypass diode: the heat it gives off inside the box can deform the box or burn it. Internal arcing can also burn the box, for example an arc at an input lead. Bad solder contacts are one cause of these arcs, and they can start a fire. Bad contacts, corrosion from moisture getting in, and loose connections all raise resistance and heat the box. An infrared camera shows this as a hot junction box. Check the diodes and run an IV curve or open-circuit voltage measurement. These help tell a diode or interconnection fault from a contact or arcing problem, and short circuits show up in the open-circuit measurement. If the box or backsheet is burnt through, expect insulation faults and leakage current. Run insulation checks and isolate the module for safety first. Replace the module instead of repairing the box, because repaired junction boxes can easily start new fires.

<!-- review notes
- sentence 2: support check: partial - Bypass diode failures sometimes deform or burn the box via heat dissipation, but 'one common cause' overstates the passages' 'sometimes'.
- sentence 4: support check: partial - Bad contacts and corrosion heating the box and IR detection of loose-connection hotspots are stated, but loose connections raising resistance is only implied by the IR figure caption.
- sentence 5: support check: partial - Short circuits detected by open-circuit measurement/IV curve and diode verification are stated, but distinguishing diode/interconnection faults from contact or arcing problems is not.
- sentence 6: support check: partial - Burnt-through box/backsheet leading to leakage current, insulation checks and safety isolation are stated, but insulation faults are not tied to burn-through specifically.
-->
