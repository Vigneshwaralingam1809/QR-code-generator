# QR Code Generator

This project generates QR codes from user input, using Python libraries `qrcode` and `matplotlib`. The user enters text or a URL, and the program generates a corresponding QR code that can be scanned with a QR code reader.

## Features

- **User Input**: Allows the user to enter data (e.g., URL, text) to generate a QR code.
- **QR Code Generation**: Uses the `qrcode` library to generate a custom QR code with user-defined settings.
- **Visualization**: Uses `matplotlib` to display the generated QR code as an image.

## Requirements

- Python 3.x
- `qrcode` library
- `matplotlib` library

### Install Dependencies

To run this project, you will need to install the necessary Python libraries. You can install them using `pip`:

```bash
pip install qrcode[pil] matplotlib
```

## How It Works

1. **User Input**: The program prompts the user to input data (text or URL).
2. **QR Code Generation**: The entered data is passed to the `qrcode` library, which generates a QR code with the following settings:
   - `version=1`: Size of the QR code (from 1 to 40).
   - `error_correction=qrcode.constants.ERROR_CORRECT_L`: Error correction level (lower values mean less redundancy).
   - `box_size=10`: Size of each individual box in the QR code.
   - `border=4`: Thickness of the QR code border.
3. **QR Code Display**: The generated QR code is rendered using `matplotlib`'s `imshow()` function, and displayed without axes.

## Example

1. Run the script.
2. Enter the data (URL or text) when prompted.
3. The QR code will be displayed as an image.

### Sample Output

If you input `https://www.example.com`, the QR code will be displayed corresponding to that URL.

## Usage

1. Clone or download this repository.
2. Run the script in your terminal or IDE:

```bash
python qr_code_generator.py
```

3. Follow the prompts to generate and view your QR code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
