---
id: concept:galvanic-isolation
type: Concept
name: Galvanic isolation
aliases:
- transformer isolation
- galvanically isolated
category: Inverters
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:transformerless-inverter
  scope:
    products:
    - prod:delta-electronics-m36u-m42u
    - prod:delta-electronics-m60u-m80u
    - prod:sma-stp-tl-us
    - prod:sma-stp-core1-us
    - prod:sma-shp-peak3
    - prod:sma-sunny-tripower-x
  note: Inverters with no transformer have no galvanic isolation between the DC and AC sides.
  cite:
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=h11
    h: 3a05208e3a80
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h51
    h: '618208203e02'
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=h11
    h: 488dfcb7f5ec
  - src: src:eq-equip-inverters-sma-stp-core1-50-stp-core-1-user-manual-v1-0-50-62
    loc: sec=h26
    h: a6f87864c88b
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h30
    h: 864ad342a1cf
  - src: src:eq-equip-inverters-sma-stp-core1-50-stp-core-1-user-manual-v1-1-50-62
    loc: sec=h25
    h: 7596f69e335e
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-quickrefguide
    loc: sec=h19
    h: 0afac6d3bbdf
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h24
    h: df742a4857a7
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h23
    h: df742a4857a7
  - src: src:sma-doc-278883
    loc: tbl=1.r33
    h: f89cd680b19c
  - src: src:eq-equip-inverters-sma-stp-20000-stp20000tl-us-10-installation
    loc: sec=h29
    h: 2e2bd8701114
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:transformer
  note: A transformer is the isolation method in isolated designs; transformerless designs lack an isolation
    transformer between AC and DC sides.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-sungrow-spec
    loc: tbl=4.r17
    h: 9ab04e54991a
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=h11
    h: 3a05208e3a80
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=h11
    h: 488dfcb7f5ec
  review: drafted
- claim_id: c3
  rel: related_to
  target: mit:isolation-transformer
  scope:
    products:
    - prod:delta-electronics-m36u-m42u
    - prod:delta-electronics-m60u-m80u
  note: The units name the isolation transformer as the element that is absent in transformerless inverters.
  cite:
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=h11
    h: 3a05208e3a80
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=h11
    h: 488dfcb7f5ec
  review: drafted
- claim_id: c4
  rel: related_to
  target: arch:ungrounded-pv-array
  scope:
    products:
    - prod:delta-electronics-m36u-m42u
    - prod:delta-electronics-m60u-m80u
  note: Without galvanic isolation, the connected PV circuits must be kept isolated from ground; neither
    side of the array may be bonded to ground.
  cite:
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=h11
    h: 3a05208e3a80
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=h11
    h: 488dfcb7f5ec
  review: drafted
- claim_id: c5
  rel: related_to
  target: arch:grounded-pv-array
  scope:
    products:
    - prod:delta-electronics-m36u-m42u
    - prod:delta-electronics-m60u-m80u
    - prod:sma-stp-tl-us
    - prod:sma-stp-core1-us
    - prod:sma-shp-peak3
  note: Grounded PV modules must not be operated with non-isolated inverters; connecting them raises an
    insulation error or event. Only the module mounting frames are to be grounded.
  cite:
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=h11
    h: 3a05208e3a80
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h51
    h: '618208203e02'
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=h11
    h: 488dfcb7f5ec
  - src: src:eq-equip-inverters-sma-stp-core1-50-stp-core-1-user-manual-v1-0-50-62
    loc: sec=h26
    h: a6f87864c88b
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h30
    h: 864ad342a1cf
  - src: src:eq-equip-inverters-sma-stp-core1-50-stp-core-1-user-manual-v1-1-50-62
    loc: sec=h25
    h: 7596f69e335e
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-quickrefguide
    loc: sec=h19
    h: 0afac6d3bbdf
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h24
    h: df742a4857a7
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h23
    h: df742a4857a7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c6
  rel: related_to
  target: proto:rs485
  note: Example of galvanic isolation between a sensor supply voltage and its RS485 interface.
  cite:
  - src: src:imt-solar-si-instruction-digital-2017-e
    loc: tbl=7.r9
    h: 6b77e90d9aba
  review: drafted
---
Galvanic isolation means two parts of a circuit have no conductive connection to each other. In inverters a transformer usually provides this isolation, and spec sheets may give the isolation method as Transformer. A transformerless inverter has no isolation transformer between its DC and AC sides, so it has no galvanic isolation. With these inverters, the PV circuits must stay isolated from ground and only the module mounting frames may be grounded. If a grounded PV array is connected to a non-isolated inverter, the inverter shows an insulation error or logs an event. Non-isolated inverters also limit how much PV array capacitance to ground they accept; one SMA manual gives a coupling capacity limit of 12.6 μF. Meters and sensors also use galvanic isolation on their signal ports, for example isolation up to 1000 V between supply and RS485, or inputs and outputs isolated to 2500 volts.

<!-- review notes
- sentence 2: support check: partial - Isolation method Transformer is shown, but 'usually' provides isolation in inverters is only implied, not stated.
- sentence 7: support check: partial - Both isolation figures appear, but the passages don't say these are meters or sensors; the 2500 V item isn't tied to a device type.
- sentence 7: review: partial - Both isolation figures (1000 V between supply and RS485, and 2500 V for all inputs and outputs) are quoted, but the passages never say these are meters and sensors or call them signal ports.
-->
