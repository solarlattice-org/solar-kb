---
id: tool:enphase-installer-platform
type: Tool
name: Enphase Installer Platform
aliases:
- Enlighten Manager
- Enphase Installer Portal
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:enphase
  note: Described as Enphase Enlighten web-based monitoring and management software; Enlighten Manager
    was renamed Enphase Installer Portal.
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: sec=h14
    h: 324833b90e75
  review: drafted
  review_note: 'support check: partial - Passage describes Enlighten as Enphase web-based monitoring software,
    but doesn''t mention the Installer Platform name/rename or explicitly state maker org (though Enphase-branded).'
---
The Enphase Installer Platform is Enphase's web-based monitoring and management platform for installers, formerly called Enlighten Manager and now also named the Enphase Installer Portal. Installers use it to view detailed performance data, manage several PV systems and remotely resolve issues that affect system performance. The gateway collects microinverter production and performance data over the AC power lines and sends it to Enlighten through an Internet or cellular connection. To check whether microinverter firmware has been updated, open the Systems tab, pick the system, open the Devices tab and read the firmware version in the Processor Load column. The platform also shows the site's grid profile and lets installers build the array layout for a system.

<!-- review notes
- sentence 4: support check: partial - Steps match, but the passage says the column shows the existing firmware version without specifying microinverter firmware.
- sentence 5: support check: partial - Evidence shows a grid profile figure and a video on building an array layout, but doesn't explicitly say the platform shows the site's grid profile; the layout building is supported by the video title.
-->
