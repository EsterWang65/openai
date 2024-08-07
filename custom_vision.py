from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# retrieve environment variables
ENDPOINT = "https://gjun-ai-04.cognitiveservices.azure.com/"
#training_key = "566f4bfb24124624b1ec58a4d6dda09d"
prediction_key = "566f4bfb24124624b1ec58a4d6dda09d"
#prediction_resource_id = os.environ["VISION_PREDICTION_RESOURCE_ID"]
file_path = "C:\Users\GM-206-E3\Downloads\test\1.jpg"

# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

with open(file_path, mode = "rb") as image_contents:
    results = predictor.classify_image("0365e7c2-0f3b-4b73-9853-333da4b55f26", "pet", image_contents.read())

    # Display the results.
for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))