# CLI

- CLI : Command Line Interface
- GUI : Graphic User Interface
- prompt : gvg4991:~/workspace $ 명령어(command -option)
- ctrl+c / esc로 prompt를 빠져나옴



- ctrl+l / clear로 터미널 지우기
- shell
- echo $SHELL로 shell의 종류를 확인 가능
- echo : python에서 print와 비슷한 역할, 화면에 문자열 출력
- '': 있는 그대로 출력, "": 입력된 내용을 출력
- ''안에서 따옴표 출력 -> ?
- man ...
- 특정 command 매뉴얼 페이지
- help와 비슷한 역할로 인터넷 없이도 이용 가능
- 'q'로 빠져나옴

## git bash 단축키
- ctrl+l: 터미널 지움
- ctrl+c: 빠져나오기
- ctrl+a: 젤앞으로 커서 이동
- ctrl+e: 젤뒤로 커서 이동
- ctrl+u: 커서를 기준으로 앞쪽의 텍스트를 다 지움
- ctrl+k: 커서를 기준으로 뒷쪽의 텍스트를 다 지움 (c9에선 안돼)
- ctrl+w: 단어단위로 삭제 (c9에선 창 종료)
- ctrl+d: 터미널이 깨끗한 상태일때 터미널 종료
- (c9에서 alt+click: 커서 이동)
  ​    
## Exercises
1. 터미널에 'Hello. World'를 출력해보자.
2. `echo 'hello`라고 입력하고 이 문제상황에서 빠져나와보자.
3. echo 매뉴얼을 참고하여 줄 바꿈(개행, newline)을 하지 않고 'yo'를 추출해보자. => echo -n ''
4. `sleep`이라고 하는 명령어의 매뉴얼 페이지를 읽고, 우리의 터미널을 5초간 재워보자. => sleep 5
5. 이번에는 터미널을 100초간 재워 보고, 중간에 깨워 보도록 하자. => sleep 100 => ctrl+c

## Summary
- `echo <string>` : 화면에 문자열 출력. ex) echo hello
- `man <command>` : 특정 커맨드 매뉴얼 페이지. ex) man echo
- `^c` : 현재 입력중인 작업 취소(Cancel) 이후 새 줄 실행.
- `^a` : 현재 입력중이 줄 맨 앞으로 커서 이동.
- `^e` : 현재 입력중이 줄 맨 뒤로 커서 이동
- `^u` : 현재 커서 기준, 앞쪽 전체 삭제.
- `^k` : 현재 커서 기준, 뒷쪽 전체 삭제.
- `^w` : 현재 커서 기준, 앞쪽 단어 단위로 삭제. (c9에서는 사용 불가)
- `alt + click` : 클릭하는 곳으로 커서 이동.
- `방향키 위, 아래` : 명령어 히스토리 탐색
- `clear` or `^l` : 화면 정리(clear screen)
- `exit` or `^d` : bash 종료