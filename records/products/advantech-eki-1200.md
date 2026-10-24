---
id: prod:advantech-eki-1200
type: Product
name: Advantech EKI-1200 Modbus gateways
aliases:
- EKI-1200
- EKI-122x
- EKI-1222
- EKI-1220
- EKI-122xR
- EKI-1222-CE
- EKI-1200 series
- EKI-122xR-CE Series
- EKI-1221
- EKI-1224
- Modbus router
category: Monitoring and communications
make: advantech
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:advantech
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122xr-um-df-10312018-manual
    loc: sec=3.1
    h: 1c8a11c01085
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-sop-modbus-gateway-redundancy-by-bridge-and-v
    loc: sec=h1
    h: 24628e33ae3d
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-sop-eki-122x-how-to-enable-new-jit-log-on-mod
    loc: sec=h1
    h: e9ecfaea0857
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:modbus-rtu
  note: Serial side; client/server (master/slave) mode selectable per serial port.
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h2
    h: 53ba0f503feb
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h2
    h: 71b5797819cd
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h8
    h: 71228e59a0d3
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h15
    h: 1f05b844b58b
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus-ascii
  note: Serial side; client/server (master/slave) mode.
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h2
    h: 53ba0f503feb
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h2
    h: 71b5797819cd
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h8
    h: 71228e59a0d3
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h15
    h: 1f05b844b58b
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus-tcp
  note: Network side; gateway bridges Modbus TCP and serial Modbus networks.
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h2
    h: 53ba0f503feb
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h15
    h: 1f05b844b58b
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:tcp-ip
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h2
    h: 53ba0f503feb
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h2
    h: 71b5797819cd
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:rs232
  note: Software-selectable serial interface on most models; the 4-port CI model is listed as RS-422/485
    only.
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h16
    h: 9a53fd64809b
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h15
    h: 1f05b844b58b
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:rs485
  note: 2-wire or 4-wire, with automatic RS-485 data flow control.
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h16
    h: 9a53fd64809b
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h15
    h: 1f05b844b58b
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:ethernet
  note: Two 10/100 Mbps ports for LAN redundancy.
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h15
    h: 1f05b844b58b
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h2
    h: 53ba0f503feb
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:udp
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:dhcp
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  review: drafted
- claim_id: c11
  rel: uses_protocol
  target: proto:snmp
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  review: drafted
- claim_id: c12
  rel: uses_protocol
  target: proto:http
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  review: drafted
- claim_id: c13
  rel: uses_protocol
  target: proto:smtp
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  review: drafted
- claim_id: c14
  rel: uses_protocol
  target: proto:ntp
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-ci-i-ds-modbus-gateway-cutsheet
    loc: sec=h6
    h: 944b6bcc7d79
  review: drafted
- claim_id: c15
  attr: max_count
  value:
    max: 16
    unit: unit:NUM
  conditions: Connections per serial port in Modbus client mode
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h15
    h: 1f05b844b58b
  review: drafted
- claim_id: c16
  attr: max_count
  value:
    max: 64
    unit: unit:NUM
  conditions: Sessions in Modbus server mode
  cite:
  - src: src:eq-equip-rs485-serial-converters-advantech-eki-1222-ce-eki-122x-series-cut-sheet
    loc: sec=h15
    h: 1f05b844b58b
  review: drafted
---
The Advantech EKI-1200 series is a family of two-way Modbus gateways. They connect Modbus RTU and Modbus ASCII serial devices to TCP/IP networks that use Modbus TCP. The family includes 1-port, 2-port and 4-port models. The I versions have a wide operating temperature range, and the CI versions add isolation and a wide operating temperature range. You choose the serial interface in software: RS-232, RS-422, or 2-wire or 4-wire RS-485. RS-485 data flow control is automatic. Each serial port can run in client (master) or server (slave) mode. A serial port supports up to 16 connections in client mode, and the gateway supports up to 64 sessions in server mode. Two independent Ethernet ports, dual power inputs and a virtual gateway feature give redundancy at the power, network and device level. You can configure the gateway with the Advantech EKI Device Configuration Utility, a web browser or a Telnet console. Configuration access can be limited to a single host PC. The network protocols it supports include DHCP, SNMP, HTTP, SMTP, NTP and UDP. CI models have port-to-port isolation and surge protection on the serial lines.

<!-- review notes
- sentence 4: support check: partial - Client/server (master/slave) per port and 16/64 limits are stated, but 64 sessions is not stated as gateway-wide versus per port.
- sentence 8: support check: partial - CI models have isolation and surge protection, but the isolation is serial-to-Ethernet/power and Ethernet-to-power, not specifically port-to-port between serial ports, and surge protection is line-to-line/ground rather than stated 'on serial lines'.
-->
