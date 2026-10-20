---
id: mit:tracker-stow-strategy
type: Mitigation
name: Tracker stow strategy
aliases:
- hail stow
- defensive stow position
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Increase in annual production loss when gust-driven tracker stow is modeled, compared with
    models that use only hourly wind data (2026 kWh Analytics Solar Risk Assessment)
  note: This is the stow loss that hourly-wind models miss. Use it to size how much stow strategy and
    stow modeling matter.
  quote: annual production losses can increase by up to 4% compared with models that rely on hourly wind
    data alone
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Passage says losses can increase by up to 4% versus hourly-wind
    models, but that is an upper bound, not a typical value.'
---
A tracker stow strategy sets when single-axis trackers leave normal tracking for a protective angle, which positions they move to, and how they return to tracking. It applies to Tracker Wind Stow Production Losses, where gusts trigger stow and the off-angle rows capture less light. For Snow Accumulation Yield Losses, changing the stow is one option to evaluate where it pays off. Check the tracker wind thresholds and the return-to-track logic. Tune site operating policies only within structural limits, and compare actual stow hours against the P50/P90 assumptions. Do not lower stow thresholds just to recover energy unless the tracker supplier and the structural engineer confirm the change stays within the design envelope. Stow protects against torsional divergence, resonance and fatigue loading. Base stow decisions on high-frequency wind data, such as three-second gusts, one-minute averages or a site met mast. Hourly averages can stay below the threshold while real gusts cross it. Several anemometers help, because storm gusts can be small and unevenly spread across a site. In hail-prone areas, a defensive hail stow, if done properly, is known to measurably reduce wind and hail damage. Where the tracker maker allows, hail stow should take priority over other stow modes. In winter, trackers frozen in a stow position can look like snow loss in the residuals. Filter them out before estimating how much loss can be recovered.

<!-- review notes
- sentence 1: support check: partial - Passages describe trackers moving to a protective angle when wind exceeds threshold and returning to normal tracking, but don't define a strategy as setting when, which positions, and how return occurs.
- sentence 7: support check: partial - Passage supports properly executed hail stow reducing damage and precedence where manufacturer allows, but doesn't specifically limit it to hail-prone areas beyond high-risk context, which is largely implied.
- sentence 8: support check: partial - Passage says frozen tracker stow positions overlap with snow events and should be filtered before estimating recoverable loss, but doesn't say they look like snow loss in residuals specifically in winter trackers beyond the general statement.
-->
