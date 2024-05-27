import os,sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from pneumonia_model_package.pneumonia_model_package import predict
from fastapi import APIRouter, UploadFile
from api.config import UPLOAD_FOLDER
from werkzeug.utils import secure_filename
from fastapi.encoders import jsonable_encoder
from api.validation import allowed_img_format
from fastapi.responses import JSONResponse
import typing as t
from loguru import logger
from api import __version__
from api.schemas import PredictionResult
from kitchenware_model_package.kitchenware_model_package import predict as kitchenwarepredict
from braintumor_model_package.braintumor_model_package import predict as braintumorpredict


api_router =  APIRouter()


@api_router.get('/health')
async def health():
    logger.info('Health Status Ok')
    return 'ok'


@api_router.get('/version')
async def version():
    return jsonable_encoder({'Api version': f'{__version__}'})


@api_router.post('/predict/chest_xray_classifier', response_model= PredictionResult, status_code=200)
async def predict_image(file: UploadFile):
    # check for file availability
    if not file:
        return {'message': 'no upload file sent'}
    else:
        data = file.filename
    logger.info(f"{data} received successfully")

    # validate and ensure file is secured
    if data and allowed_img_format(data):
        secure_data = secure_filename(data)
    
    # save the file to a location where we can access it
    with open(os.path.join(UPLOAD_FOLDER, secure_data), 'wb') as f:
        f.write(file.file.read())
    logger.info(f"file successfully saved to destination folder: {UPLOAD_FOLDER}")

    # call the predict function
    result  = predict.make_single_prediction(
        image_dir=UPLOAD_FOLDER,
        image_name=secure_data
    )

    readable_predictions = result.get('image_class')
    version = result.get('version')

    return dict([
        ('readable_prediction', readable_predictions),
        ('version', version)
    ]
    ) 
    

@api_router.post('/predict/kitchen_ware_classifier', response_model= PredictionResult, status_code=200)
async def predict_image(file: UploadFile):
    # check for file availability
    if not file:
        return {'message': 'no upload file sent'}
    else:
        data = file.filename
    logger.info(f"{data} received successfully")

    # validate and ensure file is secured
    if data and allowed_img_format(data):
        secure_data = secure_filename(data)
    
    # save the file to a location where we can access it
    with open(os.path.join(UPLOAD_FOLDER, secure_data), 'wb') as f:
        f.write(file.file.read())
    logger.info(f"file successfully saved to destination folder: {UPLOAD_FOLDER}")

    # call the predict function
    result  = kitchenwarepredict.make_single_img_prediction(
        folder=UPLOAD_FOLDER,
        file=secure_data
    )

    readable_predictions = result.get('image_class')
    version = result.get('version')

    return dict([
        ('readable_prediction', readable_predictions),
        ('version', version)
    ]
    )


@api_router.post('/predict/braintumor_classifier', response_model= PredictionResult, status_code=200)
async def predict_image(file: UploadFile):
    # check for file availability
    if not file:
        return {'message': 'no upload file sent'}
    else:
        data = file.filename
    logger.info(f"{data} received successfully")

    # validate and ensure file is secured
    if data and allowed_img_format(data):
        secure_data = secure_filename(data)
    
    # save the file to a location where we can access it
    with open(os.path.join(UPLOAD_FOLDER, secure_data), 'wb') as f:
        f.write(file.file.read())
    logger.info(f"file successfully saved to destination folder: {UPLOAD_FOLDER}")

    # call the predict function
    result  = braintumorpredict.make_single_img_prediction(
        folder=UPLOAD_FOLDER,
        file=secure_data
    )

    readable_predictions = result.get('image_class')
    version = result.get('version')

    return dict([
        ('readable_prediction', readable_predictions),
        ('version', version)
    ]
    )