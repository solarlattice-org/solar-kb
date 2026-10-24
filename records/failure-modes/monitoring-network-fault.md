---
id: fm:monitoring-network-fault
type: FailureMode
name: Monitoring network configuration fault
aliases:
- DNS server could not be resolved
- Webconnect error
- IP address conflict
- IGMP snooping
- DHCP address change
- router energy-saving LAN port
- datalogger offline
- blocked firewall ports
- datalogger network connection errors
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:igmp-snooping
  note: The switch treats the SMA device as inactive, cuts its connection, and the link does not come
    back.
  cite:
  - src: src:sma-doc-246498
    loc: sec=h451
    h: b5c8afa18dff
  - src: src:sma-doc-246498
    loc: sec=h452
    h: 64911a47d918
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:router-port-energy-saving
  note: The router or switch shuts down LAN ports to save energy.
  cite:
  - src: src:sma-doc-246498
    loc: sec=h451
    h: b5c8afa18dff
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=37.r2
    h: 7b62eb0fafb1
  - src: src:sma-doc-259761
    loc: tbl=74.r2
    h: aacc86440966
  review: drafted
  review_note: 'support check: partial - u8 and u21 mention energy saving mode on router ports and u2
    mentions LAN ports being deactivated, but none explicitly state the router/switch shuts down LAN ports
    to save energy as a cause (u8''s cause is garbled).'
- claim_id: c3
  rel: caused_by
  target: stressor:blocked-firewall-ports
  note: SMA lists ports 9523 and 3478 (registrar, proxy, STUN) as the ones that must stay open.
  cite:
  - src: src:sma-doc-246498
    loc: tbl=81.r1
    h: b9557e0ce5a3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h511
    h: c3abea00d0c7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h515
    h: c3abea00d0c7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h519
    h: c3abea00d0c7
  review: drafted
- claim_id: c4
  rel: caused_by
  target: fm:firmware-defect
  note: STP50-41 on firmware 3.12.17.R and 3.12.18.R cannot resolve DNS over a LAN connection.
  cite:
  - src: src:sma-kb-stp50-41-dns-problem-when-using-lan-ethernet
    loc: sec=h1
    h: ad1188949ab2
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-kb-dns-server-could-not-be-resolved
    loc: sec=h1
    h: d5f02e3ee0df
  - src: src:sma-kb-stp50-41-dns-problem-when-using-lan-ethernet
    loc: sec=h1
    h: ad1188949ab2
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:monitoring-gateway
  cite:
  - src: src:kb-solis-44002762194-troubleshooting-s1-w4g-st-datalogger-network-connection-errors
    loc: sec=h1
    h: 6540434b38b1
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=37.r2
    h: 7b62eb0fafb1
  - src: src:sma-doc-swebbox-ba-en-36
    loc: sec=6.6.2
    h: dcd17c991775
  review: drafted
  review_note: 'support check: partial - u4 and u8 show network connection problems for a datalogger/Sunny
    WebBox, but they don''t clearly attribute them to a network configuration fault; u37 only describes
    DHCP.'
- claim_id: c7
  rel: presents_as
  target: symptom:communication-loss
  note: The inverter cannot reach the monitoring portal.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h300
    h: 4985b8cec05a
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r68
    h: 13727c830dd3
  - src: src:sma-doc-246498
    loc: sec=h451
    h: b5c8afa18dff
  - src: src:sma-kb-dns-server-could-not-be-resolved
    loc: sec=h1
    h: d5f02e3ee0df
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:dns-resolution-error
  note: Webconnect status says the DNS server could not be resolved or is not configured. The inverter
    web interface still works.
  cite:
  - src: src:sma-kb-dns-server-could-not-be-resolved
    loc: sec=h1
    h: d5f02e3ee0df
  - src: src:sma-kb-stp50-41-dns-problem-when-using-lan-ethernet
    loc: sec=h1
    h: ad1188949ab2
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h304
    h: fe65cc3718d5
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r70
    h: e9a07e998a9d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h517
    h: 1a6d2981b2b4
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:devices-not-detected
  note: The energy manager finds none, or not all, of the devices connected over Speedwire.
  cite:
  - src: src:sma-doc-246498
    loc: tbl=81.r1
    h: b9557e0ce5a3
  review: drafted
