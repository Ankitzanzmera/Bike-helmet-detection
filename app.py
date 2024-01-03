import os,sys
from flask import Flask,request,jsonify,render_template,Response
from flask_cors import cross_origin,CORS
from Bike_helmet_detection.utils.exception import CustomException
from Bike_helmet_detection.utils.common import decodeImage,encodeImageintobase64
from Bike_helmet_detection.utils.logger import logger
app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self) -> None:
        self.filename = "inputImage.jpg"

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/predict",methods = ['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image,clApp.filename)

        os.system("cd yolov5 && python detect.py --weights best.pt --img 416 --conf 0.5 --source ../inference_data/inputImage.jpg")
        opencodedbase64  = encodeImageintobase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {'image': opencodedbase64.decode('utf-8')}
        os.system("rm -rf yolov5/runs")
        
        return jsonify(result)

    except ValueError as val:
        return Response("Value Not Found inside json data")
    except KeyError:
        return Response("Key Value Error Incorrect Key Passed")
    except Exception as e:
        raise CustomException(e,sys)
    
    
    
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host = "0.0.0.0",port = 8080)
    