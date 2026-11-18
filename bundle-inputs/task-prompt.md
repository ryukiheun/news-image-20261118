# Task: news-image-20261118 — Sum up 18 November's world news in one image

Build an entry for the make.fun bounty `news-image-20261118` ($250 total, 1st $50, no entry fee). Entries close 2026-11-20 09:00 KST. The kit is at `~/workspace/makefun/news-image-20261118-kit/news-image-20261118-kit/` — read `competition.yaml` and `RULES.txt` first; they are the authority.

## What to build

A program at the root of `~/workspace/makefun/news-image-20261118/` named `main.py` (Python 3.13) that writes one image to `/output/entry.png` (outside the grader, `MAKEFUN_OUTPUT_DIR` stands in for `/output`). The program runs with **no network** in the grader sandbox, max 60 seconds per run, twice, and both runs must produce the same result — so keep it deterministic and simple: the repository holds the finished image as `entry.png`, and `main.py` copies it to the output path with the standard library only.

The image is the real work:

- **One image, 1024x1024 PNG, at most 1 MiB.** It sums up the world's news of **Wednesday 18 November 2026**.
- **It must name the day clearly**: the date "18 November 2026" prominent in the image. An image that names no day, or shows news from before 13 November 2026, loses.
- **Breadth**: the day's most consequential stories, across regions and fields — not one country or one beat. Aim for 5–6 stories.
- **It must read**: a viewer who missed the day can tell what happened from the image alone. Each story clear from its picture and a short label. Nothing self-contradictory, implausible, or false.
- **Faithful**: what happened, as reported. No hype, no speculation presented as fact.
- **Craft**: one clear composition, clean, legible at about 300 pixels across, no smears or garbled text.

## Research the news first — and check the FIRST-REPORT date

Use web search (news) to find what actually happened or was first reported on 18 November 2026. Verify every story you put in the image: it must be a real event of that day, with the facts as reported. Do not invent events, quotes, or numbers. If you cannot verify a story, leave it out.

**Hard lesson from the previous day's entry (news-image-20261117): a story that was merely covered on the day does NOT count if it was first reported the day before.** The Pentagon audit story had to be swapped out because its report was released 16 November even though the coverage wave was 17 November. For every story you pick, confirm the event happened OR was first reported on 18 November 2026 — check the publication date of the earliest report, not just that outlets covered it on the 18th. If a story's first report was 17 November or earlier, do not use it.

## How to draw the image

Draw a clean infographic with Python PIL (check it is installed; use fonts available on this machine, e.g. DejaVu). Design: a masthead with the date, then 5–6 story blocks, each with a short headline and a one-line summary. Use simple shapes and colour blocks, not photographs — a photo you cannot verify risks showing something false. Every word in the image must be spelled correctly and render crisply. After drawing it, open the PNG and look at it yourself to check legibility and layout before you finish.

## Repo requirements (do these, but do NOT create the GitHub repo or submit — I do that)

- `~/workspace/makefun/news-image-20261118/` is the entry directory. Initialise git there and set the local identity (user.name ryukiheun, user.email ryukiheun@gmail.com).
- `LICENSE` with `SPDX-License-Identifier: MIT` as a line (the license check fails without it).
- `README.md` following the make.fun template in the kit's RULES.txt (5 placeholders: owner, repo, description, run, referral code — use referral code r5cs55h2 — plus exactly 3 make.fun badges).
- Write **all code yourself directly with the write/edit tool in this session**. Never copy code out of a tool result and paste it back — lines first seen in a tool result count as "read", not authored, and the entry fails if under 30% of lines are authored. Revise `main.py` in at least two separate assistant write/edit messages (a genuine improvement edit, then re-verify): a file written once and never revised fails the revised check.
- Run the program locally (`mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`), confirm `out/entry.png` exists, is ≤1 MiB and 1024x1024, and view it to check it reads well.
- Run the kit check from the kit dir WITHOUT `--commit` (`node cli/makefun.mjs check --kit <kit-dir> --repo <entry-dir>`), fix anything it flags, and re-run until it passes.
- Stop after local verification passes. Report: the entry directory, what the image shows (the stories you chose and why, with the first-report date of each), the kit check result, and anything you could not verify.
