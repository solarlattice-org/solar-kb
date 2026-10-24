---
id: func:scheduling
type: Function
name: Scheduling of power values and modes
aliases:
- schedules
- basic scheduling
- Power scheduling
category: Control
function_kind: control
claims:
- claim_id: c1
  attr: response_time
  value:
    max: 10
    unit: unit:MIN
  scope:
    regions:
    - region:us-ca
    standard: std:cpuc-rule-21
  conditions: 'Scheduling implemented at the gateway/EMS: time to pass the commands to the smart inverters
    after it receives the schedule, unless otherwise agreed'
  quote: The GW/EMS shall communicate the necessary commands to the Smart Inverters within 10 minutes,
    or by mutual agreement
  quote_source: SCE Rule 21 (effective Aug 29, 2023), Section Hh, Sheet 177
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: sec=h549
    h: 7a5aca9df1b1
  review: drafted
- claim_id: c2
  attr: response_time
  value:
    max: 15
    unit: unit:MIN
  scope:
    regions:
    - region:us-ca
    standard: std:cpuc-rule-21
  conditions: 'Schedules stored at an aggregator that is not on the generating facility site: time to
    pass the commands to the smart inverter after it receives the schedule'
  quote: The aggregator shall communicate the necessary commands to the Smart Inverter within 15 minutes
    of the aggregator receiving the scheduling information.
  quote_source: SCE Rule 21 (effective Aug 29, 2023), Section Hh, Sheet 177
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: sec=h549
    h: 7a5aca9df1b1
  review: drafted
---
Scheduling lets a device switch power values or operating modes at set times or over set intervals. In California, SCE Rule 21 requires smart inverter facilities to support scheduling with memory for at least 24 events. Each event changes setpoints for the volt/var, fixed power factor or volt/watt function. Under Rule 21, schedules can be held in a gateway or EMS, in the DER itself, or at an off-site aggregator. Each scheduled mode has a start time and a duration, and when it ends the inverter goes back to its defaults or takes the next commanded mode. On these SMA units you can upload schedules from a file under Configuration, Energy management, Schedules. An upload overwrites any schedules already stored. Power factor scheduling is one form of this function: the inverter's reactive power follows a schedule of inductive or capacitive power factor commands.

<!-- review notes
- sentence 1: support check: partial - The evidence has a title about selecting power values for times or intervals, and it says schedules control operating modes. It doesn't explicitly say a device switches values or modes at set times or intervals.
- sentence 4: support check: partial - The upload path and the overwriting of existing schedules are stated. The evidence doesn't name SMA or say 'Schedules' sits under Configuration, Energy management as a menu path, and the path is only partly shown.
-->
