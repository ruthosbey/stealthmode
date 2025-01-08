# StealthMode

StealthMode is a Python program designed to improve privacy on Windows systems by hiding user activity and data from unauthorized access. It achieves this by performing a series of actions that reduce traces of user activity and potential attack vectors on a Windows machine.

## Features

- **Clear Recent Files**: Deletes all files from the Windows "Recent" folder to remove traces of recently accessed files.
- **Disable File Sharing**: Turns off administrative file shares to prevent unauthorized network access.
- **Disable Remote Assistance**: Disables the remote assistance feature to prevent unauthorized remote access.
- **Clear Temporary Files**: Removes all files in the temporary folder to ensure no sensitive data remains.

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/stealthmode.git
   ```
2. Navigate to the project directory.
   ```bash
   cd stealthmode
   ```

## Usage

Run the program using Python:

```bash
python stealth_mode.py
```

This will execute the privacy-enhancing functions to help protect your Windows system from unauthorized access and data exposure.

## Disclaimer

This script is provided for educational purposes only. Use it at your own risk. Ensure you have appropriate permissions and understand the implications before running this script on any system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.