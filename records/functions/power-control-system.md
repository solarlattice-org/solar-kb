---
id: func:power-control-system
type: Function
name: Power control system
aliases:
- PCS
- UL 1741 PCS
- UL 3141 PCS
- power control systems
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: requires
  target: role:qualified-person
  note: Only qualified people may commission the PCS or set or change its maximum operating current; Generac
    commissioning also needs a password.
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h88
    h: 6d1cda0ffb8e
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: sec=2.3.8.6
    h: 13f07c533fa9
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: sec=2.2.8.6
    h: b4abbda45b6c
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: requires
  target: func:export-limitation
  scope:
    products:
    - prod:generac-pwrcell-2
  note: Power Export Limit (PEL) is one of the PCS functions on Generac PWRcell 2, alongside busbar and
    feeder conductor overload control.
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: sec=h88
    h: 6d1cda0ffb8e
  review: drafted
- claim_id: c3
  attr: response_time
  value:
    nominal: 1.95
    unit: unit:SEC
  scope:
    products:
    - prod:solis-s6-eh1p-h-us
  conditions: Measured open-loop response time of the PCS on the Solis S6-EH1P hybrid inverter
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: sec=4.5.2
    h: bb84389b07e7
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: response_time
  value:
    nominal: 4.2
    unit: unit:SEC
  scope:
    products:
    - prod:solis-s6-eh1p-h-us
  conditions: Longest steady-state time of the PCS on the Solis S6-EH1P hybrid inverter
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: sec=4.5.2
    h: bb84389b07e7
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions)
---
A power control system (PCS) regulates current so that busbars and conductors are not loaded beyond their ratings, which can be lower than the sum of all connected sources. With a certified PCS, the busbar can be loaded up to its full rating instead of following the 120% breaker sizing rule, and the PCS current settings can be used for NEC Article 690 and 705 design current calculations. PCS-controlled busbars and conductors still need properly rated overcurrent devices, and the maximum PCS current setting must never exceed the busbar rating or conductor ampacity. Generac PWRcell 2 is certified to UL 3141 and listed to the UL 1741 PCS CRD. Its PCS functions are Power Export Limit, Busbar Overload Control and Feeder Conductor Overload Control, and they are set during password-protected commissioning by a qualified person.
