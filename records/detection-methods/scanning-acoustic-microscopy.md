---
id: method:scanning-acoustic-microscopy
type: DetectionMethod
name: Scanning acoustic microscopy
aliases:
- SAM
claims:
- claim_id: c1
  rel: produces
  target: meas:acoustic-delamination-void-map
  note: SAM shows whether delamination and voids are present inside the module and where they are. It
    resolves small defects better than pulse thermography.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
Scanning acoustic microscopy is a non-destructive test for finding internal defects in PV modules, including delamination. It shows both whether delamination and voids are present inside the module and where they are. Delamination can form at any interface in the laminate, for example glass to encapsulant, cell to encapsulant, ribbon to encapsulant, or between backsheet layers. Pulse thermography can also find delamination without damaging the module, but acoustic microscopy resolves small defects better. Finding delamination early matters because it lets moisture in faster, which speeds up corrosion and causes current mismatch and power loss.

<!-- review notes
- sentence 5: support check: partial - Passage supports delamination causing faster moisture ingress, corrosion, mismatch and power loss, but does not state that early detection matters.
-->
