<!--base-images-->

# Base images

Two images, one for the BMI mappings and examples, the other for the grpc4bmi C++ server, are used as base images in this project.
Both are built on recent conda-forge and Ubuntu base images.

```{figure} _static/grpc4bmi-project-base-images-h.png
:alt: Base images
:label: base-images

*Figure 1: Inheritance diagram for the BMI and grpc4bmi base images used in the project.*
```

## BMI image

The [Basic Model Interface][bmi] (BMI) is a set of functions for querying, modifying, running, and coupling models.

The *bmi-docker* project, where I containerized the BMI mappings for [C][bmi-c], C++, [Fortran][bmi-fortran], and Python, as well as the BMI example models for these languages.

The image is built on the conda-forge image.

The image is hosted and publicly available on Docker Hub.

The image is the base for building models that expose a BMI in these languages, or for inter-language model coupling.


The image is built on the condaforge/miniforge3 base image. The OS is Linux/Ubuntu. conda, as well as the BMI language mappings and examples, are installed in CONDA_DIR=/opt/conda. The base environment is activated.

A versioned, multiplatform image built from this repository is hosted on Docker Hub at csdms/bmi. This image is automatically built and pushed to Docker Hub with the release CI workflow. The workflow is only run when the repository is tagged. 

https://github.com/csdms/bmi-docker

https://hub.docker.com/r/csdms/bmi

## grpc4bmi image

Build the grpc4bmi C++ server from gRPC conda packages.

https://github.com/csdms/grpc4bmi-docker

https://hub.docker.com/r/csdms/grpc4bmi


<!-- Links -->

[bmi]: https://bmi.csdms.io
[bmi-c]: https://github.com/csdms/bmi-c
[bmi-fortran]: https://github.com/csdms/bmi-fortran
