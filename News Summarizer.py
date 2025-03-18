import tkinter as tk
from tkinter import messagebox
from newspaper import Article
from textblob import TextBlob


def summarize_article():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Input Error", "Please enter a URL.")
        return

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()  # NLP-based summarization

        title = article.title or "N/A"
        author = ", ".join(article.authors) if article.authors else "N/A"
        published_date = article.publish_date.strftime("%Y-%m-%d") if article.publish_date else "N/A"
        summary = article.summary or "Summary not available."

        # Perform sentiment analysis
        blob = TextBlob(summary)
        sentiment = blob.sentiment

        # Display results
        result_text.delete(1.0, tk.END)  # Clear previous results
        result_text.insert(tk.END, f"📌 Title: {title}\n")
        result_text.insert(tk.END, f"📝 Author(s): {author}\n")
        result_text.insert(tk.END, f"📅 Published Date: {published_date}\n\n")
        result_text.insert(tk.END, f"📰 Summary:\n{summary}\n\n")
        result_text.insert(tk.END, f"📊 Sentiment:\n🔹 Polarity: {sentiment.polarity:.2f}\n🔹 Subjectivity: {sentiment.subjectivity:.2f}\n")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def clear_text():
    """Clears the result text box."""
    result_text.delete(1.0, tk.END)

# Set up the GUI
root = tk.Tk()
root.title("📰 News Summarizer")

# URL input
url_label = tk.Label(root, text="Enter Article URL:https://www.indiatoday.in/india/story/clashes-in-nagpur-after-muslim-groups-allege-holy-book-burnt-at-aurangzeb-tomb-protest-2694889-2025-03-17")
url_label.pack()
url_entry = tk.Entry(root, width=60)
url_entry.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

summarize_button = tk.Button(button_frame, text="Summarize", command=summarize_article)
summarize_button.grid(row=0, column=0, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=1, padx=5, pady=5)

# Result text box
result_text = tk.Text(root, wrap=tk.WORD, width=70, height=20)
result_text.pack()

# Start the GUI event loop
root.mainloop()
