from flask import Flask, render_template, request, redirect, url_for
import os
import re
import logging

app = Flask(__name__)

# Define folders for uploaded and annotated files
UPLOAD_FOLDER = 'uploads'
ANNOTATED_FOLDER = 'annotated'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ANNOTATED_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ANNOTATED_FOLDER'] = ANNOTATED_FOLDER

# Function to add newlines before specific tags
def add_newlines_before_tags(xml_content):
    """
    Adds a newline before specific tags in the XML content if there is no newline present.
    """
    tags_to_add_newline = ['div', 'p', 'list', 'item', 'head']
    
    for tag in tags_to_add_newline:
        # Create a regex pattern to find the tag and add a newline before it if not present
        pattern = r'(?<!\n)<({})'.format(tag)
        xml_content = re.sub(pattern, r'\n<\1', xml_content)
    
    return xml_content

@app.route('/')
def index():
    # List all .xml files in the uploads folder
    upload_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.xml')]
    
    # List all .xml files in the annotated folder
    annotated_files = [f for f in os.listdir(ANNOTATED_FOLDER) if f.endswith('.xml')]
    
    return render_template('index.html', upload_files=upload_files, annotated_files=annotated_files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and file.filename.endswith('.xml'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return redirect(url_for('index'))
    return 'Invalid file format', 400

@app.route('/annotate/<filename>', methods=['GET', 'POST'])
def annotate(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if request.method == 'POST':
        # Get the annotated XML from the form
        annotated_text = request.form["annotated_text"]
        
        # Save the annotated text to the annotated folder
        annotated_file_path = os.path.join(ANNOTATED_FOLDER, filename)
        with open(annotated_file_path, 'w', encoding='utf-8') as f:
            f.write(annotated_text)
        
        # Redirect back to the file list
        return redirect(url_for('index'))
    else:
        # Read the XML file content
        with open(file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        # Format the XML content by adding newlines before specific tags
        formatted_xml = add_newlines_before_tags(xml_content)
        
        # Render the template with the formatted XML content
        return render_template('annotate.html', filename=filename, xml_content=formatted_xml)

@app.route('/resume/<filename>')
def resume(filename):
    file_path = os.path.join(app.config['ANNOTATED_FOLDER'], filename)
    if request.method == 'POST':
        # Get the annotated XML from the form
        annotated_text = request.form["annotated_text"]
        
        # Save the annotated text to the annotated folder
        annotated_file_path = os.path.join(ANNOTATED_FOLDER, filename)
        with open(annotated_file_path, 'w', encoding='utf-8') as f:
            f.write(annotated_text)
        
        # Redirect back to the file list
        return redirect(url_for('index'))
    else:
        # Read the XML file content
        with open(file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        # Format the XML content by adding newlines before specific tags
        formatted_xml = add_newlines_before_tags(xml_content)
        
        # Render the template with the formatted XML content
        return render_template('annotate.html', filename=filename, xml_content=formatted_xml)
    
# @app.route('/annotate/<filename>', methods=['GET', 'POST'])
# def annotate(filename):
#     if request.method == 'POST':
#         annotated_text = request.form["annotated_text"]
#         app.logger.debug(f"Annotated text received: {annotated_text}")

if __name__ == '__main__':
    app.run(debug=True)
