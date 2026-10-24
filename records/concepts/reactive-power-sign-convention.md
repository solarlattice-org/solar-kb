---
id: concept:reactive-power-sign-convention
type: Concept
name: Reactive power sign convention
aliases:
- generator reference-arrow system
- consumer reference system
- injecting vs absorbing
- power sign convention
- generator sign convention
- consumer reference-arrow system
- load sign convention
- IEEE VAR sign convention
- meter sign convention
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: explains
  target: concept:reactive-power
  note: Defines whether positive reactive power means over-excited injection (raising voltage) or under-excited
    absorption (lowering voltage).
  cite:
  - src: src:sma-doc-275857
    loc: sec=3.2
    h: 7db7c94e4415
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: sec=3.2
    h: a37a1edffb15
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h30
    h: c47e00cd11af
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:active-power
  note: In the generator convention, active power output is positive and active power drawn from the grid
    is negative.
  cite:
  - src: src:sma-doc-275857
    loc: sec=3.2
    h: 7db7c94e4415
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: sec=3.2
    h: a37a1edffb15
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:pq-capability-diagram
  note: To convert between the consumer and generator conventions, invert the signs of P and Q. On the
    P/Q diagram this mirrors the plot through the origin.
  cite:
  - src: src:sma-doc-275857
    loc: sec=3.2
    h: 7db7c94e4415
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: sec=3.2
    h: a37a1edffb15
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:power-factor
  note: Meters and controllers sign power factor in different ways, for example by following real power,
    by following reactive power, or by quadrant.
  cite:
  - src: src:eq-equip-meters-elkor-wattson-ii-wattson-mark-ii-manual-complete
    loc: tbl=41
    h: 1b5c81f51ef9
  - src: src:eq-equip-bess-enel-enel-x-der-os-site-modbus-server-manual-v1-1-2
    loc: tbl=5.r9
    h: 3b8f180e8b73
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.3.10
    h: 42a5bb2bf830
  review: drafted
- claim_id: c5
  rel: related_to
  target: std:ieee-1547-2018
  note: This standard states its requirements in generator sign convention, which is the opposite of load
    sign convention.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h30
    h: c47e00cd11af
  review: drafted
- claim_id: c6
  rel: related_to
  target: org:iec
  note: The units say IEC uses the generator reference-arrow system internationally.
  cite:
  - src: src:sma-doc-275857
    loc: sec=3.2
    h: 7db7c94e4415
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: sec=3.2
    h: a37a1edffb15
  review: drafted
- claim_id: c7
  rel: related_to
  target: org:ieee
  note: The units say IEEE uses the generator reference-arrow system internationally.
  cite:
  - src: src:sma-doc-275857
    loc: sec=3.2
    h: 7db7c94e4415
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: sec=3.2
    h: a37a1edffb15
  review: drafted
- claim_id: c8
  rel: related_to
  target: org:vde
  note: The VDE application guide uses the consumer reference-arrow system.
  cite:
  - src: src:sma-doc-275857
    loc: sec=3.2
    h: 7db7c94e4415
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: sec=3.2
    h: a37a1edffb15
  review: drafted
- claim_id: c9
  rel: related_to
  target: prod:sel-735
  note: This meter reports VARs in four quadrants, following the IEEE VAR sign convention.
  cite:
  - src: src:eq-equip-meters-sel-735-sel-735-manual-735-im-20190828
    loc: sec=h280
    h: cd8283e51585
  review: drafted
- claim_id: c10
  rel: related_to
  target: prod:tesla-site-controller
  note: This controller assumes a defined meter sign convention when it measures and sets control points.
  cite:
  - src: src:eq-equip-bess-tesla-powerpack-system-controls-and-communication-manual
    loc: sec=4.3.1
    h: af0c396e2556
  review: drafted
---
The reactive power sign convention sets which direction of power flow counts as positive. Two systems are common: the generator reference-arrow system and the consumer (load) reference system. In the generator convention, power flowing from the plant into the grid is positive. Active power output is positive and active power drawn from the grid is negative. Positive reactive power means over-excited operation, where current lags voltage and the device injects vars, which tends to raise voltage. Negative reactive power means under-excited operation, where current leads voltage and the device absorbs vars, which tends to lower voltage. In the consumer reference system, current absorbed from the grid is positive, so exported power appears as negative. To convert values from one system to the other, invert the signs of both active and reactive power. On the P-Q capability diagram this mirrors the plot through the origin. IEC, IEEE and IEEE 1547-2018 use the generator convention. The VDE application guide uses the consumer convention. Meters and plant controllers may use their own conventions. Some let you configure the power sign, and power factor sign modes vary, so check the documentation before you enter reactive power or power factor setpoints.

<!-- review notes
- sentence 7: support check: partial - Passages show configurable power sign, varying PF sign modes and meter-specific conventions, but none explicitly advise checking documentation before entering setpoints.
-->
