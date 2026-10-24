---
id: prog:sma-om-services
type: Program
name: SMA Operations & Maintenance Services
aliases:
- SMA O&M services
- SMA Service
category: Service
program_kind: service
claims:
- claim_id: c1
  rel: issued_by
  target: org:sma
  cite:
  - src: src:sma-doc-tou-mysma-stou-services-202107-en-10
    loc: sec=h21
    h: 1b2ba25bde90
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: sec=11.2.3
    h: 12afbb4cc7ac
  review: drafted
  review_note: 'support check: partial - Passages show SMA runs service and a service-work maintenance
    plan, but nothing names a document or offering ''SMA Operations & Maintenance Services'' or states
    it is issued by SMA explicitly.'
- claim_id: c2
  rel: applies_to
  target: prod:sma-sunny-central-up-us
  note: The servicing schedule for service work in the Sunny Central UP-US manual must be carried out
    by SMA Service.
  cite:
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: sec=11.2.3
    h: 12afbb4cc7ac
  review: drafted
  review_note: 'support check: partial - The passage says the servicing schedule must be done by SMA Service,
    but does not name the Sunny Central UP-US or an O&M services offering.; review: partial - The passage,
    from the SC-UP-US manual, says the servicing schedule must be carried out by SMA Service, but it never
    names an Operations & Maintenance Services program or links one to this product.'
- claim_id: c3
  rel: applies_to
  target: region:fr
  note: SMA France S.A.S. in Lyon is listed as the service contact, with the Online Service Center.
  cite:
  - src: src:sma-doc-240154
    loc: tbl=95.r1
    h: 5d68b4328d11
  review: drafted
- claim_id: c4
  rel: applies_to
  target: region:gr
  note: An SMA service partner in Athens is listed as the service contact.
  cite:
  - src: src:sma-doc-240154
    loc: tbl=95.r1
    h: 5d68b4328d11
  review: drafted
- claim_id: c5
  rel: applies_to
  target: region:cy
  note: An SMA service partner in Athens is listed as the service contact for Cyprus.
  cite:
  - src: src:sma-doc-240154
    loc: tbl=95.r1
    h: 5d68b4328d11
  review: drafted
---
SMA provides service for its products through SMA Service, and SMA can have warranty services carried out by authorized partners. For the Sunny Central UP-US central inverter, the activities in the service-work maintenance plan must be done by SMA Service, either as needed or at the stated intervals. Service events are entered and tracked in the SMA Online Service Center, which also gives access to registered Sunny Portal systems and the SMA Service knowledge base. Only users registered as installers can order replacement service and request service compensation in the Online Service Center. To use the Online Service Center, create an SMA ID company account. The first person to register a company becomes its administrator, and anyone who registers later sends a membership request to that administrator. Service hardware may only be fitted by trained qualified persons. Fee-based services come under separate sales conditions that are shown when you order. In other countries, contact the international SMA Service Line or use the Online Service Center.

<!-- review notes
- sentence 2: support check: partial - The passage states the SMA Service and as-needed/interval requirement, but the product (Sunny Central UP-US) is not named in the passage text itself, only implied by the section.
- sentence 1: review: partial - The authorized-partner part is supported, but the cited passage only says SMA Service must do the maintenance-plan work for one product, not that SMA services all its products through SMA Service.
-->
