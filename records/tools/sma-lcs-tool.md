---
id: tool:sma-lcs-tool
type: Tool
name: SMA LCS-Tool
aliases:
- LCS Tool
- LCS-Tool
category: Software
tool_kind: software
---
The LCS-Tool is SMA's local commissioning and service software. You use it to commission the SMA Inverter Manager and the inverters connected to it, and this must be done before the inverters connect to the grid and start feeding in. The tool lets you pick a predefined country data set for the grid. SMA can also supply customer-specific country data sets, which you load through the tool. The system-level fallback, used when communication between the Inverter Manager and a higher-level controller such as a SCADA system or power plant controller fails, can only be set in the LCS-Tool. Setting it needs your SMA Grid Guard code under the Installer user group. You can also use the tool, or a customer-specific grid code file, to set the operating state an inverter falls back to when it loses communication with the Inverter Manager. The tool is used to set Peak Load Shaving with increased self-consumption (Multi-Use) for the Sunny Tripower Storage 60 with a Janitza UMG 604-PRO power analyzer. This function works only in battery storage systems. The tool can list all inverters connected to the Inverter Manager. The computer needs Windows 7 or later, 1 GB of hard disk space and 2 GB of RAM, and the tool must be installed on a local drive. Connect the computer to LAN port 1 of the Inverter Manager through a router; DHCP is recommended.
