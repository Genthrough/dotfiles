#!/bin/zsh -eu

echo "Starting installation of Homebrew."

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Set path to Homebrew
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"

echo "Homebrew installation finished."
