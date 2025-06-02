# NUM IT Support Ticket System

![image](https://github.com/user-attachments/assets/48b629e5-3b26-4aca-8200-dfe18c00698d)
![image](https://github.com/user-attachments/assets/4f0142c4-5467-4f23-b4b1-941569c1458d)


A desktop application for the National Union of Mineworkers (NUM) to log, manage, and resolve IT support requests. Built with Python and Tkinter, using SQLite for data storage.

## Features
- Submit IT support tickets with employee details, department, and issue description
- Admin view to see, update, and delete tickets
- Status management (Pending, Resolved, High Priority)
- Simple, modern Tkinter GUI
- Data stored locally in `support_db.sqlite`

## Screenshots
*(Add screenshots here if available)*

## Getting Started

### Prerequisites
- Python 3.8 or higher (recommended)
- Tkinter (usually included with Python)

### Installation
1. Clone this repository or download the source code.
2. Ensure you have Python installed.
3. (Optional) Create a virtual environment:
   ```powershell
   python -m venv env
   .\env\Scripts\Activate
   ```
4. Install dependencies (if any):
   ```powershell
   pip install -r requirements.txt
   ```
   *(No external dependencies required for basic usage)*

### Running the Application
```powershell
python main.py
```

### Packaging as an Executable
This project includes a `main.spec` file for use with PyInstaller. To build a standalone Windows executable:
```powershell
pip install pyinstaller
pyinstaller main.spec
```
The executable will be in the `dist/` folder.

## Project Structure
- `main.py` - Main application code
- `support_db.sqlite` - SQLite database file
- `main.spec` - PyInstaller spec file
- `NUM Logo.ico` - Application icon

## Customization
- Departments can be edited in the `departments` list in `main.py`.
- Status options can be changed in the `status_options` list.

## License
---
*Developed as part of a Work Integrated Learning project.*
