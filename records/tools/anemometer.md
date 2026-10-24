---
id: tool:anemometer
type: Tool
name: Anemometer
aliases:
- wind meter
- wind speed sensor
- wind sensor
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  rel: part_of
  target: prod:rainwise-pvmet
  note: Optional anemometer mounts on top of the PVmet-500 Series in place of the top cap; Mini Aervane
    (typical) or ultrasonic anemometer supported, selected via register 206.
  cite:
  - src: src:rainwise-pvmet-500-user-manual
    loc: sec=h8
    h: 54eddca45dd4
  - src: src:rainwise-pvmet-500-user-manual
    loc: sec=h15
    h: 0978991050be
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: part_of
  target: prod:alsoenergy-weather-station
  note: 'Anemometer wired to the integrated weather station terminals: speed on WSI (P14), direction on
    WDI (P10), ground on AGND (P11).'
  cite:
  - src: src:man-alsoenergy-alsoenergy-integrated-weather-station-supplement-r2
    loc: sec=h10
    h: 0ff4ec1a8d86
  - src: src:alsoenergy-kb-attachments-files-873-stem-integrated-weather-station-supplement-rev-2-10-2025
    loc: sec=h10
    h: 0ff4ec1a8d86
  - src: src:man-alsoenergy-alsoenergy-integrated-weather-station-supplement-r2
    loc: tbl=2.r4
    h: a3003a3aaee2
  - src: src:man-alsoenergy-alsoenergy-integrated-weather-station-supplement-r2
    loc: tbl=2.r2
    h: 493779192f6d
  - src: src:man-alsoenergy-alsoenergy-integrated-weather-station-supplement-r2
    loc: tbl=2.r1
    h: 3b83dcc8f1fc
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
An anemometer is a sensor that measures wind speed and wind direction at a PV site weather station. On the RainWise PVmet-500 Series it is attached to the top of the station in place of the supplied top cap, and both the Mini Aervane and an optional ultrasonic type are supported, with the type selected in a configuration register. On AlsoEnergy and Stem integrated weather stations, assemble the sensor per its own instructions, point the mount north, and land the speed, direction and ground wires on the matching station terminals. The anemometer is normally mounted about 10 m above ground. Buildings, trees and other obstructions create turbulence, so keep the sensor more than ten times the obstruction height away from it, and treat this as an absolute minimum. During tracker commissioning, check the wind reading by confirming the anemometer values are consistent and match the actual wind; on these trackers the reading is taken through the NCU with its PC software.

<!-- review notes
- sentence 3: support check: partial - Steps are stated for a weather station, but passages don't name AlsoEnergy and Stem specifically; terminal table is only evidenced as shown without brand scope.
- sentence 6: support check: partial - Consistency with real wind and reading via NCU PC software are stated, but 'during tracker commissioning' and 'these trackers' scope is only implied by the section reference.
-->
