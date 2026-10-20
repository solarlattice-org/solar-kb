---
id: mit:energy-model-update
type: Mitigation
name: Energy model update
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Extra annual production loss from tracker wind stow once gust-driven tracker response is
    modeled, compared with models that use only hourly wind data (2026 kWh Analytics Solar Risk Assessment)
  note: Shows how much an energy model built on hourly TMY3 wind data can understate stow losses.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: drafted
  review_note: 'support check: partial - Passage says losses can increase by up to 4%, an upper bound,
    whereas the statement presents it as a ''typical'' value.'
---
An energy model update means revising the production model and forecasts so they reflect how the plant actually behaves in the field, not the simplified assumptions used at design time. For Terrain Undulation Yield Losses, the model should be updated with measured row-level behavior, because rolling ground can make the real tracker field differ from the simplified geometry the model assumed. For Tracker Wind Stow Production Losses, compare actual annual stow hours with the model's assumptions and reconcile them against P50/P90 values. Updating the model only makes the loss visible and accounted for; it does not recover the energy, which needs steps such as tuning backtracking or tracker settings within structural limits.

<!-- review notes
- sentence 1: support check: partial - Passages mention updating models/forecasts with measured behavior or unrepresented stow, but don't define 'energy model update' as the broad statement claims about design-time simplified assumptions.
- sentence 4: support check: partial - Passages list tuning backtracking and tracker policies within structural limits as mitigations alongside model updates, but don't explicitly state that updating the model alone doesn't recover energy.
-->
