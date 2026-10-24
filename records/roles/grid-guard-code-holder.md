---
id: role:grid-guard-code-holder
type: Role
name: Grid Guard code holder
aliases:
- SMA Grid Guard code
- Grid Guard Code
- GGC
category: Access levels
role_kind: access-level
---
The SMA Grid Guard code is a personal access code. It unlocks grid-sensitive parameters, called SMA Grid Guard parameters, on SMA devices. Only electrically qualified persons can request it. The installer must be registered and logged in to the SMA Online Service Center, and the code is issued there free of charge under Self Help. System owners who need a parameter changed should ask their installer. To enter the code, first log in with the Installer user group. Then type the code in the Individual access code field, for example in Sunny Explorer, the Cluster Controller or the LCS-Tool. Older tools such as Sunny WebBox and Sunny Data Control use the Inst.-Code parameter instead. On the Cluster Controller, the Grid Guard symbol can take up to two minutes to appear after you enter the code. Entering the blocking code 54321 turns Grid Guard mode off again. The code is needed to set communication-loss fallback, to set feed-in management for active and reactive power setpoints, and to change the active power gradient on the Cluster Controller. With the Inverter Manager, all inverter parameters and the system fallback are protected by Grid Guard. The code may also be needed to set the country standard to Island Mode 60 or Offgrid, which is the setting used for frequency-shift power control with a battery inverter. A wrong code triggers event 9002 and the parameters stay locked. A valid code is logged as event 29001. The Sunny Tripower X does not need a Grid Guard code for configuration changes.

<!-- review notes
- sentence 3: support check: partial - Installer login, the Individual access code field, the Cluster Controller and LCS-Tool, and the Inst.-Code parameter in Sunny Data Control and Webbox are supported. Sunny Explorer entry is not described in the passages, and the Sunny Data Control and Webbox procedures log in as installer but do not mention a field named Individual access code.
- sentence 4: support check: partial - The two-minute symbol update and the blocking code 54321 are stated. The passage says the symbols take up to two minutes to update, not specifically that the symbol appears.
- sentence 5: support check: partial - The Cluster Controller steps for feed-in management and the active power gradient, and the Inverter Manager protection, are supported. The fallback on the Cluster Controller is also supported, but the passages do not clearly state that the system fallback is Grid Guard protected beyond the LCS-Tool code use. The Cluster Controller steps only show the code being entered first, not that it is strictly required.
- sentence 6: support check: partial - The passage says to set Island Mode 60 or Offgrid with the Grid Guard Code if needed, and describes P(f) for battery integration. It does not explicitly say that setting is 'the setting used' with a battery inverter, though this is implied.
-->
