---
id: symptom:snail-tracks
type: Symptom
name: Snail tracks
aliases:
- Snail Trails
- snail trail
- Worm Marks
claims:
- claim_id: c1
  rel: observed_as
  target: meas:el-crack-pattern
  note: An EL image of a module with snail tracks shows the cell cracks that the visible tracks follow,
    along with the cell edges.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.3
    h: 43e35c4c6150
  - src: src:iea-pvps-t13-01-2014
    loc: fig=36
    h: e875f24bdfb1
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:high-wet-leakage-current
  note: In wet leakage testing, modules with snail tracks tended to show high leakage currents.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.3
    h: 43e35c4c6150
  - src: src:iea-pvps-t13-01-2014
    loc: fig=39
    h: 48fafd3c7c1e
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:dark-metallization-lines
  note: The silver front-side finger paste turns grey or black at cell edges and along cracks that are
    normally invisible. This can be seen by eye through the front glass.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.3
    h: 43e35c4c6150
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.2.5
    h: d4c58ae820c4
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=10
    h: f95eb9235f8d
  review: drafted
- claim_id: c4
  attr: time_to_onset
  value:
    min: 3
    unit: unit:MO
  conditions: Earliest typical appearance after module installation. Onset is faster in summer and in
    hot climates.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.3
    h: 43e35c4c6150
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  review: drafted
- claim_id: c5
  attr: time_to_onset
  value:
    max: 1
    unit: unit:YR
  conditions: Latest typical appearance after module installation. The source gives an onset window of
    3 months to 1 year.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.3
    h: 43e35c4c6150
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  review: drafted
---
Snail tracks are grey to black lines that you can see by eye through the front glass. They form where the silver finger paste on the cell front discolours. They run along cell edges and along fine cell cracks that would otherwise be invisible, so they show where the cells are cracked. They usually appear a few months to a year after installation, and they appear faster in summer and in hot climates. The discolouration itself is not known to cause a measurable power loss, but the cell cracks it reveals can lower module power. To check how far the cracking goes, take an EL image of the module. It shows the cracks under the tracks. Do not confuse snail tracks with photobleaching. Photobleaching shows up as clear lines along cracks in encapsulant that has turned brown, which takes several years. Modules with snail tracks tend to show high leakage current in wet leakage tests, so check their insulation as well.

<!-- review notes
- sentence 5: support check: partial - The EL image shows the cracks along the tracks, but the passages never recommend EL to check the extent of cracking.
- sentence 6: support check: partial - The passages say photobleaching occurs along cracks in browned EVA, takes several years, and shouldn't be confused with snail tracks, but they don't say it appears as clear lines.
- sentence 7: support check: partial - The tendency to high wet leakage current is stated, but the advice to check insulation is not.
-->
