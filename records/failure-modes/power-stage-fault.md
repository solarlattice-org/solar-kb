---
id: fm:power-stage-fault
type: FailureMode
name: Power stage fault
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  note: O&M service lists place IGBT driver board and IGBT matrix replacement under inverter repair.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h236
    h: fdc8d39f282f
  - src: src:doe-femp-om-small-pv
    loc: sec=h29
    h: ecaae89914de
  review: drafted
  review_note: 'support check: partial - Passages list IGBT driver and IGBT matrix replacement as inverter
    repairs, but never mention a ''power stage fault'' as such.'
- claim_id: c2
  rel: detected_by
  target: method:inverter-display-check
  note: Service lists say to diagnose IGBT driver board faults from the inverter fault code.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h236
    h: fdc8d39f282f
  - src: src:doe-femp-om-small-pv
    loc: sec=h29
    h: ecaae89914de
  review: drafted
  review_note: 'support check: partial - Passages say to diagnose IGBT driver replacement with the fault
    code, but don''t mention an inverter display check or a power stage fault.'
- claim_id: c3
  rel: mitigated_by
  target: mit:igbt-driver-replacement
  note: Done as needed by an inverter specialist after diagnosis from the fault code.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h236
    h: fdc8d39f282f
  - src: src:doe-femp-om-small-pv
    loc: sec=h29
    h: ecaae89914de
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:igbt-matrix-replacement
  note: Listed as an as-needed inverter repair done by an inverter specialist.
  cite:
  - src: src:doe-femp-om-small-pv
    loc: sec=h29
    h: ecaae89914de
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  note: A start/stop reboot is listed for clearing unknown inverter errors. It is not specific to power
    stage faults.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h236
    h: fdc8d39f282f
  - src: src:doe-femp-om-small-pv
    loc: sec=h29
    h: ecaae89914de
  review: drafted
---
A power stage fault is an inverter repair case where the switching hardware, such as the IGBT driver board or the IGBT matrix, has to be diagnosed and replaced. On some inverters a red Power Fault light comes on. It means there is a power fault that needs service and may be a hazard. Use the inverter fault code to find out which board has failed before you replace anything. Restarting the inverter can clear an unknown error, but a fault that stays needs an inverter specialist.

<!-- review notes
- sentence 1: support check: partial - IGBT driver and matrix replacement are inverter repairs, but the passages never define a power stage fault or tie these replacements to it.
- sentence 3: support check: partial - The passages say to diagnose with the fault code when replacing the IGBT driver and other boards, but not explicitly to identify which board failed before replacing anything.
- sentence 4: support check: partial - The passages list the reboot to clear an unknown error and inverter specialists for board repairs, but don't say a persisting fault needs a specialist.
-->
