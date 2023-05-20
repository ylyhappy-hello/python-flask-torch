from minio import Minio
from minio.error import S3Error


def upload_file(bucket_name, save_file_name, local_file_path):
    try:
        # Create a client with the MinIO server playground, its access key
        # and secret key.
        client = Minio(
            "localhost:9000",
            access_key="ruoyi",
            secret_key="ruoyi123",
            secure=False
        )

        # Make 'asiatrip' bucket if not exist.
        found = client.bucket_exists(bucket_name)
        if not found:
            client.make_bucket(bucket_name)
        else:
            print(f"Bucket {bucket_name} already exists")

        res = client.fput_object(
            bucket_name, save_file_name, local_file_path,
        )
        print(res.location)
        print(f"{save_file_name} upload ok")
        return res.location

    except S3Error as exc:
        print("error occurred.", exc)
        return -1

upload_file("videostream", "ss.mp4", "/home/yly/evm/python-flask/yolov5/runs/detect/exp27/4cd76b71905a4ddb804c709b031f76c1.mp4")