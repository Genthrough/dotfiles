#!/bin/zsh -eu

# Move to the directory where this script exists.
cd "$(dirname "$0")" || exit

# Execute installHomebrew.sh
chmod +x ./bin/installHomebrew.sh
./bin/installHomebrew.sh


# Move to the directory where this script exists.
cd "$(dirname "$0")" || exit

# Execute installApplications.sh
chmod +x ./bin/installApplications.sh
./bin/installApplications.sh


# Move to the directory where this script exists.
cd "$(dirname "$0")" || exit

# Execute configureGuiSetting.sh
chmod +x ./bin/configureGuiSetting.sh
./bin/configureGuiSetting.sh

echo "all installation completed."
