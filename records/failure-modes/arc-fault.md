---
id: fm:arc-fault
type: FailureMode
name: Arc fault
aliases:
- DC arc faults
- DC series arc fault
- electric arc
- internal arcs
- arcing
claims:
- claim_id: c1
  rel: caused_by
  target: fm:cell-interconnection-failure
  note: If every solder bond or busbar of a cell breaks, string current is blocked. An arc can then form
    if the bypass diode cannot carry the current and the system runs at high voltage.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.4
    h: ca1c4ecfbfd5
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=33.r5
    h: 3b84e4d1e217
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  review: drafted
- claim_id: c2
  rel: caused_by
  target: fm:bypass-diode-failure
  note: An open-circuited bypass diode forces current through the failed cell string, which can lead to
    arcs and fire.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=front
    h: 44eaacc73841
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=33.r5
    h: 3b84e4d1e217
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  review: drafted
- claim_id: c3
  rel: caused_by
  target: fm:connector-defect
  note: Weak or poorly crimped connectors, or mismatched connector types, can arc. A significant share
    of PV fires start at quick connectors.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  review: drafted
- claim_id: c4
  rel: caused_by
  target: fm:junction-box-failure
  note: Internal arcs can form inside the junction box, for example from bad solder contacts.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=front
    h: a85dc942aaf6
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:mechanical-stress
  note: A junction box loosened by delamination puts mechanical stress on the diodes and connectors inside
    it, which can lead to arcs.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:junction-box
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h4
    h: 3be1d95ede61
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:burnt-junction-box
  note: A junction box burnt by an arc at its input lead.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: fig=2
    h: c93b4815ec6c
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:fire-damage
  note: DC arcs usually cause destructive fires. Onsite grass fires have likely been triggered by arc
    faults.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.9
    h: 6199cd73a1f7
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.4
    h: ca1c4ecfbfd5
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=33.r5
    h: 3b84e4d1e217
  - src: src:iea-pvps-t13-33-2025
    loc: fig=96
    h: dc0191fbeb9c
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:high-frequency-current-noise
  note: The arc's length and voltage fluctuate, which produces a high-frequency noise pattern.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.4
    h: ca1c4ecfbfd5
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:waveform-spectrum-analysis
  note: Spectrum analysis of the current and voltage waveforms. Detection is hard because arcs are transient.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.9
    h: 6199cd73a1f7
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.4
    h: ca1c4ecfbfd5
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:ml-fault-classification
  note: Examples are DA-DCGAN on framed loop current and logistic regression on time- and frequency-domain
    features.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=8.19
    h: dd8a86f90fd7
  - src: src:iea-pvps-t13-19-2021
    loc: sec=h61
    h: 2898339d54b0
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:arc-fault-circuit-interrupter
  note: Installed on individual strings.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.9
    h: 6199cd73a1f7
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:safety-isolation
  note: Isolation is the priority when there is evidence of arcing or burning.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=front
    h: a85dc942aaf6
  review: drafted
---
An arc fault is a sudden high-power discharge between two conductors. It can occur in series within a string or in parallel between strings. Arcs usually cause destructive fires, and they have likely started grass fires on site. Common origins are weak or badly crimped connectors, internal arcs in junction boxes, and broken cell interconnections where an open bypass diode cannot carry the current. Look for burnt connectors and burnt junction boxes, especially at the input leads. Arcs are transient and hard to catch. Detection relies on spectrum analysis of string current and voltage, which shows a high-frequency noise pattern. Arc fault circuit interrupters installed on individual strings protect the system. Where arcing or burn evidence is found, isolate the circuit safely first. Then replace the damaged connectors, modules or junction-box assemblies.

<!-- review notes
- sentence 3: support check: partial - Weak/badly crimped connectors, j-box internal arcs and broken interconnections are supported, but 'common origins' ranking is not stated and the diode condition is slightly off: the passages say the bypass diode fails to bypass or is open-circuited.
- sentence 4: support check: partial - Figures show a burned connector and a burnt junction box with an arc at the input lead, but no passage instructs inspecting for them, and 'especially at input leads' is only implied by one example.
-->
