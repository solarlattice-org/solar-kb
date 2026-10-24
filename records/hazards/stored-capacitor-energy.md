---
id: hazard:stored-capacitor-energy
type: Hazard
name: Stored energy in capacitors
aliases:
- DC-link capacitor discharge
- discharge wait time
- intermediate circuit capacitors
- DC bus capacitors
- Delay discharge
- internal capacitors
category: Electrical
claims:
- claim_id: c1
  rel: subclass_of
  target: hazard:electric-shock
  note: Capacitors in inverters can still hold a shock hazard after every supply source has been disconnected.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: sec=h21
    h: 65305ae518d2
  - src: src:yaskawa-solectria-dsp-yellowstone
    loc: sec=h23
    h: 94ac31790aea
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h88
    h: 478038ee477d
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=8.r3
    h: f02f0ce7d1ac
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:capacitor-discharge-wait
  note: Yaskawa-Solectria says to wait at least 5 minutes after removing all AC and DC sources before
    working on its equipment.
  cite:
  - src: src:yaskawa-solectria-dsp-yellowstone
    loc: sec=h23
    h: 94ac31790aea
  - src: src:yaskawa-solectria-power-supply-board
    loc: sec=h23
    h: 94ac31790aea
  - src: src:yaskawa-solectria-yaskawa-customer-facing-instructions-full
    loc: sec=h96
    h: 2e637a310625
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:capacitor-discharge-wait
  scope:
    products:
    - prod:chint-sch-350ktl
  note: Keep the cover on until 5 minutes after all supply sources are disconnected.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: sec=h21
    h: 65305ae518d2
  review: drafted
- claim_id: c4
  rel: controlled_by
  target: mit:capacitor-discharge-wait
  scope:
    products:
    - prod:huawei-sun2000-25-30ktl-us
  note: A delay-discharge label calls for a 5-minute wait after disconnecting all power before removing
    the cover.
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=8.r3
    h: f02f0ce7d1ac
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: mit:capacitor-discharge-wait
  scope:
    products:
    - prod:sma-sunny-island-us
  note: Wait 15 minutes before opening the unit so its capacitors can discharge.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h88
    h: 478038ee477d
  review: drafted
- claim_id: c6
  rel: controlled_by
  target: mit:capacitor-discharge-wait
  scope:
    products:
    - prod:abb-pvs-60-tl-us
    - prod:abb-uno-dm-6-0-plus-us
    - prod:abb-pvs-166-175-tl-us
    - prod:abb-uno-dm-3-3-5-0-plus-us
  note: Wait until the internal capacitors have discharged. The regulatory label gives the discharge time.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=8
    h: a2de404e05ec
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: sec=h200
    h: a2de404e05ec
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=10
    h: 518b45241c37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: sec=h206
    h: a2de404e05ec
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=8.2.4.8
    h: 5add25577173
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c7
  rel: controlled_by
  target: mit:observe-safety-labels
  scope:
    products:
    - prod:abb-pvs-60-tl-us
    - prod:abb-uno-dm-6-0-plus-us
    - prod:abb-pvs-166-175-tl-us
    - prod:abb-uno-dm-3-3-5-0-plus-us
  note: The regulatory label shows how long the stored energy takes to discharge.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=8
    h: a2de404e05ec
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: sec=h200
    h: a2de404e05ec
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=10
    h: 518b45241c37
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: sec=h206
    h: a2de404e05ec
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=8.2.4.8
    h: 5add25577173
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Passages say regulatory label indicates discharge time, but don''t
    frame it as a general observe-safety-labels control; core is present.'
---
Inverter capacitors can still hold a dangerous charge after the AC and DC sources have been disconnected, so touching internal parts can cause a life-threatening electric shock. PV modules in sunlight charge the inverter's DC bus capacitors, and that charge stays in the capacitors after the PV input is switched off. The danger applies to string inverters, central and battery inverters, and the manufacturers put warning labels on the equipment. The main control is a discharge wait after all sources are disconnected and before the cover is removed. This is 5 minutes for several string inverters and Yaskawa-Solectria equipment, and 15 minutes for the Sunny Island. Some older CPS central inverters need 60 minutes after all inputs are cut off, or a successful De-energy command, before maintenance. On FIMER inverters, check the regulatory label for the discharge time and wait until the internal capacitors have discharged.

<!-- review notes
- sentence 3: support check: partial - Warning labels exist and Sunny Island/Yaskawa equipment are mentioned, but the passages don't explicitly categorize string, central and battery inverters.
- sentence 5: support check: partial - 60 minutes or De-energy command is stated for CPS, but 'older' and 'central' inverters are not mentioned.
- sentence 6: support check: partial - Passages give the label/wait instructions but do not name FIMER.
- sentence 4: review: partial - The 5-minute waits (CPS, Huawei, Yaskawa-Solectria) and the 15-minute Sunny Island wait before opening are supported, but no passage calls the CPS/Huawei units 'string inverters'.
-->
