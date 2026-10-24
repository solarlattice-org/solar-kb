---
id: tool:tesla-opticaster
type: Tool
name: Tesla Opticaster
aliases:
- Opticaster
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:tesla
  note: Described as Tesla's autonomous site control software.
  cite:
  - src: src:eq-equip-bess-tesla-opticaster-overview
    loc: sec=front
    h: 6f38a75b0d21
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: sec=2.5.7
    h: b77f20caea7a
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.5.6
    h: 8300c71d4d0e
  - src: src:tesla-scada-design-manual-v3-4
    loc: sec=2.1.3
    h: 666d8a6d370b
  review: drafted
  review_note: 'support check: partial - Passages call Opticaster Tesla''s autonomous site control software,
    but none names Tesla Energy as the maker.'
---
Tesla Opticaster is Tesla's autonomous site control software for grid-connected battery storage sites. It forecasts load and solar production and schedules battery charging and discharging to lower electricity bills. It uses peak shaving and energy shifting based on the site's tariff. It can also maximize use of on-site renewables, support grid services, and work within incentive programs such as SGIP, ITC solar-charging rules, export limits and special programs like demand response. To configure it, Tesla needs at least the current utility tariffs, the billing cycles, and historic load and solar interval data. Tesla recommends sending these to the Project Engineer after installation using the Opticaster Checklist. Without historic data it still runs from startup, but it needs about two weeks of data to calibrate its forecast model. Opticaster runs only while the Tesla Site Controller is in Autonomous mode. If the controller is switched to another mode, such as Site Control, Opticaster stops running. By default it controls 15-minute average site demand. Check its behavior with 15-minute averaged data, because short instantaneous peaks may not get a response. Actual power can differ from target power when the battery reaches its state-of-energy limits or has hardware problems. Forecast errors at sites with spiky, unpredictable loads can also make peak shaving less effective.
