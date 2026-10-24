---
id: prod:abb-trio-20-27-6-tl-outd
type: Product
name: TRIO-20.0/27.6-TL-OUTD string inverter
aliases:
- TRIO-20.0-TL-OUTD
- TRIO-27.6-TL-OUTD
- TRIO-20.0/27.6-TL-OUTD
- TRIO-20.0-27.6-TL-OUTD-US
- TRIO-20.0/27.6
category: Inverters
make: abb
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fimer
  cite:
  - src: src:abb-fimer-string-inverter-product-manual-appendix-revg
    loc: tbl=1.r7
    h: 9043c0747fe7
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    min: 20
    max: 27.6
    unit: unit:KiloW
  conditions: Family range across TRIO-20.0 and TRIO-27.6 models
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: sec=h1
    h: 062b2b34bfe5
  review: drafted
- claim_id: c3
  attr: rated_power
  value:
    nominal: 20000
    unit: unit:W
  conditions: TRIO-20.0-TL-OUTD, nominal output power (US quick installation guide)
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-us-quick-installation-guide-revb
    loc: tbl=6.r1
    h: a29b34e6b86c
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: rated_power
  value:
    nominal: 27600
    unit: unit:W
  conditions: TRIO-27.6-TL-OUTD, nominal output power (US quick installation guide)
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-us-quick-installation-guide-revb
    loc: tbl=6.r1
    h: a29b34e6b86c
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c5
  attr: rated_power
  value:
    nominal: 20
    unit: unit:KiloW
  conditions: TRIO-20.0-TL-OUTD-S2X-400 and -S2F-400 variants, nominal output power
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=6.r4
    h: 7203cf846790
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=6.r3
    h: 94bdf29b77b5
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: rated_power
  value:
    nominal: 27.6
    unit: unit:KiloW
  conditions: TRIO-27.6-TL-OUTD-S2X-400 and -S2F-400 variants, nominal output power
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=6.r4
    h: 7203cf846790
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=6.r3
    h: 94bdf29b77b5
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c7
  attr: efficiency
  value:
    nominal: 98.2
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency, both TRIO-20.0 and TRIO-27.6 models
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-us-quick-installation-guide-revb
    loc: tbl=6.r32
    h: a34e64596661
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: efficiency
  value:
    nominal: 97.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, both TRIO-20.0 and TRIO-27.6 models
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-us-quick-installation-guide-revb
    loc: tbl=6.r33
    h: a69c9798ea52
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions)
- claim_id: c9
  rel: implements
  target: func:reverse-polarity-protection
  note: Passive inverter protection only, per the US quick installation guide.
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-us-quick-installation-guide-revb
    loc: tbl=6.r27
    h: 055fd464146b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c10
  rel: implements
  target: func:surge-protection
  note: DC and AC overvoltage surge arresters are fitted on S2X-400 variants only; S2F-400 variants have
    none.
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=6.r4
    h: 7203cf846790
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=6.r3
    h: 94bdf29b77b5
  review: drafted
---
The TRIO-20.0/27.6-TL-OUTD is a family of three-phase string inverters made by FIMER, covering nominal output powers from 20.0 kW to 27.6 kW. The TRIO-20.0 model has a nominal output of 20000 W and the TRIO-27.6 model has 27600 W. The maximum output power is higher, at 22000 W and 30000 W. Both models list a maximum efficiency of 98.2 percent, a CEC efficiency of 97.5 percent and a power factor above 0.995. Each S2X and S2F variant has two input channels with quick-fit connectors (four pairs per channel on the 20.0 kW model, five on the 27.6 kW model), a combined AC+DC disconnect switch, and string protection fuses. S2X variants have DC and AC overvoltage surge arresters. S2F variants do not have them. Reverse polarity protection is passive only, and the US version carries the cCSAus safety approval. Units built from week 27 of 2015 use Weidmüller WM4 C DC connectors. The manual has graphs showing how output power is reduced at high altitude and when the input voltage is too high or too low.

<!-- review notes
- sentence 1: support check: partial - The passages support FIMER, the 20.0 to 27.6 kW range and the three-phase models. They do not explicitly say the family consists of string inverters made by FIMER, although the u1 title says string inverters.
- sentence 7: support check: partial - The passages support the WM4 C connectors effective from week 27 of 2015 and the derating graphs for input voltage and altitude. The statement says high altitude and does not mention that the graphs show derating as a function of altitude. 'Built from week 27' is also a loose paraphrase of 'effective from'.
-->
