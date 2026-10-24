---
id: concept:neutral-ground-bond
type: Concept
name: Neutral-ground bond
aliases:
- N-G bond
- main bonding jumper
- neutral-ground bonding
- Neutral to Ground Jumper
- Bonding Jumper
category: Safety
concept_kind: electrical
claims:
- claim_id: c1
  rel: explains
  target: hazard:electric-shock
  note: A neutral-ground bond made anywhere other than the service entrance can put return current onto
    grounded parts such as enclosures, pipes and the ground itself, which creates a risk of electrocution.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-08-backup-interface-installation-and-wiring
    loc: sec=h8
    h: b1b83d29d236
  - src: src:se-academy-home-hub-technical-essentials-na-technical-02-home-hub-overview
    loc: sec=h6
    h: c778f65a11eb
  review: drafted
- claim_id: c2
  rel: related_to
  target: prod:solaredge-backup-interface
  note: The jumper should not be installed on the BI-NU version. On the BI-EU version, which is service-entrance
    certified and includes neutral-ground bonding, it depends on the AC installation.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-08-backup-interface-installation-and-wiring
    loc: sec=h8
    h: b1b83d29d236
  - src: src:se-academy-home-hub-technical-essentials-na-technical-07-backup-interface-overview
    loc: sec=h24
    h: f77798657429
  review: drafted
- claim_id: c3
  rel: related_to
  target: arch:partial-home-backup
  note: When loads are moved to a backup subpanel, neutral and ground must not be bonded at that subpanel.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-02-home-hub-overview
    loc: sec=h6
    h: c778f65a11eb
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:authority-having-jurisdiction
  note: Bonding must follow jurisdictional rules. Consult the AHJ when in doubt.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-08-backup-interface-installation-and-wiring
    loc: sec=h8
    h: b1b83d29d236
  - src: src:se-academy-home-hub-technical-essentials-na-technical-02-home-hub-overview
    loc: sec=h6
    h: c778f65a11eb
  review: drafted
- claim_id: c5
  rel: related_to
  target: symptom:enclosure-touch-voltage
  note: An improper bond can energize equipment chassis and metal piping.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-08-backup-interface-installation-and-wiring
    loc: sec=h8
    h: b1b83d29d236
  - src: src:se-academy-home-hub-technical-essentials-na-technical-02-home-hub-overview
    loc: sec=h6
    h: c778f65a11eb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Passages say improper bonding can electrify equipment chassis
    and metal piping, but they never mention touch voltage on an enclosure as a symptom by name; the relation
    is implied.'
---
A neutral-ground bond is the connection between the neutral conductor and the grounding system. It should only be made at the main service entrance panel. The neutral carries current. If it is bonded to ground anywhere else, such as in a subpanel, return current gets parallel paths back to the source through the ground system. How much current flows on those stray paths depends on the imbalance between the two lines and on the resistance of each path. Current on the ground system can energize equipment enclosures, metal piping and even the ground underfoot. This can cause electrocution, equipment damage or serious injury. Equipment differs: some backup interface versions must not have the bonding jumper installed, while service-entrance-rated versions include neutral-ground bonding that depends on the AC installation. Some string inverters warn against fitting a neutral-to-ground jumper when the neutral conductor is connected, because this can damage the unit and void the warranty. Always follow local code requirements and check with the authority having jurisdiction or a master electrician before adding or removing a bond. Bond points can be checked with continuity or bond-resistance tests, which look for a low-resistance connection.

<!-- review notes
- sentence 1: support check: partial - The 'only at main service panel' part is stated, but the passages do not define a neutral-ground bond as the neutral-to-grounding-system connection (though it is implied).
- sentence 6: support check: partial - Passages warn against a neutral-to-ground jumper when the neutral is connected, with damage and warranty voiding, but do not say the products are string inverters.
- sentence 7: support check: partial - Passages say to follow jurisdictional rules and consult the AHJ or master electrician with questions, but not 'always' before every addition or removal.
- sentence 7: review: partial - The passages say to follow jurisdictional rules and code and to consult the AHJ or a master electrician with questions, but not to check every time before adding or removing a bond.
-->
