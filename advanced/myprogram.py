# 같은 패키지 내 임포트 

# 메소드 임포트 
# from mymodule import useful_func

# 클래스 임포트
# from mymodule import UseFulClass, useful_func
# useful_func() # 자동 캐시화 

# myinstance = UseFulClass('hello')
# myinstance.report()



# 다른 패키지내 임포트 
from mypackage.mysubmodule import my_sub_func

my_sub_func();