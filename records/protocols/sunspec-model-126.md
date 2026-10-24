---
id: proto:sunspec-model-126
type: Protocol
name: SunSpec model 126 Static Volt-VAR
aliases:
- SunSpec 126
- model 126
- volt_var
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: SunSpec groups registers into numbered models, each starting with a header that gives its ID and
    length. Model 126 Static Volt-VAR is one of these models in the XGI 1500 map.
  cite:
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  - src: src:yaskawa-xgi-1500-modbus-map-docr-071063-rev-h
    loc: tbl=7.r15
    h: a80bbc7d1a63
  review: drafted
---
SunSpec model 126 Static Volt-VAR is a SunSpec information model. It is a defined group of Modbus registers that holds the points of a volt-VAR curve. The curve is set with read-write register pairs: V1, V2 and so on hold point voltages in percent of Vref, and VAr1, VAr2 and so on hold the reactive power at each point. The default voltage points are 920, 967, 1030 and 1070 for points 1, 2, 3 and 6. The default VAr values are 300 at point 1, 0 at points 2 and 3, and -300 at points 4 and up. Two read-only scale factor registers turn the raw values into real ones: V_SF scales the percent-Vref voltages and DeptRef_SF scales the dependent variable. Both default to -1. Not every register in a model is supported. Registers marked Reserved should be left alone, and only the registers the map lists as supported should be written.

<!-- review notes
- sentence 2: support check: partial - V1/V2 (% Vref, RW) and VAr1/VAr2 (RW) are shown, but 'and so on' beyond point 2 and the VAr being reactive power at each point (units '-') are only implied.
- sentence 3: support check: partial - Defaults for V1,V2,V3,V6 and VAr1-4,6 match, but VAr5 and points 7+ are not shown, so 'points 4 and up' is not fully supported.
-->
