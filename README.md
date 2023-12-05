# gRPC
gRPC implementation of API for Reddit in an alternate universe

Generate pb files based on .proto file command: 
python3 -m grpc_tools.protoc -I../proto --python_out=. --pyi_out=. --grpc_python_out=. ../proto/reddit.proto