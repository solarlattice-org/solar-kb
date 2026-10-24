---
id: prod:ase-der-gateway
type: Product
name: ASE DER Gateway
aliases:
- CA Rule 21 Gateway
category: Monitoring and communications
make: ase
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:ase
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-billygambao-30264-5-mar-2023-option1-v1
    loc: sec=h14
    h: e653ef2ac1c7
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  review: drafted
  review_note: 'support check: partial - Passages show ASE/Kalkitech provides the gateway and kalki.io,
    but don''t explicitly state ASE Telemetry as the maker or the org name.'
- claim_id: c2
  rel: certified_to
  target: std:ieee-2030-5
  note: Described as SunSpec Certified IEEE 2030.5 DER gateways.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h13
    h: 26dd33529bb8
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:ieee-2030-5
  note: Used toward the utility headend and DER aggregators, and also to on-site DER devices.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h13
    h: 26dd33529bb8
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:csip
  note: CSIP-certified IEEE 2030.5 aggregator client.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h13
    h: 26dd33529bb8
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:dnp3
  note: Available both toward the utility side and toward on-site DER devices.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h13
    h: 26dd33529bb8
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:modbus
  note: Used to talk to on-site devices such as smart inverters or EMS.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h13
    h: 26dd33529bb8
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:cellular
  note: AT&T cellular connection comes pre-configured only in select DER Gateway models; data overages
    are billed extra.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-billygambao-30264-5-mar-2023-option2-v1
    loc: sec=h12
    h: 9cfca8652584
  review: drafted
- claim_id: c8
  rel: requires
  target: tool:kalki-io
  note: All DAS/DER gateways are to be registered and connected to the kalki.io portal.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-billygambao-30264-5-mar-2023-option1-v1
    loc: sec=h14
    h: e653ef2ac1c7
  - src: src:eq-equip-telemetry-ase-ase-info-billygambao-30264-5-mar-2023-option2-v1
    loc: sec=h13
    h: e653ef2ac1c7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c9
  rel: implements
  target: func:remote-firmware-update
  note: 'Through kalki.io: firmware, security patches, licenses and configuration files are updated remotely.'
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-billygambao-30264-5-mar-2023-option1-v1
    loc: sec=h14
    h: e653ef2ac1c7
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  review: drafted
- claim_id: c10
  rel: implements
  target: func:remote-maintenance
  note: Role-based remote access to field device programming ports over a secured link.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h13
    h: 26dd33529bb8
  review: drafted
- claim_id: c11
  rel: implements
  target: func:remote-inverter-control
  note: Lets the utility monitor and control DER assets through the gateway's IEEE 2030.5 aggregator client.
  cite:
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h9
    h: 26dd33529bb8
  - src: src:eq-equip-telemetry-ase-ase-info-das-gateway-techsheet
    loc: sec=h13
    h: 26dd33529bb8
  review: drafted
---
The ASE DER Gateway is a communications gateway that links a distributed energy resource site to the utility headend system and to DER aggregators. It is sold as a CA Rule 21 gateway and is described as SunSpec certified for IEEE 2030.5, with a CSIP-certified aggregator client. On the utility side it can use IEEE 2030.5, DNP3 or IEC 104. On site it talks to smart inverters or energy management systems over Modbus, DNP3 or IEEE 2030.5. Every gateway has to be registered with the kalki.io device management portal. Through that portal, firmware, security patches, licenses and configuration files are updated remotely, and events and alarms are monitored. Kalki.io also gives role-based remote maintenance access to the programming ports of field devices such as inverters and meters. ASE obtains and manages the SunSpec X.509 IEEE 2030.5 certificate. The customer has to get the utility's permission to connect to the utility DER server. Some models ship with an AT&T cellular connection already configured, and data overages are billed extra.

<!-- review notes
- sentence 2: support check: partial - SunSpec certified IEEE 2030.5 and CSIP-certified client are stated, and the product is called CA Rule 21 Gateway, though 'sold as' is slightly interpretive.
-->
