---
id: prog:enphase-rma
type: Program
name: Enphase RMA
aliases:
- return merchandise authorization
- Enphase RMA process
- RMA
- Return Merchandise Authorization Number
category: Service
program_kind: service
claims:
- claim_id: c1
  rel: issued_by
  target: org:enphase
  cite:
  - src: src:enphase-enphase-m190-m210-installation-and-operation-guide
    loc: sec=h43
    h: b9c9bf823d6b
  - src: src:kb-enphase-enphase-service-manager-managing-rma-s-and-labor-reimbursement-requests-with-th
    loc: sec=front
    h: ac434d53eb0d
  review: drafted
- claim_id: c2
  rel: part_of
  target: prog:enphase-limited-warranty
  note: The limited warranty says defective product must be returned under an RMA number requested from
    Enphase.
  cite:
  - src: src:enphase-enphase-m190-m210-installation-and-operation-guide
    loc: sec=h43
    h: b9c9bf823d6b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: applies_to
  target: prod:enphase-iq-battery
  note: The Enphase Storage troubleshooting guide and the Service Manager RMA article both cover RMA requests
    for IQ Battery hardware.
  cite:
  - src: src:kb-enphase-enphase-service-manager-managing-rma-s-and-labor-reimbursement-requests-with-th
    loc: sec=front
    h: ac434d53eb0d
  - src: src:enphase-enphase-storage-3-3t-10-10t-troubleshooting-guide
    loc: sec=h69
    h: 5e1fdc1aaaa3
  review: drafted
  review_note: 'support check: partial - The Service Manager article lists IQ Battery models, and the
    RMA text covers ''hardware''. Neither names the Enphase Storage troubleshooting guide, and the RMA
    text doesn''t say it is about the IQ Battery.'
- claim_id: c4
  rel: applies_to
  target: prod:enphase-iq8
  note: The Service Manager article on RMA and labor reimbursement lists IQ8 microinverter models.
  cite:
  - src: src:kb-enphase-enphase-service-manager-managing-rma-s-and-labor-reimbursement-requests-with-th
    loc: sec=front
    h: ac434d53eb0d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Enphase runs a Return Merchandise Authorization (RMA) process for returning defective Enphase hardware for repair or replacement under its limited warranty. Installers can submit an RMA request only after all appropriate troubleshooting has been done without fixing the problem, and Enphase recommends working through the fault with Enphase technical support while the unit is still in the field. You can submit RMA requests in the Enphase Installer App or in the Enphase Service Manager, and the Service Manager also handles labor reimbursement requests. Include full troubleshooting details: the steps you performed, the voltages you measured and photos of the test locations. Enphase denies RMA requests with missing or incomplete steps. The limited warranty terms also require proof of purchase, the model and serial number, a detailed description of the defect and a shipping address for the replacement. Return the defective unit in its original packaging or equally protective packaging, and do not open or modify it without written approval from Enphase.

<!-- review notes
- sentence 3: support check: partial - The headings show RMA requests can be made in the Installer App and the Service Manager, and the Service Manager article title mentions labor reimbursement requests. The passages don't say the Service Manager 'handles' labor reimbursement, only that its article covers managing them.
-->
