---
id: concept:short-circuit-current
type: Concept
name: Short-circuit current
aliases:
- Isc
category: Modules
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:iv-curve
  note: Isc is one of the key values read from a string I-V curve measurement, alongside Voc, Vmpp, Impp,
    Pmpp and fill factor.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4
    h: dbeab86d1089
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4.r5
    h: 8404bef4b055
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:fill-factor
  note: Fill factor is maximum power divided by the product of open-circuit voltage and short-circuit
    current.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h24
    h: 69690a32e377
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:open-circuit-voltage
  note: Voc and Isc together form the denominator of the fill factor.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=4
    h: dbeab86d1089
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h24
    h: 69690a32e377
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:standard-test-conditions
  note: The module Isc rating is stated at STC.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=8.r2
    h: c41b4ab035d5
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h97
    h: e749cb64574d
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:ampacity
  note: Required source circuit conductor ampacity depends on the rated module short-circuit current;
    maximum PV source circuit current is 125% of the sum of parallel module Isc ratings per NEC 690.8(A).
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h97
    h: e749cb64574d
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:plane-of-array-irradiance
  note: Array short-circuit current is proportional to the solar irradiance on the system.
  cite:
  - src: src:test-ground-fault-groundtestingpvanen20221693321214407
    loc: sec=h17
    h: aa38e0df17e3
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:air-mass
  note: For amorphous silicon modules, the short-circuit response Isc/G varies with air mass because of
    spectral response.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=3.2.2
    h: cc128f301ebe
  review: drafted
- claim_id: c8
  rel: related_to
  target: method:string-short-circuit-test
  note: Field test that temporarily shorts an isolated PV string and measures Isc to confirm correct operation.
  cite:
  - src: src:iec-62446-1
    loc: sec=6.5.2
    h: c32ca77081a9
  - src: src:test-ground-fault-groundtestingpvanen20221693321214407
    loc: sec=h17
    h: aa38e0df17e3
  - src: src:iec-62446-1
    loc: sec=6.5.2.2
    h: e78cd394ec93
  review: drafted
- claim_id: c9
  rel: related_to
  target: tool:clamp-meter
  note: A suitably rated clip-on ammeter can measure string short-circuit current during the test.
  cite:
  - src: src:iec-62446-1
    loc: sec=6.5.2.2
    h: e78cd394ec93
  review: drafted
---
Short-circuit current, written Isc, is the current a PV module or string delivers when its output terminals are shorted together. It is one of the main values on the I-V curve, along with open-circuit voltage, maximum power voltage, maximum power current and maximum power. Module datasheets state Isc at standard test conditions, and conductor ampacity for PV source circuits is sized from this rated value, using 125% of the summed parallel Isc ratings. Isc is proportional to the irradiance on the array, so field measurements should be taken in clear sky on clean, unshaded modules, and strings compared with each other should agree within 5%. To test, the string is isolated and briefly shorted with a rated PV tester, shorting cable or switch box. The current is read with a rated clip-on or in-line ammeter, and the short is interrupted with a load break device before anything else is changed. Isc is also used to work out the fill factor, which is maximum power divided by the product of Voc and Isc. A low fill factor can point to faults that cost energy yield. For amorphous silicon modules, the ratio of Isc to irradiance changes with air mass and with the direct and diffuse light components because of spectral response.

<!-- review notes
- sentence 3: support check: partial - STC Isc and 125% of summed parallel ratings are stated, but 'module datasheets' stating it is not explicit.
-->
