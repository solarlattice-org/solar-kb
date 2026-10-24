---
id: concept:net-metering
type: Concept
name: Net metering
aliases:
- NEM
- net energy metering
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: comp:energy-meter
  note: The utility net meter records energy drawn from the grid and energy fed into it. Billing is based
    on the net amount consumed.
  cite:
  - src: src:trn-training-industry-reports-and-guides-nysun-2023-solar-guidebook
    loc: sec=1.4
    h: 0bd6f27204a8
  - src: src:std-utilities-eversource-ct-ct-yellowbook
    loc: sec=h151
    h: 06db6143f794
  - src: src:std-standards-fm-global-standards-fmds07106-ground-mounted-pv-202004
    loc: sec=C.6.3.1
    h: 2a0fb71e2abb
  review: drafted
- claim_id: c2
  rel: related_to
  target: arch:behind-the-meter
  note: PV generation offsets the customer's consumption behind the meter, and only the excess is exported.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=4.4.4
    h: 00e709bc9be1
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:distributed-energy-resource
  scope:
    regions:
    - region:us-ny
  note: In New York State, solar PV qualifies for net metering as a distributed generation technology.
  cite:
  - src: src:trn-training-industry-reports-and-guides-nysun-2023-solar-guidebook
    loc: sec=1.4
    h: 0bd6f27204a8
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:virtual-net-metering
  note: Variant for multi-tenant, multi-meter and affordable housing properties under California Rule
    21 interconnection agreements.
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: tbl=21.r15
    h: 51c4b34c760d
  - src: src:std-manuals-sce-rule-21
    loc: tbl=21.r14
    h: 3443702b0676
  - src: src:std-manuals-sce-rule-21
    loc: tbl=21.r13
    h: 97bc6871f1ce
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: tbl=2.r23
    h: 0b2caa0ce27e
  review: drafted
  review_note: 'support check: partial - Forms show virtual net metering for multi-tenant, multi-meter
    and affordable housing under NEM and Rule 21, but the passages don''t define it as a net metering
    variant explicitly; mostly implied.'
---
Net metering is a utility policy incentive that lets a customer offset on-site electricity use with their own renewable generation, such as a PV system. Any solar energy the site does not use flows into the utility grid, and the owner gets a credit for it on the monthly bill. The utility meter records both the energy taken from the grid and the energy fed into it, and the customer pays only for the net energy consumed. On an Eversource net meter, register ID 04 shows the energy the utility delivered and ID 10 shows the excess generation the utility received. The generator must never be connected inside the meter socket or the instrument transformer compartment. The most common approach gives full one-to-one credit for each kilowatt-hour. Monthly surplus credits carry forward, and an annual true-up compares total consumption with total generation. At true-up, depending on the utility, leftover excess may be paid at the utility's avoided cost, lost, or carried into the next year. Policies vary widely, so get the local utility's net-metering policy before sizing a system. Net metering only covers offsetting on-site loads, so net-metered systems at sites with small loads tend to be moderate in size. Variants include remote, virtual, neighborhood and agricultural net metering. California Rule 21 separates NEM-1 and NEM-2 requests from the newer Net Billing Tariff.

<!-- review notes
- sentence 8: support check: partial - Remote, virtual, neighborhood and agricultural net metering and NEM-1/NEM-2 appear, and NBT is defined, but the passages do not say Rule 21 separates NEM requests from the Net Billing Tariff.
-->
