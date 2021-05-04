#!/usr/bin/env bash

export ELF_DEVELOPMENT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/.. && pwd )"
echo $ELF_DEVELOPMENT_ROOT
export PYTHONPATH="${ELF_DEVELOPMENT_ROOT}"/src_py/:"${ELF_DEVELOPMENT_ROOT}"/build/elf/:"${ELF_DEVELOPMENT_ROOT}"/build/elfgames/go/:${PYTHONPATH}
echo $PYTHONPATH