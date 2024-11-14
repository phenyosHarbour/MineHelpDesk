import tkinter as tk
import sqlite3
import os

def initialize_db():
    conn = sqlite3.connect('support_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            workstation TEXT,
            description TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def submit_ticket(name, department, workstation, description):
    conn = sqlite3.connect('support_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tickets (name, department, workstation, description, status)
        VALUES (?, ?, ?, ?, 'Pending')
    ''', (name, department, workstation, description))
    conn.commit()
    conn.close()

def update_ticket_status(ticket_id, status):
    conn = sqlite3.connect('support_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tickets
        SET status = ?
        WHERE id = ?
    ''', (status, ticket_id))
    conn.commit()
    conn.close()

def delete_ticket(ticket_id):
    conn = sqlite3.connect('support_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM tickets
        WHERE id = ?
    ''', (ticket_id,))
    conn.commit()
    conn.close()

class TicketSubmissionForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        self.department_label = tk.Label(self, text="Department")
        self.department_label.grid(row=1, column=0)
        self.department_entry = tk.Entry(self)
        self.department_entry.grid(row=1, column=1)

        self.workstation_label = tk.Label(self, text="Workstation")
        self.workstation_label.grid(row=2, column=0)
        self.workstation_entry = tk.Entry(self)
        self.workstation_entry.grid(row=2, column=1)

        self.description_label = tk.Label(self, text="Description")
        self.description_label.grid(row=3, column=0)
        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(self, text="Submit Ticket", command=self.submit_ticket)
        self.submit_button.grid(row=4, column=0, columnspan=2)

    def submit_ticket(self):
        name = self.name_entry.get()
        department = self.department_entry.get()
        workstation = self.workstation_entry.get()
        description = self.description_entry.get()
        submit_ticket(name, department, workstation, description)
        self.master.switch_to_admin_panel()

class AdminPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.ticket_list = tk.Listbox(self)
        self.ticket_list.grid(row=0, column=0, columnspan=2)
        self.load_tickets()

        self.update_button = tk.Button(self, text="Update Status", command=self.update_status)
        self.update_button.grid(row=1, column=0)

        self.delete_button = tk.Button(self, text="Delete Ticket", command=self.delete_ticket)
        self.delete_button.grid(row=1, column=1)

    def load_tickets(self):
        conn = sqlite3.connect('support_db.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, status FROM tickets')
        tickets = cursor.fetchall()
        conn.close()

        self.ticket_list.delete(0, tk.END)
        for ticket in tickets:
            self.ticket_list.insert(tk.END, f"ID: {ticket[0]}, Name: {ticket[1]}, Status: {ticket[2]}")

    def update_status(self):
        selected_ticket = self.ticket_list.get(tk.ACTIVE)
        ticket_id = int(selected_ticket.split(",")[0].split(":")[1].strip())
        new_status = tk.simpledialog.askstring("Update Status", "Enter new status:")
        if new_status:
            update_ticket_status(ticket_id, new_status)
            self.load_tickets()

    def delete_ticket(self):
        selected_ticket = self.ticket_list.get(tk.ACTIVE)
        ticket_id = int(selected_ticket.split(",")[0].split(":")[1].strip())
        delete_ticket(ticket_id)
        self.load_tickets()

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MineHelpDesk")
        self.geometry("400x300")
        self.switch_to_ticket_submission()

    def switch_to_ticket_submission(self):
        self.clear_frame()
        self.ticket_submission_form = TicketSubmissionForm(self)
        self.ticket_submission_form.pack()

    def switch_to_admin_panel(self):
        self.clear_frame()
        self.admin_panel = AdminPanel(self)
        self.admin_panel.pack()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    initialize_db()
    app = MainApplication()
    app.mainloop()
