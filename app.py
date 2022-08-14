from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException  


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():

    try:
        raise Exception("We are testing custome message ")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing_error_message)

    logging.info("we are testing logging module")
    return "Hello this is Yuvraj Kishor Narwade"


if __name__=="__main__":
    app.run(debug=True)