from __future__ import print_function

import grpc
import users_pb2  # Importa os módulos gerados pelo protobuf para as mensagens
import users_pb2_grpc  # Importa os módulos gerados pelo protobuf para os serviços


def run():
    response = []  # Cria uma variável para armazenar a resposta do servidor

    # Cria um canal de comunicação inseguro com o servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        # Cria um stub (cliente) para o serviço definido no protobuf
        stub = users_pb2_grpc.UsersStub(channel)

        # Chama o método GetUsers do serviço
        response = stub.GetUsers(users_pb2.GetUsersRequest())

    print(response.users)  # Imprime a resposta recebida do servidor


if __name__ == '__main__':
    run()  # Executa a função run() ao rodar o script