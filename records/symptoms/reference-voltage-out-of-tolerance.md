---
id: symptom:reference-voltage-out-of-tolerance
type: Symptom
name: Reference voltage out of tolerance
aliases:
- Reference power source
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Primo, Symo and Galvo inverters report this condition as status code 460, which concerns
    the reference voltage source of the digital signal processor (DSP).
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r29
    h: b9bd723471f5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r31
    h: b9bd723471f5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r16
    h: d4d51e4531d2
  review: drafted
---
This symptom is reported by the inverter, not seen on the array: the inverter shows status code 460 on its display or in its event log. The Fronius Primo and Symo manuals describe code 460 as the reference voltage source for the digital signal processor (DSP) running outside its tolerances. The Fronius Galvo manual describes the same code but calls it the reference power source for the DSP. So the condition is inside the inverter's control electronics around the DSP, not on the DC strings or the grid connection. Do not mix it up with grid-side tolerance messages: the mains voltage tolerance of these inverters is a separate specification and does not belong to this code.

<!-- review notes
- sentence 1: support check: partial - Passages show code 460 and its description but do not state it is shown on display or in event log, nor that it is not seen on the array.
- sentence 4: support check: partial - The DSP reference source implies internal electronics, but the passages do not explicitly state it is not on the DC strings or grid connection.
- sentence 1: review: partial - The passages give code 460 as an inverter status code, but nothing says it shows on the display or event log, or that it is not visible on the array.
- sentence 4: review: partial - The DSP reference-source description points to the control electronics, but the passages never rule out the DC strings or the grid connection.
-->
