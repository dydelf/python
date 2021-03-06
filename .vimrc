syntax enable " enable syntax processing
" python import sys; sys.path.append("/usr/local/lib/python2.7/site-packages/")

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
" Plugin 'powerline/powerline'
" Plugin 'klen/python-mode'
Plugin 'scrooloose/syntastic'
Plugin 'bling/vim-airline'
Plugin 'tpope/vim-fugitive'

call vundle#end()            " required
filetype plugin indent on  " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line


syntax on
autocmd! bufwritepost .vimrc source % " automatic vimrc file reload
set guicursor+=n-v-c:blinkon0
set cursorline " highlight current line
set cursorcolumn " highlight current column
" set guicursor=a:ver25-blinkon10 

colorscheme solarized
set encoding=utf-8
" set t_Co=16
set background=dark
" let g:solarized_termcolors=256
let g:solarized_termtrans=1
" set autoindent " , disabling helped with enter key
set smartindent
set shiftwidth=4 " setting something for enter key and tabs
set shiftround " setting something with spaces inside a file
set clipboard=unnamed " setting domething for anter and key tabs
set wrap " wrap text that extends beyond the screen
set tabstop=4 " number of visual spaces per TAB
set softtabstop=4 " number of spaces per tab when editing
set expandtab " tabs are spaces
set number " show line numbers
set tw=79 " wraping text beyond 79 character
set colorcolumn=80 " highlighting column 80
" highlight ColorColumn ctermbg=233
set history=700 " history of undos
set undolevels=700 " undo levels
set showcmd " show command in a bottom bar
set noshowmode " display options
set wildmenu " visual autocomplete for command menu
set lazyredraw " redraw only when you need to
set showmatch " highlight matching {}{}[]
set incsearch " search as characters are entered
set hlsearch " highlight matches
set scrolloff=5 " display five lines above below when scrolling with a mouse
set backspace=indent,eol,start " fixes common backspace problems
set ttyfast " speed up scrolling in vim
set laststatus=2 " status bar
set ignorecase " search uppercase as lowercase
set smartcase " include only uppercase words with uppercase letter
set pastetoggle=<F2> " pasting with F2 key
set bs=2 " normal backspace use
set mouse=a " mouse on
set ttymouse=xterm2 " support mouse codes
set nobackup " backup and swap turned off
set nowritebackup
set noswapfile

filetype indent on " load file type specific indent files
" filetype off " recognizing syntax on in files????
" let mapleader = "Space" " <leader> is now , key
map <Space> <Leader>
" move vertically by visual line
nnoremap j gj
nnoremap k gk
" ctrl+hjkl is now used to move through windows
" map <A-j> <C-w>j 
" map <A-k> <C-w>k
" map <A-l> <C-w>l
" map <A-h> <C-w>h
" leader + number is now used to move through tabs
nnoremap <leader>1 1gt
nnoremap <leader>2 2gt
nnoremap <leader>3 3gt
nnoremap <leader>4 4gt
nnoremap <leader>5 5gt
nnoremap <leader>6 6gt
nnoremap <leader>7 7gt
nnoremap <leader>8 8gt
nnoremap <leader>9 9gt
nnoremap <leader>0 :tablast<cr>

" faster vertical movement
" normal mode:
nnoremap <c-j> 5j
nnoremap <c-k> 5k
" visual mode:
xnoremap <c-j> 5j
xnoremap <c-k> 5k

" highlight last inserted text
nnoremap gV '[v']
" trying to set runn command with a shortcut key
" imap <F5> <Esc>:w<CR>:!cls;py %<CR>
nnoremap <F5> :GundoToggle<CR>
nnoremap <buffer> <F9> :exec '!python3' shellescape(@%, 1)<cr>

if has('python3')
    let g:gundo_prefer_python3 = 1
endif

" pathogen configuration
execute pathogen#infect()
call pathogen#helptags()
runtime bundle/vim-pathogen/autoload/pathogen.vim
" call pathogen#runtime_append_all_bundles() " use pathogen
set sessionoptions-=options

" YCM configuration
" let g:ycm_python_binary_path = 'usr/bin/python3'

" synthastic configuration
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
"let g:syntastic_always_populate_loc_list = 1
"let g:syntastic_auto_loc_list = 1
"let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers=['pylint']
let g:syntastic_python_pylint_exec = 'pylint'
let g:syntastic_python_python_exec = 'python3'


" powerline configuration
" set guifont=Source\ Code\ Pro\ for\ Powerline\ for\ Powerline
" source ~/.vim/bundle/powerline/powerline/ext/vim/source_plugin.vim
" set rtp+=/usr/local/lib/python3.7/site-packages/powerline/bindings/vim/
set t_Co=256
" python import sys; sys.path.append("/Library/Python/2.7/site-packages")
" python from powerline.ext.vim import source_plugin; source_plugin()
"set guifont=Source\ Code\ Pro\ for\ Powerline:h15
"let g:Powerline_symbols = 'fancy'
set encoding=utf-8
"set term=xterm-256color
"set termencoding=utf-8
"set fillchars+=stl:\ ,stlnc:\



" python mode configuration
"map <leader>g :call RopeGoToDefinition()<CR>
"let g:pymode_python = 'python3'
"let ropevim_enable_shortcuts = 1
"let g:pymode_rope_goto_def_newwin = "new"
"let g:pymode_rope_extended_complete = 1
"let g:pymode_breakpoint =0
"let g:pymode_syntax = 1
"let g:pymode_virtualenv = 1

" nerdtree configuration
nmap <leader>t :NERDTree<CR>
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
