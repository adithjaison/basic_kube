#!/usr/bin/env bash


python -m grpc_tools.protoc \
    -I/basic_kube \
    --python_out=/basic_kube \
    --grpc_python_out=/basic_kube \
    /basic_kube/hello/grpc/hello.proto

python manage.py grpcrunaioserver 0.0.0.0:50051
