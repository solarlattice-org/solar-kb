---
id: symptom:whitened-insulation
type: Symptom
name: Whitened insulation
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-connection
  note: Damaged DC connectors or cables, including whitened ones, often show overheating or hot spots
    at an early stage when checked with thermography.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:low-insulation-resistance-alarm
  note: Degraded cable insulation can cause inverter low-insulation faults or switch-off, especially after
    rain or in the early morning when cables and connectors are damp.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=28.r1
    h: 4c61bdc62398
  review: drafted
  review_note: 'support check: partial - Passages link degraded/damaged cables to low-insulation faults
    or inverter switch-off after rain or early morning, but don''t tie whitened insulation specifically
    to it, and insulation failure isn''t always visible.'
---
Whitened insulation is a visible change on DC cables or connectors. Damaged parts may also look melted, burned, brittle, broken or cracked. It points to a cable or connector defect, which can lead to overheating, insulation faults, ground faults, lost production and a fire risk. Scan the affected connectors and cables with an IR camera, because damaged connectors often run hot early on. Open connectors may also show corrosion. Bad cable insulation cannot always be seen, so the only sure check is an insulation resistance measurement in dry and in damp or wet conditions. Check the monitoring data for inverter low-insulation faults or shutdowns after rain or in the early morning, when damp cables are most likely to cause trips. Also compare string currents and run fault localization on isolated circuits to find the damaged run. Do not confuse whitened cable insulation with whitening on the module backsheet, which is a separate failure called backsheet chalking.

<!-- review notes
- sentence 3: support check: partial - Thermography finding of early hot spots and corrosion in opened connectors are stated, but the passages do not explicitly recommend scanning; also corrosion is for opened connectors, not 'open connectors' generally.
- sentence 5: support check: partial - Passage says such defects can cause low-insulation faults or switch-off after rain or early morning, but does not recommend checking monitoring data or say that is when trips are most likely.
- sentence 7: support check: partial - Passages show backsheet chalking (whitening) is a separate PV module failure, but say nothing about cable insulation whitening being confused with it.
-->
