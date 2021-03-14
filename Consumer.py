import boto3
import json
import sys


def main():
    sys.argv[0];
    if(len(sys.argv) != 3):
        print("Invalid parameters")
        print("Usage: python Consumer.py [Storage (s3/ddb)] [Bucket name]")
    storageType = sys.argv[1]
    bucketName = sys.argv[2]


if __name__ == "__main__":
    main()