#! /bin/bash

if [ -f "${1:-""}" ];then
  arg_file=$1
  file_ext="$(awk -F= '/ext=/ {print $2}' ${arg_file})"
fi

if [ -z "${file_ext}" ];then
  file_ext="py"
fi

file_count="$(find . -type f -name \*.$file_ext | wc -l  | grep [0-9]*)"

echo "{\"FileCount\" : ${file_count}, \"FileExt\" : \"${file_ext}\"}"
