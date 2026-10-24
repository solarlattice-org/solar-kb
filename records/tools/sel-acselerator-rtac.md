---
id: tool:sel-acselerator-rtac
type: Tool
name: SEL-5033 ACSELERATOR RTAC software
aliases:
- SEL-5033
- AcSELerator RTAC
category: Software
tool_kind: software
---
ACSELERATOR RTAC is the SEL program that opens the project for a Real-Time Automation Controller (RTAC) so you can view or change it. You can add it as an application in QuickSet Device Manager. Open the SEL-3530 device node, go to the Applications tab and point the application file path to the RTAC executable. By default the executable is installed at C:\Program Files\SEL\AcSELerator\RTAC\RTAC.exe. Keep the option to run from the Connection Explorer context menu turned on. You can then right-click the SEL-3530 and launch the program from the Applications menu. Device Manager 6.4.1.0 dropped the SEL-3533 as an RTAC device type. Existing SEL-3533 entries are converted to SEL-3555 during the upgrade.
