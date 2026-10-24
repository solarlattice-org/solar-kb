---
id: prod:apsmart-rsd
type: Product
name: APsmart RSD rapid shutdown system
aliases:
- RSD-S-PLC
- RSD-D
- RSD-START-KIT
- APsmart Transmitter
- RSD-D(S)-PLC
- APsmart Rapid Shutdown System
- Transmitter-PLC
- Transmitter-PLC-1P
- Transmitter-PLC Outdoor Kit
category: MLPE
make: apsmart
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:apsmart
  cite:
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h2
    h: f2a667e1df6f
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h2
    h: fb22deeda601
  - src: src:eq-equip-rsd-apsmart-4301515202-transmitter-plc-datasheet-rev2-9-2023-10-07-na-1
    loc: sec=h2
    h: ebd759299477
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:rapid-shutdown-device
  cite:
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h12
    h: a0aeeda7329e
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h12
    h: a6f413982448
  - src: src:eq-equip-rsd-apsmart-4302315202-rsd-d-datasheet-rev2-4-2025-01-23
    loc: sec=h2
    h: 65bfe13ed672
  review: drafted
- claim_id: c3
  rel: implements
  target: func:rapid-shutdown
  note: Module units shut down when the Transmitter-PLC heartbeat signal is absent; manual shutdown via
    the Transmitter breaker switch.
  cite:
  - src: src:abb-fimer-apsmart-rsd-field-install
    loc: sec=h3
    h: c392ffc1e53e
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h8
    h: 9bc7851eed80
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h8
    h: b10ab25df068
  - src: src:eq-equip-rsd-apsmart-4301515202-transmitter-plc-datasheet-rev2-9-2023-10-07-na-1
    loc: sec=h2
    h: ebd759299477
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:sunspec-rapid-shutdown-signal
  note: Heartbeat signal sent by the Transmitter-PLC over the PV conductors.
  cite:
  - src: src:abb-fimer-apsmart-rsd-field-install
    loc: sec=h3
    h: c392ffc1e53e
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h12
    h: a0aeeda7329e
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h12
    h: a6f413982448
  - src: src:eq-equip-rsd-apsmart-4301515202-transmitter-plc-datasheet-rev2-9-2023-10-07-na-1
    loc: sec=h2
    h: ebd759299477
  review: drafted
  review_note: 'support check: partial - SunSpec rapid shutdown signal and heartbeat are stated, but sending
    over the PV conductors is not stated.'
- claim_id: c5
  rel: uses_protocol
  target: proto:power-line-communication
  note: PLC transmitter keeps module units connected while powered.
  cite:
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h12
    h: a0aeeda7329e
  - src: src:eq-equip-rsd-apsmart-4301515202-transmitter-plc-datasheet-rev2-9-2023-10-07-na-1
    loc: sec=h2
    h: ebd759299477
  review: drafted
  review_note: 'support check: partial - The transmitter keeping modules connected is stated, but the
    passages don''t state power line communication as the medium beyond the ''PLC'' name.'
- claim_id: c6
  rel: certified_to
  target: std:sunspec-rapid-shutdown
  note: Sources state it meets SunSpec requirements.
  cite:
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h8
    h: 9bc7851eed80
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h8
    h: b10ab25df068
  - src: src:eq-equip-rsd-apsmart-4301515202-transmitter-plc-datasheet-rev2-9-2023-10-07-na-1
    loc: sec=h2
    h: ebd759299477
  review: drafted
  review_note: 'support check: partial - Passages say it meets SunSpec requirements, but not that it is
    certified to the SunSpec specification.'
- claim_id: c7
  rel: certified_to
  target: req:nfpa-70-2017-690-12
  cite:
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h8
    h: 9bc7851eed80
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h8
    h: b10ab25df068
  - src: src:eq-equip-rsd-apsmart-4301515202-transmitter-plc-datasheet-rev2-9-2023-10-07-na-1
    loc: sec=h2
    h: ebd759299477
  review: drafted
  review_note: 'support check: partial - Passages say it meets/complies with NEC 2017 690.12, but do not
    say it is certified.'
