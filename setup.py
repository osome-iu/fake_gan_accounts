from setuptools import setup

setup(
    name="ganed",
    version="0.1",
    description="Lib for detecting Twitter accounts using GAN-generated profiles",
    license="MIT",
    author="Kaicheng Yang, Danishjeet Singh",
    author_email="yang3kc@gmail.com, singhdan@iu.edu",
    packages=["ganed"],
    python_requires=">=3.6",
    install_requires=["face_recognition>=1.3.0", "pillow", "numpy"],
)
