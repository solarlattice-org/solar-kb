---
id: method:optical-soiling-sensor
type: DetectionMethod
name: Optical soiling sensor
aliases:
- optical techniques
- Dust IQ
- Mars Soiling Sensor
claims:
- claim_id: c1
  rel: produces
  target: meas:soiling-ratio-below-unity
  note: Optical sensors measure transmission loss from dust on the sensor window and convert it into an
    equivalent loss in short-circuit current and power, which is reported as a soiling ratio or soiling
    rate.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h41
    h: 27f364fa3c19
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h17
    h: 576c10b1646b
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.2.2
    h: 7b13bcc8687f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Passages say optical sensors convert transmission loss into equivalent
    short-circuit current and power loss and that metrics are soiling ratio/rate, but never state the
    ratio is below unity.'
---
An optical soiling sensor estimates soiling loss by measuring how much light dust on its sensor surface reflects or blocks. It does this instead of comparing the electrical output of a clean device with a soiled one. One commercial type uses a pulsed blue LED to measure light scattered back by dust particles and converts the transmission loss into an equivalent loss in short-circuit current and power. Another type uses a camera behind a diffuser with image processing software. Black and white marks on its cover window let it calibrate itself. The factory calibration of the LED sensor uses a reference dust, so recalibrate it on site once local dust has built up. Do this near solar noon by measuring its internal cell under clean and soiled conditions. The result helps you decide when to clean and how much yield soiling is costing the plant. Optical sensors are among the least accurate soiling methods: their cover glass may differ from the array's, and they do not capture soiling that is spread unevenly over modules, which tends to build up on the lower parts of modules. Their advantages are low cost, simple installation, the option of several measurement points and little or no maintenance. Do not judge array soiling from a single sensor. Sensor drift, poor cleaning practice or a local obstruction can produce an apparent soiling signal that does not represent the array.

<!-- review notes
- sentence 4: support check: partial - Passages say it's calibrated with Arizona quartz dust, recalibrated on site as local dust accumulates to 5-10% loss, with internal cell measurements within two hours of solar noon; but the 5-10% condition is omitted and 'near solar noon' is approximate.
- sentence 7: support check: partial - Passage says cell-cell and optical methods are least costly, simple installation, multiple measurement points, and little or no maintenance cost; 'little or no maintenance costs' is paraphrased as maintenance, which is close, but it's stated for both methods, so fine yet slightly different.
- sentence 8: support check: partial - The note says not to rely on a single dirty irradiance sensor for dust soiling, with the same causes, but the statement generalizes to any sensor.
-->
