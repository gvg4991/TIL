# GIT & GIT HUB

## Git에 내 정보 설정

- `git config --global user.name 'MH Seo'` : 이름 설정
- `git config --global user.email '@gmail.com'`: 이메일 설정
- `git config --global --list`: 정보 설정 확인



## Git repo를 처음 생성한 경우

- `'git init` : git 초기화, 지금 폴더를 git으로 관리하겠다! (관리하려는 폴더 안에서 입력)
- `'git remote add origin 주소` : 원격 저장소(remote repository) 주소 등록
  - `'git remote set-url origin 주소` : 원격 저장소 수정



## Git repo clone한 경우

- `git clone https://github.com/gvg4991/TIL.git MINHO`
  - git hub TIL에서 복사한 주소의 git 자료를 'MINHO'폴더 생성 후 내려받기
  - 이 경우 git init, git remote add origin을 하지 않아도 된다.



## Git commit & push

- `git status` : 현재 폴더의 git의 상태 확인
- `git add .` : 현재 폴더의 변경사항들을 commit하기 위해서 준비
  - `.` 대신에 특정 파일 이름도 가능(`.`은 전체 파일)
- `git commit -m 'D04 | 190107 | Typora'` : commit, 변경 사항 저장. 메세지는 자유롭게 작성 가능.
- `git push -u origin master` : remote로 등록된 원격저장소(remote repository)에 commit한 것들 올리기
  - 이후에는 `git push` 만 입력해도 동작합니다. `git clone`을 한 경우에도 해당.
  - 이 컴퓨터에서 최초 push 인 경우, 로그인 창이 뜨며 로그인을 해줍니다.



## Git pull

- `git pull`: github에 올라가 있는 내용들, 즉 commit들을 내려받는 것 (`git push`와 반대)
- 아침에 오자마자 git pull한번 하고 시작



## Git & GitHub 재설정

``` bash
#Git 이름, 이메일 재설정
git config --global user.name 'MH Seo'
git config --global user.email '@gmail.com'

git clone https://github.com/gvg4991/TIL.git MINHO
# - git hub TIL에서 복사한 주소의 git 자료를 'MINHO'폴더 생성 후 내려받기
cd MINHO
# - MINHO폴더로 들어가기

#GitHub 로그인 정보 초기화
git credential reject
# - 업데이트 정보 초기화
protocol=https
host=github.com
#(enter 한번 더 누르기)
git push
#로그인
# - 업데이트 정보 등록
```

