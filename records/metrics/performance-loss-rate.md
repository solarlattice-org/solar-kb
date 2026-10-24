---
id: metric:performance-loss-rate
type: Metric
name: Performance loss rate
aliases:
- PLR
category: Performance
---
Performance loss rate tracks how the performance of a PV module or a whole PV system changes over time, using a chosen performance metric such as an electrical or empirical metric. It is worked out from time series data, preferably DC power readings, with AC power used when DC is not available, and it should use at least two years of historical data. The steps are: check the quality of the raw data, filter out anomalies and non-representative points, pick a performance metric such as performance ratio or a predicted-power model, apply an optional temperature correction, aggregate to days, weeks, months or years, then fit a trend against time. A linear model is fitted between time and the metric. The relative PLR is the slope coefficient divided by the intercept, scaled to a yearly basis by the number of periods per year, such as 12 for monthly or 52 for weekly data. Relative PLR is reported in percent per year. An absolute PLR is also defined, in units of the metric per year, and should be reported together with the intercept. A single linear rate is the simplest way to report it, but field systems often degrade non-linearly, so a change-point segmented regression can report the change-point time and a separate linear rate for each segment. When performance ratio is the metric, its temperature correction should follow IEC 61724-1:2017.

<!-- review notes
- sentence 2: support check: partial - DC preferred with AC fallback and the two-year minimum are stated, but the two-year figure is only a definition note (calculated using at least two years), not stated as a 'should' requirement.
- sentence 4: support check: partial - The passage describes a linear model with slope β1, intercept β0 and a scaling t (12 monthly, 52 weekly), but the equations are missing, so 'slope divided by intercept' is not explicitly stated.
-->
