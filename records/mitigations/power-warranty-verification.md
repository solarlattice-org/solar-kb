---
id: mit:power-warranty-verification
type: Mitigation
name: Power warranty verification
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: LID in crystalline silicon modules, occurring within the first days of sun exposure; this
    is the loss that power warranty checks are meant to cover
  note: The figure is for the linked failure mode (LID), not for the mitigation. The same source says
    LeTID can reach up to 10% on top of the LID loss.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
---
Power warranty verification is a recommended preventive action for light induced degradation (LID and LeTID) in crystalline silicon modules. For modules whose output does not match their rating, it is listed together with checking data sheet conformity and buying modules from trusted manufacturers. Manufacturers usually allow for LID when they label modules and set the first-year warranty, but a high LeTID rate that is hard to predict is a much bigger issue for warranties. Combine it with checking that the manufacturer uses LeTID-stable cells, asking for test reports that give percent power loss, agreeing on a tolerated loss in the contract and verifying the bill of materials. If underperformance shows up, have it confirmed by an accredited PV test laboratory, then claim for the missing power, following the warranty provider's formal procedure and archiving all communications. Mishandling can void a warranty, for example storing modules so that rain destroys the packaging, or partially shading thin-film modules. A warranty may pay for a replacement module but not for the labour to remove, ship and reinstall it, and the manufacturer may choose to repair, replace or supply extra modules instead. Proving that a module underperforms is difficult and may require an expensive standardized test of each module.
