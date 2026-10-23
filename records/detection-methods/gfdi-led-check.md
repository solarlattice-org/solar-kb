---
id: method:gfdi-led-check
type: DetectionMethod
name: GFDI indicator LED check
aliases:
- GFI led
claims:
- claim_id: c1
  rel: produces
  target: meas:inverter-fault-indicator
  note: 'The GFDI or GFI LED lights when the inverter has detected a ground fault or a blown ground fuse.
    Colour depends on the make: red on some (FIMER, Enphase, SMA), yellow on others (Yaskawa SGI).'
  cite:
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24.r2
    h: fb859c54d997
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=24
    h: abb49edd4919
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: tbl=4.r4
    h: 4e8c7635e6a3
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=h80
    h: 29c1a7cb0737
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=h131
    h: c4fb058ff9af
  - src: src:enphase-enphase-m190-m210-installation-and-operation-guide
    loc: sec=h33
    h: 473b062a177d
  - src: src:sma-doc-hf-ixx105020
    loc: tbl=12.r1
    h: 2f4a72fa8500
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=46.r2
    h: 5ef23892e8c1
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
  review_note: 'support check: partial - Passages show red LEDs (FIMER, Enphase, SMA) and yellow (a ground
    fault LED) for ground fault, but Yaskawa SGI is not named and ''blown ground fuse'' is only implied
    by SMA fuse fault.'
- claim_id: c2
  rel: produces
  target: meas:inverter-fault-code-display
  note: Alongside the LED, the display may show a ground fuse or GFDI trip message, for example event
    35 on SMA units or error 3502 on Sunny Central.
  cite:
  - src: src:sma-doc-hf-ixx105020
    loc: tbl=12.r1
    h: 2f4a72fa8500
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: tbl=4.r4
    h: 4e8c7635e6a3
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r2
    h: c8d350ec3a48
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
This check means looking at the ground fault indicator LED on the inverter or on its GFDI device to see whether the ground fault protection has tripped. If the GFDI LED is lit after a grounding fault alarm, the ground fuse has failed and should be replaced with a new one. A lit GFI LED means a ground fault was detected on the DC side of the PV array, and the inverter disconnects from the grid until the fault is cleared. LED colour varies by make: some inverters use a solid red LED, often together with a ground fuse message on the display, while others use yellow ground fault LEDs fitted in pairs so one still works if the other fails. After a GFDI trip, check the PV array for ground faults. Once the cause is fixed, the fault may need to be reset by hand. On some central inverters, the GFDI function and its signalling can be tested with the inverter switched off, by switching the GFDI breaker off and on and confirming the failure message appears and then clears. Replace the GFDI if it fails its mechanical or optical check, and in any case after at least 100 ground faults that tripped it. An indicator that is off does not prove the circuit is dead, because voltage may still be present in DC circuits, so follow electrical safety precautions.

<!-- review notes
- sentence 1: support check: partial - Passages show GFI/GFDI LEDs indicate ground fault detection, but nothing explicitly defines the check as looking at the LED to see whether protection tripped.
- sentence 2: support check: partial - Passage says if the GFDI LED is on, replace with a new fuse, but doesn't state the fuse has failed, only implied; also tied to GFDIErr alarm.
- sentence 6: support check: partial - Passage describes switching F71 off/on with inverter deactivated and failure 201 appearing/confirmed, but doesn't say F71 is a GFDI breaker or 'central inverters' explicitly (Sunny Central implied).
-->
