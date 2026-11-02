# New Jersey Demographic Explorer

An improved version of my original 2024 Python menu-driven demographics project. The program explores age, gender, education, and career estimates for New Jersey using a **CSV data file**, displays estimated population counts, exports a summary CSV, and optionally creates bar charts.

## Features
- Interactive command-line menu with input validation
- CSV-based categories (no need to edit Python code to update percentages)
- Estimated population counts calculated from percentages
- Data-quality checks for percentages that do not total 100%
- CSV summary export
- Optional PNG bar charts with matplotlib
- Automated unit tests

## Run

Python 3.9+ is recommended.

```bash
python3 main.py
```

To export a CSV without opening the interactive menu:

```bash
python3 main.py --export
```

To install the optional chart dependency:

```bash
python3 -m pip install -r requirements.txt
```

To test:

```bash
python3 -m unittest discover -s tests -v
```

## Data limitations (important)

The bundled `data/nj_demographics_2024_original_estimates.csv` uses percentages copied from the **original 2024 student project**, which attributed figures to World Population Review. These figures have **not been independently verified** and should **not** be presented as current official NJ statistics.

The original education percentages total **135.21%** and career percentages total **93.25%**. The education data may contain a typo or inconsistent categories, while career data may omit categories; **they have deliberately not been silently corrected**. The app warns about these issues. Some labels may also overlap or differ in their population denominator. To use this for real analysis, replace the CSV with verified data, clear definitions and source/year metadata (e.g., from the U.S. Census Bureau), and only multiply by the applicable population denominator.

Charts are illustrative views of the provided data; they do not establish data quality.

## File structure

```
main.py
data/nj_demographics_2024_original_estimates.csv
tests/test_demographics.py
requirements.txt
original_project.py
```

## Technologies

Python, CSV (standard library), unittest, Matplotlib (optional).

## Background

Based on a 2024 menu-driven Python project and expanded with CSV input, data validation, testing, exporting, and visualization.
