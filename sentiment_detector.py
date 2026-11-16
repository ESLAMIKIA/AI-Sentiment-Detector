# AI Sentiment Detector
# Install once: pip install textblob
# Run: python sentiment_detector.py

import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

def analyze_sentiment():
    text = text_input.get("1.0", tk.END).strip()

    if not text:
        messagebox.showinfo("Empty text", "Please enter a sentence first.")
        return

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        mood = "POSITIVE"
        emoji = "😊"
        color = "#22c55e"
        description = "This text expresses a positive feeling."
    elif polarity < -0.1:
        mood = "NEGATIVE"
        emoji = "😠"
        color = "#ef4444"
        description = "This text expresses a negative feeling."
    else:
        mood = "NEUTRAL"
        emoji = "😐"
        color = "#eab308"
        description = "This text appears mostly neutral."

    result_label.config(text=f"{emoji}  {mood}", fg=color)
    description_label.config(text=description)
    score_label.config(text=f"Sentiment score: {polarity:.2f}")

def clear_text():
    text_input.delete("1.0", tk.END)
    result_label.config(text="Your result will appear here", fg="#9ca3af")
    description_label.config(text="")
    score_label.config(text="")

root = tk.Tk()
root.title("AI Sentiment Detector")
root.geometry("520x480")
root.resizable(False, False)
root.configure(bg="#111827")

title = tk.Label(
    root, text="AI Sentiment Detector",
    font=("Segoe UI", 22, "bold"),
    bg="#111827", fg="white"
)
title.pack(pady=(28, 5))

subtitle = tk.Label(
    root, text="Enter a sentence and let AI analyze its emotion",
    font=("Segoe UI", 10),
    bg="#111827", fg="#9ca3af"
)
subtitle.pack(pady=(0, 22))

text_input = tk.Text(
    root, height=6, width=48,
    font=("Segoe UI", 12),
    bg="#1f2937", fg="white",
    insertbackground="white",
    relief="flat", padx=12, pady=12,
    wrap="word"
)
text_input.pack(padx=30, fill="x")
text_input.insert("1.0", "I really love this beautiful day!")

button_frame = tk.Frame(root, bg="#111827")
button_frame.pack(pady=18)

analyze_button = tk.Button(
    button_frame, text="Analyze Sentiment",
    command=analyze_sentiment,
    font=("Segoe UI", 11, "bold"),
    bg="#6366f1", fg="white",
    activebackground="#4f46e5",
    activeforeground="white",
    relief="flat", padx=20, pady=10,
    cursor="hand2"
)
analyze_button.pack(side="left", padx=6)

clear_button = tk.Button(
    button_frame, text="Clear",
    command=clear_text,
    font=("Segoe UI", 11),
    bg="#374151", fg="white",
    activebackground="#4b5563",
    activeforeground="white",
    relief="flat", padx=20, pady=10,
    cursor="hand2"
)
clear_button.pack(side="left", padx=6)

result_label = tk.Label(
    root, text="Your result will appear here",
    font=("Segoe UI", 20, "bold"),
    bg="#111827", fg="#9ca3af"
)
result_label.pack(pady=(12, 8))

description_label = tk.Label(
    root, text="",
    font=("Segoe UI", 10),
    bg="#111827", fg="white"
)
description_label.pack()

score_label = tk.Label(
    root, text="",
    font=("Segoe UI", 10),
    bg="#111827", fg="#9ca3af"
)
score_label.pack(pady=8)

footer = tk.Label(
    root, text="Powered by TextBlob • Simple machine learning / NLP",
    font=("Segoe UI", 8),
    bg="#111827", fg="#6b7280"
)
footer.pack(side="bottom", pady=14)

root.mainloop()
