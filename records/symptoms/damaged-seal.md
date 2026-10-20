---
id: symptom:damaged-seal
type: Symptom
name: Damaged or missing seal
aliases:
- Seal leak
- Seal will leak
- missing seal
claims:
- claim_id: c1
  rel: observed_as
  target: meas:open-junction-box
  note: On visual inspection, the sealing around the wire entrance or the lid may be squeezed, broken,
    brittle or missing altogether. This often goes with an open or loose lid or a junction box that has
    shifted on the backsheet.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=17.r1
    h: 2f54f0d00dad
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r1
    h: 2f54f0d00dad
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:jbox-terminal-corrosion
  note: If the seal at the wire entrance or housing is missing or damaged, moisture can get into the junction
    box and corrode the contacts.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=37.r3
    h: 69aa96116e44
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:jbox-seal-leak
  note: Field documentation checklists list a leaking seal as one of the junction box defect options.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: tbl=14
    h: 04a0d5ccc0bf
  - src: src:iea-pvps-t13-09-2017
    loc: tbl=15
    h: 2f5187a646f8
  review: drafted
---
Look for a damaged or missing seal on the module junction box, mainly around the wire entrance and the lid. The sealing material may be squeezed, broken, brittle or gone. Field inspection checklists record a leaking seal as a junction box defect, along with loose or fallen-off lids, cracked boxes and brittle adhesive. A bad seal lets moisture into the junction box, and the moisture corrodes the contacts. This can lead to junction box interconnection failure. Corroded or loose contacts can heat up, which shows as a hotspot on an IR camera. In the worst case they can short or arc and start a fire. Start with a visual and thermal check of the junction box. Check the bypass diodes, and use IV tracing and insulation checks if you suspect damage. Fix sealing defects or replace the damaged junction box assembly or module. If you see arcing or burn marks, isolate the circuit for safety first. Inverter enclosure seals can also be damaged if the enclosure is opened in freezing weather. Moisture can then get in, so remove any ice from the seal before opening.

<!-- review notes
- sentence 4: support check: partial - Passages state resistive heating, IR hot spot, short circuit/arcing and fire, but attribute these to bad contacts generally; corroded or loose contacts heating is only implied.
-->
