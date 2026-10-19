---
id: method:drone-inspection
type: DetectionMethod
name: Drone inspection
aliases:
- UAV
- aerial inspection
- aerial thermography
- RPA
claims:
- claim_id: c1
  rel: produces
  target: meas:ir-hotspot
  note: Drone-mounted IR cameras locate hot spots and electrical mismatches; for cell-damage hotspots
    the drone scan is done under stable irradiance and followed by IV curve comparison and visual check.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=4.1.1
    h: 22b20696439b
  - src: src:pv-root-cause-module-hotspot
    loc: sec=front
    h: 52a281766501
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-19
- claim_id: c2
  rel: produces
  target: meas:row-shadow-line-offset
  note: A drone orthomosaic or oblique images let row-end shadow lines be compared against neighbouring
    rows to reveal tracker twist; confirm with field angle measurements.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: produces
  target: meas:motor-block-aligned-loss
  note: Drone imagery is used together with row-end angle surveys, tracker command logs and normalized
    output to show whether losses follow grade breaks or motor block boundaries.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: produces
  target: meas:snow-cover-imagery
  note: Drone observations of module snow cover are aligned with weather data and SCADA production residuals.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
In a drone inspection, a UAV carrying an infrared, visual or other camera flies over the array along a pre-programmed path that covers the whole site. Aerial IR and visual imaging can find hot spots, bypass diode and junction box failures, cracked glass or cells, delamination, discoloration, open strings and mismatch between tracking systems. For tracker twist, a drone orthomosaic or oblique images let you compare row-end shadow lines with neighbouring rows. For terrain undulation, drone imagery helps show whether losses line up with grade breaks or motor block boundaries. For snow, it gives observations of module cover that you can line up with production residuals. Thermal flights need at least 600 W/m2 of irradiance. Wind speeds above 28 km/h can make it unsafe to control the aircraft, although the limit depends on the drone type. A drone covers a site much faster than a handheld camera: an IR survey of a 4 MWp plant takes roughly 5 to 10 hours with a drone, compared with 15 to 20 hours on foot. Not every thermal anomaly is a failure. Confirm findings against ground data such as IV tracing or EL imaging to avoid false positives. Drone EL and UV fluorescence surveys are harder because they need darkness, often night flying with a higher risk of losing the drone, and EL also requires energizing the strings. Flights must be carried out by a licensed, insured operator after a site risk assessment. Record the date, time, wind and battery levels in a flight log.

<!-- review notes
- sentence 7: support check: partial - u20 supports EL darkness, night flying with higher risk of losing UAV control, and energizing strings, and u3 supports UVF needing dark and risking drone damage, but the higher risk of losing control is stated only for EL, not UVF.
-->
