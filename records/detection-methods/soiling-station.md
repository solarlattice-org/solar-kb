---
id: method:soiling-station
type: DetectionMethod
name: Soiling station
aliases:
- soiling reference modules
- soiling sensor
- soiling monitors
- DustIQ Soiling Station
claims:
- claim_id: c1
  rel: produces
  target: meas:soiling-ratio-below-unity
  note: Soiling ratio is the soiled device output divided by the clean reference output. It is usually
    approximated from temperature-corrected short-circuit currents and falls below one as dust builds
    up. The soiling rate, in %/day, is the slope of this ratio between cleaning events.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.1
    h: 1bd67b0ecb1e
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.2.2
    h: 7b13bcc8687f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
A soiling station measures how much dust or dirt on the modules is cutting output. Its data help plan cleaning, and it is one of the data sources used to detect granular dust soiling losses and soiling losses in general. Electrical stations compare two PV devices placed side by side. One device is cleaned regularly and the other is left to soil, and the station records the current or power of each. The pair can be two reference cells, two modules, or a cell plus a module. A reference cell may not soil the same way a module does and does not capture uneven soiling, while a module-module setup needs more cleaning work. Ideally the clean reference is cleaned every morning, because most dust settles at night. If it is cleaned too rarely, the station will understate the soiling loss. Readings are normally evaluated around midday under clear skies with effective irradiance above 500 W/m2. Fixed arrays are measured within two hours of solar noon. Short-circuit current alone can understate the loss when dust collects unevenly, for example along the bottom cell row. For that reason, stations should log power as well as current. Soiling often varies across a site, so IEC 61724-1 recommends more than one sensor on sites larger than five MW. Choose mounting spots based on the surroundings and the prevailing wind. A single dirty sensor is not enough to confirm soiling, because sensor drift, poor cleaning or a local obstruction can produce a false soiling signal.

<!-- review notes
- sentence 7: support check: partial - IEC 61724-1 recommends more than one sensor for sites over five MW, but only when expected yearly losses exceed two percent, a condition omitted; mounting guidance on surroundings and wind is supported.
-->
