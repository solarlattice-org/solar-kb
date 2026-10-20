---
id: stressor:high-wind
type: Stressor
name: High winds
aliases:
- Damaging winds
- Straight-line winds
- Windstorms
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Annual production loss of single-axis trackers once gust-driven stow is modelled, compared
    with models that use hourly wind data only
  note: This is the extra loss that hourly TMY3 wind models miss. It is not the total loss from wind stow.
  quote: annual production losses can increase by up to 4% compared with models that rely on hourly wind
    data alone
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: drafted
  review_note: 'support check: partial - Passage says annual losses can increase by up to 4% when gust
    response is modelled versus hourly-only models, but it is an upper bound, not a typical value, and
    it doesn''t mention single-axis or TMY3 beyond the models'' description in a way matching ''typical''.'
---
Most storm damage to PV comes from racking that was poorly designed, or from bolts and fasteners that were installed badly or torqued too little. Wind can loosen these, and in a severe event racking can collapse or modules can be torn off their mounts. Single-axis trackers are at particular risk. Strong wind can set off torsional galloping, where twisting spreads from the row ends inward until the row comes apart. This has happened at gusts well below the design wind speed. High winds also loosen cables and connectors. Moisture can then get in, causing corrosion, high resistance and eventually electrical failure. High winds are one of the external stresses that can break module front glass, and broken glass and frayed wiring are common debris after a storm. To protect the structure, trackers move into a stow position when wind passes the controller threshold. This causes intermittent production dips while the rows are off angle. Reschedule maintenance when strong winds are forecast. Once the storm has passed, watch out for loose modules and debris. To reduce exposure, assess wind risk at the site, specify robust mounting and tracker wind loads, use bolted joints that resist vibration, install several anemometers, and use a sound stow strategy. Lowering stow thresholds to recover energy is not advised unless the tracker supplier and a structural engineer confirm the change is safe.

<!-- review notes
- sentence 1: support check: partial - Passages say storm damage is generally attributable to poor racking design and/or poorly installed or under-torqued fasteners, with collapse and modules ripped off, but 'most' is slightly stronger than 'generally'.
-->
