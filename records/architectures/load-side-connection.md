---
id: arch:load-side-connection
type: Architecture
name: Load-side connection
aliases:
- load-side breaker
- load side interconnection
- backfed breaker
- backfed circuit breakers
category: Interconnection
claims:
- claim_id: c1
  attr: max_count
  value:
    max: 6
    unit: unit:NUM
  conditions: Disconnecting means allowed for each power source supplying a premises (for example the
    utility service and separately the PV system); the disconnects for each source must be grouped together.
  note: The source cites NEC 230.71 and 690.13(D)&(E). Using an inverter collection subpanel with one
    disconnect lets a system have more than six inverters.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h154
    h: 2fc9cfeb4c9a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
A load-side connection ties the output of a utility-interactive inverter into the premises wiring on the load side of the service disconnect. The connection point can be a load center, a panelboard or a tapped feeder conductor. Many residential and small commercial systems use this method, often by adding backfed circuit breakers to existing distribution panels, provided the code conditions are met. The inverter interconnection needs its own dedicated disconnect and overcurrent protection with no loads on that circuit. One device may serve several inverters whose outputs are paralleled onto a common circuit. To keep the panel bus or feeder from being overloaded, the ampere ratings of all overcurrent devices supplying a busbar or conductor must not add up to more than 120 percent of its rating. From the 2014 NEC on, ampacity calculations for feeders, taps and busbars use 125 percent of the inverter's rated AC output current instead of the inverter breaker rating. Inspection checklists confirm that the backfed breaker or fuse is sized to protect the circuits and is installed in the correct location in the panel. The other option is a supply-side connection. Interactive inverters may be connected on either side of the service disconnecting means.

<!-- review notes
- sentence 6: support check: partial - The checklist items exist for sizing and location of the backfed breaker, but the passages show only items, not that they are 'inspection checklists confirming' and they mention 'or fuse' only for sizing.
-->