- claim_id: c8
  rel: certified_to
  target: req:nfpa-70-2020-690-12
  cite:
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h8
    h: 9bc7851eed80
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h8
    h: b10ab25df068
  - src: src:eq-equip-rsd-apsmart-4301515202-transmitter-plc-datasheet-rev2-9-2023-10-07-na-1
    loc: sec=h2
    h: ebd759299477
  review: drafted
  review_note: 'support check: partial - Passages say it meets/complies with NEC 2020 690.12, but not
    that it is certified.'
- claim_id: c9
  rel: certified_to
  target: req:nfpa-70-2023-690-12
  cite:
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h8
    h: 9bc7851eed80
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h8
    h: b10ab25df068
  - src: src:eq-equip-rsd-apsmart-4301515202-transmitter-plc-datasheet-rev2-9-2023-10-07-na-1
    loc: sec=h2
    h: ebd759299477
  review: drafted
  review_note: 'support check: partial - Passages say it meets/complies with NEC 2023 690.12, but not
    that it is certified.'
- claim_id: c10
  rel: lacks
  target: func:dc-arc-fault-protection
  note: No automatic shutdown on arc detection; designed to reduce fire-fighting risk but does not address
    arc fire risk.
  cite:
  - src: src:eq-equip-rsd-apsmart-rsd-s-plctransmitter-user-manual-na-en-rev4-2-2025-07-07
    loc: sec=h8
    h: 9bc7851eed80
  - src: src:eq-equip-rsd-apsmart-4302315102-rsd-dtransmitter-plc-user-manual-rev3-1-2025-01-24-na1
    loc: sec=h8
    h: b10ab25df068
  - src: src:eq-equip-rsd-apsmart-4302315202-rsd-d-datasheet-rev2-4-2025-01-23
    loc: sec=h3
    h: 18563dea9677
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:abb-uno-dm-3-3-5-0-plus-us
  conditions: UNO-DM-TL-PLUS-US-Q models, all versions, with RSD-D(S)-PLC and Transmitter-PLC
  cite:
  - src: src:abb-fimer-apsmart-rsd-field-install
    loc: sec=h3
    h: c392ffc1e53e
  review: drafted
- claim_id: c12
  rel: compatible_with
  target: prod:abb-uno-dm-6-0-plus-us
  conditions: UNO-DM-6.0-TL-PLUS-US-Q, all versions, with RSD-D(S)-PLC and Transmitter-PLC
  cite:
  - src: src:abb-fimer-apsmart-rsd-field-install
    loc: sec=h3
    h: c392ffc1e53e
  review: drafted
- claim_id: c13
  rel: compatible_with
  target: prod:yaskawa-solectria-pvi-25tl-480-aps20
  conditions: RSD-S-PLC and RSD-D with inverter plus integrated wire box; listed as PVRSS certified
  cite:
  - src: src:yaskawa-yss-rsd-mlpe-compatibility-matrix-rev5
    loc: tbl=1.r2
    h: 01eef1121573
  review: drafted
- claim_id: c14
  rel: compatible_with
  target: prod:yaskawa-solectria-pvi-25tl-208wb-aps
  conditions: RSD-S-PLC and RSD-D with wire box; listed as PVRSS certified
  cite:
  - src: src:yaskawa-yss-rsd-mlpe-compatibility-matrix-rev5
    loc: tbl=1.r6
    h: 2b725f0e010a
  review: drafted
---
The APsmart RSD system is a module-level rapid shutdown solution for North America, made up of RSD-S-PLC or dual-input RSD-D module units and a Transmitter-PLC. While the transmitter is powered it sends a heartbeat signal that keeps the modules connected; when the transmitter is switched off or its signal is lost, the module units go into rapid shutdown and restart once power comes back. You can trigger a manual shutdown with the transmitter breaker switch, or with an optional emergency stop button box on the outdoor kit that cuts the transmitter's AC supply. The system meets the SunSpec rapid shutdown signaling requirements and NEC 690.12 in the 2017, 2020 and 2023 editions. The module units do not shut down automatically when an arc is detected. They reduce the risk for firefighters but do not remove the risk of an arc fire. It is listed as compatible with FIMER UNO-DM-TL-PLUS-US-Q inverters and with Yaskawa Solectria PVI-25TL wire box models, where it is shown as PVRSS certified. If the inverter already has a SunSpec-certified rapid shutdown transmitter built in, leave out the external Transmitter-PLC.
