---
id: method:measured-vs-modeled-reconciliation
type: DetectionMethod
name: Measured vs modeled reconciliation
aliases:
- Performance vs. Model
claims:
- claim_id: c1
  rel: produces
  target: meas:performance-index-below-unity
  note: Performance Index is measured energy divided by modeled energy. A persistent shortfall against
    the model is the gap to explain before blaming field equipment.
  cite:
  - src: src:alsoenergy-kb-rescheduling-a-legacy-site-performance-yield-report-in-locusnoc
    loc: sec=front
    h: 003faad8cb7c
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: drafted
  review_note: 'support check: partial - Passages define Performance Index as measured/modeled energy
    and say to separate model-baseline gaps from field defects, but don''t state that monthly measured
    energy persistently below model yields PI below unity, nor the POAI input.'
- claim_id: c2
  rel: produces
  target: meas:air-mass-correlated-residual
  note: After clipping, curtailment, temperature, soiling and availability effects are removed, residuals
    that track air mass, season, water vapor or aerosols point to spectral effects.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h6
    h: 172487c8868e
  review: drafted
---
This method compares the energy a plant actually produced with the energy its performance model predicted, and then works out why the two differ. Measured energy is only meaningful when it is set against a model of expected performance, and the result is often given as a performance index: measured energy divided by modeled energy. Plotting measured and modeled power together, or running monthly reports, gives a quick view of how a site or component is performing. For Flawed PAN File Yield Losses, check measured plant output against the PAN file used for design or financing, and run sensitivity cases to see whether the module parameters could explain the gap. For Spectral Effect Yield Losses, remove clipping, curtailment, temperature, soiling and availability effects first, then compare the remaining residuals with air mass, precipitable water, aerosols, season and time of day. A gap caused by the model baseline must be kept separate from true operating losses, so it is not mistaken for a field defect that can be repaired. Do not use spectral correction to explain away all underperformance; it should improve the pattern in the residuals and be tied to measured or modeled atmospheric conditions. Any difference left unexplained may come from data problems or small modeling errors, and the results are only as good as the inputs: calibrated, clean irradiance sensors, well-attached temperature sensors and accurate as-built records.

<!-- review notes
- sentence 1: support check: partial - Passages describe comparing measured to modeled energy, but the 'works out why they differ' is only partially covered (other losses, model errors), not a general method description.
-->
