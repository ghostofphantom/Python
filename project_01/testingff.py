import qrcode
import webbrowser

def create_github_oauth_qr():
    # GitHub OAuth parameters
    client_id = "ghostofphantom"  # Register your OAuth app on GitHub
    redirect_uri = "https://github.com/ghostofphantom"  # Your redirect URI
    scope = "user"  # Requested permissions
    state = "random_state_string"  # CSRF protection
    
    # Create OAuth URL
    oauth_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(oauth_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("github_oauth_qr.png")
    print("QR code generated! Scan it to authorize with GitHub.")
    
    # Optional: Also open in browser
    webbrowser.open(oauth_url)

create_github_oauth_qr()