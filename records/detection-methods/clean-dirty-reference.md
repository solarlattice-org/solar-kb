---
id: method:clean-dirty-reference
type: DetectionMethod
name: Clean/dirty reference comparison
aliases:
- clean/dirty reference sensors
claims:
- claim_id: c1
  rel: produces
  target: meas:soiling-ratio-below-unity
  note: The soiling ratio comes from the temperature-compensated short-circuit currents of the cleaned
    device and the soiled device, each with its own temperature coefficient.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.2.2
    h: 7b13bcc8687f
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - The passage says the soiling ratio is computed from clean and
    soiled Isc with temperature coefficients, but it never says the ratio is below unity (the formula
    is also not shown).'
- claim_id: c2
  rel: produces
  target: meas:fill-factor-reduction
  note: When soiling is non-uniform, power can drop more than short-circuit current and fill factor can
    fall. Detecting this needs power measurements as well as Isc.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.2.2
    h: 7b13bcc8687f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
A clean/dirty reference comparison is one of the recommended ways to detect soiling losses, alongside soiling stations, performance ratio trends, visual inspection and weather-normalized production comparison. Two PV devices sit side by side: one is cleaned regularly and the other is left to soil naturally. Their current or power outputs are then compared to calculate a soiling ratio. The pair can be two reference cells, two modules, or a cell with a module. A cell pair is cheap, but the cell may soil differently from the modules and will miss non-uniform soiling. A module pair captures non-uniform soiling but costs more to maintain. The clean device should ideally be cleaned every morning, because most dust settles at night. Cleaning it too rarely can make the soiling ratio look much better than it really is. Calculations normally use clear-sky data from the middle of the day, and data is dropped when passing clouds make the short-circuit current change quickly. Logging power as well as short-circuit current is best, because non-uniform soiling can cut power and fill factor more than it cuts current. Do not measure dust soiling with a single dirty irradiance sensor. Sensor drift, poor cleaning or a local obstruction can produce a false soiling signal that does not represent the array.

<!-- review notes
- sentence 1: support check: partial - Clean/dirty reference sensors are listed among detection methods, but the passages do not say 'recommended' in a way that matches, though the list matches the other methods.
- sentence 4: support check: partial - Morning cleaning and night deposition are stated, and inadequate cleaning frequency underestimates soiling ratio; but 'looks much better' is an interpretation of 'underestimation' of the ratio, which is ambiguous in direction.
-->
