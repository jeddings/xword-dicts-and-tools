# xword-dicts-and-tools

A collection of scored word list dictionaries and scripts for crossword puzzle construction. Tools for searching, filtering, combining, and transforming `.dict` files — the scored word lists used by crossword software like Crossfire and XWord Info.

## Dictionary format

Most `.dict` files are semicolon-delimited:

```
WORD;SCORE
```

- **WORD** — the entry (uppercase letters, no spaces/punctuation in the grid)
- **SCORE** — integer, typically 0–100; higher = more desirable crossword fill

CSV files follow the same convention and are interchangeable with most scripts.

## Repository structure

```
xword-dicts-and-tools/
├── scripts/                        # All utility scripts
│   ├── *.py                        # Python scripts (see below)
│   ├── *.js / *.sh / *.R / *.awk   # JS, shell, R, and awk utilities
│   ├── cfp-to-puz-txt.xslt         # XSLT transform for puzzle format conversion
│   └── check-existence/            # Node.js word-lookup module
├── dictionaries/                   # Scored word lists
│   ├── *.dict                      # Root-level curated dictionaries
│   ├── Locations/                  # City and place name lists
│   ├── People/                     # Celebrity, athlete, author name lists
│   ├── WordLists/                  # Frequency and ngram-based lists
│   └── Idioms/                     # Idiomatic expressions
└── data/                           # Tabular data files
    ├── default.csv
    ├── chris-jones.csv
    └── phrases.xlsx
```

## Scripts

### Word search

| Script | Description |
|--------|-------------|
| `find_words.py` | Search for words matching a pattern across dict files; outputs results as CSV with timestamps |
| `findprefix.py` | Find all entries with a given prefix across all dicts; use `--dict-dir` to specify the directory |
| `findsuffix.py` | Find all entries with a given suffix across all dicts; use `--dict-dir` to specify the directory |
| `findregex.py` | Regex search across dicts; supports `$v` (vowel) and `$c` (consonant) shorthands; use `--dict-file` to specify the file |
| `find_substring.py` | Find entries containing a given substring |
| `find_consecutive_consonants.py` | Find entries with N or more consecutive consonants |
| `find_occurrence.py` | Find occurrence/frequency of specific words |
| `drop_and_pair.py` | Find word pairs where one is a subset/transform of the other; use `--dict-file` and `--min-score` options |
| `backwards.js` | Prototype: find words that spell other words in reverse |
| `check-existence.js` / `check-existence.sh` | Check whether specific words exist in any dict file |

### Dictionary manipulation

| Script | Description |
|--------|-------------|
| `combine-dict.py` | Merge multiple dict files into one, resolving duplicates |
| `filter-scores.py` | Filter and normalize scores across dict files (adjusts scores relative to max) |
| `sort_and_strip.py` | Sort a dict file and strip accent characters |
| `replace_similar.py` | Normalize similar-looking characters (accent stripping, unicode cleanup) |
| `dedup.awk` | Deduplicate lines in a dict file (awk one-liner) |
| `two-letter-combos.py` | Generate two-letter combination word entries |

### Format conversion

| Script | Description |
|--------|-------------|
| `convert-cfp-to-puz-txt.py` | Convert CrossFire `.cfp` puzzle files to plain text |
| `cfp-to-puz-txt.xslt` | XSLT stylesheet used by the CFP converter |
| `convert-encoding.sh` | Convert file character encoding |

### Data generation

| Script | Description |
|--------|-------------|
| `create-ngrams.R` | Build ngram frequency lists from a corpus |
| `fast-ngrams.R` | Faster ngram generation (optimized version) |
| `pluralize.py` | Generate plural forms of noun phrases from a dict file (uses TextBlob) |
| `mlconjug3_test.py` | Explore verb conjugation forms via mlconjug3 |

### Utilities

| Script | Description |
|--------|-------------|
| `high-match.sh` | Shell script to surface high-scoring matching entries |

## Key dictionaries

| File | Description |
|------|-------------|
| `default.dict` | Base working word list |
| `default-adjusted.dict` | Default list with manually tuned scores |
| `peter_broda_stripped.dict` | Peter Broda's scored word list |
| `peter_broda_adjusted_scores.dict` | Broda list with score adjustments |
| `all-scored-high.dict` | High-scoring entries merged across sources |
| `maiamcc.dict` | Maia Marinaccio's crossword word list |
| `chris_jones.dict` / `chris-jones-adjusted.dict` | Chris Jones list (original and adjusted) |
| `nyt_2019-05-02.dict` | NYT-derived word list |
| `spreadthewordlist_sorted.dict` | Spread the Word List, sorted |
| `wiki-ranked.dict` / `wiki-top-ranked.dict` | Wikipedia-derived ranked entries |
| `famous_names.dict` / `famous-people.dict` | Proper name lists |
| `phrasal-verbs.dict` | Phrasal verb entries |
| `english-phrases.dict` / `phrases-merged.dict` | Common English phrase lists |
| `slang-dictionary.dict` | Slang and informal entries |
| `m-w.dict` | Merriam-Webster derived list |
| `oed-new-words-*.dict` | OED new word additions by date |

## Notes

- Files ending in `~` or `.bak` are editor backups — excluded from this repo
- `words.db` (SQLite, 200MB+) is excluded due to GitHub's file size limit; use it locally or via Git LFS
- `Working/`, `TempUnused/`, and `Backup/` directories are excluded (in-progress and archived material)
