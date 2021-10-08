from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class S3Boto3StorageCustom(S3Boto3Storage):
    """
        You can change it on your own Risk
    """
    pass





class ForgivingManifestStaticFilesStorage(ManifestStaticFilesStorage):
    """
        When the file is missing during collectstatic command, let's forgive and ignore that
    """
    def hashed_name(self, name, content=None, filename=None):
        try:
            result = super().hashed_name(name, content, filename)
        except ValueError:
            # if the fille are missing, let's forgive and ignore that.
            result = name
        return result