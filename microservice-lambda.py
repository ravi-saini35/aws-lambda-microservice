
from __future__ import print_function

import boto3
import json

print('Loading function')


def lambda_handler(event, context):
    '''Provide an event that contains the following keys:

      - operation: one of the operations in the operations dict below
      - tableName: required for operations that interact with DynamoDB
      - payload: a parameter to pass to the operation being performed
    '''
    print("Received event: " + json.dumps(event, indent=2))

    operation = event['operation']

    if 'tableName' in event:
        print(event['tableName'])
        dynamo = boto3.resource('dynamodb').Table(event['tableName'])
        print(dynamo.creation_date_time)
    
    operations = {
        'create': lambda x: dynamo.put_item(Item=x),
        # insert, update adn delete to be created.
    }

    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
