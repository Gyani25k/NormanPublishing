from dependency import *

output_folder = 'output' 
filenumber = 0

def Python_NoteBook_TO_HTML(notebook_path):
    global filenumber
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        output_path = os.path.join(output_folder, f'output_file_{filenumber}.html')
        template = 'classic'
        
        filenumber += 1

        with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
            notebook_content = nbformat.read(notebook_file, as_version=4)

        html_exporter = HTMLExporter()
        html_exporter.template_name = template
        html_exporter.exclude_input = True
        html_exporter.exclude_output_prompt = True

        (html_output, resources) = html_exporter.from_notebook_node(notebook_content)

        with open(output_path, 'wb') as output_file: 
            output_file.write(html_output.encode('utf-8'))
        
        temp = {"Message": "Conversion Done"}
    except:
        temp = {"Message": "Error"}

    return json.dumps(temp)

Python_NoteBook_TO_HTML(r"email.ipynb")
