from django.urls import path
from .views import CouponApplyAPIView

app_name = 'coupons'

urlpatterns = [
    path('apply-coupon/', CouponApplyAPIView.as_view(), name='apply_coupon'), ]
