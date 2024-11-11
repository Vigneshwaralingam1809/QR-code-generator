import qrcode
import matplotlib.pyplot as plt

# Function to generate and display QR code
def generate_qr():
    input_data = input("Enter data for QR Code: ")  # Get the data from the user

    if not input_data:
        print("Please enter some data to generate the QR code.")
        return
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Display the QR code using matplotlib
    plt.imshow(img)
    plt.axis('off')  # Hide axes
    plt.show()

# Call the function to generate and display QR code
generate_qr()
