---
id: state:equalization-charge
type: OperatingState
name: Equalization charge
aliases:
- equalizing charge
- equalization
- Equalize
category: Storage
claims:
- claim_id: c1
  rel: subclass_of
  target: state:battery-charging
  note: Equalize is listed as a value of the active battery charging process (BatChrgOp).
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=59.r8
    h: 5d5442a05b51
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=110.r8
    h: e0a3caa18621
  review: drafted
---
Equalization charge is a battery charging process that brings series-connected cells to a common, nearly full state of charge. Without regular equalization, cell charge levels slowly drift apart, which can weaken battery performance and cause early battery failure. The active charging process shows Equalize when this charge is running. The event log records a status change when the battery enters equalization charge. You can start a manual equalization charge, which runs only once and can be ended with Stop. With Idle, the device waits until the conditions for equalization are met. Automatic equalization charge is switched on or off under Battery > Charge, and its completion times, abort time for lithium-ion batteries and cycle time are set there. The generator request can be set to start the generator during equalization charge, or during both equalization and full charge. This is a normal maintenance state and needs no action unless you want to change its schedule or stop it.

<!-- review notes
- sentence 8: support check: partial - Passages describe equalization as beneficial and stoppable, but do not state it is a normal state needing no action.
-->
