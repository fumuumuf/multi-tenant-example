FROM centos:centos7
ARG PY_VERSION="3.8.5"

# postgreSQL version
ENV PG_VERSION=11

RUN yum update -y \
    && yum install -y https://repo.ius.io/ius-release-el7.rpm \
    && yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm \
    && yum -y groupinstall 'Development tools' \ 
    && yum install -y centos-release-scl llvm-toolset-7 llvm5.0

RUN yum install -y \
        gcc \
        make \
        git \
        openssl-devel \
        libffi-devel \
        which \ 
        zlib-devel \
        readline-devel \
        bzip2-devel \
        libffi-devel \
        postgresql${PG_VERSION}-libs \
        postgresql${PG_VERSION}-devel \
    && rm -rf /var/cache/yum/* && yum clean all

# add postgre path
ENV PATH /usr/pgsql-${PG_VERSION}/bin:${PATH}

WORKDIR /var/www/django

COPY ./apps/requirements.txt requirements.txt

# make local venv environment
ENV HOME=/root
ENV PYENV_ROOT ${HOME}/.pyenv
ENV PATH ${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}

# PY_VERSION で指定されたバージョンの python をインストール
RUN cd ${HOME} && git clone git://github.com/yyuu/pyenv.git .pyenv \
  && pyenv install ${PY_VERSION} &&  pyenv rehash && pyenv global ${PY_VERSION}

# install python packages
RUN pip --no-cache-dir install -U pip \
  && pip --no-cache-dir install -r requirements.txt
