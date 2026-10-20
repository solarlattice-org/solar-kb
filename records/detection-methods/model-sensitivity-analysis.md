---
id: method:model-sensitivity-analysis
type: DetectionMethod
name: Model sensitivity analysis
claims:
- claim_id: c1
  rel: produces
  target: meas:model-explained-production-gap
  note: Sensitivity cases show whether the gap between expected and measured production can plausibly
    be explained by changes in PAN (module model file) parameters rather than by a field defect.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: drafted
  review_note: 'support check: partial - Passage supports sensitivity cases testing whether the gap is
    explained by PAN parameters, but says nothing about the specific signals (AC power below baseline,
    POA irradiance with no anomaly) or the shortfall shrinking when parameters vary.'
---
Model sensitivity analysis means running the energy model several times with different module parameter inputs to see how much the expected yield moves. It is used to detect flawed PAN file yield losses, which are modeling losses where the module file in PVsyst or a similar tool does not match how the module actually behaves. First identify the exact PAN file behind the energy estimate, including its source, version and any manual edits. Then compare it with datasheets, independent lab data, third-party files and measured site behavior. The sensitivity cases show whether a persistent gap between expected and measured performance could plausibly come from the PAN parameters. Only use it after weather, availability, clipping, curtailment, soiling, degradation and instrument problems have been checked, because the plant may be running normally while the baseline is wrong. Keep this analysis separate from real operational losses so that a baseline problem is not handled as a field defect that needs repair. Treat the module file as a controlled input. Using different module files across teams can distort design comparisons and fault diagnosis.

<!-- review notes
- sentence 1: support check: partial - Passage says to run sensitivity cases on PAN parameters to see if they explain the gap, but doesn't describe running the model several times or measuring how much expected yield moves.
- sentence 5: support check: partial - The persistent gap is defined after those other issues are reviewed and the plant may be operating normally, but 'only use it after' is a stronger prescriptive ordering than stated.
-->
