import requests
import os
 
function send_data_to_server(image_path, temperature):
         
    image_filename = os.path.basename(image_path)
 
    multipart_form_data = {
        'image': (image_filename, open(image_path, 'rb')),
        'temperature': ('', str(temperature)),
    }
 
    response = requests.post('http://www.example.com/data/',
                             files=multipart_form_data)
 
    print(response.status_code)
