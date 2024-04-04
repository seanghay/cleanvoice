import setuptools

with open("README.md", "r") as f:
  long_description = f.read()

setuptools.setup(
  name="cleanvoice",
  version="0.0.2",
  description="A Fast Speech Enhancement toolkit using Conv-TasNet",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/seanghay/cleanvoice",
  author="Seanghay Yath",
  author_email="seanghay.dev@gmail.com",
  license="MIT",
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Natural Language :: English",
  ],
  python_requires=">3.5",
  packages=setuptools.find_packages(exclude=["bin"]),
  package_dir={"cleanvoice": "cleanvoice"},
  package_data={"cleanvoice": ["convtasnet.onnx"]},
  include_package_data=True,
  install_requires=["onnxruntime", "librosa", "numpy"],
)
