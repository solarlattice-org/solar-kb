---
id: concept:ond-file
type: Concept
name: OND file
aliases:
- PVsyst OND
- inverter OND file
- .OND
category: Inverters
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: tool:pvsyst
  note: OND files describe inverters for PVsyst simulation; the CPS guidance refers to PVsyst v7.4.8.
  cite:
  - src: src:chint-using-cps-inverters-with-pvsyst-2024
    loc: sec=h3
    h: 7daad258c631
  review: drafted
- claim_id: c2
  rel: related_to
  target: prod:chint-sch-275ktl
  note: This inverter has four OND file variants, which differ in kW/kVA rating (275 kW or 250 kW, each
    at 275 kVA) and in string input count (36 or 24 inputs, 12 MPPTs).
  cite:
  - src: src:chint-using-cps-inverters-with-pvsyst-2024
    loc: sec=h3
    h: 7daad258c631
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:constant-power-factor
  note: A fixed power factor required by the interconnection is set in PVsyst Energy Management, not by
    editing the OND file. Use an OND model whose kVA exceeds its kW to simulate kVA overhead.
  cite:
  - src: src:chint-using-cps-inverters-with-pvsyst-2024
    loc: sec=h3
    h: 7daad258c631
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:limit-active-power
  note: Active power limits set to meet an interconnect limit are entered at project level in PVsyst,
    so the OND file can stay as published.
  cite:
  - src: src:chint-using-cps-inverters-with-pvsyst-2024
    loc: sec=h3
    h: 7daad258c631
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:apparent-power
  note: Some inverters carry different apparent and active power ratings (kVA overhead), and each rating
    combination gets its own OND file.
  cite:
  - src: src:chint-using-cps-inverters-with-pvsyst-2024
    loc: sec=h3
    h: 7daad258c631
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
An OND file is the inverter definition file that PVsyst uses when it simulates a PV project. Project financiers want the OND file used as published, with no edits, so project-specific changes are made in PVsyst instead. A manufacturer may publish several OND files for one base model to cover its variants, such as different kW and kVA ratings or string input counts. Picking the file that matches the installed configuration matters. The file name can include the datasheet version, which helps with configuration management. If the interconnection requires a fixed power factor and the agreement allows kVA overhead, simulate with the model whose apparent power is higher than its active power. The power factor and any active power limits for the simulation are then set with the PVsyst Energy Management function, not by editing the OND file.

<!-- review notes
- sentence 1: support check: partial - The passage implies OND files are used in PVsyst simulation, but it never defines an OND file as the inverter definition file.
- sentence 3: support check: partial - The passage says multiple OND versions cover variants and that choosing the correct one matters, but it describes this for CPS specifically, not manufacturers in general.
- sentence 4: support check: partial - The passage says the file name structure includes the datasheet version for configuration management, but it doesn't say 'can include'.
-->
