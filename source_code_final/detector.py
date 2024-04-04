import argparse
import pickle
from collections import Counter
from pathlib import Path

import face_recognition
from PIL import Image, ImageDraw
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

import re

DEFAULT_ENCODINGS_PATH = Path("output/encodings.pkl")
BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"

# Create directories if they don't already exist
Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

parser = argparse.ArgumentParser(description="Recognize faces in an image")
parser.add_argument("--train", action="store_true", help="Train on input data")
parser.add_argument(
    "--validate", action="store_true", help="Validate trained model"
)
parser.add_argument(
    "--test", action="store_true", help="Test the model with an unknown image"
)
parser.add_argument(
    "-m",
    action="store",
    default="hog",
    choices=["hog", "cnn"],
    help="Which model to use for training: hog (CPU), cnn (GPU)",
)
parser.add_argument(
    "-f", action="store", help="Path to an image with an unknown face"
)
args = parser.parse_args()


def encode_known_faces(
    model: str = "hog"
) -> dict:
    """
    Loads images in the training directory and builds a dictionary of their
    names and encodings.
    """
    names = []
    encodings = []

    for filepath in Path("training").glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)

    return {"names": names, "encodings": encodings}


def recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> list:
    """
    Given an unknown image, get the locations and encodings of any faces and
    compares them against the known encodings to find potential matches.
    """
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )


    pillow_image = Image.fromarray(input_image)
    draw = ImageDraw.Draw(pillow_image)


    for bounding_box, unknown_encoding in zip(
        input_face_locations, input_face_encodings
    ):
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "unknown"
        _display_face(draw, bounding_box, name)
    
    del draw
    pillow_image.show()
        



def validation_recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> tuple:
    """
    Given an unknown image, get the locations and encodings of any faces and
    compares them against the known encodings to find potential matches.
    """
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )

    predicted_names = []

    for unknown_encoding in input_face_encodings:
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "unknown"
        predicted_names.append(name)

    filename_without_number = re.sub(r'\d+(?=\.[^.]+$)', '', image_location)
    return predicted_names, [Path(filename_without_number).stem] * len(predicted_names)



def _recognize_face(unknown_encoding, loaded_encodings):
    """
    Given an unknown encoding and all known encodings, find the known
    encoding with the most matches.
    """
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]




def validate(model: str = "hog") -> list:
    """
    Runs recognize_faces on a set of images with known faces to validate
    known encodings.
    """
    actual_labels = []
    predicted_labels = []

    for filepath in Path("validation").rglob("*"):
        if filepath.is_file():
            predicted_names, actual_names = validation_recognize_faces(
                image_location=str(filepath.absolute()), model=model
            )
            actual_labels.extend(actual_names)
            predicted_labels.extend(predicted_names)

    return actual_labels, predicted_labels




def _display_face(draw, bounding_box, name):
    """
    Draws bounding boxes around faces, a caption area, and text captions.
    """
    top, right, bottom, left = bounding_box
    draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)
    text_left, text_top, text_right, text_bottom = draw.textbbox(
        (left, bottom), name
    )
    draw.rectangle(
        ((text_left, text_top), (text_right, text_bottom)),
        fill=BOUNDING_BOX_COLOR,
        outline=BOUNDING_BOX_COLOR,
    )
    draw.text(
        (text_left, text_top),
        name,
        fill=TEXT_COLOR,
    )



def plot_confusion_matrix(predicted_labels, actual_labels, class_names=None):
#   actual = np.array(actual_labels)
#   predicted = np.array(predicted_labels)

  # Calculate confusion matrix
  cm = confusion_matrix(actual_labels, predicted_labels)
  actual=actual_labels
  predicted=predicted_labels

  # Get unique class names if not provided
#   actual_labels.append("not "+actual_labels[0])
#   print(cm)
#   if class_names is None:
#       class_names = np.unique(actual_labels)
    #   print(class_names)
#   exit()

  # Create confusion matrix plot
  sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', xticklabels=[actual_labels[0],"not "+actual_labels[0]], yticklabels=[actual_labels[0],"not "+actual_labels[0]])
  plt.xlabel('Predicted labels',fontsize=13)
  plt.ylabel('True labels',fontsize=13)
  plt.title('Confusion Matrix',fontsize=17)
  plt.show()

  print(classification_report(actual, predicted))






if __name__ == "__main__":
    if args.train:
        encodings = encode_known_faces(model=args.m)
        with DEFAULT_ENCODINGS_PATH.open(mode="wb") as f:
            pickle.dump(encodings, f)

    if args.validate:
        actual_labels, predicted_labels = validate(model=args.m)
        # print(actual_labels)
        # print("\n")
        # print(predicted_labels)
        # exit()
        plot_confusion_matrix(predicted_labels=predicted_labels,actual_labels=actual_labels)

    if args.test:
        recognize_faces(image_location=args.f, model=args.m)
