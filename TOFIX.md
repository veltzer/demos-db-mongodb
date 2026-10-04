# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `first_exercise/exercise.txt:30` - tells students to verify the import by running `"show_data.py"`, but the script from the previous phase is `show_all_data.py` (as line 22 correctly says); fix the name.
- `rsconstruct.toml:21` - only `shellcheck` is configured; the four Python scripts in `first_exercise/` are never linted, and there is no `pyproject.toml` declaring their `pymongo` dependency. Add a `pyproject.toml` (bare `pymongo`, ruff in the dev group, `uv.lock`) and a `[processor.ruff]` with `src_dirs = ["first_exercise"]`.

## Low

- `first_exercise/import_csv.py:10` - `open('movies.csv')` is relative to the current directory and has no `encoding`/`newline=''`; `movies.csv` contains non-ASCII text (e.g. `Français`) and quoted fields, so it breaks when run from another directory or under a non-UTF-8 locale. Resolve the path from `__file__` and open with `encoding="utf-8", newline=""`.
- `README.md:2` - the README is a single description line; it does not mention `first_exercise/`, that `start.sh`/`stop.sh` run MongoDB in docker, or that the scripts need `pymongo`. Add a short usage section.
