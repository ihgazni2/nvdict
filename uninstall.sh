pip3 uninstall nvdict
git rm -r dist
git rm -r build
git rm -r nvdict.egg-info
rm -r dist
rm -r build
rm -r nvdict.egg-info
git add .
git commit -m "remove old build"

