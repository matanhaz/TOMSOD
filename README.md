# How to run:


1. install requirements
2. run inside venv `pipreqs --mode no-pin --ignore diagnoser,sfl_diagnoser .`
3. `python Run.py <project name>` - keys in the file project_info.txt
4. extract matrix from `matrixes` folder into the same folder
5. run `python extract_matrixes.py <project name>`
6. create dir called barinel inside projects/<repo name>
7. inside barinel create 2 dirs: matrixes and matrixes_before_change
8. copy stage 4 output to matrixes_before_change
9. run: `python sfl_diagnoser/main.py <repo name> git old <method - Sanity1/Sanity2/Sanity3/topic>`
10. python experiments.py <repo name> for experiments
