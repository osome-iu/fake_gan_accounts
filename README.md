# Introduction

This repo contains the code and information for the paper "Characteristics and prevalence of fake social media accounts with AI-generated profiles".

We analyze the fake accounts using GAN-generated images as their profiles on Twitter.

# `ganed` package

The `ganed` package implements the `GANEyeDistance` metric proposed in our paper.
The metric can help detect GAN-generated profiles on Twitter.

## Usage

### Install

The package is not on PyPI.
Assuming you are under the root directory of this project, you can use the following command:

```bash
pip install -e ./
```

This would install the package locally to your current Python environment.
It will also install the following dependencies:

- `face_recognition>=1.3.0`
- `pillow`
- `numpy`

Note that we only tested the package under Python 3.

### Examples

Using the package is straightforward:

```python
import ganed

ganed_calc = ganed.GANEyeDistance()

# Assumeing image_path is a path to an image on your disk
ganed_result = ganed_calc.calculate_distance(path_to_image=image_path)

# Assuming pil_image is a PIL.Image.Image instance
ganed_result = ganed_calc.calculate_distance(pil_image=pil_image)
```

## Recommendations

Applying the package to an input image would yield a `GANEyeDistance` value between 0 and 1.
A value close to 0 indicates that the eye locations of the input image are close to the expected locations of GAN-generated faces.

According to our experiment, using a threshold of 0.02 leads to a recall of over 99.5% for GAN-generated faces.
However, false positives are inevitable.
So, additional examinations are necessary to determine the true nature of the images labeled as positive.

# Data release

We also release the `TwitterGAN` dataset collected for our study.
The dataset contains 1,353 fake accounts with GAN-generated profiles.
We share their recent tweets and their profile images.
You can download the files from Zenodo (link coming soon).

- `TwitterGAN_tweets.ndjson.gz`: User objects and recent tweets from each account, collected using Twitter's V2 API. Each line is a JSON object containing the information for one account.
- `TwitterGAN_profiles.tar.gz`: Profile images for the accounts.
- `TwitterGAN_id_label_mapping.csv`: Mapping between user IDs, labels, and the profile image file names.