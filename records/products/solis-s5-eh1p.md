---
id: prod:solis-s5-eh1p
type: Product
name: Solis S5-EH1P hybrid
aliases:
- S5-EH1P
- S5-EH1PK-L
- S5-EH1P(3-6)K
- Solis Single Phase Hybrid inverter
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:kb-solis-44002492966-solis-hybrid-inverter-s5-eh1p-3-6-k-l-or-rhi-3-6-k-48es-5g-and-puredr
    loc: sec=front
    h: 45b6ab0b365d
  - src: src:kb-solis-44002492966-solis-hybrid-inverter-s5-eh1p-3-6-k-l-or-rhi-3-6-k-48es-5g-and-puredr
    loc: sec=h1
    h: 02c41dbcacd2
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Described as a single-phase hybrid inverter.
  cite:
  - src: src:kb-solis-44002492966-solis-hybrid-inverter-s5-eh1p-3-6-k-l-or-rhi-3-6-k-48es-5g-and-puredr
    loc: sec=h1
    h: 02c41dbcacd2
  - src: src:kb-solis-44002561750-which-datalogger-is-compatible-with-your-solis-inverter
    loc: tbl=2.r3
    h: f1663c3212e9
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:puredrive-battery
  note: A Solis KB video shows the S5-EH1P(3-6)K-L installed with three Puredrive 5kWh batteries, including
    connection and settings configuration.
  cite:
  - src: src:kb-solis-44002492966-solis-hybrid-inverter-s5-eh1p-3-6-k-l-or-rhi-3-6-k-48es-5g-and-puredr
    loc: sec=h1
    h: 02c41dbcacd2
  review: drafted
- claim_id: c4
  rel: implements
  target: func:self-consumption-optimization
  scope:
    applications:
    - self-consumption
  note: A Solis KB article covers Self-Use mode setup for the S5-EH1P(3-6)K.
  cite:
  - src: src:kb-solis-44002492947-rhi-3-6-k-48es-5g-and-s5-eh1p-3-6-k-self-use-setup
    loc: sec=front
    h: f0fdd1c1925d
  review: drafted
  review_note: 'support check: partial - Only the title of a Self-Use setup article for the S5-EH1P(3-6)K
    is given, which implies a Self-Use mode. The passage has no text that explicitly states self-consumption
    optimization.'
---
The Solis S5-EH1P(3-6)K-L is a Solis hybrid inverter family for single-phase systems. Solis lists it as a Single Phase Hybrid model in its datalogger compatibility table. A Solis knowledge-base video shows it installed with three Puredrive 5kWh batteries. The video covers mounting the inverter, connecting the batteries and configuring settings. Solis publishes a Self-Use mode setup guide for this family. It shares that guide with the RHI-(3-6)K-48ES-5G. Solis points users to its datasheet, its user manual, the certificates download section and the Online Service Center hybrid troubleshooting section. The ratings and certifications themselves are not given in this evidence.

<!-- review notes
- sentence 2: support check: partial - The passage lists Inverter Type: Single Phase Hybrid with the model number. It never says this is a datalogger compatibility table.
-->
