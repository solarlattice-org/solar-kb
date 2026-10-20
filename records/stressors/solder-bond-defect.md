---
id: stressor:solder-bond-defect
type: Stressor
name: Solder bond defect
aliases:
- cold solder joint
- cold solder point
- weak solder bonds
- failed solder bond
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    min: 5
    max: 10
    unit: unit:K
  conditions: Open-circuit substrings or module strings caused by unreliable or cold solder joints in
    the junction box, compared with active strings in IR thermography
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
---
A solder bond defect is a weak, cold or failing soldered joint. It is usually a production error caused by a soldering temperature that is too low or by chemical residues left on the joint by earlier process steps. Thermal fatigue can break solder bonds. As a joint starts to fail, its resistance and heating rise, and this can discolor the encapsulant and leave burn marks. A weak solder bond can produce a localized hotspot in the module. Persistent hotspots are commonly linked to solder bond defects. If every solder bond on a cell breaks, current in that string is blocked. When the bypass diode cannot carry the current at high system voltage, an arc and fire can result, which is a cell interconnection failure. In junction boxes, cold solder joints can open substrings, cut off the bypass diode or arc and burn the box. These failures typically appear within one to two years of installation and affect a small share of modules from the same production batch. A junction box that runs hotter than its neighbors may point to a cold solder joint. A failed connection to the bypass diode only heats up under shade, so test each string at night with a reverse-bias bypass diode check combined with infrared thermography. To reduce exposure, manufacturers can run a dark reverse voltage sweep and automated visual inspection of the junction box soldering. In the field, if one module fails, all modules should be tested because the fire risk is high.
