import unittest
import boto3
import json
import Consumer

class TestConsumer(unittest.TestCase):
    
    def test_create_request_s3(self):
        client = boto3.client('s3')
        Consumer.widget_create_request('s3', self.widget)
        test_key = 'widgets/Kosta-Sergakis/10'
        curr_test = client.get_object(Bucket='usu-cs5260-kosta-web', Key=test_key)
        test_json = json.load(curr_test['Body'])
        
        self.assertEqual(test_json['type'], 'create')
        self.assertEqual(test_json['requestId'], '27272727')
        self.assertEqual(test_json['widgetId'], '10')
        self.assertEqual(test_json['owner'], 'Kosta Sergakis')
        self.assertEqual(test_json['label'], 'XYYYY')
        self.assertEqual(test_json['description'], 'This is a unit test')
        self.assertEqual(test_json['otherAttributes'][0]['name'], 'name1')
        self.assertEqual(test_json['otherAttributes'][0]['value'], 'value1')
    
    def test_create_request_ddb(self):
        Consumer.widget_create_request('ddb', self.widget)
        test_key = 'widgets/Kosta-Sergakis/10'
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('widgets')
        response = table.get_item(
            Key={
                'owner' : 'Kosta Sergakis',
                'widget_id' : '10',
            }
        )
        
        test_json = response['Item']
        
        
        self.assertEqual(test_json['widget_id'], '10')
        self.assertEqual(test_json['owner'], 'Kosta Sergakis')
        self.assertEqual(test_json['label'], 'XYYYY')
        self.assertEqual(test_json['description'], 'This is a unit test')
        self.assertEqual(test_json['attributes'][0]['name'], 'name1')
        self.assertEqual(test_json['attributes'][0]['value'], 'value1')
        
        
        
    widget = {
        'type' : 'create',
        'requestId' : '27272727',
        'widgetId' : '10',
        'owner' : 'Kosta Sergakis',
        'label' : 'XYYYY',
        'description' : 'This is a unit test',
        'otherAttributes' : [
            { 
                'name' : 'name1',
                'value' : 'value1',
            },
        ]
    }
    
if __name__ == '__main__':
    unittest.main()