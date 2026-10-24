---
id: prod:generac-pv-link
type: Product
name: Generac PV Link
aliases:
- PV Link
- S2502
- PV Link Optimizer
category: MLPE
make: generac
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:power-optimizer
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h30
    h: 34d782318c7d
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h57
    h: 90fa1a608a46
  review: drafted
- claim_id: c2
  rel: manufactured_by
  target: org:generac
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h30
    h: 34d782318c7d
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h79
    h: 26c1394f8fff
  review: drafted
- claim_id: c3
  rel: implements
  target: func:rapid-shutdown
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h30
    h: 34d782318c7d
  review: drafted
- claim_id: c4
  rel: implements
  target: func:ground-fault-protection
  note: Ground fault detection and interruption (GFDI).
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h30
    h: 34d782318c7d
  review: drafted
- claim_id: c5
  rel: implements
  target: func:dc-arc-fault-protection
  note: Arc fault detection and circuit interruption (AFCI).
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h30
    h: 34d782318c7d
  review: drafted
- claim_id: c6
  rel: implements
  target: func:remote-firmware-update
  note: Over-the-air updates usually happen automatically; installers should confirm firmware is current.
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h62
    h: 52a88cfe4a8b
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:power-line-communication
  note: Bidirectional PLC carried on the DC output to talk to inverters and other REbus devices.
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h30
    h: 34d782318c7d
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:ul-1741
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=3.r18
    h: c6022e9b824c
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:ul-1699b
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=3.r18
    h: c6022e9b824c
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:csa-c22-2-no-107-1
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=3.r18
    h: c6022e9b824c
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:generac-pwrcell-inverter
  note: Enabled, configured and monitored from the PWRcell Inverter control panel.
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h68
    h: 27045505d3cb
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h67
    h: c372ab218ad9
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h79
    h: 26c1394f8fff
  review: drafted
- claim_id: c12
  rel: requires
  target: prod:staubli-mc4
  note: Field wiring must use Staubli MC4 connectors only.
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h57
    h: 90fa1a608a46
  review: drafted
- claim_id: c13
  rel: incompatible_with
  target: arch:grounded-pv-array
  note: Modules that need positive or negative grounding would interfere with PLC communication.
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h30
    h: 34d782318c7d
  review: drafted
- claim_id: c14
  attr: rated_power
  value:
    nominal: 2500
    unit: unit:W
  conditions: continuous
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=3.r1
    h: 2bd5e8df3f19
  review: drafted
- claim_id: c15
  attr: max_input_voltage
  value:
    max: 420
    unit: unit:V
  conditions: absolute maximum DC input voltage
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=3.r5
    h: a89e405e4890
  review: drafted
- claim_id: c16
  attr: max_input_current
  value:
    max: 18
    unit: unit:A
  conditions: maximum input short-circuit current per PV Link
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=3.r7
    h: bd42ead076f1
  review: drafted
  review_note: 'support check: partial - The passage gives max input short-circuit current 18 A, but ''per
    PV Link'' is not stated.'
- claim_id: c17
  attr: rated_output_current
  value:
    max: 8
    unit: unit:A
  conditions: maximum continuous output current per PV Link
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=3.r11
    h: f06738ec7805
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h57
    h: 90fa1a608a46
  review: drafted
- claim_id: c18
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: peak efficiency
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=3.r2
    h: 07bc81f414b7
  review: drafted
- claim_id: c19
  attr: nominal_voltage
  value:
    nominal: 380
    unit: unit:V
  conditions: regulated DC output bus (REbus)
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h30
    h: 34d782318c7d
  review: drafted
  review_note: possible conflict with c20 (same source; check the conditions)
- claim_id: c20
  attr: nominal_voltage
  value:
    nominal: 190
    unit: unit:V
  conditions: REbus stated as plus/minus 190 VDC nominal regulated DC bus
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h57
    h: 90fa1a608a46
  review: drafted
  review_note: possible conflict with c19 (same source; check the conditions)
---
Generac PV Link is a non-isolated boost-type DC-DC optimizer. It raises the PV input voltage and feeds it onto REbus, Generac's regulated 380 VDC bus. It is rated for 2,500 W continuous, with a 420 VDC absolute maximum input, an 8 A continuous output current and a 99 percent peak efficiency. It uses power line communication on its DC output and includes ground fault protection, arc fault protection and rapid shutdown. Firmware updates arrive over the air. Connect it only to REbus-compatible equipment such as the PWRcell Inverter, never to a conventional PV inverter. Use Staubli MC4 connectors only. Never wire PV Links in series. You can parallel at most three on one home run. Units leave the factory disabled. Enable each one from the inverter control panel. If a PV Link shows offline, check its DC disconnect, its PLM channel setting, the REbus wiring and the REbus fuses. It is certified to UL 1741, UL 1699B and CSA C22.2 No. 107.1.

<!-- review notes
- sentence 4: support check: partial - REbus-compatible only and MC4 only are stated; the PWRcell Inverter is the controlling device but 'never conventional PV inverter' is implied by damage warning, fairly well covered.
-->
