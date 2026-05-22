# Flask To-Do List Web Application

A full-stack Python web application engineered with Flask to create, track, edit, and manage task lists through a browser interface.

## Features

- **Full Lifecycle Task Management**: Add new items, update text on existing items, toggle completion states, and wipe out entries.
- **Form Input Interception**: Rejects whitespace and empty submissions to prevent broken entries.
- **RESTful Pattern Architecture**: Separates mutation pathways cleanly across explicit POST-based endpoint targets (`/checked/<id>`, `/delete/<id>`, `/edit/<id>`).

## Prerequisites

- Python 3.x
- Flask Framework

```bash
pip install flask
```

## Project Directory Structure

Ensure your folder architecture matches this layout before running:
```text
├── main.py
└── templates/
    └── index.html
```

## How to Run

1. Save the code to a file named `main.py`.
2. Ensure your matching template file resides at `templates/index.html`.
3. Boot the local development server:
   ```bash
   python main.py
   ```
4. Open your web browser and navigate to: `http://127.0.0`

## Technical Details

- **Memory State Engine**: Retains structural dictionary nodes inside an internal variable list during engine runtime execution.
- **Form Handling Data Bindings**: Extracts incoming browser text elements safely using key-indexed standard lookups against the `request.form` mapping payload.
