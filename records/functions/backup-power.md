---
id: func:backup-power
type: Function
name: Backup power
aliases:
- battery backup
- EPS output
- emergency power supply
- backup mode
- battery-backup function
- backup power supply
- battery-backup operation
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  attr: response_time
  value:
    max: 30
    unit: unit:MilliSEC
  scope:
    products:
    - prod:sma-sunny-tripower-smart-energy
  conditions: Automatic switchover of backup loads to the integrated backup output after a utility grid
    failure
  cite:
  - src: src:sma-kb-does-the-sunny-tripower-smart-energy-have-an-integrated-battery-backup-function-or
    loc: sec=h1
    h: d562d4341e8d
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 30
    unit: unit:MilliSEC
  scope:
    products:
    - prod:sma-sunny-tripower-smart-energy
  conditions: Lower end of the adjustable backup switchover time
  note: The source gives the adjustable range as 30 ms to 10 s.
  cite:
  - src: src:sma-kb-does-the-sunny-tripower-smart-energy-have-an-integrated-battery-backup-function-or
    loc: sec=h1
    h: d562d4341e8d
  review: drafted
- claim_id: c3
  attr: setting_range
  value:
    max: 10
    unit: unit:SEC
  scope:
    products:
    - prod:sma-sunny-tripower-smart-energy
  conditions: Upper end of the adjustable backup switchover time
  note: The source gives the adjustable range as 30 ms to 10 s.
  cite:
  - src: src:sma-kb-does-the-sunny-tripower-smart-energy-have-an-integrated-battery-backup-function-or
    loc: sec=h1
    h: d562d4341e8d
  review: drafted
- claim_id: c4
  attr: setting_range
  value:
    min: 10
    max: 99990
    unit: unit:MilliSEC
  scope:
    regions:
    - region:it
  conditions: 'EPS Switching Time: delay from grid failure until the backup (EPS) port activates, set
    in SolisCloud advanced settings under EPS Mode (Italy only)'
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h66
    h: 680b8dd97029
  review: drafted
- claim_id: c5
  attr: setting_range
  value:
    min: 10
    max: 100
    unit: unit:PERCENT
  scope:
    regions:
    - region:it
  conditions: 'EPS DOD: minimum battery state of charge kept for EPS use, set in SolisCloud advanced settings
    under EPS Mode (Italy only)'
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h66
    h: 680b8dd97029
  review: drafted
- claim_id: c6
  rel: requires
  target: func:backup-transfer
  note: Sunny Tripower Smart Energy disconnects backup loads from the grid automatically; Solis uses an
    ATS for whole-home backup.
  cite:
  - src: src:sma-kb-does-the-sunny-tripower-smart-energy-have-an-integrated-battery-backup-function-or
    loc: sec=h1
    h: d562d4341e8d
  - src: src:kb-solis-44002827896-whole-home-backup-topology-using-eps-and-ats
    loc: sec=h2
    h: c1916795a033
  review: drafted
---
Backup power keeps chosen loads running during a grid outage. It draws on PV production and stored battery energy through a dedicated backup or EPS output. On Solis hybrid inverters the EPS output can feed an automatic transfer switch for whole-home backup. The switch moves the house loads between the utility grid and the inverter backup supply. The Sunny Tripower Smart Energy has a built-in three-phase backup supply. It separates the backup loads from the grid automatically, so no manual switchover is needed, and it handles unbalanced loads. While on backup, the Sunny Tripower Smart Energy still charges its battery from surplus PV. On Generac PWRcell systems, the EnaIslanding setpoint must be on before the inverter can enter Island Mode for backup. On the Sunny Boy Smart Energy, the backup type parameter can be set to Off, Secure power supply or Automatic backup operation. It is found under Configuration, Energy management.

<!-- review notes
- sentence 5: support check: partial - Passage says systems with the PWRcell Battery need EnaIslanding on to enter Island Mode; the statement generalizes to all PWRcell systems.
-->
