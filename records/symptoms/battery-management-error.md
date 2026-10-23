---
id: symptom:battery-management-error
type: Symptom
name: Battery management system error
aliases:
- Internal error in battery management
- XA12Bms
- XW12Bms
claims:
- claim_id: c1
  rel: observed_as
  target: meas:bms-error-message
  note: Sunny Island shows F931 (XA12Bms, level 3 error) or W947 (XW12Bms, level 1 warning). Both report
    an internal battery-management error passed on over SiCom by the external battery management system.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r13
    h: ac2f10b48cae
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r14
    h: 5946dd290693
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=83.r5
    h: dc53936a955b
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=84.r7
    h: ba1081550807
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
The Sunny Island battery inverter reports an internal error in the battery management system as error F931 at level 3 or as warning W947 at level 1. The message does not come from the inverter itself: the external battery management system sends it over the SiCom link. The fix for both codes is to remove the cause inside the external battery management system, using the battery manufacturer's documentation. Other SiCom codes cover specific battery conditions, such as overvoltage, undervoltage, short circuit or a general battery error. If one of those appears, it points to a more specific cause than this internal management error. If the inverter detects external battery management that has not been configured, it raises a separate error. In that case, run the quick configuration guide (QCG) and set up a system with external energy management.
