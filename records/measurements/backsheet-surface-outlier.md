---
id: meas:backsheet-surface-outlier
type: Measurement
name: Backsheet surface profile outlier
---
This signature comes from optical profilometry scans of the module backsheet. The three-dimensional surface relief is captured as two-dimensional profile data. A machine learning algorithm first fits the normal backsheet surface in the scan. It then flags points that deviate from that surface as outliers. The flagged outliers are cracks, bubbles or delamination in the backsheet material. For each crack found, its width and depth are then calculated. The method can quantify cracks over a large physical area. This gives it an advantage over X-ray computed tomography and laser scanning confocal microscopy. It can find cracks before they are visible to the eye, which helps screen backsheet materials after shorter exposure times. Backsheet cracking produces this pattern. Its cracks may be local, run between cells or along busbars, or cover the whole module surface. Backsheet delamination also produces outliers. It shows as a wavy backsheet with local bumps, bubbles or ripples where the layers have separated.
