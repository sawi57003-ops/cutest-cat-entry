# Cutest Cat — make.fun `cutest-cat-01`

Entry for the make.fun bounty **"Draw the cutest cat"** ($100, top 3 share:
1st $50, 2nd $30, 3rd $20).

The picture is a hand-drawn style illustration of an orange kitten with big
eyes, drawn in the spirit of the Puss-in-Boots avatar on the bounty card.

## How it works

- `cat.png` — the picture (1024x1024 PNG, 662,389 bytes, under the 1 MiB cap).
- `main.py` — copies `cat.png` byte-for-byte to `/output/entry.png`.
  No network, no randomness, no timestamps: two runs write identical bytes.

## Verify determinism

```sh
python3 main.py /tmp/out1/entry.png
python3 main.py /tmp/out2/entry.png
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png cat.png
```

All three hashes must match.

## License

MIT — see `LICENSE`.
