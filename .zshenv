# go environment variables
export GOROOT="/usr/local/Cellar/go/1.15.2"
export GOPATH="$HOME/Projects"
export GOPATH="$HOME/Library/golib:$GOPATH"

# paths
export PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"
export PATH="$HOME/Library/golib/bin:$PATH"
export PATH="$HOME/Projects/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# clean home
export ZDOTDIR="$HOME/.config/zsh"
export fpath=( "$HOME/.config/zsh/.zfunctions" $fpath )
export PYLINTHOME="$HOME/.local/share/pylint.d"
export NPM_CONFIG_USERCONFIG="$HOME/.config/npm/npmrc"
