---
id: func:forecast-based-charging
type: Function
name: Forecast-based battery charging
aliases:
- weather-forecast-based charging
- forecast-based charging
- forecast-dependent charging
- predictive battery charging
- optimized storage management
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  rel: requires
  target: prod:sma-sunny-home-manager-2
  note: The energy manager plans battery charging and discharging from PV and consumption forecasts.
  cite:
  - src: src:sma-kb-how-does-the-forecast-battery-charging-work
    loc: sec=h1
    h: 478a15dd5db6
  - src: src:sma-kb-setting-up-forecast-based-battery-charging-with-the-sunny-home-manager-2-0-in-sunny
    loc: sec=h1
    h: d877c131cea9
  review: drafted
- claim_id: c2
  rel: requires
  target: role:installer
  note: Configuring the function in Sunny Portal requires installer authentication.
  cite:
  - src: src:sma-kb-how-does-the-forecast-battery-charging-work
    loc: sec=h1
    h: 478a15dd5db6
  - src: src:sma-kb-setting-up-forecast-based-battery-charging-with-the-sunny-home-manager-2-0-in-sunny
    loc: sec=h1
    h: d877c131cea9
  review: drafted
- claim_id: c3
  rel: requires
  target: tool:sma-sunny-portal
  note: Activated and configured in Sunny Portal under the Sunny Home Manager device properties.
  cite:
  - src: src:sma-kb-setting-up-forecast-based-battery-charging-with-the-sunny-home-manager-2-0-in-sunny
    loc: sec=h1
    h: d877c131cea9
  - src: src:sma-kb-system-conditions-for-forecast-based-battery-charging
    loc: sec=h1
    h: a46660a11c55
  review: drafted
- claim_id: c4
  rel: requires
  target: func:export-limitation
  note: Only enable when an active power feed-in limitation is set; plants without a feed-in limitation
    do not need the function.
  cite:
  - src: src:sma-kb-setting-up-forecast-based-battery-charging-with-the-sunny-home-manager-2-0-in-sunny
    loc: sec=h1
    h: d877c131cea9
  - src: src:sma-kb-system-conditions-for-forecast-based-battery-charging
    loc: sec=h1
    h: a46660a11c55
  review: drafted
- claim_id: c5
  rel: requires
  target: prod:sma-sunny-island
  note: One of the supported battery inverters; Sunny Boy Storage is the alternative.
  cite:
  - src: src:sma-kb-how-does-the-forecast-battery-charging-work
    loc: sec=h1
    h: 478a15dd5db6
  - src: src:sma-kb-system-conditions-for-forecast-based-battery-charging
    loc: sec=h1
    h: a46660a11c55
  review: drafted
- claim_id: c6
  rel: requires
  target: prod:sma-sunny-boy-storage
  scope:
    products:
    - prod:sma-sunny-boy-storage
    firmware_min: V1.50.12.R
  note: For SBS 3.7/5.0/6.0-10 the function has been available since firmware V1.50.12.R.
  cite:
  - src: src:sma-kb-how-does-the-forecast-battery-charging-work
    loc: sec=h1
    h: 478a15dd5db6
  - src: src:sma-kb-system-conditions-for-forecast-based-battery-charging
    loc: sec=h1
    h: a46660a11c55
  review: drafted
- claim_id: c7
  rel: requires
  target: prod:sma-sunny-home-manager
  scope:
    products:
    - prod:sma-sunny-home-manager
    firmware_min: 1.12.13.R
  note: Older Sunny Home Manager-10 path, used with Sunny Island -11 devices or Sunny Boy Smart Energy.
  cite:
  - src: src:sma-kb-system-conditions-for-forecast-based-battery-charging
    loc: sec=h1
    h: a46660a11c55
  review: drafted
- claim_id: c8
  attr: default_value
  value:
    nominal: 48
    unit: unit:HR
  scope:
    products:
    - prod:sma-sunny-home-manager-2
  conditions: Forecast period of forecast-based battery charging when the 'Shortened forecast period'
    option is not activated; activating that option shortens it to 24 hours
  cite:
  - src: src:sma-kb-battery-is-not-getting-fully-charged-with-sunny-home-manager
    loc: sec=h1
    h: c95ab3bb8d67
  review: drafted
---
Forecast-based battery charging lets the Sunny Home Manager 2.0 schedule battery charging and discharging so that the PV system does not need to be curtailed by a feed-in limit. It takes a PV yield forecast built from internet weather data, subtracts a learned household consumption forecast, and holds back enough battery capacity to absorb the energy that would otherwise be curtailed. On sunny days the battery charges around noon at peak generation. On poor days it charges in the morning, so a battery that is not fully charged is intended behaviour. Setup is done in Sunny Portal with installer access and needs the system location, string configuration, feed-in and electricity tariffs, and the active power feed-in limitation. The 'Operating mode Active power' parameter must be set to 'Act. power lim. via PV system ctrl' on all inverters. The required SoC field reserves part of the battery from this planning. The shortened forecast period option cuts the horizon from 48 to 24 hours, so more surplus PV goes into the battery on the current day. The function is supported only on all-SMA systems (Sunny Boy or Sunny Tripower PV inverters with Sunny Island, Sunny Boy Storage or Sunny Tripower Smart Energy). It cannot be used when Tigo optimizers are integrated into Sunny Portal. Time-slot battery charging, load peak capping, Modbus battery control and EEBUS communication switch off or restrict the function. Switching it off stops only the battery planning, and the other forecasts keep running. In an SMA example with feed-in limited to 60 percent, derating losses fell from 3 percent to 1.5 percent of PV generation. Wrong forecasts can leave the battery under-used and lower self-sufficiency.

<!-- review notes
- sentence 5: support check: partial - The 48-to-24-hour shortening and the extra surplus charging are stated, but the passages say only that the required-SoC field excludes a battery component, or that forecast-based charging activates once the set SoC is reached; they do not say it reserves part of the battery.
- sentence 6: support check: partial - All-SMA support, the listed SMA devices and the Tigo exclusion are stated, but 'Sunny Tripower Smart Energy' appears only in u13, not in the support requirements, and the SMA-only limit is worded as sources registered in the Sunny Home Manager.
-->
