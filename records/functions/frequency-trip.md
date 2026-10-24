---
id: func:frequency-trip
type: Function
name: Frequency trip
aliases:
- frequency protection
- over/under-frequency trip
- PTOF
- PTUF
- Grid Frequency Protection
- Shall Trip Function
- Frequency Trip Settings
- Grid Over Frequency Protection
- Grid Low Frequency Protection
category: Protection
function_kind: protection
claims:
- claim_id: c1
  attr: default_value
  value:
    nominal: 56.5
    unit: unit:HZ
  scope:
    standard: std:ieee-1547-2018
  conditions: UF2 shall-trip default frequency
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=25.r4
    h: 3614858a0cd9
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c2
  attr: setting_range
  value:
    min: 50
    max: 57
    unit: unit:HZ
  scope:
    standard: std:ieee-1547-2018
  conditions: UF2 allowable frequency setting range
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=25.r4
    h: 3614858a0cd9
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c3
  attr: default_value
  value:
    nominal: 0.16
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: UF2 default clearing time
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=25.r4
    h: 3614858a0cd9
  review: drafted
- claim_id: c4
  attr: default_value
  value:
    nominal: 62
    unit: unit:HZ
  scope:
    standard: std:ieee-1547-2018
  conditions: OF2 shall-trip default frequency
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=25.r1
    h: 50c2daaa9bd2
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions)
- claim_id: c5
  attr: setting_range
  value:
    min: 61.8
    max: 66
    unit: unit:HZ
  scope:
    standard: std:ieee-1547-2018
  conditions: OF2 allowable frequency setting range
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=25.r1
    h: 50c2daaa9bd2
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c6
  attr: default_value
  value:
    nominal: 0.16
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: OF2 default clearing time
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=25.r1
    h: 50c2daaa9bd2
  review: drafted
- claim_id: c7
  attr: trip_threshold
  value:
    nominal: 58.5
    unit: unit:HZ
  conditions: PPL EU required UF1 shall-trip setting
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  review: disputed
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c11
    (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
  conflicts_with:
  - func:frequency-trip#c15
  - func:frequency-trip#c17
  - func:frequency-trip#c21
- claim_id: c8
  attr: trip_time
  value:
    nominal: 301
    unit: unit:SEC
  conditions: PPL EU required UF1 clearing time
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  review: disputed
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions)
  conflicts_with:
  - func:frequency-trip#c16
  - func:frequency-trip#c18
  - func:frequency-trip#c20
  - func:frequency-trip#c22
- claim_id: c9
  attr: trip_threshold
  value:
    nominal: 56.5
    unit: unit:HZ
  conditions: PPL EU required UF2 shall-trip setting
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  review: disputed
  review_note: possible conflict with c7 (same source; check the conditions); possible conflict with c11
    (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
  conflicts_with:
  - func:frequency-trip#c15
  - func:frequency-trip#c17
  - func:frequency-trip#c19
- claim_id: c10
  attr: trip_time
  value:
    nominal: 0.2
    unit: unit:SEC
  conditions: PPL EU required UF2 clearing time
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  review: disputed
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c12
    (same source; check the conditions)
  conflicts_with:
  - func:frequency-trip#c16
  - func:frequency-trip#c18
  - func:frequency-trip#c20
  - func:frequency-trip#c22
- claim_id: c11
  attr: trip_threshold
  value:
    nominal: 61.2
    unit: unit:HZ
  conditions: PPL EU required OF1 shall-trip setting
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: disputed
  review_note: possible conflict with c7 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
  conflicts_with:
  - func:frequency-trip#c15
  - func:frequency-trip#c19
  - func:frequency-trip#c21
- claim_id: c12
  attr: trip_time
  value:
    nominal: 301
    unit: unit:SEC
  conditions: PPL EU required OF1 clearing time
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: disputed
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions)
  conflicts_with:
  - func:frequency-trip#c16
  - func:frequency-trip#c18
  - func:frequency-trip#c20
  - func:frequency-trip#c22
- claim_id: c13
  attr: trip_threshold
  value:
    nominal: 62
    unit: unit:HZ
  conditions: PPL EU required OF2 shall-trip setting
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: disputed
  review_note: possible conflict with c7 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions)
  conflicts_with:
  - func:frequency-trip#c17
  - func:frequency-trip#c19
  - func:frequency-trip#c21
