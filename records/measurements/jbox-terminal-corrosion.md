---
id: meas:jbox-terminal-corrosion
type: Measurement
name: Loose or corroded terminals
aliases:
- Bad contacts
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    min: 5
    max: 10
    unit: unit:K
  conditions: Open-circuit substrings or module strings caused by unreliable (cold solder) connections
    in separated junction boxes, compared with active strings during IR thermography
  note: Refers to open-circuit substrings that result from bad junction box connections, not to the terminal
    itself.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
---
During junction box inspection, this signature shows up as terminals, wire attachments or lids that are loose, oxidised or corroded. Inside the box you may find parts that are disconnected, broken, burned or corroded, and the potting material can hide the fault until it is removed. Bad or corroded contacts raise the internal resistance and heat the junction box, so an infrared camera can show the box as a hotspot. In an IR survey, a wire connection that is clearly hotter than the wire itself should be checked for a loose or corroded contact. Corrosion usually follows moisture getting into a damaged or detached box, for example through a cracked housing or a missing seal at the wire entrance. Mechanical contacts can work loose through day-night and seasonal thermal cycling. This pattern points to junction box interconnection failure or junction box failure, which can lead to power loss, open or short circuits, internal arcing and fire. A junction box that runs hotter than its neighbours can mean a cold solder joint with raised contact resistance.
