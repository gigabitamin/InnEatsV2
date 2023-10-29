from django.contrib.auth.decorators import login_required


# settings.py TEMPLATES OPTIONS 에 추가
@login_required
def user_info(request):
    # 사용자 정보를 가져와서 컨텍스트 변수로 반환
    user_info = request.user
    # user_info = {
    #     'username': request.user.username,
    #     'email': request.user.email,
    #     # 다른 사용자 정보 필드 추가
    # }    
    return {'user_info': user_info}