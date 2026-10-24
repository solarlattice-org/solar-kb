---
id: state:emergency-charge
type: OperatingState
name: Emergency charge
aliases:
- force charge
- emergency charge mode
- EmCharge
- Emerg Charge
- emergency charge operation
category: Storage
claims:
- claim_id: c1
  rel: subclass_of
  target: state:battery-charging
  scope:
    products:
    - prod:sma-sunny-island-us
  note: Emergency charge mode charges a lead-acid battery from a generator connected to the Sunny Island
    while grid and generator management are inactive.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h606
    h: 2d28ef0c4071
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Emergency charge mode lets the battery inverter recharge a depleted battery from a generator, for example after the system has shut itself down automatically. You start it from the Quick Configuration Guide: select Emerg Charge, set the maximum external current to suit the generator, and confirm. Disconnect all loads first. Then either bridge AC1 to AC2 for a stationary generator or plug a portable generator straight into AC1. With the bridge in place, connect the generator before you start it so the magnetizing current does not trip the generator fuse. Battery management stays active and keeps using the current battery settings and charging phase. Generator management, grid management, reverse power protection and relay protection are all switched off, and voltage, current and frequency limits are not monitored. To pause the charge, for example to refuel the generator, press and hold the button. Press and hold it again to resume. While the mode is running, the operating state parameters of the master and slave units read EmCharge, and the event list shows display number E115 for emergency charge.

<!-- review notes
- sentence 6: support check: partial - Operating state parameters read EmCharge and E115 is Emergency charge, but E115 is only a display number description; the passages don't say it appears in the event list, and master state shows 'Run/EmCharge'.
-->
