import tkinter as tk
from tkinter import ttk, messagebox
import database

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Desktop Management Tool")
        self.root.geometry("800x500")

        database.create_tables()

        self.tabControl = ttk.Notebook(self.root)
        self.tab_catalog = ttk.Frame(self.tabControl)
        self.tab_feedback = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab_catalog, text="Book Catalog")
        self.tabControl.add(self.tab_feedback, text="User Reviews")
        self.tabControl.pack(expand=1, fill="both", padx=10, pady=10)

        self.build_catalog_tab()
        self.build_feedback_tab()

    def build_catalog_tab(self):
        self.tree = ttk.Treeview(self.tab_catalog, columns=("ID", "ISBN", "Title", "Author", "Copies"), show="headings")
        for col in ("ID", "ISBN", "Title", "Author", "Copies"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)
        self.load_books()

    def load_books(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in database.search_books():
            self.tree.insert("", "end", values=(book['id'], book['isbn'], book['title'], book['author'], book['copies']))

    def build_feedback_tab(self):
        self.tree_fb = ttk.Treeview(self.tab_feedback, columns=("User", "Book", "Rating", "Comments"), show="headings")
        for col in ("User", "Book", "Rating", "Comments"):
            self.tree_fb.heading(col, text=col)
        self.tree_fb.pack(fill="both", expand=True, padx=5, pady=5)
        self.load_feedback()

    def load_feedback(self):
        for row in self.tree_fb.get_children():
            self.tree_fb.delete(row)
        for fb in database.get_all_feedback():
            self.tree_fb.insert("", "end", values=(fb['user_name'], fb['book_title'], f"{fb['rating']} Stars", fb['comments']))

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()