---
id: method:optical-profilometry
type: DetectionMethod
name: Optical profilometry
aliases:
- profilometry scans
claims:
- claim_id: c1
  rel: produces
  target: meas:backsheet-surface-outlier
  note: A machine learning algorithm fits the backsheet surface in the profilometry data and flags outliers.
    These outliers can be cracks, bubbles or delamination, and crack width and depth are then calculated
    for each crack.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: fig=66
    h: 7e4162410fbe
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h57
    h: 6959b882ad79
  - src: src:iea-pvps-t13-16-2021
    loc: fig=67
    h: 8e696a6b320a
  review: drafted
---
Optical profilometry scans the backsheet surface of a module. It records the three-dimensional crack topography as two-dimensional profile data. A machine learning algorithm finds the backsheet surface in the scan and flags outliers from that surface. These outliers mark cracks, bubbles or delamination. Crack width and depth are then calculated for each crack found, which is how the method confirms backsheet cracking. It can measure cracks over a large physical area, which gives it an advantage over X-ray computed tomography and laser scanning confocal microscopy. It can find cracks before they can be seen, which shortens the exposure testing needed to spot materials that form small microcracks. Backsheet cracking matters because it can break down the module's electrical insulation and create a serious safety hazard.

<!-- review notes
- sentence 3: support check: partial - Width and depth are calculated per identified crack, but the passages do not say this is how the method confirms cracking.
-->
