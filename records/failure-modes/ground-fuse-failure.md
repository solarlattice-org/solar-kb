---
id: fm:ground-fuse-failure
type: FailureMode
name: Grounding fuse failure
aliases:
- Fuse for solar module ground
- Ground Fuse flt
- negative grounding fuse
claims:
- claim_id: c1
  rel: affects
  target: comp:ground-fuse
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r4
    h: bfc22e660bc0
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=50.r3
    h: 70fd2314506c
  - src: src:sungrow-sungrow-sg3150ud-mv-us-sg4400ud-mv-us-user-manual-ver23
    loc: tbl=45.r4
    h: 5c09b5ed0638
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:inverter-shutdown
  note: 'Fronius Galvo status 472: the inverter stops feeding energy into the grid.'
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:ground-fault
  note: Ground fault protection (GFDI) faults list a blown negative grounding fuse as something to check.
  cite:
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24
    h: abb49edd4919
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24.r2
    h: fb859c54d997
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=50.r3
    h: 70fd2314506c
  - src: src:sungrow-sungrow-sg3150ud-mv-us-sg4400ud-mv-us-user-manual-ver23
    loc: tbl=45.r4
    h: 5c09b5ed0638
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:inverter-display-check
  note: Fronius Galvo status 551 shows a warning message on the display.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fuse-check
  note: Take out the negative grounding fuse and check whether it has blown.
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r4
    h: bfc22e660bc0
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=50.r3
    h: 70fd2314506c
  - src: src:sungrow-sungrow-sg3150ud-mv-us-sg4400ud-mv-us-user-manual-ver23
    loc: tbl=45.r4
    h: 5c09b5ed0638
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:gfdi-led-check
  note: If the LED on the GFDI is lit, replace the fuse.
  cite:
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24
    h: abb49edd4919
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24.r2
    h: fb859c54d997
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:ground-fuse-replacement
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24
    h: abb49edd4919
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24.r2
    h: fb859c54d997
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-installer
  note: Do this if the status code keeps coming back.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24
    h: abb49edd4919
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24.r2
    h: fb859c54d997
  review: drafted
  review_note: 'support check: partial - The GFDIErr row says to contact the after-sales service center,
    but it is a grounding fault entry and not clearly tied to a fuse failure.'
- claim_id: c10
  rel: mitigated_by
  target: mit:safety-isolation
  note: Wait until the capacitors have fully discharged before you remove the grounding fuse.
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r4
    h: bfc22e660bc0
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:ground-conductor-check
  note: Check that the inverter negative pole is securely grounded. For MV units, also check the transformer
    neutral point and the PT/CT neutral grounding.
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r4
    h: bfc22e660bc0
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=50.r3
    h: 70fd2314506c
  - src: src:sungrow-sungrow-sg3150ud-mv-us-sg4400ud-mv-us-user-manual-ver23
    loc: tbl=45.r4
    h: 5c09b5ed0638
  review: drafted
---
In this failure, the fuse that connects the PV array (solar module) to ground has blown or is faulty. Depending on the inverter, the inverter may stop feeding power into the grid, or it may only show a warning on its display. Ground fault protection alarms can also point to this fault, because a blown negative grounding fuse is one of the listed things to check. To confirm, let the capacitors discharge fully, take out the negative grounding fuse and check whether it has blown. On some units, a lit LED on the GFDI shows that the fuse needs replacing. Replace the ground fuse. Also check that the negative pole is securely grounded and, on medium-voltage units, that the transformer neutral is connected and grounded. If the fault keeps coming back, contact the system installer or the manufacturer's service team.

<!-- review notes
- sentence 1: support check: partial - The passages say the solar module ground fuse is defective, but not specifically that it connects the PV array to ground or that it has blown (blown is only to be checked).
- sentence 5: support check: partial - Replacing the fuse and checking the negative pole grounding are stated, but the transformer neutral is only to be checked after a blown fuse, and 'connected and grounded' is a loose paraphrase.
-->
