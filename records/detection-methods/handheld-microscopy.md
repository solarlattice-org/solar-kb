---
id: method:handheld-microscopy
type: DetectionMethod
name: Handheld microscopy
claims:
- claim_id: c1
  rel: produces
  target: meas:biofilm-surface-coverage
  note: Handheld digital microscope images of the module surface show bio-soiling. In a dataset of 50,000
    images, mean surface coverage was reported as 3.2 +/- 4.9%, with observed values from 0.2% to 34%.
    These are coverage fractions, not power losses.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h6
    h: 27c24638759c
  review: drafted
---
Handheld microscopy means imaging the module surface up close with a handheld digital microscope. It is used to confirm sub-aerial biofilms when widespread fungal soiling losses are suspected, either alongside or in place of a close visual inspection. Run it after reviewing rainfall and cleaning response: a production deficit that rain does not clear but manual cleaning does points to biological soiling instead of ordinary dust. It matters most when you need to know the contaminant type to choose a cleaning method, judge how likely the soiling is to return, or update the forecast. Biological deposits can be patchy, so sample several array areas instead of relying on one representative module. The method has been used on more than 15 GW of PV assets, and it has found bio-soiling in eight Koppen-Geiger climate zones. The microscope shows what the deposit is and how much surface it covers. To measure the energy loss, compare cleaning records with SCADA, irradiance and weather-normalized production.

<!-- review notes
- sentence 3: support check: partial - The rain/cleaning-response review is stated, but the passages list it as the first step and don't say it is a precondition ('run it after') for microscopy.
- sentence 7: support check: partial - Passages support comparing cleaning records with SCADA, irradiance and normalized production as key evidence, and microscope imaging of surface coverage, but don't explicitly say the microscope can't measure energy loss.
-->
