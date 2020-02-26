# 어려운 물리학 난제를 풀기 위한 공동 연구에 삼성전자가 참가하게 되었다.
# 공동 연구에 필요한 여러 과제 중 삼성전자는 원자들의 움직임을 시뮬레이션 하는 역할을 담당하게 되었다.
#
#
#
# 원자들은 2차원 평면에서 이동하며 두 개 이상의 원자가 충돌 할 경우 충돌한 원자들은 모두 보유한 에너지를 방출하고 소멸된다.
#
#
#
# 원자의 움직임은 다음과 같다.
#
# 1. 원자의 최초 위치는 2차원 평면상의 [x, y] 이다.
#
# 2. 원자는 각자 고유의 움직이는 방향을 가지고 있다. (상하좌우 4방향)
#
#  - 상 : y 가 증가하는 방향
#
#  - 하 : y 가 감소하는 방향
#
#  - 좌 : x 가 감소하는 방향
#
#  - 우 : x 가 증가하는 방향
#
# 3. 모든 원자들의 이동속도는 동일하며 1초에 1 만큼의 거리를 이동한다.
#
# 4. 모든 원자들은 최초 위치에서 동시에 이동을 시작한다.
#
#   5. 두 개 이상의 원자가 동시에 충돌 할 경우 충돌한 원자들은 모두 보유한 에너지를 방출하고 소멸된다.
#
#
#
#
#
#
#
#
#
#
# [그림-1] 과 같이 원자들의 [x, y] 위치와 이동방향이 주어지고 각 원자들의 보유 에너지가 1 이라고 가정해보자.
# (실제 입력에서 원자들의 보유 에너지는 각각 다를 수 있다.)
#
#
#
# 충돌된 원자들이 소멸하면서 방출하는 에너지는 다음과 같다.
#
# -       1초 후에 I, J 원자가 충돌 후 소멸하면서 2 에너지 방출
#
# -       1.5초 후에 A, B 원자가 충돌 후 소멸하면서 2 에너지 방출
#
# -       2초 후에 D, E, G, H 원자가 충돌 후 소멸하면서 4 에너지 방출
#
# -       3초 후에 M, N 원자가 충돌 후 소멸하면서 2 에너지 방출
#
#
#
#   [그림-1]의 경우 시간이 흘러도 원자 C, F, K, L 은 영원히 충돌하지 않아 소멸되지 않는다.
#
#   따라서 원자들이 소멸되면서 방출하는 에너지의 총합은 10 이다.
#
#
#
# N 개의 원자들의 [x, y] 위치, 이동 방향, 보유 에너지가 주어질 때 원자들이 소멸되면서 방출하는 에너지의 총합을 구하는 프로그램을 작성하라.
#
#
#
#
#
# [제약 사항]
#
# 1. 원자들의 수 N 은 1,000개 이하이다. (1≤N≤1,000)
#
# 2. 각 원자들의 보유 에너지 K 는 1 이상 100 이하이다. (1≤K≤100)
#
# 3. 원자들의 최초 위치 [x, y] 는 -1,000 이상 1,000 이하의 정수로 주어진다. (-1,000≤x,y≤1,000)
#
# 4. 원자들은 2차원 평면 위에서 움직이며 원자들이 움직일 수 있는 좌표의 범위에 제한은 없다.
#
# 5. 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)로 주어진다.
#
# 6. 원자들은 동시에 1초에 이동 방향으로 1만큼 이동한다.
#
# 7. 원자들의 최초 위치는 서로 중복되지 않는다.
#
# 8. 원자들은 2개 이상의 원자들이 서로 충돌할 경우 보유한 에너지를 방출하면서 바로 소멸된다.
#
# 9. 원자들은 이동 방향은 처음에 주어진 방향에서 바뀌지 않는다.
#
# 10. 원자들이 충돌하여 소멸되며 방출되는 에너지는 다른 원자의 위치나 이동 방향에 영향을 주지 않는다.
#
#
#
# [입력]
#
# 입력의 가장 첫 줄에는 총 테스트 케이스의 개수 T가 주어진다.
#
# 그 다음 줄부터는 각 테스트 케이스가 주어지며 각 테스트 케이스의 첫째 줄에는 원자들의 수 N이 주어진다.
#
# 다음 N개의 줄에는 원자들의 x 위치, y 위치, 이동 방향, 보유 에너지 K가 주어진다.
#
# 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)로 주어진다.
#
#
#
# [출력]
#
# 테스트 케이스 T에 대한 결과는 “#T”을 찍고, 한 칸 띄고, 방출되는 에너지의 총합을 출력한다. ( T는 테스트케이스의 번호를 의미하며 1부터 시작한다. )


import sys
sys.stdin = open('input.txt')








