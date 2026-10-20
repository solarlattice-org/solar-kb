---
id: method:pid-lab-test
type: DetectionMethod
name: PID susceptibility lab test
aliases:
- IEC 62804
- IEC 62804-1
- PID test
- System Voltage Durability Qualification Test
claims:
- claim_id: c1
  rel: produces
  target: meas:stress-test-power-loss
  note: STC power is measured before and after voltage-bias stress; IEC 62804-type tests use a 5% power
    degradation pass/fail criterion. For PID-p in bifacial PERC, flash testing from the rear shows much
    larger loss than from the front.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h7
    h: 4ba0228f747c
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.5
    h: 9b7c70ce3171
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: drafted
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Bifacial glass/glass PERC modules with EVA under combined-accelerated stress testing with
    -1200 V bias during illumination; relative degradation when flash tested from the front at STC, attributed
    to PID-p on the rear
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passage says ''almost 10%'' under -1200 V combined stress flash
    tested from front, not ''up to 10%'' as a typical value; also a field-like combined test.; possible
    conflict with c3 (same source; check the conditions)'
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 50
    unit: unit:PERCENT
  conditions: Same combined-accelerated stress test of bifacial PERC glass/glass EVA modules with -1200
    V bias; relative degradation when flash tested from the rear at STC
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c2 (same source; check the conditions)
---
The PID susceptibility lab test checks how sensitive a module is to Potential Induced Degradation (PID) by putting a high voltage on the shorted module leads while the outer surfaces of the module are grounded. In the chamber method the module is held at about 60°C and 85% relative humidity for 96 hours under its rated system voltage and polarity, and the humidity itself provides the path to ground. Another method grounds the module face with a conductive electrode such as metal foil, typically at 25°C for 168 hours. This method skips frame features like edge clips or rear rails that would slow PID in the field. Power is measured before and after the stress. A module that loses more than 5% fails, and modules that failed the 60°C test also degraded from PID outdoors. Testing for polarization-type PID (PID-p) calls for UV illumination through a transparent electrode. In bifacial PERC modules the loss shows up much more strongly when the rear side is flash tested. Leakage current can be logged during the test to check that it is stable, but it is a weak indicator of how much the module has degraded. Limits: the test has not been shown to match field behavior for SHJ modules, chamber temperature and humidity must be kept uniform, and long tests at 85°C can set off other degradation mechanisms.

<!-- review notes
- sentence 4: support check: partial - The >5% fail criterion and outdoor failure of modules failing the 60°C test are stated, but measuring power before and after stress is not explicitly stated.
- sentence 7: support check: partial - SHJ relationship unexplored, chamber uniformity issue, and 85°C extended tests causing other degradation are stated, but the 85°C caveat is about extended tests in damp heat with bias and uniformity is an 'issue needing attention'; broadly matches.
-->
