from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Simulated database (list of assets)
assets = []

@app.route('/')
def index():
    return render_template('index.html', assets=assets)

@app.route('/add', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        company_name = request.form.get('company_name')
        asset_type = request.form.get('asset_type')
        description = request.form.get('description')
        invoice_number = request.form.get('invoice_number')
        invoice_date = request.form.get('invoice_date')
        purchase_amount = request.form.get('purchase_amount')
        vendor_name = request.form.get('vendor_name')
        warranty_start = request.form.get('warranty_start')
        warranty_end = request.form.get('warranty_end')

        # Handling file upload
        file = request.files.get('invoice_file')
        if file and file.filename:
            invoice_filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], invoice_filename))
        else:
            invoice_filename = None

        # Store asset details
        assets.append({
            'user_name': user_name,
            'company_name': company_name,
            'asset_type': asset_type,
            'description': description,
            'invoice_number': invoice_number,
            'invoice_date': invoice_date,
            'purchase_amount': purchase_amount,
            'vendor_name': vendor_name,
            'warranty_start': warranty_start,
            'warranty_end': warranty_end,
            'invoice_file': invoice_filename
        })

        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
