# ----------------------------
# Zsh
# ----------------------------
alias ls='ls -G'


# ----------------------------
# Homebrew
# ----------------------------
eval "$(/opt/homebrew/bin/brew shellenv)"


# ----------------------------
# anyenv
# ----------------------------
export PATH="$HOME/.anyenv/bin:$PATH"
eval "$(anyenv init -)"

# ----------------------------
# Zinit
# ----------------------------
source $HOMEBREW_PREFIX/opt/zinit/zinit.zsh

# Plugins
# Load the pure theme, with zsh-async library that's bundled with it.
zinit ice pick"async.zsh" src"pure.zsh"
zinit light sindresorhus/pure
# Syntax highlight
zinit light zsh-users/zsh-syntax-highlighting
# Completion
zinit light zsh-users/zsh-autosuggestions
zinit light zsh-users/zsh-completions
