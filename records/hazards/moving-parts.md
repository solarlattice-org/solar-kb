---
id: hazard:moving-parts
type: Hazard
name: Moving parts
aliases:
- pinch points
- tracker motion
- generator moving parts
- crush hazard
- movable generator parts
- suddenly moving parts
category: Mechanical
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:machine-guarding
  scope:
    standard: std:ieee-c2-2017
  note: Applies to equipment parts that move suddenly and are likely to injure people nearby. Pulleys,
    belts and mechanical transmission machinery are guarded per ANSI/ASME B15.1:2000.
  quote: shall be guarded or isolated
  quote_source: NESC 2017 (IEEE C2-2017) Rule 122
  cite:
  - src: src:std-standards-nesc-2017-nesc
    loc: sec=h122
    h: df36ed4c07e6
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:machine-guarding
  scope:
    standard: std:nfpa-70e-2009
  note: 'Rotating equipment: guards keep employees from contacting moving or energized parts.'
  quote: Guards, barriers, and access plates shall be maintained
  quote_source: NFPA 70E 2009 §230.2
  cite:
  - src: src:std-standards-nfpa-nfpa-70e-2009
    loc: sec=h87
    h: bedd40997f82
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:follow-manufacturer-instructions
  scope:
    products:
    - prod:sma-sunny-island
    - prod:sma-sunny-island-us
  note: Install, maintain and work on a generator that the Sunny Island can start automatically according
    to the generator manufacturer's specifications, and operate it only with its safety equipment.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h639
    h: ec8ac3b4a615
  - src: src:sma-doc-278742
    loc: sec=h42
    h: 54ea4526cfeb
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h50
    h: bbdc5c7e06ed
  - src: src:sma-doc-259761
    loc: sec=h577
    h: 721c02ab1605
  - src: src:sma-doc-259761
    loc: sec=h41
    h: 45d9fcfccc29
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: sec=h23
    h: 66759a18e49c
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: sec=h141
    h: 66759a18e49c
  review: drafted
- claim_id: c4
  rel: controlled_by
  target: mit:keep-clear-of-moving-parts
  scope:
    products:
    - prod:powin-stack750
  note: Applies when lifting and moving an HVAC-mounted frame during battery enclosure HVAC replacement.
  cite:
  - src: src:powin-wi-036-s750-hvac-replacement-rev-0
    loc: sec=h14
    h: 7057defeca3d
  review: drafted
---
Moving parts of machinery can crush or cut off body parts when a person is close to them while they move. In off-grid and backup systems, a Sunny Island can start a generator automatically, so the generator's moving parts can begin moving without warning. Run the generator only with its safety equipment, and install, maintain and service it according to the manufacturer's specifications. Tracking mounts add load-bearing moving parts, actuators and controls that need more maintenance than fixed arrays. The NESC requires parts that move suddenly and could injure people nearby to be guarded or isolated, and requires pulleys and belts to be guarded per ANSI/ASME B15.1. When you lift and move heavy frames, such as an HVAC-mounted frame on a battery enclosure, stay clear of the moving parts to avoid being crushed.

<!-- review notes
- sentence 1: support check: partial - Crush/sever from moving parts is stated, but not the generic 'machinery' or 'when close while they move' condition; examples are generator and HVAC frame.
- sentence 2: support check: partial - Auto-start by Sunny Island is stated, but 'off-grid and backup systems' and 'without warning' are not in the passages.
- sentence 6: support check: partial - Warning covers lifting and moving the HVAC-mounted frame and keeping clear, but 'heavy frames' generally and 'battery enclosure' are not stated.
-->
