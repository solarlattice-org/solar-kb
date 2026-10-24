---
id: concept:bathtub-curve
type: Concept
name: Bathtub failure curve
aliases:
- infant mortality
- wear-out failures
- bathtub curve
category: Reliability
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: metric:mtbf
  note: MTBF relates to the failure rate in the constant-failure segment between infant mortality and
    wear-out.
  cite:
  - src: src:enphase-enphase-reliability-of-microinverters-tech-brief
    loc: sec=h10
    h: f1cdc4d28e32
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c2
  rel: related_to
  target: concept:weibull-distribution
  note: The Weibull shape parameter beta separates infant mortality (beta below 1), random failures (beta
    equal to 1) and wear-out (beta above 1).
  cite:
  - src: src:std-standards-ieee-ieee-gold-book-493-2007
    loc: sec=2.8.5
    h: d4836c342828
  review: drafted
  review_note: 'support check: partial - u6 gives the beta thresholds for infant mortality, random failure
    and wear-out, but it never links the Weibull distribution to the bathtub curve by name.'
- claim_id: c3
  rel: related_to
  target: comp:microinverter
  note: The Enphase tech brief says its microinverters show the typical bathtub failure curve.
  cite:
  - src: src:enphase-enphase-reliability-of-microinverters-tech-brief
    loc: sec=h4
    h: 2940edd16b6b
  - src: src:enphase-enphase-reliability-of-microinverters-tech-brief
    loc: sec=h5
    h: 96f32e7003de
  review: drafted
---
The bathtub curve is the typical shape of a product's failure rate over its service life when you look at a large population of units. The name comes from that shape. The curve has three segments: early failures, also called infant mortality, then a long stretch of constant random failures, and finally wear-out. Infant mortality reflects the quality of the manufacturing process. These failures tend to show up very soon after installation, and the failure rate falls over time. Manufacturers reduce them with in-factory testing. In the flat middle segment, failures are random and the rate stays roughly constant. This segment reflects how reliable the design is in its operating environment, and it is the part of the curve that mean time between failures describes. Getting through infant mortality does not mean a unit will last until wear-out. A low rate of random failures continues throughout the useful life. Wear-out makes the failure rate rise at the end of a product's design life, and this sets its useful service life. In life-data analysis, the Weibull shape parameter shows which segment applies: values below one mean infant mortality, one means random failures (the exponential distribution), and values above one mean wear-out.

<!-- review notes
- sentence 3: support check: partial - u3 supports the manufacturing-quality link, the early timing and the reduction through factory testing, and u4 says the early-life failure rate decreases with time. But 'manufacturers reduce them' is generalized from Enphase's own testing.
-->
