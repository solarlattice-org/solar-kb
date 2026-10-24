---
id: tool:alsoenergy-powertrack
type: Tool
name: AlsoEnergy PowerTrack platform and API
aliases:
- PowerTrackUserGuide
- PowerTrack User Guide
- AlsoEnergy API
- PowerTrack Monitoring Platform
- PowerTrack software
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:alsoenergy
  note: PowerTrack is identified as a trademark of AlsoEnergy.
  cite:
  - src: src:alsoenergy-alsoenergy-operation-and-maintenance-manual-rev-2
    loc: sec=front
    h: fab2a9e449ad
  review: drafted
  review_note: 'support check: partial - The passage says PowerTrack is a trademark of AlsoEnergy and
    the document is AlsoEnergy''s, but it doesn''t explicitly say AlsoEnergy makes the platform and API.'
- claim_id: c2
  rel: manufactured_by
  target: org:stem
  note: The current user guide states the PowerTrack software is provided by Stem US Operations, Inc.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: sec=h2
    h: 70cefddcf832
  review: drafted
---
PowerTrack is a web-based monitoring platform for logging in and managing a portfolio of solar sites, with separate login addresses for the Americas and for international users. Its Chart Builder lets users plot built-in charts or create custom charts, and charts can also be used as dashboard widgets. For sites with both PV and Stem Athena storage, an API link can show high-level BESS metrics in PowerTrack, with 5-minute granularity and a 5-minute delay. More detailed skid or block level BESS data requires a direct edge link between the Athena datalogger and the PowerManager datalogger through an SEL RTAC. User roles include API Readonly, a basic user with API access, and API Administrator, an administrator with API access. AcquiSuite data loggers are set up with a PowerTrack upload URL so they can send data to the platform. After Stem or AlsoEnergy approves a new site, the customer must also approve it under Config > Site Config > Basic > Site Status. Training videos are in the PowerTrack Help menu, and the same PowerTrack login also works for the AlsoEnergy knowledge base.

<!-- review notes
- sentence 4: support check: partial - The passage says the SEL RTAC link between the Athena APC and PowerManager gives skid/block-level data and that much more data is available via a direct onsite connection, but it doesn't say this is the only way to get detailed data.
- sentence 6: support check: partial - The passages give a PowerTrack upload URL, but they don't mention AcquiSuite data loggers or say that it's used to send data to the platform.
-->
