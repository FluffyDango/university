#!/usr/bin/env bash
set -euo pipefail

USER_HOME="$HOME"
ZSH_CUSTOM="${ZSH_CUSTOM:-$USER_HOME/.oh-my-zsh/custom}"
OH_MY_ZSH_DIR="$USER_HOME/.oh-my-zsh"
ZSHRC="$USER_HOME/.zshrc"

sudo apt update

change_to_zsh() {
    if ! command -v zsh >/dev/null; then
        echo "Installing zsh..."
        sudo apt install -y zsh
    else
        echo "zsh already installed."
    fi
    if [ ! -d "$OH_MY_ZSH_DIR" ]; then
        echo "Cloning Oh My Zsh..."
        git clone https://github.com/ohmyzsh/ohmyzsh.git "$OH_MY_ZSH_DIR"
    else
        echo "Oh My Zsh already present."
    fi
    if [ ! -d "$ZSH_CUSTOM/themes/powerlevel10k" ]; then
        echo "Installing Powerlevel10k theme..."
        git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
            "$ZSH_CUSTOM/themes/powerlevel10k"
    else
        echo "Powerlevel10k already present."
    fi

    declare -A plugins=(
        [zsh-autosuggestions]=https://github.com/zsh-users/zsh-autosuggestions.git
        [zsh-syntax-highlighting]=https://github.com/zsh-users/zsh-syntax-highlighting.git
        [fast-syntax-highlighting]=https://github.com/zdharma-continuum/fast-syntax-highlighting.git
    )

    for plugin in "${!plugins[@]}"; do
        target="$ZSH_CUSTOM/plugins/$plugin"
        if [ ! -d "$target" ]; then
            echo "Installing $plugin..."
            git clone "${plugins[$plugin]}" "$target"
        else
            echo "$plugin already present."
        fi
    done

}

add_shell_setup() {
    if [ -f "$ZSHRC" ]; then
        echo "Backing up existing .zshrc to .zshrc.pre-oh-my-zsh"
        cp "$ZSHRC" "${ZSHRC}.pre-oh-my-zsh"
    fi

    cat > "$ZSHRC" << 'EOF'
export PAGER=less
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(zsh-autosuggestions zsh-syntax-highlighting fast-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

alias ..='cd ..'
alias ll='ls -lA'
alias relfaucet='docker exec main_faucet_1 pkill -HUP -f faucet.faucet'
EOF
    echo "Wrote new $ZSHRC"

    if [ "$SHELL" != "$(command -v zsh)" ]; then
        echo "Changing default shell to zsh..."
        chsh -s "$(command -v zsh)"
        echo "Default shell updated. You may need to log out and back in."
    else
        echo "Default shell is already zsh."
    fi
}

setup_docker() {
    sudo apt install docker-compose -y
    sudo usermod -aG docker $USER
    newgrp docker
}

change_to_zsh
add_shell_setup
setup_docker
