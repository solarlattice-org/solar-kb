---
id: concept:interconnection-process
type: Concept
name: Interconnection process
aliases:
- interconnection application
- interconnection study
- interconnection agreement
- Interconnection Request
- Interconnection Studies
category: Grid
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: std:ieee-1547
  note: IEEE 1547 sets the technical interconnection requirements but does not cover procedural or contractual
    issues.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=4.5
    h: 26637afb4e4e
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:ul-1741
  note: UL 1741 certifies interconnection equipment such as inverters against IEEE 1547.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=4.5
    h: 26637afb4e4e
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:permission-to-operate
  note: The process ends with a written Authorization to Interconnect once the inspection, documentation
    and Witness Test are satisfactory.
  cite:
  - src: src:std-utilities-nat-grid-ma-ny-interconnect-stds-ma
    loc: sec=h21
    h: 89c9e91ca783
  review: drafted
- claim_id: c4
  rel: related_to
  target: org:caiso
  note: The distribution provider coordinates with the CAISO when Reliability or Network Upgrades are
    expected.
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: sec=h456
    h: 5817cf6f5528
  - src: src:std-manuals-sce-rule-21
    loc: sec=h283
    h: f1c2d5d7e12d
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:listed-equipment
  note: The Simplified Process for networks applies to Listed inverter-based facilities.
  cite:
  - src: src:std-utilities-nat-grid-ma-ny-interconnect-stds-ma
    loc: sec=h21
    h: 89c9e91ca783
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:area-eps
  cite:
  - src: src:std-utilities-nat-grid-ma-ny-interconnect-stds-ma
    loc: sec=1.2
    h: c3fa7c056011
  review: drafted
  review_note: 'support check: partial - Passage defines Area EPS as the Company EPS and mentions the
    interconnection process, but doesn''t explicitly relate the process to Area EPS beyond the definition.'
---
Interconnection covers the technical and procedural steps needed before a PV system or other distributed generator can run in parallel with the utility grid. Every grid-connected PV system needs an interconnection agreement. This agreement sets the terms, conditions and equipment requirements, and it is usually handled by the local distribution utility. The procedures come from state and utility policy rather than from IEEE 1547. They include the application and schedule, customer agreements, fees, metering, billing and permitting and inspection. A small net-metered system may only need a one-page contract. A larger exporting system usually pays for an initial screening and then a more detailed power flow study, which can show that grid upgrades are needed at the applicant's cost. The detailed studies look at short circuit, stability and power flow. They identify the interconnection facilities and upgrades needed to fix overloads and voltage problems. The full review and approval can take 6 to 12 months, so contact the utility early to learn the application requirements, costs and schedule. Once the inspection, documentation and any witness test are satisfactory, the utility issues a written Authorization to Interconnect. This is similar to permission to operate.

<!-- review notes
- sentence 3: support check: partial - Procedures based on state/utility policy, with application, schedule, agreements, permitting and inspection, and IEEE 1547 not covering procedures, are stated; fees, metering and billing are called contractual aspects, not procedures.
- sentence 7: support check: partial - The written Authorization to Interconnect after satisfactory inspection, documentation and witness test is stated, but the passage doesn't equate it to permission to operate.
-->
