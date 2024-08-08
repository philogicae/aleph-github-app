apt update -y
apt upgrade -y
apt install -y git zsh python3-pip

# Change terminal
chsh -s $(which zsh)
zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
Set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc
exec zsh

# Plugins ZSH
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
Set in ~/.zshrc:
plugins=( git zsh-syntax-highlighting zsh-autosuggestions )
source ~/.zshrc

# Exa better than ls
apt install exa -y
Set in ~/.zshrc :
if [ -x "$(command -v exa)" ]; then
    alias ls="exa"
    alias la="exa --long --all --group"
fi
source ~/.zshrc

# Tmux
apt install tmux -y
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
tmux
nano  ~/.tmux.conf
Copy config to ~/.tmux.conf
tmux source ~/.tmux.conf
cd ~/.tmux/plugins/tpm/scripts && ./install_plugins.sh

# Ranger
pip install ranger-fm