# Setup — Moon Knight profile for `kuxx12257`

Everything here goes into the repo named **`kuxx12257`** (same name as your
username — that's what makes GitHub show it on your profile page). That repo
already exists on your account, so you're adding files to it, not creating it.

It must be **public**, or the profile page won't render it.

---

## 1. File layout

Put the files in exactly this structure:

```
kuxx12257/
├── README.md
├── assets/
│   ├── banner.svg
│   ├── tagline.svg
│   ├── divider.svg
│   └── play-badge.svg
└── docs/
    └── index.html
```

Via the web UI: go to the repo → **Add file → Upload files** → drag the whole
folder in. GitHub keeps the folder structure.

Via git:

```bash
git clone https://github.com/kuxx12257/kuxx12257.git
cd kuxx12257
# copy README.md, assets/ and docs/ in here
git add -A
git commit -m "Moon Knight profile"
git push
```

## 2. Turn on the music page

The play button in the README points at a GitHub Pages site. To switch it on:

**Repo → Settings → Pages → Source: "Deploy from a branch" → Branch: `main`,
folder: `/docs` → Save.**

Give it about a minute, then check <https://kuxx12257.github.io/kuxx12257>.
Until Pages is enabled that link 404s — the rest of the README works regardless.

## 3. If your default branch is `master`, not `main`

The image URLs in `README.md` are absolute and hardcode `main`. If your repo
uses `master`, fix them in one pass:

```bash
sed -i 's|/kuxx12257/kuxx12257/main/|/kuxx12257/kuxx12257/master/|g' README.md
```

---

## Editing it later

`build_readme.py` generates `README.md`; `build_assets.py` generates the SVGs.
Both are plain Python with no dependencies.

To add or remove a skill, edit the `SKILLS` list near the top of
`build_readme.py` and re-run `python3 build_readme.py`. Each entry is
`("Label", "logo")` where `logo` is:

- a [simple-icons](https://simpleicons.org) slug (`"python"`, `"tensorflow"`)
  for a real product logo, tinted gold;
- `"moon"` for the gold crescent, used on every concept skill;
- `None` for no icon at all.

Same idea for `PROJECTS` — edit the list, re-run the script.

Prefer to hand-edit `README.md` directly? Fine — just know the scripts will
overwrite it if you run them again.

---

## Things worth checking before you publish

**Your email.** The README uses `2kushagrayadav12257@gmail.com`, the address on
your Claude account. The PDF résumé's text layer reads
`2kushagrayadav8e12257@gmail.com` — the `8e` looks like an artifact of how the
PDF was produced, but you're the only one who knows which is right. Fix it in
the two `mailto:` links if I picked wrong.

**Three project links in your résumé are broken.** I used the real repo names
from your account instead:

| Résumé says | Actually named |
|---|---|
| `deep-fake-detection-extended_1` | `Deep-Fake-Detection-extended` |
| *(preprint listed by DOI only)* | also linked to your `sphbla-m` repo |
| *(not listed)* | added `Quantitative_risk_simulation_jp_morgan_jobsim` |

Worth fixing in the résumé PDF too — that first one 404s for anyone who types it.

**Six skills I inferred rather than read off your résumé.** Git, GitHub, VS Code,
Linux, Markdown and Jupyter aren't in your Technical Skills section, but they're
safe bets for someone shipping ML repos. If any is wrong, delete it from the
`SKILLS` list in `build_readme.py`.

**The `[edit to match transcript]` and `[confirm with university]` notes** are
still sitting in your résumé PDF's coursework and availability lines. I left them
out of the README, but go clean them out of the PDF before you send it anywhere.

---

## On the artwork and the music

All four SVGs are original — geometric crescents, an ankh-in-diamond divider, a
bone/black/gold palette. No Marvel artwork or characters are reproduced, so
there's nothing here that could get the repo flagged.

The player page hosts **no audio file**. It embeds Marvel Music's own official
YouTube upload and Spotify's official embed widget, both of which stream from
the rights holders and pay out normally. The page carries an attribution line
and a "not affiliated with Marvel" disclaimer.

One thing I could not test from here: VEVO channels sometimes disable off-site
embedding, and I had no way to check that without loading the real player. If it
turns out to be blocked, the page detects it and swaps in a message plus an
"Open on YouTube" button — so it degrades cleanly instead of showing a dead box.
Load the Pages URL once after you enable it and you'll know within a second.
