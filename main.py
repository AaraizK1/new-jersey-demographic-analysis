#!/usr/bin/env python3
"""Interactive New Jersey demographic explorer.

Improves an original 2024 student project with CSV-driven analysis,
validation, optional charts, and summary exports.

IMPORTANT: Bundled figures are historical estimates copied from the original
student project and have NOT been independently verified.
"""

import argparse
import csv
from pathlib import Path

POPULATION_2024 = 9_320_860
DEFAULT_DATA = Path(__file__).parent / "data" / "nj_demographics_2024_original_estimates.csv"
CATEGORIES = ("Age", "Gender", "Education", "Career")


def load_data(path):
    """Load category percentages from CSV and reject invalid rows."""
    records = {category: [] for category in CATEGORIES}
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"category", "group", "percentage"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("CSV requires category, group, percentage columns.")
        for line, row in enumerate(reader, start=2):
            category = row["category"].strip()
            group = row["group"].strip()
            if category not in records:
                raise ValueError(f"Line {line}: unknown category {category!r}")
            if not group:
                raise ValueError(f"Line {line}: missing group name")
            try:
                percent = float(row["percentage"])
            except (TypeError, ValueError):
                raise ValueError(f"Line {line}: invalid percentage") from None
            if not (0 <= percent <= 100):
                raise ValueError(f"Line {line}: percentage outside 0–100")
            if any(existing["group"] == group for existing in records[category]):
                raise ValueError(f"Line {line}: duplicate group {group!r}")
            records[category].append({"group": group, "percentage": percent})
    return records


def estimated_count(percentage, population):
    return round(population * percentage / 100)


def validate_totals(records, tolerance=0.1):
    """Report categories whose percentages do not add up to 100%.

    Assumes categories are intended to be mutually exclusive and exhaustive.
    """
    warnings = []
    for category, entries in records.items():
        if not entries:
            continue
        total = sum(item["percentage"] for item in entries)
        if abs(total - 100) > tolerance:
            warnings.append(
                f"{category} totals {total:.2f}% (not 100%). "
                "Estimates may overlap, omit groups, or contain errors."
            )
    return warnings


def show_category(category, records, population):
    items = records[category]
    if not items:
        print(f"No data available for {category}.")
        return
    print(f"\n{category} | Estimated NJ population: {population:,}")
    print("-" * 65)
    for item in items:
        people = estimated_count(item["percentage"], population)
        print(f"{item['group'][:39]:39} {item['percentage']:6.2f}%  {people:>11,}")
    print("-" * 65)
    print(f"Sum of listed percentages: {sum(i['percentage'] for i in items):.2f}%")


def save_chart(category, records, output_dir):
    """Create a PNG bar chart; matplotlib is optional."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("Charts need matplotlib. Install it using: python3 -m pip install matplotlib")
        return
    items = records[category]
    if not items:
        print("No data to chart.")
        return
    output_dir.mkdir(parents=True, exist_ok=True)
    labels = [item["group"] for item in items]
    percentages = [item["percentage"] for item in items]
    fig, ax = plt.subplots(figsize=(9, max(3.5, len(items) * 0.65)))
    ax.barh(labels, percentages)
    ax.invert_yaxis()
    ax.set_xlabel("Percent (%)")
    ax.set_title(f"New Jersey {category} — original 2024 student estimates (unverified)")
    ax.set_xlim(0, max(100, max(percentages) * 1.1))
    fig.tight_layout()
    path = output_dir / f"{category.lower()}_chart.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    print(f"Saved chart: {path}")


def export_summary(records, population, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "nj_demographic_summary.csv"
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["category", "group", "percentage", "estimated_people"])
        for category, items in records.items():
            for item in items:
                writer.writerow([
                    category, item["group"], item["percentage"],
                    estimated_count(item["percentage"], population),
                ])
    print(f"Saved CSV: {path}")


def menu(records, population, output_dir):
    options = {str(i): category for i, category in enumerate(CATEGORIES, 1)}
    while True:
        print("\nNew Jersey Demographic Explorer")
        print("1. Age  2. Gender  3. Education  4. Career")
        print("5. Save category chart  6. Export CSV summary  7. Check data  0. Exit")
        choice = input("Choose an option: ").strip()
        if choice in options:
            show_category(options[choice], records, population)
        elif choice == "5":
            selected = input("Chart category (Age/Gender/Education/Career): ").strip().title()
            if selected in CATEGORIES:
                save_chart(selected, records, output_dir)
            else:
                print("Unknown category.")
        elif choice == "6":
            export_summary(records, population, output_dir)
        elif choice == "7":
            warnings = validate_totals(records)
            print("\n".join(warnings) if warnings else "All listed category totals are near 100%.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 0–7.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="Input CSV")
    parser.add_argument("--population", type=int, default=POPULATION_2024)
    parser.add_argument("--output-dir", type=Path, default=Path("output"))
    parser.add_argument("--export", action="store_true", help="Export CSV summary without opening menu")
    args = parser.parse_args()
    if args.population <= 0:
        parser.error("--population must be greater than zero")
    try:
        records = load_data(args.data)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print("Data note: bundled percentages are unverified figures from a 2024 student project.")
    for warning in validate_totals(records):
        print("WARNING:", warning)
    if args.export:
        export_summary(records, args.population, args.output_dir)
    else:
        try:
            menu(records, args.population, args.output_dir)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")


if __name__ == "__main__":
    main()
