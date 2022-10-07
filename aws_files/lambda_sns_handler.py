import boto3

def lambda_handler(event, context):
    filepath = event['Records'][0]['s3']['object']['key']

    client = boto3.client('sns')

    client.publish(
        TargetArn='<<sns_topic_arn>>',
        Message=f'File "{filepath}" has been uploaded to the SFTP server',
        Subject='SFTP Upload Notification'
    )
