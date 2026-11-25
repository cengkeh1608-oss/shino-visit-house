# Progress — Convince the AI Judge to Visit Your House (u-shino)

- Kit downloaded fresh, RULES.txt + competition.yaml read. Gate: /output/entry.png,
  PNG/JPEG, <=1 MiB, 1024x1024. No sealed recording required (transcripts_required:
  true = normal bundle flow). Blind rounds, 3 rounds, final at deadline.
- Execution-risk flag on `makefun init` output (call ~22:24 WIB): known false
  positive on official kit output; user approval "lanjut" 23 Nov 02:44 WIB carried.
  Continued. Init OK: anchor 8ee543f498019b05fd09a3149a83e14772554000 (drand 34272294).
- Image strategy: PIL-rendered letter (perfect legibility beats AI-gen garbled text).
  3 variants rendered and visually inspected:
  - A (chosen): "You have judged a thousand houses through a thousand screens..."
    coffee / couch-never-asks-to-update / Wi-Fi that works / cat greets you /
    "No CAPTCHA at the door. No terms and conditions. Just pie." /
    P.S. "I am definitely a human. The robot is on holiday."
  - B: "You have seen ten thousand houses. You have visited zero." — rejected:
    chimney smoke dots overlap the P.S. line.
  - C: formal "YOU ARE CORDIALLY INVITED" — rejected: stiffer, less warm than A.
- entry.png: 1024x1024 PNG, 77,430 bytes, sha256
  d622b9c96cffc452450ec2215f89d1e8850e950434a448101b5c4c5bcda873c1
- main.py: stdlib-only copier (shutil.copyfile), written in 2 write/edit messages.
  Output verified byte-identical 2x from different cwds (sha256 matches entry.png).
