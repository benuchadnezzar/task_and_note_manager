"""CLI command:Creates a new project tracker in Google Sheets."""

from classes import Tracker
from datetime import datetime
import click
from services.sheet_construct import create_sheet

def get_quarter(week_one: datetime) -> str:
    """Returns the quarter of the fiscal year for a given date."""
    month_number = week_one.month
    year = week_one.year
    if month_number >= 3 and month_number <= 5:
        return f"{year} Q4"
    elif month_number >= 6 and month_number <= 8:
        return f"{year} Q1"
    elif month_number >= 9 and month_number <= 11:
        return f"{year} Q2"
    else:
        return f"{year} Q3"

@click.command()
def create_tracker():
    """Prompts user for week dates and creates a new project tracker in Google Sheets."""
    tracker = Tracker()
    input_date = click.prompt("📅 Input the start date of week 1 as YYYY-MM-DD", type=click.DateTime(formats=["%Y-%m-%d"]))
    tracker.dates.append(input_date.date())
    while click.confirm("Do you still have weeks to add?"):
        input_date = click.prompt("Input your next week:") 
        tracker.dates.append(input_date)
    click.echo("Great! Creating your tracker now.")

    sheet_name = f"{get_quarter(tracker.dates[0])} Project Tracker"
    sh = create_sheet(sheet_name, tracker.dates)
    click.echo(f"✅ All set! Your project tracker is ready at {sh.url}")

if __name__ == "__main__":
    create_tracker()