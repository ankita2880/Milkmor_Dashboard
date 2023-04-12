from rest_framework.response import Response
from .serializers import UserLoginSerializer
from rest_framework.views import APIView
from login import models
from login import serializers
from login import utils



class UserLogin(APIView):
    def post(self, request):

        # serializer_instance  = UserLoginSerializer(data = reqeust.data)
        print('postttttttttttttt',request.data)
        serializer_instance = serializers.UserLoginSerializer(
            data=request.data
        )
        if not serializer_instance.is_valid():
            return utils.create_response(
                serializer_instance.errors, 400, message="Data is not valid"
            )
        mobile_no = serializer_instance.validated_data.get("mobile_no")
        print("=======+>",serializer_instance.validated_data,mobile_no)
        user_instance = models.User.objects.filter(mobile_no =mobile_no ).last()

        if not user_instance:
            return utils.create_response({}, 400, message="Invalid mobile no")

        return Response(status=200, data = "Success ")

class UserForgotPassword(APIView):
    def post(self,request):
        
        print('otppppppppppppppppppppppppppppppppppp',request.data)
    
        return Response(status=200, data = "Success OTP")
