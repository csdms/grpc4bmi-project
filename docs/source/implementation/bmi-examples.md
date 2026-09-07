# BMI example models

CSDMS maintains a set of example models (nominally of temperature diffusion; each is named *Heat*), listed in {numref}`mappings-and-examples`, that are written in C, C++, Fortran, and Python and wrapped with a Basic Model Interface (BMI).
They are included in the {ref}`bmi-base-image`.

Below, we describe writing grpc4bmi servers for these example models and using the grpc4bmi Python client to run them.

```{figure} ../_static/grpc4bmi-project-bmi-example-images.png
:alt: BMI example Docker images
:name: bmi-example-images

: Inheritance diagram for the BMI example model grpc4bmi server images.
```


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
