import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ===== User credentials =====
USERNAME = "kunal"
PASSWORD = "1234"

# ===== Custom Colors and Styles =====
bg_color = "#1e1e2f"
fg_color = "#ffffff"
button_color = "#4caf50"
highlight_color = "#03dac5"
font_header = ("Helvetica", 18, "bold")
font_text = ("Helvetica", 12)

# ====== Splash Screen ======
def splash_screen():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.configure(bg=bg_color)
    width, height = 500, 300
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    splash.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(splash, text="Smart Student Dashboard", font=("Helvetica", 20, "bold"), bg=bg_color, fg=highlight_color)
    label.pack(expand=True)

    splash.after(2000, splash.destroy)  # 2 seconds delay
    splash.mainloop()

# ====== Main Dashboard Window ======
def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Smart Student Dashboard")
    dashboard.configure(bg=bg_color)
    dashboard.geometry("600x500")

    tk.Label(dashboard, text="Welcome to Smart Student Dashboard", bg=bg_color, fg=highlight_color, font=font_header).pack(pady=20)

    # DSA LAB
    def dsa_lab():
        win = tk.Toplevel(dashboard)
        win.title("DSA Lab")
        win.configure(bg="#263238")
        tk.Label(win, text="DSA Topics", font=font_header, fg=highlight_color, bg="#263238").pack(pady=20)
        tk.Label(win, text="🔹 Sorting Algorithms\n🔹 Linked Lists\n🔹 Stack, Queue", font=font_text, bg="#263238", fg="white").pack(pady=10)

    # DIGITAL LOGIC LAB
    def logic_lab():
        win = tk.Toplevel(dashboard)
        win.title("Digital Logic Design Lab")
        win.configure(bg="#1b1f22")
        tk.Label(win, text="Digital Logic Topics", font=font_header, fg="#ffd600", bg="#1b1f22").pack(pady=20)
        tk.Label(win, text="🔹 AND, OR, NOT gates\n🔹 Flip-flops\n🔹 Karnaugh maps", font=font_text, bg="#1b1f22", fg="white").pack(pady=10)

    # SECURE TRANSACTION LAB
    def secure_lab():
        win = tk.Toplevel(dashboard)
        win.title("Secure Transaction Lab")
        win.configure(bg="#1a237e")
        tk.Label(win, text="Secure Transaction Topics", font=font_header, fg="#ffccbc", bg="#1a237e").pack(pady=20)
        tk.Label(win, text="🔹 OTP Verification\n🔹 Basic Encryption\n🔹 Secure login system", font=font_text, bg="#1a237e", fg="white").pack(pady=10)

    # DATA VISUALIZATION LAB
    def data_viz_lab():
        win = tk.Toplevel(dashboard)
        win.title("Data Visualization Lab")
        win.configure(bg="#004d40")
        tk.Label(win, text="Data Visualization", font=font_header, fg="#00e676", bg="#004d40").pack(pady=20)

        # Chart
        fig = plt.Figure(figsize=(4, 3), dpi=100)
        ax = fig.add_subplot(111)
        subjects = ['DSA', 'Logic', 'Secure', 'Viz']
        scores = [80, 70, 90, 85]
        ax.bar(subjects, scores, color='#80deea')
        ax.set_title("Lab Performance")

        chart = FigureCanvasTkAgg(fig, master=win)
        chart.get_tk_widget().pack()

    # Buttons
    style = {"bg": button_color, "fg": "white", "activebackground": "#81c784", "font": font_text, "width": 30}

    tk.Button(dashboard, text="DSA Lab", command=dsa_lab, **style).pack(pady=10)
    tk.Button(dashboard, text="Digital Logic Design Lab", command=logic_lab, **style).pack(pady=10)
    tk.Button(dashboard, text="Secure Transaction Lab", command=secure_lab, **style).pack(pady=10)
    tk.Button(dashboard, text="Data Visualization Lab", command=data_viz_lab, **style).pack(pady=10)
    tk.Button(dashboard, text="Exit", command=dashboard.destroy, bg="#b71c1c", fg="white", font=font_text, activebackground="#f44336", width=30).pack(pady=30)

    dashboard.mainloop()

# ====== Login Page ======
def login_page():
    login = tk.Tk()
    login.title("Login")
    login.configure(bg=bg_color)
    login.geometry("400x300")

    tk.Label(login, text="Student Login", font=font_header, fg=highlight_color, bg=bg_color).pack(pady=20)

    tk.Label(login, text="Username", bg=bg_color, fg="white", font=font_text).pack()
    username_entry = tk.Entry(login, font=font_text)
    username_entry.pack()

    tk.Label(login, text="Password", bg=bg_color, fg="white", font=font_text).pack()
    password_entry = tk.Entry(login, show="*", font=font_text)
    password_entry.pack()

    def validate_login():
        if username_entry.get() == USERNAME and password_entry.get() == PASSWORD:
            login.destroy()
            open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    tk.Button(login, text="Login", command=validate_login, bg=button_color, fg="white", font=font_text, activebackground="#388e3c", width=20).pack(pady=20)

    login.mainloop()

# ==== Run App ====
splash_screen()
login_page()