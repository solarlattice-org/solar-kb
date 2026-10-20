---
id: meas:reflectance-increase
type: Measurement
name: Increased glass reflectance
aliases:
- increase in reflection
- gain in reflectance
- optical reflection
claims:
- claim_id: c1
  attr: current_drop
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Field-deployed EFG-Si module with delamination and discoloration, mostly around the module
    edge, over its first 3 years of deployment
  note: The source gives this as approximately 5% (~5%). Over the same period Pmax fell by nearly 20%,
    which the source attributes to delamination, moisture ingress and contact corrosion, not only to reflection.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 11.5
    unit: unit:PERCENT
  conditions: PV system after 12 years of exposure. Most of the loss came from lower Isc and was mainly
    attributed to delamination at the cell/encapsulant interface
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
  review_note: 'support check: partial - The 11.5% loss after 12 years, mostly from Isc loss attributed
    to cell/encapsulant delamination, is stated, but it is a total power loss, not a loss from increased
    glass reflectance specifically.'
---
This signature is a rise in the light the module front reflects, compared with an earlier measurement or with a module in good condition. Hemispherical reflectance is measured in the lab with an integrating sphere, and in the field with a small hand-held spectrometer. Because readings can vary between repeats, the repeatability of the measurement has to be taken into account. Removing or abrading the anti-reflective coating during cleaning raises reflectance step by step as the number of cleaning cycles grows. In tests, nylon brushes and fine sand caused a larger increase. Glass with an anti-reflective coating showed a clear change after long brush cleaning tests, while uncoated structured glass showed no measurable effect. Glass corrosion or abrasion can make the glass look hazy, milky or rougher than the surrounding glass. The glass may also pick up soiling more easily. Delamination creates new air interfaces inside the module, and these add reflection. That lowers short-circuit current and can cause current mismatch and bypass diode activation. In principle, a reflectometer could be used to measure how far the layers have separated in a delaminated module.

<!-- review notes
- sentence 1: support check: partial - The passages discuss gains in reflectance (after cleaning, after delamination), but do not define a signature as a rise in front reflectance compared with an earlier measurement or good module; it is implied only.
- sentence 2: support check: partial - Lab integrating sphere, field hand-held spectrometer and the need to account for repeatability are stated, but the explanation that readings vary between repeats is only a gloss.
-->
