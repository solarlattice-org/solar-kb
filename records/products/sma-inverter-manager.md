---
id: prod:sma-inverter-manager
type: Product
name: SMA Inverter Manager
aliases:
- Inverter Manager
category: Monitoring and communications
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-doc-278879
    loc: tbl=33.r1
    h: de34be78ad63
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  review: drafted
  review_note: 'support check: partial - The passages name the product ''SMA Inverter Manager'' and the
    text mentions SMA, but nothing explicitly states SMA manufactures it.'
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  note: Device for monitoring and controlling inverters in decentralized PV plants
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  review: drafted
- claim_id: c3
  attr: max_count
  value:
    max: 42
    unit: unit:NUM
  conditions: Sunny Tripower 60 or Sunny Highpower 75 inverters monitored and controlled per Inverter
    Manager
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  review: drafted
- claim_id: c4
  attr: max_count
  value:
    max: 20
    unit: unit:NUM
  conditions: Sunny Tripower Storage 60 units with battery storage per Inverter Manager
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  review: drafted
- claim_id: c5
  attr: operating_temperature
  value:
    min: -40
    max: 75
    unit: unit:DEG_C
  conditions: Operating temperature range; relative humidity 5 % to 95 % non-condensing
  cite:
  - src: src:sma-doc-278879
    loc: sec=3.6
    h: '1e4642883028'
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:sma-sunny-tripower-60
  note: Up to 42 units; to be operated exclusively with Sunny Tripower 60, Sunny Tripower Storage 60 and
    Sunny Highpower Peak1
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:sma-shp-peak1
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  review: drafted
- claim_id: c8
  rel: compatible_with
  target: prod:sma-sunny-tripower-storage-60
  note: Up to 20 units with battery storage systems
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c9
  rel: requires
  target: tool:sma-lcs-tool
  note: LCS-Tool on a PC via Ethernet is the primary user interface and is needed to commission and maintain
    the inverters through the Inverter Manager
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:ethernet
  note: LAN 1 to the external network, LAN 2 to the inverters (RJ45); maximum Ethernet cable length 100
    m
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c11
  rel: uses_protocol
  target: proto:rs485
  note: D-Sub 9 RS485 in SunSpec mode for the optional I/O Box and for SunSpec-compatible weather stations;
    maximum RS485 cable length 1200 m
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c12
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: SunSpec Modbus TCP is used for plant monitoring and for remote active/reactive power setpoints
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  rel: uses_protocol
  target: proto:modbus-tcp
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c14
  rel: implements
  target: func:active-power-setpoint
  note: As a constant value, a curve, or a remote command via SunSpec Modbus TCP with the I/O Box
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c15
  rel: implements
  target: func:remote-dispatch
  note: Grid management commands arrive as digital signals at the I/O Box, which passes setpoints to the
    Inverter Manager; it then controls every inverter in the plant
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c16
  rel: implements
  target: func:communication-loss-fallback
  note: If communication with the Inverter Manager is lost, the inverters switch to a predefined fallback
    state set in the grid code file or through LCS-Tool; a system fallback toward a superior SCADA or
    power plant controller can also be configured
  cite:
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: sec=6.6
    h: d97262135449
  review: drafted
- claim_id: c17
  rel: requires
  target: prod:sma-digital-io-box
  note: Optional; required to receive digital grid management signals
  cite:
  - src: src:sma-doc-278879
    loc: sec=h343
    h: bac64c9aebcf
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
  review_note: 'support check: partial - I/O Box is described as optional and receiving grid management
    signals, but ''requires'' is not strictly stated beyond that function.; review: partial - The passages
    support that the I/O Box receives digital grid-management signals and relays setpoints, but they mark
    the I/O Box interface as optional (''en option''), so the bare ''requires'' relation is not supported.'
- claim_id: c18
  rel: certified_to
  target: std:ul-508
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c19
  rel: certified_to
  target: std:ul-60950-1
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c20
  rel: certified_to
  target: std:csa-c22-2-no-60950-1-07
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c21
  rel: certified_to
  target: std:en-60950-1
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c22
  rel: certified_to
  target: std:en-55022
  note: Class A
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c23
  rel: certified_to
  target: std:en-61000-3-2
  note: Class D
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c24
  rel: certified_to
  target: std:en-61000-3-3
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c25
  rel: certified_to
  target: std:en-55024
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
- claim_id: c26
  rel: certified_to
  target: std:fcc-part-15b
  note: Class A
  cite:
  - src: src:sma-doc-278879
    loc: tbl=84
    h: a5bef107f01c
  review: drafted
---
The SMA Inverter Manager is an SMA device that monitors and controls inverters in decentralized PV plants. It is meant for indoor use only. One unit can handle up to 42 Sunny Tripower 60 or Sunny Highpower 75 inverters, or up to 20 Sunny Tripower Storage 60 units with battery storage. It may only be used with the Sunny Tripower 60, the Sunny Tripower Storage 60 and the Sunny Highpower Peak1. You need the LCS-Tool on a PC connected over Ethernet to commission and maintain the inverters. The LCS-Tool is the main user interface for the plant. The unit has two Ethernet ports: LAN 1 goes to the external network and LAN 2 goes to the inverters. An RS485 port in SunSpec mode connects the optional I/O Box and SunSpec-compatible weather stations. Monitoring works through Sunny Portal or SunSpec Modbus TCP. Active and reactive power setpoints can be a constant value, a curve, or a remote command sent via SunSpec Modbus TCP with the I/O Box. If the inverters lose communication with the Inverter Manager, they switch to a fallback state that was set in advance in the grid code file or through the LCS-Tool. Its operating temperature range is -40 °C to +75 °C, and it runs on a 9 to 36 V DC supply.
