---
id: func:disable-permit-service
type: Function
name: Permit service / cease to energize
aliases:
- disable permit service
- cease to energize
- connect/disconnect command
- remote disconnect
- cease to energize and trip
- Permit service
category: Control
function_kind: control
claims:
- claim_id: c1
  attr: trip_time
  value:
    max: 2
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: Time to cease to energize and trip after the permit service setting is disabled
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=4.6.1
    h: 16f92e29ae87
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c2
  attr: trip_time
  value:
    max: 2
    unit: unit:SEC
  scope:
    regions:
    - region:us-ca
    standard: std:cpuc-rule-21
    valid_from: '2023-08-29'
  conditions: UL 1741 SB smart inverter receiving a disable permit service command via communication;
    alternative is to initiate opening of a switch for galvanic isolation
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: sec=h553
    h: 76add0fb8947
  review: drafted
---
Permit service is an on/off setting that decides whether a DER may enter service or stay in service; if it is set to disabled, the DER must cease to energize the Area EPS and trip. While it has ceased to energize, the DER may not deliver active power. Any reactive power exchange must come only from passive devices and stay below 10% of nameplate when the aggregate rating is under 500 kVA, or below 3% at 500 kVA and above. Another way to meet the requirement is to disconnect the local EPS from the Area EPS. A DER cannot enter service again until voltage and frequency are within the enter-service ranges and permit service is set back to Enabled. To field-check cease to energize, operate a load interrupting device and confirm the output terminals go dead and do not reconnect before the required delay. Repeat this on each phase. Some utility commissioning requirements point to the IEEE 1547.1a clause 7.5.1 procedures for this test instead. In the Yaskawa Solectria SGI XTM Modbus map, fault value 13 means Grid Support Cease Energize. Tesla commercial battery controls have a read-only Cease to Energize status bit at register 22275 and a writable Permit boolean at register 22262 that lets the system resume operation.

<!-- review notes
- sentence 2: support check: partial - Passages support the no-active-power rule, the passive-device reactive limits and the disconnection alternative. But they permit import of power for housekeeping and auxiliary loads, so 'may not deliver active power' is fine while the omitted exception is a detail.
- sentence 5: support check: partial - The passage says testing follows IEEE 1547.1a Clause 7.5.1, but it does not show this is only some utilities' commissioning requirements or an alternative to another procedure.
-->