- claim_id: c14
  attr: trip_time
  value:
    nominal: 0.2
    unit: unit:SEC
  conditions: PPL EU required OF2 clearing time
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: disputed
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c12
    (same source; check the conditions)
  conflicts_with:
  - func:frequency-trip#c16
  - func:frequency-trip#c18
  - func:frequency-trip#c20
  - func:frequency-trip#c22
- claim_id: c15
  attr: trip_threshold
  value:
    nominal: 62
    unit: unit:HZ
  conditions: Generac PWRmicro OF2 frequency trip
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r1
    h: f3190f9274e9
  review: disputed
  conflicts_with:
  - func:frequency-trip#c7
  - func:frequency-trip#c9
  - func:frequency-trip#c11
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c19 (same source; check the conditions); possible conflict with c21 (same source; check the conditions)
- claim_id: c16
  attr: trip_time
  value:
    nominal: 0.16
    unit: unit:SEC
  conditions: Generac PWRmicro OF2 clearing time
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r1
    h: f3190f9274e9
  review: disputed
  conflicts_with:
  - func:frequency-trip#c8
  - func:frequency-trip#c10
  - func:frequency-trip#c12
  - func:frequency-trip#c14
  review_note: possible conflict with c18 (same source; check the conditions); possible conflict with
    c20 (same source; check the conditions)
- claim_id: c17
  attr: trip_threshold
  value:
    nominal: 61.2
    unit: unit:HZ
  conditions: Generac PWRmicro OF1 frequency trip
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r2
    h: 4df42ceedb23
  review: disputed
  conflicts_with:
  - func:frequency-trip#c7
  - func:frequency-trip#c9
  - func:frequency-trip#c13
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c19 (same source; check the conditions); possible conflict with c21 (same source; check the conditions)
- claim_id: c18
  attr: trip_time
  value:
    nominal: 300
    unit: unit:SEC
  conditions: Generac PWRmicro OF1 clearing time
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r2
    h: 4df42ceedb23
  review: disputed
  conflicts_with:
  - func:frequency-trip#c8
  - func:frequency-trip#c10
  - func:frequency-trip#c12
  - func:frequency-trip#c14
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions)
- claim_id: c19
  attr: trip_threshold
  value:
    nominal: 58.5
    unit: unit:HZ
  conditions: Generac PWRmicro UF1 frequency trip
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r3
    h: 7ab836be4e7c
  review: disputed
  conflicts_with:
  - func:frequency-trip#c9
  - func:frequency-trip#c11
  - func:frequency-trip#c13
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c21 (same source; check the conditions)
- claim_id: c20
  attr: trip_time
  value:
    nominal: 300
    unit: unit:SEC
  conditions: Generac PWRmicro UF1 clearing time
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r3
    h: 7ab836be4e7c
  review: disputed
  conflicts_with:
  - func:frequency-trip#c8
  - func:frequency-trip#c10
  - func:frequency-trip#c12
  - func:frequency-trip#c14
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions)
- claim_id: c21
  attr: trip_threshold
  value:
    nominal: 56.5
    unit: unit:HZ
  conditions: Generac PWRmicro UF2 frequency trip
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r4
    h: aa2f35f33a37
  review: disputed
  conflicts_with:
  - func:frequency-trip#c7
  - func:frequency-trip#c11
  - func:frequency-trip#c13
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c19 (same source; check the conditions)
- claim_id: c22
  attr: trip_time
  value:
    nominal: 0.16
    unit: unit:SEC
  conditions: Generac PWRmicro UF2 clearing time
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r4
    h: aa2f35f33a37
  review: disputed
  conflicts_with:
  - func:frequency-trip#c8
  - func:frequency-trip#c10
  - func:frequency-trip#c12
  - func:frequency-trip#c14
  review_note: possible conflict with c18 (same source; check the conditions); possible conflict with
    c20 (same source; check the conditions)
