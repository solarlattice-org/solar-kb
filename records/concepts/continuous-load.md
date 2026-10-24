---
id: concept:continuous-load
type: Concept
name: Continuous load
aliases:
- 125% rule
- continuous current
- permanent load
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: comp:ac-circuit-breaker
  note: Breaker specifications give a continuous load rating, and breaker nominal current is reduced when
    the load lasts longer than one hour.
  cite:
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: tbl=8.r1
    h: f63ed489565b
  - src: src:sma-doc-275587
    loc: sec=h27
    h: 72d122bd272c
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: tbl=8
    h: d0feeb808b79
  review: drafted
- claim_id: c2
  rel: related_to
  target: mit:ac-protective-device-sizing
  note: SMA applies a reduction factor for loads lasting more than one hour when it sizes circuit breakers
    for PV systems.
  cite:
  - src: src:sma-doc-275587
    loc: sec=h27
    h: 72d122bd272c
  review: drafted
  review_note: 'support check: partial - The 0.9 reduction for loads over 1 h is stated as a datasheet
    load factor, but the passage doesn''t explicitly say SMA applies it when sizing circuit breakers (implied
    only).'
- claim_id: c3
  rel: related_to
  target: concept:overcurrent-protection
  note: The optional AC breaker for the SGI 500XT lists a continuous current pickup setting and a continuous
    load rating.
  cite:
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: tbl=8.r1
    h: f63ed489565b
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: tbl=8
    h: d0feeb808b79
  review: drafted
---
A continuous load is a device or circuit that stays on, such as a refrigerator or a Wi-Fi router. A non-continuous load, such as a microwave, air conditioner or electric stove, switches on and off. In the PV sector, loads can run for longer than one hour. SMA treats such a permanent load as a reason to reduce a circuit breaker's usable current, using a factor of 0.9. Breaker sizing also includes other factors, such as breakers mounted side by side with no gap and the ambient temperature inside the distribution board. Some breaker specifications state a continuous load rating. One example is the 80% rating listed for the optional AC breaker of the Solectria SGI 500XT. Equipment datasheets often state their limits as continuous current. One example is the Enphase IQ Combiner 6C, which gives continuous ampere limits for PV, battery, EV charger and backfeed circuits. The NABCEP PV resource guide lists checking continuous load calculations as a design review step under NEC Article 690.

<!-- review notes
- sentence 2: support check: partial - The 0.9 reduction for permanent load >1 h and PV long loads are stated, but 'SMA' isn't named and the reduction is applied to nominal current in a breaker context only implicitly.
- sentence 5: support check: partial - The IQ Combiner 6C passage gives continuous ampere limits for PV, battery, EV charger and backfeed, but the general claim that datasheets often state limits as continuous current isn't stated.
- sentence 6: support check: partial - The passage lists 'Confirm continuous load calculations' under NEC Article 690, but it doesn't identify it as a NABCEP resource guide or a design review step explicitly.
-->
