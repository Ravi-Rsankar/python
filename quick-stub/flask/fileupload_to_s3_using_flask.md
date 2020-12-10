# Upload file to the S3 bucket using Flask-Python

## Configurations

In Aws S3 management console create a bucket and make it `Public` 

Provide the **Access Key** and the **Secret Access key** for AWS

## Code Components

The python file is s3upload.py

The code implements two functionalities.

1. It takes the multipart file and persists in a specified directory
2. Upload the file to the S3 bucket

## Testing through rest client(Postman)

In postman, set method type to **POST**.

Then select Body -> form-data -> Enter your parameter name (**file** according to your code)

and on right side next to value column, there will be **dropdown "text, file"**, select **File**. choose your image file and post it.

For rest of **"text" based parameters**, you can post it like normally you do with postman. Just enter parameter name and select "text" from that right side dropdown menu and enter any value for it,  hit send button. Your controller method should get called.