- claim_id: c23
  attr: trip_threshold
  value:
    nominal: 62
    unit: unit:HZ
  scope:
    regions:
    - region:iso-ne
  conditions: SolarEdge ISO New England setting FgMax1
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: tbl=2.r1
    h: 1eda7a6cb10b
  review: drafted
  review_note: possible conflict with c25 (same source; check the conditions); possible conflict with
    c27 (same source; check the conditions); possible conflict with c29 (same source; check the conditions)
- claim_id: c24
  attr: trip_time
  value:
    nominal: 160
    unit: unit:MilliSEC
  scope:
    regions:
    - region:iso-ne
  conditions: SolarEdge ISO New England setting FgMax1 time
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: tbl=2.r1
    h: 1eda7a6cb10b
  review: drafted
  review_note: possible conflict with c26 (same source; check the conditions); possible conflict with
    c28 (same source; check the conditions)
- claim_id: c25
  attr: trip_threshold
  value:
    nominal: 61.2
    unit: unit:HZ
  scope:
    regions:
    - region:iso-ne
  conditions: SolarEdge ISO New England setting FgMax2
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: tbl=2.r2
    h: b275a4627529
  review: drafted
  review_note: possible conflict with c23 (same source; check the conditions); possible conflict with
    c27 (same source; check the conditions); possible conflict with c29 (same source; check the conditions)
- claim_id: c26
  attr: trip_time
  value:
    nominal: 300000
    unit: unit:MilliSEC
  scope:
    regions:
    - region:iso-ne
  conditions: SolarEdge ISO New England setting FgMax2 time
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: tbl=2.r2
    h: b275a4627529
  review: drafted
  review_note: possible conflict with c24 (same source; check the conditions); possible conflict with
    c30 (same source; check the conditions)
- claim_id: c27
  attr: trip_threshold
  value:
    nominal: 58.5
    unit: unit:HZ
  scope:
    regions:
    - region:iso-ne
  conditions: SolarEdge ISO New England setting FgMin1
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: tbl=2.r3
    h: 9c4b323e6329
  review: drafted
  review_note: possible conflict with c23 (same source; check the conditions); possible conflict with
    c25 (same source; check the conditions); possible conflict with c29 (same source; check the conditions)
- claim_id: c28
  attr: trip_time
  value:
    nominal: 300000
    unit: unit:MilliSEC
  scope:
    regions:
    - region:iso-ne
  conditions: SolarEdge ISO New England setting FgMin1 time
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: tbl=2.r3
    h: 9c4b323e6329
  review: drafted
  review_note: possible conflict with c24 (same source; check the conditions); possible conflict with
    c30 (same source; check the conditions)
- claim_id: c29
  attr: trip_threshold
  value:
    nominal: 56.5
    unit: unit:HZ
  scope:
    regions:
    - region:iso-ne
  conditions: SolarEdge ISO New England setting FgMin2
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: tbl=2.r4
    h: bfcf8582de93
  review: drafted
  review_note: possible conflict with c23 (same source; check the conditions); possible conflict with
    c25 (same source; check the conditions); possible conflict with c27 (same source; check the conditions)
- claim_id: c30
  attr: trip_time
  value:
    nominal: 160
    unit: unit:MilliSEC
  scope:
    regions:
    - region:iso-ne
  conditions: SolarEdge ISO New England setting FgMin2 time
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: tbl=2.r4
    h: bfcf8582de93
  review: drafted
  review_note: possible conflict with c26 (same source; check the conditions); possible conflict with
    c28 (same source; check the conditions)
- claim_id: c31
  attr: default_value
  value:
    nominal: 61.2
    unit: unit:HZ
  scope:
    products:
    - prod:chint-sca-25ktl-208
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: CPS GridFrqMax1, IEEE 1547-2018 and ISO-NE profiles
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=26
    h: 1c2bb196b629
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=31
    h: 45dcc2011c57
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=7
    h: 45dcc2011c57
  review: drafted
- claim_id: c32
  attr: default_value
  value:
    nominal: 60.5
    unit: unit:HZ
  scope:
    products:
    - prod:chint-sca-25ktl-208
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    standard: std:cpuc-rule-21
  conditions: CPS GridFrqMax1, Rule 21 profile
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=26
    h: 1c2bb196b629
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=31
    h: 45dcc2011c57
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=7
    h: 45dcc2011c57
  review: drafted
  review_note: possible conflict with c35 (same source; check the conditions)