- claim_id: c10
  rel: detected_by
  target: method:communication-status-check
  note: Read the Webconnect status, current IP address, gateway and DNS server in the inverter's instantaneous
    values.
  cite:
  - src: src:sma-kb-dns-server-could-not-be-resolved
    loc: sec=h1
    h: d5f02e3ee0df
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:igmp-snooping-disable
  cite:
  - src: src:sma-doc-246498
    loc: sec=h452
    h: 64911a47d918
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:lan-port-energy-saving-disable
  note: Another option is a router port where energy saving is off by default, for example LAN 1.
  cite:
  - src: src:sma-doc-246498
    loc: sec=h451
    h: b5c8afa18dff
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=37.r2
    h: 7b62eb0fafb1
  review: drafted
  review_note: 'support check: partial - u2 says configure the LAN ports not to be deactivated and u8
    says use LAN 1 where energy saving is usually disabled, though u8''s wording on the cause is garbled.'
- claim_id: c13
  rel: mitigated_by
  target: mit:firewall-port-opening
  cite:
  - src: src:sma-doc-246498
    loc: tbl=81.r1
    h: b9557e0ce5a3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h511
    h: c3abea00d0c7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h515
    h: c3abea00d0c7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h519
    h: c3abea00d0c7
  - src: src:kb-solis-44002762194-troubleshooting-s1-w4g-st-datalogger-network-connection-errors
    loc: sec=h10
    h: 8618f5032f7c
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:static-ip-public-dns
  note: 'Plan this carefully: a wrong static IP can cause IP conflicts or put the device outside the router''s
    address range.'
  cite:
  - src: src:sma-kb-dns-server-could-not-be-resolved
    loc: sec=h1
    h: d5f02e3ee0df
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:firmware-update
  note: For the affected STP50-41, update to 3.12.20.R or higher.
  cite:
  - src: src:sma-kb-stp50-41-dns-problem-when-using-lan-ethernet
    loc: sec=h1
    h: ad1188949ab2
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:network-connection-check
  note: Check network components such as DLAN and WLAN access points, Wi-Fi band and password, and that
    router DHCP is on.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h511
    h: c3abea00d0c7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h515
    h: c3abea00d0c7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h519
    h: c3abea00d0c7
  - src: src:kb-solis-44002762194-troubleshooting-s1-w4g-st-datalogger-network-connection-errors
    loc: sec=h10
    h: 8618f5032f7c
  review: drafted
---
This fault is in the network setup, not the PV hardware: the inverter or data logger cannot talk to the monitoring portal because of a network settings problem. It shows up as Webconnect errors such as no connection, or a DNS server that is not configured or could not be resolved. Sometimes the energy manager also cannot find devices on the network. Common causes are IGMP snooping on the switch, router LAN ports that shut down to save energy, and firewall rules that block the required ports. To confirm it, log into the inverter and read the Webconnect status, plus the current IP address, gateway and DNS server. To fix it, turn off IGMP snooping, stop the router from shutting down LAN ports, and open the required ports in the firewall. If DNS still fails, set a static IP address with a public DNS server, but plan it carefully so you do not create IP conflicts. On some STP50-41 firmware versions, DNS fails over LAN because of a firmware bug, and a firmware update fixes it.

<!-- review notes
- sentence 3: support check: partial - IGMP snooping and the firewall are stated as causes, but router LAN ports shutting down for energy saving is not clearly stated as a cause.
- sentence 5: support check: partial - IGMP snooping deactivation, not deactivating LAN ports and opening firewall ports are all stated, but energy-saving shutdown of ports is not explicitly stated.
- sentence 7: support check: partial - u11 states the affected firmware versions and the fix by firmware update, but never calls the cause a firmware bug.
- sentence 1: review: partial - The passages say Webconnect or portal communication errors probably come from network settings, but they never say 'not the PV hardware' and never mention data loggers, only inverters.
- sentence 7: review: partial - The affected STP50-41 firmware versions, the DNS failure over LAN and the fix by firmware update are all stated, but the article never calls the cause a firmware bug.
-->
