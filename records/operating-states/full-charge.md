---
id: state:full-charge
type: OperatingState
name: Full charge
aliases:
- full charging
- Full
category: Storage
claims:
- claim_id: c1
  rel: subclass_of
  target: state:battery-charging
  note: Full charge is reported as one value of the active battery charging process parameter BatChrgOp.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=59.r6
    h: c939d9992c3a
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=110.r6
    h: 701c41e77fba
  review: drafted
---
Full charge is a routine charging process in which the Sunny Island brings the battery up to at least 95% state of charge. Its purpose is to make up for earlier undercharging and to extend battery life. The Sunny Island starts a full charge on its own once the full-charge cycle time (parameter CycTmFul) has run out, or once total discharge since the last full charge adds up to eight times the battery's rated capacity. One manual gives the default interval as every 14 days or after eight nominal charge throughputs. You can set the charging voltage (ChrgVtgFul) and the duration (AptTmFul) to match the battery maker's recommendations. One manual lists a default cell charge voltage of 2.45 V for full charging. While a full charge is running, the active charging process parameter BatChrgOp reads Full (2). Entering this mode is logged as event 9321 or shown on the display as E205. If an external charger or charge controller meets the full-charge criteria, the Sunny Island counts that as a full charge it did itself. The generator request can be set so that a generator is called for during full charge.

<!-- review notes
- sentence 5: support check: partial - BatChrgOp Full (2), event 9321 and E205 are stated as status change to full charge, but 'logged as event 9321 or display E205' is plausible; the link is not explicit about entering mode being logged, though close.
-->
