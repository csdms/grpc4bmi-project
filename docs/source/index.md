<!-- grpc4bmi-project -->

# Coupling containerized models

Containerization allows models to be run in any environment that supports Docker, making them more portable and easier to reuse.
It also ensures that the models are built with consistent dependencies, improving their sustainability.

```{toctree}
:caption: Project Description
:hidden: true
:maxdepth: 2

Base Images <base-images>
implementation/index
```

```{toctree}
:caption: Project Resources
:hidden: true
:maxdepth: 2

License <license>
Code of Conduct <code-of-conduct>
Contributors <contributing>
Credits <credits>
Getting Help <support>
```

## Overview

In this project, we use Docker to containerize several models from the [CSDMS Model Repository][model-repo].
The models are written in C, C++, Fortran, and Python.
Images of the models are hosted and made publicly available on [Docker Hub][csdms-docker].
Each model has a [Basic Model Interface][bmi] (BMI), allowing it to be controlled with a set of common functions.

To facilitate model coupling, we used [grpc4bmi][grpc4bmi], software developed by the Netherlands eScience Center, which allows communication with BMI functions in a container through the [Google Remote Procedure Call][grpc] (gRPC) framework.
The BMI functions for each model are exposed as endpoints in a container by a grpc4bmi server.
A grpc4bmi client, written in Python, can then make calls to the containerized BMI functions.

### Topics

* Containerizing the BMI mappings and example models for C, C++, Fortran, and Python
* Containerizing the grpc4bmi software
* Building grpc4bmi servers for
  * the BMI exampls models
  * models from the CSDMS Model Repository
* Running models with the grpc4bmi Python client

## Acknowledgments

```{include} ../../README.md
:start-after: "<!-- start-ack -->"
:end-before: "<!-- end-ack -->"
```

<!-- Links -->

[model-repo]: https://csdms.colorado.edu/wiki/Model_download_portal
[csdms-docker]: https://hub.docker.com/u/csdms
[bmi]: https://bmi.csdms.io
[grpc]: https://grpc.io
[grpc4bmi]: https://grpc4bmi.readthedocs.io/en/latest/index.html
