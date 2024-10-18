from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("admindashboard/", views.admindashboard, name="admindashboard"),
    path("userdashboard/", views.userdashboard, name="userdashboard"),
    path("user_registration/", views.user_registration, name="user_registration"),
    path("user_login/", views.user_login, name="user_login"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("user_edit_profile/", views.user_edit_profile, name="user_edit_profile"),
    path("logout/", views.Logout, name="logout"),
    path("users/", views.users, name="users"),
    path("feedback/", views.feedback, name="feedback"),
    path("view_contacts/", views.view_contacts, name="view_contacts"),
    path("turfs/", views.turfs, name="turfs"),
    path("view_user_details/<int:myid>/", views.view_user_details, name="view_user_details"),
    path("delete_user/<int:myid>/", views.delete_user, name="delete_user"),
    path("add_turf/", views.add_turf, name="add_turf"),
    path("book_turf/", views.book_turf, name="book_turf"),
    path("bookturf/", views.bookturf, name="bookturf"),
    path("view_turf_details/<int:myid>/", views.view_turf_details, name="view_turf_details"),
    path("view_user_turf_details/<int:myid>/", views.view_user_turf_details, name="view_user_turf_details"),
    path("delete_turf/<int:myid>/", views.delete_turf, name="delete_turf"),
    path("edit_turf/<int:myid>/", views.edit_turf, name="edit_turf"),
    path("payment/", views.payment, name="payment"),
    path("mybookings/", views.mybookings, name="mybookings"),
    path("bookings/", views.bookings, name="bookings"),
    path("report/", views.report, name="report"),
    path("check_availability/<int:myid>/", views.check_availability, name="check_availability"),
    path("view_receipt/<int:myid>/", views.view_receipt, name="view_receipt"),
    path("post_feedback/", views.post_feedback, name="post_feedback"),
    path("delete_user/<int:myid>/", views.delete_user, name="delete_user"),
    path("delete_feedback/<int:myid>/", views.delete_feedback, name="delete_feedback"),
    path("delete_contact/<int:myid>/", views.delete_contact, name="delete_contact"),
]