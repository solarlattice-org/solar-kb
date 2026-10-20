---
id: method:junction-box-inspection
type: DetectionMethod
name: Junction box inspection
aliases:
- junction-box checks
claims:
- claim_id: c1
  rel: produces
  target: meas:visible-burn-marks
  note: Burnt or deformed junction boxes are seen when heat from a failed bypass diode builds up inside
    the box; visual burn-mark checks are listed with junction-box checks for diode failure.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: fig=6
    h: 7ea1ad25052d
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=front
    h: 44eaacc73841
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:ir-hot-connection
  note: A junction box that runs hotter than its neighbours in an infrared image can point to a loose
    connection or a cold solder joint inside it.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c3
  rel: produces
  target: meas:open-junction-box
  note: Open, badly closed, poorly bonded or detached boxes are found by visual inspection.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: fig=30
    h: e257fda96cf2
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r2
    h: a7af7c498f88
  review: drafted
- claim_id: c4
  rel: produces
  target: meas:jbox-terminal-corrosion
  note: Loose, oxidised or corroded junction box parts are listed as junction box findings.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=6.r7
    h: 01b6bd9e4187
  review: drafted
  review_note: 'support check: partial - The table row lists junction box loose, oxidation, corrosion,
    but ''terminals'' and the ''finding of inspection'' framing are only loosely stated.'
- claim_id: c5
  rel: produces
  target: meas:jbox-poor-wiring
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: fig=30
    h: e257fda96cf2
  - src: src:pv-root-cause-junction-box-failure
    loc: fig=3
    h: 6b74b49772f8
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Junction box inspection means checking the module junction box by eye and with a thermal camera. It is used together with diode checks, IV tracing and insulation checks when damage is suspected. For bypass diode failure, junction-box checks are combined with IV curve signatures, infrared thermography and visual searches for burn marks to find diodes that are open or shorted. Visual inspection is the usual way to find junction box failures, such as boxes that are open, badly bonded to the backsheet, poorly wired, loose, oxidised or corroded. Heat from a failed bypass diode can deform or burn the junction box, so burn marks and melting on the box are key signs. An infrared camera can find higher resistance or mismatch in the box. A box that runs hotter than the others may point to a cold solder joint. Some faults cannot be found this way. An open connection that only matters under shade stays hidden without shading or a night reverse-bias string test, and a failed diode cannot always be told apart from a bad joint without opening the box destructively. For safety, remember that parts inside DC boxes fed by a PV array may still be live after isolation. Isolate any module that shows arcing or burn evidence. If one junction box failure is found, test all modules because the fire risk is high.

<!-- review notes
- sentence 4: support check: partial - Heat from bypass diode failure deforming or burning the box is stated, but 'melting' and 'key signs' are not.
-->
