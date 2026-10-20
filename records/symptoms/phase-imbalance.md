---
id: symptom:phase-imbalance
type: Symptom
name: Phase imbalance
aliases:
- Grid Voltage Imbalance
- Unbalance
- DIFERENT VOLTAGE BETWEEN PHASES
- voltage imbalance
claims:
- claim_id: c1
  rel: observed_as
  target: meas:negative-sequence-voltage-imbalance
  note: Revenue/PQ meter quantity V_IMB in percent, updated every 10/12 cycles; reported as zero when
    positive-sequence voltage is below 13 V.
  cite:
  - src: src:sel-735-im-20250228
    loc: tbl=367
    h: dc6dc586373a
  - src: src:sel-735-im-20250228
    loc: sec=h559
    h: bf4e428b2cda
  - src: src:sel-735-im-20250228
    loc: tbl=75.r7
    h: a3fbcec75cb8
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:negative-sequence-current-imbalance
  note: Meter quantity I_IMB in percent; reported as zero when positive-sequence current is below 10 mA.
  cite:
  - src: src:sel-735-im-20250228
    loc: tbl=367
    h: dc6dc586373a
  - src: src:sel-735-im-20250228
    loc: sec=h559
    h: bf4e428b2cda
  - src: src:sel-735-im-20250228
    loc: tbl=75.r7
    h: a3fbcec75cb8
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:zero-sequence-imbalance
  note: V0_IMB and I0_IMB; zero-sequence voltage imbalance reads zero on delta-connected (Form 5) meters.
  cite:
  - src: src:sel-735-im-20250228
    loc: tbl=367
    h: dc6dc586373a
  - src: src:sel-735-im-20250228
    loc: sec=h559
    h: bf4e428b2cda
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:phase-voltage-spread-alert
  note: Default monitoring alert checks that meter phase voltages are within 5% of each other.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=12.r10
    h: cec53a327f7b
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:grid-voltage-imbalance-fault
  note: Inverter fault (e.g. Sungrow fault code 17) raised when grid phase voltages differ beyond a settable
    imbalance threshold; inverter reconnects when grid returns to normal.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r1
    h: 3d7464a5ab51
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=9
    h: 7abcbbacf5be
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=33
    h: 7abcbbacf5be
  review: drafted
  review_note: 'support check: partial - The fault, reconnection on grid recovery, and the adjustable
    imbalance parameter are stated. The passages don''t say the fault is raised when phase voltages exceed
    that threshold. They also don''t say the inverter''s fault code 17 is a Sungrow-specific example beyond
    what is shown.'
---
Phase imbalance means the three AC phase voltages or currents at the grid connection are not equal. Power quality meters report it as negative-sequence and zero-sequence imbalance in percent for both voltage and current, and can log it as a one-minute average. Monitoring platforms can raise a default alert when the meter phase voltages are not within 5% of each other. Inverters may trip on a grid voltage imbalance fault and normally reconnect once the grid returns to normal. If the fault keeps coming back, measure the actual grid phase voltages first. A large difference points to the utility side, so contact the power company. If the measured difference is within what the local utility allows, the inverter imbalance threshold can be adjusted. Contact the manufacturer if the fault persists after that. On the transformer side, check for low or variable load, check the primary voltage, and make sure the ground connections and tank grounding are correct.

<!-- review notes
- sentence 1: support check: partial - The passages define imbalance quantities and say grid phase voltages differ, but they don't state this general definition, and they don't mention currents at the grid connection.
- sentence 4: support check: partial - The Grid Voltage Imbalance fault and reconnection after the grid returns to normal are stated, but the passages don't say the inverter trips; reconnecting implies a disconnect.
- sentence 7: support check: partial - The passages give actions for variable load, primary voltage, ground connections and tank ground, but the low-voltage item is not stated as low load, and nothing says these are transformer-side checks.
-->
