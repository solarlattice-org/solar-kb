---
id: hazard:battery-thermal-runaway
type: Hazard
name: Battery thermal runaway
aliases:
- thermal runaway
- cell venting
- cascading thermal runaway
- delayed cascading
- deep seated fire
category: Battery
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:cell-thermal-barriers
  note: Thermal or physical barriers between cells and modules, such as aluminum plates, heat-resistant
    plastics, intumescent or phase change materials, slow or stop cascading from cell to cell. Missing
    barriers contributed to cascading at McMicken.
  cite:
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=6.3
    h: 9f4b4a9bddcd
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=4.3
    h: fdfe2f919c6e
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=6
    h: b218da0ba88d
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:battery-liquid-cooling
  note: Cooling plates in contact with a water or glycol loop pull heat away from neighboring cells. The
    report rates this better than air cooling or plain plates that have no heat sink.
  cite:
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=6.3
    h: 9f4b4a9bddcd
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:water-cooling-extinguishment
  note: Cutting off oxygen has little effect on a reaction that feeds itself. Heat has to be removed,
    for example with water, or the fuel has to be dispersed.
  cite:
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=3.2
    h: 336fb71f0d6c
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: tbl=14
    h: b927736a3445
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: controlled_by
  target: mit:battery-compartmentalization
  note: Smaller cells and isolated sub-groups that vent on their own limit the fuel mass, the heat and
    the volume of explosive gas.
  cite:
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=6.3
    h: 9f4b4a9bddcd
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: mit:cell-spacing-air-gap
  note: A designed air gap between prismatic cells cuts heat transfer, but an air gap alone may not prevent
    cascading.
  cite:
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=6.3
    h: 9f4b4a9bddcd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: controlled_by
  target: mit:bess-ventilation
  note: Venting to open atmosphere keeps flammable off-gas from collecting inside enclosures.
  cite:
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=6.3
    h: 9f4b4a9bddcd
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=6
    h: b218da0ba88d
  review: drafted
- claim_id: c7
  rel: controlled_by
  target: mit:thermal-runaway-protection
  conditions: VRLA, lithium-ion and lithium metal polymer battery systems
  quote: shall be provided with a listed device or other approved method to preclude, detect, and control
    thermal runaway
  quote_source: NFPA 1 2009 §52.3.2 (as reproduced in NFPA 855 2020 Annex F)
  cite:
  - src: src:std-standards-nfpa-855-20-pdf
    loc: sec=h61
    h: 702216dd0fff
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: controlled_by
  target: proc:bess-emergency-response
  note: Training and emergency response procedures should cover cascading thermal runaway, flammable gases
    and how to enter a system after a failure.
  cite:
  - src: src:trn-training-bess-dnv-mcmickenfinaltechnicalreport
    loc: sec=6
    h: b218da0ba88d
  review: drafted
---
Thermal runaway in a lithium-ion cell is an internal chemical reaction that releases heat. It can keep going without oxygen and without any visible flame, so it is not the same thing as an ordinary fire. A cell first becomes unstable and gives off gas. Its voltage then drops to zero as an internal short dumps all of its stored energy, and the temperature can briefly reach 300 to 600 °C. Any electrical, thermal or mechanical abuse can start it, and so can an internal defect. At the McMicken BESS, lithium plating and dendrite growth inside a cell caused the internal short. When cells are tightly packed with no thermal barrier, heat passes from cell to cell and module to module. Leftover heat can restart cascading minutes after the fire appears to be out. Runaway without flame gives off toxic and flammable gases such as H2, CO, HCl, HCN and HF. These gases can collect in a closed enclosure and explode. Clean-agent suppression such as Novec 1230 does not stop cascading. Heat must be removed, for example by cooling with water, or the fuel must be dispersed. Design controls include thermal barriers between cells, liquid cooling, air gaps, smaller compartmentalized battery groups, and ventilation to open air. Crews need training and emergency response procedures that cover cascading runaway, flammable gases, and safe entry into a system after a failure.

<!-- review notes
- sentence 5: support check: partial - The passages support flame-free runaway, the toxic and flammable gases listed, and explosion at McMicken, but the gases H2, CO, HCl, HCN and HF are listed as emissions of the secondary burn rather than of flameless runaway.
-->
