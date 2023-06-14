from enum import Enum
import json


class ResponseStatus(Enum):
    PENDING = 'pending'
    FULFILLED = 'fulfilled'
    REJECTED = 'rejected'


response = '''{
    "status":"fulfilled"
}'''

data = json.loads(response)
status = data['status']

print(ResponseStatus(status))
