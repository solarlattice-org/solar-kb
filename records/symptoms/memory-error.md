---
id: symptom:memory-error
type: Symptom
name: Internal memory error
aliases:
- EepromErr
- Memory Fail
- Memory error detected
- Error in DSP data memory
- Internal memory error 1
- Memory loss
- Failure in memory/ EEPROM
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-output
  note: After a DSP RAM read or write error, the KACO unit does not feed the grid again until the next
    day or until it is reset.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r3
    h: 8047db4c6a7b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
An internal memory error shows up as an inverter status code or alarm. It means the internal memory, EEPROM or memory unit has a problem. On Fronius inverters, code 721 means the EEPROM was reinitialized or is defective. It appears as a warning on the display: acknowledge it, and call a trained service technician if it keeps coming back. Fronius code 451 reports a memory error and the inverter tries to reconnect by itself. Codes 516, 519 and 772 mean the memory unit cannot be reached or is unavailable. On CPS and Solectria inverters, the EepromErr alarm is an internal alarm. Watch it for 5 minutes to see if it clears by itself, and contact post-sales service if it does not. On the FIMER inverter, Memory Fail means it cannot communicate with the memory board that stores daily energy values. Remove the board, check the solder joints on the connector terminals, and reseat it firmly in its slot. On a KACO unit, a DSP RAM error can stop grid feed-in until the next day or a reset. Disconnect the DC side, wait 1 minute, then switch the unit back on. Check first whether the fault comes back after a restart. A fault that keeps returning points to defective memory hardware that needs service.

<!-- review notes
- sentence 4: support check: partial - The EepromErr definition and remedy are stated, but the passages don't name CPS or Solectria as the brands.
- sentence 7: support check: partial - Restart-then-service guidance is present, but 'defective memory hardware' as the conclusion for a recurring fault isn't stated; the passages only say to contact service if it persists.
- sentence 7: review: partial - Restarting and contacting service if the fault persists is stated, but the conclusion that a recurring fault points to defective memory hardware is not in the passages.
-->
