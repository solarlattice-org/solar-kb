---
id: prod:chint-sca-23-28ktl
type: Product
name: CPS SCA23-28KTL-DO/US-480
aliases:
- SCA 23 28 KTL
- CPS 23 28 KTL
- Chint/23 28 kW
- SCA23/28KTL
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  note: The SCA23/28KTL appears in an inverter installation manual, in a figure on derating against PV
    input voltage.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: fig=168
    h: 7e8e0c618fe3
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: fig=169
    h: e1bbb0ecff95
  review: drafted
  review_note: 'support check: partial - The passages show SCA23/28KTL in a derating figure caption, but
    not the specific model CPS SCA23-28KTL-DO/US-480 or that it is an inverter instance.'
---
The SCA23/28KTL is a PV inverter family. It appears in the CSI 23-28KTL-CT inverter installation manual. That manual has a curve showing how the SCA23/28KTL derates its output depending on PV input voltage.

<!-- review notes
- sentence 1: support check: partial - The caption shows the SCA23/28KTL name with derating, implying an inverter, but nothing names the CSI 23-28KTL-CT manual or calls it a family.
- sentence 2: support check: partial - The caption states a derating curve of PV input voltage for SCA23/28KTL, but 'that manual' is not identified and the output derating is only implied.
- sentence 1: review: partial - The derating-curve caption implies the SCA23/28KTL is a PV inverter, but no passage calls it a family or names the CSI 23-28KTL-CT installation manual (that name appears only in the source id).
-->
