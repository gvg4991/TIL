# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
#     <link href="https://fonts.googleapis.com/css?family=Do+Hyeon" rel="stylesheet">
#     <!-- 구글폰트에서 폰트를 선정 후 주소를 가지고 옴 -->
#     <link rel="stylesheet" href="06_font.css">
#     <!-- 링크를 통해 css를 연결할 땐 위 코딩이 필수적임 -->
# </head>
# <body>
#     <p class="font">
#         Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
#     </p>
# </body>
# </html>


# .font {
#     font-size: 40px;
#     font-style: italic;
#     font-weight: 700; /* bold */
#     font-family: 'Times New Roman', Times, serif;
#     /* '구글폰트'에서 폰트를 가지고 올 수 있다. */
#     line-height: 1.2;  /* 1.5배수 */
#     letter-spacing: -2px;  /* 장평이 (+)넓어짐 (-)좁아짐 */
#     text-align: center;  /* 가운데 정렬 */
# }



# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
#     <style>
#         /* 1. color name */
#         h1 {
#             color: red;
#         }
#         h2 {
#             color: #0000ff;
#         }
#         h3 {
#             color: rgb(0,255,0);
#         }
#         p {
#             color: rgba(255,0,0,0.3);
#         }
#         /* 단위 길이(font-size) */
#         html {
#             font-size: 10px;
#         }
#         ol {
#             font-size: 1.2rem;
#             /* 10px*1.2=12px */
#         }
#         ul {
#             font-size: 1.2em;
#             /* 10px(html)*1.2(ul)*1.2(li)=14.4px */
#         }
#         .em {
#             font-size: 1.2em;
#         }
#         .vh {
#             font-size: 5vh;
#             /* 브라우저의 세로길이에 맞게 글씨 크기 변동 */
#         }
#         .vw {
#             font-size: 5vw;
#             /* 브라우저의 가로길이에 맞게 글씨 크기 변동 */
#         }
#     </style>
# </head>
# <body>
#     <div>
#         저는 10픽셀입니다.
#     </div>
#     <ol>
#         <li>저는 1.2rem입니다.</li>
#     </ol>
#     <ul>
#         <li class="em">저는 1.2em입니다.</li>
#     </ul>

#     <span class="vh">5vh</span>
#     <span class="vw">5vw</span>

#     <h1>빨간색</h1>
#     <h2>파란색</h2>
#     <h3>초록색</h3>
#     <p>흐릿한 빨간색(투명도)</p>
# </body>
# </html>



# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
#     <style>
#         /* 전체 선택자 */
#         *{
#             color: red;
#         }
#         /* 태그 선택자 (h1에 적용) */
#         h1,p {
#             color: rosybrown;
#         }
#         /* 클래스 선택자 (클래스명이 블루인 클래스에 적용) */
#         .blue {
#             color: blue;
#         }
#         /* #아이디 선택자 */
#         #green {
#             color: green;
#         }
#         .pink {
#             color: pink;
#         }
#     </style>
# </head>
# <body>
#     <p>red, 전체 선택자</p>
#     <h1>rosybrown, 태그 선택자</h1>
#     <h2 class="blue">blue, c.클래스 선택자</h2> 
#     <h3 id="green">green, #아이디 선택자</h3>
#     <!-- 클래스는 .class / 아이디는 #id -->
#     <h1 class="blue">h1 vs .blue ? class 승</h1>
#     <h1 id="green">h1 vs #green ? id 승</h1> 
#     <h1 id="green" class="blue">h1 vs #green vs .blue ? id 승</h1>
#     <!-- 전체 선택자 < 태그 < 클래스 < 아이디 -->

#     <p>낸 <span class="blue">파랑색</span>이고, 여는 <span class="pink">핑크색</span>일 수 있나?</p>
# </body>
# </html>