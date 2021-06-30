# Password Checker for Marisa's Puzzle Hunt

Hello!

## What is this?
Pastebin has a limit on the number of attempts you can use when unlocking a password-protected paste. Too many incorrect attempts will result in you being locked out for a period of time. While you can get around this by using a VPN to change your IP address, that's a pain. So I have created this tool to let you check passwords! Once you're sure you're correct, you can go enter your password in the pastebin without any worries of being locked out.

## How to use
Make sure you have python3 installed on your device, then download `passwordchecker.py`. Then navigate to the file's location in your terminal and run `python passwordchecker.py`. You could also run the code online somewhere like https://www.online-python.com/.

When running the file, you should automatically be greeted by a few simple instructions about how to use the tool. For the sake of redundancy, I have also reproduced some of those instructions here.

1. When you first start the program, enter the name of the pastebin you'd like to check the password for. Spaces and capitalization don't matter for paste names. For example, entering "thesty" is the same as entering "The Sty".
2. After selecting a pastebin, enter your password guess. Capitalization DOES MATTER for passwords. By default, you can assume that passwords use lowercase letters unless your clue specifically seems to use capital letters. Feel free to ask me if it's ambiguous! Also: passwords will never contain spaces or punctuation.
3. At any time when guessing a password, you can type 'back' to go back to the layer where you choose a pastebin, and you can type 'exit' from there to close the tool.
