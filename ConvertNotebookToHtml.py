from dependency import *

def Python_NoteBook_TO_HTML(notebook_path):
    try:
        file_name = os.path.splitext(os.path.basename(notebook_path))[0]
        output_path = os.path.join(f'{file_name}.html')

        with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
            notebook_content = nbformat.read(notebook_file, as_version=4)

        html_exporter = HTMLExporter(template_name="classic")
        html_exporter.exclude_input = True
        html_exporter.exclude_output_prompt = True
        html_exporter.embed_images = False
        html_exporter.anchor_link_text = ''

        # Customize options for the HTML exporter
        html_exporter.exclude_output = False  
        html_exporter.exclude_input_prompt = True
        html_exporter.exclude_output_prompt = True
        # html_exporter.exclude_code_cell = True
        html_exporter.exclude_unknown = True



        (html_output, resources) = html_exporter.from_notebook_node(notebook_content)

        with open(output_path, 'wb') as output_file:
            output_file.write(html_output.encode('utf-8'))

        temp = {"Message": "Conversion Done", "Filename": file_name}
    except Exception as e:
        temp = {"Message": str(e)}

    print(temp)
    return json.dumps(temp)

Python_NoteBook_TO_HTML(r"blog-20200426-shapley.ipynb")

