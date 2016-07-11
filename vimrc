" configure expanding of tabs for various file types
au BufRead,BufNewFile *.py set expandtab
au BufRead,BufNewFile *.c set noexpandtab
au BufRead,BufNewFile *.h set noexpandtab
au BufRead,BufNewFile Makefile* set noexpandtab

" ---------------------------------------------
" configure editor with tabs and other stuff...
" ---------------------------------------------
set expandtab
set textwidth=80
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set cindent
set number
set hlsearch
set ruler
syntax on
set showcmd
