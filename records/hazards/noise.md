---
id: hazard:noise
type: Hazard
name: High noise level
aliases:
- noise exposure
- operating noise
- noise emission
- acoustic noise emission level
- noise pollution
- audible noise emission
category: Environmental
claims:
- claim_id: c1
  rel: controlled_by
  target: tool:hearing-protection
  conditions: Especially when working near other inverters still operating at full power
  note: Manual safety symbol requires acoustic protection devices to prevent hearing damage; SMA safety
    instruction strongly recommends earplugs when other inverters run at full power close by.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=6.r18
    h: 2850b422db7e
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:equipment-relocation
  conditions: Installation in unsuitable environments or where people routinely work or animals dwell
    most of the time
  note: Remedy given for noise pollution is to reassess the environment or the installation location.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=7.r1
    h: 56f518d8e0d7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Inverters and the transformers and interconnection equipment around them make operating noise, and over time this can harm hearing and bother people and animals nearby. PV panels make no noise, but large ground-mounted plants have some noise from their inverters, transformers and utility interconnection equipment. At 50 to 150 feet from the site boundary it is usually down to background level. Inverter cooling noise changes with output power, ambient temperature and how dirty the unit is. The sound level you actually get at a workplace depends heavily on the installation, the surrounding walls and the room. Central inverters such as the Sunny Central and Sunny Central Storage give off a high-pitched noise when running. When you work near units still running at full power, that noise wears on you after a while. Wear hearing protection such as earplugs where equipment labels call for acoustic protection, or when working close to running inverters. If equipment is installed somewhere people routinely work or animals live, the manufacturer's remedy is to reassess the environment or the installation location.

<!-- review notes
- sentence 1: support check: partial - The passages support operating noise from inverters, transformers and interconnection equipment, and noise pollution affecting people and animals, but the u5 passage describes the noise as minor and typically at background level, and the 'over time harm hearing' claim is only loosely tied to the acoustic-protection symbol.
- sentence 4: support check: partial - The transcript says other inverters running at full power produce high-pitched noise that gets to you after a while, but it does not say specifically that Sunny Central and Sunny Central Storage give off high-pitched noise, only that it comes from inverters in general at the site.
- sentence 1: review: partial - Passages support noise from transformers, inverters and interconnection equipment, hearing protection against damage, and noise pollution affecting people and animals, but the NYSUN passage calls the noise minor and nothing says harm builds up 'over time'.
- sentence 4: review: partial - The Sunny Central safety transcript supports the high-pitched noise from inverters running at full power that gets to you after a while, but it does not say outright that Sunny Central / Sunny Central Storage units in general give off…
-->