#
# ----------------------------------------------
# 5
# 14
# -6 5 3 1
# -3 5 2 1
# -5 2 1 1
# 3 5 3 1
# 5 7 1 1
# 6 7 3 1
# 7 5 2 1
# 5 3 0 1
# -4 -4 1 1
# -4 -6 0 1
# 5 -3 2 1
# 4 -6 0 1
# 6 -4 1 1
# 9 -7 2 1
# 10
# -998 0 2 8
# -5 0 3 4
# 5 0 2 1
# 998 0 3 7
# 0 -5 0 5
# 0 6 1 9
# 5 3 3 8
# 6 3 3 5
# 7 3 3 1
# 10 3 2 5
# 100
# 377 -267 0 7
# -799 -305 3 5
# 411 -968 2 5
# 472 756 1 1
# -160 -499 0 7
# 95 -738 1 9
# -808 -332 3 2
# -14 818 2 7
# -87 -724 3 8
# -770 -768 2 3
# -765 425 3 7
# -690 -655 2 10
# 768 810 3 2
# 805 674 0 8
# -446 -965 0 5
# -447 -834 0 4
# 846 -948 3 10
# 799 286 0 10
# -398 409 3 5
# -465 963 3 4
# -300 365 2 10
# -667 -395 1 5
# -880 348 0 10
# -114 -510 2 3
# 94 238 0 6
# -490 -526 3 4
# 727 771 1 3
# -863 -196 0 10
# 587 511 3 2
# -745 272 0 9
# 11 183 3 2
# 570 -281 3 5
# 636 -408 2 2
# -594 370 0 6
# 882 -862 2 8
# 48 781 0 3
# -569 428 0 5
# 821 359 1 3
# -348 965 0 8
# -377 240 1 9
# 0 -37 0 7
# -48 512 2 2
# -860 -776 2 7
# 871 15 1 9
# -711 626 1 2
# -540 -744 0 8
# -985 943 0 5
# 490 157 2 7
# 271 -970 0 10
# -957 -856 3 3
# 886 -678 1 5
# 640 -665 1 7
# 25 -44 0 6
# 789 318 0 7
# 889 209 0 3
# -457 283 3 3
# 342 -689 0 2
# 759 980 1 5
# -953 -932 2 7
# 572 -215 1 3
# 57 105 0 6
# 95 608 2 3
# -393 191 2 5
# -409 -112 0 9
# 155 412 1 4
# 854 -316 1 1
# -379 -821 3 4
# 811 -882 1 10
# -396 -405 0 6
# 852 -850 2 4
# 810 -100 2 7
# -383 206 1 5
# 959 522 2 9
# 513 140 3 8
# 147 -538 2 1
# -69 50 0 6
# 944 534 1 3
# -543 183 0 1
# -301 -816 2 7
# 287 -316 1 2
# 58 -585 1 6
# -649 437 3 10
# 975 -692 0 8
# -814 503 0 2
# -342 -885 3 8
# -6 899 0 1
# -980 -24 0 6
# 942 476 1 10
# 562 -794 0 10
# 667 -123 0 8
# 257 694 1 6
# -988 -886 3 5
# -117 -882 2 6
# -529 709 1 9
# 332 -703 1 5
# 105 697 1 6
# -367 -658 1 8
# -321 -274 3 4
# 954 -70 0 5
# -731 -518 2 5
# 500
# -200 971 3 89
# -513 992 2 14
# -478 54 0 96
# -987 -899 1 29
# -602 451 1 58
# -324 671 2 81
# 751 423 0 1
# -828 316 1 92
# 23 -651 1 48
# 764 455 0 7
# -483 1000 1 41
# 615 244 3 22
# 865 -622 2 72
# 879 -390 1 73
# -804 442 1 57
# -518 622 0 15
# -436 -620 3 30
# -368 709 1 70
# -710 519 1 70
# -690 725 1 64
# 319 -954 0 23
# 205 -398 1 69
# 768 -913 2 89
# 638 -653 3 34
# -37 886 2 65
# 696 388 3 11
# -78 54 0 91
# 588 -238 3 82
# 75 -306 3 24
# -285 -613 3 78
# -803 -157 1 1
# -283 -555 2 98
# 563 523 2 41
# 481 345 3 47
# 551 -375 1 3
# 365 539 1 17
# -745 -353 2 74
# 656 922 3 91
# 278 273 2 56
# 233 -922 1 34
# 10 538 3 8
# -552 390 1 34
# -379 343 1 31
# -510 952 3 49
# 786 -930 2 34
# -800 620 1 30
# -896 -469 3 2
# 866 -376 0 43
# -494 9 1 99
# 736 -459 1 3
# -622 653 0 86
# 991 -146 0 29
# 144 -538 3 84
# -298 860 1 99
# -928 856 2 20
# -260 165 2 96
# -939 -395 3 45
# 662 32 3 27
# 877 840 2 41
# -426 -689 2 86
# 864 -845 1 31
# 195 -272 2 39
# 641 -177 1 6
# 147 500 0 42
# 986 79 2 95
# -273 555 2 81
# -531 267 3 92
# -371 -649 3 87
# -965 570 0 39
# 892 -728 2 66
# -184 -660 2 51
# -683 133 2 69
# 395 -233 2 60
# -143 514 3 54
# -681 140 2 22
# 220 -290 0 41
# 53 -36 3 61
# -316 754 3 67
# -588 -592 2 4
# -846 -217 0 72
# 961 -906 3 38
# 911 -976 2 69
# 645 500 1 75
# -408 840 0 63
# -135 931 3 77
# 147 390 2 43
# 798 605 0 36
# 747 883 2 87
# -340 821 1 85
# 674 911 3 64
# -36 -32 2 52
# 175 897 1 10
# -277 -854 1 22
# -719 615 3 93
# 647 602 2 8
# 610 318 3 60
# -729 -959 3 18
# 115 -789 2 44
# -150 -991 2 45
# -680 501 1 13
# -564 -127 2 21
# -232 67 1 66
# -567 -848 2 76
# 939 -58 0 4
# 630 -308 3 73
# 379 420 2 91
# -311 170 1 65
# -685 -262 1 41
# 869 714 1 58
# -30 -649 1 45
# -804 -402 1 79
# 107 -936 1 14
# -124 538 3 13
# 295 -751 0 61
# -88 834 2 21
# 877 897 1 42
# 934 -646 1 40
# 428 -968 0 91
# -484 612 3 21
# -326 -788 2 87
# -294 -318 0 23
# 117 616 0 17
# -492 468 2 9
# -604 231 1 99
# -646 -434 1 99
# 613 -616 0 68
# 290 -41 0 28
# 369 116 3 62
# -633 816 1 46
# 530 902 2 96
# -479 880 2 48
# -51 -45 1 73
# -841 -544 2 88
# 925 -109 1 19
# -290 736 0 77
# 360 972 3 53
# 663 964 0 83
# 400 198 2 41
# -948 709 0 14
# 39 -5 0 95
# -323 -29 0 23
# 194 3 1 25
# 781 -872 2 47
# 989 -65 0 12
# 954 991 3 25
# -977 -945 3 37
# 255 -566 0 44
# -647 989 3 10
# 546 137 3 39
# 682 876 2 5
# -944 -847 3 95
# -470 371 0 37
# -99 -408 3 89
# -875 -12 3 12
# -167 617 0 62
# -249 -221 2 61
# 455 572 2 29
# -425 878 2 24
# -104 -579 3 80
# -64 359 0 25
# -777 -200 0 79
# 357 -31 0 29
# 805 155 2 51
# 778 -572 1 41
# -601 726 3 44
# 497 338 3 17
# 218 369 2 44
# 591 -313 0 23
# -807 988 2 58
# 806 -65 3 29
# -266 787 0 84
# 905 451 0 46
# 681 -363 0 93
# 492 800 2 97
# -760 278 0 23
# -443 -645 3 76
# 139 -893 1 79
# 736 531 0 59
# -4 579 0 92
# -465 331 2 75
# 153 -821 2 76
# -958 10 2 11
# 237 -742 0 43
# 827 823 3 79
# 944 453 0 21
# 588 365 2 8
# 766 690 3 96
# 504 758 1 9
# 974 561 1 80
# -945 -66 1 52
# 539 -737 0 53
# -929 -489 2 26
# -462 149 0 53
# -764 -249 3 71
# -727 -887 0 7
# -432 632 3 31
# -391 -420 0 21
# -132 246 1 88
# -720 327 2 60
# -356 -697 1 89
# 922 913 1 98
# -266 473 1 49
# 59 -824 1 62
# -329 -432 1 34
# -923 364 1 69
# -249 -172 3 22
# 148 -678 3 29
# -425 -708 0 49
# 886 789 3 41
# 816 518 1 53
# -539 544 0 53
# 686 139 2 49
# 952 383 2 85
# 400 -725 3 3
# 886 -797 2 15
# -423 -969 2 90
# 781 917 2 54
# -609 586 3 32
# -874 -284 2 63
# -588 880 0 17
# -390 -311 0 56
# -60 645 1 82
# 544 -734 1 96
# -962 38 1 7
# -237 -236 1 36
# -698 -160 2 14
# 755 30 3 1
# 831 -466 1 17
# -265 -77 3 55
# 680 -295 0 24
# -779 -360 2 76
# -719 -466 3 65
# -957 -610 2 39
# 72 -99 0 26
# -900 -343 3 98
# -398 -939 2 38
# -434 -443 3 85
# 109 -69 2 28
# 579 -710 2 48
# -945 -539 1 7
# 388 -562 3 45
# 150 -897 3 45
# -275 358 1 43
# 565 -624 3 8
# -856 -97 3 36
# 888 264 1 39
# -673 -735 1 96
# 793 -536 3 82
# 114 -364 1 55
# 921 -507 0 46
# 743 -27 3 15
# -259 609 0 62
# -935 -141 1 88
# -385 601 2 5
# 233 956 3 95
# 349 -348 0 45
# -154 -701 0 96
# 692 -427 3 18
# 70 -66 3 51
# -922 -151 1 9
# -770 -844 3 14
# -182 805 1 85
# -132 584 0 10
# 14 -404 2 25
# -237 -173 3 50
# -46 -190 0 56
# 433 508 2 79
# -294 -604 1 68
# -402 366 2 78
# -301 -53 1 8
# -392 458 3 64
# -240 -924 3 62
# 98 -291 3 61
# -372 -118 2 93
# -889 -455 0 82
# -316 10 1 28
# -72 890 1 63
# -605 -440 0 81
# -116 473 1 38
# 984 -167 0 63
# -358 -736 1 26
# -434 -825 3 73
# 434 -263 0 37
# -749 -837 1 20
# -715 -279 2 82
# -281 388 0 49
# -68 -640 2 67
# 763 322 1 17
# -265 654 3 1
# 293 -209 1 11
# -956 -897 0 43
# -426 41 1 17
# 42 -65 3 34
# 668 386 2 31
# 40 -564 2 48
# -894 -797 2 47
# 275 122 1 65
# 270 -462 1 63
# -119 756 2 89
# 750 -213 1 67
# -880 193 2 80
# 162 -33 2 88
# 57 -897 1 65
# 951 -147 3 54
# 717 751 1 22
# 137 190 2 95
# -57 -112 3 22
# -693 504 0 85
# 2 747 1 68
# 809 759 0 88
# 881 351 2 93
# 165 106 3 77
# 64 -298 1 2
# -39 -776 2 8
# 781 -715 3 47
# 453 -993 0 36
# 971 -823 0 69
# -862 -402 3 6
# -36 4 3 33
# -457 -992 3 33
# 130 -768 3 87
# 992 -666 3 85
# 3 -187 2 59
# -675 -674 3 19
# 117 158 1 16
# 116 536 0 22
# -434 473 2 8
# -435 819 3 74
# 31 930 1 85
# -847 679 3 75
# -981 -75 3 11
# -259 -51 2 11
# 83 942 2 28
# -367 78 3 61
# 504 255 3 99
# -363 254 3 95
# -562 -34 3 33
# 309 867 0 73
# 546 911 0 79
# 443 -179 0 91
# 818 624 1 17
# 513 -53 0 19
# 642 680 0 45
# 593 -756 3 68
# -671 354 3 50
# -256 226 2 45
# 603 -354 3 62
# -639 -146 3 52
# -428 -368 0 53
# 508 -928 3 35
# -597 668 0 75
# -798 -320 2 34
# -270 -311 0 53
# 173 -957 3 100
# 518 342 1 53
# 349 -581 1 89
# 909 479 0 94
# 299 848 0 18
# 770 724 2 40
# -594 -341 1 13
# 980 901 1 46
# -506 567 2 85
# 170 -954 1 99
# -809 -904 3 75
# -816 15 0 56
# 249 -126 2 88
# -231 -563 3 53
# -919 -503 0 29
# 468 10 3 24
# 535 3 2 88
# -6 -359 1 5
# -895 -71 1 54
# -429 677 2 16
# 148 718 2 4
# 241 985 3 46
# -965 -785 3 44
# 136 -880 2 40
# 300 524 0 43
# -273 -903 3 2
# 235 920 3 45
# 288 235 0 1
# 217 900 0 98
# -673 877 2 78
# -500 -702 2 1
# -765 -829 2 37
# 725 257 0 15
# 416 468 0 75
# 403 783 1 73
# 363 800 3 37
# 856 659 0 11
# -778 464 0 98
# 390 191 0 78
# -180 -62 2 16
# -574 44 1 19
# 410 395 0 4
# 366 944 2 73
# -124 -687 3 33
# 897 -558 2 27
# 929 430 0 45
# 549 46 3 63
# 1000 -466 0 1
# 950 -811 1 37
# -141 -395 3 20
# -944 540 3 18
# -286 55 0 95
# -904 -345 1 97
# 3 -458 3 48
# 501 -266 1 50
# -815 655 2 7
# -733 -545 2 61
# -274 -86 1 83
# -914 -83 0 23
# 567 -858 2 15
# -351 -832 2 54
# 555 -340 1 63
# 949 -169 3 40
# -655 -916 1 6
# 287 565 1 92
# -730 966 1 79
# 1 634 1 45
# -819 -726 0 13
# -830 -438 1 97
# 0 724 2 33
# 276 125 1 43
# -748 -555 0 63
# -161 -48 2 70
# 61 249 0 9
# -977 -541 2 12
# -646 740 3 28
# 962 874 2 39
# 307 760 2 26
# -955 -385 2 75
# -266 -312 1 30
# 940 -235 1 74
# -30 -666 3 8
# 806 872 2 59
# -806 163 3 92
# 1000 -895 1 64
# 253 133 0 35
# 251 -736 0 28
# 425 858 2 18
# 783 -140 2 61
# 924 -875 3 94
# -322 63 3 67
# 358 -498 0 98
# -306 -529 1 63
# 915 -707 1 12
# -438 992 1 97
# 7 82 1 28
# -510 57 0 90
# 155 -384 3 47
# -346 686 3 83
# -690 -946 2 90
# 883 894 0 100
# -574 -974 1 60
# -920 679 2 86
# -776 571 0 56
# 867 -871 0 98
# -551 388 2 68
# -324 -397 3 36
# -179 449 0 7
# 833 255 0 85
# -271 -546 0 48
# 589 -581 3 44
# 124 628 0 12
# 143 -679 2 97
# -102 851 3 53
# 866 637 2 21
# 712 -347 3 42
# -9 405 2 27
# -688 282 2 27
# 48 271 3 55
# -696 -867 0 75
# -267 581 2 34
# 395 -992 3 49
# -729 -178 2 15
# 362 720 3 82
# 487 -855 1 17
# -22 806 3 10
# -402 -756 0 78
# -78 63 2 39
# 727 823 0 1
# -606 695 2 65
# 625 155 1 97
# 203 791 0 4
# -624 -506 3 49
# 576 403 2 69
# 562 -434 0 50
# 437 -528 0 61
# -602 916 3 31
# -352 -416 0 32
# -413 -158 0 20
# -277 838 2 71
# -857 -68 2 23
# -735 791 0 95
# 937 -75 0 10
# 115 -498 3 84
# 696 -806 1 96
# -34 686 0 7
# -252 -950 3 48
# 1000
# -791 -788 2 1
# -606 755 2 65
# -328 493 2 95
# 236 793 0 56
# 43 51 3 11
# 559 813 3 40
# 318 428 2 32
# -724 87 1 58
# -456 232 1 15
# 192 -295 2 78
# 739 -606 3 57
# -233 226 3 80
# 764 -997 3 84
# 126 -292 2 66
# 446 1 1 49
# -235 -943 3 28
# 388 -46 0 16
# -268 -261 0 22
# -235 -67 3 72
# -716 312 3 94
# -166 729 1 15
# -246 -421 3 7
# -833 -835 1 83
# -358 -936 2 35
# 844 755 2 4
# 164 95 2 38
# -627 -808 0 83
# -706 -536 3 89
# 825 -796 1 73
# -255 -296 3 68
# -312 -766 0 94
# -309 442 2 84
# 194 -31 2 54
# -806 -402 2 62
# 357 -533 0 3
# 859 -64 0 18
# -519 624 2 5
# 957 -796 1 45
# 396 -516 3 81
# 754 -890 3 39
# 155 399 3 83
# 828 659 1 49
# -805 -233 0 20
# -155 68 2 56
# -768 -357 1 96
# 798 279 3 57
# -142 -846 2 21
# -529 -925 0 55
# -885 -201 2 78
# 632 526 3 80
# 544 810 0 97
# -827 281 1 4
# -315 624 2 5
# -16 472 3 44
# 818 -807 1 29
# -207 681 2 77
# -101 -605 3 3
# -777 -223 0 94
# -13 524 3 3
# -931 587 1 86
# -371 -107 1 33
# -712 405 2 43
# -297 510 3 62
# 475 -398 1 72
# -993 614 2 64
# 26 85 3 52
# -456 51 3 81
# -186 -668 1 13
# -222 987 2 56
# -714 -210 0 10
# -630 -277 2 16
# -932 607 1 33
# -876 -401 2 71
# 766 -798 2 10
# 659 990 2 16
# -509 698 2 57
# 31 655 0 21
# -895 -824 1 28
# -646 168 0 30
# 942 -958 2 79
# -140 954 1 76
# -523 -282 3 75
# 456 905 1 31
# 243 -547 1 16
# 463 -647 0 17
# 684 697 0 34
# 869 -365 2 48
# -239 -655 3 15
# 508 490 1 72
# 497 -189 3 47
# 240 -935 0 59
# 10 200 3 39
# -418 -498 2 39
# -242 -933 3 92
# 809 -372 0 23
# -254 -714 2 41
# -215 -765 3 91
# 967 493 2 56
# -254 709 3 39
# -453 -620 3 73
# -178 -20 2 92
# -128 -401 0 89
# 1000 -390 1 47
# -827 -273 1 76
# 844 675 2 8
# -920 860 3 11
# 889 -474 1 84
# 654 770 0 16
# 797 -369 0 87
# 879 677 0 33
# 197 -993 3 87
# 378 859 1 69
# -235 -496 0 71
# 594 347 0 23
# -737 -823 3 82
# -810 979 1 60
# -194 -243 0 41
# 176 531 3 29
# 582 206 0 52
# -9 -289 2 87
# 807 -368 0 34
# -443 474 3 86
# -109 -974 1 60
# -431 205 3 54
# 820 -632 1 82
# 727 224 0 33
# -483 -946 1 22
# 206 899 3 59
# -89 -574 1 94
# -414 -902 1 88
# -526 -847 3 87
# -491 234 2 2
# -253 -307 0 73
# 542 155 1 96
# 549 -392 2 52
# 267 626 2 68
# -55 466 0 86
# -656 661 2 74
# -99 -157 1 38
# 32 935 2 3
# -333 663 1 54
# -313 -942 0 23
# 148 -612 2 70
# 225 -822 1 91
# 710 294 1 56
# -449 688 1 11
# 228 -402 3 62
# 717 261 3 41
# -902 -74 0 75
# -462 -246 2 13
# 470 873 3 17
# -66 431 1 91
# -316 159 3 84
# -519 794 0 93
# 701 -874 0 50
# -306 6 0 62
# -268 -163 0 21
# -731 -600 3 19
# 342 -747 3 33
# -198 341 2 61
# -977 524 0 99
# 963 180 1 69
# -8 -150 1 67
# 399 -205 2 67
# 442 216 3 91
# 866 488 3 52
# 529 183 3 37
# -954 -795 3 45
# 68 -938 2 33
# 633 881 1 14
# -49 403 2 84
# 326 -905 1 51
# -472 -661 3 83
# 609 -154 1 49
# -779 -227 3 22
# 685 -595 2 82
# -915 -591 2 89
# -574 -983 0 57
# -889 -874 3 46
# 771 -48 1 92
# -771 -52 1 9
# -907 -860 2 38
# 293 -653 3 19
# -462 157 1 33
# -726 159 0 84
# -161 -953 2 21
# 683 327 0 73
# 332 753 2 66
# 953 -507 1 86
# 462 872 3 66
# -208 -559 2 1
# 739 264 1 49
# 509 -632 0 69
# 170 -485 2 84
# 308 767 0 92
# 918 718 3 38
# 42 387 2 6
# -832 873 1 42
# 699 -201 2 16
# 214 117 2 75
# -652 -697 1 73
# 518 -202 2 50
# -946 423 0 36
# 236 656 2 28
# -731 248 2 32
# -35 -430 3 65
# -823 629 1 51
# 956 688 0 42
# -972 -308 1 99
# -706 364 0 44
# -825 -268 0 12
# 802 -45 1 15
# 334 -586 3 36
# 413 469 0 56
# -686 -655 0 34
# 255 -458 2 43
# -285 -25 2 56
# 459 -488 1 54
# -401 -157 0 5
# -313 -151 1 36
# 120 -71 2 68
# 628 916 3 94
# -371 -669 3 2
# -542 -679 1 58
# 5 801 1 60
# 28 -121 0 83
# -315 865 0 3
# -988 -348 1 82
# -564 296 3 78
# 526 339 1 84
# 324 922 1 63
# 467 -738 2 26
# 674 -722 2 2
# 826 -809 3 100
# -277 866 0 1
# 460 764 3 38
# -478 -267 2 94
# 82 -994 2 86
# -224 -831 0 68
# 488 -817 2 76
# 675 -768 0 79
# 728 254 0 60
# 182 -122 3 3
# 760 922 1 80
# 51 416 2 85
# -675 18 2 51
# -706 834 2 74
# 32 488 0 27
# -605 195 1 30
# 162 465 1 76
# -39 142 2 22
# 204 -52 0 71
# 619 -767 1 26
# -661 -688 1 88
# -883 -612 0 13
# -587 166 3 56
# -353 910 3 68
# -883 -949 0 19
# -613 -640 1 42
# 632 -748 0 99
# 759 -465 1 66
# 510 -836 2 96
# -85 15 2 56
# -245 -705 2 66
# -572 -172 3 44
# -870 -164 1 50
# -283 -303 0 22
# 195 -423 1 81
# 677 -870 3 97
# 33 -819 2 32
# 281 -891 3 83
# -771 -711 2 14
# 160 -380 1 87
# 802 467 2 21
# -608 528 2 95
# -658 256 3 85
# -235 -961 3 14
# -598 -688 1 75
# -504 -476 1 47
# 818 -354 3 15
# 197 410 1 64
# -475 934 2 7
# 279 936 1 68
# -668 951 1 38
# 88 247 0 22
# -328 -413 3 98
# -482 828 2 76
# -697 699 1 78
# 325 536 2 16
# 257 -690 0 77
# 423 719 3 22
# -22 669 0 61
# 898 -558 3 100
# 949 -376 0 28
# -769 -455 3 37
# 777 -382 0 63
# -749 -207 1 27
# 507 -490 1 18
# 301 -617 1 45
# 893 996 0 25
# 871 -719 1 1
# -609 -875 0 86
# -797 915 0 39
# 631 -840 3 61
# -876 195 2 84
# -912 528 1 79
# -680 -353 3 32
# -750 -893 1 67
# 363 880 0 17
# -281 132 2 80
# 432 -116 1 97
# 63 -331 0 81
# 512 -541 1 20
# -630 444 0 99
# -934 192 0 20
# -226 261 3 43
# 664 -191 1 15
# -50 769 3 77
# -159 -636 1 68
# -923 -427 1 58
# -579 -232 2 2
# 524 931 1 39
# 55 -596 2 84
# -504 55 1 32
# -10 -391 3 3
# -588 -4 3 2
# 787 727 2 84
# 233 -618 2 21
# 278 512 1 11
# -722 -259 1 86
# -768 -363 3 76
# -748 922 1 7
# -514 -973 0 98
# -767 -886 2 2
# -946 -201 2 80
# -862 -549 1 17
# 951 -205 1 98
# -585 -536 1 86
# -276 -297 0 22
# -319 129 1 63
# -18 521 2 52
# 599 754 3 50
# -139 -872 2 100
# -284 -37 1 55
# 474 683 3 88
# 774 -473 3 68
# 835 873 1 52
# 228 -972 2 85
# 482 -741 2 64
# -752 -867 0 9
# 599 214 2 33
# 185 -560 1 99
# -177 -553 3 17
# 992 942 3 94
# -453 -118 2 6
# -611 -687 3 84
# 922 -627 0 71
# 226 -691 3 32
# -158 -727 1 71
# 70 742 2 4
# -603 -426 1 56
# -231 -445 3 44
# -224 925 2 29
# -778 758 2 93
# 917 456 0 49
# -119 -576 1 31
# 348 230 1 13
# -294 -690 0 51
# 527 -737 1 54
# 106 804 1 25
# -883 -344 2 77
# 836 724 1 3
# 261 306 1 49
# 367 703 2 5
# 297 970 0 68
# 477 925 3 7
# 221 920 2 66
# 57 206 2 34
# -657 945 2 77
# -111 659 2 31
# 430 -563 0 31
# -861 960 1 46
# -196 -911 3 16
# -177 954 2 69
# 420 -338 1 21
# -766 870 3 91
# -92 -135 2 29
# -395 -903 3 49
# -171 327 2 28
# 465 591 0 40
# 912 -350 2 12
# -259 848 3 84
# -7 -930 2 54
# -946 -17 1 7
# -308 460 2 79
# -498 407 0 84
# -208 -344 1 80
# -340 334 1 56
# 843 -82 0 52
# -470 141 0 97
# 741 687 1 78
# 733 -924 3 50
# 762 225 2 73
# -88 795 3 93
# -168 -426 1 66
# -654 -993 1 61
# -1000 -126 3 41
# -956 -539 2 40
# 639 -990 2 9
# 297 -989 3 81
# 607 -629 1 3
# 963 -198 2 19
# 644 -65 0 75
# -550 522 0 41
# 467 -793 1 55
# -557 766 1 68
# 98 -747 0 6
# 327 -259 3 16
# 401 -679 0 66
# 92 -694 3 63
# -399 -193 0 2
# -796 616 1 8
# -246 322 3 13
# 441 351 0 61
# -296 -159 1 33
# 706 548 1 26
# 245 -43 3 33
# 793 521 0 84
# -246 222 2 16
# -356 119 2 31
# -198 -671 1 72
# 558 -154 1 24
# 977 908 3 31
# 371 305 2 12
# 419 373 2 85
# 360 994 1 99
# -914 -836 2 28
# 612 697 1 38
# 485 306 3 31
# 616 -29 2 53
# -135 -205 3 80
# -182 -531 1 61
# 387 120 1 74
# 644 361 0 47
# 12 90 0 87
# -247 850 3 76
# -149 -968 0 31
# 995 778 0 31
# 241 -939 0 99
# 592 -166 0 86
# -463 -36 3 91
# 301 594 0 94
# -380 -593 0 85
# -734 -838 0 22
# -368 505 2 52
# 374 -94 3 3
# 667 -24 0 85
# -952 280 1 55
# -808 634 1 73
# -209 -249 0 93
# 185 -512 1 53
# 159 559 0 7
# -262 433 3 49
# 242 -171 3 69
# -375 13 1 6
# -656 -980 1 63
# -650 563 3 59
# 128 -779 1 22
# -593 -81 1 64
# 489 47 3 52
# 510 -520 0 14
# -607 610 3 84
# 34 613 0 37
# 191 -144 0 26
# 443 152 1 66
# 383 -261 3 53
# 669 743 2 97
# 372 220 0 4
# 467 278 1 52
# -826 -357 1 96
# 490 -825 1 62
# -894 177 2 54
# -171 258 3 82
# 179 365 2 77
# 278 -786 1 73
# 476 509 0 100
# 308 -87 1 39
# 735 164 3 46
# -984 -438 0 38
# -91 -546 3 44
# -953 953 1 38
# -305 1 1 79
# -523 -951 1 51
# -474 -820 3 68
# -838 188 2 58
# -719 -9 2 62
# -680 94 1 29
# 729 748 2 87
# -682 13 2 70
# -83 -366 2 67
# -316 678 0 100
# -700 -666 1 91
# 339 -888 2 34
# -675 527 1 63
# 786 -946 3 74
# -757 -800 0 61
# 790 -566 3 55
# 130 -914 3 4
# -498 734 0 64
# 382 -339 2 77
# 76 160 2 63
# 684 765 2 62
# 228 436 0 86
# -559 -953 1 70
# -212 668 0 81
# -324 -233 1 14
# 959 -682 2 22
# -843 933 1 28
# 291 -239 2 52
# 225 -222 3 90
# -359 193 2 84
# 860 -899 1 11
# -927 628 1 39
# 708 -79 3 78
# 263 993 2 35
# 72 260 3 65
# -165 -187 1 13
# -376 984 2 8
# -301 -508 1 61
# 97 -235 0 68
# 833 -814 1 94
# -327 630 3 64
# 804 25 0 30
# -630 838 0 71
# -268 418 1 99
# 49 -845 2 22
# 696 -759 1 46
# -959 503 3 92
# 194 351 2 14
# -347 -636 2 64
# 640 -589 0 7
# 635 -426 3 60
# -779 -464 1 2
# 546 -509 1 48
# 737 995 1 34
# 149 583 3 26
# 211 821 1 74
# 27 334 2 61
# -995 -975 1 71
# 161 -750 0 29
# 123 154 1 52
# -20 -537 0 8
# 1 -826 2 56
# 378 -828 0 89
# -745 -20 2 24
# -546 184 1 15
# -841 -785 3 26
# 721 -959 2 22
# -416 207 1 15
# -980 3 2 11
# -352 -511 3 2
# 175 113 2 59
# -141 -331 2 74
# 601 -893 0 72
# 698 -366 1 96
# -868 928 2 11
# 696 -893 2 15
# -923 -184 3 71
# -543 -207 0 26
# 982 772 1 65
# -330 -374 3 66
# -377 -430 2 90
# 79 -409 0 65
# -793 -841 3 49
# 416 918 2 44
# 305 631 0 62
# 70 -655 2 82
# -520 -211 2 51
# 209 235 3 39
# -80 -186 3 83
# 880 -461 2 22
# -499 -733 2 2
# 72 -152 0 90
# -403 449 0 99
# -501 -207 3 21
# 595 80 0 78
# 109 -721 1 100
# -118 -897 0 42
# 47 -671 2 17
# -946 304 1 88
# 105 -743 0 78
# -659 295 3 49
# 624 -57 2 95
# 490 832 3 16
# 870 -55 2 87
# 645 222 0 74
# 642 966 1 67
# 162 -411 2 5
# 828 -599 3 94
# 669 -281 2 30
# 187 -508 0 51
# -171 254 0 95
# 113 -691 1 39
# -668 -767 3 37
# 344 -406 1 88
# 98 973 1 39
# 166 -315 0 91
# -552 -959 0 5
# -444 -210 3 43
# 260 -918 2 49
# 324 -646 2 56
# 563 -280 1 70
# -49 -734 1 97
# -864 576 0 48
# -86 -337 3 90
# -203 -891 1 54
# -543 837 2 50
# 426 824 1 4
# -897 456 1 42
# -803 290 3 29
# -125 424 1 40
# 292 791 1 50
# 235 288 1 41
# -931 -207 1 41
# -510 -229 2 84
# 463 260 2 63
# -76 643 3 65
# -164 -677 0 82
# -100 -836 2 31
# -680 539 3 72
# -844 -342 1 94
# -384 482 1 10
# -631 144 2 61
# 499 945 0 78
# -626 -913 3 89
# 326 -525 1 85
# -832 -519 3 81
# 223 -992 3 58
# -173 775 3 100
# -477 -907 0 89
# 674 393 2 90
# 154 956 3 84
# -343 363 2 82
# 252 423 1 70
# -300 14 0 1
# -514 417 0 99
# 257 532 0 6
# 127 568 3 54
# -394 -639 2 49
# -210 148 3 67
# -404 -806 3 41
# 692 -383 0 89
# 377 -446 1 69
# -652 -750 2 9
# 579 -772 3 26
# 501 -634 1 97
# 480 -964 3 47
# 511 393 1 26
# -371 -553 2 60
# -282 784 2 11
# -51 791 3 60
# -719 523 2 7
# -961 -691 0 7
# -38 477 2 58
# -270 -443 0 92
# 912 839 0 77
# 814 -857 3 72
# 646 -83 0 46
# 781 -942 2 82
# -499 766 2 37
# -746 -385 0 93
# 570 -843 2 30
# -845 960 1 61
# 332 411 1 85
# -929 948 3 38
# -474 293 1 63
# -893 -156 0 75
# 471 -461 0 88
# 456 -113 1 28
# 628 -309 2 47
# -575 -571 3 56
# 356 50 3 96
# 193 926 1 48
# 660 705 1 7
# -218 31 3 11
# -609 -323 0 94
# 993 516 2 56
# 926 138 1 67
# -677 296 1 19
# 299 -23 2 39
# 589 -208 1 32
# 335 220 1 72
# -229 -348 2 94
# 206 784 1 12
# -918 -711 0 53
# -749 825 3 24
# 253 -207 3 52
# 734 -566 2 26
# -468 -340 0 44
# 333 432 0 4
# 661 887 2 64
# -399 737 3 10
# -195 -106 1 91
# -617 -396 1 40
# -769 49 2 61
# -36 -62 0 18
# 917 538 1 78
# -69 -796 2 29
# -847 563 1 21
# -244 -561 2 73
# 367 -587 0 78
# -660 -895 2 81
# -104 96 1 45
# 539 -725 3 21
# -501 586 0 57
# 393 675 0 25
# -431 -338 1 1
# 840 -431 3 35
# 833 332 1 86
# 386 -772 2 97
# 253 606 0 8
# -250 -241 3 64
# 658 611 1 32
# 478 -492 1 15
# -404 306 2 73
# 16 70 1 14
# 388 -219 1 88
# 776 -854 1 55
# -82 -94 0 13
# 383 727 1 20
# -362 821 1 61
# 935 638 1 71
# -212 -477 2 67
# -309 -79 0 4
# 86 -958 3 18
# 4 -445 0 35
# -117 972 3 30
# -37 285 0 44
# 550 -682 0 95
# 260 -727 0 84
# 567 731 0 48
# -240 114 1 23
# 594 544 3 46
# -940 -322 3 69
# 1 672 0 54
# 759 570 0 75
# -630 357 0 86
# 685 -853 3 60
# -529 -244 1 17
# 863 169 3 66
# -47 110 2 74
# 427 -991 0 69
# 745 -724 0 17
# 530 485 2 67
# -806 838 3 86
# -561 266 2 18
# 406 816 2 1
# -870 -121 2 76
# 313 471 3 68
# 78 563 1 63
# 956 -792 1 47
# -972 711 1 91
# 236 311 0 43
# 492 908 3 94
# -854 -474 0 95
# -564 812 2 51
# -803 747 2 62
# 475 -617 1 95
# -163 782 2 41
# 251 951 1 31
# 577 974 3 42
# 555 -875 0 9
# -169 906 3 29
# 901 -444 0 66
# -256 211 0 54
# 581 -717 0 25
# -784 964 3 57
# 935 682 2 87
# 410 -76 1 61
# 330 -5 0 93
# -282 121 1 94
# 375 225 0 13
# 959 -465 0 7
# -158 -900 3 29
# -218 868 1 88
# -945 151 1 11
# 51 656 1 49
# -486 -384 3 99
# -818 -517 0 17
# -787 -546 0 100
# -537 38 2 17
# 450 198 1 63
# -405 257 3 94
# -912 885 1 35
# -567 -438 0 82
# -954 363 2 23
# 964 705 3 88
# 760 907 2 83
# 498 439 3 80
# 342 -542 3 68
# -422 792 2 32
# 494 -72 3 39
# 852 -313 0 9
# 858 379 0 82
# 425 -354 3 66
# -405 515 1 2
# 422 -649 2 24
# -58 789 3 98
# 525 282 0 24
# -770 853 1 55
# -776 -31 3 36
# -632 838 1 70
# -212 -685 3 39
# -703 483 1 77
# 457 791 3 73
# -830 625 3 59
# -903 -64 3 60
# 496 -497 2 27
# -165 248 1 9
# -5 -821 2 69
# 651 373 3 27
# 187 294 3 81
# 445 921 2 55
# 188 918 3 69
# 818 861 3 58
# 229 -757 3 83
# -420 -491 0 67
# 143 622 2 37
# -529 -881 3 86
# 574 953 2 96
# -656 -949 0 26
# -355 -601 1 66
# 585 -441 2 76
# -138 -35 2 36
# 732 892 2 85
# 714 -594 1 52
# 577 760 0 69
# -988 -266 3 59
# 483 -606 0 78
# -60 68 3 100
# 909 -815 2 29
# 320 -666 2 76
# -829 176 2 1
# 595 46 0 40
# 166 650 1 58
# -704 -312 0 55
# 301 58 2 63
# -540 703 1 5
# -584 -959 2 37
# 519 537 3 45
# -850 -203 1 90
# -327 76 2 43
# -704 538 3 38
# 967 393 3 14
# -889 -202 3 6
# -169 598 1 96
# 855 328 3 48
# -381 -217 2 1
# -461 336 2 52
# -927 809 3 16
# -351 -175 0 62
# 50 194 0 54
# 841 -480 2 25
# -820 -921 1 73
# -914 892 0 45
# 20 -943 2 50
# 823 271 1 59
# -587 578 0 67
# 22 -444 2 40
# 821 -789 1 38
# 531 28 0 5
# -633 741 0 80
# -156 -519 1 10
# -885 -632 3 14
# -647 730 3 79
# 804 -9 0 16
# -422 -68 1 90
# -459 590 0 9
# -152 274 3 67
# -750 203 3 49
# -278 -8 2 90
# 293 -2 2 63
# -148 990 2 12
# -656 679 3 35
# -154 41 3 22
# -529 498 0 1
# 69 357 1 58
# -324 -393 1 24
# -65 468 0 66
# -323 0 1 84
# -340 975 1 26
# -618 45 1 76
# -272 -618 2 18
# -395 127 2 89
# -410 28 1 29
# 988 120 2 33
# 817 851 2 12
# 138 -50 3 13
# 226 -743 1 53
# 502 -985 3 7
# 238 595 2 20
# 188 443 1 65
# -75 -567 0 30
# 265 -70 2 84
# 314 480 1 41
# -460 -297 1 34
# -873 -188 0 89
# 35 -205 0 12
# -994 -281 1 6
# 450 -819 1 73
# -296 869 1 4
# 86 1000 2 5
# 995 96 0 29
# 236 634 1 79
# 50 7 1 66
# -952 -644 1 91
# 785 691 1 51
# 617 -645 2 37
# 675 780 0 34
# -986 -433 1 100
# -960 -163 3 85
# 821 -862 2 32
# -701 361 0 13
# 360 -803 0 29
# -61 -900 1 63
# 408 -501 1 29
# 952 759 2 30
# -139 -358 3 62
# -747 -260 2 15
# 634 -610 1 89
# -948 -462 2 56
# 773 -910 3 52
# -547 -318 2 82
# 781 674 1 41
# 518 -957 2 71
# -572 5 1 61
# -700 -12 2 92
# 507 -916 0 98
# 348 -892 2 57
# 332 -171 2 9
# -569 -181 3 80
# -312 -542 3 41
# -278 280 0 33
# 8 -536 2 18
# -535 -87 2 57
# 13 -811 2 55
# 845 283 0 74
# -419 -768 3 29
# 839 -957 0 97
# 325 209 2 85
# 783 -751 0 56
# 638 350 2 6
# -848 -252 2 45
# -533 -552 0 73
# -184 -826 1 1
# -449 142 0 23
# -739 -463 1 1
# 126 306 2 42
# 780 -107 3 85
# -156 -735 2 40
# 627 373 3 27
# -75 -626 0 42
# -845 -706 0 25
# -484 -827 1 50
# -597 129 3 96
# 520 -600 3 94
# 917 -706 0 22
# 899 -663 1 23
# 280 565 3 5
# -62 258 1 39
# 372 52 1 37
# -761 465 0 88
# 333 294 1 50
# 427 918 2 79
# -739 -814 0 8
# -940 -34 3 73
# -638 -749 1 14
# 796 -338 3 25
# 844 -498 1 59
# -266 -73 3 60
# 991 -340 3 32
# 260 557 2 11
# 247 701 1 47
# 589 825 1 21
# 997 7 2 86
# 35 -579 3 38
# 311 -147 2 78
# -251 -752 1 5
# -73 502 2 72
# -825 543 3 88
# 430 -882 1 12
# -272 111 2 83
# 670 -946 0 20
# -321 647 0 68
# 389 710 3 14
# -474 -365 3 49
# -435 991 1 4
# 320 619 2 24
# -275 868 0 1
# 717 298 2 86
