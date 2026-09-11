# BMI example models

CSDMS maintains a set of example models (nominally of temperature diffusion; each is named *Heat*), listed in {numref}`table:mappings-and-examples`, that are written in C, C++, Fortran, and Python and wrapped with a Basic Model Interface (BMI).
They are included in the {ref}`bmi-base-image`,
which is the base for the {ref}`grpc4bmi-base-image`,
which, as shown in {numref}`figure:bmi-example-images`,
is the base for the grpc4bmi servers for these examples.

Below, we describe writing the grpc4bmi servers for these models and running them through the grpc4bmi Python client.

```{figure} ../_static/grpc4bmi-project-bmi-example-images.png
:alt: BMI example Docker images
:name: figure:bmi-example-images

: Inheritance diagram for the BMI example model grpc4bmi server images.
```

:::{note}

In the examples below, the source repository contains two options for building a grpc4bmi server: one titled *conda-base*, the other *source-base*.
Here, we'll use the *conda-base* option.
It uses the grpc4bmi base image described in the {ref}`base-images` section, where conda-forge is used to satisfy all dependencies.
The *source-base* option is an alternative where all grpc4bmi dependencies are built from source, which can be tricky.
:::

## C example

From the root directory of the [source repository][example-c-server-source], the file structure of the grpc4bmi server for the C *Heat* model is:

```sh
images/conda-base
├── Dockerfile
├── README.md
└── server
    ├── CMakeLists.txt
    └── heatc-grpc4bmi-server.cxx
```

Note that the server is actually a C++ project to match the grpc4bmi software and its dependencies.

The server source, `heatc-grpc4bmi-server.cxx`, includes:

1. the *Heat* model header, `bmi_heat.h`,
and the grpc4bmi server header, `bmi_grpc_server.h`
1. a main program that instantiates the model's BMI and calls the grpc4bmi *run_bmi_server* function, passing in the model's BMI instance

The build system is CMake.
In Docker, the server is compiled into the executable *heatc-grpc4bmi-server* and installed alongside the existing *Heat* model into `CONDA_DIR=/opt/conda`.
The server executable is the entry point into the container, exposed through port `55555`.

:::{admonition} BMI C example grpc4bmi server image
:class: seealso

* Source repository: <https://github.com/csdms/bmi-example-c-grpc4bmi>
* Image repository: <https://hub.docker.com/r/csdms/bmi-example-c-grpc4bmi>
:::

## C++ example

:::{admonition} BMI C++ example grpc4bmi server image
:class: seealso

* Source repository: <https://github.com/csdms/bmi-example-cxx-grpc4bmi>
* Image repository: <https://hub.docker.com/r/csdms/bmi-example-cxx-grpc4bmi>
:::

## Fortran example

:::{warning}
This example is still under development.
:::

:::{admonition} BMI Fortran example grpc4bmi server image
:class: seealso

* Source repository: <https://github.com/csdms/bmi-example-fortran-grpc4bmi>
<!--* Image repository: <https://hub.docker.com/r/csdms/bmi-example-c-grpc4bmi>-->
:::

## Python example

:::{admonition} BMI Python example grpc4bmi server image
:class: seealso

* Source repository: <https://github.com/csdms/bmi-example-python-grpc4bmi>
* Image repository: <https://hub.docker.com/r/csdms/bmi-example-python-grpc4bmi>
:::


<!-- Links -->

[example-c-server-source]: https://github.com/csdms/bmi-example-c-grpc4bmi
[example-c-server-image]: https://hub.docker.com/r/csdms/bmi-example-c-grpc4bmi
