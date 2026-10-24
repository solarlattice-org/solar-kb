---
id: tool:alsoenergy-locusnoc
type: Tool
name: LocusNOC
aliases:
- Locus NOC
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:https-rest-api
  note: The Locus Energy v3 API gives programmatic access to much of the LocusNOC data over an HTTPS endpoint
    and returns it as JSON.
  cite:
  - src: src:alsoenergy-kb-locus-energy-v3-api
    loc: sec=front
    h: 20fbaf5e601a
  review: drafted
---
LocusNOC is a monitoring platform. Users move between its pages and functions through a Search-Browse Pane, so they do not have to search for the same site or component again. Advanced searches and groups let users view sites and components that match criteria they define. Alerts can be acknowledged throughout the platform, and data extracts are available. Users can upload a company logo to show in the LocusNOC header or to attach to Graphical Reports. The Locus Energy v3 API gives programmatic access to much of the LocusNOC data and returns it in JSON. The Power LCS 400 works with a listed set of inverters through LocusNOC, including ABB Trio, Chint CPS, Solectria PVI/XGI, Fronius Symo, Huawei Sun2000, SMA STP/Core 1, SolarEdge and Sungrow string inverters. If an inverter is not on that list, ask your sales representative about the PowerTrack Platform instead. Display in mobile browsers was improved for phones and tablets in the 2018.07.05 release, and there is also a MyLocusEnergy mobile app. The old charting tool has been removed from the interface.

<!-- review notes
- sentence 3: support check: partial - Only the titles/keywords of the articles are given; the titles indicate acknowledged alerts throughout LocusNOC and data extracts, but there is no body text stating that data extracts are available.
- sentence 6: support check: partial - The list and the PowerTrack advice are present, but the statement's list is only a subset and the 'string inverters' label is applied to all, e.g., Chint CPS and Solectria; core content is supported.
- sentence 7: support check: partial - Mobile browser rendering improvement is stated for the 2018.07.05 release, and the MyLocusEnergy Mobile App article exists by title only, with no body text confirming details.
-->
