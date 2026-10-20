---
id: mit:model-sensitivity-review
type: Mitigation
name: Model sensitivity review
aliases:
- sensitivity analysis
- sensitivity cases
---
A model sensitivity review checks how much the energy model output depends on the module parameter (PAN) file. It is used to address flawed PAN file yield losses. It applies when measured output stays below what was expected, even after weather, availability, clipping, curtailment, soiling, degradation and instrument problems have been checked. First identify the exact PAN file behind the energy estimate, including its source, its version and any manual edits. Then run sensitivity cases to see whether differences in the PAN parameters could plausibly explain the production gap. Keep this comparison apart from real operational losses, so that a wrong model baseline is not treated as a field defect that can be repaired. The review should be combined with using validated module files, recording which PAN source and version was chosen, and updating forecasts when independent tests show material parameter differences. The review fixes nothing physical in the plant. The plant may be running normally, and the problem may only be the expected baseline.

<!-- review notes
- sentence 1: support check: partial - Passages list reviewing model sensitivity as a detection method for flawed PAN files, but do not define it as checking how much output depends on the PAN file.
- sentence 7: support check: partial - The passages say PAN losses are modeling losses and the plant may operate normally with a wrong baseline, but they don't say the review itself fixes nothing physical.
-->
