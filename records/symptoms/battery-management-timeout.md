---
id: symptom:battery-management-timeout
type: Symptom
name: External battery management timeout
aliases:
- ExtBMSTimeout
- WrnExtBMSTmOut
- Event 9308
- F952
- W953
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Sunny Island shows F952 (ExtBMSTimeout, level 3) or W953 (WrnExtBMSTmOut, level 1 warning) when
    the battery management timeout monitor triggers.
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=84.r11
    h: 64475c2614a9
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r17
    h: 804f83351d54
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r18
    h: 06c5e3c86a9e
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=84.r12
    h: c2de461cfa32
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:bms-error-message
  note: 'Logged as Event 9308 (battery error or battery fault): the external battery management cannot
    be reached and communication with the BMS has been interrupted.'
  cite:
  - src: src:sma-doc-278742
    loc: tbl=76.r6
    h: b6a661156a04
  - src: src:sma-doc-259761
    loc: tbl=72.r6
    h: cefb8bc9ec0c
  - src: src:sma-kb-f952-or-event-9308-extbmstimeout-error-on-sunny-island
    loc: sec=h1
    h: 498b8c50cddf
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h58
    h: 484cff67fd34
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h50
    h: 7a6c31c14118
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
This shows up on the battery inverter as fault F952 or warning W953, or as Event 9308 in the event log, when the timeout monitor for the external battery management system triggers. It means the inverter can no longer reach the external battery management system: communication between the Sunny Island and the lithium-ion battery BMS has been interrupted. Check the communication cabling first. Make sure the data cable to the external lithium-ion battery is connected correctly and is no longer than 30 meters. Next, confirm that the CAN or ComSync communication bus has a terminator at its end. On the Sunny Island this terminator resistor goes on the ComSyncOut port. On networked models, check that the battery communication parameters, such as the IP address, are set correctly. The inverter can take up to 10 minutes to switch back on after this event. This is not the same as F221 or Event 9332, where the battery management is detected but has not been configured. In that case, set up the system again with external energy management. It is also not the same as E906 to E908 or F931. Those codes pass on errors reported by the BMS itself, so check the battery manufacturer's documentation for them. If the timeout continues after the cabling, termination and settings have been checked, contact SMA Service.

<!-- review notes
- sentence 3: support check: partial - The data cable being connected correctly and the 30 m limit are both stated, but the passages don't say to check cabling first, so that ordering is missing.
- sentence 4: support check: partial - The terminator requirement and the ComSyncOut port are stated, but the passages give no ordering such as checking this 'next'.
- sentence 5: support check: partial - Checking the parameters such as the IP address and the up to 10 minutes wait are stated, but the 'networked models' qualifier is not in the passages.
- sentence 8: support check: partial - The SMA article says to contact SMA Service if the issue persists after the above steps, but those steps cover only cabling length and termination, not the settings check.
-->
