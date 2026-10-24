---
id: concept:temperature-coefficient
type: Concept
name: Temperature coefficient
aliases:
- Voc temperature coefficient
- Pmax temperature coefficient
- temperature coefficient of power
- Temperature coefficient of voltage
- Array Power-Temperature Coefficient
- Open-circuit voltage temperature coefficient
- Temperature coefficient of P MPP
- voltage-temperature coefficient
category: Modules
concept_kind: physics
claims:
- claim_id: c1
  rel: explains
  target: concept:string-sizing
  note: The Voc temperature coefficient sets the cold-weather open-circuit voltage, which is used to check
    that the series string stays below the maximum system voltage.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h73
    h: 0b03943db93d
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h389
    h: c9e8498c8209
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1.2
    h: 54888f628680
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h76
    h: 2db32337047e
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:open-circuit-voltage
  note: Voc rises as temperature drops below 25 °C; the coefficient is used to translate it.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h18
    h: 88505e777c47
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h389
    h: c9e8498c8209
  - src: src:eq-equip-inverters-sungrow-sungrow-sg60ku-m-user-manual-ver14
    loc: tbl=19.r5
    h: '128343534467'
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h76
    h: 2db32337047e
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:short-circuit-current
  note: The Isc coefficient is small and positive for crystalline silicon.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h18
    h: 88505e777c47
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h73
    h: 0b03943db93d
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1.2
    h: 54888f628680
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:maximum-power-point
  note: Separate coefficients exist for Vmp, Imp and Pmax; Voc and Isc coefficients should not be assumed
    to apply to Vmp and Imp.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h18
    h: 88505e777c47
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h73
    h: 0b03943db93d
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: tbl=20.r11
    h: 32b75a1276e8
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:crystalline-silicon
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h73
    h: 0b03943db93d
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1.2
    h: 54888f628680
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:thin-film-pv
  note: Thin-film modules have different coefficients than crystalline silicon; manufacturer instructions
    govern voltage calculations.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h73
    h: 0b03943db93d
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:standard-test-conditions
  note: Coefficients translate datasheet values from the 25 °C rating reference to other temperatures.
  cite:
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h389
    h: c9e8498c8209
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h18
    h: 88505e777c47
  review: drafted
  review_note: 'support check: partial - The 25 °C rating reference and datasheet STC data are stated,
    but explicit translation of STC values to other temperatures via coefficients is only implied through
    the Voc low-temperature equation.'
- claim_id: c8
  rel: related_to
  target: concept:single-diode-model
  note: Performance models such as the Sandia array model use four separate temperature coefficients (Isc,
    Imp, Voc, Vmp).
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h18
    h: 88505e777c47
  review: drafted
  review_note: 'support check: partial - The four coefficients (Isc, Imp, Voc, Vmp) are described for
    a performance model, but the passages do not name it the Sandia model or link it to the single-diode
    model.'
---
A temperature coefficient describes how much a PV cell's voltage, current or power changes for each degree of change in cell temperature. For crystalline silicon, a hotter cell gives noticeably lower voltage and power and a slightly higher current, so the voltage and power coefficients are negative. Typical crystalline silicon values are about -0.4 %/°C for voltage, +0.04 %/°C for short-circuit current and -0.45 %/°C for maximum power, and thin-film modules have different values. Datasheets list these coefficients next to the STC ratings, for example -0.32 %/°C for open-circuit voltage or -0.41 %/°C for Pmpp on some products. Modules reach their highest voltage at the lowest temperature, so the Voc coefficient is used to find the cold-weather string voltage and to check it stays below the maximum system voltage when sizing strings. Detailed models such as the Sandia array model use separate coefficients for Isc, Imp, Voc and Vmp, because the Voc and Isc values do not correctly describe Vmp and Imp.

<!-- review notes
- sentence 4: support check: partial - The -0.32 %/°C Voc and -0.41 %/°C Pmpp values appear, and the datasheet lists STC data and coefficients, but 'next to STC ratings' for those specific values is only loosely supported.
-->
