"""
API Serializers for course home
"""

from rest_framework import serializers

from openedx.core.lib.api.serializers import CourseKeyField

from .common import CourseCommonSerializer


class UnsucceededCourseSerializer(serializers.Serializer):
    """Serializer for unsucceeded course"""
    display_name = serializers.CharField()
    course_key = CourseKeyField()
    org = serializers.CharField()
    number = serializers.CharField()
    run = serializers.CharField()
    is_failed = serializers.BooleanField()
    is_in_progress = serializers.BooleanField()
    dismiss_link = serializers.CharField()


class LibraryViewSerializer(serializers.Serializer):
    """Serializer for library view"""
    display_name = serializers.CharField()
    library_key = serializers.CharField()
    url = serializers.CharField()
    org = serializers.CharField()
    number = serializers.CharField()
    can_edit = serializers.BooleanField()


class CourseHomeSerializer(serializers.Serializer):
    """Serializer for course home"""
    allow_course_reruns = serializers.BooleanField()
    allow_to_create_new_org = serializers.BooleanField()
    allow_unicode_course_id = serializers.BooleanField()
    allowed_organizations = serializers.ListSerializer(
        child=serializers.CharField(),
        allow_empty=True
    )
    archived_courses = CourseCommonSerializer(required=False, many=True)
    can_create_organizations = serializers.BooleanField()
    course_creator_status = serializers.CharField()
    courses = CourseCommonSerializer(required=False, many=True)
    in_process_course_actions = UnsucceededCourseSerializer(many=True, required=False, allow_null=True)
    libraries = LibraryViewSerializer(many=True, required=False, allow_null=True)
    libraries_enabled = serializers.BooleanField()
    taxonomies_enabled = serializers.BooleanField()
    library_authoring_mfe_url = serializers.CharField()
    taxonomy_list_mfe_url = serializers.CharField()
    optimization_enabled = serializers.BooleanField()
    redirect_to_library_authoring_mfe = serializers.BooleanField()
    request_course_creator_url = serializers.CharField()
    rerun_creator_status = serializers.BooleanField()
    show_new_library_button = serializers.BooleanField()
    split_studio_home = serializers.BooleanField()
    studio_name = serializers.CharField()
    studio_short_name = serializers.CharField()
    studio_request_email = serializers.CharField()
    tech_support_email = serializers.CharField()
    platform_name = serializers.CharField()
    user_is_active = serializers.BooleanField()
