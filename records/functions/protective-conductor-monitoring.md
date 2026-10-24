---
id: func:protective-conductor-monitoring
type: Function
name: Protective conductor monitoring
aliases:
- PE monitoring
- grounding conductor monitoring
- protective conductor monitor
category: Protection
function_kind: protection
claims:
- claim_id: c1
  rel: requires
  target: role:utility-approval
  note: SMA says the protective conductor monitor may be switched off on any grid type to avoid false
    triggering from grid problems, but only after talking to the local grid operator.
  cite:
  - src: src:sma-kb-event-9-or-901
    loc: sec=h1
    h: a4c82face2c9
  review: drafted
  review_note: 'support check: partial - The passage says monitoring can be deactivated after consulting
    the local grid operator, but nothing says it requires a utility approver role; that role requirement
    is not stated.'
---
Protective conductor monitoring is an inverter protection function. It detects when the grounding (PE) conductor is missing or wired incorrectly, and when that happens it disconnects the inverter from the utility grid. On SMA inverters this condition shows up as event 9 or event 901. To troubleshoot, inspect all of the AC cabling, especially N and PE. Look for loose terminals and confirm the conductors are landed on the correct terminals. Measure the N-PE voltage at the inverter and at the sub-distribution. It must be below 0.3 V on TN-C grids and below 30 V on TT grids. On other grid types it can also be deactivated to stop false trips, but only after consulting the local grid operator. A second protective conductor may then be needed as well. During SMA commissioning, check that the grounding conductor is connected to ground, for example at a grounding busbar or a foundation ground electrode. On TN systems, also measure to confirm a conductive connection between neutral and the grounding conductor. If the event keeps appearing after the AC installation has been checked, contact SMA Service. Have ready the device type and serial number, the grid type, the N-PE readings, and whether the monitoring is switched on or off.
