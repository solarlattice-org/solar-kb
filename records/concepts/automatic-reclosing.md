---
id: concept:automatic-reclosing
type: Concept
name: Automatic reclosing
aliases:
- recloser
- reclosing coordination
- reclosing
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:cease-to-energize
  note: The DER must cease to energize before reclosure; momentary cessation meets this.
  cite:
  - src: src:std-standards-ieee-ieee1547
    loc: sec=4.2.2
    h: f1f82d1a89f7
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=6.3
    h: 2df1cc34a51e
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:islanding
  note: If PV remains online in an island when reclosing occurs, it may be out of synchronism with the
    utility.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=2.5.6
    h: b4bdbb219779
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.7
    h: 7166bd75e175
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: tbl=22.r7
    h: 8a904c32bc4b
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:anti-islanding
  note: Reliance on islanding detection is one accepted means of ceasing energization before reclosing.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=6.3
    h: 2df1cc34a51e
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=2.5.6
    h: b4bdbb219779
  review: drafted
- claim_id: c4
  rel: related_to
  target: mit:direct-transfer-trip
  note: Transfer trip is listed as a means to cease DER energization when the Area EPS is isolated.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=6.3
    h: 2df1cc34a51e
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:area-eps
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=6.3
    h: 2df1cc34a51e
  - src: src:std-standards-ieee-ieee1547
    loc: sec=4.2.2
    h: f1f82d1a89f7
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c6
  rel: related_to
  target: concept:ansi-device-numbers
  note: Device number 79 is the AC reclosing relay.
  cite:
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: tbl=80.r1
    h: 8277956ab03b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: related_to
  target: comp:ac-circuit-breaker
  note: Reclosers act like circuit breakers with built-in relaying; breakers can also be used for reclosing
    duty.
  cite:
  - src: src:book-electric-power-system-basics
    loc: sec=h127
    h: 3645cfe30046
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: tbl=80.r1
    h: 8277956ab03b
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h90
    h: 2260410822cb
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:scada
  note: Automatic reclosing may be disabled through SCADA during work on energized lines, with tagging
    or display requirements.
  cite:
  - src: src:std-standards-nesc-2017-nesc
    loc: sec=h476
    h: a333f906925b
  review: drafted
---
Automatic reclosing means a breaker or recloser closes again on its own a limited number of times after a fault trip, so the faulted section gets power back. When the fault was temporary, service comes back with no further action. When the fault is still there, the device trips again, and after its set number of attempts it locks out until someone resets it by hand. Common sequences use 1, 2 or 3 reclosing attempts. On distribution circuits, the open time between attempts is usually set somewhere from about 0.2 s to 30 s. If reclosing happens too fast, a PV inverter may still be running in an island and may have lost synchronism with the grid. Closing out of synchronism counts as a fault and can trip the breaker or damage equipment. A strict reading of IEEE 1547 means PV must disconnect faster than 2 s when the utility recloses in less than 2 s. Utilities can also lengthen the reclose delay, or add voltage sensing or sync-check relaying so the line recloses only when the PV side is de-energized. An inverter that rides through a fault on a nearby section will see a series of voltage dips, one for each reclose attempt. This is why consecutive-disturbance ride-through matters.

<!-- review notes
- sentence 7: support check: partial - Passages support a series of disturbances on each reclosure and the DER ride-through requirement, but do not name 'consecutive-disturbance ride-through' as the reason beyond the figure titles; also one dip per attempt applies for a persistent fault.
-->
