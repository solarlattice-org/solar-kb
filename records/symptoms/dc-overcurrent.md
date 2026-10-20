---
id: symptom:dc-overcurrent
type: Symptom
name: DC overcurrent
aliases:
- PVx Over current
- Overcurrent at the DC input
claims:
- claim_id: c1
  rel: observed_as
  target: meas:dc-input-overcurrent-event
  note: Inverter flags overcurrent on a PV input (CPS reports it per input as PVx, x=1,2,3; SMA as events
    3803-3808) and briefly stops feeding in. The CPS manuals say to check the PV input current first.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=38.r4
    h: 6bf04fd80ae7
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r4
    h: 6bf04fd80ae7
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=62.r4
    h: 6bf04fd80ae7
  review: drafted
  review_note: 'support check: partial - Passages support PV input overcurrent per input (PVx, SMA 3803-3808)
    and brief feed-in interruption, but not the specific signal behaviors (current reaching limit, AC
    output dropping to zero then resuming) or that CPS briefly stops feeding in.'
---
The inverter reports overcurrent on one of its PV inputs. CPS units name the input as PVx, where x is 1, 2 or 3. On SMA string inverters, overcurrent at the DC input makes the inverter stop feeding in for a short time. If the message comes up often, check that the PV array is correctly rated and wired. SMA events 3801 and 3802 for DC overcurrent tell you to check the PV array and look for ground faults. On CPS units, first check the PV input current. Then turn both the AC and DC switches off, wait one minute for stored energy to discharge, and switch them back on. If the CPS inverter still cannot clear the fault after a restart, replace the inverter. During DC inspection, confirm that string and array overcurrent protective devices are fitted and correctly specified. Where strings have no protective device, confirm that the module maximum series fuse rating is above the possible reverse current. Also confirm that string cables are sized for the combined fault current of parallel strings. Any back-feed current from the inverter must stay below both the module fuse rating and the cable ampere rating.
