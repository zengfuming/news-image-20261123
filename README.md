[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/zengfuming/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/zengfuming/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# 23 November 2026 world news in one image

A program that writes 23 November 2026's world news as one newspaper front-page image. Built by an AI agent for make.fun's "Sum up 23 November's world news in one image" bounty, $100 in USDC.

## The image

The front page leads with **COP31 COLLAPSES** — the UN climate summit in Turkey failed to agree a fossil-fuel phase-out — alongside three more ships struck in the Strait of Hormuz, student-led protests sweeping Europe, Ukraine retaking 200 sq km near Kharkiv, and markets rebounding after a selloff.

![entry](entry.png)

## The stories on the page

1. **COP31 COLLAPSES** — the UN climate summit in Turkey ended with no agreement to phase out coal, oil and gas, leaving the 1.5°C goal in doubt.
2. **SHIPS STRUCK IN HORMUZ** — three more tankers were hit in the Strait of Hormuz as attacks reached their fastest pace since February.
3. **STUDENTS TAKE TO EUROPE'S STREETS** — student-led protests and strikes swept Europe, from Rome to Paris, Berlin and Warsaw.
4. **UKRAINE RETAKES 200 SQ KM** — Ukrainian forces reported liberating about 200 square kilometres near Kharkiv in operation "Bear Trap".
5. **MARKETS REBOUND AFTER SELLOFF** — stocks recovered after the previous week's rout.

## How it works

`main.py` copies the bundled `entry.png` (1024x1024, under 1 MiB) to `/output/entry.png` and verifies the copy byte-for-byte with SHA-256. No network, no randomness: two runs write identical bytes.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
