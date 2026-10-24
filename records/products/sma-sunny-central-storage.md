---
id: prod:sma-sunny-central-storage
type: Product
name: Sunny Central Storage
aliases:
- SCS
- SCS UP
- Sunny Central Storage UP
- SCS 3450 UP
- SCS 3600 UP
- SCS 3800 UP
- SCS 3950 UP
- SCS 3950 UP-XT
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-sunny-central-storage-manuals
    loc: sec=h1
    h: c8b8dc23aa09
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Described as a battery inverter that connects only to a battery or storage device.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: compatible_with
  target: prod:sma-hybrid-controller
  note: Listed among compatible inverters of the SMA Hybrid Controller, including the Sunny Central Storage
    UP.
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2
    h: 3dd628d2646d
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r13
    h: 60b27eba1709
  review: drafted
- claim_id: c4
  rel: has_hazard
  target: hazard:electric-shock
  note: Two AC sources (grid via MV transformer and a separate auxiliary supply) and DC sources must be
    checked for absence of voltage.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c5
  rel: has_hazard
  target: hazard:stored-capacitor-energy
  note: DC link capacitors may stay charged after the inverter is switched off; measure between the DC
    switch and the inverter stacks.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c6
  rel: has_hazard
  target: hazard:dc-arc-flash
  note: Arc flash risk is highlighted especially on the DC side.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c7
  rel: has_hazard
  target: hazard:disconnecting-under-load
  note: Never pull a DC fuse under load.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c8
  rel: has_hazard
  target: hazard:wildlife
  note: Rodents chew cables causing ground faults; snakes and wasps may hide behind door bends.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c9
  rel: has_hazard
  target: hazard:noise
  note: Earplugs recommended near other inverters running at full power.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
  review_note: 'support check: partial - Earplugs are recommended near other inverters running at full
    power because of high-pitched noise, but the video does not say Sunny Central Storage itself has a
    noise hazard beyond that.'
- claim_id: c10
  rel: requires
  target: tool:insulating-gloves
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c11
  rel: requires
  target: tool:arc-rated-clothing
  note: Flame-resistant clothing and an arc flash protection jacket are listed as personal protective
    equipment.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c12
  rel: requires
  target: tool:face-shield
  note: Helmet with built-in visor; goggles alone are not enough.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  rel: requires
  target: tool:lockout-tagout-kit
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c14
  rel: requires
  target: tool:multimeter
  note: Use your own test equipment, rated for the job, to verify absence of voltage.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
  review_note: 'support check: partial - The video requires your own rated test and measurement equipment
    (CAT III/IV 1500 V) to verify voltage-free conditions, but it names no digital multimeter specifically
    (the captions only say ''teach multis savee'').'
---
The Sunny Central Storage (SCS) is an SMA central battery inverter family, usually installed in a medium-voltage power station with its own medium-voltage transformer and switchgear. The UP generation includes the SCS 3450, 3600, 3800 and 3950 UP and UP-XT models, and older manuals cover the SCS 500 to 1000 range. It connects only to a battery, and it does not need the separate DC-DC converter that a Sunny Central PV inverter needs when a battery is added. SMA publishes requirements for the medium-voltage transformers and internal power supply transformers used with it, as well as test instructions for the power-generating unit protection test on the Sunny Central Storage UP. The SMA Hybrid Controller lists it, including the UP version, as a compatible inverter. Before any work, stop the inverter with the start/stop key switch and take the key. Then isolate and lock out both AC sources (the grid and the auxiliary supply) and the DC battery source. The DC link capacitors can stay charged after shutdown. DC arc flash is a key hazard, so never pull fuses under load. Required PPE includes flame-resistant clothing, an arc flash jacket, a helmet with a visor, electrician's gloves and safety shoes. Earplugs are recommended near inverters that are running.

<!-- review notes
- sentence 1: support check: partial - The passages support an SMA battery inverter used in a medium-voltage power station with its own transformer and switchgear, but 'central' and 'family' are only loosely stated.
-->
