#!/bin/zsh -eu

echo "Starting installation of Homebrew."

# Check if Homebrew is already installed
if command -v brew >/dev/null 2>&1; then
    echo "Homebrew is already installed."
else
    # Install Homebrew
    if /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"; then
        echo "Homebrew installation finished."
    else
        echo "Homebrew installation failed." >&2
        exit 1
    fi
fi

# Set path to Homebrew
eval "$(/opt/homebrew/bin/brew shellenv)"

echo "Homebrew installation finished."


# the command below is unnecessary because the content below is included in dotfiles.
# echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> ~/.zshrc
