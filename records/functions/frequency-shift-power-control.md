---
id: func:frequency-shift-power-control
type: Function
name: Frequency-shift power control
aliases:
- FSPC
- frequency shift power control
- power adjustment via frequency
- P(f)
- power control via frequency
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: subclass_of
  target: func:frequency-watt
  note: PV inverter output is curtailed as the AC frequency set by the battery inverter rises
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=17.5
    h: 1e72be26c078
  - src: src:sma-kb-frequency-shift-power-control-p-f
    loc: sec=h1
    h: d227cdd0a9b2
  review: drafted
- claim_id: c2
  rel: requires
  target: prod:sma-sunny-island-us
  scope:
    applications:
    - off-grid
  note: The Sunny Island shifts the stand-alone grid frequency to signal Sunny Boy inverters to limit
    power
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=17.5
    h: 1e72be26c078
  review: drafted
- claim_id: c3
  rel: requires
  target: role:grid-guard-code-holder
  note: A Grid Guard code may be needed to set the country standard to Island Mode 60 or Offgrid
  cite:
  - src: src:sma-kb-frequency-shift-power-control-p-f
    loc: sec=h1
    h: d227cdd0a9b2
  review: drafted
  review_note: 'support check: partial - The article says to set the country standard with your Grid Guard
    Code ''if needed'', which supports the note. It does not clearly state that FSPC requires a Grid Guard
    code holder.; review: partial - The SMA article says to set the Country Standard with your Grid Guard
    Code ''if needed'', which supports the note, but it does not say frequency-shift power control always
    requires a Grid Guard code holder.'
- claim_id: c4
  attr: default_value
  value:
    nominal: 61
    unit: unit:HZ
  scope:
    applications:
    - off-grid
    - backup
  conditions: Start frequency of curtailment (buckling overfrequency) on SMA PV inverters with country
    standard set to Island Mode 60 / Offgrid
  cite:
  - src: src:sma-kb-frequency-shift-power-control-p-f
    loc: sec=h1
    h: d227cdd0a9b2
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c5
  attr: default_value
  value:
    nominal: 62
    unit: unit:HZ
  scope:
    applications:
    - off-grid
    - backup
  conditions: Frequency at which SMA PV inverter active power reaches 0% under the Island Mode default
    curve
  cite:
  - src: src:sma-kb-frequency-shift-power-control-p-f
    loc: sec=h1
    h: d227cdd0a9b2
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c6
  attr: default_value
  value:
    nominal: 100
    unit: unit:PERCENT
  scope:
    applications:
    - off-grid
    - backup
  conditions: Default active power change per Hz in case of overfrequency, Island Mode
  cite:
  - src: src:sma-kb-frequency-shift-power-control-p-f
    loc: sec=h1
    h: d227cdd0a9b2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Frequency-shift power control lets a battery inverter curtail AC-coupled PV inverters by raising the frequency of the stand-alone grid, so the battery does not overcharge when PV output exceeds the loads. On the Sunny Island 4548-US / 6048-US, the Sunny Boy starts limiting power once the frequency rises above f0 by fAC Start delta, and its output falls to 0 W at fAC Limit delta. If the frequency drops below fAC Delta- or rises above fAC Delta+, the Sunny Boy inverters disconnect from the stand-alone grid. When a diesel generator is running, the generator sets the frequency, so in most cases the Sunny Boys keep feeding their full power. On newer SMA PV inverters, set the country standard to Island Mode 60 or Offgrid. By default, curtailment then starts at 61Hz and falls linearly to zero active power at 62Hz. On firmware below 4.0, the start and end points are under Device Parameters, AC Side, Island Mode. On firmware above 4.0, and on SBSE or STPX, search for P(f) in the inverter or ennexOS. Once a Sunny Boy has stand-alone grid parameters, it no longer complies with IEEE 1547. Only use these settings on inverters that are disconnected from the utility grid, and check with the power company.

<!-- review notes
- sentence 5: support check: partial - The country standard and the 61 Hz and 62 Hz defaults are stated. 'Newer' inverters is not stated, and a Grid Guard Code 'if needed' is omitted.
- sentence 7: support check: partial - u14 says the Sunny Boy no longer complies with IEEE 929 and 1547 and to consult the power company. The instruction to use these settings only on inverters disconnected from the utility grid is only loosely supported by u13.
-->
