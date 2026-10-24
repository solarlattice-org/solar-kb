---
id: func:inertial-response
type: Function
name: Inertial response
aliases:
- synthetic inertia
- virtual inertia
- Virtual Machine
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: requires
  target: func:grid-forming
  scope:
    products:
    - prod:tesla-megapack-platform
  note: In the Tesla Megapack system the inertial response comes from the inverter-level Virtual Machine,
    which works within Grid-Forming mode.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.1.2.1
    h: 1c09f84c6b0e
  review: drafted
  review_note: 'support check: partial - Passage says the Virtual Machine gives the inertial response
    and is part of Grid-Forming mode, but doesn''t explicitly state inertial response requires grid forming.'
---
Inertial response is when a DER changes its active power output in proportion to the rate of change of frequency (ROCOF). In the past, grid inertia came from the rotating mass of large synchronous generators. Inverter-based resources have no rotating mass, but their power electronics can imitate inertia. IEEE 1547-2018 does not require inertial response but permits it, and lists it among the other allowed capabilities. The permission applies to both Category I and Category II DER under abnormal grid conditions. On Tesla Megapack systems, an inverter function called the Virtual Machine produces the inertial power response, reacting proportionally to ROCOF. Tesla's Grid-Forming mode combines this inverter-level inertial and droop response with the site-level frequency droop or voltage control response.

<!-- review notes
- sentence 5: support check: partial - Passage says the Tesla System achieves inertia via the Virtual Machine responding proportionally to ROCOF, but doesn't specify Megapack or call it an inverter function explicitly.
-->
