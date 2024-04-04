# Quick start

1. Easily install it using [pipx](https://pipx.pypa.io/stable/): `pipx install git+https://github.com/henhuy/reiners_chat.git`
2. Afterwards you can run it from terminal via: `reiners_chat`

# Configuration

Video chats are stored as simple JSON with follwing structure:
```
{
  "<name-to-show-in-gui>": "<url-to-open-in-browser>",
  ...
}
```
By default, tool is looking in `~/.python_local/reiners_chat.json` for list of chats.
But you can also set env variable `REINERS_CHATFILE` to point to another JSON file holding chats.
