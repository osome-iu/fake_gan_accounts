import face_recognition
from PIL import Image
import numpy as np


class GANEyeDistance:
    def __init__(self):
        self.left_eye_ground_truth = (0.3808205078125, 0.4770548828125)
        self.right_eye_ground_truth = (0.6152169921875, 0.4771314453125)

    def calculate_distance(self, path_to_image=None, pil_image=None):
        """
        Calculate the GANEyeDistance of the given image
        :param path_to_image: path to the image
        :param pil_image: PIL.Image.Image instance, if the image is already loaded using pillow
        :return: GANEyeDistance, a number between 0 and 1, where small values means the eyes in the given image are close to the ground truth coordinates in GAN generated faces
        """
        if isinstance(path_to_image, str):
            image = face_recognition.load_image_file(path_to_image)
            pil_image = Image.fromarray(image)
        elif isinstance(pil_image, Image.Image):
            image = np.array(pil_image)
        else:
            raise ValueError("`path_to_image` or `pil_image` must be specified")
        try:
            size_x, size_y = pil_image.size
            # Using the 5 point mode of face recognition
            face_landmarks_list = face_recognition.face_landmarks(image, model="small")
            if len(face_landmarks_list) == 0:
                # GANED = 1 if no face is detected
                return 1
            elif len(face_landmarks_list) > 1:
                # GANED = 1 if multiple faces are detected
                return 1
            else:
                # Calculate GANED if there is one face detected
                face_landmarks = face_landmarks_list[0]
                # Extract the coordinates of the eyes
                # `face_recognition` returns two points for each eye
                (le_x1, le_y1), (le_x2, le_y2) = face_landmarks["left_eye"]
                (re_x1, re_y1), (re_x2, re_y2) = face_landmarks["right_eye"]
                # Use the midpoint of the two points of each eye as the center of the eye
                le_x = (le_x1 + le_x2) / 2
                le_y = (le_y1 + le_y2) / 2
                re_x = (re_x1 + re_x2) / 2
                re_y = (re_y1 + re_y2) / 2
                # Normalize the eye coordinates using the image size
                le_x_norm = le_x / size_x
                le_y_norm = le_y / size_y
                re_x_norm = re_x / size_x
                re_y_norm = re_y / size_y
                # Extract the ground truth coordinates
                le_x_gt, le_y_gt = self.left_eye_ground_truth
                re_x_gt, re_y_gt = self.right_eye_ground_truth

                # Calculate the GANEyeDistance
                distance = np.sqrt(
                    (le_x_norm - le_x_gt) ** 2 + (le_y_norm - le_y_gt) ** 2
                ) + np.sqrt((re_x_norm - re_x_gt) ** 2 + (re_y_norm - re_y_gt) ** 2)
                # Normalize the GANEyeDistance: sqrt(2) is the longest distance between two points in a 1 by 1 square, and there are two eyes, so the denominator is 2 * sqrt(2)
                distance_norm = distance / (2 * np.sqrt(2))
                return distance_norm

        except Exception as e:
            print(e)
            # GANED = 1 if there are errors in loading the image or detecting the face
            return 1
