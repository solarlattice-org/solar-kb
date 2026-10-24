---
id: prog:sma-service-rebate
type: Program
name: SMA Service Rebate
aliases:
- Service Rebate
- Service Call Rebate
category: Service
program_kind: service
claims:
- claim_id: c1
  rel: issued_by
  target: org:sma
  cite:
  - src: src:sma-kb-requesting-service-rebate
    loc: sec=h1
    h: bdf59476917b
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
- claim_id: c2
  rel: applies_to
  target: region:us
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
- claim_id: c3
  rel: applies_to
  target: region:pr
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
- claim_id: c4
  rel: applies_to
  target: region:ca
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
- claim_id: c5
  rel: applies_to
  target: region:au
  note: Separate Australian claim procedure; requires a case number and a warranty case.
  cite:
  - src: src:sma-kb-requesting-a-sma-service-rebate-au-only
    loc: sec=h1
    h: 4f56144a2627
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-ev-charger
  note: Rebate is provided for exchanging the EV Charger.
  cite:
  - src: src:sma-kb-is-there-a-sma-service-rebate-for-the-ev-charger
    loc: sec=h1
    h: 4894dec4ba6f
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-sunny-boy
  scope:
    regions:
    - region:us
    - region:pr
    - region:ca
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sma-sunny-boy-240
  scope:
    regions:
    - region:us
    - region:pr
    - region:ca
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
  review_note: 'support check: partial - Sunny Boy Micro (SB240) and Multi-gate units are listed, but
    the Sunny Boy 240 and Sunny Multigate product is only loosely matched.'
- claim_id: c9
  rel: applies_to
  target: prod:sma-inverter-manager
  scope:
    regions:
    - region:us
    - region:pr
    - region:ca
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:jms-f-rapid-shutdown-device
  scope:
    regions:
    - region:us
    - region:pr
    - region:ca
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:sma-sunny-tripower
  scope:
    regions:
    - region:us
    - region:pr
    - region:ca
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
- claim_id: c12
  rel: applies_to
  target: prod:sma-stp-core1-us
  scope:
    regions:
    - region:us
    - region:pr
    - region:ca
  note: Covers full unit or board replacement per inverter.
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
  review_note: 'support check: partial - CORE1 gets $250 per full unit or board replacement, but ''Sunny
    Tripower CORE1-US'' and the US-specific naming are not stated.'
- claim_id: c13
  rel: applies_to
  target: prod:sma-shp-peak3
  scope:
    regions:
    - region:us
    - region:pr
    - region:ca
  note: Covers full unit or board replacement per inverter.
  cite:
  - src: src:sma-kb-sma-service-rebate-process-for-us-puerto-rico-and-canada-customers
    loc: sec=h1
    h: 56986eb9c2d5
  review: drafted
  review_note: 'support check: partial - PEAK3 gets $250 per full unit or board replacement, but the ''Sunny
    Highpower'' naming is not stated.'
---
The SMA Service Rebate pays installers who replace SMA inverters or swap boards at customer sites on SMA's behalf. The job must be a warranty case: the equipment must still be under SMA warranty and SMA must have authorized the replacement. To claim, order the replacement through the Online Service Center, then open that case, fill in the replacement report with the date, fix status and serial numbers, and upload your invoice. In the US, Puerto Rico and Canada, use an installer-level account, submit the request within 60 days of the RMA creation date, and address the invoice to SMA America, LLC. Labor costs are not covered. In Australia, payment usually arrives within 30 days. It can be delayed or rejected if the billing address or invoice format is wrong, the amount is over the allowed limit, or the defective unit is not returned. The European article lists a fixed 100 € for travel and setup plus 20 € for each inverter replaced. US rates start at $150 for the first Sunny Boy-class device and $250 for the first Sunny Tripower. Replacing an SMA EV Charger also qualifies for the rebate.
