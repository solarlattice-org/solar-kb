---
id: stressor:sodium-ion-migration
type: Stressor
name: Sodium ion migration
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 100
    unit: unit:PERCENT
  conditions: Field power degradation from PID in crystalline silicon modules, where sodium ions drift
    from the front glass to the cell surface; the source says losses can reach almost 100% and may develop
    within several months
  note: Reported as 'almost 100%' for PID overall, not just for sodium migration.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.5
    h: c440122cb9d9
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
Sodium ion migration happens when positive sodium ions (Na+) move out of the module's front or rear glass and through the encapsulant toward the solar cells. A leakage current flows between the cells and ground when the voltage between them is high, and this current drives the ions. The ions build up in the anti-reflective coating near the silicon. From there they enter defects in the p-n junction and create shunt paths. This is the mechanism behind shunting-type potential induced degradation. The shunted cells lower the fill factor of the IV curve. Field losses can grow over several months and reach almost total power loss. Several things speed up the migration: soda-lime glass that contains sodium, low-resistivity EVA encapsulant, and anti-reflective coatings that contain sodium. High humidity, elevated temperature, rain wetting, condensation and soiling also speed it up. It affects strings with a large voltage to ground of a particular polarity. Modules with p-type cells degrade in negative-polarity strings. Sodium can also come from handling during cell production. Na+ that penetrates the passivating dielectric can degrade surface passivation in a related mode called PID-penetration. Exposure can be reduced by using modules designed to resist PID and higher-resistivity encapsulation. One source reports that shunting-type PID has not been observed in current cell types. Affected modules can often recover by applying reverse voltage, for example at night. Recovery is slower without accelerating factors.

<!-- review notes
- sentence 7: support check: partial - PID-resistant modules and the note that PID-Shunting has not been observed in current cell types are stated, but higher-resistivity encapsulation is only mentioned as mitigating PID-Delamination, not shunting.
-->
