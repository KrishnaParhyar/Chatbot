import tkinter as tk
import google.generativeai as genai

genai.configure(api_key="your-api-key-here")
model = genai.GenerativeModel('models/gemini-1.5-flash')

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_window.config(state=tk.NORMAL) 
    chat_window.insert(tk.END, f"You: {user_input}\n", 'user')
    entry.delete(0, tk.END)

    try:
        response = model.generate_content(user_input)
        chat_window.insert(tk.END, f"Bot: {response.text}\n", 'bot')
    except Exception as e:
        chat_window.insert(tk.END, f"Error: {e}\n", 'error')

    chat_window.config(state=tk.DISABLED)  
    chat_window.yview(tk.END)  

root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x650")
root.configure(bg="#f7f7f7")

header = tk.Label(root, text="AI Chatbot", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", pady=10)
header.pack(fill=tk.X)

chat_window = tk.Text(root, bg="#FFFFFF", fg="#333333", font=("Helvetica", 12), wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


scrollbar = tk.Scrollbar(chat_window, command=chat_window.yview)
chat_window.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

entry = tk.Entry(root, font=("Helvetica", 14), bg="#f1f1f1", borderwidth=2, relief="solid")
entry.pack(padx=10, pady=(0, 10), fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message, font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
send_button.pack(pady=(0, 10))

chat_window.tag_config('user', foreground='#4CAF50', font=("Helvetica", 12, "bold"))
chat_window.tag_config('bot', foreground='#0288d1', font=("Helvetica", 12, "italic"))
chat_window.tag_config('error', foreground='red', font=("Helvetica", 12, "bold"))

root.mainloop()
