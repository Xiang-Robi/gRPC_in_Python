import grpc
import time
from concurrent import futures

import fibonacci_pb2
import fibonacci_pb2_grpc


ONE_HOUR_IN_SECONDS = 3600


# usually iterative version has less overhead than recursive version,
# because you can control what info to put into the iterative stack,
# while the recursive stack (return address, local variables, etc.) is handled implicitly.
def iterative_fibonacci(n):
    if n <= 1:
        return n

    cache = [0, 1]
    for _ in range(1, n):
        cache[1], cache[0] = cache[0] + cache[1], cache[1]

    return cache[1]


class FibonacciServicer(fibonacci_pb2_grpc.FibonacciServicer):
    def __init__(self, port=6000):
        self.port = port

    # implementation of the Fibonacci service declared in the proto file
    def Fibonacci(self, request, context):
        response = fibonacci_pb2.FibonacciMessage()
        response.value = iterative_fibonacci(request.value)
        return response

    def start_server(self):
        # create a gRPC server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        fibonacci_pb2_grpc.add_FibonacciServicer_to_server(FibonacciServicer(), server)

        # bind the server to the specified port
        server.add_insecure_port('[::]:{}'.format(self.port))
        server.start()
        print('Server started. \nListening on port {}.'.format(self.port))

        # keep the server alive
        try:
            while True:
                time.sleep(ONE_HOUR_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)


if __name__ == '__main__':
    server = FibonacciServicer()
    server.start_server()
