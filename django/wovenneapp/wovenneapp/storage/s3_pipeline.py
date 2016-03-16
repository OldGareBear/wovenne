from django.contrib.staticfiles.storage import CachedFilesMixin, ManifestFilesMixin
from pipeline.storage import PipelineMixin
from storages.backends.s3boto import S3BotoStorage

class S3PipelineManifestStorage(PipelineMixin, ManifestFilesMixin, S3BotoStorage):
    """Class combining functionality from the pipeline and s3boto modules into
    a new storage backend that concatenates and compresses static assets;
    rewrites asset URIs to a remote asset host; and uploads static assets
    to that host -- all as part of static file collection.

    """

#
# The following lambdas are aliases for the concrete S3 storage classes used by
# static and media assets.
#
# Static assets should run through the asset pipeline before being uploaded
# to S3, while media assets can be uploaded to S3 directly.
#
# The location parameter is force set to make sure that the root of the
# S3 bucket is segmented by the corresponding asset type, that is,
#
#    wovenne-static-prod.s3.amazonaws.com/static
#    wovenne-static-prod.s3.amazonaws.com/media
#

StaticRootS3Storage = lambda: S3PipelineManifestStorage(location='static')
MediaRootS3Storage  = lambda: S3BotoStorage(location='media')
