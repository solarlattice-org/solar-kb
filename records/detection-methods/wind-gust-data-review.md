---
id: method:wind-gust-data-review
type: DetectionMethod
name: Wind gust data review
claims:
- claim_id: c1
  rel: produces
  target: meas:stow-event-output-dip
  note: Dips are intermittent and weather-correlated, occurring while irradiance supports production and
    rows sit in stow during gusty periods; seen by aligning stow telemetry with gust records and irradiance-normalized
    output.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h2
    h: 3c102c6647a1
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=front
    h: 7527536ecf9c
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Increase in annual production loss once gust-driven tracker response is modeled, compared
    with models that use only hourly wind data (2026 kWh Analytics Solar Risk Assessment).
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Wind gust data review compares tracker stow telemetry with high-frequency wind gust records, controller wind thresholds, SCADA production and output normalized to plane-of-array irradiance during windy periods. Line these events up with production, irradiance and inverter status so that stow loss is kept separate from clipping, grid curtailment, outages and sensor faults. The review confirms tracker wind stow production losses. These show up as intermittent output dips linked to weather while irradiance is still good. Monthly reviews can miss them because the dips get lumped in with availability, curtailment or weather variance. If only lower-resolution wind data is available, use suitable gust conversion methods and record the uncertainty before you change any project loss assumptions. Compare actual annual stow hours against the energy model assumptions. Do not lower stow thresholds to recover energy unless the tracker supplier and the structural engineer confirm the change stays within the design envelope. On-site wind speed is best measured with an anemometer mounted 10 m above ground level.

<!-- review notes
- sentence 3: support check: partial - Signature and missed-in-monthly-review points are stated, but the passage doesn't say a review 'confirms' losses; this is a description of possible signatures.
- sentence 6: support check: partial - Passages say wind speed is measured with an anemometer at 10 m above ground level as best practice, but 'best measured' phrasing is slightly stronger; the practice is stated for the met station generally, so it is essentially supported.
-->
