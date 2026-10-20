---
id: comp:backsheet
type: Component
name: Backsheet
aliases:
- back-sheet
claims:
- claim_id: c1
  attr: degradation_rate
  value:
    nominal: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Typical mean yearly degradation from yellowing in the discolouration of encapsulant or backsheet
    failure mode
  note: The source mostly links yellowing to the EVA encapsulant. It treats it as a mainly cosmetic issue
    before any current or power loss is detected.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c2
  attr: degradation_rate
  value:
    max: 1
    unit: unit:PERCENT-PER-YR
  conditions: Yellowing-related degradation in hot and humid or moderate climates (discolouration of encapsulant
    or backsheet)
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
---
The backsheet is the rear layer of a PV module. It shields the electrical parts from the environment and keeps the module safe to operate at high DC voltage. Backsheets also give the module mechanical strength and electrical insulation, so if they degrade and crack, the insulation can fail and create a serious hazard. A common build is a UV-resistant fluoropolymer outer layer, an inner PET layer for insulation and an EVA layer for adhesion. Some variants add an aluminium foil as a moisture barrier. Other backsheet types on the market include PVF-PET-PVF (Tedlar), PVDF-PET-PVDF, polyamide-based, pure PET and polyolefin-based films. Some modules use glass or a transparent backsheet on the rear instead. Failure modes that affect the backsheet include delamination, cracking, chalking and discolouration. Delamination can show up as bubbles, ripples or peeling layers, and chalking leaves a white powder that comes off when wiped. Cracks that go through the whole backsheet let moisture in and can make the insulation resistance collapse, especially in wet conditions. This can cause insulation faults that stop inverters from starting in the morning. Local overheating from hot cells can crack the backsheet or make it bubble and deform. In extreme cases the junction box can come off. Inspection is mainly visual, and insulation testing is used for delamination and cracking. Recommended checks include confirming the IEC 61215 certification and the bill of materials, plus continuous ground fault detection.

<!-- review notes
- sentence 7: support check: partial - u28 supports bubbles, deformation and junction box detachment above 170°C, and u13 supports local cracking from overheating, but the 170°C threshold and the pairing of cracking with those effects are not fully stated.
- sentence 8: support check: partial - The passages give VI with INS detection and recommend checking IEC 61215 certification and BOM and ground fault detection at all times. They do not say that inspection is 'mainly' visual or that insulation testing is for delamination and cracking specifically, though the INS detection codes for those defects are close.
-->
