---
id: tool:yaskawa-solectria-solrenview
type: Tool
name: SolrenView
aliases:
- SolrenView data logger
- SolrenView web monitoring
- SolrenView gateway
- SolrenView DAS
- SolrenView Web-Based Monitoring
- SolrenView.com
- SRV data logger
- SolrenView Logger
- SRV-LCD-3PTL-OUTDOOR
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:yaskawa-solectria
  note: Sources call it Solectria's own SolrenView monitoring system.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=4.8.8
    h: 5667bd0db47c
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=2.4.4
    h: 314a24ec8fcb
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: sec=7
    h: ca9b77b77664
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: uses_protocol
  target: proto:modbus
  note: Data logger polls inverters and revenue-grade meters on a Modbus daisy chain with unique Modbus
    IDs.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=h69
    h: 1b777fbc51b3
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=2.4.4
    h: 314a24ec8fcb
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: uses_protocol
  target: proto:ethernet
  note: Uplink to SolrenView servers over Ethernet twisted pair through a customer-supplied gateway.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=4.8.8
    h: 5667bd0db47c
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=h69
    h: 1b777fbc51b3
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: sec=7
    h: ca9b77b77664
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  note: RS-485 wiring from the PVI 23-28TL inverter can be fed directly into SolrenView.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: sec=14.2
    h: 60255fd61884
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
SolrenView is the Yaskawa Solectria web-based monitoring service, made up of a data logger or gateway that regularly collects operating values from the inverter and sends them to the SolrenView monitoring servers. It is an optional monitoring add-on for Solectria string inverters such as the PVI 3800-7600TL, PVI 14-20TL, PVI 23-28TL and PVI 50-60TL, and it is also used with SGI central inverters. To enable data logging, turn on SRV Mode in the inverter Config menu. If the logger cannot upload, it stores data in flash memory, and after a few weeks the oldest data is lost, so get internet working soon after commissioning. Customer Support must activate the monitoring site. An I in the upper right corner of the logger screen confirms a connection to the SolrenView servers. Leave SRV Mode off when a third-party monitoring service is used or when SolrenView service has not been purchased. Only qualified personnel should make SolrenView connections, and all DC and AC power must be disconnected first because of the risk of electric shock.

<!-- review notes
- sentence 2: support check: partial - The passages cover the PVI 3800-7600TL, 14-20TL, 23-28TL and 50-60TL as optional or external, but nothing states SGI central inverters use SolrenView.
-->
