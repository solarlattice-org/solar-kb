---
id: concept:maximum-power-point
type: Concept
name: Maximum power point
aliases:
- MPP
- Pmax point
- Pmp
- point de puissance maximale
- punto di massima potenza
- Punkt maximaler Leistung
category: Modules
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:iv-curve
  note: The MPP is the operating point on the I-V curve, at its knee, where current times voltage is greatest.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h648
    h: c818e97d970e
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h193
    h: b6d6595edd52
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h70
    h: 0e13bed67f14
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1
    h: 8864236b9c21
  review: drafted
- claim_id: c2
  rel: related_to
  target: func:mppt
  note: MPPT is the process or electronics that keep a PV array at its MPP as conditions change.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1
    h: 8864236b9c21
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h71
    h: 7b4492be8d05
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=20.r1
    h: 43bb41054db8
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:open-circuit-voltage
  note: The maximum power voltage Vmp is typically about 70% to 80% of Voc.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h70
    h: 0e13bed67f14
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1
    h: 8864236b9c21
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:short-circuit-current
  note: The maximum power current Imp is typically about 90% of Isc.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h70
    h: 0e13bed67f14
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1
    h: 8864236b9c21
  review: drafted
- claim_id: c5
  rel: related_to
  target: state:mpp-operation
  note: An inverter can regulate DC voltage so that it runs at the MPP, or hold the voltage constant with
    no MPP tracking.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=20.r1
    h: 43bb41054db8
  review: drafted
---
The maximum power point is the operating point on the current-voltage curve of a PV cell, module, string or array where current times voltage reaches its maximum. It sits at the knee of the I-V curve and is the most efficient operating point for the irradiance and cell temperature at that moment. The MPP keeps moving as irradiance and temperature change, so the inverter or charge controller has to keep tracking it. This tracking is called maximum power point tracking (MPPT). The connected load sets the operating point according to Ohm's law. The load resistance that gives maximum power equals Vmp divided by Imp. A battery load fixes the operating point at the battery voltage. An interactive inverter looks for the MPP as long as the array voltage stays within the inverter's limits. Module labels and datasheets list rated Vmp, Imp and maximum power, which are used for design and for comparison with field measurements.

<!-- review notes
- sentence 3: support check: partial - Passages say the MPP changes with irradiance and temperature and define MPPT, but do not explicitly say the inverter or charge controller must keep tracking because it moves.
- sentence 6: support check: partial - Passages say rated I-V parameters are on product labels and used for design and field comparison, and u22 shows Imp, Vmp, Pmax listed, but datasheets are not explicitly mentioned.
-->
