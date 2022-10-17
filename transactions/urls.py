from django.urls import path

from transactions.views.auth_view import AuthView, LogoutView

urlpatterns = [
    path('api-token-auth/', AuthView.as_view()),
    path('api-token-logout/', LogoutView.as_view())
    # path("room", room_view.RoomAPIView.as_view(), name="room"),
    # path("room/<int:pk>", room_view.RoomAPIView.as_view(), name="room-by-pk"),
    # path("customer", customer_view.CustomerAPIView.as_view(), name="customer"),
    # path("customer/<int:pk>", customer_view.CustomerAPIView.as_view(), name="customer-by-pk"),
    # path("event", event_view.EventAPIView.as_view(), name="event"),
    # path("event/<int:pk>", event_view.EventAPIView.as_view(), name="event-by-pk"),
    # path("event/public", event_view.EventPublicAPIView.as_view(), name="event-public"),
    # path("event/book/<int:pk>", event_view.BookEventAPIView.as_view(), name="event-book"),
    # path("event/cancel/<int:pk>", event_view.CancelBookingAPIView.as_view(), name="cancel-booking"),
]
