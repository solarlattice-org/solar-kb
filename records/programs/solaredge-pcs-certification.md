---
id: prog:solaredge-pcs-certification
type: Program
name: SolarEdge PCS Certification NA
aliases:
- PCS certification
category: Certification
program_kind: certification
claims:
- claim_id: c1
  rel: issued_by
  target: org:solaredge
  cite:
  - src: src:se-academy-solaredge-pcs-certification-na-technical
    loc: sec=h1
    h: 8b8f15e4880e
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - The passage is a SolarEdge course that grants certification,
    but it never explicitly says SolarEdge issues it, though that is strongly implied.'
- claim_id: c2
  rel: part_of
  target: prog:solaredge-academy
  note: Delivered as a course on the SolarEdge Academy learning site.
  cite:
  - src: src:se-academy-solaredge-pcs-certification-na-technical
    loc: sec=h1
    h: 8b8f15e4880e
  - src: src:se-academy-solaredge-pcs-certification-na-technical
    loc: sec=front
    h: '5e5743107686'
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:solaredge-nexis
  note: Includes a SolarEdge Nexis PCS training module on busbar overload control (BBoC).
  cite:
  - src: src:se-academy-solaredge-pcs-certification-na-technical
    loc: sec=h2
    h: 93b217f20ad9
  - src: src:se-academy-solaredge-pcs-certification-na-technical-02-solaredge-nexis-pcs-training
    loc: sec=h5
    h: 85575254651c
  review: drafted
---
SolarEdge runs this certification course to teach installers how to install and commission sites that use SolarEdge Power Control Systems (PCS). To earn the certification and the right to install SolarEdge PCS, you have to finish the training and pass the certification exam. The course has a PCS certification overview, a SolarEdge Nexis PCS training module and a final PCS certification exam. The Nexis module explains PCS busbar overload control (BBoC), where to install the CTs, how to enable PCS with a meter, and why BBoC matters. BBoC keeps busbar current within its rating by using CTs to measure both the inverter output and the grid current flowing onto the busbar. The training reminds technicians to treat conductors as energized until tested, to wear proper PPE, and to follow NEC, local AHJ and OSHA rules. The course is offered in English on the SolarEdge Academy site under course code 015-EX-ENNAM-COMM-PCS-NA.

<!-- review notes
- sentence 4: support check: partial - The summary and outline list what BBoC is, where to install CTs, enabling PCS and why BBoC matters. Enabling with a meter appears only in the outline, and the passages don't tie these topics to the Nexis module specifically.
-->
