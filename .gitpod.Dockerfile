FROM gitpod/workspace-full


# Install apt packages and clean up cached files
RUN pyenv install 3.10 \
    && pyenv global 3.10
