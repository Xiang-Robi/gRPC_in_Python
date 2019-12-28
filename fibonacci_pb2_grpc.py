# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import fibonacci_pb2 as fibonacci__pb2


class FibonacciStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Fibonacci = channel.unary_unary(
        '/Fibonacci/Fibonacci',
        request_serializer=fibonacci__pb2.FibonacciMessage.SerializeToString,
        response_deserializer=fibonacci__pb2.FibonacciMessage.FromString,
        )


class FibonacciServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Fibonacci(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FibonacciServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Fibonacci': grpc.unary_unary_rpc_method_handler(
          servicer.Fibonacci,
          request_deserializer=fibonacci__pb2.FibonacciMessage.FromString,
          response_serializer=fibonacci__pb2.FibonacciMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Fibonacci', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))