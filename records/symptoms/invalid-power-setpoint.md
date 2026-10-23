---
id: symptom:invalid-power-setpoint
type: Symptom
name: Invalid power setpoint
aliases:
- ComInvalid
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On SMA Sunny Central CP XT, error 8701 flags invalid external active power setpoints, 8703 an
    invalid power factor in the external reactive power setpoint, and 8704 invalid external active and
    reactive setpoints. All three are warnings, and the manual's corrective measure is to contact SMA
    Service.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r6
    h: f52a146dca89
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r4
    h: 02e2835e142b
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r7
    h: a330cf1d5cfe
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:setpoint-status-cominvalid
  note: The SMA setpoint status display reads ComInvalid when a communication-based control mode (WCtlCom,
    VArCtlCom or PFCtlCom) is selected and the received setpoint content is invalid. It is distinct from
    ComFail, which means the setpoint signal is missing.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=42.r5
    h: 3c77b9807c8e
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=41.r3
    h: 379c7ca50547
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=42
    h: f11ed5228096
  review: drafted
  review_note: 'support check: partial - ComInvalid with the stated modes (WCtlCom, VArCtlCom, PFCtlCom)
    and invalid content is supported, but the passages don''t mention ComFail meaning the setpoint signal
    is missing in the active-power context (only reactive ComFail in u4), which is close but the distinction
    is mostly supported; the note''s ''SMA setpoint status'' framing is generally fine.'
- claim_id: c3
  rel: observed_as
  target: meas:analog-setpoint-signal-low
  note: External active power setpoints below 2 mA are treated as invalid. The inverter keeps the last
    valid value, or uses Pmax after a day change, until valid setpoints return.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r4
    h: 02e2835e142b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - 8701 states setpoints below 2 mA are invalid and last valid value/Pmax
    is used, but the passage doesn''t say ''analog'' explicitly nor mention AC power staying at that value
    as an observed signal; mostly inferred.'
- claim_id: c4
  rel: observed_as
  target: meas:setpoint-feedback-mismatch
  note: On Tesla System Controllers, a setpoint with the correct index and data type but a value outside
    the allowed range raises no IIN flag and does not take effect. Only the feedback point shows that
    the command was not accepted.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=5.1
    h: 4bdd9912e855
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=5.1
    h: 943ce4e82f51
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=6.1
    h: 707b23825ec7
  review: drafted
---
An invalid power setpoint means the inverter has received an external active or reactive power command that it rejects as unusable. On the SMA Sunny Central CP XT it shows as warning 8701 for active power, 8703 for the reactive power factor, or 8704 for both, and the manual's corrective measure is to contact SMA Service. The setpoint status display reads ComInvalid when a communication-based control mode is selected but the setpoint content is invalid, so first check the power specification settings. Do not confuse it with ComFail, which means a valid setpoint signal has been missing for at least five minutes and points to communication units or cabling. For analog active power setpoints, a signal below 2 mA counts as invalid, and the inverter keeps the last valid value, or Pmax after a day change, until valid setpoints return. An SMA Cluster Controller treats a setpoint as invalid if it has no configuration for it or the value is outside the configured range, and a fallback can be configured to take over after a set time. On Tesla controllers, an out-of-range value can be ignored without any error flag, so compare each setpoint with its feedback point to confirm the command was accepted.

<!-- review notes
- sentence 1: support check: partial - Passages say external setpoints are invalid, but not explicitly that the inverter received a command and rejected it as unusable; 8701 notes fallback to last valid value.
- sentence 4: support check: partial - ComFail is described as the expected signal absent for at least five minutes with communication/cabling measures, but the passages state this only for reactive power setpoint modes, and ComFail is not explicitly contrasted with ComInvalid.
- sentence 5: support check: partial - 8701 supports below 2 mA being invalid and last valid value or Pmax after day change, but 'analog' is not stated for 8701 itself.
- sentence 4: review: partial - The table says ComFail means a valid setpoint signal has been absent for at least five minutes and gives communication-unit and cabling measures, but it says this only for the reactive power modes VArCtlCom/PFCtlCom, and the sentence applies it to…
-->
