#!/bin/sh
${PYTHON} -m pip install . -vv

# copy the [de]activate scripts to $PREFIX/etc/conda/[de]activate.d
# This will allow them to be run on environment activation.
# See https://conda-forge.org/docs/maintainer/adding_pkgs.html#activate-scripts
for SUFFIX in "sh" "fish"; do
  for CHANGE in "activate" "deactivate"; do
    mkdir -p "${PREFIX}/etc/conda/${CHANGE}.d"
    cp "${RECIPE_DIR}/${CHANGE}.${SUFFIX}" "${PREFIX}/etc/conda/${CHANGE}.d/${PKG_NAME}_${CHANGE}.${SUFFIX}"
  done
done