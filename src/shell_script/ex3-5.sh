#!/bin/bash

# 내부 함수를 정의하여 리눅스 명령어를 실행하고 입력된 인자를 전달합니다.
execute_ls() {
    ls "$@"
}

# 내부 함수를 호출하여 ls 명령어 실행
execute_ls -l
