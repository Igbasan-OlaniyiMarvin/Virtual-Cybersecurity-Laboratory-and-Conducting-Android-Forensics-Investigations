import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import webbrowser  # ✅ For clickable link

DB_PATH = "sample_sms.db"

# Unified data fetcher
def fetch_data(query, params=None):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        return cursor.fetchall()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []
    finally:
        conn.close()

# Populate any tree widget
def populate_tree(tree, columns, data):
    tree.delete(*tree.get_children())
    for i, row in enumerate(data, 1):
        tree.insert("", "end", values=(i,) + row)

def export_data(data, headers):
    if not data:
        messagebox.showinfo("Export", "No data to export.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data)
        messagebox.showinfo("Export", f"Data exported to {file_path}")

# GUI Setup
root = tk.Tk()
root.title("Android Forensics Dashboard")
root.geometry("900x600")
root.configure(bg="#e6f2ff")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#f5faff", fieldbackground="#f5faff", foreground="black")
style.configure("TNotebook.Tab", padding=[10, 5])
style.map("TNotebook.Tab", background=[("selected", "#cce6ff")])

# Notebook Tabs
tabs = ttk.Notebook(root)
tabs.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

### --- SMS TAB ---
sms_tab = ttk.Frame(tabs)
tabs.add(sms_tab, text="📨 SMS Viewer")

sms_columns = ("#", "Sender", "Date", "Message")
sms_tree = ttk.Treeview(sms_tab, columns=sms_columns, show="headings")
for col in sms_columns:
    sms_tree.heading(col, text=col)
    sms_tree.column(col, anchor=tk.W, width=150 if col == "Message" else 120)
sms_tree.pack(fill=tk.BOTH, expand=True, pady=5)

sms_filter_frame = ttk.Frame(sms_tab)
sms_filter_frame.pack(fill=tk.X, padx=10, pady=5)
ttk.Label(sms_filter_frame, text="Filter by Number:").pack(side=tk.LEFT)
sms_filter_entry = ttk.Entry(sms_filter_frame, width=20)
sms_filter_entry.pack(side=tk.LEFT, padx=5)

def filter_sms():
    number = sms_filter_entry.get().strip()
    query = "SELECT address, date, body FROM sms WHERE address = ?" if number else "SELECT address, date, body FROM sms"
    params = (number,) if number else None
    data = fetch_data(query, params)
    populate_tree(sms_tree, sms_columns, data)

ttk.Button(sms_filter_frame, text="Apply Filter", command=filter_sms).pack(side=tk.LEFT, padx=5)
ttk.Button(sms_filter_frame, text="Clear", command=lambda: populate_tree(sms_tree, sms_columns, fetch_data("SELECT address, date, body FROM sms"))).pack(side=tk.LEFT)
ttk.Button(sms_filter_frame, text="Export CSV", command=lambda: export_data(fetch_data("SELECT address, date, body FROM sms"), ["Sender", "Date", "Message"])).pack(side=tk.RIGHT)

populate_tree(sms_tree, sms_columns, fetch_data("SELECT address, date, body FROM sms"))

### --- CALL LOG TAB ---
call_tab = ttk.Frame(tabs)
tabs.add(call_tab, text="📞 Call Logs")

call_columns = ("#", "Number", "Type", "Duration", "Date")
call_tree = ttk.Treeview(call_tab, columns=call_columns, show="headings")
for col in call_columns:
    call_tree.heading(col, text=col)
    call_tree.column(col, anchor=tk.W, width=120)
call_tree.pack(fill=tk.BOTH, expand=True, pady=5)

ttk.Button(call_tab, text="Load Call Logs", command=lambda: populate_tree(
    call_tree, call_columns,
    fetch_data("SELECT number, type, duration, date FROM call_logs")
)).pack(side=tk.LEFT, padx=10, pady=5)

ttk.Button(call_tab, text="Export CSV", command=lambda: export_data(
    fetch_data("SELECT number, type, duration, date FROM call_logs"),
    ["Number", "Type", "Duration", "Date"]
)).pack(side=tk.LEFT, padx=10)

### --- BROWSER HISTORY TAB ---
browser_tab = ttk.Frame(tabs)
tabs.add(browser_tab, text="🌐 Browser History")

browser_columns = ("#", "URL", "Title", "Visit Time")
browser_tree = ttk.Treeview(browser_tab, columns=browser_columns, show="headings")
for col in browser_columns:
    browser_tree.heading(col, text=col)
    browser_tree.column(col, anchor=tk.W, width=180 if col == "URL" else 140)
browser_tree.pack(fill=tk.BOTH, expand=True, pady=5)

ttk.Button(browser_tab, text="Load History", command=lambda: populate_tree(
    browser_tree, browser_columns,
    fetch_data("SELECT url, title, visit_time FROM browser_history")
)).pack(side=tk.LEFT, padx=10, pady=5)

ttk.Button(browser_tab, text="Export CSV", command=lambda: export_data(
    fetch_data("SELECT url, title, visit_time FROM browser_history"),
    ["URL", "Title", "Visit Time"]
)).pack(side=tk.LEFT, padx=10)

### --- Clickable Link (PDF Report) ---
def open_report(event):
    webbrowser.open_new("file:///C:/Users/YourName/Documents/Final_Cybersecurity_Project_Report.pdf")  # Update path

report_link = tk.Label(root, text="📄 Click here to open the final report (PDF)", fg="blue", cursor="hand2", bg="#e6f2ff", font=('Arial', 10, 'underline'))
report_link.pack(side=tk.BOTTOM, pady=10)
report_link.bind("<Button-1>", open_report)

root.mainloop()
