---
id: tool:delta-electronics-dss
type: Tool
name: Delta Solar System Software (DSS)
aliases:
- Delta Solar System Software
- DSS 3ph
- DSS V5
- DSS
- Delta solar system
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:delta-electronics
  note: Delta's guide names its own Delta solar system software as the tool for checking inverter values.
  cite:
  - src: src:eq-equip-inverters-delta-heco-information-hawaii-delta-introduction-of-heco-rule14-default-setting-2
    loc: sec=h3
    h: 3bd9659c4cd2
  review: drafted
  review_note: 'support check: partial - Passage names Delta''s own ''Delta solar system (DSS)'' software
    for checking inverter values, but nothing explicitly states Delta Electronics makes it beyond the
    name.'
- claim_id: c2
  rel: uses_protocol
  target: proto:rs485
  note: Connects from a laptop to the inverters through a USB-to-RS485 converter. The RS485 COM port is
    chosen in the Communication dropdown.
  cite:
  - src: src:eq-equip-inverters-delta-heco-information-hawaii-delta-introduction-of-heco-rule14-default-setting-2
    loc: sec=h3
    h: 3bd9659c4cd2
  - src: src:eq-equip-inverters-delta-m60u-m80u-firmware-fw-update-via-dss
    loc: sec=front
    h: 5db42dfe28da
  - src: src:eq-equip-inverters-delta-delta-solar-system-software-dss-3ph-ul-v5-4-2-fw-update
    loc: sec=front
    h: 26b2fb6b34eb
  review: drafted
---
Delta Solar System Software (DSS) is a Delta PC program. It runs on a laptop and connects to Delta three-phase string inverters through a USB-to-RS485 converter. To connect, choose 3ph-MxxU in Monitor Mode and pick the RS485 COM port. Start communication, enter the start and end inverter IDs, then search. Make sure every needed ID is found before you go on. For a firmware update, open the Firmware screen, browse to the supplied file and press Upgrade. Wait for the Upgrade Done pop-up. An inverter can have up to five boards that may need updating: AFCI, COMM, CS, DSP and RED. The firmware file names show which board each file is for. If different models share one daisy-chained RS485 line, uncheck the IDs you do not want to update before loading DSP or COMM firmware. DSS can also save the inverter's grid settings to an Excel file and load an edited file back. This function needs password access.

<!-- review notes
- sentence 6: support check: partial - Save to excel, load edited file and password access are stated, but 'grid settings' and that the password applies to this function are only implied by headings; load of edited file is stated.
-->
