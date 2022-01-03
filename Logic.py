from proto import pokemon_pb2, pokemon_pb2_grpc


class RequestRpc(pokemon_pb2_grpc.PokemonServicer):
    def GetByNo(self, request, context):
        if request.id == 1:
            pokemonDetail = pokemon_pb2.PokemonDetail(id=11, name="喷火龙")
        else:
            pokemonDetail = pokemon_pb2.PokemonDetail(id=22, name="葫芦娃")
        return pokemonDetail