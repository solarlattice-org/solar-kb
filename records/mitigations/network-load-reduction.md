---
id: mit:network-load-reduction
type: Mitigation
name: Network load reduction
---
Network load reduction is a corrective action for SMA inverters that report a busy or overloaded communication network. You either lower the number of devices on the network or make the devices query data less often. It applies to event 10248, where the network is busy and data exchange between devices is poor and heavily delayed. It also applies to event 10249, where the network is overloaded and devices exchange no data at all. For a busy network, the manuals say to increase the query intervals first and to remove devices only if needed. For an overloaded network, they say to remove devices first and to increase the data query intervals if needed. For event 10250, a high package error rate can mean the network is overloaded or the link to the switch or DHCP router is disrupted. Before reducing load, check that Ethernet cables and connectors are undamaged and plugged in correctly. The query interval settings are described in the matching installation manual. System owners should ask their installer to investigate. Once the load is back in the normal range, the inverter logs event 10255, and no further action is needed.

<!-- review notes
- sentence 5: support check: partial - Causes and cable/connector check are stated, but the passage doesn't say to check cables 'before reducing load' (it lists it first, with load reduction 'if necessary'); also the check applies to Ethernet connections only, a minor qualifier, and the switch/DHCP router wording matches.
-->
