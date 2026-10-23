---
id: symptom:battery-charge-overcurrent
type: Symptom
name: Excessive battery charging current
aliases:
- battery charging current too high
- XA08DcHiCur
- XA09DcHiChgCur
- XW08DcHiCur
claims:
- claim_id: c1
  rel: observed_as
  target: meas:bms-error-message
  note: 'Sunny Island reports this through SiCom messages from the external battery management system:
    F927 and F928 are level 3 errors, and W943 and W944 are level 1 warnings. F928 and W944 refer specifically
    to charge mode.'
  quote: 'Error message via SiCom: battery charging current too high'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r10
    h: 46116b699209
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r11
    h: 31317c5d1763
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r9
    h: 155b307f1d8b
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r10
    h: be5d14ac6c9b
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155
    h: 9ec13aab83bd
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=84.r3
    h: 406f77ce8e3d
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=83.r2
    h: 97d2709e5a7c
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=83.r1
    h: 462f224eee0f
  review: drafted
---
The Sunny Island battery inverter shows this condition when the external battery management system reports over SiCom that the battery charging current is too high. F927 and F928 are level 3 error messages, and W943 and W944 are level 1 warnings. F928 and W944 cover the case where the current is too high in charge mode. The manual's fix is to remove the cause in the external battery management system, following the battery manufacturer's documentation. Check the charging limits first. The maximum battery charging current is set by BatChrgCurMax, which should match the battery manufacturer's value. Charging current is also capped by GdCurNom and GnCurNom (nominal currents of the external energy sources) and by InvChrgCurMax (maximum AC charging current). If the battery current sensor was reinstalled, recalibrate it with BatCurAutoCal so the maximum charging current is calculated correctly. When reading sensor data, note that the measured battery current is negative while the battery is charging.

<!-- review notes
- sentence 4: support check: partial - The parameters and their limiting roles are stated, but nothing says to check charging limits first as a fix for these codes, and GdCurNom and GnCurNom are described as nominal currents of the external energy sources.
-->
