---
id: hazard:wildlife
type: Hazard
name: Wildlife and insects
aliases:
- snakes
- wasps
- rodents
- Wildlife and livestock
- pests
- venomous animals
category: Environmental
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:pest-nest-removal
  note: Annual inspection for pest intrusion and removal of nests from junction, pull and combiner boxes,
    around the array, and from inverter enclosures; use safe sanitation because pests may carry disease.
  cite:
  - src: src:trn-oandm-femp-om-for-small-pv-systems
    loc: tbl=5.r1
    h: 374d47759df9
  - src: src:trn-oandm-femp-om-for-small-pv-systems
    loc: tbl=6.r4
    h: e0e48ad92bc0
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:enclosure-sealing-check
  note: Find and repair cracks that pests use to get into the inverter enclosure; gaskets should be sealed
    so rodents cannot get in and chew cables.
  cite:
  - src: src:trn-oandm-femp-om-for-small-pv-systems
    loc: tbl=6.r4
    h: e0e48ad92bc0
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:rodent-protection
  scope:
    products:
    - prod:sma-sunny-central-storage
  note: Manufacturer offers rodent protection options for Sunny Central and Sunny Central Storage inverters,
    since chewed cables are a common cause of ground faults.
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
  review_note: 'support check: partial - u8 says rodent protection options exist and rodents cause ground
    faults, but the passage doesn''t mention a Sunny Central Storage scope beyond the overall talk; the
    ''common cause'' is stated, so core is supported, with product scoping loosely covered.'
- claim_id: c4
  rel: controlled_by
  target: mit:first-aid-training
  note: Recommended for plant staff because bites from animals such as rats and snakes threaten worker
    health.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: tbl=18.r1
    h: 5d31a54780d3
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: proc:venomous-bite-response
  note: Rapid response procedures for poisonous snakes or arachnids must be known and followed, in some
    cases with anti-venom kept on site; staff must know what to do after bites or stings.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h76
    h: 6dfb733bb990
  - src: src:solarpower-europe-om-guidelines
    loc: sec=2
    h: f68ececd943f
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=2.1
    h: 74b1a24487cc
  review: drafted
- claim_id: c6
  rel: controlled_by
  target: tool:personal-protective-equipment
  note: Everyone entering the site should be trained in site dangers and have the PPE and tools needed;
    for hot and dry sites, wildlife risk assessment and PPE planning are called for.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=2
    h: f68ececd943f
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=2.1
    h: 74b1a24487cc
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h17
    h: da525f81bf0c
  review: drafted
- claim_id: c7
  rel: controlled_by
  target: tool:insect-repellent
  note: Work in mosquito areas calls for mosquito nets and repellent, and in some cases preventive anti-malaria
    medication.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h76
    h: 6dfb733bb990
  review: drafted
- claim_id: c8
  rel: controlled_by
  target: proc:job-hazard-analysis
  note: Written risk assessments listing site hazards, including wildlife, and the steps taken to mitigate
    them.
  cite:
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=2.1
    h: 74b1a24487cc
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h17
    h: da525f81bf0c
  review: drafted
---
Animals and insects on solar and storage sites put workers at direct risk. Snake bites can kill, spider bites cause pain and swelling, tick bites can lead to tick bite fever, bee stings can trigger allergic reactions, and bugs can fly into the eyes. Snakes like to hide behind the bends of inverter doors, and wasps and other insects build nests there, so take care when opening equipment for service. Wildlife also damages equipment. Rodents chew cables once they get past unsealed gaskets, which commonly causes ground faults, and nesting insects and animals can cause short circuits or arc flashes. Ground-mounted plants in rural and farming areas are the most exposed. Termites, rats and snakes cause failures, mostly in solar cables and modules, and hot dry sites add poisonous snakes, spiders and scorpions. Inspect DC wiring boxes and inverter enclosures every year for pests, remove nests using safe sanitation, and repair any cracks or gaps that animals use to get in. Know the rapid response procedure for venomous bites before you go to site, keep anti-venom on site where required, and get first aid training. Do not kill these animals, because it is often illegal and makes a bite more likely. Handling pesticides, herbicides and rodent poisons is a hazard in itself. Plan every job with a risk assessment, proper training and the right PPE.
