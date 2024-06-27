#!/bin/zsh -eu

# List of scripts to execute
scripts=(
  "createSymbolicLink.sh"
  "installHomebrew.sh"
  "installApplications.sh"
  "setUpVirtualEnvironment.sh"
  "configureGuiSetting.sh"
)

# Execute each script in the list
for script in "${scripts[@]}"; do
  cd "$(dirname "$0")" || exit
  chmod +x "./bin/$script"
  "./bin/$script"
done

echo "all installation completed."

# Relogin to shell
exec $SHELL -l
