---
id: symptom:ct-installation-error
type: Symptom
name: Incorrect current transformer installation
aliases:
- ct cal
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ct-calibration-event
  note: Generac PWRcell 'ct cal' events 0x8069, 0x806A and 0x806C report that a single line (L1, L2 or
    L3) has more than one CT on it, or that a CT is on the neutral wire.
  quote: Line 1 has multiple CTs on it (or a CT is on the neutral wire)
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r8
    h: a859becc7448
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r8
    h: a859becc7448
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r9
    h: 1ef381ab671a
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r9
    h: 1ef381ab671a
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r11
    h: 46554694b404
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r11
    h: 46554694b404
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r10
    h: 8f968d5d6b07
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r10
    h: 8f968d5d6b07
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r12
    h: 571d21a567a0
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r12
    h: 571d21a567a0
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=19.r13
    h: 90787148ab7a
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=20.r13
    h: 90787148ab7a
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:implausible-grid-point-reading
  note: During commissioning, measured values at the grid connection point may be wrong because the current
    transformer is installed or wired incorrectly. Check that the values are plausible and appear at the
    right time.
  cite:
  - src: src:sma-video-online-training-sma-storage-xl-package-01sma-storage-xl-package-safety-installat
    loc: sec=h1
    h: a3cf1627ce8a
  - src: src:sma-video-online-training-commercial-storage-01-sma-commercial-storage-solution-safety-ins
    loc: sec=01
    h: a6a65d1b8963
  review: drafted
---
This symptom means the current transformers (CTs) that measure site current are placed or wired wrongly. Typical errors are more than one CT on one line, a missing CT, or a CT clamped around the neutral wire. On Generac PWRcell inverters it shows up as a 'ct cal' event code. Events 0x8069, 0x806A and 0x806C each point to a single line with multiple CTs. Events 0x806B, 0x806D and 0x806E point to a pair of lines with multiple or missing CTs. For all six codes, also check whether a CT sits on the neutral. Generac says to place the CTs around the main service conductors, between the service meter and the point where the inverter connects. Use one CT per phase, which means two CTs on a 120/240 Vac single-phase service. At commissioning, check that grid connection point readings make sense and appear at the right time. A wrongly installed or wrongly wired CT can make these values wrong. Before you disconnect a CT's current measurement at the device, short its secondary circuit. Opening the secondary while primary current is flowing can cause a voltage peak that damages the CT.

<!-- review notes
- sentence 3: support check: partial - Rows support the pair-of-lines multiple or missing CTs and the neutral wire possibility, but 'also check whether a CT sits on the neutral' as an instruction is only implied by the parenthetical.
- sentence 4: support check: partial - The passage says install CTs around main service conductors between the meter and interconnection point, one per phase, two for 1-phase 120/240 Vac, but does not attribute to Generac explicitly.
-->
