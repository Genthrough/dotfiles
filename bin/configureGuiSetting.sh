#!/bin/zsh -eu

# Dock settings
defaults write com.apple.dock orientation right
defaults write com.apple.dock tilesize -int 25
defaults write com.apple.dock autohide -bool true
defaults write com.apple.dock launchanim -bool false
defaults write com.apple.dock show-recents -bool false
killall Dock
echo "Dock settings updated."

# Global settings
defaults write -g AppleShowAllExtensions -bool true
echo "Global settings updated."

# Battery menu settings
defaults write com.apple.menuextra.battery ShowPercent -string "YES"
echo "Battery menu settings updated."

# Trackpad settings
defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad Clicking -int 1
defaults write -g com.apple.trackpad.scaling -float 15
echo "Trackpad settings updated."
