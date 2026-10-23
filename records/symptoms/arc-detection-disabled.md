---
id: symptom:arc-detection-disabled
type: Symptom
name: Arc detection disabled
aliases:
- Arc Detector switched off
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Fronius Galvo, Primo and Symo inverters, status code 566 shows when the Arc Detector has been
    switched off, for example because arc monitoring is done externally. The code comes back every day
    until the Arc Detector is turned back on. The manuals say it is not an error and is cleared by pressing
    Enter.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r14
    h: 3f109500023b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r10
    h: 1aec4318b5f2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: d0b8e59a980d
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:arc-detector-status-reading
  note: The Arc.det. Status item in the Fronius INFO menu shows the current state of arc detection and
    interruption.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=11.r2
    h: 0e672356a0e5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=13.r2
    h: 0e672356a0e5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=13.r2
    h: 0e672356a0e5
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: sec=h113
    h: 6164b053739a
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h104
    h: 6164b053739a
  - src: src:fronius-fronius-primo-208-240-operating-instructions-42-0410-2116
    loc: sec=h393
    h: 8627ed66f2bf
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h382
    h: 8627ed66f2bf
  review: drafted
  review_note: 'support check: partial - Passages say Arc.det. Status shows the current arc detection/interruption
    status, but don''t mention the Fronius INFO menu or that it reflects disabled state.'
---
On Fronius Galvo, Primo and Symo inverters, a disabled arc detector shows up as status code 566 on the inverter display. The usual reason is that the internal Arc Detector was turned off on purpose, for example because arcs are monitored by external equipment. The code comes back every day until the Arc Detector is switched on again. The manufacturer says this is not an error, and you can confirm the code by pressing the Enter key. To check the current state of arc detection and interruption, open Arc.det. Status in the INFO menu. The Arc Detection setup item has a status view and a self-test start, so you can confirm the detector works after you turn it back on. On some other inverters, arc protection is turned on or off with a parameter that is enabled by default, so check that setting first.

<!-- review notes
- sentence 5: support check: partial - Arc.det. Status displays current status of arc detection/interruption, but the passages don't name the INFO menu.
- sentence 6: support check: partial - Arc Detection setting has ArcDetector Status/Start Self-test options, but passages don't say it's used to confirm operation after re-enabling.
- sentence 7: support check: partial - One passage shows an ARCEnable parameter enabled by default and arc detection enable/disable interface, but 'check that setting first' advice isn't stated and default applies to specific grid codes.
-->
