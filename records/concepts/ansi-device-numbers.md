---
id: concept:ansi-device-numbers
type: Concept
name: ANSI device numbers
aliases:
- ANSI device codes
- device 27
- device 59
- device 81
- ANSI/IEEE Standard Device Numbers
- standard device numbers
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: part_of
  target: std:ieee-c37-2-2008
  note: The short reference cites IEEE Standard C37.2-2008 as the source of the device numbers and the
    application letter suffixes.
  cite:
  - src: src:ref-standards-ansi-device-numbers-short
    loc: sec=h1
    h: a440001bf934
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:single-line-diagram
  note: National Grid requires industry standard device numbers on functional single-line diagram submittals.
  cite:
  - src: src:std-utilities-nat-grid-ma-ny-shared-constr-esb756
    loc: sec=h259
    h: 0d5b4a12b19e
  - src: src:std-utilities-nat-grid-ma-ny-shared-constr-esb756
    loc: sec=h348
    h: 0d5b4a12b19e
  - src: src:std-utilities-nat-grid-ma-ny-shared-constr-esb756
    loc: sec=h173
    h: 4e46f59fc651
  review: drafted
- claim_id: c3
  rel: related_to
  target: comp:grid-protection-device
  note: In North America, protective relays are usually identified by standard device numbers.
  cite:
  - src: src:ref-standards-ansi-device-numbers-short
    loc: sec=h1
    h: a440001bf934
  review: drafted
---
ANSI device numbers are standard numeric codes. In North America they are the usual way to name protective relays and other switchgear devices. The full list and definitions are in IEEE C37.2. Letters are sometimes added to a number to show the application. For grid protection of PV and storage systems, the common codes are 27 for an undervoltage relay, 59 for an overvoltage relay and 81 for a frequency relay. Utilities such as National Grid require these standard device numbers on functional single-line diagrams submitted for interconnection. The National Grid reference list of device numbers points to ANSI C37.2-1987.

<!-- review notes
- sentence 1: support check: partial - Protective relays are generally named by device numbers in North America, but 'other switchgear devices' and 'numeric codes' are not explicitly stated.
- sentence 3: support check: partial - Codes 27, 59, 81 map to undervoltage, overvoltage, frequency relays, but the passages don't say they are the common codes for PV and storage grid protection.
- sentence 4: support check: partial - National Grid requires standard device numbers on functional single-line diagrams, but 'for interconnection' and 'these' specific numbers are not stated; also 'utilities such as' generalizes.
-->
