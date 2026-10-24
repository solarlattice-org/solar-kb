---
id: concept:harmonic-distortion
type: Concept
name: Harmonic distortion
aliases:
- THD
- total harmonic distortion
- current harmonics
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: method:waveform-spectrum-analysis
  note: Advanced meters use waveform capture to show the harmonic content as a spectrum or as a table
    of magnitudes and phase shifts.
  cite:
  - src: src:eq-equip-meters-shark-shark-200-shark-200-data-logging-power-and-energy-meter-user-manual-e149701
    loc: sec=h20
    h: 22bb72e3412e
  review: drafted
- claim_id: c2
  rel: related_to
  target: meas:ac-line-thd-high
  note: THD is calculated per phase for current and voltage channels, as the rms of the harmonic components
    divided by the rms of the fundamental.
  cite:
  - src: src:sel-735-im-20250228
    loc: sec=h507
    h: 4930f12c9b73
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:current-transformer-operation
  note: Instrument transformers pass almost no information above about 1200 Hz, so they can hide higher-order
    harmonics.
  cite:
  - src: src:eq-equip-meters-shark-shark-200-shark-200-data-logging-power-and-energy-meter-user-manual-e149701
    loc: sec=h20
    h: 22bb72e3412e
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:short-circuit-ratio
  note: Current distortion limits for distribution systems get higher as the ratio of short-circuit current
    to load current (Isc/IL) increases.
  cite:
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: tbl=74
    h: 8372cb978380
  review: drafted
- claim_id: c5
  rel: related_to
  target: prod:fronius-symo
  note: Total harmonic distortion is listed in the inverter's technical data.
  cite:
  - src: src:eq-equip-inverters-fronius-symo-operating-manual
    loc: tbl=56.r12
    h: bf2f0a482f61
  - src: src:eq-equip-inverters-fronius-symo-operating-manual
    loc: tbl=44.r16
    h: 5bbca956ecb5
  - src: src:eq-equip-inverters-fronius-symo-operating-manual
    loc: tbl=38.r16
    h: 867e2e488da6
  review: drafted
---
A distorted waveform can be broken down into a set of sine waves at whole multiples of the fundamental frequency. These higher-frequency parts are called harmonics, and the low-order odd ones (3rd, 5th, 7th and 9th) have traditionally been the most common. Inductive and capacitive impedance change with frequency. A system that behaves normally at 60 Hz can therefore behave very differently when harmonics are present. Total harmonic distortion (THD) is the rms value of the harmonic components divided by the rms value of the fundamental. Meters calculate it per phase for both currents and voltages. Instrument transformers pass almost no information above about 1200 Hz, so monitoring through CTs can hide higher-order harmonics. Not seeing distortion does not prove it is absent. Advanced meters offer waveform capture, which shows one or two cycles as a waveform, a harmonic spectrum or a table of harmonic magnitudes and phase angles. Inverter datasheets list THD as an output specification. Across Fronius Symo models the listed values range from below 1% to below 3.5%. Current distortion limits for distribution systems depend on the ratio of short-circuit current to load current. The total demand distortion limit rises from 5% in the lowest ratio band to 20% above a ratio of 1000.

<!-- review notes
- sentence 6: support check: partial - Values <1% to <3.5% appear, but passages don't say datasheets generally list THD or identify them as Fronius Symo models explicitly.
-->
