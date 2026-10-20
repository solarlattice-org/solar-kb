---
id: stressor:boron-oxygen-defects
type: Stressor
name: Boron-oxygen defects
aliases:
- BO-LID
- B-O LID
- Boron-Oxygen complexes
- boron-oxygen complex
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: LID tied to boron and oxygen content in p-type boron-doped crystalline silicon cells, during
    the first days of sun exposure
  note: The source says LID is limited to this range. It contrasts this with LeTID, which can reach up
    to 10% and comes on top of the LID loss.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: drafted
---
Boron-oxygen defects are complexes that form in boron-doped silicon cells when leftover oxygen from manufacturing is exposed to light or current. Once formed, these complexes trap electrons and holes so they no longer produce current, which lowers the cell's electrical output and drives Light Induced Degradation (LID). Czochralski-grown monocrystalline cells are hit hardest because they contain a lot of oxygen. Mainly p-type boron-doped mono and multicrystalline modules are affected. The loss appears early, within the first hours to days of sun exposure, and shows up mainly as lower STC power, with some drop in short-circuit current and open-circuit voltage. The degradation rate rises with the boron concentration and even more strongly with the oxygen concentration. Over time, hydrogen can return the cell to a regenerated state, but this slow recovery is hard to measure in the field. Manufacturers usually cover this loss in the module's power rating and tolerance. It only counts as a module failure if the rating does not allow for it. Exposure is reduced by using gallium instead of boron as the dopant in p-type cells, or by using n-type cells. Even so, small boron impurities can still cause some LID. Most manufacturers now stabilise cells in-line during production. Owners can also check the bill of materials for the cell type and verify power warranties.
