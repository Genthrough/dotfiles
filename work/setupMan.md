## memo for shell script

1. install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. set path to homebrew
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/ryo/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"

3. log in to AppStore
This is to enable "mas" to install applications.

4. Move “.Brewfile” to home directory

5. Install the applications described in "Brewfile"
>> brew bundle --global

by this command, homebrew install the applications in Brewfile.
brew ... -> application which is normally installed with command "brew install ..."
cask ... -> application which is normally installed with command "brew install --cask ..."
mas ... -> application which is normally installed with AppStore
it seems plugins for VS code and Google Chrome can be described in the Brewfile.
I have to confirm this.



## Brewfile
by hitting the command below, Homebrew installs the application specifiee in ~/.Brewfile
brew bundle --global

couldn't install vagrant
maybe need to install with Rosetta
is it possible to install with Rosetta with command line?

## GUI setting
keyboard -> keyboard shortcut
 Input sources
  change the shortcut key to command + Space
 Spotlight
  change the shortcut key to control + Space
 Modifier Keys
  change control to Capslock
  change Capslock to control


setup mail
add accounts

add applications to Dock

import the gesture and license of BetterTouchTool

customize shell
https://qiita.com/kinchiki/items/57e9391128d07819c321


pyenv should be managed with anyenv
python should be managed with pyenv
brew "python@3.12"
brew "pyenv"

echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(anyenv init -)"' >> ~/.zshrc


## there are several types of shells

1. Login Shell:
This shell is used when a user logs into the system.
To determine your current login shell, use the command:
> echo $SHELL

In my case, it's zsh.
The login shell can also serve as an interactive shell.

2. Interactive Shell:
This shell is used for direct interaction with the Terminal.
It allows users to execute commands and scripts directly.

3. Shell Script:
The shell specified in the script's shebang (#!) line determines which shell executes the script.
For example, #!/bin/bash specifies Bash, while #!/bin/zsh specifies Zsh.

https://qiita.com/ko1nksm/items/59c2e8a7afa969af8212


## dotfiles
when creating symbolic link, the path must be specified by full path.
The command to create symbolic link is as follows
ln -s "original path" "link path"
-s option is used to create symbolic link, not hard link.




## git config
git config --global user.name "Genthrough"
git config --global user.email "raghdwds@gmail.com"
ssh-keygen -t ed25519 -C "raghdwds@gmail.com"
pbcopy < ~/.ssh/id_ed25519.pub 

cd
mkdir dotfiles
cd dotfiles
git init
git branch -M main

