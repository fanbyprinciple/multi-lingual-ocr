from pdf2image import convert_from_path
import os 

all_files = []
file_names = []
for root, dirs, files in os.walk('./pdfs'):
    for f in files:
        all_files.append(os.path.join(root, f))
        file_names.append(f.split('.')[0])
    break

print(all_files)

for i,j  in zip(all_files, file_names):
    try:
        images = convert_from_path(i)
        print(images)

        c = 1
        for page in images:
            image_name = j + "_page_" + str(c) + ".jpg"
            page.save('./pdfs/extracted/'+image_name, "JPEG")
            c = c + 1

    except Exception as e:
        print(e)


