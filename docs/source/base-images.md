<!--base-images-->

# Base images

Two Docker images, one for the BMI mappings and examples, the other for the grpc4bmi C++ server, are used as base images in this project.
Both are built on recent conda-forge and Ubuntu base images.

```{figure} _static/grpc4bmi-project-base-images-h.png
:alt: Base Docker images
:name: base-images

: Inheritance diagram for the BMI and grpc4bmi base images.
```

## BMI base image

The BMI base image contains built versions of the BMI mappings and example models for C, C++, Fortran, and Python.
This image is the base for building models that expose a BMI in these languages, or for inter-language model coupling.

```{table} : Repositories contained in the BMI base image.
:widths: auto
:width: 75%

| Language | Mapping       | Example implementation |
| -------- | ------------- | ---------------------- |
| C        | [bmi-c]       | [bmi-example-c]        |
| C++      | [bmi-cxx]     | [bmi-example-cxx]      |
| Fortran  | [bmi-fortran] | [bmi-example-fortran]  |
| Python   | [bmi-python]  | [bmi-example-python]   |
```

The image is built on the [condaforge/miniforge3][miniforge3] base image available from Docker Hub.
The OS is Linux/Ubuntu.
The shell is bash.
Conda, as well as the BMI language mappings and examples, are installed in `CONDA_DIR=/opt/conda`.
The base environment is activated.

The source code used to build this image, as well as simple examples of its use, can be found on GitHub at [csdms/bmi-docker][bmi-image-source].
A versioned, multiplatform image built from this repository is hosted on Docker Hub at [csdms/bmi][bmi-image-image].

:::{admonition} BMI base image
:class: seealso

* Source repository: <https://github.com/csdms/bmi-docker>
* Image repository: <https://hub.docker.com/r/csdms/bmi>
:::

## grpc4bmi base image

The grpc4bmi base image is built on the BMI base image, so it contains everything described in the section above.
Further, it contains a built version of the [grpc4bmi C++ server][grpc4bmi-cxx-server], also installed in `CONDA_DIR=/opt/conda`.
Dependencies for the server are met with gRPC conda packages available from the conda-forge channel.

The source code used to build this image can be found on GitHub at [csdms/grpc4bmi-docker][grpc4bmi-image-source].
A versioned, multiplatform image built from this repository is hosted on Docker Hub at [csdms/grpc4bmi][grpc4bmi-image-image].

:::{admonition} grpc4bmi base image
:class: seealso

* Source repository: <https://github.com/csdms/grpc4bmi-docker>
* Image repository: <https://hub.docker.com/r/csdms/grpc4bmi>
:::

<!-- Links -->

[bmi]: https://bmi.csdms.io

[bmi-c]: https://github.com/csdms/bmi-c
[bmi-cxx]: https://github.com/csdms/bmi-cxx
[bmi-fortran]: https://github.com/csdms/bmi-fortran
[bmi-python]: https://github.com/csdms/bmi-python
[bmi-example-c]: https://github.com/csdms/bmi-example-c
[bmi-example-cxx]: https://github.com/csdms/bmi-example-cxx
[bmi-example-fortran]: https://github.com/csdms/bmi-example-fortran
[bmi-example-python]: https://github.com/csdms/bmi-example-python
[miniforge3]: https://hub.docker.com/r/condaforge/miniforge3/
[bmi-image-source]: https://github.com/csdms/bmi-docker
[bmi-image-image]: https://hub.docker.com/r/csdms/bmi
[grpc4bmi-cxx-server]: https://github.com/csdms/grpc4bmi/tree/main/cpp
[grpc4bmi-image-source]: https://github.com/csdms/grpc4bmi-docker
[grpc4bmi-image-image]: https://hub.docker.com/r/csdms/grpc4bmi
