import base64
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from captcha.views import CaptchaStore, captcha_image

from rest_framework_simplejwt.views import TokenObtainPairView

from login.serializer import DmallTokenObtainPairSerializer


class CaptchaAPIView(APIView):

    def get(self, request):
        hash_key = CaptchaStore.generate_key()
        try:
            # 获取图片id
            id_ = CaptchaStore.objects.filter(hashkey=hash_key).first().id
            image = captcha_image(request, hash_key)
            # 将图片转换为base64
            image_base = 'data:image/png;base64,%s' % base64.b64encode(image.content).decode('utf-8')
            json_data = json.dumps({"id": id_, "image_base": image_base})
            # 批量删除过期验证码
            CaptchaStore.remove_expired()
        except:
            json_data = None
        return HttpResponse(json_data, content_type="application/json")


class DmallTokenObtainPairView(TokenObtainPairView):
    # 登录成功返回token
    serializer_class = DmallTokenObtainPairSerializer


# 在你的app文件下下的views.py中写入
# 首先，我们刚开始写接口的时候是这样的，这样是没有身份验证的，直接就访问成功
def aa(request):
    """业务逻辑"""
    return JsonResponse({"msg": "ok"}, json_dumps_params={"ensure_ascii": False})


# 现在生成了token之后，我们应该这样写：
# 把函数方法写成类的形式，继承APIView类。
# APIView是REST framework提供的所有视图的基类, 继承自Django的View，对Django中的View进行了拓展，具备了认证、授权、限流、不同请求数据的解析的功能。
class test(APIView):
    def get(self, request):  # 请求为get时的业务逻辑
        """业务逻辑"""
        return JsonResponse({"msg": "ok"}, json_dumps_params={"ensure_ascii": False})

    def post(self, request):  # 请求为post时的业务逻辑
        """业务逻辑"""
        return JsonResponse({"msg": "ok"}, json_dumps_params={"ensure_ascii": False})