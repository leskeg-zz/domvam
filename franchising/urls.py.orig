from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

# from mongoadmin import site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'franchising.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # SECURITY WARNING: not for production use!
    
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True})
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(site.urls)),
    url(r'^admin/?$', 'realty.views.admin_login', name='admin_login'),
    url(r'^adminpage/', include('mongonaut.urls')),
    url(r'^$', 'realty.views.home', name='home'),
    url(r'^-+(?P<filter_words>[\w-]+)/?$', 'realty.views.home', name='home'),
    url(r'^card+(?P<obj_id>[\w]+)/?$', 'realty.views.card', name='card'),
    url(r'^agency-page+(?P<obj_id>[\w]+)/?$', 'realty.views.agency_page', name='agency_page'),
    url(r'^add-card$', 'realty.views.add_card', name='add_card'),
    url(r'^action-card$', 'realty.views.action_card', name='action_card'),
    url(r'^register$', 'realty.views.register', name='register'),
    url(r'^agency_list$', 'realty.views.agency_list', name='agency_list'),
    url(r'^registerAgency$', 'realty.views.registerAgency', name='registerAgency'),
    url(r'^login$', 'realty.views.login_view', name='login'),
    url(r'^logout$', 'realty.views.logout_view', name='logout'),
    url(r'^user-profile$', 'realty.views.user_profile', name='user_profile'),
    url(r'^add-review/(?P<obj_id>[\w]+)/?$', 'realty.views.add_review', name='add_review'),
    url(r'^feedback/(?P<obj_id>[\w]+)/(?P<review_id>[0-9]+)/?$', 'realty.views.feedback', name='feedback'),
    url(r'^favorite-cards$', 'realty.views.favorite_cards', name='favorite_cards'),
    url(r'^my-cards$', 'realty.views.my_cards', name='my_cards'),
    url(r'^mobile', 'realty.views.mobile_filter', name='mobile_filter'),
    url(r'^authmobile', 'realty.views.mobile_auth', name='mobile_auth'),
    url(r'^support', 'realty.views.ticket', name='ticket'),
    url(r'^enable_user', 'realty.views.enable_user', name='enable_user'),
    url(r'^action_agency_by_username', 'realty.views.action_agency_by_username', name='action_agency_by_username'),
    url(r'^validate_email_agency', 'realty.views.validate_email_agency', name='validate_email_agency'),
    url(r'^disable_user', 'realty.views.disable_user', name='disable_user'),
    url(r'^make_user_admin', 'realty.views.make_user_admin', name='make_user_admin'),
    url(r'^unmake_user_admin', 'realty.views.unmake_user_admin', name='unmake_user_admin'),
    url(r'^add_profile_image', 'realty.views.add_profile_image', name='add_profile_image'),
    url(r'^add_agency_details', 'realty.views.add_agency_details', name='add_agency_details'),
    url(r'^yandex_+(?P<num>[\wd]+)+.txt', 'realty.views.yandex_txt', name='yandex_txt'),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'ef99b3aebfcd135529b9b21ae.html', 'realty.views.ef99b3aebfcd135529b9b21ae', name='ef99b3aebfcd135529b9b21ae'),


    # ajax requests:
    url(r'^one_card', 'realty.views.one_card', name='one_card'),
    url(r'^get_contact_phone', 'realty.views.get_contact_phone', name='get_contact_phone'),
    url(r'^edit_contact_list', 'realty.views.edit_contact_list', name='edit_contact_list'),
    url(r'^add_new_contact', 'realty.views.add_new_contact', name='add_new_contact'),
    url(r'^add-favorite-card', 'realty.views.add_favorite_card', name='add_favorite_card'),
    url(r'^get_regions', 'realty.views.get_regions', name='get_regions'),
    url(r'^ajax/add/get_cat_tabs', 'realty.views.ajax_get_cat_tabs', name='get_cat_tabs'),
    url(r'^ajax/add/get_cat_types', 'realty.views.ajax_get_cat_types', name='get_cat_types'),
    url(r'^ajax/get_filter', 'realty.views.ajax_get_filter', name='get_filter'),
    url(r'^ajax/get_favorite_cards', 'realty.views.get_favorite_cards', name='get_favorite_cards'),
    url(r'^ajax/get_cards', 'realty.views.get_cards', name='get_cards'),
    url(r'^ajax/ajax_add_card', 'realty.views.ajax_add_card', name='ajax_add_card'),
    url(r'^ajax/ajax_login', 'realty.views.ajax_login', name='ajax_login'),
    url(r'^ajax/ajax_register', 'realty.views.ajax_register', name='ajax_register'),
    url(r'^ajax/get_region_in_english', 'realty.views.get_region_in_english', name='get_region_in_english'),
    url(r'^ajax/get_region_autocomplete2', 'realty.views.get_region_autocomplete2', name='get_region_autocomplete2'),
    url(r'^ajax/get_region_autocomplete', 'realty.views.get_region_autocomplete', name='get_region_autocomplete'),
    url(r'^ajax/get_cat_type_commercial', 'realty.views.get_cat_type_commercial', name='get_cat_type_commercial'),
    url(r'^edit_user_profile', 'realty.views.edit_user_profile', name='edit_user_profile'),
    url(r'^ajax/ajax_upload_image', 'realty.views.ajax_upload_image', name='ajax_upload_image'),
    url(r'^ajax/ajax_get_region_counters', 'realty.views.ajax_get_region_counters', name='ajax_get_region_counters'),
    url(r'^ajax/ajax_get_my_cards', 'realty.views.ajax_get_my_cards', name='ajax_get_my_cards'),
    url(r'^ajax/ajax_get_my_favorites', 'realty.views.ajax_get_my_favorites', name='ajax_get_my_favorites'),
    url(r'^ajax/get_address_autocomplete', 'realty.views.get_address_autocomplete', name='get_address_autocomplete'),
    url(r'^add_info_agency', 'realty.views.add_info_agency', name='add_info_agency'), 
    url(r'^get_cards_agency', 'realty.views.get_cards_agency', name='get_cards_agency'), 

    url(r'^test', 'realty.views.test', name='test'),

    url(r'^captcha/', include('captcha.urls')),


    
)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


