---
id: symptom:cracked-insulation
type: Symptom
name: Cracked or brittle insulation
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-connection
  note: Damaged connectors or cables that look brittle, cracked or whitened often already show overheating
    or hot spots when checked with thermography at an early stage.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  review: drafted
  review_note: 'support check: partial - Passages say brittle/cracked cables often show overheating/hot
    spots on thermography, but the string-current-lower signal and the specific link to ''cracked insulation''
    as a hot connection observation are not stated.'
---
Damaged DC cables and connectors can look brittle, cracked, broken or whitened, and in worse cases melted or burned. This damage usually points to a cable defect or a connector defect, and either one can cause insulation faults, ground faults, overheating, lost production and a risk of fire. A thermography check often shows the affected connector or cable running hot early on, before it fails completely. If the damage is on a connector, open it and look for corrosion. Corrosion points to a connector defect rather than a fault along the cable run. Cracks in a module backsheet can also break down insulation and lead to ground faults, so check whether the damage is on the wiring or on the module itself. Start with a visual inspection. Then test insulation resistance, do a thermal inspection, compare string currents, and isolate the circuit to find the fault.

<!-- review notes
- sentence 2: support check: partial - Cable and connector defect pages list insulation faults, ground faults, overheating, production loss and fire risk (connector page lacks explicit production loss), but 'this damage usually points to' these defects is not explicitly stated.
- sentence 4: support check: partial - Passages say opened connectors can show corrosion, but not that corrosion distinguishes a connector defect from a cable-run fault or that one should open it to check.
- sentence 5: support check: partial - Backsheet cracking causing insulation failure and potential ground fault is stated, but the advice to check wiring versus module is not in the passages.
- sentence 6: support check: partial - The listed detection methods match, but the passages give no ordered sequence (start with visual, then others) and the list is for cable defect only.
-->
