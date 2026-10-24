---
id: concept:ground-coverage-ratio
type: Concept
name: Ground coverage ratio
aliases:
- GCR
- ground cover ratio
category: Design
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: symptom:inter-row-shading
  note: In the PowerTrack model, the GCR-based shading calculation works like the inter-row shading calculation,
    but takes a single coverage value instead of full array geometry.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h7
    h: a97ce08a4269
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:single-axis-tracker
  note: GCR is one of the tracker details entered during site performance-model setup, together with tracking
    type, initial tracker angle and azimuth/tilt.
  cite:
  - src: src:alsoenergy-kb-attachments-files-869-advanced-site-configuration-performance-modeling-r10-5
    loc: tbl=10
    h: 3b75a72cc091
  - src: src:alsoenergy-kb-attachments-files-869-advanced-site-configuration-performance-modeling-r10-5
    loc: tbl=10.r1
    h: 29dad1517265
  - src: src:alsoenergy-kb-attachments-files-869-advanced-site-configuration-performance-modeling-r10-5
    loc: tbl=37
    h: 3e0d6c0bae4d
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:bifaciality
  note: A yield study compared bifacial gain between two tracker models at the same GCR.
  cite:
  - src: src:eq-equip-trackers-bifacial-yeild-report-fise-eng-report-ideematec-final-h4plus-vs-ltec
    loc: fig=9
    h: d986918b7f7e
  review: drafted
- claim_id: c4
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: PowerTrack's expected-energy model can use GCR as one of its shading inputs.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h7
    h: a97ce08a4269
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  review: drafted
- claim_id: c5
  rel: related_to
  target: prod:ftc-solar-voyager
  note: The Voyager specifications list a supported ground coverage ratio range of 20% to 60%.
  cite:
  - src: src:eq-equip-trackers-ftc-voyager-installation-manual-890003-rev-3-a
    loc: tbl=2.r12
    h: 288277bfa38a
  review: drafted
---
Ground coverage ratio, or GCR, is a single number that says how much of the ground area is covered by PV modules. Performance models use it to estimate row-to-row shading in a simpler way than a full inter-row shading model, which needs the size, spacing and orientation of the array. In the PowerTrack model, the shading result reduces the direct part of plane-of-array irradiance, and the diffuse and albedo parts are then weighted to get the effective irradiance. When you set up a site model for trackers, you enter GCR along with tracking type, initial tracker angle and azimuth or tilt. Tracker specifications list the GCR range they support. For example, the FTC Voyager lists 20% to 60%, and one NREL tracker study table shows an overall GCR of 0.25. Yield comparisons between tracker designs, including studies of bifacial gain, are run at the same GCR so the results can be compared fairly.

<!-- review notes
- sentence 2: support check: partial - The passages say the GCR calculation uses a simple value while inter-row needs size, spacing and orientation, but they don't say performance models in general use it to estimate row-to-row shading.
- sentence 3: support check: partial - Direct irradiance is blocked and diffuse and albedo are estimated then scaled by weighting factors, but the passage doesn't say the shading result reduces the direct part exactly this way for all three components.
- sentence 5: support check: partial - Voyager's 20%-60% is supported and an overall GCR of 0.25 appears, but the passages don't say it is from an NREL tracker study or that specs generally list supported GCR ranges.
- sentence 6: support check: partial - The passages show comparisons at the same GCR for both models, but they don't state this is done so results compare fairly or that it holds for all yield comparisons.
-->
