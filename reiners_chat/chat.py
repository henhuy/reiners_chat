import os
import json
import webbrowser
import tkinter as tk


CHATFILE = os.environ.get(
    "REINERS_CHATFILE", os.path.expanduser("~/.python_local/reiners_chat.json")
)


def get_chats():
    if not os.path.exists(CHATFILE):
        raise FileNotFoundError(
            f"Cannot find chat file at {CHATFILE}. You can adapt file location using env var 'REINERS_CHATFILE'."
        )
    with open(CHATFILE) as json_file:
        return json.load(json_file)


def open_chat(chat_name):
    webbrowser.open(CHATS[chat_name], new=1)


def to_clipboard(window, chat_name: str):
    window.clipboard_append(CHATS[chat_name])


CHATS = get_chats()


def run():
    # Creating tkinter window
    window = tk.Tk()
    window.title("RLI Chats")

    tk.Label(window, text="List of chats:").grid(column=0, row=0)

    for i, chat in enumerate(CHATS):
        submit_button = tk.Button(
            window, text=chat, command=lambda name=chat: open_chat(name), width=30
        )
        submit_button.grid(column=0, row=i + 1)
        copy_button = tk.Button(
            window, text="Copy", command=lambda name=chat: to_clipboard(window, name), width=5
        )
        copy_button.grid(column=1, row=i + 1)

    window.mainloop()


if __name__ == "__main__":
    run()
