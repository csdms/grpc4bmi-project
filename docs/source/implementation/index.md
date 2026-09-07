# Implementation

grpc4bmi uses a client-server execution model, as depicted in {numref}`grpc4bmi-model`.

:::{figure} ../_static/grpc4bmi-project-grpc4bmi-model.png
:alt: grpc4bmi client-server model
:name: grpc4bmi-model

: A diagram of the grpc4bmi client-server model.
:::

A grpc4bmi server is built in a container alongside a model wrapped with a Basic Model Interface (BMI).
The server process exposes the BMI functions of the model as endpoints.
On the host, grpc4bmi has a Python client.
Method calls made on the client are serialized into a protocol buffer message by gRPC, sent over the network socket to the server inside the container, and executed against the model's BMI.
The result is serialized back in the same way.

In the following sections, we describe how to:

1. construct grpc4bmi servers for the BMI example models and for models selected from the CSDMS Model Repository, and
1. communicate with these servers through the grpc4bmi Python client.

```{toctree}
:caption: Implementation
:hidden: true
:maxdepth: 2

bmi-examples
csdms-models
```
