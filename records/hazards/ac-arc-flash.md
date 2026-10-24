---
id: hazard:ac-arc-flash
type: Hazard
name: AC arc flash
aliases:
- arc flash
- arc blast
- arcing fault
- electric arc
category: Electrical
claims:
- claim_id: c1
  rel: controlled_by
  target: tool:arc-rated-clothing
  note: Described as the most common industry-accepted PPE for body protection from arc flash; PPE aims
    to limit burns to a curable level.
  cite:
  - src: src:book-practical-solution-guide-to-arc-flash-hazards-2nd-ed
    loc: sec=h80
    h: 032cb724d40d
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: proc:isolate-upstream-ac-sources
  scope:
    products:
    - prod:tesla-megapack-2
    - prod:tesla-megapack-2-xl
  conditions: Required when working in the AC bus bar area or when labeled incident energy exceeds the
    maximum allowed.
  cite:
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: sec=7.2.1
    h: ec9f38e26739
  - src: src:tesla-megapack-2-xl-operation-and-maintenance-manual-v1-1
    loc: sec=6.2.2.1
    h: 77a5ab8d9ea1
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:arc-flash-labeling
  note: Labels state expected incident energy and recommended PPE.
  cite:
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: sec=7.2.1
    h: ec9f38e26739
  - src: src:tesla-megapack-2-xl-operation-and-maintenance-manual-v1-1
    loc: sec=6.2.2.1
    h: 77a5ab8d9ea1
  - src: src:book-practical-solution-guide-to-arc-flash-hazards
    loc: sec=1.10
    h: a08623843178
  review: drafted
- claim_id: c4
  rel: controlled_by
  target: proc:arc-flash-hazard-assessment
  note: A qualified person calculates the flash protection boundary, incident energy and hazard/risk category
    from power system data.
  cite:
  - src: src:book-practical-solution-guide-to-arc-flash-hazards
    loc: sec=1.10
    h: a08623843178
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: mit:current-limiting-devices
  cite:
  - src: src:book-practical-solution-guide-to-arc-flash-hazards
    loc: sec=1.10
    h: a08623843178
  review: drafted
- claim_id: c6
  rel: controlled_by
  target: mit:safety-isolation
  scope:
    products:
    - prod:generac-pwrmicro
  note: Open PV breakers and render equipment inoperable before servicing; never unplug AC or DC connectors
    under load.
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: sec=h23
    h: 8c250461e617
  review: drafted
---
The arc gives off intense heat, sound and pressure waves. It can set clothing on fire and cause severe or fatal burns. The risk comes up when work is done on exposed live parts, for example in panel boards and in the AC bus bar area of battery storage enclosures. AC arc flash is better understood than DC arc flash, and its industry calculation methods are backed by many equipment tests. Before work, check the arc flash label for the expected incident energy and the recommended PPE. On Megapack units, isolate them from upstream AC sources when working in the AC bus bar area or when the incident energy is above the allowed maximum. Never unplug connectors under load. Open the breakers and make the equipment inoperable before servicing. Lower the risk by following procedures, using the right tools, keeping up preventive maintenance and planning the work. Wear arc-rated clothing in case an arc still happens.

<!-- review notes
- sentence 2: support check: partial - Exposed live parts work and the AC bus bar area isolation requirement are stated, but panel boards are only shown in a figure caption and 'battery storage enclosures' is not stated as such.
- sentence 6: support check: partial - Risk reduction measures are stated, and arc-rated clothing is the common PPE, but the passages do not explicitly say to wear arc-rated clothing in case an arc still occurs.
-->
