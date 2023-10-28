
from django.urls import path
from . import views

urlpatterns = [

    path('youtube_list_user', views.youtube_list_user, name='youtube_list_user'),
    path('naver_blog_list_user', views.naver_blog_list_user, name='naver_blog_list_user'),

    path('youtube_user_preferred_tour_theme_type/<int:id>', views.youtube_user_preferred_tour_theme_type, name='youtube_user_preferred_tour_theme_type'),
    # path('youtube_user_address/<int:id>', views.youtube_user_address, name='youtube_user_address'),
    path('get_user_address/<int:id>', views.get_user_address, name='get_user_address'),
    path('get_user_preferred_region/<int:id>', views.get_user_preferred_region, name='get_user_preferred_region'),
    path('get_user_preferred_accommodation_type/<int:id>', views.get_user_preferred_accommodation_type, name='get_user_preferred_accommodation_type'),
    path('get_user_preferred_tour_theme_type/<int:id>', views.get_user_preferred_tour_theme_type, name='get_user_preferred_tour_theme_type'),

    # path('sign_up2/', views.sign_up_upload_image, name='sign_up_upload_image,'),
    # path('upload/image/', views.upload_image, name='upload_image,'),
    path('my_page/', views.my_page, name='my_page'),
    path('my_page/update/<int:id>', views.my_page_update, name='my_page_update'),
    path('my_page/update/username/<int:id>', views.my_page_update_username, name='my_page_update_username'),
    path('my_page/update/email/<int:id>', views.my_page_update_email, name='my_page_update_email'),
    path('my_page/update/password/<int:id>', views.my_page_update_password, name='my_page_update_password'),
    path('my_page/update/name/<int:id>', views.my_page_update_user_name, name='my_page_update_user_name'),
    path('my_page/update/phone/<int:id>', views.my_page_update_user_phone, name='my_page_update_user_phone'),
    path('my_page/update/address/<int:id>', views.my_page_update_user_address, name='my_page_update_user_address'),
    path('my_page/update/preferred_region_no/<int:id>', views.my_page_update_preferred_region_no, name='my_page_update_preferred_region_no'),
    path('my_page/update/preferred_accommodation_type_no/<int:id>', views.my_page_update_preferred_accommodation_type_no, name='my_page_update_preferred_accommodation_type_no'),
    path('my_page/update/preferred_tour_theme_type_no/<int:id>', views.my_page_update_preferred_tour_theme_type_no, name='my_page_update_preferred_tour_theme_type_no'),


    path('my_page/update/custom/<int:id>', views.my_page_update_custom, name='my_page_update_custom'),
    path('my_page/delete/move<int:id>', views.my_page_delete_move, name='my_page_delete_move'),
    path('my_page/delete/', views.my_page_delete, name='my_page_delete'),
    path('my_page/delete/view/', views.MyPageDeleteView.as_view(), name='my_page_delete_view'),


    path('youtube/list/<str:keyword>', views.youtube_list, name='youtube_list'),
    path('youtube/detail/<str:youtube_id>', views.youtube_detail, name='youtube_detail'),
    path('youtube/list/kdy/<str:keyword>', views.youtube_list_kdy, name='youtube_list_kdy'),
    path('youtube/detail/<str:keyword>', views.youtube_detail, name='youtube_detail'),
    path('youtube/all/lists/', views.youtube_all_lists, name='youtube_all_lists'),
    path('youtube/all/detail/<str:youtube_id>', views.youtube_all_detail, name='youtube_all_detail'),
    path('youtube/insert/', views.youtube_insert, name='youtube_insert'),
    path('youtube/update/<str:youtube_id>', views.youtube_update, name='youtube_update'),
    path('youtube/delete/<str:youtube_id>', views.youtube_delete, name='youtube_delete'),
    path('youtube/search/custom/form/', views.youtube_search_custom_form, name='youtube_search_custom_form'),
    path('youtube/search/custom/', views.youtube_search_custom, name='youtube_search_custom'),
    path('youtube/search/ajax/form', views.youtube_search_ajax_form, name='youtube_search_ajax_form'),
    path('youtube/search/ajax/', views.youtube_search_ajax, name='youtube_search_ajax'),

    path('naver_blog/list/<str:keyword>', views.naver_blog_list, name='naver_blog_list'),
    path('naver_blog/detail/<str:naver_blog_id>', views.naver_blog_detail, name='naver_blog_detail'),
    path('naver_blog/list/kdy/<str:keyword>', views.naver_blog_list_kdy, name='naver_blog_list_kdy'),
    path('naver_blog/detail/<str:keyword>', views.naver_blog_detail, name='naver_blog_detail'),
    path('naver_blog/all/lists/', views.naver_blog_all_lists, name='naver_blog_all_lists'),
    path('naver_blog/all/detail/<str:naver_blog_id>', views.naver_blog_all_detail, name='naver_blog_all_detail'),
    path('naver_blog/insert/', views.naver_blog_insert, name='naver_blog_insert'),
    path('naver_blog/update/<str:naver_blog_id>', views.naver_blog_update, name='naver_blog_update'),
    path('naver_blog/delete/<str:naver_blog_id>', views.naver_blog_delete, name='naver_blog_delete'),
    path('naver_blog/search/custom/form/', views.naver_blog_search_custom_form, name='naver_blog_search_custom_form'),
    path('naver_blog/search/custom/', views.naver_blog_search_custom, name='naver_blog_search_custom'),
    path('naver_blog/search/ajax/form', views.naver_blog_search_ajax_form, name='naver_blog_search_ajax_form'),
    path('naver_blog/search/ajax/', views.naver_blog_search_ajax, name='naver_blog_search_ajax'),


]

