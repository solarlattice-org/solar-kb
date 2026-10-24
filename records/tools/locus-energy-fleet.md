---
id: tool:locus-energy-fleet
type: Tool
name: Locus Energy LOCUS Fleet
aliases:
- LOCUS Fleet
- LOCUS_Fleet
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:locus-energy
  note: The terms of use describe the Locus Platform as the websites and API that Locus Energy, Inc offers
    for energy monitoring and asset management.
  cite:
  - src: src:alsoenergy-kb-locus-energy-terms-of-use-agreement
    loc: sec=h5
    h: e43b75cbdfa3
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:https-rest-api
  note: The Locus Energy v3 API is reached through an HTTPS endpoint prefix and returns JSON. The license
    terms allow at most two data calls per second.
  cite:
  - src: src:alsoenergy-kb-locus-energy-v3-api
    loc: sec=front
    h: 20fbaf5e601a
  - src: src:alsoenergy-kb-locus-energy-terms-of-use-agreement
    loc: sec=h5
    h: e43b75cbdfa3
  review: drafted
---
The Locus platform is a web and API service from Locus Energy for monitoring PV energy production and managing assets. It is made up of the LocusNOC and SolarNOC website, a client site, the Locus API, and extra features such as Virtual Irradiance. End-users have more limited access, for example through the Client Portal. Fleet reports are covered in the Locus knowledge base. Virtual Irradiance data can be used to evaluate system and fleet performance, either through Locus reports or through the API. The v3 API gives programmatic access to much of the LocusNOC data and returns JSON. The license allows no more than two data calls per second. For incentive reporting, the LGate production meter records generation every 5 minutes. The platform then aggregates this data and submits it each month to programs such as Mass CEC PTS and PJM GATS. Set component-level alerts so you know when a site goes offline. The LGate can only hold about two months of production data in its internal memory. Locus does not warrant the accuracy of platform or Virtual Irradiance data. Check any action based on Virtual Irradiance data independently, and expect gaps in the data when source data is missing.

<!-- review notes
- sentence 1: support check: partial - The platform is defined as web sites and API for energy monitoring and asset management, but the passages don't say it monitors PV energy production specifically (the license does mention photovoltaic systems for API use).
- sentence 3: support check: partial - The license supports using VI Data for system and fleet performance evaluations through Locus reports or the API, but the Fleet Reports passage has only a title and no content, so it doesn't show that fleet reports are covered.
- sentence 7: support check: partial - The passages disclaim warranty on platform info and VI Data, require independent verification of actions based on VI Data, and say source data gaps may cause VI Data gaps, but the first sentence goes beyond them, since the platform information disclaimer says Locus makes best efforts to ensure accuracy.
-->
