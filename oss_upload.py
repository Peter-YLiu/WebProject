import oss2


def upload_to_oss(local_file_path, filename, bucket_name, access_key_id, access_key_secret, endpoint):
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    # 上传文件并设置为公共读
    bucket.put_object_from_file(filename, local_file_path, headers={'x-oss-object-acl': oss2.OBJECT_ACL_PUBLIC_READ})
    oss_url = f"https://{bucket_name}.{endpoint}/{filename}"

    return oss_url
