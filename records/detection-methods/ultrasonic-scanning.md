---
id: method:ultrasonic-scanning
type: DetectionMethod
name: Ultrasonic scanning
aliases:
- ultrasonic scanner
claims:
- claim_id: c1
  rel: produces
  target: meas:acoustic-delamination-void-map
  note: The ultrasonic scanner gives a higher-resolution view of delaminations that are not obvious, including
    ones that visual inspection cannot find, but each examination takes longer.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
Ultrasonic scanning uses an ultrasonic scanner to check a PV module for areas where its internal layers have come apart. It is used to detect delamination, where the layers of glass, encapsulant, cells and backsheet lose their bond. It is most useful for less obvious delaminations. It shows them at higher resolution than a visual check, which only finds delamination that is easy to see. Like X-ray tomography, it takes longer per examination than visual inspection or thermography. Pulse and lock-in thermography can also find delaminations that are not visible, so they are faster options to consider before a detailed ultrasonic scan.

<!-- review notes
- sentence 1: support check: partial - The passage says an ultrasonic scanner may be used to examine delaminations, but it doesn't describe how the scanner works or say it checks a module for areas where layers have come apart.
- sentence 2: support check: partial - The passage supports using an ultrasonic scanner for delamination, but it only lists some layers (glass, encapsulant, active layers, back layers) and doesn't tie the scanner to all of them.
- sentence 4: support check: partial - The passage says X-ray tomography and the ultrasonic scanner require a greater examination time, but it doesn't compare them with visual inspection or thermography.
- sentence 5: support check: partial - The passage says pulse and lock-in thermography detect delaminations that can't be identified visually, but it doesn't say they are faster or should be tried before an ultrasonic scan.
-->
