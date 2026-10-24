---
id: concept:battery-charging-stages
type: Concept
name: Battery charging stages
aliases:
- bulk charge
- absorption charge
- float charge
- equalization charge
- charge taper
- Charging phases
- IUoU procedure
- three-level charge control
- multi-stage charging algorithms
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: state:float-charge
  note: Float charge is the final stage. It holds the battery full at a reduced charging voltage.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h17
    h: 668e52e11175
  - src: src:sma-doc-260329
    loc: sec=2.1
    h: aa29a6188cf1
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.5
    h: 165b6683fb63
  review: drafted
- claim_id: c2
  rel: related_to
  target: state:boost-charge
  note: Boost charge is one of the charging processes the battery management can select during the constant
    voltage phase.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h16
    h: 7f22d149d051
  - src: src:sma-doc-260329
    loc: sec=2.2
    h: e012c72d98e3
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.5
    h: 165b6683fb63
  review: drafted
- claim_id: c3
  rel: related_to
  target: state:full-charge
  note: Full charge is one of the charging processes the battery management can select during the constant
    voltage phase.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h16
    h: 7f22d149d051
  - src: src:sma-doc-260329
    loc: sec=2.2
    h: e012c72d98e3
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.5
    h: 165b6683fb63
  review: drafted
- claim_id: c4
  rel: related_to
  target: state:equalization-charge
  note: Equalization charge is a constant voltage process that evens out the state of charge between cells.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h16
    h: 7f22d149d051
  - src: src:sma-doc-260329
    loc: sec=h22
    h: 374e652dc59d
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.5.3
    h: f4db99488919
  review: drafted
- claim_id: c5
  rel: related_to
  target: mit:equalization-charge
  note: Regular equalization helps prevent individual cells from failing early.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h22
    h: 374e652dc59d
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h620
    h: f3802cb2769a
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.5.3
    h: f4db99488919
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:state-of-charge
  note: Float charge ends when the state of charge falls below 70% or when discharges reach 30% of nominal
    capacity.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h17
    h: 668e52e11175
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.5
    h: 165b6683fb63
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h620
    h: f3802cb2769a
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:lead-acid-battery
  note: The SMA documentation shows the charging phases with sample values for an AGM battery.
  cite:
  - src: src:sma-doc-260329
    loc: fig=3
    h: 319b6b72762e
  - src: src:sma-doc-260329
    loc: sec=2.1
    h: aa29a6188cf1
  review: drafted
---
Battery charging stages are the sequence of phases a charge controller or battery inverter steps through to charge a battery fully without overcharging it. In the first stage, called the constant current or bulk phase, charging current is held at a set limit and the battery voltage rises as the battery takes on charge. When the voltage reaches its setpoint, the constant voltage or absorption phase begins: voltage is held steady and the current tapers off continuously for a set absorption time. During absorption, the battery management picks a boost, full or equalization charge process, and each one has its own voltage and time settings that should follow the battery maker's recommendations. Absorption is followed by float charge, which keeps the battery full at a much lower voltage to avoid early aging from overcharging. Float charge ends, and charging returns to the constant current phase, once discharges add up to 30% of nominal capacity or the state of charge drops below 70%. Equalization charge deliberately overcharges the battery under control, so that cells in a series string that have drifted apart all end up fully charged; this prevents early cell failure. Technicians can watch the stage in progress through the active charging process and remaining absorption time display values, and through event messages such as the change to float charge.
