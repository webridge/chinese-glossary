#!/bin/bash

# Copyright (C) alick<alick9188@gmail.com>
# License: GPLv3+

# This script can check whether the items in the glossary file is in order.
# It bring you the diff between the original file and the sorted one.
# 脚本用来检查词条是否按顺序排列。
# 它会显示出原始文件中词条和排序后词条的 diff 结果。

# 事先过滤掉了非英文字母打头的行。
# 排序依据：按第一个逗号(,)前的词/词组排序，忽略大小写，
#           稳定排序（相等条目次序不变）

tmpfile="tmp"
CDIFF=""

# check whether color diff is available
type cdiff > /dev/null 2>&1
[ $? -eq 0 ] && CDIFF="cdiff" || CDIFF="less"

LC_ALL=C grep '^[[:alpha:]]' glossary.csv > "$tmpfile"
LC_ALL=C sort -f -t , -k 1,1 -s tmp | diff -u "$tmpfile" - | $CDIFF
rm "$tmpfile"
