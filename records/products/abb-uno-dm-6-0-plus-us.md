---
id: prod:abb-uno-dm-6-0-plus-us
type: Product
name: UNO-DM-6.0-TL-PLUS-US string inverter
aliases:
- UNO-DM-6.0-TL-PLUS
- UNO-DM-6.0-TL-PLUS-US
category: Inverters
make: abb
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:abb
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: sec=h1
    h: 3c113dace49f
  review: drafted
  review_note: 'support check: partial - The manual passage shows ''ABB'' but doesn''t say it is the manufacturer
    (and ''ABB Ltd'' is not stated), though it is strongly implied by the branding.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Described as a string inverter.
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: sec=h7
    h: 5d9935bfac9d
  review: drafted
- claim_id: c3
  attr: rated_power
  value:
    nominal: 6
    unit: unit:KiloW
  conditions: Power class given in the product manual title
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: sec=h1
    h: 3c113dace49f
  review: drafted
---
The UNO-DM-6.0-TL-PLUS-US is a string inverter from ABB. Its product manual gives it a 6.0 kW power class. The manual has chapters on characteristics, safety and accident prevention, lifting and transport, installation, instruments, operation and maintenance. A later manual covers a variant called UNO-DM-6.0-TL-PLUS-US-QU.

<!-- review notes
- sentence 4: support check: partial - The passage names the -QU variant but does not say a later manual covers it.
-->
