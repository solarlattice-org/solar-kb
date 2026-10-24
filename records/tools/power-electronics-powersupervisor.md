---
id: tool:power-electronics-powersupervisor
type: Tool
name: Power Electronics PowerSupervisor
aliases:
- PowerSupervisor
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:power-electronics
  note: Manual describes it as a software tool for use with Power Electronics products.
  cite:
  - src: src:eq-equip-inverters-power-electronics-software-powersupervisor-en
    loc: sec=h5
    h: 02fef817ce23
  - src: src:eq-equip-inverters-power-electronics-software-powersupervisor-en
    loc: sec=h11
    h: 4bd43096736d
  - src: src:eq-equip-inverters-power-electronics-software-powersupervisor-en
    loc: sec=h8
    h: 149cb30fdb18
  review: drafted
  review_note: 'support check: partial - Passages say it is a tool for Power Electronics products and
    give company contacts, but never explicitly state that Power Electronics makes it (only implied by
    ''our products'').'
- claim_id: c2
  rel: uses_protocol
  target: proto:tcp-ip
  note: Monitoring and configuration of supported equipment is done over TCP/IP.
  cite:
  - src: src:eq-equip-inverters-power-electronics-software-powersupervisor-en
    loc: sec=h11
    h: 4bd43096736d
  review: drafted
---
PowerSupervisor is a Windows application from Power Electronics for monitoring and configuring the company's equipment over TCP/IP. Use it to speed up commissioning and maintenance work: it gives technicians remote access, can save configuration backups, and has charts for tracking inverter performance. Work is organised in plant files. From the main screen you can open an existing plant file or create a new one, and the last 10 plant files you opened are listed for quick access. When the computer is online, the software looks for a new version at startup, installs it in the background, and runs the new version the next time it is launched. The manual is written for qualified customers. Other customers are pointed to the PowerMonitoring manual instead. The software comes in English and Spanish. The first edition of the manual covers software version 13.3.0.

<!-- review notes
- sentence 3: support check: partial - Open/create plant file and last 10 recent files are stated, but 'work is organised in plant files' is only implied.
- sentence 5: support check: partial - Targeted to qualified customers is stated, but the passage says 'For customers, refer to PowerMonitoring Manual' (likely garbled), so 'other customers' is an interpretation.
-->
