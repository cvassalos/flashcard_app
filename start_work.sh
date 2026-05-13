#!/bin/bash

SESSION="flashcard"

tmux new-session -d -s "$SESSION" -n "lazygit" "lazygit"
tmux new-window -t "$SESSION:1" -n "php_server" "php -S localhost:8000"
tmux new-window -t "$SESSION:2" -n "index.php" "nvim index.php"
tmux new-window -t "$SESSION:3" -n "stack.php" "nvim stack.php"

tmux attach-session -t "$SESSION"
