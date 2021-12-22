from flask import Flask, request, render_template
import PyPDF2
 
app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    path = request.form['path']
    angle = request.form['angle']
    pagenumber = request.form['pagenumber']
    return changing(str(path),int(pagenumber),int(angle))
 
def changing(path,pgnumber,angle):
    try:

        pdf_in = open(path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_in)
        pdf_writer = PyPDF2.PdfFileWriter()
        if pgnumber>pdf_reader.numPages:
            return "Error :- Out Of Index"
        else:
            for pagenum in range(pdf_reader.numPages):
                page = pdf_reader.getPage(pagenum)
                if pgnumber==0:
                    page.rotateClockwise(int(angle))
                else:
                    if pagenum == pgnumber-1:
                        page.rotateClockwise(int(angle))
                pdf_writer.addPage(page)
        pdf_out = open('rotated.pdf', 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()
        return "Completed Check Folder"
    except Exception as e:
        return "Error:-"+str(e)

    

if __name__ == '__main__':
    app.run()