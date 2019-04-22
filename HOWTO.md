# Push your code
- directly to master branch to directory `sessions/<session>/<firstname_lastname>/`
- use input files (if any) from session dir `open('../input.txt', 'r')`

# use own requirements.txt
- setup your `sessions/<session>/<firstname_lastname>/requirements.txt`
- in root directory create new file `/requirements.txt` with content 
  `-r sessions/<session>/<firstname_lastname>/requirements.txt`
- root's `/requirements.txt` is in .gitignore, so every student has his/her own version of requirements.txt managed by PyCharm