#!/bin/bash

git init

for day in $(seq 1 365)
do
    date=$(date -d "2025-01-01 +$((day-1)) days" +%Y-%m-%d)

    echo "$date" >> contributions.txt

    git add contributions.txt

    GIT_AUTHOR_DATE="$date 12:00:00" \
    GIT_COMMITTER_DATE="$date 12:00:00" \
    git commit -m "Contribution $date"
done