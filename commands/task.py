"""Creates a new task in the tracker and Asana."""

from classes import Task, Tracker, Event
from datetime import datetime
from dotenv import load_dotenv
from gspread_formatting import *
import click
import gspread
import os

load_dotenv()

@click.command()
@click.argument("name")
@click.argument("main_type")
@click.argument("start_date")
@click.argument("due_date")
@click.argument("hours")
@click.option("--priority", "-p", default=len(Task.priorities) + 1, help="Numerical rank of priority")
@click.option("--sub_type", "-s", default="", help="Milestone, Task, Cancelled, Define, Measure, Analyze, Improve, Control")
@click.option("--responsible", "-r", default="Ben K", help="Name of responsible person")

def check_priorities():
    pass

def check_hours():
    pass

def create_task():
    task = Task(name, main_type, start_date, due_date, priority, sub_type, responsible, hours)
    task.add_to_tracker(name, start_date, due_date, priority, main_type, sub_type, responsible, hours)
    task.add_to_asana(name, start_date, due_date, priority, main_type, sub_type, responsible, hours)
    task.add_to_calendar(start_date, due_date, hours)

if __name__ == "__main__":
    create_task()