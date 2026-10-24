---
id: concept:dc-ac-ratio
type: Concept
name: DC/AC ratio
aliases:
- inverter loading ratio
- ILR
- DC/AC oversizing ratio
- DC to AC ratio
- DC Oversizing
- DC Ratio
- DC oversizing range
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: metric:clipping-loss
  note: Clipping losses depend on the energy available relative to the inverter nameplate; above about
    3% clipping, raising the ratio further may bring diminishing value.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h68
    h: dd07c575ad31
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: related_to
  target: fm:inverter-clipping
  note: The inverter caps AC output at its rating however far the array is oversized.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-16-home-hub-oversizing
    loc: sec=h3
    h: 35645465a4f3
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h68
    h: dd07c575ad31
  review: drafted
- claim_id: c3
  rel: related_to
  target: stressor:high-dc-ac-ratio
  note: Going above the recommended or maximum ratio can damage the inverter and void the warranty.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h63
    h: 2e0d4d03ed65
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h88
    h: 2e0d4d03ed65
  - src: src:eq-equip-inverters-solectria-xgi-1500-xgi-1500-166-manual-rev-p-17-oct-2022
    loc: sec=h45
    h: ae2ccecbdb59
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:standard-test-conditions
  note: The ratio uses DC power rated at STC.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h68
    h: dd07c575ad31
  - src: src:se-academy-home-hub-technical-essentials-na-technical-16-home-hub-oversizing
    loc: sec=h3
    h: 35645465a4f3
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:nameplate-rating
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h68
    h: dd07c575ad31
  - src: src:se-academy-home-hub-technical-essentials-na-technical-16-home-hub-oversizing
    loc: sec=h3
    h: 35645465a4f3
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:short-circuit-current
  note: The DC/AC ratio limit and the Isc limit both have to be met.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h63
    h: 2e0d4d03ed65
  - src: src:eq-equip-inverters-solectria-xgi-1500-xgi-1500-166-manual-rev-p-17-oct-2022
    loc: sec=h45
    h: ae2ccecbdb59
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=h47
    h: ae2ccecbdb59
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: related_to
  target: arch:single-axis-tracker-plant
  note: The suggested oversizing range depends on the racking style.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=12
    h: 58a9cc15ba00
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=12.r2
    h: 1c8a31b6cbec
  review: drafted
---
The DC/AC ratio compares the DC power of the PV array with the AC power rating of the inverter. A ratio above one is called DC oversizing. For example, 13,000 W DC on a 10,000 W inverter is oversized to 130 percent. The inverter still delivers no more than its rated AC power, however large the array is. The ratio uses STC module ratings and ignores project details. Actual performance depends on location and racking style, so a tracker or a sunny site gains more from the same ratio. Extra DC power above the inverter nameplate is lost as clipping. Once clipping goes above about 3 percent, a higher ratio may add less and less value. Schneider suggests narrower oversizing ranges for trackers than for fixed tilt: 1.25 to 1.35 for steep fixed tilt, 1.20 to 1.30 for single-axis and 1.10 to 1.20 for two-axis trackers. Inverter manuals set a maximum allowed ratio, for example 2.0 to 2.6 across XGI 1500 variants. At sites that often see more than 1000 W/m2, a lower ratio is recommended. Going above the recommended ratio, or above the short-circuit current limit, can damage the inverter and void the warranty. Size strings to meet both limits.

<!-- review notes
- sentence 1: support check: partial - Passage defines DC oversizing as DC power available greater than inverter can convert, with an example ratio; the explicit 'ratio above one' is only implied by 130% example.
- sentence 3: support check: partial - STC basis, ignoring project configuration, and dependence on location and racking are stated, but the claim that trackers/sunny sites gain more is stated as performance advantage, roughly consistent; 'gains more from the same ratio' is a mild extrapolation.
- sentence 4: support check: partial - Diminishing value above 3% clipping is stated, but the passage does not say that extra DC above nameplate is lost as clipping in those words.
- sentence 5: support check: partial - The ranges are correct, but 'Schneider suggests narrower ranges for trackers' is inaccurate: ranges are the same width and merely lower.
- sentence 6: support check: partial - Max ratios of 2.0-2.6 for XGI 1500 variants and lower ratio recommendation above 1000 W/m2 are stated, though the XGI variants listed are 2.0-2.6 and the high-irradiance note concerns other inverters (limit 1.5).
-->
