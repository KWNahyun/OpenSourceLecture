#!/bin/bash

# 입력된 이름으로 폴더가 있는지 확인하고, 없는 경우 폴더를 생성합니다.
read -p "폴더 이름을 입력하세요: " folder_name

if [ -d "$folder_name" ]; then
    echo "폴더가 이미 존재합니다."
else
    mkdir "$folder_name"
    echo "폴더를 생성했습니다."
fi

# 5개의 파일을 생성합니다.
for i in {1..5}
do
    touch "$folder_name/file$i.txt"
    echo "이것은 파일 $i 입니다." > "$folder_name/file$i.txt"
done

# 생성된 파일들을 압축합니다.
tar -czvf "$folder_name.tar.gz" "$folder_name"

# 새로운 폴더를 생성하여 압축을 해제합니다.
mkdir extracted_folder
tar -xzvf "$folder_name.tar.gz" -C extracted_folder

echo "압축 해제가 완료되었습니다."