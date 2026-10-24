---
id: concept:om-contract
type: Concept
name: O&M contract
aliases:
- operations and maintenance contract
- performance-based O&M
- fixed-price O&M
- O&M agreement
- O&M services agreement
category: Market
concept_kind: finance
claims:
- claim_id: c1
  rel: related_to
  target: metric:availability
  note: Contractual availability is technical availability with agreed exclusion factors applied. It is
    calculated at inverter level on an annual basis, and it is the KPI that best reflects the provider's
    service.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=10.5.1
    h: 6b3fb1a2164f
  - src: src:solarpower-europe-om-guidelines
    loc: sec=11.5
    h: 10f2d9c59257
  - src: src:solarpower-europe-om-guidelines
    loc: sec=h141
    h: 421583b73b24
  review: drafted
- claim_id: c2
  rel: related_to
  target: metric:energy-based-availability
  note: Energy-based availability is generally used in the availability guarantee chapter of the O&M contract.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=10.5.3
    h: 84ef0f2bedff
  review: drafted
- claim_id: c3
  rel: related_to
  target: metric:performance-ratio
  note: PR guarantees are no longer standard in third-party O&M contracts. A PR target can still trigger
    a joint analysis of causes.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=h141
    h: 421583b73b24
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=10.1
    h: 02c123deaa1d
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:power-purchase-agreement
  note: When operations fail, the asset owner can face liabilities under third-party agreements, including
    any PPA.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=11.1
    h: f9d7ab6b793b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
An O&M contract is an agreement between the asset owner and an O&M service provider to manage, operate and maintain a solar PV power plant. Together with the EPC contract it is a key project finance document, and it should limit financial risk by allocating operational risk appropriately. The scope usually covers the whole plant, including modules, mounting or trackers, inverters, cabling, combiner boxes, monitoring and SCADA, the substation, security and vegetation control. Most contracts set a fixed fee for operations, preventive maintenance and an agreed response time. Corrective maintenance and services outside the scope are charged separately, for example per service action, at hourly rates or as time and materials. Best practice is a fixed fee plus escalation, and the basic fee is often priced per kWp installed. Performance-based contracts are tied to KPIs such as availability, energy yield or performance ratio. Each KPI must be defined in enough detail that all parties calculate the same value. Current guidance prefers availability guarantees and response time price adjustments over PR guarantees. The fee is reduced when the provider misses its agreed response times to plant alarms. The contract should state its effective date, term, renewal options and termination rights. It should also make sure the maintenance it requires keeps the component warranties valid.
