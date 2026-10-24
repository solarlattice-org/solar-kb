---
id: proto:igmp
type: Protocol
name: IGMP multicast
aliases:
- IGMP
- IGMPv3
- IGMP snooping
- Internet Group Management Protocol
- IGMP version 3
category: Communication
protocol_kind: transport
---
IGMP, the Internet Group Management Protocol, lets IP network devices sign hosts up to multicast groups. It works on LANs and VLANs that have a multicast-capable IP router, and on network devices that support multicast filtering. A querier, which is a router or a switch, sends periodic query packets. Hosts answer with report packets that name the group they want to join, and a switch with IGMP Snooping on then forwards that group's traffic only to the ports that sent reports. Version 1 is defined in RFC-1112. Version 2 (RFC-2236) adds group-specific queries, leave messages and querier election. Version 3 (RFC-3376) adds source filtering, which accepts or excludes traffic from listed sources. Without IGMP Snooping, IP multicast traffic is always forwarded and floods the network. With it, traffic reaches only the hosts that need it. You can turn snooping and querying on or off from the USB console or the web interface. On the CLI the command is ip igmp-snooping, and the no form turns it off. Snooping is globally disabled by default and only works in 802.1Q VLAN mode. Use ip igmp static-group to add a static multicast MAC address and its member ports. The IGMP Table page lists the active groups, router and querier ports, and the snooping version for each VLAN.
