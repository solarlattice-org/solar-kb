---
id: tool:thermal-imager
type: Tool
name: Thermal imaging camera
aliases:
- IR camera
- thermal imager
- infrared camera
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  attr: accuracy
  value:
    nominal: 2
    unit: unit:PERCENT
  conditions: Current industry standard accuracy for thermal imaging cameras, stated as ±2% or ±2 °C,
    whichever is bigger
  cite:
  - src: src:test-ir-thermography-t820264-en
    loc: sec=h41
    h: 56aff9d90d14
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c2
  attr: accuracy
  value:
    nominal: 2
    unit: unit:DEG_C
  conditions: Current industry standard accuracy for thermal imaging cameras, stated as ±2% or ±2 °C,
    whichever is bigger
  cite:
  - src: src:test-ir-thermography-t820264-en
    loc: sec=h41
    h: 56aff9d90d14
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c3
  attr: accuracy
  value:
    nominal: 1
    unit: unit:PERCENT
  conditions: More advanced FLIR Systems thermal imaging cameras, stated as ±1% or ±1 °C, whichever is
    bigger
  cite:
  - src: src:test-ir-thermography-t820264-en
    loc: sec=h41
    h: 56aff9d90d14
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'possible conflict with c1 (same source; check the conditions); review: the compiler-flagged
    conflict (tool:thermal-imager#c5) is a scenario difference, resolved at review'
- claim_id: c4
  attr: accuracy
  value:
    nominal: 1
    unit: unit:DEG_C
  conditions: More advanced FLIR Systems thermal imaging cameras, stated as ±1% or ±1 °C, whichever is
    bigger
  cite:
  - src: src:test-ir-thermography-t820264-en
    loc: sec=h41
    h: 56aff9d90d14
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c5
  attr: accuracy
  value:
    nominal: 2
    unit: unit:PERCENT
  conditions: Satir Hotfind camera (384x288 detector, 8 to 14 μm spectral range), as listed in an IEA
    PVPS review table
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: tbl=3.r9
    h: 1de39efc03f4
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'review: the compiler-flagged conflict (tool:thermal-imager#c3) is a scenario difference,
    resolved at review'
---
A thermal imaging camera picks up infrared radiation from a surface and turns it into a visible image. In a radiometric image, every pixel is a temperature reading. It measures without contact and shows the temperature across whole surfaces of electrical equipment, so it finds hot spots before failures or fires happen. Use it for infrared thermography of energized equipment under load. It can find high-resistance or corroded connections, overheated connectors, internal fuse damage, internal breaker faults and uneven load sharing. It scans whole components, which makes it less likely than a spot infrared thermometer to miss a critical problem. A reading can differ from the true temperature by the stated percentage or by the stated number of degrees, whichever is larger. The usual industry spec is plus or minus 2 percent or 2 degrees Celsius. To interpret images correctly you need to understand the physics and construction of the installation you are inspecting, so training is recommended. Analysis software is needed for spot and area temperature measurements, temperature difference checks, trending and inspection reports.

<!-- review notes
- sentence 3: support check: partial - Passages support inspections under load and the listed fault types (high-resistance, corroded, fuse, breaker, uneven load, overheated connector), but 'energized' and the term infrared thermography use are not exactly stated, and examples are for low voltage equipment.
- sentence 6: support check: partial - Passage says knowing the physics and construction is needed to interpret images and mentions training courses, but doesn't explicitly recommend training as the remedy.
- sentence 7: support check: partial - Passages say software is needed to analyze images and report, and list spot, area, difference, trending features in extensive packages, but basic software included with camera does basic analysis, so 'needed' for all these is overstated.
-->
