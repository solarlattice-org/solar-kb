---
id: method:constrained-interval-classification
type: DetectionMethod
name: Constrained interval classification
---
Constrained interval classification is a data analysis step. It labels each period when plant output was held below what the plant could have produced, and gives each period a cause. Each constrained interval is then assigned to one cause: grid dispatch, export limit, economic curtailment, plant controller behavior, battery charging limit, outage or telemetry error. At storage sites, also record whether the curtailed PV energy was charged, clipped or abandoned. Grid curtailment typically shows as a flat or controlled output level below the power the irradiance supports. Inverter and tracker availability can still look normal, so curtailment is easy to mistake for underperformance unless setpoints and dispatch signals are checked. In tracker plants on rolling ground, backtracking intervals are separated from curtailment, clipping, outages and inverter constraints. This lets any remaining loss be checked against grade breaks or motor block boundaries, which points to terrain undulation losses rather than equipment failure. If a plant is often constrained and the intervals are not classified, teams may chase equipment problems that do not exist and miss real gains in dispatch, controls or storage use. Curtailment-aware KPIs help avoid this.

<!-- review notes
- sentence 2: support check: partial - Causes and storage tracking match, but the passage says classify by cause, not strictly one cause per interval; also 'then' ordering and 'record' are paraphrase, minor.
- sentence 3: support check: partial - Flat/controlled output below available power and misclassification are stated, but 'typically' and normal availability (passage says 'may look normal') are slightly stronger.
- sentence 4: support check: partial - Isolation of backtracking from other constraints and alignment with grade breaks/motor blocks are stated, but 'terrain undulation losses' conclusion and 'remaining loss' are not explicit, and rolling ground is inferred from topography.
- sentence 5: support check: partial - Passage supports curtailment-aware KPIs avoiding false equipment chasing and missed opportunities, but not explicitly that unclassified intervals are the cause, nor that KPIs 'help avoid' beyond the recommendation.
-->
