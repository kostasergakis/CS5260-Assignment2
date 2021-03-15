import boto3
import json
import sys
import time



def main():
    sys.argv[0];
    if(len(sys.argv) != 3):
        print("Invalid parameters")
        print("Usage: python Consumer.py [Storage (s3/ddb)] [Bucket name]")
    storage_type = sys.argv[1]
    bucket_name = sys.argv[2]
    
    s3_request = boto3.resource('s3')
    s3_client = boto3.client('s3')
    
    bucket = s3_request.Bucket('usu-cs5260-kosta-requests')
    
    #while True:
        #check for requests in the bucket
    bucket_requests = []
    for item in bucket.objects.all():
        bucket_requests.append(item)
    
    print(bucket_requests[0])
    
    if len(bucket_requests) > 0:
        #get the most recent request 
        curr_request = s3_client.get_object(Bucket=bucket_name, Key=bucket_requests[0].key)
        #delete the request from the bucket (it is being used)
        #s3_client.delete_object(Bucket=bucket_name, Key=curr_request.key)
        request_json = json.load(curr_request['Body'])
        
        request_type = request_json['type']
        

        options[request_type](storage_type, request_json)
        
    else:
        time.sleep(.2)

def widget_create_request(storage_type, request_json):
    #TO DO in this assignment
    if(storage_type == 's3'):
        client = boto3.client('s3')
        bucket_name = 'usu-cs5260-kosta-web'
        key = 'widgets/' + request_json['owner'].replace(' ', '-') + '/' + request_json['widgetId']
        client.put_object(
            Body=json.dumps(request_json).encode('UTF-8'),
            Bucket=bucket_name, 
            Key=key
        )
        
    if(storage_type == 'ddb'):
        client = boto3.client('dynamodb')
        
        widget = {
            'widget_id' : request_json['widgetId'],
            'owner' : request_json['owner'],
            'label' : request_json['label'],
            'description' : request_json['description'],
            'attributes' : request_json['otherAttributes'],
        }
        table = ''
        client.put_object(
            
        )
        print(widget)
    #print(request_json)
    return

def widget_delete_request():
    #TO DO in the next assignment.
    return

def widget_change_request():
    #TO DO in the next assignment.
    return        

options = {
    'create' : widget_create_request,
    'delete' : widget_delete_request,
    'change' : widget_change_request,
}

if __name__ == "__main__":
    main()
    
    
