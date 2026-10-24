---
id: concept:transformerless-inverter
type: Concept
name: Transformerless inverter topology
aliases:
- transformerless
- TL inverter
- transformer-based inverter
- Non-isolated
- TL
category: Inverters
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:galvanic-isolation
  note: Transformerless inverters have no isolation transformer between the DC and AC sides, so they provide
    no galvanic isolation.
  cite:
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=h11
    h: 3a05208e3a80
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=h11
    h: 488dfcb7f5ec
  - src: src:eq-equip-inverters-sma-stp-20000-stp20000tl-us-10-installation
    loc: sec=h29
    h: 2e2bd8701114
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:transformer
  note: This topology leaves out the isolation transformer between the AC and DC sides.
  cite:
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=h11
    h: 3a05208e3a80
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=h11
    h: 488dfcb7f5ec
  - src: src:eq-equip-inverters-sma-stp-20000-stp20000tl-us-10-installation
    loc: sec=h29
    h: 2e2bd8701114
  review: drafted
- claim_id: c3
  rel: related_to
  target: arch:ungrounded-pv-array
  note: Delta transformerless inverters need PV circuits isolated from ground. If the array is grounded,
    the inverter shows INSULATION (E34).
  cite:
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=h11
    h: 3a05208e3a80
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=h11
    h: 488dfcb7f5ec
  review: drafted
  review_note: 'support check: partial - Passages state PV circuits must be isolated from ground and E34
    appears, but they don''t name Delta; the brand is not stated.'
---
A transformerless inverter has no isolation transformer between its DC input and its AC output, so there is no galvanic isolation between the PV array and the grid. Galvanic isolation means there is no conductive connection between two parts of a circuit. Datasheets list this design as transformerless or non-isolated, and some model codes shorten it to TL. Many string inverters from SMA, Fronius, Huawei, CPS and Yaskawa Solectria use this topology. Some transformerless inverters need the PV circuits to stay isolated from ground. If a grounded array is connected, the inverter reports an insulation error. Never connect an AC line terminal to ground on these units: it can damage the inverter and void the warranty. On one SMA design, the AC output and neutral are not bonded to ground inside the inverter. The PV open-circuit voltage must be at least the peak AC line voltage. Transformerless designs can reach high conversion efficiency. One example lists a peak efficiency of 99.0% and a CEC efficiency of 98.5%.

<!-- review notes
- sentence 4: support check: partial - Passages show transformerless topology for several products, but no manufacturer names appear for Fronius, Huawei, Yaskawa; only SMA (STP) and CPS (SCH) model codes suggest brands; 'many' not established.
- sentence 8: support check: partial - Values 99.0% max and 98.5% CEC are listed, but 'peak' vs max and that they are from one example are not confirmed; 'can reach high efficiency' is interpretive.
-->
