---
id: concept:scada
type: Concept
name: SCADA
aliases:
- supervisory control and data acquisition
- Supervision Control And Data Acquisition
- Supervisory Controls and Data Acquisition
category: Monitoring
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:data-acquisition-system
  note: A SCADA package covers control, telemetry (data acquisition), Historian data storage and data
    access.
  cite:
  - src: src:tesla-scada-design-manual-v3-4
    loc: sec=2
    h: cca0022f6ac4
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:remote-monitoring
  note: SCADA monitors real-time data and helps troubleshoot faults remotely.
  cite:
  - src: src:eq-equip-trackers-ati-array-tech-v3-presentation
    loc: sec=h18
    h: 707b352adce3
  review: drafted
- claim_id: c3
  rel: related_to
  target: proto:modbus
  note: SMA uses SCADA, the control center software, as its example of a Modbus master system.
  cite:
  - src: src:eq-equip-inverters-sma-sunny-central-modbus-sc2xxx-ti-en-17
    loc: tbl=7.r14
    h: 1784ec82ac3e
  review: drafted
  review_note: 'support check: partial - Passage says SCADA is used as an example Modbus master system,
    but it does not name SMA; the manufacturer attribution is not in the passage.'
- claim_id: c4
  rel: related_to
  target: concept:automatic-reclosing
  note: The NESC allows SCADA to disable a recloser's automatic reclosing if confirmation signals and
    tags or electronic displays are in place.
  cite:
  - src: src:std-standards-nesc-2017-nesc
    loc: sec=h476
    h: a333f906925b
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:ip-addressing
  note: Tesla's SCADA design manual gives SCADA devices such as the RTAC, the SEL-700G relay and the meters
    static IP addresses.
  cite:
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=13.r9
    h: c9fdb82e3634
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=13.r10
    h: c5eae8d82f9f
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=13.r4
    h: 09e5c939fbf9
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=13.r11
    h: 4ba1e14a37e8
  review: drafted
  review_note: 'support check: partial - RTAC, SEL700G and meters have Static DHCP status, but the passages
    do not say it''s Tesla''s SCADA design manual (implied), and the relay is named SEL700G; mostly fine
    but source attribution is not stated.'
- claim_id: c6
  rel: related_to
  target: prod:sel-rtac
  note: The RTAC appears in the device IP plan of Tesla's SCADA design manual.
  cite:
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=13.r9
    h: c9fdb82e3634
  review: drafted
- claim_id: c7
  rel: related_to
  target: comp:single-axis-tracker
  note: SCADA monitors trackers and can send them set-point change commands.
  cite:
  - src: src:eq-equip-trackers-ati-array-tech-v3-presentation
    loc: sec=h18
    h: 707b352adce3
  review: drafted
- claim_id: c8
  rel: related_to
  target: state:stopped
  note: Sunny Central return code 21609 means the inverter was stopped by SCADA or a PPC over Modbus.
  cite:
  - src: src:eq-equip-inverters-sma-sunny-central-modbus-sc2xxx-ti-en-17
    loc: tbl=35.r13
    h: 88fd7adbb356
  review: drafted
  review_note: 'support check: partial - Return code 21609 reads ''Stop: Scada or PPC, Modbus'', but the
    passage does not mention Sunny Central or explicitly say the inverter was stopped.'
- claim_id: c9
  rel: related_to
  target: state:standby
  note: Sunny Central return code 21612 means the inverter was put in standby by SCADA or a PPC over Modbus.
  cite:
  - src: src:eq-equip-inverters-sma-sunny-central-modbus-sc2xxx-ti-en-17
    loc: tbl=35.r15
    h: 2ff133ad4e92
  review: drafted
  review_note: 'support check: partial - Return code 21612 reads ''Standby: Scada or PPC, Modbus'', but
    the passage does not mention Sunny Central or explicitly say the inverter was put in standby.'
---
SCADA stands for supervisory control and data acquisition. A SCADA system is a set of computer systems with logical and physical interfaces that monitor and control how a facility operates. At a solar plant, SCADA gathers and analyzes real-time data from trackers and other generating equipment. It stores this data so output can be optimized, and it helps find faults and troubleshoot them remotely. SCADA also sends commands, such as set-point changes to trackers. On some central inverters, a stop or standby command from SCADA or a power plant controller over Modbus shows up as its own return code. In Modbus terms, SCADA is the control center software that acts as the master polling field devices. SCADA networks usually give devices like automation controllers, protection relays and meters static IP addresses. Utilities use SCADA measurements to build load and PV models. That data has to match the same time period and feeder configuration as the analysis. If SCADA disables a recloser's automatic reclosing during work, the NESC requires a confirmation signal and a visible tag or display, both at the operating point and at the device.

<!-- review notes
- sentence 4: support check: partial - Set-point commands and the return codes for stop and standby from SCADA or PPC over Modbus are present, but 'central inverters' is not stated in the passages.
- sentence 5: support check: partial - Passage says SCADA is control center software used as an example Modbus master, but it does not say it polls field devices.
- sentence 6: support check: partial - The passages show static IPs for specific devices in one design table, but they do not show that SCADA networks usually do this.
- sentence 7: support check: partial - Passage says SCADA data can model load and PV and must match the same period and feeder configuration, but it says utilities use it only implicitly, and it also covers validating results.
- sentence 8: support check: partial - NESC requires a confirmation signal and tag or display at the SCADA point, but at the device it requires either preventing manual override or a signal or flag, not a tag.
-->