- claim_id: c33
  attr: setting_range
  value:
    min: 60
    max: 66
    unit: unit:HZ
  scope:
    products:
    - prod:chint-sca-25ktl-208
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: CPS over-frequency thresholds GridFrqMax1-3, all profiles
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=26
    h: 1c2bb196b629
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=31
    h: 45dcc2011c57
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=7
    h: 45dcc2011c57
  review: drafted
- claim_id: c34
  attr: setting_range
  value:
    min: 48
    max: 60
    unit: unit:HZ
  scope:
    products:
    - prod:chint-sca-25ktl-208
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: CPS under-frequency thresholds GridFrqMin1-3, all profiles
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=26
    h: 1c2bb196b629
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=31
    h: 45dcc2011c57
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=7
    h: 45dcc2011c57
  review: drafted
- claim_id: c35
  attr: default_value
  value:
    nominal: 57
    unit: unit:HZ
  scope:
    products:
    - prod:chint-sca-25ktl-208
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    standard: std:cpuc-rule-21
  conditions: CPS GridFrqMin2 and GridFrqMin3, Rule 21 profile (56.5 Hz for IEEE 1547-2018 and ISO-NE)
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=26
    h: 1c2bb196b629
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=31
    h: 45dcc2011c57
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=7
    h: 45dcc2011c57
  review: drafted
  review_note: possible conflict with c32 (same source; check the conditions)
- claim_id: c36
  attr: setting_range
  value:
    min: 0
    max: 1000
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-25ktl-208
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: CPS frequency trip times, IEEE 1547-2018 and ISO-NE profiles
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=26
    h: 1c2bb196b629
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=31
    h: 45dcc2011c57
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=7
    h: 45dcc2011c57
  review: drafted
- claim_id: c37
  attr: setting_range
  value:
    min: 0
    max: 655
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-25ktl-208
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    standard: std:cpuc-rule-21
  conditions: CPS under-frequency trip times FrqMinTripT1-3, Rule 21 profile
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=26
    h: 1c2bb196b629
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=31
    h: 45dcc2011c57
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=7
    h: 45dcc2011c57
  review: drafted
- claim_id: c38
  attr: setting_range
  value:
    min: 0
    max: 1310
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-50-100k-t
  conditions: CPS frequency trip times (FrqMaxTripT1/T2/T3, FrqMinTripT1)
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=43
    h: 281df4b8b471
  review: drafted
- claim_id: c39
  attr: setting_range
  value:
    min: 0.016
    max: 600
    unit: unit:SEC
  scope:
    products:
    - prod:fronius-galvo
  conditions: Fronius Galvo frequency limit violation tolerance time
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: tbl=9.r6
    h: 2a74c7f7e2a4
  review: drafted
---
Frequency trip disconnects the inverter from the grid when grid frequency stays above an over-frequency limit or below an under-frequency limit for longer than its set clearing time. Settings normally come in two stages per direction, such as OF1/OF2 and UF1/UF2, each with its own frequency and clearing time; utilities like PPL EU and ISO New England publish their own required values. CPS string inverters expose GridFrqMax1-3, GridFrqMin1-3 and matching trip time parameters, with separate defaults for the IEEE 1547-2018, Rule 21 and ISO-NE profiles. The Fronius Galvo states a frequency trip accuracy of 0.05 Hz and has a settable tolerance time for frequency limit violations. On Solis hybrids running from a generator, the HF1/HF2 and LF1/LF2 trip points can be widened to stop nuisance trips, but only in backup or off-grid mode, and they must be set back when the grid returns.

<!-- review notes
- sentence 1: support check: partial - Passages say the inverter disconnects after a programmed delay, but the u36 text ties disconnect to abnormal voltage, and the clearing-time tables don't state the general mechanism fully.
- sentence 2: support check: partial - Two stages per direction and PPL EU/ISO-NE values are shown, but 'normally' and that utilities publish their own required values (ISO-NE settings are SolarEdge settings) aren't stated.
- sentence 3: support check: partial - Parameters and profile defaults shown, but a single product doesn't show all of GridFrqMin1-3 in u30, and some tables only have IEEE/Rule21; mostly supported across passages.
-->
