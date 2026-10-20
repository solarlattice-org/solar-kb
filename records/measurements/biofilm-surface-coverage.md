---
id: meas:biofilm-surface-coverage
type: Measurement
name: Biofilm surface coverage
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production loss from fungal bio-soiling in humid subtropical regions; may not
    recover after rainfall
  quote: Fungal bio-soiling can create persistent 5-11% production losses in humid subtropical regions
    and may not recover after rainfall.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  review: drafted
---
This signature is the share of the module glass covered by biological growth, measured by imaging the surface directly with a handheld digital microscope. In one large microscope image dataset, average coverage was a few percent, but some spots ranged from well under one percent to about a third of the surface. Bio-soiling was found in eight climate zones. The deposits are mostly sub-aerial biofilms, especially black fungi, which grow as dark masses on the glass and trap other particles. High coverage points to widespread fungal soiling losses, which lower glass transmittance and cause a loss that does not wash off in rain the way ordinary dust does. Growth is patchy, so check modules in several parts of the array rather than relying on one module as representative. Use microscopy to confirm the cause after monitoring shows a production deficit that persists after rain but recovers after manual cleaning. Biofilms grow most readily in humid climates where condensation forms on the modules.

<!-- review notes
- sentence 1: support check: partial - Passages say surface coverage was measured by handheld microscope imaging, but do not define the signature as share of glass covered, and 'typical power loss' is not coverage.
- sentence 4: support check: partial - Fungal soiling lowering transmittance and not washing off like dust is stated, but nothing says high coverage points to widespread losses as an inference.
- sentence 7: support check: partial - Passage says biofilm formation is likely in high humidity and condensation promotes growth in São Paulo, but 'most readily' is a stronger comparative claim.
-->
