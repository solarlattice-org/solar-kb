---
id: meas:ir-warm-substring
type: Measurement
name: Warm substring in IR image
aliases:
- OC substrings
- open substrings
signals:
- point: model_160.DCV
  unit: unit:V
  pattern: input voltage stepped down compared with peer inputs at similar irradiance
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    min: 5
    max: 10
    unit: unit:K
  conditions: Open-circuit substrings or module strings from unreliable junction box connections, compared
    with active strings during IR thermography inspection
  quote: Open-circuit (OC) substrings or module strings appear 5-10 K hotter in IRT inspection compared
    to active strings.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
In an IR image, one whole substring of a module looks warmer than the active substrings next to it. This happens because an inactive part does not turn sunlight into DC power, so the energy stays in the module as heat. Open-circuited substrings caused by cold solder joints or other weak connections in the junction box show this pattern. Thermal inspection can find these junction box interconnection failures when they leave a substring disconnected. If one substring is overheated with an irregular pattern, it points to a short-circuited bypass diode or a shorted substring. The power of that substring is lost and the module open-circuit voltage drops. The temperature difference between inactive and active parts is small and roughly proportional to irradiance, so it may not show up under low light. Take images at high irradiance, above 600 W/m², with no clouds, low wind and steady ambient temperature. A bypass diode that is open or not connected does not show up in a daytime IR scan. At night, feed a reverse current of 3% to 5% of rated Isc into the string and look for a substring that has warmed slightly. A wide-angle IR camera can show modules or strings that are not producing or not connected, because their temperature is clearly different from their neighbours. Check suspect modules with a visual inspection and electrical tests, such as comparing their IV curves with a normal module.

<!-- review notes
- sentence 5: support check: partial - Passages say mode A/open BPD can't be detected by IRT and recommend night reverse-bias test at 3-5% Isc looking for a warmed substring, but 'daytime' IR and 'reverse current' wording is slightly extended (open BPD is mode A, undetected without shading).
-->
