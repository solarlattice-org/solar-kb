---
id: fm:flawed-pan-file-losses
type: FailureMode
name: Flawed PAN File Yield Losses
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:inaccurate-model-input
  note: The PAN module parameter file used in PVsyst or a similar energy model is optimistic, incomplete
    or does not match the delivered modules.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h4
    h: 88a270e92419
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h5
    h: 25d3cd8b21f5
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:expected-vs-measured-gap
  note: The gap remains after weather, availability, clipping, curtailment, soiling, degradation and instrumentation
    have been checked. The plant may be running normally while the baseline is wrong.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h4
    h: 88a270e92419
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c3
  rel: detected_by
  target: method:pan-file-comparison
  note: Identify the exact PAN file used, including its source, version and any manual edits. Then compare
    it with manufacturer and third-party files and with datasheets.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:independent-test-validation
  note: Check the PAN parameters against independent lab measurements.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: detected_by
  target: method:model-sensitivity-analysis
  note: Run sensitivity cases to see whether the PAN parameters could plausibly explain the production
    gap.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:measured-vs-modeled-reconciliation
  note: Reconcile measured plant performance with the file used for financing or design.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: mitigated_by
  target: mit:validated-module-files
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:model-input-documentation
  note: Record which PAN source and version was selected and manage PAN provenance as a controlled input,
    so that teams do not use inconsistent module representations.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h7
    h: acd2a7ec2ad2
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c9
  rel: mitigated_by
  target: mit:model-sensitivity-review
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c10
  rel: mitigated_by
  target: mit:forecast-update
  note: Update the forecast when independent testing shows material differences in the parameters.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c11
  rel: distinguished_from
  target: fm:soiling-losses
  by: method:measured-vs-modeled-reconciliation
  note: A PAN-file loss is a modeling baseline error, not a fault that can be repaired in the field. The
    gap persists after soiling has been reviewed and ruled out.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h4
    h: 88a270e92419
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: drafted
  review_note: 'support check: partial - Passages say the gap persists after soiling is reviewed and it
    is a modeling not field fault, but don''t explicitly state a differentiation from soiling via reconciliation.'
- claim_id: c12
  rel: distinguished_from
  target: fm:grid-curtailment-losses
  by: method:measured-vs-modeled-reconciliation
  note: Curtailment is a real operational loss. A PAN-file gap remains after curtailment and clipping
    have been accounted for.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h4
    h: 88a270e92419
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Gap persisting after curtailment and clipping are reviewed is
    stated, but curtailment as real operational loss and explicit differentiation method are not stated.'
---
Flawed PAN file losses are modeling losses, not physical faults. They happen when the module parameter file used in the energy model does not represent how the real modules behave. If the file's parameters are optimistic, incomplete or do not match the delivered modules, the model can overstate expected energy. In the field, this shows up as a lasting gap between expected and measured output after weather, availability, clipping, curtailment, soiling, degradation and instrumentation have all been checked. The plant itself may be working normally. To confirm it, find the exact PAN file used, including its source, version and any edits. Compare it with datasheets, independent lab data and third-party files. Run sensitivity cases to check whether the PAN parameters can explain the gap. Keep this analysis separate from real operational losses, so a model error is not treated as a field defect that needs repair. To prevent or correct this loss, use validated module files, record which PAN source and version was chosen, and update forecasts when independent testing shows material differences.
