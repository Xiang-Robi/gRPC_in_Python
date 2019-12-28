import grpc

# fibonacci_pb2 contains the message class
# fibonacci_pb2_grpc.FibonacciStub is the client class
# fibonacci_pb2_grpc.FibonacciServicer is the server class
import fibonacci_pb2
import fibonacci_pb2_grpc


class FibonacciClient:
    def __init__(self, host='localhost', port=6000):
        self.host = host
        self.port = port

        # open a gRPC channel, and then bind the client stub to the channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = fibonacci_pb2_grpc.FibonacciStub(self.channel)

    def calculate_fibonacci(self, n=3):
        # create message
        to_server_message = fibonacci_pb2.FibonacciMessage(value=n)

        # call the Fibonacci service via rpc
        response = self.stub.Fibonacci(to_server_message)
        return response.value

    def validate_user_input(self, s):
        try:
            num = int(user_input)
            if num < 0:
                return False
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    client = FibonacciClient()
    user_input = input("Please enter a non-zero integer: ")

    while True:
        if not client.validate_user_input(user_input):
            print('Invalid input.')
            user_input = input("Please enter a non-zero integer: ")
        else:
            user_input_number = int(user_input)
            print('You entered {}.'.format(user_input_number))
            break

    result = client.calculate_fibonacci(user_input_number)
    print('The Fibonacci number is {}.'.format(result))
