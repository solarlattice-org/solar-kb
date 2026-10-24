---
id: concept:voltage-levels
type: Concept
name: Voltage levels
aliases:
- low voltage
- medium voltage
- high voltage
- LV
- MV
- HV-EHV
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: std:ansi-c84-1
  note: ANSI C84.1 defines voltage ranges.
  cite:
  - src: src:ref-standards-grid-standards-voltage-tolerance
    loc: fig=2
    h: e75c8689f88f
  review: drafted
- claim_id: c2
  rel: related_to
  target: tool:vlf-hipot-tester
  note: Very low frequency test voltages are chosen by the phase-to-phase system voltage class.
  cite:
  - src: src:std-standards-neta-ats-ansi-neta-ats-2009
    loc: tbl=17
    h: 079ce7f8f125
  - src: src:std-standards-neta-ats-neta-ats-2009
    loc: tbl=17
    h: 079ce7f8f125
  review: drafted
---
Voltage levels are classes of nominal system voltage, such as low voltage (LV) and medium voltage (MV), used to group equipment, test requirements and grid rules. NETA ATS defines low voltage as a class of nominal system voltages of 1000 volts or less. Tesla Megapack manuals classify LV as 50 to 1,000 V AC and 50 to 2,000 V DC, and MV as 1,000 to 35,000 V AC and 2,000 to 35,000 V DC. Electricity is generated at voltages too low to transmit efficiently over long distances, so step-up transformers raise it to higher levels. Utilities deliver three-phase, four-wire service to larger customers at nominal voltages such as 4,160 V and 13,200 V. The voltage class decides which test levels apply: for example, very low frequency cable test voltages are set by the phase-to-phase system voltage, from 5 kV to 35 kV. Inverter nominal voltage is usually given as a line-to-line value, so check how it is stated before comparing it with the service voltage.

<!-- review notes
- sentence 1: support check: partial - Passages define LV and MV as classes of nominal voltage, but do not state they are used to group equipment, test requirements and grid rules.
- sentence 3: support check: partial - Ranges match, but the passages do not mention Tesla Megapack manuals as the source.
- sentence 5: support check: partial - Table rows show 3-phase 4-wire at 4,160 V and 13,200 V, but 'larger customers' is only implied by load minimums (500 kVA and up).
- sentence 7: support check: partial - Passage says nominal inverter voltage is specified as line-to-line, but not the 'usually' or the advice about comparing with service voltage.
-->
