---
id: method:pan-file-comparison
type: DetectionMethod
name: Model file comparison
claims:
- claim_id: c1
  rel: produces
  target: meas:module-parameter-deviation
  note: The PAN file used for the energy estimate is checked against manufacturer data sheets, independent
    lab measurements and third-party PAN files to find parameter differences.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:model-explained-production-gap
  note: Sensitivity cases show whether a persistent expected-vs-measured gap can plausibly be explained
    by PAN parameters rather than by a field fault.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h4
    h: 88a270e92419
  review: drafted
---
Model file comparison checks the PAN module file used in PVsyst or a similar energy model against other sources, to see whether the yield expectation is wrong rather than the plant. Start by identifying the exact PAN file behind the energy estimate, including its source, its version and any manual edits. Then run sensitivity cases to test whether the production gap can plausibly be explained by the PAN parameters, and reconcile measured performance against the file used for financing or design. The method detects Flawed PAN File Yield Losses, where optimistic, incomplete or inconsistent module parameters overstate modeled energy. Keep this comparison separate from real operating losses, so a baseline problem in the model is not mistaken for a field defect that can be repaired. Treat the PAN file's origin as a controlled input, so that teams do not compare designs or diagnose operations using inconsistent module models.
