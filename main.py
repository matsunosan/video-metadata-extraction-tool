import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pymediainfo import MediaInfo
import os

def extract_metadata(file_path):
    try:
        media_info = MediaInfo.parse(file_path)
        metadata_text = ""
        for track in media_info.tracks:
            metadata_text += f"Track type: {track.track_type}\n"
            for key, value in track.to_data().items():
                metadata_text += f"{key}: {value}\n"
            metadata_text += "\n"
        metadata_display.delete(1.0, tk.END)
        metadata_display.insert(tk.END, metadata_text)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract metadata: {str(e)}")

def open_file_dialog():
    file_path = filedialog.askopenfilename(
        filetypes=[("Video files", "*.mp4 *.mov *.avi *.wmv *.mkv")]
    )
    if file_path:
        extract_metadata(file_path)

def save_metadata():
    metadata_text = metadata_display.get(1.0, tk.END)
    if not metadata_text.strip():
        messagebox.showwarning("No Data", "No metadata to save.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if save_path:
        try:
            with open(save_path, "w") as file:
                file.write(metadata_text)
            messagebox.showinfo("Saved", f"Metadata saved successfully at {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save metadata: {str(e)}")

app = tk.Tk()
app.title("Video Metadata Extractor")

# Змінюємо розмір вікна та додаємо стилізацію
app.geometry("800x600")
app.configure(bg="#2d2d2d")

open_button = tk.Button(app, text="Open Video File", command=open_file_dialog, bg="#4CAF50", fg="white", padx=10, pady=5)
open_button.pack(pady=10)

metadata_display = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=25, bg="#1e1e1e", fg="white", insertbackground="white", padx=10, pady=5)
metadata_display.pack(pady=10, fill=tk.BOTH, expand=True)

save_button = tk.Button(app, text="Save Metadata", command=save_metadata, bg="#2196F3", fg="white", padx=10, pady=5)
save_button.pack(pady=10)

app.mainloop()
