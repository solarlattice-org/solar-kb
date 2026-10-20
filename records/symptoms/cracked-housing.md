---
id: symptom:cracked-housing
type: Symptom
name: Cracked or brittle housing
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-connection
  note: Damaged DC connectors that look brittle or cracked often show overheating or hot spots early on
    in an infrared thermography check.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  review: drafted
---
Cracked or brittle housing turns up in visual inspection on two main parts: the module junction box (its housing and lid) and DC connectors or cables. On a junction box, the housing or lid may look weathered, brittle, cracked, warped, melted or burned. The lid may be loose or missing, and the seals at the wire entry or lid may be squeezed, broken, brittle or gone. If the cracks are on a connector or cable, suspect a connector defect. A damaged connector can also look melted, burned, broken or whitened, and opened connectors may show corrosion. If the cracks are on the junction box, suspect a junction box failure. Water can get in through a brittle or cracked housing or a missing seal and corrode the contacts inside. Start with a visual check. Then do an infrared scan under load, because affected connectors often run hot at an early stage. Make the circuit safe before any hands-on or tactile inspection. Damaged connectors can cause arcing, ground faults and fire.

<!-- review notes
- sentence 3: support check: partial - Melted, burned, broken, whitened and corrosion in opened connectors are stated, but the 'if cracks on a connector, suspect connector defect' diagnostic guidance is an inference.
- sentence 5: support check: partial - Visual inspection and IR under load are listed, and early hot spots are noted, but an explicit order (visual first, then IR) is not stated.
- sentence 6: support check: partial - Safe isolation for visual/tactile inspection and arcing, ground fault and fire hazards are stated, but the instruction to make the circuit safe is only implied by 'under safe isolation'.
-->
