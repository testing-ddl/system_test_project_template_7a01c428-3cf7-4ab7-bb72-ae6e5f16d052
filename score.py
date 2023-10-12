import os
import sys

from anomalib.deploy import OpenVINOInferencer

inferencer = OpenVINOInferencer(
    path="padim/mvtec/mteal_nut/run/weights/openvino/model.bin",
    metadata="padim/mvtec/mteal_nut/run/weights/openvino/metadata.json",  
    device="CPU"
)

def score(image):
    print("Generating predictions for image {}".format(image))
    predictions = inferencer.predict(image=image)
    return predictions.pred_score, predictions.pred_label

if __name__ == "__main__":
    dataset_path = os.path.join(os.environ["DOMINO_DATASETS_DIR"], os.environ["DOMINO_PROJECT_NAME"])
    pred_score, pred_label = score(os.path.join(dataset_path, "metal_nut/test/bent/000.png"))
    print("pred_score: ", pred_score)
    print("pred_label: ", pred_label)
    
