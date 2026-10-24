---
id: tool:sungrow-isolarcloud
type: Tool
name: iSolarCloud
aliases:
- Sungrow iSolarCloud
- iSolarCloud App
- iSolarCloud Web
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sungrow
  note: Sungrow installer FAQ articles list the make as SunGrow.
  cite:
  - src: src:kb-sungrow-how-to-set-inverter-parameters-with-isolarcloud-app
    loc: sec=front
    h: 2f2123c09c2e
  - src: src:kb-sungrow-how-to-create-a-plant-with-isolarcloud-web
    loc: sec=front
    h: a6890bff7b28
  review: drafted
  review_note: 'support check: partial - Passages show make SunGrow on iSolarCloud FAQ articles, but don''t
    explicitly state iSolarCloud is made by Sungrow (org id not shown); implied only.; review: partial
    - The note holds, since both iSolarCloud FAQ articles carry make: SunGrow and come from sungrowpower.com,
    but neither passage says that Sungrow makes iSolarCloud; that is only implied by the metadata.'
---
iSolarCloud is Sungrow's monitoring and configuration platform. You can use it as a mobile app or through a web portal. To change inverter parameters in the app, log in, open the plant, go to Device, select the inverter and open Setting. The Setting area is split into Initial Grid, System Parameters, Protection Parameters and Power Control. To create a plant on the web portal, log in with an iSolarCloud account or register a new one, select Create Plant, fill in the plant information and add the communication device. After you create the plant, wait for the device data to upload before you check it. The web portal has separate European, International and Australian servers, so log in to the one that matches the site's region.

<!-- review notes
- sentence 5: support check: partial - Passage says to wait for device data to be uploaded after creating the plant, but doesn't say to wait before checking it.
- sentence 6: support check: partial - Three servers are listed, but the passage doesn't say to choose by site region.
- sentence 1: review: partial - The titles show that an iSolarCloud App sets inverter parameters and an iSolarCloud Web creates plants, which supports app plus web portal and configuration, but no passage calls it a monitoring platform.
-->
