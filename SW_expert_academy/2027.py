# 주어진 텍스트를 그대로 출력하세요.

print('''
#++++
+#+++
++#++
+++#+
++++# ''')

for a in range(0,5):
    print('+++++'[a].replace('+','#'))
