# Password Checker for Marisa's Puzzle Hunt

Hello

Because pastebin has a limit on the number of attempts you can use when unlocking a password-protected paste, I have created this tool to let you check passwords. Once you're sure you're correct, you can go enter your password in the pastebin without any worries of being locked out.

To use this tool, simply navigate to the file's location in your terminal and run `python passwordchecker.py` (assuming you have python installed). You should automatically be greeted by a few simple instructions about how to use the tool.

For the sake of redundancy, I have also reproduced some of those instructions here.

First, enter the name of the pastebin you'd like to check the password for. No need to wrap your answer in `'` or `"` characters. Your answer will automatically be interpreted as a string. You also don't have to worry about capitalization or spaces; the code will strip that all away anyway.

Next, enter your guess for the password. Again, no need to wrap your answer in a string.

At any time when guessing a password, you can type 'back' to go back to the layer where you choose a pastebin, and you can type 'exit' from there to close the tool.
