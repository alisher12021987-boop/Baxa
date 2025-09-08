yosh=int(input('oshizzi kkiriting '))
obuna=int(input('qancha yil obuna boolgansiz '))
asosiy=15
jami=0
yoshchi=0
if yosh>50:
    print(f'yoshiz {yosh} bolgani uchun sizgaa 20% chegirma bor')
    jami=asosiy*0.20
    print(jami)
elif obuna>=3 and obuna<=4:
    print(f'obuna yili {obuna} bolgani uchun sizga 10% chegirma bor')
    yoshchi=asosiy*0.10
    print(yoshchi)
elif obuna>=5:
    print(f'sizda {obuna} dan kop bolgani uchun 15% chegirma bor')
    yoshchi=asosiy^0,15
    print(yoshchi)
