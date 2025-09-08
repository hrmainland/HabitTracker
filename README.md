# Habit Tracker

A command-line habit tracking application that leverages the [Pixela API](https://pixe.la/) to create beautiful GitHub-style contribution graphs for personal habit monitoring and visualization.

<img width="672" alt="Habit tracking graph visualization" src="https://user-images.githubusercontent.com/1097533/47780099-0e27cb80-dd3e-11e8-87ef-426bb7cfc76c.png">

## Overview

This application provides a streamlined interface for logging daily habits through terminal commands and visualizing progress through pixel-based contribution graphs. The system supports multiple habit types and includes mobile notification capabilities through Pushover integration.

## Features

- **Command-line Interface**: Simple terminal-based habit logging with intuitive argument parsing
- **Visual Progress Tracking**: GitHub-style contribution graphs powered by the Pixela API
- **Multiple Habit Support**: Track various activities including meditation, exercise, reading, and more
- **Mobile Notifications**: Push notifications via [Pushover](https://pushover.net/) integration
- **Flexible Date Entry**: Support for retroactive logging with relative date specifications
- **Automated Data Management**: Streamlined data upload and synchronization with Pixela

## Architecture

The application is structured into modular components:

- `Pixela/` - Core API integration and data management
- `Pushover/` - Mobile notification system
- `log_habits.py` - Primary habit logging interface
- `update_files.py` - Data synchronization utilities
- `draft_report.py` - Reporting functionality

## Usage

Habit data is uploaded via the terminal using a simple command structure where arguments are passed as strings, decoded, and transmitted to the Pixela API.

### Example Commands

```bash
# Log activities for today
python log_habits.py med 2 run 1

# Log retroactive entries
python log_habits.py -2 med 3 run yesterday med read 2 tod run
```

This example logs:
- Two days ago: 3 meditation sessions and 1 run
- Yesterday: 1 meditation session and 1 reading session  
- Today: 1 run

## Supported Habits

The system includes predefined habit types with associated time values:
- Meditation (`med`): 30 minutes per session
- Journaling (`jrn`): 10 minutes per session
- Sleep tracking (`sleep`): 10-hour blocks
- Web development (`web`): 30 minutes per session
- Exercise (`ex`): 45 minutes per session
- Computer Science study (`cs`): 30 minutes per session

## Requirements

- Python 3.x
- Active Pixela account and API credentials
- Pushover account (optional, for notifications)

## Configuration

Set up your API credentials and configure habit definitions through the provided configuration modules in the `Pixela/` directory.
