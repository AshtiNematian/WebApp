from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .form import CouponApplyForm
from .models import Coupon


class CouponApplyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        now = timezone.now()
        form = CouponApplyForm(request.data)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
                request.session['coupon_id'] = coupon.id
                return Response(status=status.HTTP_200_OK)
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
