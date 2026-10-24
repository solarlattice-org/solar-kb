---
id: tool:ignition-scada
type: Tool
name: Ignition SCADA
aliases:
- Ignition
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:ftp-push
  note: An AlsoEnergy commissioning article covers setting up and updating the FTP script on an Ignition
    site. FTP, PowerTrack and the Ignition Library are listed as keywords.
  cite:
  - src: src:alsoenergy-kb-updating-ftp-script-for-and-ignition-site
    loc: sec=front
    h: 4743b0e69574
  review: drafted
  review_note: 'support check: partial - The article on updating the FTP script for an Ignition site,
    with those keywords, is in the passage. The passage doesn''t say that Ignition SCADA uses FTP push
    as its protocol, though the FTP script article implies a link.'
---
Ignition is SCADA software. AlsoEnergy's site commissioning articles cover setting it up on monitored PV sites. To add the KPI Library script, first get credentials for the SourceGear Vault client, then download the latest KPI zip file from the Libraries repository. Open the project in Ignition Designer and use File, then Import, to load the KPI Library zip file. If the import fails, bring in the library by hand: import and copy the code from the JSON folders stored in SourceGear Vault. A separate article covers configuring and updating the FTP script on an Ignition site, including how to find the computer name, and uses the PowerTrack Ignition Library. The KPI article's keywords say the library involves Python and SQL.

<!-- review notes
- sentence 1: support check: partial - The Site Commissioning articles on Ignition are in the passages. Nothing in them says Ignition is SCADA software, and nothing says it is set up on monitored PV sites.
- sentence 5: support check: partial - The article title, table of contents (configuring FTP, obtaining the computer name) and keywords are in the passage. The passage doesn't state that the article uses the PowerTrack Ignition Library, though the keywords and attachment suggest it.
-->
