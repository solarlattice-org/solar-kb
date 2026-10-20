---
id: method:accredited-lab-test
type: DetectionMethod
name: Accredited laboratory testing
claims:
- claim_id: c1
  rel: produces
  target: meas:pmax-below-rated
  note: The lab test confirms module underperformance, so the operator can claim for the missing power.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=20.r1
    h: 18272d94a323
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=20
    h: 6442f10b15ac
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=39.r1
    h: 18272d94a323
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=39
    h: 6442f10b15ac
  review: drafted
---
Accredited laboratory testing means sending modules to an accredited PV test laboratory, which confirms whether they really produce less power than they should. It is listed as a corrective action: once the lab confirms the underperformance, the owner can claim for the missing power. Light induced degradation is a power loss caused by exposure to light, and it can be large enough to justify lab confirmation. An optional preventive step is independent third-party testing of sample modules at the factory gate or when they arrive on site, backed by a contractual agreement. Accredited labs also test non-standard mounting setups, such as facade mounting. Accurate IV measurements need test equipment and irradiance reference devices calibrated by, or traceable to, an accredited laboratory. Even in a lab, the certified accuracy of a module IV measurement has limits, and most PV laboratories find it hard to do better than a few percent.

<!-- review notes
- sentence 3: support check: partial - LID is power change from light exposure with losses up to 30%, but passages do not link it to lab confirmation justification, and 'up to' is a bound.
- sentence 5: support check: partial - Passage mentions testing of non-standard mounting configurations by an accredited lab (e.g. facade) as a mitigation, but not that labs 'also test' them as general practice; close paraphrase though.
-->
