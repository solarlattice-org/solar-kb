---
id: tool:irradiance-meter
type: Tool
name: Handheld irradiance meter
aliases:
- solar irradiance meter
- solar meter
- reference cell meter
- multifunction irradiance meter
- multi-function PV survey meter
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  attr: accuracy
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Error in total irradiance measured with a reference cell on Si devices when the spectral
    irradiance at reporting conditions is unknown; ranges from negligible to as high as 8-10 % depending
    on clouds, water vapor, aerosols and solar zenith angle
  note: Spectral error is reduced only when the reference cell is calibrated to the local reporting-condition
    spectrum. A matched reference cell does not reduce it.
  cite:
  - src: src:std-standards-standards-testing-performance-testing-astm-e2848-13
    loc: sec=h21
    h: 3bf2166f1b86
  review: drafted
  review_note: 'support check: partial - The 8-10% upper bound for Si with unknown reporting-condition
    spectrum, its dependence on atmospheric factors, and the calibration note are stated, but ''up to
    10%'' as a handheld meter''s accuracy is not stated; the passage concerns reference cells generally.;
    review: partial - The passage supports the 8-10% error for Si devices when the reporting-condition
    spectrum is unknown, its atmospheric dependencies, and the calibration/matched-cell note, but it describes
    spectral error of reference cells in general, not the overall accuracy of a handheld irradiance…'
---
A handheld irradiance meter measures solar irradiance. Many models use a small PV cell as the sensor. A PV cell sensor gives better readings than a pin diode sensor, because a pin diode may not respond to sunlight the same way a PV cell does. Commissioning to IEC 62446 calls for an irradiance reading along with the continuity, open-circuit voltage, short-circuit current and insulation tests. The irradiance reading shows how much solar power is available at that time. Multifunction models also measure compass bearing, inclination, and module and ambient temperature, which makes them useful for site surveys. Some can send readings wirelessly to a PV tester, so irradiance is logged during the electrical tests. During O&M sensor checks, set a clean, recently calibrated handheld sensor at the same pitch and orientation as the site's global horizontal or plane-of-array sensor. Compare the two readings and replace the fixed sensor if it is out of range. O&M tool lists put it alongside a temperature sensor, inclinometer, compass and clamp meter. Accuracy depends on calibration. A reference cell that is not calibrated to the local spectrum can be off by as much as 8-10 % on silicon devices.

<!-- review notes
- sentence 3: support check: partial - The passage lists continuity, Voc, Isc, insulation and irradiance as the absolute minimum testing and says an irradiance meter measures available solar power, but it does not say IEC 62446 specifically calls for the irradiance reading.
- sentence 6: support check: partial - The tool lists include an irradiance meter alongside a temperature sensor, inclinometer, compass and DC clamp meter, but across separate lists and not together in one list.
-->
