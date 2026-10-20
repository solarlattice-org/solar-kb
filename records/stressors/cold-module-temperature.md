---
id: stressor:cold-module-temperature
type: Stressor
name: Cold module temperature
claims:
- claim_id: c1
  attr: degradation_rate
  value:
    nominal: 7
    unit: unit:PERCENT-PER-YR
  conditions: Mean degradation rate of modules affected by cell cracks in cold and snow climate zones
    (Köppen-Geiger D&E), linked to high snow loads and long periods below 0°C
  note: The source gives this as an approximate mean ('ca.'). The same source says cell cracks elsewhere
    usually cost less than 3%/a.
  quote: in cold and snow climate zones (D&E in Köppen and Geiger classification) cell cracks seem to
    have a more pronounced impact
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=h73
    h: 2b81eb1f882b
  review: drafted
---
Cold module temperature is one of the factors that controls how long snow stays on an array. The others are low sun angle, frame geometry, portrait or landscape orientation and tracker position. When snow lasts longer, Snow Accumulation Yield Losses last longer too. Full snow cover blocks irradiance, and patchy snow causes electrical mismatch between clear and covered cells. In cold climates, thermal cycling can get worse and condensation can form inside electronics, causing performance drift or short circuits. Cooling fans may also fail at low temperature. The voltage of crystalline silicon modules rises as they get colder, so inverters and charge controllers have to be sized for this. Cell cracks appear to hurt modules more in cold and snow climates. Where snow loads are high and temperatures stay below 0°C for long periods, choose modules that resist cell cracking. Most modules are designed and type-approved for ambient temperatures from -40°C to +40°C. Installation manuals give -40°C as the lowest operating temperature. In winter, cold-weather inverter behavior, frozen tracker stow positions and sensor icing can happen at the same time as snow events. Filter these out before putting a number on snow loss. To limit cold exposure, use electronics cooled by natural convection rather than fans. Put inverters or charge controllers in a dry, sheltered place, or hang them on the back of the PV rack.

<!-- review notes
- sentence 2: support check: partial - Full cover blocking irradiance and patchy snow causing mismatch are stated, but the passages do not say that longer snow duration lengthens the loss period, though that is implied.
- sentence 4: support check: partial - The passage says c-Si voltage increases as temperature falls and that inverters and charge controllers need to be sized appropriately, but it does not explicitly link the sizing to the voltage rise.
- sentence 6: support check: partial - The passages give an ambient range of -40°C to +40°C for design and type approval, and a manual's operating range of -40°C to 85°C, but they do not say that manuals give -40°C as the lowest operating temperature for most modules.
-->
