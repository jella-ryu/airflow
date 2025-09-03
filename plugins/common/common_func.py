def get_sftp():
    print('sftp 작업을 시작합니다.')

def regist(name, sex, *args):
    print(f'이름: {name})')
    print(f'성별: {sex}')
    print(f'기타 정보들: {args}')

def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타 정보들: {args}')
    # 값이 있는지 확인
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    # 값이 있으면 출력
    if email:
        print(email)
    if phone:
        print(phone)