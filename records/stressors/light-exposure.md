---
id: stressor:light-exposure
type: Stressor
name: Sunlight exposure
aliases:
- direct sunlight
- light exposure
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Module power change from light exposure (LID / light soaking), general figure across technologies
  quote: could potentially entail losses up to 30%
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passage says losses ''could potentially entail losses up to 30%'',
    which is an upper bound, not a typical value.'
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 10
    max: 30
    unit: unit:PERCENT
  conditions: Amorphous silicon modules within the first months of outdoor exposure (Staebler-Wronski
    effect)
  note: Crystalline modules lose only a few percent in the first exposure hours and then regenerate over
    several years; CIS modules can instead gain from light exposure.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h4
    h: c8bc75bb2d8d
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Sunlight exposure means light reaching PV modules and other equipment. When modules are first exposed to light, they can lose power in a way that depends on the cell technology. This loss is known as Light Induced Degradation (LID). Crystalline modules lose a few percent of power in the first hours of exposure and then regenerate slowly over several years. Amorphous silicon modules degrade during the first months outdoors because of the Staebler-Wronski effect, and their output then varies with the seasons. CIS modules can instead gain power from light exposure. Light also triggers LID effects linked to the bill of materials, metallic impurities and hydrogen. As a secondary effect, it may contribute to delamination when the encapsulant becomes brittle. When an inverter sits in direct sun, it can overheat and limit its power output. Its electrical parts, gaskets and user interface also wear out early. To reduce exposure, mount inverters in shade or on walls that do not face the sun, or build a simple shade structure over them. Store spare equipment away from direct sunlight. For modules, include stabilization losses in yield assumptions and choose low-LID technologies. Check unexpected early losses with IV curve tracing and flash testing. Switching wafer doping from boron to gallium has largely solved LID.

<!-- review notes
- sentence 1: support check: partial - LID as power change from light exposure and technology-dependent initial loss is stated, but 'light reaching PV modules and other equipment' definition is not.
-->
