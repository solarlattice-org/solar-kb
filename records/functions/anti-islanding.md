---
id: func:anti-islanding
type: Function
name: Anti-islanding
aliases:
- unintentional islanding protection
- loss of mains protection
- islanding detection
- AI
- Anti-Islanding Detection
- island detection systems
category: Protection
function_kind: protection
claims:
- claim_id: c1
  attr: trip_time
  value:
    max: 2
    unit: unit:SEC
  conditions: Disconnection after an island forms, as the IEEE 1547 requirement is summarized in an overview
    of unintentional islanding test results
  cite:
  - src: src:ref-standards-ieee-ieee-1541-1-overview
    loc: sec=h50
    h: 77e3915831a7
  review: drafted
---
Anti-islanding automatically disconnects the inverter when the utility grid goes down or is switched off for maintenance, so that an unintentional island does not endanger people working on the lines. CPS SCH100/125KTL inverters keep perturbing the output frequency by injecting a small amount of reactive power. On a stable grid this has little effect, but in an island it pushes the frequency far enough to make the inverter stop and disconnect. IEEE 1547 and UL 1741 require islanding detection and test it, but they do not define the detection method, so vendor schemes differ and are often proprietary. Low-voltage ride-through can make islands more likely because low voltage can no longer be used to detect them. In SolisCloud, the CERT mode Anti-Islanding Setting can be set to the default method, ROCOF, both combined, or disabled. The Huawei SUN2000-45KTL-US-HV-D0 lists anti-islanding protection as supported. On the Fronius Primo, status code 456 means the anti-islanding function has stopped running properly.

<!-- review notes
- sentence 5: support check: partial - Huawei support is stated and code 456 description matches, but the passage does not tie code 456 to the Fronius Primo.
-->
