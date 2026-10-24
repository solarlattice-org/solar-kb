---
id: concept:pan-file
type: Concept
name: PAN file
aliases:
- PVsyst PAN
- module PAN file
- .PAN
- module parameter file
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:energy-yield-assessment
  note: PAN parameters are used to translate weather into expected power and energy.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h5
    h: 25d3cd8b21f5
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h4
    h: 88a270e92419
  review: drafted
- claim_id: c2
  rel: related_to
  target: fm:flawed-pan-file-losses
  note: Incorrect or nonrepresentative PAN files can bias simulated module performance and overstate modeled
    energy.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h5
    h: 25d3cd8b21f5
  review: drafted
- claim_id: c3
  rel: related_to
  target: symptom:expected-vs-measured-gap
  note: A flawed PAN file shows up as a persistent gap between expected and measured performance while
    the plant may be operating normally.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h4
    h: 88a270e92419
  review: drafted
- claim_id: c4
  rel: related_to
  target: method:pan-file-comparison
  note: Compare manufacturer and third-party PAN files and data sheets, lab measurements and site behavior.
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
- claim_id: c5
  rel: related_to
  target: method:model-sensitivity-analysis
  note: Sensitivity cases test whether a production gap is plausibly explained by PAN parameters.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: drafted
- claim_id: c6
  rel: related_to
  target: mit:validated-module-files
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  review: drafted
- claim_id: c7
  rel: related_to
  target: mit:model-input-documentation
  note: Document the selected PAN source and version; treat PAN provenance as a controlled modeling input.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h7
    h: acd2a7ec2ad2
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  review: drafted
---
A PAN file is the module parameter file that PVsyst or a similar energy model uses to describe how a PV module behaves. It holds the module's electrical behavior, temperature response, low-light performance, incidence angle (IAM) assumptions and other parameters that turn weather data into expected power. If those parameters are optimistic, incomplete or do not match the modules actually delivered, the modeled energy can be too high. The expected yield is then off before any physical fault exists at the plant. Files made by the manufacturer and files made independently can differ, and the difference can affect procurement comparisons, financing assumptions and post-construction variance analysis. In the field, a flawed PAN file looks like a persistent gap between expected and measured performance that remains after weather, availability, clipping, curtailment, soiling, degradation and instrumentation have been checked, even though the plant may be running normally. To diagnose it, find the exact PAN file used, including its source, version and any manual edits. Compare it with data sheets, independent lab data, third-party files and site behavior, then run sensitivity cases. Treat PAN source and version as a controlled, documented model input, and keep model-baseline problems separate from real operational losses so that no one tries to repair a field defect that does not exist.
