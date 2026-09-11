# BMI example models

CSDMS maintains a set of example models (nominally of temperature diffusion; each is named *Heat*), listed in {numref}`table:mappings-and-examples`, that are written in C, C++, Fortran, and Python and wrapped with a Basic Model Interface (BMI).
They are included in the {ref}`bmi-base-image`.

Below, we describe writing grpc4bmi servers for these example models and using the grpc4bmi Python client to run them.

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
