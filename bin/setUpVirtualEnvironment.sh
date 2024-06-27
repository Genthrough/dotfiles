#!/bin/zsh -eu

# Define the Python version to install
PYTHON_VERSION="3.12.4"

echo "Setting up virtual environment."

# Move to home directory; exit script if unsuccessful.
cd || exit

# Ensure anyenv directory exists
if [ ! -d "$HOME/.anyenv" ]; then
  echo "anyenv not found. Please install anyenv first."
  exit 1
fi

# Temporalily set PATH to include anyenv
export PATH="$HOME/.anyenv/bin:$PATH"

if [ ! -d "$HOME/.config/anyenv/anyenv-install" ]; then
  echo "anyenv init not completed. Initializing anyenv..."
  anyenv install --init
fi

# Initialize anyenv
eval "$(anyenv init -)"

# Install pyenv if not already installed
if [ ! -d "$HOME/.anyenv/envs/pyenv" ]; then
  anyenv install pyenv
fi

# source shell config
source "$HOME/.zshrc"

# Install necessary Python version if not already installed
if ! pyenv versions --bare | grep -q "^${PYTHON_VERSION}$"; then
  pyenv install "${PYTHON_VERSION}"
fi
pyenv global "${PYTHON_VERSION}"


# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
  echo "Homebrew not found. Please install Homebrew first."
  exit 1
fi


# Install Poetry if not already installed
if ! brew list --formula | grep -q "^poetry$"; then
  brew install poetry
fi

echo "Virtual environment setup completed."
