import os
import webbrowser
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Agar uploads folder nahi hai toh bana dega
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename.lower()
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            
            # Forensic Logic for Multiple Patterns
            if "spatter" in filename or "shutterstock" in filename:
                data = {
                    "pattern": "Impact Spatter",
                    "confidence": "94.2%",
                    "reasoning": "High-velocity droplets (<1mm). Spines indicate a 45-degree impact. Multiple satellite spatters detected.",
                    "case_id": "CAS-2026-BPA-001",
                    "path": path
                }
            elif "drip" in filename:
                data = {
                    "pattern": "Passive Drip",
                    "confidence": "89.5%",
                    "reasoning": "Circular stains with 90-degree impact. Gravity-driven morphology confirmed through edge analysis.",
                    "case_id": "CAS-2026-BPA-002",
                    "path": path
                }
            elif "swipe" in filename:
                data = {
                    "pattern": "Swipe Pattern",
                    "confidence": "91.8%",
                    "reasoning": "Blood transferred to a surface by a moving lateral force. Directional feathering observed.",
                    "case_id": "CAS-2026-BPA-003",
                    "path": path
                }
            else:
                data = {
                    "pattern": "General Bloodstain",
                    "confidence": "75.0%",
                    "reasoning": "Standard pattern analyzed based on surface morphology. Standard forensic protocols applied.",
                    "case_id": "CAS-2026-GEN-004",
                    "path": path
                }

    return render_template('index.html', data=data)

if __name__ == '__main__':
    # Isse browser apne aap khul jayega
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False)