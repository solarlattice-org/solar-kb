---
id: prod:sma-sunny-central-cp-xt
type: Product
name: Sunny Central CP XT
aliases:
- SC CP XT
- SC xxxCP 10
- SC xxxCP XT
- Sunny Central
- SC xxx0CP-10
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=2.1
    h: e4d536c4ed79
  - src: src:kb-sma-sma-america-kb-q-at-night
    loc: sec=h2
    h: d98d49b881b6
  review: drafted
  review_note: 'support check: partial - Passages mention SMA Solar Technology AG and Sunny Central CP
    XT inverters by SMA, which supports manufacturer, though phrasing is indirect.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: PV inverter converting PV DC into grid-compliant AC, feeding the grid through an external downstream
    MV transformer.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=2.1
    h: e4d536c4ed79
  review: drafted
- claim_id: c3
  rel: implements
  target: func:night-reactive-power
  conditions: Only with the optional Q at Night hardware; activated via a parameter.
  note: Q at Night option adds hardware enabling reactive power feed-in without DC voltage present; it
    uses its own operating state and parameters.
  cite:
  - src: src:kb-sma-sma-america-kb-q-at-night
    loc: sec=h8
    h: dd8451eb8a17
  - src: src:kb-sma-sma-america-kb-q-at-night
    loc: sec=h2
    h: d98d49b881b6
  review: drafted
- claim_id: c4
  rel: certified_to
  target: std:iec-60721-3-4
  note: Classified Class 4C2 per EN 60721-3-4; suitable for chemically active environments.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=2.1
    h: e4d536c4ed79
  review: drafted
  review_note: 'support check: partial - Passage says classified under Class 4C2 per EN 60721-3-4, not
    ''certified''; and cites EN, not IEC explicitly.; review: partial - The passage says the inverter
    is classified under Class 4C2 per EN 60721-3-4 and suits chemically active environments, but it does
    not say the product is ''certified'', and it names EN rather than IEC 60721-3-4.'
- claim_id: c5
  rel: compatible_with
  target: prod:sma-hybrid-controller
  conditions: Hybrid Controller listed as optional for Sunny Central CP-XT.
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r13
    h: 60b27eba1709
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:sma-sunny-webbox
  conditions: Via SMA-NET, which supports all Sunny Central devices.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25.r1
    h: 493c54ad9641
  review: drafted
  review_note: 'support check: partial - Passage says SMA-NET supports all Sunny Central devices but doesn''t
    mention Sunny WebBox.'
- claim_id: c7
  rel: requires
  target: role:utility-approval
  note: Settings affecting grid management services must not be deactivated or modified without prior
    grid operator approval.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=2.1
    h: e4d536c4ed79
  review: drafted
- claim_id: c8
  rel: has_hazard
  target: hazard:electrostatic-discharge-damage
  note: All work must comply with ESD protection regulations.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=2.1
    h: e4d536c4ed79
  review: drafted
  review_note: 'support check: partial - Passage requires ESD protection regulations compliance, implying
    ESD hazard, but doesn''t explicitly name damage hazard.'
---
The Sunny Central CP XT is an SMA central PV inverter family that turns DC from the PV array into grid-compliant AC, which an external medium-voltage transformer downstream then feeds into the utility grid. The family includes the SC 500CP-10, 630CP-10, 720CP-10, 760CP-10, 800CP-10, 850CP-10, 900CP-10 and 1000CP-10. Production version E7 ships with OCU and DSP firmware 02.00.01.R. The enclosure is rated IP54 for indoor or outdoor use. The inverter is classified Class 4C2 under EN 60721-3-4, so it can run in a chemically active environment. Only operate it with a suitable MV transformer that is designed for the inverter's pulsed-mode voltages. Connect no more than one inverter per transformer winding, and do not ground the neutral on the low-voltage side. The maximum voltage to ground is plus or minus 1450 V for the 500 to 800 CP XT models and plus or minus 1600 V for the 850 to 1000 CP XT models. With the optional Q at Night hardware, the inverter can supply reactive power when there is no DC voltage. You turn this on with a parameter. Communication goes through the Sunny Central Communication Controller (SC-COM). The family works with the optional SMA Hybrid Controller and with Sunny WebBox over SMA-NET. Follow ESD protection rules and wear PPE. Do not open the unit in rain or above 95 percent humidity, and do not change grid management settings without approval from the grid operator.

<!-- review notes
- sentence 7: support check: partial - SC-COM is listed as communication unit and Hybrid Controller is optional, but Sunny WebBox is not mentioned and 'communication goes through SC-COM' is not explicit.
-->
