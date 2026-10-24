---
id: concept:string-sizing
type: Concept
name: String sizing
aliases:
- string configuration
- string length
- modules per string
- PV string sizing
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:mppt-voltage-range
  note: A wide MPP DC voltage range allows many string combinations to perform optimally.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=4.7
    h: 7a6ffbedb2af
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:temperature-coefficient
  note: Manual sizing uses NEC 690.7 temperature multiplication factors or the module maker's temperature
    coefficient so string voltage stays under the limit at minimum design temperature.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=4.7
    h: 7a6ffbedb2af
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:system-voltage-class
  note: String length is capped by the system maximum voltage, given as 600 V in the US.
  cite:
  - src: src:trn-training-industry-reports-and-guides-nrel-one-axis-trackers-improved-reliability-durability-perf
    loc: sec=h52
    h: d668bc6dd55d
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:voltage-drop
  note: The same manual advises keeping DC and AC wiring voltage losses to no more than 2 percent.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=4.7
    h: 7a6ffbedb2af
  review: drafted
- claim_id: c5
  rel: related_to
  target: tool:solectria-string-sizing-tool
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h81
    h: 12b5f946e0c6
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h109
    h: 12b5f946e0c6
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=4.7
    h: 7a6ffbedb2af
  review: drafted
- claim_id: c6
  rel: related_to
  target: comp:single-axis-tracker
  note: Fitting a whole number of strings on each tracker unit makes field wiring much simpler.
  cite:
  - src: src:trn-training-industry-reports-and-guides-nrel-one-axis-trackers-improved-reliability-durability-perf
    loc: sec=h52
    h: d668bc6dd55d
  review: drafted
---
String sizing means choosing how many PV modules to wire in series in each string, so the string voltage suits the inverter and the system voltage limit. String length is the most modules you can put in series without going over the system maximum voltage. In the US that limit is 600 V, and strings usually run from 8 to 20 modules. If you size strings by hand, apply the NEC 690.7 temperature multiplication factors or the module maker's temperature coefficient, so the string stays below 600 V dc at the minimum design temperature. The string should also operate inside the inverter's MPP voltage range. An inverter with a wide range, such as 200 V to 500 V, accepts many string combinations. Manufacturers tell installers to check the inverter specifications and use industry-standard sizing methods required by local code. Some vendors, such as Yaskawa Solectria, offer an online string sizing tool. Inputs on the same inverter may have different numbers of modules per string on purpose, so mismatched I-V curves between MPPT inputs are not always a fault. On trackers, fitting a whole number of strings on each tracker unit makes field wiring simpler. A half string needs a jumper to the next unit.

<!-- review notes
- sentence 1: support check: partial - Passages define string length as modules in series limited by the max system voltage, but don't mention suiting the inverter (the MPPT range appears in other passages, not these) or define string sizing as stated; the u22 field only says number of modules.
- sentence 4: support check: partial - The wide 200-500 V range allowing many string combinations is stated, but the passage does not explicitly say the string should operate within the MPP range.
- sentence 5: support check: partial - Passages say to refer to specifications and use industry-standard techniques per local code, and that Yaskawa Solectria offers a tool; 'some vendors' generalization and 'check the inverter specifications' are close but acceptable, with the manufacturers-in-general claim slightly stronger.
- sentence 6: support check: partial - Passage says differing module counts per string may be intended by design, but it doesn't say explicitly that mismatched curves are not a fault, though this is implied.
- sentence 1: review: partial - The passages support modules in series limited by the system maximum voltage and a modules-per-string field, but nothing in them says the string voltage must suit the inverter.
- sentence 4: review: partial - The wide 200-500 V MPP range allowing many string combinations is stated, but the passage never says the string should operate inside the MPP voltage range.
-->
