Containerization allows models to be run in any environment that supports Docker, making them more portable and easier to reuse.
It also ensures that the models are built with consistent dependencies, improving their sustainability.

In this project, we containerized several models from the [CSDMS Model Repository][model-repo].
The models are written in C, C++, Fortran, and Python.
Images of the models are hosted and made publicly available in the [CSDMS organization][csdms-docker] on Docker Hub.
Each model has a [Basic Model Interface][bmi] (BMI), allowing it to be controlled with a standard set of functions.

To facilitate model coupling, we used [grpc4bmi][grpc4bmi], software developed by the Netherlands eScience Center that allows communication with BMI functions in a container through the [Google Remote Procedure Call][grpc] (gRPC) framework.
The BMI functions for each model are exposed as endpoints in a container by a grpc4bmi server.
A grpc4bmi client, written in Python, can then make calls to the containerized BMI functions.

While containerizing these models and providing access to them through Docker Hub is important for their reuse, sustainability, and portability, equally important is the documentation for how this is done.
The idea is to help others in the community see how this process could improve the reuse, sustainability, and portability of their own models.
To this end, each source code repository on GitHub, and each image repository on Docker Hub, contains careful instructions on each step of the process, along with links to documentation for grpc4bmi, BMI, and Docker.

<!-- Links -->

[model-repo]: https://csdms.colorado.edu/wiki/Model_download_portal
[csdms-docker]: https://hub.docker.com/u/csdms
[bmi]: https://bmi.csdms.io
[grpc]: https://grpc.io
[grpc4bmi]: https://grpc4bmi.readthedocs.io/en/latest/index.html
