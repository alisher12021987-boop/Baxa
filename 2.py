a1=int(input('1-mahsulot narxi '))
a2=int(input('2- mahsulot narxi '))
a3=int(input('3-mahsulot narxi '))
sum=a1+a2+a3
jami=0
if sum>100 and sum<=199:
    print(f'{sum} bolgani uchun sizga 10% chegirma bor')
    jami=sum*0.10
    print(sum-jami)
elif sum>200 and sum<=499:
    print(f'{sum} bolgani uchun sizga 15% chegirma bor')
    jami=sum*0.15
    print(sum-jami)
elif sum>500:
    print(f'{sum} bolgani uchun sizga 20% chegirma bor')
    jami=sum*0.20
    print(sum-jami)



