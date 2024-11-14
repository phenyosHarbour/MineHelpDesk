MineHelpDesk

MineHelpDesk is a demo IT support ticket management application, initially designed for a trade union, but adaptable for broader company needs. This proof-of-concept version includes limited features and configurations to demonstrate basic functionality. Future adaptations could expand this to a fully configurable IT support tool for any organization.

Features

Ticket Submission: Employees can submit IT support tickets by entering key details like name, department, workstation, and a description of the issue.

Admin Panel: Admins can review submitted tickets, update their status, and delete resolved tickets.

Status Management: Tickets can be marked as "Pending," "Resolved," or "High Priority" for streamlined support handling.

SQLite Database: Uses a simple SQLite database to store and manage ticket data.

Basic UI: Built with Tkinter, providing a straightforward user interface for basic operations.

Limitations

This application is a limited-feature demo designed for demonstration purposes only:

Reduced Functionality: Lacks the advanced features typical of enterprise-level helpdesk software.

Simplified Database: Uses SQLite for simplicity, without robust security or advanced data handling.

Basic UI: Limited user interface design without customization options or user authentication.

Getting Started

Requirements

Python 3.x should be installed on your system.

Tkinter library (usually included with Python).

Installation & Setup

Clone or download this repository.

Place the support_db.sqlite database file in the same directory as main.exe.

Run the executable file (main.exe) to launch the application.

Usage

Employee Mode: Employees can submit IT tickets by filling out the form and clicking "Submit Ticket."

Admin Mode: Admins can access the "View Tickets" feature to manage tickets, update statuses, or remove resolved tickets.

Future Development

This application has the potential for future customization to suit a range of business environments. While currently limited, additional features and configurations can be added to meet specific organizational requirements, transforming it into a versatile IT support tool for any company.

Disclaimer

This application is provided as a demo and should not be considered a complete, production-ready solution. Its limited functionalities and configurations do not represent a fully-deployed IT support software product. Instead, this project serves as a foundational base, intended to visualize what a fully-developed application could achieve.

Investigation

The main components of the MineHelpDesk application are:

* **Ticket submission**: Employees can submit IT support tickets by entering key details like name, department, workstation, and a description of the issue. 📝
* **Admin panel**: Admins can review submitted tickets, update their status, and delete resolved tickets. 🛠️
* **Status management**: Tickets can be marked as "Pending," "Resolved," or "High Priority" for streamlined support handling. 📊
* **SQLite database**: Uses a simple SQLite database to store and manage ticket data. 🗄️
* **Basic UI**: Built with Tkinter, providing a straightforward user interface for basic operations. 🖥️
