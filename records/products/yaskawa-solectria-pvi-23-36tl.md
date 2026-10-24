---
id: prod:yaskawa-solectria-pvi-23-36tl
type: Product
name: Solectria PVI 23-36TL
aliases:
- PVI 23 36 TL
- Yaskawa 23 36 TL
- Yaskawa23 to 36 TL
- PVI 23 28 TL
- Solectria 23 28 TL
- PVI 36 TL
- PVI 23-28TL
- PVI 36TL-480
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:yaskawa-solectria
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=h3
    h: 90b8d6ffa7ab
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: sec=h2
    h: 78af2334c646
  review: drafted
  review_note: 'support check: partial - Passages show copyright by Yaskawa - Solectria Solar on manuals,
    but don''t explicitly name the PVI 23-36TL as the product or state it is made by them.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: The datasheet title describes the PVI 23TL, 28TL and 36TL as transformerless three-phase string
    inverters.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: sec=h83
    h: 4eb61ea206be
  review: drafted
---
The Solectria PVI 23-36TL is a Yaskawa Solectria Solar family of transformerless three-phase string inverters made up of the PVI 23TL, PVI 28TL and PVI 36TL. The inverters have an internal arc board for DC arc detection. If that board fails its self-check, the inverter reports an Arc Board Error. An Arc Board Error can come from a communication fault between the arc board and the inverter, or from an abnormal reading inside the arc board. For an Arc Board Error, watch the inverter for five minutes to see whether the alarm clears by itself. If it does not, contact Solectria Customer Service. The PVI 36TL-480 is listed in the Yaskawa Solectria interconnection guidelines for its transformerless PVI inverters.

<!-- review notes
- sentence 1: support check: partial - Datasheet URL supports the 23TL/28TL/36TL transformerless three-phase string inverter grouping and the manuals show Yaskawa Solectria, but a 'PVI 23-36TL family' by that maker is only implied.
- sentence 2: support check: partial - Arc Board Error from internal arc board self-check error is stated, but 'for DC arc detection' purpose is not in the passages.
-->
