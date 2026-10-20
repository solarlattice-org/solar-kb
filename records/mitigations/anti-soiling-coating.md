---
id: mit:anti-soiling-coating
type: Mitigation
name: Anti-soiling coating
aliases:
- ASC
- AS Coatings
- easy-to-clean
- self-cleaning
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 20
    unit: unit:PERCENT
  conditions: Performance loss from soiling summarized by Mondal et al., varying with test site and boundary
    conditions
  note: Context for ASC benefit; the source also reports cleaning cost reductions of 20-50% from ASC alone
    depending on local weather, and a 3.2% gain in annual economic yield in a simulated typical Riyadh
    year with ASC and optimized cleaning.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h70
    h: d27e8de83a79
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - The passage says Mondal et al. summarize performance loss ''up
    to 20%'' depending on test sites and boundary conditions, and gives the 20-50% cleaning cost and 3.2%
    yield figures. But it frames the 20% loss in the context of soiling, not as a typical value, and the
    statement lists it as a ''typical'' loss for ASC.'
---
An anti-soiling coating is a surface layer on the module glass that makes it harder for particles to stick, and it is used as a preventive measure against soiling losses. It is chosen at the design and procurement stage, as part of the EPC's work, while cleaning is the corrective measure handled by O&M. Coatings can be hydrophobic, which makes water bead up and roll off carrying dust, or hydrophilic, which spreads water across the surface. Some titanium dioxide types also break down organic dirt under UV light. The main benefit is that rain and other natural cleaning can do more of the work, so cleaning can be done less often and cleaning costs go down. Sources do not agree on how well these coatings work. A coating only helps if it suits the local soiling type, and in some conditions a coated module can get dirtier than uncoated glass. Some coatings reduce light transmission on their own, and their service life is not guaranteed in every climate. Use cleaning methods that do not wear the coating away. Dry brushing has caused serious damage in some cases, and sandstorms also shorten coating life. Judge whether a coating is worth it site by site, weighing climate, cleaning cycles and cost. Standard tests such as IEC 62788-7-3 can check durability in advance.

<!-- review notes
- sentence 1: support check: partial - Passages say ASCs hinder particle deposition and are a preventive measure. They don't explicitly describe the coating as a surface layer on the module glass that makes it harder for particles to stick.
-->
