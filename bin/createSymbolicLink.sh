#!/bin/zsh -eu

# Move to the directory where this script exists.
cd "$(dirname "$0")/.." || exit

for f in .??*; do
    [ "$f" = ".git" ] && continue
    [ "$f" = ".gitconfig.local.template" ] && continue
    [ "$f" = ".gitmodules" ] && continue
    [ "$f" = ".gitignore" ] && continue

    ln -snfv ${PWD}/"$f" ~/
done
