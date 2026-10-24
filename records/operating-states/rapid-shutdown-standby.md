---
id: state:rapid-shutdown-standby
type: OperatingState
name: Rapid shutdown safe state
aliases:
- RSD standby
- safe mode
- module-level shutdown state
- rapid shutdown state
category: MLPE
claims:
- claim_id: c1
  rel: part_of
  target: func:rapid-shutdown
  note: The safe state is the result of the rapid shutdown function being executed after the keep-alive
    or AC signal is lost or an initiator is pressed.
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=1.1
    h: 589ca577d9c1
  - src: src:abb-fimer-apsmart-rsd-field-install
    loc: sec=h3
    h: c392ffc1e53e
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: sec=2.8.1
    h: c188cd5199a8
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Passages describe shutdown on loss of AC/heartbeat signal or
    RSD button press, but none defines a ''safe state'' concept or states it as the result of those triggers.'
- claim_id: c2
  attr: output_limit
  value:
    max: 30
    unit: unit:V
  scope:
    products:
    - prod:solis-rsd
  conditions: PV array and inverter DC capacitors after first responders cut AC power to the building;
    reached in under 10 seconds
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=1.1
    h: 589ca577d9c1
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  attr: output_limit
  value:
    max: 240
    unit: unit:V-A
  scope:
    products:
    - prod:solis-rsd
  conditions: PV array output after AC power to the building is cut; reached in under 10 seconds
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=1.1
    h: 589ca577d9c1
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Passage says ''240VA'' (garbled 240VAin) within 10 seconds after
    AC is cut, but it applies to array and capacitors together and the unit is ambiguous.'
- claim_id: c4
  rel: part_of
  target: req:nfpa-70-2017-690-12
  note: The initiation device off position shows that the safe state has been commanded.
  quote: The device "off" positin shallindiate thet the rapid shutdown function has been initiated
  cite:
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h53
    h: dbd263da1130
  review: drafted
  review_note: 'support check: partial - 690.12(C) says the off position indicates rapid shutdown has
    been initiated, but ''safe state'' isn''t mentioned; it says initiated, not that the safe state is
    commanded.; review: partial - 690.12(C) supports the link to NEC 690.12 and says the off position
    indicates the rapid shutdown function has been initiated, but the passage never mentions a ''safe
    state'' being commanded.'
---
The rapid shutdown safe state is the condition in which module-level shutdown devices have de-energized the PV array conductors after rapid shutdown was triggered. With SunSpec-type PLC devices, the module devices keep running only while they receive a continuous heartbeat signal from the transmitter, and they shut down once that signal stops. With AC-signal devices, cutting AC power to the building makes the devices pull the array and inverter DC capacitors down to a low safe voltage within seconds. A green LED on the device means AC power is present and its PV output may be live. On some hybrid inverters, pressing the RSD button cuts power to the internal transmitter, switches off the battery input and shuts the inverter down. The off position of the initiation device shows that rapid shutdown has been initiated, and SMA inverters log the event message Rapid shutdown has been triggered. On one SMA device, a green Ready LED that turns on for five seconds and off for five seconds means the system is in Safe Mode. No action is needed while shutdown is intended. If an Enphase IQ System Controller stays in the rapid shutdown state after the initiator is reset, the installer should test the RSD switch wiring, then the equipment and then the E3 board. A rapid shutdown system error on the IQ System Controller appears as Manual Override on the Installer Portal dashboard.

<!-- review notes
- sentence 1: support check: partial - Passages say the array drops to 30V after the trigger, but do not describe module-level devices de-energizing array conductors as a defined safe state.
- sentence 7: support check: partial - Passages say to test RSD wiring and then the E3 board after equipment/wiring, but 'no action needed while shutdown is intended' and the explicit order and initiator reset are not stated.
- sentence 7: review: partial - The passages support testing the wiring and then the E3 board after equipment and wiring when the controller is stuck in rapid shutdown, but 'no action needed while shutdown is intended' and 'after the initiator is reset' are not stated.
-->
