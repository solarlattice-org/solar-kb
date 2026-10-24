---
id: prod:enphase-iq-cable
type: Product
name: Enphase IQ Cable
aliases:
- Q Cable
- QD cable
- IQ Cable
category: Connectors and cable
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:enphase
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=6.2
    h: ad208eaf8f7e
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.6
    h: 9760f9a695b9
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:ac-cable
  note: Continuous 12 AWG, double-insulated, outdoor-rated cable with integrated microinverter connectors.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=6.2
    h: ad208eaf8f7e
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.6
    h: 9760f9a695b9
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.4.2
    h: f467acc1106f
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:enphase-iq6
  note: IQ Series microinverters require the Q Cable; voltage rise tables cover IQ6+.
  cite:
  - src: src:enphase-enphase-iq6-iq6-microinverter-installation-guide
    loc: sec=h1
    h: 538631470d98
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=h39
    h: c2244104b154
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:enphase-iq7
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.6
    h: 9760f9a695b9
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=h40
    h: f179311d6e30
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=h41
    h: b58843104455
  review: drafted
  review_note: 'support check: partial - IQ7 raw cable tables exist for IQ7, 7+, 7X, 7A, implying compatibility,
    but only table titles are given with no explicit statement.'
- claim_id: c5
  rel: compatible_with
  target: prod:enphase-iq8
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=6.2
    h: ad208eaf8f7e
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=h42
    h: 2eb7e7364a1c
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=h43
    h: 0705ef22119f
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=h45
    h: bbff9a167a18
  review: drafted
  review_note: 'support check: partial - IQ8 raw cable table titles imply compatibility, but no explicit
    statement is given; the cable text only says microinverters generally.'
- claim_id: c6
  rel: has_hazard
  target: hazard:electric-shock
  note: Unused connectors must be covered with sealing caps; do not install the terminator with power
    connected.
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=h14
    h: c735af634041
  review: drafted
- claim_id: c7
  rel: has_hazard
  target: hazard:fire
  note: Damaged conductors when stripping the sheath or uncovered connectors pose fire risk.
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=h14
    h: c735af634041
  review: drafted
  review_note: 'support check: partial - Risk of fire is stated, and the stripping and uncovered-connector
    warnings appear, but the passage doesn''t explicitly tie them to fire risk.'
- claim_id: c8
  attr: rated_output_current
  value:
    max: 20
    unit: unit:A
  conditions: Maximum current of Enphase connectors on the cable assemblies; maximum OCPD also 20 A
  cite:
  - src: src:enphase-enphase-iq7-series-integrated-mc4-installation-guide
    loc: sec=h17
    h: bcd686e29a83
  review: drafted
- claim_id: c9
  attr: operating_temperature
  value:
    min: -40
    max: 79
    unit: unit:DEG_C
  conditions: Ambient temperature range for Enphase connectors on the cable assemblies
  cite:
  - src: src:enphase-enphase-iq7-series-integrated-mc4-installation-guide
    loc: sec=h17
    h: bcd686e29a83
  review: drafted
---
The Enphase IQ Cable, earlier called the Q Cable, is a continuous 12 AWG, double-insulated, outdoor-rated AC cable with connectors built in at intervals so microinverters plug straight into it. It is used with IQ Series microinverters, including IQ6, IQ7 and IQ8 models. IQ Series microinverters need this cable and do not work with older Enphase cabling. The cable specification table lists a 600 V voltage rating. The connectors are rated for at most 20 A and a maximum 20 A OCPD, at ambient temperatures from -40 to 79 °C. Enphase recommends keeping voltage rise below 1% in the IQ Cable and below 2% across all of the AC wiring. Accessories include field-wireable connectors, raw cable with no connectors, cable clips, a disconnect tool, sealing caps for unused connectors and terminators for cut cable ends. Shock and fire hazards apply. Cap every unused connector, avoid nicking the conductors when you strip the sheath, and never install the terminator with power connected. Do not plug microinverters into cable that has been left disconnected in wet conditions, because doing so voids the Enphase warranty.

<!-- review notes
- sentence 1: support check: partial - The description is supported and the Q Cable name appears in the passages, but nothing says the Q Cable is the earlier name of the IQ Cable, and 'AC' isn't stated explicitly.
-->
