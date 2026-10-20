---
id: symptom:ground-fault
type: Symptom
name: Ground fault alarm or trip
aliases:
- insulation fault
- leakage current high
- Insulation resistance low
- GFCIErr
- IsolationErr
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-insulation-resistance-alarm
  note: Inverter protection code IsolationErr (insulation resistance low); the advised response is to
    isolate strings and add them back one at a time until the alarm returns, then trace that string for
    leakage to earth.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r1
    h: 616d37333b43
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8
    h: ceb3e766d6c1
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=37.r1
    h: 616d37333b43
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=37
    h: ceb3e766d6c1
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - IsolationErr and the add-one-string-at-a-time procedure are stated,
    but nothing says the inverter stops exporting (model_103.W) while the alarm is active.'
- claim_id: c2
  rel: observed_as
  target: meas:high-leakage-current-alarm
  note: Inverter codes GFCIErr (leakage current high) and Fault0090 (dynamic leakage current high); found
    by the same one-string-at-a-time procedure.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r2
    h: aa54fddbab59
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r4
    h: de8c8c13b8b3
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=37.r2
    h: aa54fddbab59
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=40.r4
    h: de8c8c13b8b3
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8
    h: ceb3e766d6c1
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=37
    h: ceb3e766d6c1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - GFCIErr and Fault0090 with the one-string-at-a-time procedure
    are stated, but output dropping to zero on trip is not stated.'
- claim_id: c3
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: A red light on the inverter can mean a ground fault may be present. Do not touch metal parts until
    the right PPE is on.
  cite:
  - src: src:doe-femp-om-small-pv
    loc: sec=h3
    h: 82129b1df69b
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:unequal-pole-currents
  note: Clamp-meter readings on the positive and negative conductors should match. A difference points
    to a possible fault.
  cite:
  - src: src:doe-femp-om-small-pv
    loc: sec=h3
    h: 82129b1df69b
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: observed_as
  target: meas:dc-power-voltage-change
  note: Ground faults were detected as sequential changes in the mean DC power and voltage at the array
    output.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=8.18
    h: f0f4e23dee4d
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - The paper monitors mean DC power and voltage to detect ground
    faults as sequential changes, but the evidence does not say ground faults specifically showed abrupt
    changes in both quantities.'
- claim_id: c6
  rel: observed_as
  target: meas:low-ground-fault-resistance
  note: Ground fault resistance is listed as a monitored inverter parameter. Inverters include insulation
    test circuits that check for ground leakage.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.7
    h: f7efa7d0f7bc
  - src: src:iea-pvps-t13-19-2021
    loc: tbl=5.r8
    h: 794656bed1e1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Inverters'' insulation test circuits are stated and u21 lists
    Ground Fault Resistance, but the evidence doesn''t say it is a monitored inverter parameter indicating
    a low value as a fault observation.'
---
A ground fault happens when current leaks to ground through an unexpected connection or weakened insulation. This lowers efficiency and creates a safety hazard. It usually shows up at the inverter as a low insulation resistance alarm, a high leakage current alarm or a red fault light, and the inverter opens the circuit. If an inverter shows a ground fault light, put on the right PPE before touching any metal on the system. To find the faulted string, isolate all strings at the fuse holders. Then add one string at a time and restart the inverter until the alarm comes back. Trace that string for leakage to earth. Common causes are damaged cable insulation, a wire pinched between the module and the racking, or wire rubbing on a rough conduit edge as it expands and contracts. Connector defects can also cause it, especially poorly crimped or mismatched connectors. Check these by visual and tactile inspection, IR imaging under load and insulation resistance testing. Broken module glass or a cracked backsheet can also cause ground faults. With broken glass, the fault can be intermittent and appear mostly on rainy days. A clamp-meter check showing different current on the positive and negative conductors also points to a fault.

<!-- review notes
- sentence 2: support check: partial - The alarms (IsolationErr, GFCIErr) and red light are in the evidence, and u13 says the inverter opens the circuit, but 'usually shows up' as these is a mild generalization.
-->
