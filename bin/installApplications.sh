#!/bin/zsh -eu

# Inform user about starting installation.
echo "Starting installation of applications from Brewfile."

# Move to home directory; exit script if unsuccessful.
cd || exit

# Install applications from Brewfile using brew bundle.
brew bundle --global

# Inform user about completion.
echo "Application installation finished."
