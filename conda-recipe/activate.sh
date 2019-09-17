IPYTHONDIR=${IPYTHONDIR:-$HOME/.ipython}
echo "import richprompt.load; richprompt.load(); del richprompt.load" > ${IPYTHONDIR}/profile_default/startup/000-richprompt.py
