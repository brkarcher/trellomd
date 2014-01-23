# trellomd

Write a trello board to a human readable markdown file!

## Steps

1. Rename trellomd.cfg.example to trellomd.cfg.
2. Find the board URL for the board you want to back up, e.g. https://trello.com/b/nC8QJJoZ/trello-development, and put that in trellomd.cfg where it belongs.
3. Go to https://trello.com/1/appKey/generate and copy that 32-character key.  That goes in trellomd.cfg as dev_key, and also in the next step:
4. While logged in as a Trello user with read permissions on the board in question, go to https://trello.com/1/authorize?key=DEV_KEY_GOES_HERE&name=trellomd&expiration=30days&response_type=token.  Change or lose the "&expiration=30days" in that url if you'd like.  Now, grab that 64-character key and put it in trello.md as token.
5. Run with python3!  Preferably, get it piped into a file.  Run it with cron.  Send directly to a markdown renderer.  Print and stick it to your fridge.  Etcetera, Etcetera.

## Todo

* Support additional options (make labels optional, stickers, due dates, etc.)
* Do something to make this easier to run on multiple boards.  Take the board id as a command line argument, maybe?
* Make this a sublime 3 plugin?
* Python2 support?
* Make the key collection part nicer?
