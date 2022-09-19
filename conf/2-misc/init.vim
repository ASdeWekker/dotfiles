lua require('plugins')

let $NVIM_TUI_ENABLE_CURSOR_SHAPE=1
filetype plugin indent on
let base16colorspace=256
syntax enable
" colorscheme base16-gooey

map <C-n> :NERDTreeToggle<CR>

set background=dark
set backspace=indent,eol,start
set clipboard+=unnamedplus
set cursorline
set encoding=utf-8
set expandtab
set fileencoding=utf-8
set fileformats=unix
set fileformats=unix,dos
set hidden
set lazyredraw
set noswapfile
set number
set scrolloff=3
set shiftwidth=4
set smartcase
set tabstop=4
set title
set ttimeoutlen=0
set undofile
set undodir=~/.config/nvim/temp/undodir 
set wildmenu

