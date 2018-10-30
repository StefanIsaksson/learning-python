import platform

message = f'Hello from Python {platform.python_version()}'
message_border = '*' * len(message)

print(message_border)
print(message)
print(message_border)