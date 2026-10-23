---
id: symptom:user-power-limit
type: Symptom
name: User-set power limitation
aliases:
- LIMxxx% CODE:00
- Power limitation
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On ABB/FIMER inverters the display shows LIMxxx% CODE:00, where xxx is the power reduction percentage.
    On TRIO units it appears with display symbol b6.
  quote: The message indicates that the user has set an output power limitation for the inverter.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r1
    h: ae71d9db84fd
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r1
    h: e437ee039933
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r1
    h: fb1bdd0da281
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r1
    h: fb1bdd0da281
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42
    h: 57382cfeaa0d
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:flat-output-below-available-power
  note: AC output is held at the user-set percentage of nominal output power. LIM 100% means no limitation
    and LIM 50% means a limit of half the nominal output.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=51.r1
    h: ae71d9db84fd
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=42.r1
    h: e437ee039933
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=58.r1
    h: fb1bdd0da281
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r1
    h: fb1bdd0da281
  review: drafted
  review_note: 'support check: partial - Passages give the user-set limit and LIM percentage meanings,
    but say nothing about AC power staying flat while irradiance would support more, or about model_103.W
    and POAI behaviour.'
---
The inverter display shows LIMxxx% CODE:00. This means a user has set an output power limit on the inverter, and xxx is the power reduction percentage. LIM 100% means there is no limit. LIM 50% means output is capped at half of the nominal output power, so monitoring shows AC power flattened at that level. This is a configuration state, not a hardware fault. The fix is to check the limit value under Settings > Power Reduction, or under Settings > Power Limitation on TRIO units. Do not confuse it with the other limitation codes. CODE:01 is over-frequency derating, CODE:02 is the ten-minute average grid overvoltage derating, CODE:03 is an anti-islanding limit and CODE:04 is a limit caused by low grid voltage. The inverter can also reduce its own power because of high temperature, high input voltage or high input current. Those cases do not come from a percentage set by the user.

<!-- review notes
- sentence 2: support check: partial - LIM 100% meaning no limit and LIM 50% meaning half of nominal output are stated, but the passages never say that monitoring shows AC power flattened at that level.
- sentence 3: support check: partial - The user-set limit and the check of Settings > Power Reduction (or Power Limitation on the b6 rows) are stated, but 'not a hardware fault' is not explicitly stated, and the TRIO attribution is only implied by the b6 symbol.
- sentence 5: support check: partial - Passages list thermal, high input voltage and high input current as causes of power limiting, and separate them from the user-set percentage, but they do not explicitly say those cases do not come from a user-set percentage.
-->
