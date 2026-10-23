---
id: symptom:anti-islanding-disabled
type: Symptom
name: Anti-islanding protection disabled
aliases:
- SPUI
- Special Purpose Utility-Interactive
- Active Anti islanding Disabled
- Passive Anti islanding Disabled
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'Fronius Symo shows state code 581 when the Special Purpose Utility-Interactive (SPUI) setup is
    active. Islanding protection is then deactivated and the unit no longer complies with IEEE1547. The
    manual says this is not an error: confirm the code with the Enter key.'
  quote: the islanding function is deactivated, frequency-dependent power reduction is activated, and
    the frequency and voltage limits are being changed
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r18
    h: ca9a756700ef
  review: drafted
---
On a Fronius Symo, this condition appears on the display as state code 581. The code means the Special Purpose Utility-Interactive setup has been activated. In this mode the islanding function is switched off, power is reduced depending on frequency, and the frequency and voltage limits are changed. The inverter then no longer meets IEEE1547. Fronius says code 581 is not an error, and the operator confirms it with the Enter key. Even so, check that the deactivated islanding protection was intended for this site. Keep this separate from code 456, which means the anti-islanding function has stopped running properly. That is a malfunction, not a deliberate setting. On some other products, anti-islanding methods can be turned on or off through configuration settings. These include active reactive pulse, frequency shift, frequency drift and passive checks. Some manufacturers allow only qualified personnel to disable anti-islanding, while Solis inverters ship with it enabled and it cannot be disabled. Anti-islanding protection comes built in on Fronius Symo inverters, so if it is found disabled, look first at the setup configuration.

<!-- review notes
- sentence 1: support check: partial - Code 581 and SPUI setup activation are stated, but the evidence doesn't say it's shown on the display of a Symo specifically (state code row only).
- sentence 3: support check: partial - Not an error and Enter confirmation are stated, but the advice to check the islanding deactivation was intended for the site is not in the passage.
- sentence 4: support check: partial - Code 456 described as anti-islanding function stopped running properly, but the passages don't name Fronius or state it's a malfunction versus a deliberate setting (only implied).
- sentence 7: support check: partial - Integrated anti-islanding protection and the 581 SPUI deactivation are in the passages, but the passages don't state the troubleshooting advice to look first at the setup configuration.
- sentence 7: review: partial - The passages show that islanding protection is integrated on the Symo and that the SPUI setup (581) turns it off, but the advice to look first at the setup configuration is an inference that is not stated.
-->
