#!/bin/zsh -eu

# move to home directory
cd

# clone dotfiles
git clone https://github.com/Genthrough/dotfiles.git

# Move to home directory; exit script if unsuccessful.
cd || exit

